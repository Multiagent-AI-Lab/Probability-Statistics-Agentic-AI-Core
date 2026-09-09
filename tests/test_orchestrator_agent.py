"""
Tests for OrchestratorAgent.run_full_pipeline con enforce_gate.
"""

import os
import shutil
import tempfile
from pathlib import Path

import pytest

from src.multiagent_core.orchestrator_agent import OrchestratorAgent

_TODAS_LAS_UNIDADES = [
    "UNIDAD_1_ESTADISTICA_DESCRIPTIVA",
    "UNIDAD_2_PROBABILIDAD_COMBINATORIA",
    "UNIDAD_3_VARIABLES_ALEATORIAS_DISCRETAS",
    "UNIDAD_4_DISTRIBUCIONES_CONJUNTAS",
    "UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS",
    "UNIDAD_6_MODELADO_SIMULACION",
    "UNIDAD_7_INFERENCIA_ESTIMACION",
    "UNIDAD_8_PROYECTO_INTEGRADOR",
]


def _completar_unidades_faltantes(lecciones_dir: str) -> None:
    """Crea un .md vacío por cada unidad del curso que el fixture no haya
    escrito, solo para que @Architect (bloqueante en run_full_pipeline
    desde que se conectó al gate) no bloquee estos tests por completitud
    de curso -- no es lo que estos tests aíslan."""
    existentes = {Path(f).stem for f in os.listdir(lecciones_dir)}
    for unidad in _TODAS_LAS_UNIDADES:
        if unidad in existentes:
            continue
        with open(
            os.path.join(lecciones_dir, f"{unidad}.md"), "w", encoding="utf-8"
        ) as f:
            f.write(f"# {unidad}\n")


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

$$\\mu = \\frac{1}{n}\\sum_{i=1}^{n} x_i$$

$$\\sigma^2 = \\frac{1}{n}\\sum_{i=1}^{n} (x_i - \\mu)^2$$

$$\\sigma = \\sqrt{\\sigma^2}$$

$$CV = \\frac{\\sigma}{\\mu}$$

$$\\boxed{\\bar{x} = 10.0}$$

```python
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

diametros = [8.0, 10.0, 12.0]
print(f"Media: {sum(diametros) / len(diametros):.4f} nm")
plt.plot(diametros)
sns.histplot(diametros)
```

Interpretación: el diámetro medio de las nanopartículas es de 10.0 nm con
una dispersión de 2.0 nm, lo que confirma una síntesis homogénea dentro de
la tolerancia del proceso.

