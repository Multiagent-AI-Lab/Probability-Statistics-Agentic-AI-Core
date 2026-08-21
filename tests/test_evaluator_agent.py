"""
Tests para EvaluatorAgent.evaluate_notebook -- rúbrica de 4 criterios
(rigor teórico, excelencia de código, visualización, interpretación nano).
"""

from src.multiagent_core.evaluator_agent import EvaluatorAgent


def test_notebook_completo_aprueba_con_score_alto():
    agent = EvaluatorAgent()
    audit_results = {"score": 100.0, "metrics": {"has_plots": True}}
    content_results = {
        "total_words": 1000,
        "component_checks": {
            "Visualización Profesional": True,
            "Contexto Nanotecnológico": True,
        },
    }

    resultado = agent.evaluate_notebook(audit_results, content_results)

    assert resultado["passed"] is True
    assert resultado["total_score"] == 100.0
    assert resultado["feedback"] == []


def test_notebook_vacio_no_aprueba_y_da_feedback_de_lo_que_falta():
    """audit_results.get("score", 100.0) defaultea a 100.0 -- un dict vacío
    no penaliza excelencia_codigo (asume código correcto por ausencia de
    auditoría), así que solo rigor/visualización/nano generan feedback."""
    agent = EvaluatorAgent()

    resultado = agent.evaluate_notebook({}, {})

    assert resultado["passed"] is False
    assert len(resultado["feedback"]) == 3
    assert resultado["category_scores"]["excelencia_codigo"] == 25.0


def test_rigor_teorico_se_limita_a_25_puntos_maximo():
    agent = EvaluatorAgent()
    content_results = {"total_words": 5000}

    resultado = agent.evaluate_notebook({}, content_results)

    assert resultado["category_scores"]["rigor_teorico"] == 25.0


def test_sin_graficos_ni_contexto_nano_da_feedback_especifico():
    agent = EvaluatorAgent()

    resultado = agent.evaluate_notebook({}, {})

    assert any("gráficos" in msg for msg in resultado["feedback"])
    assert any("Nanotecnología" in msg for msg in resultado["feedback"])


def test_has_plots_desde_audit_results_cuenta_igual_que_desde_content_results():
    agent = EvaluatorAgent()

    resultado_por_audit = agent.evaluate_notebook({"metrics": {"has_plots": True}}, {})
    resultado_por_content = agent.evaluate_notebook(
        {}, {"component_checks": {"Visualización Profesional": True}}
    )

    assert (
        resultado_por_audit["category_scores"]["visualizacion_datos"]
        == resultado_por_content["category_scores"]["visualizacion_datos"]
        == 25.0
    )
