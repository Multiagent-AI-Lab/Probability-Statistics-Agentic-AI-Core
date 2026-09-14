"""Tests for EngineerAgent.

Cubre dos responsabilidades:
- `check_code_implementation`: ejecución real del código y contraste de su
  salida contra los `\\boxed{}` de la misma sección (H-01: antes bastaba
  con que la subcadena "scipy" apareciera en el texto).
- `check_monte_carlo_convergence`: guardrail de convergencia Monte Carlo.
"""

import textwrap
import time

from src.multiagent_core.council._contraste_boxed import _ROTULO_INLINE
from src.multiagent_core.council.engineer_agent import (
    _MAX_CHARS_SALIDA_SECCION,
    EngineerAgent,
)


def _seccion(codigo: str, boxed: str) -> str:
    """Arma una sección de lección: un bloque de código seguido del valor
    final que ese código debería producir, encuadrado en `\\boxed{}`."""
    return (
        "## 1. Sección de prueba\n\n```python\n"
        + textwrap.dedent(codigo).strip()
        + "\n```\n\nPor lo tanto $$\\boxed{"
        + boxed
        + "}$$\n"
    )


# --- Ejecución real y contraste contra \boxed{} (H-01) ---


def test_codigo_cuya_salida_coincide_con_el_boxed_pasa():
    agent = EngineerAgent()
    texto = _seccion("print(round(2 + 2, 4))", "4")

    resultado = agent.check_code_implementation(texto)

    assert resultado["passed"] is True
    assert resultado["discrepancias"] == []


def test_codigo_cuya_salida_contradice_el_boxed_falla():
    """El corazón de H-01: un ejemplo cuyo código dice 7.5 y cuyo texto
    afirma 9.9 debe ser detectado, no aprobado por contener 'scipy'."""
    agent = EngineerAgent()
    texto = _seccion("import scipy.stats\nprint(round(3 * 2.5, 4))", "9.9")

    resultado = agent.check_code_implementation(texto)

    assert resultado["passed"] is False
    assert resultado["discrepancias"]


def test_la_subcadena_scipy_ya_no_basta_para_aprobar():
    """H-01: `passed = 'scipy' in code_text` aprobaba cualquier documento
    que mencionara la palabra, sin ejecutar nada."""
    agent = EngineerAgent()
    texto = _seccion("import scipy.stats\nprint(round(1.0, 4))", "42.0")

    resultado = agent.check_code_implementation(texto)

    assert resultado["passed"] is False


def test_tolerancia_numerica_acepta_redondeo_del_texto():
    """El texto redondea a 4 decimales; el código imprime más precisión."""
    agent = EngineerAgent()
    texto = _seccion("print(1 / 3)", "0.3333")

    resultado = agent.check_code_implementation(texto)

    assert resultado["passed"] is True


def test_boxed_con_unidades_se_compara_solo_por_el_numero():
    agent = EngineerAgent()
    texto = _seccion("print(round(15.65, 4))", r"15.65\ \text{nm}")

    resultado = agent.check_code_implementation(texto)

    assert resultado["passed"] is True


def test_boxed_simbolico_sin_numero_no_genera_discrepancia():
    """`\\boxed{X = F^{-1}(U)}` (UNIDAD 6) no declara un valor numérico:
    no hay nada que contrastar, y no debe inventarse una falla."""
    agent = EngineerAgent()
    texto = _seccion("print('sin valor numerico')", "X = F^{-1}(U)")

    resultado = agent.check_code_implementation(texto)

    assert resultado["passed"] is True
    assert resultado["discrepancias"] == []


def test_seccion_sin_codigo_ejecutable_no_genera_discrepancia():
    agent = EngineerAgent()
    texto = "## Teoría\n\nSolo prosa, sin bloque de código. $$\\boxed{3.14}$$\n"

    resultado = agent.check_code_implementation(texto)

    assert resultado["discrepancias"] == []


def test_codigo_que_falla_al_ejecutarse_se_reporta():
    agent = EngineerAgent()
    texto = _seccion("raise ValueError('boom')", "1.0")

    resultado = agent.check_code_implementation(texto)

    assert resultado["passed"] is False
    assert resultado["errores_de_ejecucion"]


def test_bloques_no_ejecutables_se_omiten_sin_penalizar():
    """Bloques con ipytest/agentes del repo/red no se ejecutan en la
    auditoría; omitirlos no debe contar como error de ejecución."""
    agent = EngineerAgent()
    texto = _seccion(
        "import ipytest\nipytest.run('-vv')",
        "1.0",
    )

    resultado = agent.check_code_implementation(texto)

    assert resultado["errores_de_ejecucion"] == []


