"""
Tests for CouncilPipeline.
"""

from src.multiagent_core.pipeline import CouncilPipeline


def test_council_pipeline():
    pipeline = CouncilPipeline()
    sample_text = """# Título de Prueba
""" + "teoría " * 850 + """
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
    sample_text = """# Título de Prueba
""" + "teoría " * 850 + """
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
