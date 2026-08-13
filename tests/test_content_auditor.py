"""
Tests for ContentAuditorAgent.
"""

from src.multiagent_core.content_auditor_agent import ContentAuditorAgent


def test_content_auditor():
    auditor = ContentAuditorAgent()
    nano_paragraph = (
        "En este problema aplicado a nanotecnología estudiamos el comportamiento "
        "de nanopartículas de oro dispersas en una solución coloidal. " * 15
    )
    sample_text = """# Teoría Completa
""" + "palabra " * 850 + f"""

## Ejemplo Analítico Paso a Paso
El paso 1 consiste en calcular el potencial zeta de nanopartículas de oro.
{nano_paragraph}
La solución final es \\boxed{{42.0}}.

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


def test_nano_context_fails_when_mention_is_too_short():
    auditor = ContentAuditorAgent()
    sample_text = """# Teoría Completa
""" + "palabra " * 850 + """

## Ejemplo Analítico Paso a Paso
El paso 1 consiste en calcular algo. La solución final es \\boxed{42.0}.
Mencion breve de nanopartículas sin desarrollo real del contexto aplicado.

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
    assert res["component_checks"]["Contexto Nanotecnológico"] is False


def test_nano_context_passes_with_150_plus_words():
    auditor = ContentAuditorAgent()
    nano_paragraph = (
        "En este problema aplicado a nanotecnología estudiamos el comportamiento "
        "de nanopartículas de oro dispersas en una solución coloidal. " * 15
    )
    sample_text = """# Teoría Completa
""" + "palabra " * 850 + f"""

## Ejemplo Analítico Paso a Paso
El paso 1 consiste en calcular el potencial zeta de nanopartículas de oro.
{nano_paragraph}
La solución final es \\boxed{{42.0}}.

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
    assert res["component_checks"]["Contexto Nanotecnológico"] is True

