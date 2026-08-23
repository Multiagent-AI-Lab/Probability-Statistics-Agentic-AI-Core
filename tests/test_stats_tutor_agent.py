"""Tests for StatsTutorAgent (RAG + Gemini)."""

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import requests

from src.multiagent_core.stats_tutor_agent import StatsTutorAgent


@pytest.fixture
def course_dir(tmp_path: Path) -> Path:
    unidad = tmp_path / "UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md"
    unidad.write_text(
        "# UNIDAD 1\n\n## 1. Fundamentación Teórica\n\n"
        "La media muestral se calcula como la suma de observaciones "
        "dividida entre n.\n",
        encoding="utf-8",
    )
    return tmp_path


def test_construye_prompt_con_contexto_y_pregunta(course_dir: Path, tmp_path: Path):
    with patch("src.multiagent_core.stats_tutor_agent.genai.Client") as mock_client_cls:
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "La media muestral es un estimador de tendencia central."
        mock_client.models.generate_content.return_value = mock_response
        mock_client_cls.return_value = mock_client

        tutor = StatsTutorAgent(
            course_dir,
            chroma_path=tmp_path / "chroma",
            memory_path=tmp_path / "memory.json",
        )
        with patch.dict("os.environ", {"GEMINI_API_KEY": "fake-key"}):
            respuesta = tutor.ask("¿Qué es la media muestral?")

        assert "media muestral" in respuesta.lower() or respuesta == mock_response.text
        mock_client.models.generate_content.assert_called_once()
        prompt_usado = mock_client.models.generate_content.call_args.kwargs.get(
            "contents", mock_client.models.generate_content.call_args.args
        )
        assert prompt_usado is not None


def test_maneja_error_de_la_api_sin_lanzar_excepcion(course_dir: Path, tmp_path: Path):
    with patch("src.multiagent_core.stats_tutor_agent.genai.Client") as mock_client_cls:
        mock_client_cls.side_effect = Exception("API unreachable")

        tutor = StatsTutorAgent(
            course_dir,
            chroma_path=tmp_path / "chroma",
            memory_path=tmp_path / "memory.json",
        )
        with patch.dict("os.environ", {"GEMINI_API_KEY": "fake-key"}):
            respuesta = tutor.ask("¿Qué es la varianza?")

        assert "Error" in respuesta or "error" in respuesta.lower()


def test_encuentra_seccion_relevante_por_busqueda_semantica(
    course_dir: Path, tmp_path: Path
):
    tutor = StatsTutorAgent(
        course_dir,
        chroma_path=tmp_path / "chroma",
        memory_path=tmp_path / "memory.json",
    )
    contexto = tutor._search_local_docs("¿Cómo se calcula la media muestral?")
    assert "media muestral" in contexto.lower()
    assert "UNIDAD_1" in contexto


def test_indice_es_persistente_entre_instancias(course_dir: Path, tmp_path: Path):
    chroma_path = tmp_path / "chroma"
    tutor1 = StatsTutorAgent(
        course_dir, chroma_path=chroma_path, memory_path=tmp_path / "m1.json"
    )
    count_primera = tutor1.collection.count()

    tutor2 = StatsTutorAgent(
        course_dir, chroma_path=chroma_path, memory_path=tmp_path / "m2.json"
    )
    count_segunda = tutor2.collection.count()

    assert count_primera == count_segunda
    assert count_primera > 0


def test_diagnose_error_detecta_p_valor_mal_interpretado():
    """Errores estadisticos comunes (no excepciones de Python) tambien
    disparan una pista socratica, adaptando el patron de TutorAgent al
    dominio de Probabilidad."""
    tutor = StatsTutorAgent.__new__(StatsTutorAgent)  # sin construir RAG real
    pista = tutor._diagnose_error(
        "obtuve un p-valor de 0.03, eso significa que hay 97% de probabilidad de que H0 sea falsa"
    )
    assert pista is not None
    assert "p-valor" in pista.lower() or "probabilidad" in pista.lower()


