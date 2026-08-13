"""
Tests for SafetyGateAgent (8 unidades + distincion warning/critico).
"""

import pytest
from src.multiagent_core.council.safety_gate_agent import SafetyGateAgent


@pytest.mark.parametrize("unit_num", range(1, 9))
def test_unit_forbidden_terms_covers_all_8_units(unit_num):
    gate = SafetyGateAgent()
    assert f"UNIDAD {unit_num}" in gate.unit_forbidden_terms


def test_forbidden_term_in_early_unit_is_critical():
    gate = SafetyGateAgent()
    text = "En esta unidad usamos el Error Tipo I para decidir Rechazar H_0."
    result = gate.validate_assumptions(text, "UNIDAD 2")
    assert result["passed"] is False
    assert result["critical"] is True


def test_missing_assumption_warning_is_not_critical():
    gate = SafetyGateAgent()
    text = "Aplicamos t-test sobre los datos de resistencia del nanowire."
    result = gate.validate_assumptions(text, "UNIDAD 3")
    assert result["passed"] is False
    assert result["critical"] is False


def test_unit_required_terms_mismatch_is_critical():
    gate = SafetyGateAgent()
    text = "Esta unidad no menciona ninguno de los temas esperados de probabilidad."
    result = gate.validate_assumptions(text, "UNIDAD 2")
    assert result["critical"] is True


def test_unit_required_terms_present_is_not_critical_for_mismatch():
    gate = SafetyGateAgent()
    text = "Estudiamos combinatoria, permutaciones y el Teorema de Bayes aplicado a nanopartículas."
    result = gate.validate_assumptions(text, "UNIDAD 2")
    assert result["passed"] is True
    assert result["critical"] is False
