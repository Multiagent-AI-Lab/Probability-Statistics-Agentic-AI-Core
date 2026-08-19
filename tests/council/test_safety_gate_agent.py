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


def test_regression_identifier_in_code_block_does_not_trigger_warning():
    gate = SafetyGateAgent()
    text = """
Ajustamos el modelo con scikit-learn.

```python
from sklearn.linear_model import LinearRegression, RANSACRegressor

modelo = LinearRegression().fit(radio_nm, corrimiento_spr)
```
"""
    result = gate.validate_assumptions(text, "UNIDAD 8")
    assert not any("regression" in w.lower() for w in result["warnings"])


def test_regresion_con_supuestos_verificados_en_espanol_no_dispara_warning():
    gate = SafetyGateAgent()
    text = (
        "Antes de aplicar la regresión lineal, verificamos linealidad, "
        "homocedasticidad, independencia de los residuos y normalidad."
    )
    result = gate.validate_assumptions(text, "UNIDAD 8")
    assert not any("regression" in w.lower() for w in result["warnings"])


def test_regresion_en_espanol_sin_supuestos_si_dispara_warning():
    gate = SafetyGateAgent()
    text = "Aplicamos una regresión lineal a los datos de diámetro de nanopartículas."
    result = gate.validate_assumptions(text, "UNIDAD 8")
    assert any("regres" in w.lower() for w in result["warnings"])
    assert result["critical"] is False
