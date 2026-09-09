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

import ast
import re
import time

import pytest

from src.multiagent_core.exercise_verifier_agent import (
    ExerciseVerifierAgent,
    ResultadoVerificacion,
    reportar_resultado_ejercicio,
)

UNIDAD_5_PATH = "lecciones/UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.md"
UNIDAD_1_PATH = "lecciones/UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md"
UNIDAD_7_PATH = "lecciones/UNIDAD_7_INFERENCIA_ESTIMACION.md"
UNIDAD_8_PATH = "lecciones/UNIDAD_8_PROYECTO_INTEGRADOR.md"


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


def _leer_leccion(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def leer_configuracion_del_verificador(path: str) -> tuple[list[str], list[str]]:
    """Extrae `variables_requeridas` y `checks` del `ExerciseVerifierAgent`
    que la celda de Autoevaluación de esa lección construye.

    Los tests de checks auto-referenciales (CRÍTICO-2) deben ejercitar lo que
    el alumno realmente ejecuta en el notebook, no una copia en el test que
    podría desincronizarse de la lección.
    """
    contenido = _leer_leccion(path)
    match = re.search(
        r"verificador = (ExerciseVerifierAgent\(.*?\n\))",
        contenido,
        re.DOTALL,
    )
    assert match is not None, f"no se encontró el ExerciseVerifierAgent en {path}"

    # `plantilla=plantilla_original` es un nombre, no un literal: se sustituye
    # por None para que la llamada sea evaluable con `ast.literal_eval`.
    fuente = match.group(1).replace("plantilla=plantilla_original", "plantilla=None")
    llamada = ast.parse(fuente, mode="eval").body
    argumentos = {kw.arg: ast.literal_eval(kw.value) for kw in llamada.keywords}
    return argumentos["variables_requeridas"], argumentos["checks"]


def leer_plantilla_original(path: str) -> str:
    """Extrae el literal `plantilla_original = \"\"\"...\"\"\"` de la lección."""
    contenido = _leer_leccion(path)
    match = re.search(
        r'plantilla_original = """(.*?)"""',
        contenido,
        re.DOTALL,
    )
    assert match is not None, f"no se encontró plantilla_original en {path}"
    return match.group(1)


def verificador_de_leccion(path: str) -> ExerciseVerifierAgent:
    variables, checks = leer_configuracion_del_verificador(path)
    return ExerciseVerifierAgent(
        variables_requeridas=variables,
        checks=checks,
        plantilla=leer_plantilla_original(path),
    )


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


# --------------------------------------------------------------------------
# Fix round 1 — CRÍTICO-1: aislamiento real de la ejecución del código del alumno
# --------------------------------------------------------------------------


def test_codigo_del_alumno_no_puede_importar_os(auditor_de_ejercicio):
    """El docstring prometía "sin acceso a builtins peligrosos", pero un dict de
    globals sin `__builtins__` explícito hace que Python inyecte el módulo
    completo: `import os` y `open` quedaban disponibles."""
    codigo = """
import os

p_ventana = os.name
"""
    resultado = auditor_de_ejercicio.verificar(codigo)
    assert resultado.aprueba is False
    assert any(
        "no ejecuta" in issue or "no está permitido" in issue.lower()
        for issue in resultado.issues
    ), f"`import os` debe fallar dentro del código evaluado; issues={resultado.issues}"


def test_codigo_del_alumno_no_puede_usar_open(auditor_de_ejercicio):
    codigo = """
p_ventana = open("/etc/passwd")
"""
    resultado = auditor_de_ejercicio.verificar(codigo)
    assert resultado.aprueba is False
    assert any(
        "no ejecuta" in issue or "no está permitido" in issue.lower()
        for issue in resultado.issues
    ), f"`open` no debe ser accesible; issues={resultado.issues}"


def test_bucle_infinito_corta_por_timeout(auditor_de_ejercicio):
    """Un `while True: pass` colgaba el proceso indefinidamente. Debe cortar por
    timeout en unos pocos segundos y reportarse como issue, no aprobar."""
    verificador = ExerciseVerifierAgent(
        variables_requeridas=auditor_de_ejercicio.variables_requeridas,
        checks=auditor_de_ejercicio.checks,
        plantilla=auditor_de_ejercicio.plantilla,
        timeout=5,
    )
    inicio = time.monotonic()
    resultado = verificador.verificar("while True:\n    pass\n")
    transcurrido = time.monotonic() - inicio

    assert resultado.aprueba is False
    assert transcurrido < 30, (
        "el verificador no cortó el bucle infinito en un tiempo razonable "
        f"({transcurrido:.1f}s)"
    )
    assert any(
        "timeout" in issue.lower() or "tiempo" in issue.lower()
        for issue in resultado.issues
    ), f"se esperaba un issue de timeout; issues={resultado.issues}"


# --------------------------------------------------------------------------
# Fix round 1 — CRÍTICO-2: los checks de U1/U8 eran auto-referenciales
# --------------------------------------------------------------------------


def test_u1_no_aprueba_redefiniendo_el_dataset():
    """Con checks auto-referenciales (`abs(media - np.mean(datos)) < 1e-6`) el
    alumno podía redefinir `datos` con 3 números arbitrarios y aprobar sin
    haber hecho el análisis pedido."""
    verificador = verificador_de_leccion(UNIDAD_1_PATH)
    trampa = """
import numpy as np

datos = np.array([52.7, 53.9, 1.0])
media = np.mean(datos)
mediana = np.median(datos)
std = np.std(datos, ddof=1)
outliers = np.array([52.7, 53.9])
media_sin_outliers = np.mean([d for d in datos if d not in (52.7, 53.9)])
"""
    resultado = verificador.verificar(trampa)
    assert resultado.aprueba is False, "redefinir `datos` no debe aprobar la Unidad 1"


def test_u8_no_aprueba_redefiniendo_el_dataset():
    verificador = verificador_de_leccion(UNIDAD_8_PATH)
    trampa = """
import numpy as np
import scipy.stats as stats

sno2 = np.array([1.0, 2.0, 3.0])
in2o3 = np.array([4.0, 5.0, 6.0])

media_sno2 = np.mean(sno2)
std_sno2 = np.std(sno2, ddof=1)
media_in2o3 = np.mean(in2o3)
std_in2o3 = np.std(in2o3, ddof=1)
levene_stat, levene_p = stats.levene(sno2, in2o3)
t_stat, t_p = stats.ttest_ind(sno2, in2o3, equal_var=False)
"""
    resultado = verificador.verificar(trampa)
    assert (
        resultado.aprueba is False
    ), "redefinir `sno2`/`in2o3` no debe aprobar la Unidad 8"


def test_u1_aprueba_la_solucion_correcta():
    """Contrapeso del test anterior: los valores fijos deben seguir aprobando
    al alumno que sí resuelve el ejercicio sobre el dataset de la plantilla."""
    verificador = verificador_de_leccion(UNIDAD_1_PATH)
    solucion = """
import numpy as np

datos = np.array([21.4, 22.1, 20.8, 23.3, 21.9, 22.5, 52.7, 21.2, 22.8, 21.1, 22.2, 21.6, 53.9, 22.0])

media = np.mean(datos)
mediana = np.median(datos)
std = np.std(datos, ddof=1)

q1, q3 = np.percentile(datos, [25, 75])
iqr = q3 - q1
outliers = datos[(datos < q1 - 1.5 * iqr) | (datos > q3 + 1.5 * iqr)]
media_sin_outliers = np.mean(datos[~np.isin(datos, outliers)])
"""
    resultado = verificador.verificar(solucion)
    assert resultado.aprueba is True, resultado.issues


def test_u8_aprueba_la_solucion_correcta():
    verificador = verificador_de_leccion(UNIDAD_8_PATH)
    solucion = """
import numpy as np
import scipy.stats as stats

sno2 = np.array([3.58, 3.62, 3.55, 3.60, 3.57, 3.63, 3.59, 3.56])
in2o3 = np.array([3.71, 3.68, 3.75, 3.70, 3.73, 3.69, 3.72, 3.74])

media_sno2 = np.mean(sno2)
std_sno2 = np.std(sno2, ddof=1)
media_in2o3 = np.mean(in2o3)
std_in2o3 = np.std(in2o3, ddof=1)
levene_stat, levene_p = stats.levene(sno2, in2o3)
t_stat, t_p = stats.ttest_ind(sno2, in2o3, equal_var=False)
"""
    resultado = verificador.verificar(solucion)
    assert resultado.aprueba is True, resultado.issues


# --------------------------------------------------------------------------
# Fix round 1 — IMPORTANTE-3: los `# TODO:` propios del alumno no reprueban
# --------------------------------------------------------------------------


def test_todo_propio_del_alumno_no_reprueba(auditor_de_ejercicio):
    """`TODO_MARKER_PATTERN` reprobaba CUALQUIER `# TODO:`, con un mensaje que
    además mentía ("de la plantilla"). Solo los TODO literales de la plantilla
    original deben contar como ejercicio sin resolver."""
    solucion = """
import scipy.stats as stats

# TODO: repasar la diferencia entre cdf y sf antes del examen
mu = 15.0
sigma = 0.8

p_ventana = stats.norm.cdf(16, mu, sigma) - stats.norm.cdf(14, mu, sigma)
percentil_90 = stats.norm.ppf(0.9, mu, sigma)
p_exceso = stats.norm.sf(17, mu, sigma)
"""
    resultado = auditor_de_ejercicio.verificar(solucion)
    assert resultado.aprueba is True, resultado.issues


def test_todo_de_la_plantilla_sigue_reprobando(auditor_de_ejercicio):
    """La otra mitad del contrato: los TODO literales de la plantilla siguen
    detectándose aunque el alumno haya añadido código alrededor."""
    plantilla = leer_plantilla_writefile_de_unidad_5()
    solucion = plantilla + "\n\np_ventana = 0.0\npercentil_90 = 0.0\np_exceso = 0.0\n"
    resultado = auditor_de_ejercicio.verificar(solucion)
    assert resultado.aprueba is False
    assert any("TODO" in issue for issue in resultado.issues), resultado.issues


# --------------------------------------------------------------------------
# Fix round 1 — IMPORTANTE-4: U7 aprobaba con el resultado hardcodeado
# --------------------------------------------------------------------------


def test_u7_no_aprueba_con_z_hardcodeado():
    """`z_estadistico = 2.4` es un número fácil de memorizar. Exigir además las
    variables intermedias (error estándar y numerador) impide aprobar copiando
    solo el resultado final."""
    verificador = verificador_de_leccion(UNIDAD_7_PATH)
    trampa = """
import numpy as np
import scipy.stats as stats

z_estadistico = 2.4
p_valor = 2 * (1 - stats.norm.cdf(2.4))
"""
    resultado = verificador.verificar(trampa)
    assert (
        resultado.aprueba is False
    ), "hardcodear z_estadistico sin las variables intermedias no debe aprobar"


def test_u7_aprueba_la_solucion_correcta():
    verificador = verificador_de_leccion(UNIDAD_7_PATH)
    solucion = """
import numpy as np
import scipy.stats as stats

n = 36
sigma = 3.0
mu_0 = 25.0
x_bar = 26.2

error_estandar = sigma / np.sqrt(n)
diferencia = x_bar - mu_0
z_estadistico = diferencia / error_estandar
p_valor = 2 * (1 - stats.norm.cdf(abs(z_estadistico)))
"""
    resultado = verificador.verificar(solucion)
    assert resultado.aprueba is True, resultado.issues


# --------------------------------------------------------------------------
# Menor (Task 6, cierre de brechas): boilerplate de las 32 celdas de
# autoevaluación extraído a `reportar_resultado_ejercicio`. Estos tests de
# caracterización comparan el output de la función nueva contra una copia
# literal del bloque de ~18 líneas que se repetía en las 32 celdas -- deben
# imprimir EXACTAMENTE lo mismo para que el refactor sea puro (sin cambio de
# comportamiento observable por el alumno).
# --------------------------------------------------------------------------


class _DebuggerFalso:
    """Doble determinista de SocraticDebugger: devuelve el `error_type` que
    recibió en vez de una pregunta socrática real, para que las aserciones no
    dependan del texto pedagógico (que puede cambiar) sino de qué parámetros
    recibió la función bajo prueba."""

    def generate_socratic_question(self, error_type: str, context: str) -> str:
        return f"[{error_type}|{context}]"


def _bloque_original(resultado, resultado_ejercicio, nombre_ejercicio, unidad):
    """Copia literal del bloque que aparecía en las 32 celdas de
    autoevaluación, previa al refactor. Sirve como oráculo del test."""
    if (
        resultado["issues"]
        or resultado["metrics"]["has_security_risk"]
        or not resultado_ejercicio.aprueba
    ):
        debugger = _DebuggerFalso()
        for issue in resultado["issues"]:
            tipo_error = "syntax_error" if "SyntaxError" in issue else "generic"
            print("💡", debugger.generate_socratic_question(tipo_error, unidad))
        for issue in resultado["security_issues"]:
            print("🔒", debugger.generate_socratic_question("security_risk", unidad))
            print("   ", issue)
        for issue in resultado_ejercicio.issues:
            print("❌", debugger.generate_socratic_question("generic", unidad))
            print("   ", issue)
        print(f"\n--- Detalle técnico ({nombre_ejercicio}) ---")
        print(resultado)
        print(resultado_ejercicio)
    else:
        print(
            "✅ Tu código pasa las verificaciones automáticas de estilo, seguridad y resultado."
        )
        print(resultado)
        print(resultado_ejercicio)


def _resultado_auditor(issues=None, security_issues=None, has_security_risk=None):
    issues = issues or []
    security_issues = security_issues or []
    if has_security_risk is None:
        has_security_risk = bool(security_issues)
    return {
        "issues": issues,
        "security_issues": security_issues,
        "metrics": {"has_security_risk": has_security_risk},
    }


@pytest.mark.parametrize(
    "resultado, resultado_ejercicio",
    [
        pytest.param(
            _resultado_auditor(),
            ResultadoVerificacion(aprueba=True, issues=[]),
            id="camino_feliz_aprueba",
        ),
        pytest.param(
            _resultado_auditor(issues=["SyntaxError: algo mal en la línea 3"]),
            ResultadoVerificacion(aprueba=True, issues=[]),
            id="issue_de_estilo_syntax_error",
        ),
        pytest.param(
            _resultado_auditor(issues=["nombre de variable poco descriptivo"]),
            ResultadoVerificacion(aprueba=True, issues=[]),
            id="issue_de_estilo_generico",
        ),
        pytest.param(
            _resultado_auditor(security_issues=["uso de eval() sobre entrada externa"]),
            ResultadoVerificacion(aprueba=True, issues=[]),
            id="hallazgo_de_seguridad",
        ),
        pytest.param(
            _resultado_auditor(),
            ResultadoVerificacion(
                aprueba=False, issues=["No se cumple: abs(media - 1.0) < 1e-6"]
            ),
            id="ejercicio_no_aprueba",
        ),
        pytest.param(
            _resultado_auditor(
                issues=["SyntaxError: paréntesis sin cerrar"],
                security_issues=["riesgo de path traversal"],
            ),
            ResultadoVerificacion(
                aprueba=False,
                issues=["No se definieron las variables requeridas: media"],
            ),
            id="todos_los_hallazgos_a_la_vez",
        ),
    ],
)
def test_reportar_resultado_ejercicio_replica_el_bloque_original(
    capsys, resultado, resultado_ejercicio
):
    """La función nueva debe imprimir carácter por carácter lo mismo que el
    bloque duplicado que reemplaza, para las combinaciones de hallazgos que
    aparecen en las 32 celdas reales (sin issues, con issues de estilo, con
    riesgo de seguridad, con ejercicio reprobado, y con todo a la vez)."""
    nombre_ejercicio = "Ejercicio 2"
    unidad = "Unidad 3"

    _bloque_original(resultado, resultado_ejercicio, nombre_ejercicio, unidad)
    esperado = capsys.readouterr().out

    reportar_resultado_ejercicio(
        resultado,
        resultado_ejercicio,
        nombre_ejercicio=nombre_ejercicio,
        unidad=unidad,
        debugger=_DebuggerFalso(),
    )
    obtenido = capsys.readouterr().out

    assert obtenido == esperado
