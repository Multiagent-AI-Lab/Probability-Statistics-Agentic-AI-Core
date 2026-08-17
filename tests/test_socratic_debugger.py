"""Tests for SocraticDebugger extendido con errores de código de estudiante."""

from external_skills.pedagogy.socratic_debugger import SocraticDebugger


def test_genera_pregunta_para_zerodivisionerror():
    debugger = SocraticDebugger()
    pregunta = debugger.generate_socratic_question("zerodivisionerror", "Unidad 1")
    assert "?" in pregunta
    assert len(pregunta) > 20
    assert "divid" in pregunta.lower()


def test_genera_pregunta_para_syntax_error_scipy():
    debugger = SocraticDebugger()
    pregunta = debugger.generate_socratic_question("syntax_error", "Unidad 3")
    assert "?" in pregunta
    assert "scipy" in pregunta.lower()


def test_tipos_existentes_no_se_rompen():
    debugger = SocraticDebugger()
    assert "?" in debugger.generate_socratic_question("normality", "Unidad 7")
    assert "?" in debugger.generate_socratic_question("p_value", "Unidad 7")
    assert "?" in debugger.generate_socratic_question("variance", "Unidad 1")


def test_tipo_desconocido_usa_fallback_generico():
    debugger = SocraticDebugger()
    pregunta = debugger.generate_socratic_question("tipo_inexistente", "Unidad 5")
    assert "?" in pregunta
