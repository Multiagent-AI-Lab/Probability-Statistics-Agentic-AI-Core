"""Tests for EngineerAgent.check_monte_carlo_convergence (guardrail de convergencia Monte Carlo)."""

from src.multiagent_core.council.engineer_agent import EngineerAgent


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
