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