def test_boxed_de_otro_ejemplo_analitico_no_es_falso_positivo():
    """Patrón real de las lecciones (UNIDAD 7 §1.3, dos `\\boxed{}` en la
    misma sección: alpha=0.2466 y beta=0.6068 derivados a mano de una
    exponencial). El bloque de código verifica un escenario AgNP
    completamente distinto. No es una discrepancia.

    Nota (N-03, Task 2): con un solo `\\boxed{}` en la sección, este
    mismo patrón (rótulo ausente del stdout, código de otro ejemplo) es
    indistinguible del caso que N-03 corrige -un solo `\\boxed{}` cuyo
    rótulo no aparece en el stdout porque el código no lo imprime con
    ese nombre, siendo el MISMO ejemplo- y con la relajación de N-03 se
    reportaría como discrepancia. La sección real de UNIDAD 7 §1.3 tiene
    dos `\\boxed{}` (verificado en el .md), por lo que nunca activa esa
    rama; el test se ajusta a dos `\\boxed{}` para reflejar el patrón
    real, en vez del caso de un solo boxed que ya no ocurre en el curso."""
    agent = EngineerAgent()
    texto = (
        "## 1. Sección de prueba\n\n"
        r"$$\alpha = P(X > 28 \mid \mu=20) = e^{-28/20} \approx \boxed{0.2466}$$"
        "\n"
        r"$$\beta = P(X \le 28 \mid \mu=30) = 1 - e^{-28/30} \approx \boxed{0.6068}$$"
        "\n\n```python\n"
        "print(f'Region de no rechazo: (48.6934, 51.3066) nm')\n"
        "print(f'beta=0.1492, potencia=0.8508')\n"
        "```\n"
    )

    resultado = agent.check_code_implementation(texto)

    assert resultado["discrepancias"] == []


def test_boxed_en_porcentaje_coincide_con_salida_en_proporcion():
    """`\\boxed{0.1126\\ (11.26\\%)}` frente a un print de 0.1126."""
    agent = EngineerAgent()
    texto = _seccion("print(round(0.1126, 4))", r"0.1126\ (11.26\%)")

    resultado = agent.check_code_implementation(texto)

    assert resultado["discrepancias"] == []


def test_codigo_solo_simbolico_no_genera_discrepancia():
    """UNIDAD 7 §6.2: el bloque resuelve el MLE con SymPy y no imprime
    ningún número; su `\\boxed{}` es una fórmula, no un valor."""
    agent = EngineerAgent()
    texto = _seccion(
        "import sympy as sp\nmu = sp.Symbol('mu')\nexpr = sp.diff(mu**2, mu)",
        r"\hat{\mu}_{MLE} = \bar{X}",
    )

    resultado = agent.check_code_implementation(texto)

    assert resultado["discrepancias"] == []


def test_valor_analitico_ausente_de_la_salida_se_detecta():
    """Un `\\boxed{}` derivado a mano en una sección teórica se verifica con
    el código de la sección computacional: si el valor declarado no aparece
    en ninguna salida de la unidad y el código sí trabaja sobre esos mismos
    datos, el texto está desincronizado del código."""
    agent = EngineerAgent()
    texto = (
        "### 2.2 Paso analítico\n\n"
        r"$$\bar{x} = \frac{156.5}{10} = \boxed{19.99\ \text{nm}}$$"
        "\n\n### 4. Solución computacional\n\n```python\n"
        "print(f'Suma: {156.5:.4f} nm')\n"
        "print(f'Media: {156.5 / 10:.4f} nm')\n"
        "```\n"
    )

    resultado = agent.check_code_implementation(texto)

    assert resultado["passed"] is False
    assert any(d["valor_declarado"] == 19.99 for d in resultado["discrepancias"])


def test_valor_analitico_correcto_no_se_reporta():
    """Control del test anterior: con el valor correcto no hay hallazgo."""
    agent = EngineerAgent()
    texto = (
        "### 2.2 Paso analítico\n\n"
        r"$$\bar{x} = \frac{156.5}{10} = \boxed{15.65\ \text{nm}}$$"
        "\n\n### 4. Solución computacional\n\n```python\n"
        "print(f'Media: {156.5 / 10:.4f} nm')\n"
        "```\n"
    )

    resultado = agent.check_code_implementation(texto)

    assert resultado["discrepancias"] == []


