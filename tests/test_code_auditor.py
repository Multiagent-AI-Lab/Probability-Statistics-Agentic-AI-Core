"""
Tests for CodeAuditorAgent.
"""

from src.multiagent_core.code_auditor_agent import CodeAuditorAgent


def test_code_auditor_clean():
    auditor = CodeAuditorAgent()
    code = """
import numpy as np
import scipy.stats as stats
from IPython.display import display, Math

mu, sigma = 10, 2
display(Math(rf'\\mu = {mu}, \\sigma = {sigma}'))
"""
    res = auditor.audit_code(code)
    assert res["passed"] is True
    assert res["metrics"]["uses_scipy"] is True
    assert res["metrics"]["uses_display_math"] is True


def test_code_auditor_syntax_error():
    auditor = CodeAuditorAgent()
    code = "def invalid_syntax(: pass"
    res = auditor.audit_code(code)
    assert res["passed"] is False
    assert len(res["issues"]) > 0


def test_detecta_uso_de_eval():
    auditor = CodeAuditorAgent()
    code = """
import scipy.stats as stats
resultado = eval("2 + 2")
"""
    res = auditor.audit_code(code)
    assert res["metrics"]["has_security_risk"] is True
    assert any("eval" in issue.lower() for issue in res["security_issues"])
    assert res["passed"] is False


def test_detecta_uso_de_exec():
    auditor = CodeAuditorAgent()
    code = """
import scipy.stats as stats
exec("x = 1")
"""
    res = auditor.audit_code(code)
    assert res["metrics"]["has_security_risk"] is True
    assert any("exec" in issue.lower() for issue in res["security_issues"])


def test_detecta_credencial_expuesta():
    auditor = CodeAuditorAgent()
    code = """
import scipy.stats as stats
api_key = "sk-abcdef1234567890"
"""
    res = auditor.audit_code(code)
    assert res["metrics"]["has_security_risk"] is True
    assert any("credencial" in issue.lower() or "api_key" in issue.lower() for issue in res["security_issues"])


def test_no_marca_riesgo_con_os_environ():
    auditor = CodeAuditorAgent()
    code = """
import os
import scipy.stats as stats
api_key = os.environ["GEMINI_API_KEY"]
"""
    res = auditor.audit_code(code)
    assert res["metrics"]["has_security_risk"] is False


def test_codigo_limpio_no_reporta_security_issues():
    auditor = CodeAuditorAgent()
    code = """
import numpy as np
import scipy.stats as stats
from IPython.display import display, Math

mu, sigma = 10, 2
display(Math(rf'\\mu = {mu}, \\sigma = {sigma}'))
"""
    res = auditor.audit_code(code)
    assert res["metrics"]["has_security_risk"] is False
    assert res["security_issues"] == []