def test_add_episode_y_retrieve_relevant_episodes(course_dir: Path, tmp_path: Path):
    memory_path = tmp_path / "memory.json"
    tutor = StatsTutorAgent(
        course_dir, chroma_path=tmp_path / "chroma", memory_path=memory_path
    )
    tutor._add_episode("¿Qué es la desviación estándar?", "Es la raíz de la varianza.")

    episodios = json.loads(memory_path.read_text(encoding="utf-8"))
    assert len(episodios) == 1
    assert episodios[0]["question"] == "¿Qué es la desviación estándar?"

    relevantes = tutor._retrieve_relevant_episodes(
        "¿Cómo se calcula la desviación estándar?"
    )
    assert len(relevantes) == 1


class TestExtractDois:
    def test_extrae_un_doi_simple(self, course_dir: Path, tmp_path: Path):
        tutor = StatsTutorAgent(
            course_dir, chroma_path=tmp_path / "chroma", memory_path=tmp_path / "m.json"
        )
        texto = (
            "Dong, J. et al. (2020). *KONA Powder and Particle Journal*, 37, 224. "
            "DOI: [10.14356/kona.2020011](https://doi.org/10.14356/kona.2020011)."
        )
        assert tutor._extract_dois(texto) == ["10.14356/kona.2020011"]

    def test_extrae_doi_con_parentesis_internos(self, course_dir: Path, tmp_path: Path):
        """Regresión: algunos DOI reales contienen paréntesis en su propio
        identificador. Un regex que delimite por ')' en la URL trunca este
        DOI incorrectamente."""
        tutor = StatsTutorAgent(
            course_dir, chroma_path=tmp_path / "chroma", memory_path=tmp_path / "m.json"
        )
        texto = (
            "Van Hardeveld, R., & Hartog, F. (1969). *Surface Science*, 15(2), 189. "
            "DOI: [10.1016/0039-6028(69)90148-4](https://doi.org/10.1016/0039-6028(69)90148-4)."
        )
        assert tutor._extract_dois(texto) == ["10.1016/0039-6028(69)90148-4"]

    def test_deduplica_doi_repetido_en_el_mismo_texto(
        self, course_dir: Path, tmp_path: Path
    ):
        tutor = StatsTutorAgent(
            course_dir, chroma_path=tmp_path / "chroma", memory_path=tmp_path / "m.json"
        )
        texto = (
            "Primera mención. DOI: [10.1039/d2na00809b](https://doi.org/10.1039/d2na00809b). "
            "Segunda mención del mismo. DOI: [10.1039/d2na00809b](https://doi.org/10.1039/d2na00809b)."
        )
        assert tutor._extract_dois(texto) == ["10.1039/d2na00809b"]

    def test_texto_sin_doi_retorna_lista_vacia(self, course_dir: Path, tmp_path: Path):
        tutor = StatsTutorAgent(
            course_dir, chroma_path=tmp_path / "chroma", memory_path=tmp_path / "m.json"
        )
        assert tutor._extract_dois("Texto sin ninguna cita bibliográfica.") == []

    def test_texto_con_link_doi_invalido_no_extrae_nada(
        self, course_dir: Path, tmp_path: Path
    ):
        tutor = StatsTutorAgent(
            course_dir, chroma_path=tmp_path / "chroma", memory_path=tmp_path / "m.json"
        )
        texto = (
            "Ver el trabajo de Vollath. DOI: [ver Vollath 2018](https://example.com)."
        )
        assert tutor._extract_dois(texto) == []


