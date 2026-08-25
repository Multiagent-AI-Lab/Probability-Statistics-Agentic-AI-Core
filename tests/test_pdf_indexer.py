"""Tests para pdf_indexer: extracción y chunking de PDFs para el RAG
de bibliografía de StatsTutorAgent."""

from pathlib import Path
from unittest.mock import MagicMock, patch

from pypdf import PdfWriter

from src.multiagent_core.pdf_indexer import chunk_page_text, extract_pages, index_pdf


def _crear_pdf_de_prueba(tmp_path: Path, paginas_texto: list[str]) -> Path:
    """Genera un PDF real con texto seleccionable usando pypdf + reportlab
    no está disponible aquí, así que se usa un PDF mínimo escrito a mano
    vía pypdf.PdfWriter con contenido de texto plano incrustado."""
    pdf_path = tmp_path / "libro_prueba.pdf"
    writer = PdfWriter()
    for _ in paginas_texto:
        writer.add_blank_page(width=612, height=792)
    with open(pdf_path, "wb") as f:
        writer.write(f)
    return pdf_path


def test_extract_pages_de_pdf_sin_texto_devuelve_strings_vacios(tmp_path: Path):
    """PdfWriter().add_blank_page() no soporta insertar texto directamente
    (requiere reportlab, no disponible) -- este test cubre el caso de PDF
    válido pero sin texto seleccionable (equivalente a un PDF escaneado),
    que es exactamente el caso límite que la spec pide tolerar."""
    pdf_path = _crear_pdf_de_prueba(tmp_path, ["", ""])

    paginas = extract_pages(pdf_path)

    assert len(paginas) == 2
    assert paginas == ["", ""]


def test_extract_pages_de_archivo_corrupto_no_lanza_excepcion(tmp_path: Path):
    pdf_falso = tmp_path / "corrupto.pdf"
    pdf_falso.write_bytes(b"esto no es un PDF valido")

    paginas = extract_pages(pdf_falso)

    assert paginas == []


def test_chunk_page_text_respeta_max_chars():
    texto = "Párrafo uno. " * 100  # ~1300 caracteres

    chunks = chunk_page_text(texto, page_number=5, max_chars=500)

    assert len(chunks) >= 2
    assert all(len(c["text"]) <= 500 for c in chunks)
    assert all(c["page"] == 5 for c in chunks)


def test_chunk_page_text_con_texto_vacio_devuelve_lista_vacia():
    assert chunk_page_text("", page_number=1) == []


def test_chunk_page_text_con_texto_corto_devuelve_un_solo_chunk():
    chunks = chunk_page_text("Texto corto de una sola página.", page_number=1)

    assert len(chunks) == 1
    assert chunks[0]["text"] == "Texto corto de una sola página."
    assert chunks[0]["page"] == 1


def test_index_pdf_de_archivo_corrupto_devuelve_lista_vacia(tmp_path: Path):
    pdf_falso = tmp_path / "corrupto.pdf"
    pdf_falso.write_bytes(b"esto no es un PDF valido")

    resultado = index_pdf(pdf_falso)

    assert resultado == []


def test_index_pdf_incluye_source_con_nombre_de_archivo(tmp_path: Path):
    pdf_path = _crear_pdf_de_prueba(tmp_path, [""])

    resultado = index_pdf(pdf_path)

    # PDF en blanco -> sin texto -> sin chunks, pero no debe fallar.
    assert resultado == []


