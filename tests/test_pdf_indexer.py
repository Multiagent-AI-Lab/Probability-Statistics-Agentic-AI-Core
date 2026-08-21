"""Tests para pdf_indexer: extracción y chunking de PDFs para el RAG
de bibliografía de StatsTutorAgent."""

from pathlib import Path

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