def test_ejemplo_analitico_autocontenido_no_se_reporta():
    """UNIDAD 7 §1.6 resuelve a mano un Z-test de notas de examen que ningún
    bloque de la unidad reproduce: sus datos no aparecen en la salida, así
    que su resultado ausente no es evidencia de error."""
    agent = EngineerAgent()
    texto = (
        "### 1.6 Ejemplo resuelto\n\n"
        r"$$z_0 = \frac{7.8-8}{0.5/\sqrt{50}} \approx \boxed{-2.83}$$"
        "\n\n### 2. Otro caso\n\n```python\n"
        "print(f'limite={48.6934:.4f}')\n"
        "```\n"
    )

    resultado = agent.check_code_implementation(texto)

    assert resultado["discrepancias"] == []


def test_boxed_emitido_por_el_codigo_contradice_al_texto():
    """H-05 real de UNIDAD 6: el texto afirma T=12.3957 y la celda SymPy
    imprime su propio `\\boxed{6.8447}` para el mismo U=0.35. El `\\boxed{}`
    que emite el código es la afirmación más fuerte disponible."""
    agent = EngineerAgent()
    texto = (
        "### 2.3 Evaluación para $U = 0.35$\n\n"
        r"$$\boxed{T = 12.0 \times 1.03297 \approx 12.3957 \text{ segundos}}$$"
        "\n\n### 3. Verificación simbólica\n\n```python\n"
        "from IPython.display import display, Math\n"
        "t = 6.8447\n"
        'display(Math(fr"Tiempo para U=0.35: \\boxed{{{t:.4f}}}"))\n'
        "```\n"
    )

    resultado = agent.check_code_implementation(texto)

    assert resultado["passed"] is False
    assert any(d["valor_declarado"] == 12.3957 for d in resultado["discrepancias"])


def test_display_math_no_queda_invisible_para_la_auditoria():
    """IPython está instalado, así que `Math(...)` real imprime
    '<IPython.core.display.Math object>' y el número quedaría fuera de
    stdout: toda la fase de verificación simbólica sería invisible."""
    agent = EngineerAgent()
    texto = (
        "## 1. Sección\n\n```python\n"
        "from IPython.display import display, Math\n"
        'display(Math(r"resultado = 7.5"))\n'
        "```\n\n"
        r"Por lo tanto $$\boxed{7.5}$$"
        "\n"
    )

    resultado = agent.check_code_implementation(texto)

    assert resultado["discrepancias"] == []


def test_sintaxis_de_notebook_no_silencia_la_verificacion():
    """Una línea `%pip install` hace fallar la compilación del archivo
    entero: sin filtrarla, la unidad no produce salida y aprueba por
    vacuidad -- el mismo silencio que H-01 denuncia."""
    agent = EngineerAgent()
    texto = (
        "## 1. Setup\n\n```python\n%pip install -q distfit\n```\n\n"
        "## 2. Cálculo\n\n```python\nprint(round(3 * 2.5, 4))\n```\n\n"
        r"Por lo tanto $$\boxed{9.9}$$"
        "\n"
    )

    resultado = agent.check_code_implementation(texto)

    assert resultado["errores_de_ejecucion"] == []
    assert resultado["passed"] is False


def test_reporta_uso_de_scipy_o_statsmodels_como_metadato():
    """Se sigue reportando (Gold Standard §3.6), pero ya no decide el veredicto."""
    agent = EngineerAgent()
    texto = _seccion("import scipy.stats\nprint(round(1.0, 4))", "1.0")

    resultado = agent.check_code_implementation(texto)

    assert resultado["has_scipy_or_statsmodels"] is True


# --- Guardrail de convergencia Monte Carlo (comportamiento preexistente) ---


def test_iteraciones_insuficientes_dispara_warning_critico():
    agent = EngineerAgent()
    code = """
import numpy as np
N_sim = 50
muestras = np.random.uniform(0, 1, N_sim)
"""
    result = agent.check_monte_carlo_convergence(code)
    assert result["critical"] is True
    assert any(
        "convergencia" in w.lower() or "iteraciones" in w.lower()
        for w in result["warnings"]
    )


def test_iteraciones_suficientes_no_dispara_warning():
    agent = EngineerAgent()
    code = """
import numpy as np
N_sim = 50_000
muestras = np.random.uniform(0, 1, N_sim)
"""
    result = agent.check_monte_carlo_convergence(code)
    assert result["critical"] is False
    assert result["warnings"] == []


