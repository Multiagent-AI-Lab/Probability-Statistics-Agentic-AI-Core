"""Tests for SemanticAuditorAgent.check_semantics.

Todos mockean llamar_juez_semantico -- ningún test hace red real
(Global Constraint del plan)."""

from unittest.mock import patch

from src.multiagent_core.council.semantic_auditor_agent import SemanticAuditorAgent


def test_sin_hallazgos_devuelve_passed_true_y_listas_vacias():
    agent = SemanticAuditorAgent()
    prosa = "A mayor varianza, menor confiabilidad del estimador."
    formulas = [r"\text{Var}(\hat{\theta}) \propto \frac{1}{\text{confiabilidad}}"]

    with patch(
        "src.multiagent_core.council.semantic_auditor_agent.llamar_juez_semantico",
        return_value="SIN_INVERSIONES",
    ):
        resultado = agent.check_semantics(prosa, formulas)

    assert resultado["passed"] is True
    assert resultado["inversiones_semanticas"] == []
    assert resultado["auditoria_incompleta"] is False


def test_inversion_semantica_detectada_no_bloquea_passed():
    """Important de diseño (Global Constraint): passed debe seguir True
    aunque haya hallazgos semánticos -- son severidad advertencia, y
    passed=False sin hallazgos tipados dispararía la red de seguridad
    bloqueante de qa_agent.py (líneas 183-191)."""
    agent = SemanticAuditorAgent()
    prosa = "A mayor varianza, mayor confiabilidad del estimador."
    formulas = [r"\text{Var}(\hat{\theta}) \propto \frac{1}{\text{confiabilidad}}"]

    respuesta_llm = (
        "INVERSION: La prosa afirma que a mayor varianza hay mayor "
        "confiabilidad, pero la fórmula muestra relación inversa."
    )
    with patch(
        "src.multiagent_core.council.semantic_auditor_agent.llamar_juez_semantico",
        return_value=respuesta_llm,
    ):
        resultado = agent.check_semantics(prosa, formulas)

    assert resultado["passed"] is True
    assert len(resultado["inversiones_semanticas"]) == 1
    assert (
        "confiabilidad" in resultado["inversiones_semanticas"][0]["afirmacion"]
        or "confiabilidad" in resultado["inversiones_semanticas"][0]["explicacion"]
    )


def test_sin_formulas_validadas_no_evalua_inversion_semantica():
    """Sin ancla (ninguna fórmula ya validada en la sección), no hay
    contra qué contrastar la prosa -- se abstiene, no llama al LLM para
    ese chequeo (ahorra costo y evita que el LLM invente su propio
    criterio de qué es correcto)."""
    agent = SemanticAuditorAgent()

    with patch(
        "src.multiagent_core.council.semantic_auditor_agent.llamar_juez_semantico"
    ) as mock_llm:
        resultado = agent.check_semantics("Alguna prosa sin fórmulas cerca.", [])

    mock_llm.assert_not_called()
    assert resultado["inversiones_semanticas"] == []


def test_constante_falsa_detectada_contra_tabla_curada():
    agent = SemanticAuditorAgent()
    prosa = "La constante de Boltzmann vale 1.602e-19 J/K."

    resultado = agent.check_semantics(prosa, [])

    assert resultado["passed"] is True
    assert len(resultado["afirmaciones_no_verificables"]) == 1
    hallazgo = resultado["afirmaciones_no_verificables"][0]
    assert hallazgo["constante"] == "constante de boltzmann"
    assert abs(hallazgo["valor_afirmado"] - 1.602e-19) < 1e-25
    assert abs(hallazgo["valor_real"] - 1.380649e-23) < 1e-28


def test_constante_correcta_no_genera_hallazgo():
    agent = SemanticAuditorAgent()
    prosa = "La constante de Boltzmann vale 1.380649e-23 J/K."

    resultado = agent.check_semantics(prosa, [])

    assert resultado["afirmaciones_no_verificables"] == []


def test_constante_no_catalogada_se_ignora_sin_llamar_al_llm():
    agent = SemanticAuditorAgent()
    prosa = "La constante gravitacional vale 6.674e-11."

    with patch(
        "src.multiagent_core.council.semantic_auditor_agent.llamar_juez_semantico",
        return_value="SIN_INVERSIONES",
    ):
        resultado = agent.check_semantics(prosa, [])

    assert resultado["afirmaciones_no_verificables"] == []


def test_fallo_del_llm_activa_fail_open():
    """Global Constraint: un error de infraestructura nunca se reporta
    como si fuera un hallazgo de contenido."""
    agent = SemanticAuditorAgent()
    prosa = "A mayor varianza, menor confiabilidad."
    formulas = [r"\text{Var}(\hat{\theta}) \propto \frac{1}{\text{confiabilidad}}"]

    with patch(
        "src.multiagent_core.council.semantic_auditor_agent.llamar_juez_semantico",
        return_value=None,
    ):
        resultado = agent.check_semantics(prosa, formulas)

    assert resultado["passed"] is True
    assert resultado["auditoria_incompleta"] is True
    assert resultado["inversiones_semanticas"] == []