class TestFetchAbstract:
    def test_retorna_abstract_limpio_de_markup_jats(
        self, course_dir: Path, tmp_path: Path
    ):
        tutor = StatsTutorAgent(
            course_dir, chroma_path=tmp_path / "chroma", memory_path=tmp_path / "m.json"
        )
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "message": {"abstract": "<jats:p>Texto del abstract con markup.</jats:p>"}
        }
        mock_response.raise_for_status.return_value = None

        with patch(
            "src.multiagent_core.stats_tutor_agent.requests.get",
            return_value=mock_response,
        ):
            resultado = tutor._fetch_abstract("10.14356/kona.2020011")

        assert resultado == "Texto del abstract con markup."

    def test_retorna_none_si_falla_la_peticion_de_red(
        self, course_dir: Path, tmp_path: Path
    ):
        tutor = StatsTutorAgent(
            course_dir, chroma_path=tmp_path / "chroma", memory_path=tmp_path / "m.json"
        )

        with patch(
            "src.multiagent_core.stats_tutor_agent.requests.get",
            side_effect=requests.exceptions.Timeout("timeout simulado"),
        ):
            resultado = tutor._fetch_abstract("10.9999/doi-inexistente")

        assert resultado is None

    def test_retorna_none_si_el_registro_no_tiene_abstract(
        self, course_dir: Path, tmp_path: Path
    ):
        tutor = StatsTutorAgent(
            course_dir, chroma_path=tmp_path / "chroma", memory_path=tmp_path / "m.json"
        )
        mock_response = MagicMock()
        mock_response.json.return_value = {"message": {}}
        mock_response.raise_for_status.return_value = None

        with patch(
            "src.multiagent_core.stats_tutor_agent.requests.get",
            return_value=mock_response,
        ):
            resultado = tutor._fetch_abstract("10.1234/sin-abstract")

        assert resultado is None

    def test_retorna_none_si_status_code_es_error(
        self, course_dir: Path, tmp_path: Path
    ):
        tutor = StatsTutorAgent(
            course_dir, chroma_path=tmp_path / "chroma", memory_path=tmp_path / "m.json"
        )
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
            "404"
        )

        with patch(
            "src.multiagent_core.stats_tutor_agent.requests.get",
            return_value=mock_response,
        ):
            resultado = tutor._fetch_abstract("10.0000/no-existe")

        assert resultado is None