def test_umbral_personalizable():
    agent = EngineerAgent()
    code = """
import numpy as np
N_sim = 2000
muestras = np.random.uniform(0, 1, N_sim)
"""
    result_umbral_bajo = agent.check_monte_carlo_convergence(code, min_iterations=1000)
    result_umbral_alto = agent.check_monte_carlo_convergence(code, min_iterations=5000)

    assert result_umbral_bajo["critical"] is False
    assert result_umbral_alto["critical"] is True


def test_codigo_sin_simulacion_no_dispara_nada():
    agent = EngineerAgent()
    code = """
import scipy.stats as stats
resultado = stats.norm.cdf(1.96)
"""
    result = agent.check_monte_carlo_convergence(code)
    assert result["critical"] is False
    assert result["warnings"] == []


def test_detecta_multiples_variables_de_conteo_de_muestras():
    agent = EngineerAgent()
    code = """
import numpy as np
n_muestras = 100
datos = np.random.normal(0, 1, n_muestras)
"""
    result = agent.check_monte_carlo_convergence(code)
    assert result["critical"] is True


def test_n_samples_de_tamano_de_dataset_no_dispara_falso_positivo():
    """n_samples (ingles) se usa en las lecciones para tamano de dataset
    (p. ej. UNIDAD_8, RANSAC con 45 filas), no para iteraciones Monte Carlo.
    No debe disparar el guardrail aunque el valor este bajo el umbral."""
    agent = EngineerAgent()
    code = """
import numpy as np
np.random.seed(74)
n_samples = 45
radio_nm = np.linspace(5, 60, n_samples).reshape(-1, 1)
spr_pico = 2.3 * radio_nm.ravel() + np.random.normal(0, 3, n_samples)
"""
    result = agent.check_monte_carlo_convergence(code)
    assert result["critical"] is False
    assert result["warnings"] == []


# --------------------------------------------------------------------------
# Regresión de ReDoS en `_ROTULO_INLINE` (hallazgo CRITICAL de
# @security-reviewer sobre el fix de N-01, cerrado con cuantificadores
# acotados). `_valores_junto_al_rotulo` ya corta cada línea a
# `_MAX_CHARS_POR_LINEA_ROTULO` antes de aplicar el regex, así que estos
# tests ejercitan `_ROTULO_INLINE` directamente -sin esa cota externa-
# para que una futura edición que reintroduzca un cuantificador sin
# límite (`+`/`*` en vez de `{1,40}`) se detecte aunque la cota de línea
# también se toque en el mismo cambio.
# --------------------------------------------------------------------------

_TECHO_SEGUNDOS_REDOS = 2.0


def test_rotulo_inline_no_escala_cuadratico_sin_signo_igual():
    """Una linea larga sin ningun '=' no debe colgar ni degradar
    cuadraticamente: es exactamente el caso real de un traceback largo o
    un repr() de un array de NumPy sin saltos de linea."""
    salida = "a" * 100_000

    t0 = time.perf_counter()
    resultado = _ROTULO_INLINE.findall(salida)
    duracion = time.perf_counter() - t0

    assert resultado == []
    assert duracion < _TECHO_SEGUNDOS_REDOS, (
        f"_ROTULO_INLINE tardo {duracion:.2f}s sobre 100_000 "
        "caracteres sin '=' -- posible regresion de ReDoS"
    )


def test_rotulo_inline_no_escala_cuadratico_con_muchos_signos_igual():
    """Muchos '=' seguidos sin un numero valido detras tampoco debe
    degradar: agota la otra rama del backtracking (el identificador, no
    el numero)."""
    salida = "a=" * 50_000

    t0 = time.perf_counter()
    resultado = _ROTULO_INLINE.findall(salida)
    duracion = time.perf_counter() - t0

    assert resultado == []
    assert duracion < _TECHO_SEGUNDOS_REDOS, (
        f"_ROTULO_INLINE tardo {duracion:.2f}s sobre 50_000 "
        "repeticiones de 'a=' -- posible regresion de ReDoS"
    )


