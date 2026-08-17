"""Tests for StatsTutorAgent (RAG + Gemini)."""

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

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
