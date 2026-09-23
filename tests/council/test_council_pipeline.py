"""
Tests for CouncilPipeline.
"""

from unittest.mock import patch

from src.multiagent_core.pipeline import CouncilPipeline


def test_council_pipeline():
    pipeline = CouncilPipeline()
    sample_text = (
        """# Título de Prueba
"""
        + "teoría " * 850
        + """
$$\\boxed{E = mc^2}$$

```python
import scipy.stats as stats
from IPython.display import display, Math
import matplotlib.pyplot as plt
import seaborn as sns

data = [1, 2, 3, 4, 5]
stats.shapiro(data)
plt.plot(data)
sns.histplot(data)
display(Math(r'\\bar{x} = 3.0'))
```
Interpretación y análisis nanotecnológico con referencia a Walpole.
"""
    )
    res = pipeline.process_content(sample_text)
    assert "reports" in res
    assert "final_qa" in res


def test_council_pipeline_invokes_all_8_agents():
    pipeline = CouncilPipeline()
    assert hasattr(pipeline, "architect")
    assert hasattr(pipeline, "scientist")
    assert hasattr(pipeline, "engineer")
    assert hasattr(pipeline, "safety_gate")
    assert hasattr(pipeline, "analyst")
    assert hasattr(pipeline, "librarian")
    assert hasattr(pipeline, "qa")
    assert hasattr(pipeline, "editor")


def test_council_pipeline_reports_include_architect_and_editor():
    pipeline = CouncilPipeline()
    sample_text = (
        """# Título de Prueba
"""
        + "teoría " * 850
        + """
$$\\boxed{E = mc^2}$$

```python
import scipy.stats as stats
from IPython.display import display, Math
import matplotlib.pyplot as plt
import seaborn as sns

data = [1, 2, 3, 4, 5]
stats.shapiro(data)
plt.plot(data)
sns.histplot(data)
display(Math(r'\\bar{x} = 3.0'))
```
Interpretación y análisis nanotecnológico con referencia a Walpole.
"""
    )
    res = pipeline.process_content(sample_text)
    assert "architect" in res["reports"]
    assert "editor" in res["reports"]


def test_council_pipeline_propagates_unit_name_to_safety_gate():
    """Sin unit_name, SafetyGateAgent no puede evaluar secuencia curricular
    (checks 2/3 de validate_assumptions dependen de matchear unit_name contra
    el texto) — regresión del bug detectado en pipeline.py antes de esta task."""
    pipeline = CouncilPipeline()
    texto_con_anacronismo = (
        "# UNIDAD 2 PROBABILIDAD COMBINATORIA\n\n"
        + "Esta unidad menciona por error una Prueba de Hipótesis y Rechazar H_0.\n"
        + ("relleno " * 850)
    )
    res = pipeline.process_content(texto_con_anacronismo, unit_name="UNIDAD 2")
    assert res["reports"]["safety_gate"]["critical"] is True


def test_council_pipeline_blocks_on_low_monte_carlo_iterations():
    """El guardrail de convergencia Monte Carlo de EngineerAgent debe conectarse
    a la decision final del pipeline: N_sim bajo => eng_res["passed"] False =>
    approved False vía QAAgent.final_audit (regresión del hallazgo de review
    final: check_monte_carlo_convergence existía pero nunca se invocaba)."""
    pipeline = CouncilPipeline()
    sample_text = (
        """# Título de Prueba
"""
        + "teoría " * 850
        + """
$$\\boxed{E = mc^2}$$

```python
import scipy.stats as stats
from IPython.display import display, Math
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

N_sim = 50
data = np.random.normal(size=N_sim)
stats.shapiro(data)
plt.plot(data)
sns.histplot(data)
display(Math(r'\\bar{x} = 3.0'))
```
Interpretación y análisis nanotecnológico con referencia a Walpole.
"""
    )
    res = pipeline.process_content(sample_text)
    assert res["reports"]["engineer"]["passed"] is False
    assert len(res["reports"]["engineer"]["monte_carlo_warnings"]) > 0
    assert res["approved"] is False


def test_semantic_auditor_no_corre_sin_la_variable_de_entorno(monkeypatch):
    """AUDITAR_SEMANTICA ausente (default de producción y de CI) --
    process_content NO debe invocar a SemanticAuditorAgent ni agregar
    "semantic" a reports."""
    monkeypatch.delenv("AUDITAR_SEMANTICA", raising=False)
    pipeline = CouncilPipeline()
    texto = "Palabra " * 850 + "\n\n$$X = 5$$"

    resultado = pipeline.process_content(texto, unit_name="TEST")

    assert "semantic" not in resultado["reports"]


def test_semantic_auditor_corre_si_la_variable_de_entorno_esta_activa(monkeypatch):
    monkeypatch.setenv("AUDITAR_SEMANTICA", "1")
    monkeypatch.setenv("GEMINI_API_KEY", "fake-key")
    pipeline = CouncilPipeline()
    texto = "Palabra " * 850 + "\n\n$$X = 5$$"

    with patch(
        "src.multiagent_core.council.semantic_auditor_agent.llamar_juez_semantico",
        return_value="SIN_INVERSIONES",
    ):
        resultado = pipeline.process_content(texto, unit_name="TEST")

    assert "semantic" in resultado["reports"]
    assert resultado["reports"]["semantic"]["passed"] is True
