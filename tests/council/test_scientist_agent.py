"""
Tests para ScientistAgent.check_theory -- rigor matemático y notación LaTeX.
"""

from src.multiagent_core.council.scientist_agent import ScientistAgent


def test_pasa_con_suficientes_palabras_y_formulas():
    agent = ScientistAgent()
    texto = (
        ("teoría estadística " * 400)
        + "$$\\mu = 1$$ " * 5
        + r"\begin{align} x \end{align}"
    )

    resultado = agent.check_theory(texto)

    assert resultado["word_count"] >= 800
    assert resultado["passed"] is True


def test_falla_por_pocas_palabras_aunque_tenga_formulas_suficientes():
    agent = ScientistAgent()
    texto = "$$x$$ " * 10

    resultado = agent.check_theory(texto)

    assert resultado["word_count"] < 800
    assert resultado["passed"] is False


def test_falla_por_pocas_formulas_aunque_tenga_palabras_suficientes():
    agent = ScientistAgent()
    texto = "teoría sin ninguna fórmula matemática " * 100

    resultado = agent.check_theory(texto)

    assert resultado["math_equation_count"] < 10
    assert resultado["passed"] is False


def test_detecta_solucion_boxed():
    agent = ScientistAgent()
    texto = r"\boxed{x = 1}"

    resultado = agent.check_theory(texto)

    assert resultado["has_boxed_solution"] is True


def test_no_detecta_boxed_si_no_esta_presente():
    agent = ScientistAgent()

    resultado = agent.check_theory("texto sin solución encuadrada")

    assert resultado["has_boxed_solution"] is False