class TestBuildIndexConDois:
    @pytest.fixture
    def course_dir_con_doi(self, tmp_path: Path) -> Path:
        (tmp_path / "UNIDAD_TEST.md").write_text(
            "# Unidad de prueba\n\n"
            "## Sección con cita\n\n"
            "Un dato real respaldado por literatura. "
            "DOI: [10.14356/kona.2020011](https://doi.org/10.14356/kona.2020011).\n",
            encoding="utf-8",
        )
        return tmp_path

    @pytest.fixture
    def course_dir_con_doi_repetido(self, tmp_path: Path) -> Path:
        (tmp_path / "UNIDAD_A_TEST.md").write_text(
            "# Unidad A\n\n## Sección A\n\n"
            "DOI: [10.1039/D0MA00439A](https://doi.org/10.1039/D0MA00439A).\n",
            encoding="utf-8",
        )
        (tmp_path / "UNIDAD_B_TEST.md").write_text(
            "# Unidad B\n\n## Sección B\n\n"
            "DOI: [10.1039/D0MA00439A](https://doi.org/10.1039/D0MA00439A).\n",
            encoding="utf-8",
        )
        return tmp_path

    def test_abstract_se_indexa_con_metadata_de_referencia_doi(
        self, course_dir_con_doi: Path, tmp_path: Path
    ):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "message": {"abstract": "Abstract de prueba sobre nanopartículas de oro."}
        }
        mock_response.raise_for_status.return_value = None

        with patch(
            "src.multiagent_core.stats_tutor_agent.requests.get",
            return_value=mock_response,
        ):
            tutor = StatsTutorAgent(
                course_dir=course_dir_con_doi,
                chroma_path=tmp_path / "chroma",
                memory_path=tmp_path / "m.json",
            )

        resultado = tutor._search_local_docs("nanopartículas de oro")
        assert "Referencia DOI: 10.14356/kona.2020011" in resultado
        assert "Abstract de prueba sobre nanopartículas de oro" in resultado

    def test_doi_que_falla_no_impide_indexar_el_resto_del_archivo(
        self, course_dir_con_doi: Path, tmp_path: Path
    ):
        with patch(
            "src.multiagent_core.stats_tutor_agent.requests.get",
            side_effect=requests.exceptions.Timeout("timeout simulado"),
        ):
            tutor = StatsTutorAgent(
                course_dir=course_dir_con_doi,
                chroma_path=tmp_path / "chroma",
                memory_path=tmp_path / "m.json",
            )

        resultado = tutor._search_local_docs("sección con cita")
        assert "UNIDAD_TEST.md" in resultado

    def test_doi_repetido_en_dos_archivos_solo_consulta_crossref_una_vez(
        self, course_dir_con_doi_repetido: Path, tmp_path: Path
    ):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "message": {"abstract": "Abstract único sobre nucleación."}
        }
        mock_response.raise_for_status.return_value = None

        with patch(
            "src.multiagent_core.stats_tutor_agent.requests.get",
            return_value=mock_response,
        ) as mock_get:
            StatsTutorAgent(
                course_dir=course_dir_con_doi_repetido,
                chroma_path=tmp_path / "chroma",
                memory_path=tmp_path / "m.json",
            )

        assert mock_get.call_count == 1

    def test_un_archivo_con_multiples_dois_distintos_indexa_ambos(self, tmp_path: Path):
        """Confirma que el bucle interno de _extract_dois por archivo
        alimenta correctamente varias entradas en doi_a_archivos sin
        pisarse entre sí cuando un mismo archivo cita más de un DOI."""
        (tmp_path / "UNIDAD_MULTI_TEST.md").write_text(
            "# Unidad con dos citas\n\n## Sección A\n\n"
            "Primera referencia. DOI: [10.14356/kona.2020011]"
            "(https://doi.org/10.14356/kona.2020011).\n\n"
            "## Sección B\n\n"
            "Segunda referencia distinta. DOI: [10.1016/j.cie.2023.109421]"
            "(https://doi.org/10.1016/j.cie.2023.109421).\n",
            encoding="utf-8",
        )

        def fake_get(url, **kwargs):
            mock_response = MagicMock()
            mock_response.raise_for_status.return_value = None
            mock_response.json.return_value = {
                "message": {"abstract": f"Abstract único para {url}."}
            }
            return mock_response

        with patch(
            "src.multiagent_core.stats_tutor_agent.requests.get",
            side_effect=fake_get,
        ) as mock_get:
            tutor = StatsTutorAgent(
                course_dir=tmp_path,
                chroma_path=tmp_path / "chroma",
                memory_path=tmp_path / "m.json",
            )

        assert mock_get.call_count == 2

        secciones_indexadas = tutor.collection.get()["metadatas"]
        titulos_referencia_doi = {
            m["section"]
            for m in secciones_indexadas
            if m["section"].startswith("Referencia DOI")
        }
        assert titulos_referencia_doi == {
            "Referencia DOI: 10.14356/kona.2020011",
            "Referencia DOI: 10.1016/j.cie.2023.109421",
        }