def test_salida_larga_no_escala_sin_limite_global_i4():
    """I-4 (INFO, auditoría 2026-09-13): antes de esta cota, el único
    límite era `_MAX_CHARS_POR_LINEA_ROTULO` -por línea, no por
    documento-, así que un stdout de muchas líneas (cada una dentro de
    la cota) seguía escalando linealmente con el tamaño TOTAL del
    documento en `_extraer_numeros`. No es ReDoS (el regex ya es
    lineal) pero es trabajo desperdiciado evitable con una cota global
    aplicada antes de cualquier procesamiento.

    Mide el post-procesamiento de texto directamente (`_extraer_numeros`
    sobre una salida ya capturada, con y sin la cota aplicada), no
    `check_code_implementation` de punta a punta: ese camino completo
    pasa por `_ejecutar_unidad` (subprocess con el preámbulo de
    matplotlib), cuyo overhead fijo (~9s, medido) domina cualquier caso
    de prueba -trivial o no- y haría que este test mida ese costo
    preexistente y no relacionado, en vez del que I-4 realmente acota."""
    agent = EngineerAgent()
    salida_enorme = "p = " + "(" * 5_000_000  # muy por encima de la cota

    t0 = time.perf_counter()
    agent._extraer_numeros(salida_enorme[:_MAX_CHARS_SALIDA_SECCION])
    duracion_con_cota = time.perf_counter() - t0

    t0 = time.perf_counter()
    agent._extraer_numeros(salida_enorme)
    duracion_sin_cota = time.perf_counter() - t0

    assert duracion_con_cota < 1.0, (
        f"_extraer_numeros tardo {duracion_con_cota:.2f}s incluso con la "
        "salida ya truncada a _MAX_CHARS_SALIDA_SECCION -- la cota deberia "
        "mantenerlo bajo sin importar el tamano original del documento"
    )
    assert duracion_sin_cota > duracion_con_cota, (
        "sin la cota, procesar la salida completa (5_000_000 caracteres) "
        "deberia tomar notoriamente mas que procesar la version truncada "
        "-- si no hay diferencia, la cota global (I-4) no esta acotando "
        "nada real"
    )


def test_salida_de_la_unidad_tambien_queda_acotada_i4():
    """I-4, hallazgo de la revisión final de rama (2026-09-14): la cota
    `_MAX_CHARS_SALIDA_SECCION` se aplicaba a `salida` (una sola sección,
    dentro de `check_code_implementation`) pero NO a
    `salida_de_la_unidad` -la concatenación de TODAS las secciones-, que
    se pasa sin truncar a `_contrastar_contra_la_unidad`. Una unidad con
    muchas secciones, cada una dentro de la cota individual, seguía
    escalando la concatenación con el tamaño TOTAL de la unidad: exactamente
    el escenario que el propio comentario de I-4 decía cerrar.

    Ejercita el código real de `check_code_implementation` (no solo la
    función de post-procesamiento en aislamiento) parcheando
    `_ejecutar_unidad` y `_contrastar_contra_la_unidad` para inspeccionar
    exactamente qué tamaño de `salida_de_la_unidad` llega a esta última,
    sin pagar el overhead de subprocess/matplotlib de una ejecución real."""
    from unittest.mock import patch

    from src.multiagent_core.council.engineer_agent import EngineerAgent as _EA

    # Dos secciones: una con `\boxed{}` sin código propio (activa
    # _contrastar_contra_la_unidad, que usa salida_de_la_unidad completa)
    # y otra con un bloque ejecutable trivial (necesario para que
    # hay_algo_que_verificar sea True y _ejecutar_unidad -mockeada abajo-
    # llegue a invocarse).
    texto = (
        "## 1. Teoría\n\n$$\\boxed{p = 0.42}$$\n\n"
        "## 2. Cómputo\n\n```python\nprint('x = 1')\n```\n"
    )

    # 300 secciones de 10_000 caracteres -> unión de 3_000_000 caracteres,
    # muy por encima de _MAX_CHARS_SALIDA_SECCION*10 (2_000_000): confirma
    # que el truncado de unidad SÍ recorta un caso que lo excede.
    secciones_grandes = {f"sección {i}": ("x" * 10_000) for i in range(300)}
    tamanos_recibidos = []

    def _contrastar_espia(titulo, esperados, salida_de_la_unidad, discrepancias):
        tamanos_recibidos.append(len(salida_de_la_unidad))

    agent = _EA()
    with patch.object(
        agent, "_ejecutar_unidad", return_value=(secciones_grandes, None, None)
    ), patch(
        "src.multiagent_core.council.engineer_agent._contrastar_contra_la_unidad",
        side_effect=_contrastar_espia,
    ):
        resultado = agent.check_code_implementation(texto)

    assert resultado is not None
    assert len(tamanos_recibidos) == 1, "se esperaba una sola llamada"
    assert tamanos_recibidos[0] <= _MAX_CHARS_SALIDA_SECCION * 10, (
        f"salida_de_la_unidad llegó con {tamanos_recibidos[0]} caracteres a "
        f"_contrastar_contra_la_unidad -- debería quedar acotada a "
        f"{_MAX_CHARS_SALIDA_SECCION * 10} (10x la cota por sección)"
    )
