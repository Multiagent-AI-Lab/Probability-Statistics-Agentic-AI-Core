"""
Tests de caracterización para el hallazgo H-06: la celda de Autoevaluación de las
8 unidades aprobaba (imprimía "OK") entregas degeneradas (archivo vacío, `pass`,
solo un comentario, la plantilla sin tocar, o una respuesta numéricamente
imposible) porque `CodeAuditorAgent.audit_code` solo verifica estilo/OWASP y
nunca el resultado real del ejercicio.

Estos tests ejercitan `ExerciseVerifierAgent.verificar`, la pieza nueva que la
celda de Autoevaluación usa además de `CodeAuditorAgent` para exigir: código no
vacío/no trivial, sin `# TODO:` de la plantilla sin resolver, y valores que
satisfacen `assert`s de referencia calculados con SciPy en la propia celda.
"""

import re

import pytest

from src.multiagent_core.exercise_verifier_agent import ExerciseVerifierAgent

UNIDAD_5_PATH = "lecciones/UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.md"


def leer_plantilla_writefile_de_unidad_5() -> str:
    """Extrae el bloque `%%writefile solucion_ejercicio_u5.py` tal cual aparece
    en la lección (la plantilla que el alumno recibe antes de completarla)."""
    with open(UNIDAD_5_PATH, encoding="utf-8") as f:
        contenido = f.read()

    match = re.search(
        r"```python\n%%writefile solucion_ejercicio_u5\.py\n(.*?)\n```",
        contenido,
        re.DOTALL,
    )
    assert match is not None, "no se encontró la celda %%writefile de la Unidad 5"
    return match.group(1)


@pytest.fixture
def auditor_de_ejercicio() -> ExerciseVerifierAgent:
    """Verificador configurado con los checks de referencia de la Unidad 5
    (distribución normal, mu=15.0, sigma=0.8), tal como los da el brief de
    la auditoría."""
    checks = [
        "abs(p_ventana - (stats.norm.cdf(16, 15, 0.8) - stats.norm.cdf(14, 15, 0.8))) < 1e-6",
        "abs(percentil_90 - stats.norm.ppf(0.9, 15, 0.8)) < 1e-6",
        "abs(p_exceso - stats.norm.sf(17, 15, 0.8)) < 1e-6",
    ]
    variables_requeridas = ["p_ventana", "percentil_90", "p_exceso"]
    return ExerciseVerifierAgent(
        variables_requeridas=variables_requeridas,
        checks=checks,
        plantilla=leer_plantilla_writefile_de_unidad_5(),
    )


def test_autoevaluacion_rechaza_archivo_vacio(auditor_de_ejercicio):
    resultado = auditor_de_ejercicio.verificar("")
    assert resultado.aprueba is False


def test_autoevaluacion_rechaza_solo_comentario(auditor_de_ejercicio):
    resultado = auditor_de_ejercicio.verificar("# no hice nada")
    assert resultado.aprueba is False


def test_autoevaluacion_rechaza_plantilla_sin_tocar(auditor_de_ejercicio):
    plantilla_original = leer_plantilla_writefile_de_unidad_5()
    resultado = auditor_de_ejercicio.verificar(plantilla_original)
    assert (
        resultado.aprueba is False
    ), "la plantilla con # TODO: intactos no debe aprobar"


def test_autoevaluacion_rechaza_pass(auditor_de_ejercicio):
    resultado = auditor_de_ejercicio.verificar("pass")
    assert resultado.aprueba is False


def test_autoevaluacion_rechaza_respuesta_imposible(auditor_de_ejercicio):
    resultado = auditor_de_ejercicio.verificar("p = 999.0\npercentil = -50.0")
    assert resultado.aprueba is False, "una probabilidad > 1 no debe aprobar"


def test_autoevaluacion_acepta_solucion_correcta(auditor_de_ejercicio):
    solucion_correcta = """
import scipy.stats as stats

mu = 15.0
sigma = 0.8

p_ventana = stats.norm.cdf(16, mu, sigma) - stats.norm.cdf(14, mu, sigma)
percentil_90 = stats.norm.ppf(0.9, mu, sigma)
p_exceso = stats.norm.sf(17, mu, sigma)
"""
    resultado = auditor_de_ejercicio.verificar(solucion_correcta)
    assert resultado.aprueba is True, resultado.issues
