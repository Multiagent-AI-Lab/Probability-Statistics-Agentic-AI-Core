"""
Tests for LayoutEditorialAgent.detect_duplicate_blocks.
"""

from src.multiagent_core.council.layout_editorial_agent import LayoutEditorialAgent


INTRO_SCIPY = (
    "## TEMA: AJUSTE DE DISTRIBUCIONES\n\n"
    "Este es un bloque introductorio largo sobre SciPy que se repite igual "
    "en dos unidades distintas del curso, palabra por palabra, sin ningun "
    "cambio, para simular el caso real detectado en U1 y U6 del diagnostico "
    "original del proyecto de Probabilidad y Estadistica."
)


def test_no_duplicates_returns_empty_list():
    editor = LayoutEditorialAgent()
    lessons = {
        "UNIDAD 1": "## Estadistica Descriptiva\n\nContenido único de la unidad uno sobre medidas de tendencia central.",
        "UNIDAD 2": "## Probabilidad\n\nContenido único de la unidad dos sobre combinatoria y Bayes.",
    }
    result = editor.detect_duplicate_blocks(lessons)
    assert result == []


def test_detects_cross_unit_duplicate():
    editor = LayoutEditorialAgent()
    lessons = {
        "UNIDAD 1": INTRO_SCIPY + "\n\n## Resto de U1\n\nContenido propio de estadistica descriptiva.",
        "UNIDAD 6": INTRO_SCIPY + "\n\n## Resto de U6\n\nContenido propio de inferencia y estimacion.",
    }
    result = editor.detect_duplicate_blocks(lessons)
    assert len(result) >= 1
    involved_units = {loc[0] for dup in result for loc in dup["locations"]}
    assert "UNIDAD 1" in involved_units
    assert "UNIDAD 6" in involved_units


def test_detects_intra_file_duplicate():
    editor = LayoutEditorialAgent()
    lessons = {
        "UNIDAD 4": INTRO_SCIPY + "\n\n## Seccion intermedia\n\nAlgo distinto aqui.\n\n" + INTRO_SCIPY,
    }
    result = editor.detect_duplicate_blocks(lessons)
    assert len(result) >= 1
    locations = result[0]["locations"]
    assert len({loc[1] for loc in locations}) >= 2


def test_ignores_short_blocks():
    editor = LayoutEditorialAgent()
    lessons = {
        "UNIDAD 1": "## Titulo\n\nCorto.",
        "UNIDAD 2": "## Titulo\n\nCorto.",
    }
    result = editor.detect_duplicate_blocks(lessons)
    assert result == []