Referencia: DOI: [10.14356/kona.2020011](https://doi.org/10.14356/kona.2020011)
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
    _completar_unidades_faltantes(lecciones_dir)

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


# El código de esta unidad calcula una media de 10.0 nm pero el texto
# encuadra 99.0: es el desajuste texto/código que @Engineer debe atrapar.
# (Antes esta fixture solo omitía la palabra "scipy", que era el criterio
# del agente hasta H-01; ya no basta con mencionar una librería.)
UNIDAD_CON_DESAJUSTE_DE_ENGINEER = (
    """# UNIDAD 1 ESTADISTICA DESCRIPTIVA
## Asignatura: Probabilidad y Estadística Inferencial

---

## 1. Fundamentación Teórica y Conceptos Clave
"""
    + ("teoría descriptiva " * 850)
    + """

$$\\mu = \\frac{1}{n}\\sum_{i=1}^{n} x_i$$

$$\\sigma = \\sqrt{\\sigma^2}$$

## 2. Solución Computacional

```python
import matplotlib.pyplot as plt
import seaborn as sns

diametros = [8.0, 10.0, 12.0]
print(f"Media: {sum(diametros) / len(diametros):.4f} nm")
plt.plot(diametros)
sns.histplot(diametros)
```

El texto afirma un resultado que el código contradice:

$$\\boxed{\\bar{x} = 99.0}$$

Interpretación: el diámetro medio de las nanopartículas es de 10.0 nm con
una dispersión de 2.0 nm, lo que confirma una síntesis homogénea dentro de
la tolerancia del proceso.

Referencia: DOI: [10.14356/kona.2020011](https://doi.org/10.14356/kona.2020011)
"""
)


@pytest.fixture
def temp_lecciones_dir_con_desajuste_de_engineer():
    tmp_dir = tempfile.mkdtemp()
    lecciones_dir = os.path.join(tmp_dir, "lecciones")
    notebooks_dir = os.path.join(tmp_dir, "notebooks")
    os.makedirs(lecciones_dir)

    with open(
        os.path.join(lecciones_dir, "UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(UNIDAD_CON_DESAJUSTE_DE_ENGINEER)
    _completar_unidades_faltantes(lecciones_dir)

    yield lecciones_dir, notebooks_dir
    shutil.rmtree(tmp_dir)


def test_enforce_gate_blocks_when_engineer_fails(
    temp_lecciones_dir_con_desajuste_de_engineer,
):
    lecciones_dir, notebooks_dir = temp_lecciones_dir_con_desajuste_de_engineer
    orchestrator = OrchestratorAgent(
        lecciones_dir=lecciones_dir, notebooks_dir=notebooks_dir
    )

    results = orchestrator.run_full_pipeline(enforce_gate=True)

    by_file = {os.path.basename(r["md_filename"]): r for r in results}
    u1_result = by_file["UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md"]
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
        def process_content(self, md_text, unit_name="", file_tree=None):
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


def test_check_gate_reason_incluye_detalle_numerico_de_scientist_y_analyst():
    """El mensaje de reason debe incluir el detalle que causó el fallo
    (word_count/math_equation_count de scientist, plot_count de analyst),
    no solo el nombre del agente -- para que quien depure localmente sepa
    qué corregir sin tener que re-ejecutar el pipeline manualmente."""
    orchestrator = OrchestratorAgent(
        lecciones_dir="lecciones", notebooks_dir="notebooks"
    )

    class _StubCouncil:
        def process_content(self, md_text, unit_name="", file_tree=None):
            return {
                "reports": {
                    "safety_gate": {"passed": True, "critical": False},
                    "engineer": {"passed": True},
                    "editor": {"passed": True},
                    "scientist": {
                        "passed": False,
                        "word_count": 120,
                        "math_equation_count": 2,
                    },
                    "analyst": {
                        "passed": False,
                        "plot_count": 0,
                        "has_interpretation": False,
                    },
                }
            }

    orchestrator.council = _StubCouncil()

    gate_decision = orchestrator._check_gate("UNIDAD_1.md", "texto", set())

    assert gate_decision["blocked"] is True
    assert "120" in gate_decision["reason"]
    assert "2" in gate_decision["reason"]
    assert "0" in gate_decision["reason"]


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


@pytest.fixture
def temp_lecciones_dir_incompleto():
    """Solo UNIDAD_1 presente -- @Architect debe reportar 7 unidades
    faltantes cuando run_full_pipeline le pasa el file_tree real."""
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

    yield lecciones_dir, notebooks_dir
    shutil.rmtree(tmp_dir)


def test_run_full_pipeline_bloquea_por_architect_cuando_faltan_unidades(
    temp_lecciones_dir_incompleto,
):
    """run_full_pipeline conoce el listado completo de .md del directorio,
    a diferencia de process_content() invocado aislado por lección -- por
    eso es el único caller que puede pasarle file_tree real a @Architect
    sin el falso-bloqueo que describe GOVERNANCE.md §2.1 (una unidad válida
    bloqueada solo porque otra no está presente en ese momento: aquí SÍ
    faltan de verdad, así que el bloqueo es la señal correcta)."""
    lecciones_dir, notebooks_dir = temp_lecciones_dir_incompleto
    orchestrator = OrchestratorAgent(
        lecciones_dir=lecciones_dir, notebooks_dir=notebooks_dir
    )

    results = orchestrator.run_full_pipeline(enforce_gate=True)

    u1_result = results[0]
    assert u1_result["gate_blocked"] is True
    assert "architect" in u1_result["gate_reason"].lower()
    assert not os.path.exists(
        os.path.join(notebooks_dir, "UNIDAD_1_ESTADISTICA_DESCRIPTIVA.ipynb")
    )


def test_ninguna_leccion_real_del_curso_es_bloqueada_por_el_gate():
    """Gate de no-regresión: corre el pipeline real (enforce_gate=True) sobre
    las 8 lecciones reales del curso en lecciones/, no sobre fixtures
    sintéticas. Si una edición futura hace caer alguna lección por debajo de
    los umbrales de engineer/editor/scientist/analyst/safety_gate, este test
    debe fallar antes de que el contenido se publique — detalle en
    GOVERNANCE.md §2.1.

    Las rutas se anclan a este archivo (no a strings relativos al cwd de
    pytest) para que el test sea robusto sin importar desde dónde se invoque.

    UNIDAD 6 y UNIDAD 7 ya no están excluidas: Task 2 corrigió los bugs de
    contenido que las bloqueaban a propósito (H-05 en U6: la celda SymPy
    ahora resuelve la forma simplificada consistente con el texto; H-02 en
    U7: la $d$ de Cohen usa la media muestral real). Las 8 unidades deben
    aprobar el gate por igual — `tests/council/test_adversarial.py` verifica
    en cambio que el Consejo detectaba esos bugs mientras existieron (los
    tests de detección ahí se invirtieron a `approved is True` junto con
    este cambio)."""
    repo_root = Path(__file__).resolve().parent.parent
    orchestrator = OrchestratorAgent(
        lecciones_dir=str(repo_root / "lecciones"),
        notebooks_dir=str(repo_root / "notebooks"),
    )

    results = orchestrator.run_full_pipeline(enforce_gate=True)

    assert len(results) == 8, "Se esperan exactamente las 8 lecciones del curso"

    bloqueadas = [
        (r["md_filename"], r["gate_reason"]) for r in results if r["gate_blocked"]
    ]
    assert bloqueadas == [], (
        "El gate real bloquea contenido ya publicado del curso: " f"{bloqueadas}"
    )


# ---------------------------------------------------------------------------
# C-1: el veredicto agregado de @QA debe gobernar el gate de producción.
#
# Antes de este fix, `_check_gate` leía `reports[name]["passed"]` de solo 4
# agentes (_BLOCKING_REPORTS) y nunca consultaba `final_qa["approved"]`. Toda
# la maquinaria de hallazgos tipados de @QA —y la reescritura completa de
# @Librarian, que ni siquiera estaba en esa tupla— quedaba inerte para el
# pipeline real: una unidad podía citar un DOI que no resuelve en Crossref y
# publicarse igual.
# ---------------------------------------------------------------------------


class _StubCouncilConQA:
    """Consejo de prueba que devuelve reportes fijos y delega el veredicto
    agregado en el @QA real, igual que `CouncilPipeline.process_content`."""

    def __init__(self, reports):
        self._reports = reports
        from src.multiagent_core.council.qa_agent import QAAgent

        self._qa = QAAgent()

    def process_content(self, md_text, unit_name="", file_tree=None):
        final_qa = self._qa.final_audit(self._reports)
        return {
            "approved": final_qa["approved"],
            "reports": self._reports,
            "final_qa": final_qa,
        }


def _reportes_todos_ok():
    ok = {"passed": True}
    return {
        "safety_gate": {"passed": True, "critical": False, "warnings": []},
        "engineer": dict(ok),
        "editor": dict(ok),
        "scientist": dict(ok),
        "analyst": dict(ok),
        "librarian": {
            "passed": True,
            "has_references": True,
            "dois_verificados": ["10.1000/valido"],
            "dois_no_resueltos": [],
        },
    }


def test_gate_bloquea_cuando_librarian_reporta_un_doi_que_no_resuelve():
    """C-1 (RED antes del fix): `librarian` no está en _BLOCKING_REPORTS, así
    que un DOI que no resuelve en Crossref no bloqueaba la publicación aunque
    @QA lo clasificara como hallazgo bloqueante `referencia_inexistente`."""
    orchestrator = OrchestratorAgent(
        lecciones_dir="lecciones", notebooks_dir="notebooks"
    )

    reports = _reportes_todos_ok()
    reports["librarian"] = {
        "passed": False,
        "has_references": True,
        "dois_verificados": [],
        "dois_no_resueltos": ["10.9999/doi-inexistente"],
    }
    orchestrator.council = _StubCouncilConQA(reports)

    gate_decision = orchestrator._check_gate("UNIDAD_1.md", "texto", set())

    assert gate_decision["blocked"] is True, (
        "un DOI que no resuelve debe bloquear la publicación real, no solo "
        "aparecer como metadato del reporte de @Librarian"
    )
    assert "10.9999/doi-inexistente" in gate_decision["reason"]


def test_gate_bloquea_cuando_qa_reprueba_por_un_hallazgo_tipado():
    """C-1 (RED antes del fix): un agente que SÍ está en _BLOCKING_REPORTS
    puede devolver `passed: True` y aun así aportar un hallazgo bloqueante
    tipado (invariante violado). El gate debe leer el veredicto agregado de
    @QA, no el booleano crudo de cada agente."""
    orchestrator = OrchestratorAgent(
        lecciones_dir="lecciones", notebooks_dir="notebooks"
    )

    reports = _reportes_todos_ok()
    reports["scientist"] = {
        "passed": True,
        "invariantes_violados": ["probabilidad fuera de [0,1]: 1.75"],
    }
    orchestrator.council = _StubCouncilConQA(reports)

    gate_decision = orchestrator._check_gate("UNIDAD_1.md", "texto", set())

    assert gate_decision["blocked"] is True, (
        "@QA marcó approved=False por un hallazgo bloqueante; el gate de "
        "producción debe bloquear igual que si fallara un _BLOCKING_REPORTS"
    )
    assert "1.75" in gate_decision["reason"]


def test_gate_no_bloquea_por_advertencias_no_bloqueantes_de_qa():
    """Contraparte: una advertencia (supuesto estadístico sin verificar) no
    debe convertirse en un gate de publicación. El fix conecta el veredicto
    de @QA, que ya distingue severidades — no endurece el gate a cualquier
    hallazgo."""
    orchestrator = OrchestratorAgent(
        lecciones_dir="lecciones", notebooks_dir="notebooks"
    )

    reports = _reportes_todos_ok()
    reports["safety_gate"] = {
        "passed": True,
        "critical": False,
        "warnings": ["no se verificó normalidad antes de la prueba t"],
    }
    orchestrator.council = _StubCouncilConQA(reports)

    gate_decision = orchestrator._check_gate("UNIDAD_1.md", "texto", set())

    assert gate_decision["blocked"] is False, gate_decision["reason"]