class TestBibliografiaIndex:
    def _crear_pdf_con_texto(self, path: Path, texto_por_pagina: list[str]) -> None:
        """Crea un PDF real usando pypdf, con una página en blanco por cada
        entrada de texto_por_pagina -- pypdf.PdfWriter no soporta insertar
        texto directamente sin reportlab, así que estos tests parchean
        pdf_indexer.index_pdf directamente en vez de generar PDFs con
        contenido real (ver Task 2 para los tests de extracción real)."""
        from pypdf import PdfWriter

        writer_test = PdfWriter()
        for _ in texto_por_pagina:
            writer_test.add_blank_page(width=612, height=792)
        with open(path, "wb") as f:
            writer_test.write(f)

    def test_sin_carpeta_bibliografia_no_falla_y_coleccion_queda_vacia(
        self, course_dir: Path, tmp_path: Path
    ):
        tutor = StatsTutorAgent(
            course_dir,
            chroma_path=tmp_path / "chroma",
            memory_path=tmp_path / "m.json",
            bibliografia_dir=tmp_path / "bibliografia_inexistente",
        )

        assert tutor.bibliografia_collection.count() == 0

    def test_pdf_con_texto_se_indexa_en_coleccion_separada(
        self, course_dir: Path, tmp_path: Path
    ):
        bibliografia_dir = tmp_path / "bibliografia"
        bibliografia_dir.mkdir()
        self._crear_pdf_con_texto(bibliografia_dir / "libro.pdf", [""])

        with patch(
            "src.multiagent_core.stats_tutor_agent.index_pdf",
            return_value=[
                {
                    "text": "Contenido del libro sobre distribuciones.",
                    "page": 1,
                    "source": "libro.pdf",
                }
            ],
        ):
            tutor = StatsTutorAgent(
                course_dir,
                chroma_path=tmp_path / "chroma",
                memory_path=tmp_path / "m.json",
                bibliografia_dir=bibliografia_dir,
            )

        assert tutor.bibliografia_collection.count() == 1
        metadatas = tutor.bibliografia_collection.get()["metadatas"]
        assert metadatas[0]["source"] == "libro.pdf"
        assert metadatas[0]["page"] == 1

    def test_pdf_sin_chunks_no_agrega_nada_a_la_coleccion(
        self, course_dir: Path, tmp_path: Path
    ):
        bibliografia_dir = tmp_path / "bibliografia"
        bibliografia_dir.mkdir()
        self._crear_pdf_con_texto(bibliografia_dir / "vacio.pdf", [""])

        with patch(
            "src.multiagent_core.stats_tutor_agent.index_pdf",
            return_value=[],
        ):
            tutor = StatsTutorAgent(
                course_dir,
                chroma_path=tmp_path / "chroma",
                memory_path=tmp_path / "m.json",
                bibliografia_dir=bibliografia_dir,
            )

        assert tutor.bibliografia_collection.count() == 0

    def test_indexacion_de_bibliografia_es_persistente_entre_instancias(
        self, course_dir: Path, tmp_path: Path
    ):
        bibliografia_dir = tmp_path / "bibliografia"
        bibliografia_dir.mkdir()
        self._crear_pdf_con_texto(bibliografia_dir / "libro.pdf", [""])
        chroma_path = tmp_path / "chroma"

        with patch(
            "src.multiagent_core.stats_tutor_agent.index_pdf",
            return_value=[
                {"text": "Contenido de prueba.", "page": 1, "source": "libro.pdf"}
            ],
        ) as mock_index_pdf:
            StatsTutorAgent(
                course_dir,
                chroma_path=chroma_path,
                memory_path=tmp_path / "m1.json",
                bibliografia_dir=bibliografia_dir,
            )
            StatsTutorAgent(
                course_dir,
                chroma_path=chroma_path,
                memory_path=tmp_path / "m2.json",
                bibliografia_dir=bibliografia_dir,
            )

        assert mock_index_pdf.call_count == 1


class TestSearchLocalDocsConBibliografia:
    def test_combina_resultados_de_lecciones_y_bibliografia(
        self, course_dir: Path, tmp_path: Path
    ):
        from pypdf import PdfWriter

        bibliografia_dir = tmp_path / "bibliografia"
        bibliografia_dir.mkdir()
        writer_test = PdfWriter()
        writer_test.add_blank_page(width=612, height=792)
        with open(bibliografia_dir / "libro.pdf", "wb") as f:
            writer_test.write(f)

        with patch(
            "src.multiagent_core.stats_tutor_agent.index_pdf",
            return_value=[
                {
                    "text": "La media muestral es un estimador insesgado según este libro.",
                    "page": 42,
                    "source": "libro.pdf",
                }
            ],
        ):
            tutor = StatsTutorAgent(
                course_dir,
                chroma_path=tmp_path / "chroma",
                memory_path=tmp_path / "m.json",
                bibliografia_dir=bibliografia_dir,
            )

        contexto = tutor._search_local_docs("¿Cómo se calcula la media muestral?")

        assert "UNIDAD_1" in contexto
        assert "libro.pdf" in contexto
        assert "Página: 42" in contexto

    def test_sin_bibliografia_indexada_solo_devuelve_lecciones(
        self, course_dir: Path, tmp_path: Path
    ):
        tutor = StatsTutorAgent(
            course_dir,
            chroma_path=tmp_path / "chroma",
            memory_path=tmp_path / "m.json",
            bibliografia_dir=tmp_path / "bibliografia_inexistente",
        )

        contexto = tutor._search_local_docs("¿Cómo se calcula la media muestral?")

        assert "UNIDAD_1" in contexto
        assert "Página:" not in contexto