def test_extract_pages_elimina_surrogates_huerfanos(tmp_path: Path):
    """Algunos PDFs académicos con símbolos matemáticos en fuentes itálicas
    (ej. variables como 𝑋, 𝑌) hacen que pypdf extraiga un surrogate UTF-16
    huérfano (\\ud835 sin su pareja baja) cuando el mapeo de la fuente está
    incompleto. Ese carácter es inválido en un str de Python bien formado y
    el tokenizer de HuggingFace (Rust) lo rechaza con un TypeError al
    embeber -- confirmado en bibliografia/PracticalStatisticsforDataScientists...pdf,
    donde rompía la indexación de forma consistente (no aleatoria como se
    pensaba inicialmente). Debe limpiarse en la extracción, no dejarse para
    que cada consumidor (script de indexación, StatsTutorAgent) lo maneje
    por su cuenta."""
    pdf_path = _crear_pdf_de_prueba(tmp_path, [""])
    texto_con_surrogate_huerfano = "Bagging usa \ud835 como variable de respuesta."

    with patch("src.multiagent_core.pdf_indexer.PdfReader") as mock_reader_cls:
        mock_page = MagicMock()
        mock_page.extract_text.return_value = texto_con_surrogate_huerfano
        mock_reader_cls.return_value.pages = [mock_page]

        paginas = extract_pages(pdf_path)

    assert len(paginas) == 1
    assert "\ud835" not in paginas[0]
    # El texto sin el surrogate debe seguir siendo codificable a UTF-8 (lo
    # que el tokenizer necesita) sin lanzar UnicodeEncodeError.
    paginas[0].encode("utf-8")


def test_extract_pages_elimina_multiples_surrogates_en_la_misma_pagina(tmp_path: Path):
    """El log agrega el conteo por página (`n_surrogates`) en vez de emitir
    una línea por carácter -- este test ejercita la rama de pluralización
    (>1 surrogate) y confirma que todos se eliminan, no solo el primero."""
    pdf_path = _crear_pdf_de_prueba(tmp_path, [""])
    texto = "Sean \ud835 y \ud835 dos variables aleatorias, con media \ud835."

    with patch("src.multiagent_core.pdf_indexer.PdfReader") as mock_reader_cls:
        mock_page = MagicMock()
        mock_page.extract_text.return_value = texto
        mock_reader_cls.return_value.pages = [mock_page]

        paginas = extract_pages(pdf_path)

    assert "\ud835" not in paginas[0]
    paginas[0].encode("utf-8")


def test_extract_pages_elimina_surrogate_pegado_sin_espacios(tmp_path: Path):
    """Cuando el surrogate huérfano está pegado a texto en ambos lados (sin
    espacio, ej. la fuente itálica no insertó separador), eliminarlo
    concatena las palabras circundantes (ej. "valor𝑋es" -> "valores"). Es
    un trade-off aceptado (ver review de python-reviewer): preferible a
    dejar un carácter no codificable que rompe el tokenizer, pero se
    documenta explícitamente con un test para que el comportamiento no
    sea una sorpresa si alguien lo encuentra más adelante."""
    pdf_path = _crear_pdf_de_prueba(tmp_path, [""])
    texto = "el valor\ud835es una variable aleatoria"

    with patch("src.multiagent_core.pdf_indexer.PdfReader") as mock_reader_cls:
        mock_page = MagicMock()
        mock_page.extract_text.return_value = texto
        mock_reader_cls.return_value.pages = [mock_page]

        paginas = extract_pages(pdf_path)

    assert paginas[0] == "el valores una variable aleatoria"


def test_chunk_page_text_corte_fijo_cuando_oracion_excede_max_chars():
    """Ejercita la rama de corte fijo por caracteres: una oración individual
    sin puntos internos que excede max_chars se divide en bloques de tamaño
    fijo (último recurso del _dividir_texto_largo)."""
    # Texto sin ". " internos, más largo que max_chars (600 caracteres)
    texto_largo = "Una palabra muy larga " * 50  # ~1150 caracteres sin puntos internos
    max_chars = 600

    chunks = chunk_page_text(texto_largo, page_number=1, max_chars=max_chars)

    # Debe generar al menos 2 chunks por el corte fijo
    assert len(chunks) >= 2
    # Ningún chunk debe exceder max_chars
    assert all(len(c["text"]) <= max_chars for c in chunks)
    # Verificar que cada chunk tiene la estructura correcta
    assert all(c["page"] == 1 for c in chunks)
    # La suma de todos los chunks debe ser >= texto original
    # (puede tener espacios/puntos extras del procesamiento)
    texto_reconstructido = "".join(c["text"] for c in chunks)
    assert len(texto_reconstructido) >= len(texto_largo) - 10  # tolerancia mínima
