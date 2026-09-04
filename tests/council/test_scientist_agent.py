"""
Tests para ScientistAgent.check_theory -- rigor matemático, notación LaTeX
estructurada e invariantes de dominio estadístico.

Tras H-01 el agente ya no cuenta símbolos `$` sueltos: exige bloques LaTeX
con estructura de fórmula real, exige que la solución `\\boxed{}` que ya
calculaba efectivamente cuente en el veredicto, y valida invariantes que se
pueden verificar sin LLM (probabilidad en [0,1], |rho| <= 1, varianza >= 0).
"""

from src.multiagent_core.council.scientist_agent import ScientistAgent

_TEORIA = "teoría estadística de nanopartículas " * 400


def test_pasa_con_formulas_estructuradas_boxed_y_sin_invariantes_violados():
    agent = ScientistAgent()
    texto = (
        _TEORIA
        + r"$$\mu = \sum_{i=1}^{n} x_i / n$$ "
        + r"$$\sigma^2 = E[(X - \mu)^2]$$ "
        + r"\begin{align} \rho = 0.85 \end{align} "
        + r"$\boxed{\mu = 12.5}$"
    )

    resultado = agent.check_theory(texto)

    assert resultado["passed"] is True
    assert resultado["invariantes_violados"] == []


def test_falla_por_pocas_palabras_aunque_tenga_formulas_suficientes():
    agent = ScientistAgent()
    texto = r"$$\mu = 1$$ " * 10 + r"$\boxed{x = 1}$"

    resultado = agent.check_theory(texto)

    assert resultado["word_count"] < 800
    assert resultado["passed"] is False


def test_falla_sin_formulas_estructuradas_aunque_tenga_palabras_suficientes():
    agent = ScientistAgent()

    resultado = agent.check_theory(_TEORIA + r"$\boxed{x = 1}$")

    assert resultado["tiene_formulas_estructuradas"] is False
    assert resultado["passed"] is False


def test_simbolos_dolar_sueltos_no_cuentan_como_formula():
    """H-01: `text.count("$") >= 10` aprobaba prosa con `$x$` repetido.
    Un `$x$` suelto no es una fórmula: no tiene relación ni operador."""
    agent = ScientistAgent()
    texto = ("el nanotubo mide $x$ colores y $y$ sabores " * 120) + r"$\boxed{z}$"

    resultado = agent.check_theory(texto)

    assert resultado["tiene_formulas_estructuradas"] is False
    assert resultado["passed"] is False


def test_falla_si_no_hay_solucion_boxed():
    """H-01: `has_boxed_solution` se calculaba y se descartaba del veredicto.
    El Gold Standard §3.5 lo exige, así que debe contar."""
    agent = ScientistAgent()
    texto = _TEORIA + r"$$\mu = \sum x_i / n$$ $$\sigma^2 = E[(X-\mu)^2]$$"

    resultado = agent.check_theory(texto)

    assert resultado["has_boxed_solution"] is False
    assert resultado["passed"] is False


def test_detecta_solucion_boxed():
    agent = ScientistAgent()

    resultado = agent.check_theory(r"\boxed{x = 1}")

    assert resultado["has_boxed_solution"] is True


def test_no_detecta_boxed_si_no_esta_presente():
    agent = ScientistAgent()

    resultado = agent.check_theory("texto sin solución encuadrada")

    assert resultado["has_boxed_solution"] is False


def test_probabilidad_mayor_que_uno_viola_invariante():
    agent = ScientistAgent()

    resultado = agent.check_theory(r"Se obtiene $P(A) = 1.75$ en el experimento.")

    assert any("1.75" in v for v in resultado["invariantes_violados"])
    assert resultado["passed"] is False


def test_probabilidad_negativa_viola_invariante():
    agent = ScientistAgent()

    resultado = agent.check_theory(r"El cálculo arroja $P(X = 3) = -0.2$.")

    assert any("-0.2" in v for v in resultado["invariantes_violados"])


def test_probabilidad_valida_no_viola_invariante():
    agent = ScientistAgent()

    resultado = agent.check_theory(r"La probabilidad es $P(A) = 0.35$.")

    assert resultado["invariantes_violados"] == []


def test_correlacion_fuera_de_rango_viola_invariante():
    agent = ScientistAgent()

    resultado = agent.check_theory(r"Se obtuvo $\rho = 1.4$ entre radio y SPR.")

    assert any("rho" in v.lower() for v in resultado["invariantes_violados"])


def test_correlacion_valida_no_viola_invariante():
    agent = ScientistAgent()

    resultado = agent.check_theory(r"Se obtuvo $\rho = -0.87$ entre radio y SPR.")

    assert resultado["invariantes_violados"] == []


def test_varianza_negativa_viola_invariante():
    agent = ScientistAgent()

    resultado = agent.check_theory(r"El resultado fue $\sigma^2 = -4.5$ nm².")

    assert any("varianza" in v.lower() for v in resultado["invariantes_violados"])


def test_suma_de_pmf_distinta_de_uno_viola_invariante():
    agent = ScientistAgent()

    resultado = agent.check_theory(
        r"Verificamos que $\sum_{i} P(x_i) = 2$ para la función de masa."
    )

    assert any("pmf" in v.lower() or "masa" in v.lower() for v in resultado["invariantes_violados"])


def test_suma_de_pmf_igual_a_uno_no_viola_invariante():
    agent = ScientistAgent()

    resultado = agent.check_theory(r"Se cumple que $\sum_{i} P(x_i) = 1$.")

    assert resultado["invariantes_violados"] == []


def test_probabilidad_expresada_como_fraccion_no_es_falso_positivo():
    """Regresión: `$P(C|G_B)=2/3$` (UNIDAD 2, Tres Prisioneros) leía "2"
    como la probabilidad declarada y reportaba un invariante violado
    sobre contenido correcto."""
    agent = ScientistAgent()

    resultado = agent.check_theory(r"Se confirma $P(A|G_B)=1/3$ y $P(C|G_B)=2/3$.")

    assert resultado["invariantes_violados"] == []


def test_probabilidad_como_producto_no_es_falso_positivo():
    """Regresión: `$P(X = 2) = 190 \\times 0.0025 \\times ...$` (UNIDAD 3,
    binomial) leía "190" como el valor final."""
    agent = ScientistAgent()

    resultado = agent.check_theory(
        r"$$\boxed{P(X = 2) = 190 \times 0.0025 \times 0.397214 \approx 0.18868}$$"
    )

    assert resultado["invariantes_violados"] == []


def test_coeficiente_que_multiplica_una_probabilidad_no_es_falso_positivo():
    """Regresión: `p-valor = 2 \\cdot P(Z < -2.55)` (UNIDAD 7) leía el
    coeficiente 2 como si fuera una probabilidad declarada."""
    agent = ScientistAgent()

    resultado = agent.check_theory(
        r"$$\text{p-valor} = 2 \cdot P(Z < -2.55) = 2 \cdot 0.00539 \approx \boxed{0.0108}$$"
    )

    assert resultado["invariantes_violados"] == []
