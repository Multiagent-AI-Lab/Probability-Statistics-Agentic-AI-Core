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


def test_orchestrator_uses_council_pipeline_internally():
    from src.multiagent_core.pipeline import CouncilPipeline

    orchestrator = OrchestratorAgent(
        lecciones_dir="lecciones", notebooks_dir="notebooks"
    )
    assert hasattr(orchestrator, "council")
    assert isinstance(orchestrator.council, CouncilPipeline)
