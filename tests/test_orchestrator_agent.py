"""
Tests for OrchestratorAgent.run_full_pipeline con enforce_gate.
"""

import os
import shutil
import tempfile

import pytest

from src.multiagent_core.orchestrator_agent import OrchestratorAgent

UNIDAD_2_CONTENIDO_MEZCLADO = """# UNIDAD 2 PROBABILIDAD COMBINATORIA
## Asignatura: Probabilidad y Estadística Inferencial

---

## 1. Contenido equivocado
Esta unidad menciona por error una Prueba de Hipótesis y Rechazar H_0,
lo cual pertenece a unidades posteriores del curso, no a Probabilidad.
""" + ("relleno " * 850)

UNIDAD_1_CONTENIDO_OK = (
    """# UNIDAD 1 ESTADISTICA DESCRIPTIVA
## Asignatura: Probabilidad y Estadística Inferencial

---

## 1. Fundamentación Teórica y Conceptos Clave
"""
    + ("teoría descriptiva " * 850)
    + """

$$\\boxed{\\bar{x} = 10.0}$$

$$\\mu = \\frac{1}{n}\\sum_{i=1}^{n} x_i$$

$$\\sigma^2 = \\frac{1}{n}\\sum_{i=1}^{n} (x_i - \\mu)^2$$

$$\\sigma = \\sqrt{\\sigma^2}$$

$$CV = \\frac{\\sigma}{\\mu}$$

```python
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

plt.plot([1, 2, 3])
sns.histplot([1, 2, 3])
```

Interpretación y diccionario de variables de nanotecnología con nanopartículas.
"""
)


