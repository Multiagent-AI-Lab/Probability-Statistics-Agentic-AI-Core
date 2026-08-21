"""
Tests para LibrarianAgent.verify_references -- verificación real de citas
(no el stub anterior que devolvía passed: True incondicional).
"""

from unittest.mock import MagicMock, patch

import requests

from src.multiagent_core.council.librarian_agent import LibrarianAgent


def test_falla_si_no_hay_ningun_doi_ni_palabra_clave_de_referencia():
    agent = LibrarianAgent()

    resultado = agent.verify_references("Texto sin ninguna cita bibliográfica.")

    assert resultado["passed"] is False
    assert resultado["has_references"] is False


def test_pasa_si_hay_palabra_clave_de_referencia_conocida_sin_doi():
    agent = LibrarianAgent()

    resultado = agent.verify_references(
        "Según Walpole y Montgomery, la distribución normal..."
    )

    assert resultado["has_references"] is True
    assert resultado["passed"] is True


def test_extrae_dois_del_texto_en_formato_markdown():
    agent = LibrarianAgent()
    texto = "Ver DOI: [10.1234/abcd.5678](https://doi.org/10.1234/abcd.5678)"

    dois = agent._extract_dois(texto)

    assert dois == ["10.1234/abcd.5678"]


@patch("src.multiagent_core.council.librarian_agent.requests.get")
def test_doi_valido_que_resuelve_en_crossref_pasa(mock_get):
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"message": {"title": ["Un paper real"]}}
    mock_get.return_value = mock_response

    agent = LibrarianAgent()
    texto = "Ver DOI: [10.1234/abcd.5678](https://doi.org/10.1234/abcd.5678)"

    resultado = agent.verify_references(texto)

    assert resultado["passed"] is True
    assert resultado["has_references"] is True
    assert resultado["dois_verificados"] == ["10.1234/abcd.5678"]
    assert resultado["dois_no_resueltos"] == []


@patch("src.multiagent_core.council.librarian_agent.requests.get")
def test_doi_que_no_resuelve_en_crossref_no_pasa(mock_get):
    mock_get.side_effect = requests.RequestException("timeout")

    agent = LibrarianAgent()
    texto = "Ver DOI: [10.9999/inexistente](https://doi.org/10.9999/inexistente)"

    resultado = agent.verify_references(texto)

    assert resultado["passed"] is False
    assert resultado["dois_no_resueltos"] == ["10.9999/inexistente"]


@patch("src.multiagent_core.council.librarian_agent.requests.get")
def test_no_llama_a_crossref_si_no_hay_ningun_doi_en_el_texto(mock_get):
    agent = LibrarianAgent()

    agent.verify_references("Según Walpole, la media muestral...")

    mock_get.assert_not_called()


@patch("src.multiagent_core.council.librarian_agent.requests.get")
def test_doi_no_resuelto_no_pasa_aunque_haya_palabra_clave_de_referencia(mock_get):
    """Si el texto cita un DOI, ese DOI debe resolver -- la presencia de una
    palabra clave conocida (Walpole) no compensa un DOI roto, porque citar
    un DOI que no existe es una afirmación bibliográfica más fuerte y más
    fácil de verificar que solo mencionar un autor de referencia."""
    mock_get.side_effect = requests.RequestException("not found")

    agent = LibrarianAgent()
    texto = "Según Walpole, ver DOI: [10.9999/roto](https://doi.org/10.9999/roto)"

    resultado = agent.verify_references(texto)

    assert resultado["passed"] is False
    assert resultado["dois_no_resueltos"] == ["10.9999/roto"]
