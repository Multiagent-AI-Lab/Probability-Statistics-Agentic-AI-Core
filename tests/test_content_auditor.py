"""
Tests for ContentAuditorAgent.
"""

from src.multiagent_core.content_auditor_agent import ContentAuditorAgent


def test_content_auditor():
    auditor = ContentAuditorAgent()
    sample_text = """# Teoría Completa
""" + "palabra " * 850 + """

## Ejemplo Analítico Paso a Paso
El paso 1 consiste en calcular el potencial zeta de nanopartículas de oro.
La solución final es \\boxed{42.0}.

```python
import sympy as sp
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure()
sns.histplot([1, 2, 3])
plt.figure()
sns.boxplot([1, 2, 3])
```

## Interpretación y Diccionario de Variables
Interpretación detallada del modelo estadístico.
"""
    res = auditor.audit_content(sample_text)
    assert res["passed"] is True
    assert res["component_checks"]["Teoría Completa"] is True
    assert res["component_checks"]["Contexto Nanotecnológico"] is True
