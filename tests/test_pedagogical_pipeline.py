"""
Tests for PedagogicalReviewPipeline and EvaluatorCriticAgent.
"""

from src.multiagent_core.pedagogical_pipeline import PedagogicalReviewPipeline


def test_pedagogical_review_pipeline():
    pipeline = PedagogicalReviewPipeline()
    sample_lesson = """# UNIDAD DE PRUEBA GENERICA
## Asignatura: Probabilidad y Estadística Inferencial
### UCEMICH — Ingeniería en IA y Nanotecnología
### Autor y Profesor: Mtro. Luis José Yudico Anaya

---

## 1. Fundamentación Teórica y Conceptos Clave
""" + "teoría estadística " * 900 + """

$$\\boxed{\\bar{x} = 10.0}$$

```python
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import sympy as sp

# Prueba t de Student con verificación de normalidad por Shapiro-Wilk
data = [12.1, 13.4, 11.8, 12.9, 13.1]
stats.shapiro(data)
stats.ttest_1samp(data, 12.0)
plt.plot(data)
sns.histplot(data)
```

Interpretación post-gráfico y diccionario de variables nanotecnológicas.
"""
    report = pipeline.review_and_auto_fix_lesson(sample_lesson, "Unidad Genérica Test")

    assert "synthesis" in report
    assert report["synthesis"]["coherence_score"] >= 80.0
    assert len(report["synthesis"]["critiques"]) >= 4


def test_critical_block_true_when_safety_gate_critical():
    pipeline = PedagogicalReviewPipeline()
    sample_lesson = """# UNIDAD 2 PROBABILIDAD Y COMBINATORIA
## Asignatura: Probabilidad y Estadística Inferencial
### UCEMICH — Ingeniería en IA y Nanotecnología
### Autor y Profesor: Mtro. Luis José Yudico Anaya

---

## 1. Fundamentación Teórica y Conceptos Clave
""" + "teoría estadística " * 900 + """

$$\\boxed{\\bar{x} = 10.0}$$

```python
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import sympy as sp

# Prueba t de Student con verificación de normalidad por Shapiro-Wilk
data = [12.1, 13.4, 11.8, 12.9, 13.1]
stats.shapiro(data)
stats.ttest_1samp(data, 12.0)
plt.plot(data)
sns.histplot(data)
```

Interpretación post-gráfico y diccionario de variables nanotecnológicas.
"""
    report = pipeline.review_and_auto_fix_lesson(sample_lesson, "UNIDAD 2")

    assert "critical_block" in report
    assert report["critical_block"] is True


def test_critical_block_false_when_no_safety_issues():
    pipeline = PedagogicalReviewPipeline()
    sample_lesson = """# UNIDAD DE PRUEBA GENERICA
## Asignatura: Probabilidad y Estadística Inferencial
### UCEMICH — Ingeniería en IA y Nanotecnología
### Autor y Profesor: Mtro. Luis José Yudico Anaya

---

## 1. Fundamentación Teórica y Conceptos Clave
""" + "teoría estadística " * 900 + """

$$\\boxed{\\bar{x} = 10.0}$$

```python
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import sympy as sp

data = [12.1, 13.4, 11.8, 12.9, 13.1]
plt.plot(data)
sns.histplot(data)
```

Interpretación post-gráfico y diccionario de variables nanotecnológicas.
"""
    report = pipeline.review_and_auto_fix_lesson(sample_lesson, "Unidad Genérica Test")

    assert report["critical_block"] is False


def test_pedagogical_pipeline_uses_council_internally():
    from src.multiagent_core.pipeline import CouncilPipeline

    pipeline = PedagogicalReviewPipeline()
    assert hasattr(pipeline, "council")
    assert isinstance(pipeline.council, CouncilPipeline)