@pytest.fixture
def temp_lecciones_dir():
    tmp_dir = tempfile.mkdtemp()
    lecciones_dir = os.path.join(tmp_dir, "lecciones")
    notebooks_dir = os.path.join(tmp_dir, "notebooks")
    os.makedirs(lecciones_dir)

    with open(
        os.path.join(lecciones_dir, "UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(UNIDAD_1_CONTENIDO_OK)
    with open(
        os.path.join(lecciones_dir, "UNIDAD_2_PROBABILIDAD_COMBINATORIA.md"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(UNIDAD_2_CONTENIDO_MEZCLADO)

    yield lecciones_dir, notebooks_dir
    shutil.rmtree(tmp_dir)


def test_enforce_gate_true_blocks_critical_unit(temp_lecciones_dir):
    lecciones_dir, notebooks_dir = temp_lecciones_dir
    orchestrator = OrchestratorAgent(
        lecciones_dir=lecciones_dir, notebooks_dir=notebooks_dir
    )

    results = orchestrator.run_full_pipeline(enforce_gate=True)

    by_file = {os.path.basename(r["md_filename"]): r for r in results}
    u2_result = by_file["UNIDAD_2_PROBABILIDAD_COMBINATORIA.md"]
    u1_result = by_file["UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md"]

    assert u2_result["gate_blocked"] is True
    assert u2_result["gate_reason"] != ""
    assert not os.path.exists(
        os.path.join(notebooks_dir, "UNIDAD_2_PROBABILIDAD_COMBINATORIA.ipynb")
    )

    assert u1_result["gate_blocked"] is False
    assert os.path.exists(
        os.path.join(notebooks_dir, "UNIDAD_1_ESTADISTICA_DESCRIPTIVA.ipynb")
    )


def test_enforce_gate_false_compiles_everything(temp_lecciones_dir):
    lecciones_dir, notebooks_dir = temp_lecciones_dir
    orchestrator = OrchestratorAgent(
        lecciones_dir=lecciones_dir, notebooks_dir=notebooks_dir
    )

    results = orchestrator.run_full_pipeline(enforce_gate=False)

    for r in results:
        assert r["gate_blocked"] is False

    assert os.path.exists(
        os.path.join(notebooks_dir, "UNIDAD_1_ESTADISTICA_DESCRIPTIVA.ipynb")
    )
    assert os.path.exists(
        os.path.join(notebooks_dir, "UNIDAD_2_PROBABILIDAD_COMBINATORIA.ipynb")
    )


def test_generate_curriculum_map_writes_mermaid_file(temp_lecciones_dir):
    lecciones_dir, notebooks_dir = temp_lecciones_dir
    orchestrator = OrchestratorAgent(
        lecciones_dir=lecciones_dir, notebooks_dir=notebooks_dir
    )

    map_path = orchestrator.generate_curriculum_map()

    assert os.path.exists(map_path)
    with open(map_path, encoding="utf-8") as f:
        content = f.read()
    assert "graph LR" in content
    assert "U1" in content


def test_run_full_pipeline_also_generates_curriculum_map(temp_lecciones_dir):
    lecciones_dir, notebooks_dir = temp_lecciones_dir
    orchestrator = OrchestratorAgent(
        lecciones_dir=lecciones_dir, notebooks_dir=notebooks_dir
    )

    orchestrator.run_full_pipeline(enforce_gate=False)

    assert os.path.exists(os.path.join(notebooks_dir, "curriculum_map.mmd"))


def test_orchestrator_uses_council_pipeline_internally():
    from src.multiagent_core.pipeline import CouncilPipeline

    orchestrator = OrchestratorAgent(
        lecciones_dir="lecciones", notebooks_dir="notebooks"
    )
    assert hasattr(orchestrator, "council")
    assert isinstance(orchestrator.council, CouncilPipeline)


UNIDAD_SIN_SCIPY = (
    """# UNIDAD 1 ESTADISTICA DESCRIPTIVA
## Asignatura: Probabilidad y Estadística Inferencial

---

## 1. Fundamentación Teórica y Conceptos Clave
"""
    + ("teoría descriptiva " * 850)
    + """

$$\\boxed{\\bar{x} = 10.0}$$

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.plot([1, 2, 3])
sns.histplot([1, 2, 3])
```

Interpretación y diccionario de variables de nanotecnología con nanopartículas.
"""
)


@pytest.fixture
def temp_lecciones_dir_sin_scipy():
    tmp_dir = tempfile.mkdtemp()
    lecciones_dir = os.path.join(tmp_dir, "lecciones")
    notebooks_dir = os.path.join(tmp_dir, "notebooks")
    os.makedirs(lecciones_dir)

    with open(
        os.path.join(lecciones_dir, "UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(UNIDAD_SIN_SCIPY)

    yield lecciones_dir, notebooks_dir
    shutil.rmtree(tmp_dir)


def test_enforce_gate_blocks_when_engineer_fails(temp_lecciones_dir_sin_scipy):
    lecciones_dir, notebooks_dir = temp_lecciones_dir_sin_scipy
    orchestrator = OrchestratorAgent(
        lecciones_dir=lecciones_dir, notebooks_dir=notebooks_dir
    )

    results = orchestrator.run_full_pipeline(enforce_gate=True)

    u1_result = results[0]
    assert u1_result["gate_blocked"] is True
    assert "engineer" in u1_result["gate_reason"].lower()
    assert not os.path.exists(
        os.path.join(notebooks_dir, "UNIDAD_1_ESTADISTICA_DESCRIPTIVA.ipynb")
    )


def test_check_gate_reason_lists_every_failed_blocking_report():
    """Cuando más de un reporte de _BLOCKING_REPORTS falla a la vez, el
    mensaje de reason debe nombrarlos todos, no solo el primero."""
    orchestrator = OrchestratorAgent(
        lecciones_dir="lecciones", notebooks_dir="notebooks"
    )

    class _StubCouncil:
        def process_content(self, md_text, unit_name=""):
            passing_report = {"passed": True, "critical": False, "warnings": []}
            return {
                "reports": {
                    "safety_gate": {"passed": True, "critical": False},
                    "engineer": {"passed": False},
                    "editor": {"passed": False},
                    "scientist": passing_report,
                    "analyst": passing_report,
                }
            }

    orchestrator.council = _StubCouncil()

    gate_decision = orchestrator._check_gate("UNIDAD_1.md", "texto", set())

    assert gate_decision["blocked"] is True
    assert "engineer" in gate_decision["reason"]
    assert "editor" in gate_decision["reason"]


UNIDAD_2_SOLO_ANACRONISMO = (
    """# UNIDAD 2 PROBABILIDAD COMBINATORIA
## Asignatura: Probabilidad y Estadística Inferencial

---

## 1. Fundamentación Teórica y Conceptos Clave
"""
    + ("teoría de combinatoria y axiomas de Bayes " * 850)
    + """

Esta unidad menciona por error una Prueba de Hipótesis y Rechazar H_0,
lo cual pertenece a unidades posteriores del curso, no a Probabilidad.

$$\\boxed{P(A) = 0.5}$$

$$P(A \\cap B) = P(A)P(B)$$

$$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$$

$$C(n,k) = \\frac{n!}{k!(n-k)!}$$

```python
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

plt.plot([1, 2, 3])
sns.histplot([1, 2, 3])
```

Interpretación y análisis de combinatoria y permutación aplicada a nanopartículas.
"""
)


@pytest.fixture
def temp_lecciones_dir_solo_anacronismo():
    tmp_dir = tempfile.mkdtemp()
    lecciones_dir = os.path.join(tmp_dir, "lecciones")
    notebooks_dir = os.path.join(tmp_dir, "notebooks")
    os.makedirs(lecciones_dir)

    with open(
        os.path.join(lecciones_dir, "UNIDAD_2_PROBABILIDAD_COMBINATORIA.md"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(UNIDAD_2_SOLO_ANACRONISMO)

    yield lecciones_dir, notebooks_dir
    shutil.rmtree(tmp_dir)


def test_enforce_gate_still_blocks_on_safety_gate_critical(
    temp_lecciones_dir_solo_anacronismo,
):
    """Aísla el bloqueo por safety_gate.critical de los 4 reportes nuevos
    (engineer/editor/scientist/analyst) para que el test no dependa
    implícitamente del orden de evaluación en _check_gate: el fixture pasa
    los 4 reportes nuevos y solo falla safety_gate."""
    lecciones_dir, notebooks_dir = temp_lecciones_dir_solo_anacronismo
    orchestrator = OrchestratorAgent(
        lecciones_dir=lecciones_dir, notebooks_dir=notebooks_dir
    )

    results = orchestrator.run_full_pipeline(enforce_gate=True)

    u2_result = results[0]
    assert u2_result["gate_blocked"] is True
    assert "🚨" in u2_result["gate_reason"]
