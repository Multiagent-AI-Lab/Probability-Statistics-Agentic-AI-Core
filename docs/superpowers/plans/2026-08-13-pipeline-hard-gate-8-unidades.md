# Hard-Gate de Compilación + Soporte 8 Unidades — Plan de Implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Hacer que el pipeline de agentes (`src/multiagent_core/`) soporte 8 unidades curriculares (en vez de 5/7) y pueda bloquear la compilación de una lección cuando tiene anacronismos curriculares críticos o duplica contenido de otra unidad, con backup automático antes de sobrescribir y sin romper el flujo actual mientras el contenido de U2/U5/U6 sigue en reescritura.

**Architecture:** Cada agente del "council" gana una responsabilidad puntual y aislada: `SafetyGateAgent` distingue warnings informativos de bloqueos críticos y cubre 8 unidades; `LayoutEditorialAgent` gana detección de bloques duplicados (cross-unit e intra-archivo); `NotebookCompilerAgent` sanea más patrones de LaTeX roto; `ContentAuditorAgent` mide de verdad la longitud del contexto nanotecnológico. `OrchestratorAgent.run_full_pipeline(enforce_gate=...)` es el único punto que decide si una unidad bloqueada se compila o no — el resto de agentes solo reportan, no deciden. `run_pedagogical_editorial_autofix.py` gana backup automático y pasa `enforce_gate=False` explícitamente mientras dura la Fase 1 de reescritura de contenido.

**Tech Stack:** Python 3, pytest, regex (`re`), `hashlib` (fingerprinting), `shutil` (backup).

## Global Constraints

- Fuente de verdad: `lecciones/*.md`. Nunca editar `notebooks/*.ipynb` a mano (regla existente del proyecto, `CLAUDE.md`).
- Los 8 nombres de unidad canónicos son: `UNIDAD 1` .. `UNIDAD 8`, siguiendo la tabla de renumeración del spec (U1 Estadística Descriptiva, U2 Probabilidad/Combinatoria, U3 VA Discretas, U4 Distribuciones Conjuntas, U5 VA Continuas, U6 Modelado y Simulación, U7 Inferencia y Estimación, U8 Proyecto Integrador).
- Warnings de supuestos estadísticos (Shapiro, Levene, etc.) nunca son críticos — solo anacronismos de secuencia curricular (`unit_forbidden_terms`) y mismatch temático total (`unit_required_terms` ausente) son críticos.
- Todo cambio en `src/multiagent_core/` sigue el patrón TDD ya usado en el repo (test primero, en `tests/` con la misma estructura de carpetas que `src/multiagent_core/`).
- No tocar el contenido de `lecciones/*.md` en este plan — solo el código del pipeline. La única excepción es el archivo de test (`tests/test_pedagogical_pipeline.py`), que sí se edita.

---

## Task 1: Extender `SafetyGateAgent` a 8 unidades con distinción warning/crítico

**Files:**
- Modify: `src/multiagent_core/council/safety_gate_agent.py`
- Test: `tests/council/test_safety_gate_agent.py` (nuevo archivo)

**Interfaces:**
- Consumes: nada (agente hoja, sin dependencias internas)
- Produces: `SafetyGateAgent.validate_assumptions(lesson_text: str, unit_name: str = "") -> Dict[str, Any]` con claves `passed: bool`, `warnings: List[str]`, `critical: bool` (nueva)

- [ ] **Step 1: Escribir el test que falla — 8 unidades en `unit_forbidden_terms`**

Crear `tests/council/test_safety_gate_agent.py`:

```python
"""
Tests for SafetyGateAgent (8 unidades + distincion warning/critico).
"""

import pytest
from src.multiagent_core.council.safety_gate_agent import SafetyGateAgent


@pytest.mark.parametrize("unit_num", range(1, 9))
def test_unit_forbidden_terms_covers_all_8_units(unit_num):
    gate = SafetyGateAgent()
    assert f"UNIDAD {unit_num}" in gate.unit_forbidden_terms


def test_forbidden_term_in_early_unit_is_critical():
    gate = SafetyGateAgent()
    text = "En esta unidad usamos el Error Tipo I para decidir Rechazar H_0."
    result = gate.validate_assumptions(text, "UNIDAD 2")
    assert result["passed"] is False
    assert result["critical"] is True


def test_missing_assumption_warning_is_not_critical():
    gate = SafetyGateAgent()
    text = "Aplicamos t-test sobre los datos de resistencia del nanowire."
    result = gate.validate_assumptions(text, "UNIDAD 3")
    assert result["passed"] is False
    assert result["critical"] is False


def test_unit_required_terms_mismatch_is_critical():
    gate = SafetyGateAgent()
    text = "Esta unidad no menciona ninguno de los temas esperados de probabilidad."
    result = gate.validate_assumptions(text, "UNIDAD 2")
    assert result["critical"] is True


def test_unit_required_terms_present_is_not_critical_for_mismatch():
    gate = SafetyGateAgent()
    text = "Estudiamos combinatoria, permutaciones y el Teorema de Bayes aplicado a nanopartículas."
    result = gate.validate_assumptions(text, "UNIDAD 2")
    assert result["passed"] is True
    assert result["critical"] is False
```

- [ ] **Step 2: Correr el test para confirmar que falla**

Run: `pytest tests/council/test_safety_gate_agent.py -v`
Expected: FAIL — `unit_forbidden_terms` solo tiene UNIDAD 1-5, y `validate_assumptions` no retorna la clave `critical`.

- [ ] **Step 3: Implementar — extender `unit_forbidden_terms` y `unit_required_terms`, agregar `critical`**

Reemplazar el contenido completo de `src/multiagent_core/council/safety_gate_agent.py`:

```python
"""
SafetyGateAgent (@Safety_Gate): Agente Guardián de Supuestos Estadísticos,
Secuencia Curricular y Pedagogía Socrática.
"""

import re
from typing import Dict, Any, List


class SafetyGateAgent:
    """Agente Guardián de la Seguridad Instruccional, Supuestos Estadísticos y Secuencia Curricular."""

    def __init__(self):
        self.assumptions_rules = {
            "t-test": ["shapiro", "normal", "normality"],
            "anova": ["levene", "bartlett", "homoscedasticity", "homocedasticidad"],
            "regression": ["linearity", "homoscedasticidad", "independencia", "residuals"],
        }

        # Reglas de secuencia curricular estricta (Anacronismos prohibidos).
        # Terminos de Inferencia Avanzada (Pruebas de Hipotesis formales) estan
        # prohibidos hasta antes de UNIDAD 7 (Inferencia y Estimacion).
        hipotesis_terms = [
            "Prueba UMP", "Error Tipo I", "Error Tipo II", "Rechazar H_0",
            "Región Crítica", "Prueba de Hipótesis", "Likelihood Ratio",
            "Prueba t de Student", "ANOVA",
        ]
        self.unit_forbidden_terms = {
            "UNIDAD 1": hipotesis_terms,
            "UNIDAD 2": hipotesis_terms,
            "UNIDAD 3": hipotesis_terms,
            "UNIDAD 4": hipotesis_terms,
            "UNIDAD 5": hipotesis_terms,
            "UNIDAD 6": hipotesis_terms,
        }

        # Terminos requeridos por unidad: al menos uno debe aparecer para que
        # la unidad sea tematicamente coherente con su nombre curricular.
        self.unit_required_terms = {
            "UNIDAD 2": ["combinatoria", "bayes", "axioma", "permutación", "permutacion", "combinación", "combinacion"],
            "UNIDAD 4": ["conjunta", "marginal", "condicional", "covarianza"],
            "UNIDAD 6": ["simulación", "simulacion", "monte carlo", "transformada inversa"],
        }

    def validate_assumptions(self, lesson_text: str, unit_name: str = "") -> Dict[str, Any]:
        warnings = []
        critical_flags = []
        text_lower = lesson_text.lower()

        # 1. Validacion de Supuestos Estadisticos en Codigo/Teoria (NO critico)
        for test, required_assumptions in self.assumptions_rules.items():
            if test in text_lower:
                has_assumption = any(ass in text_lower for ass in required_assumptions)
                if not has_assumption:
                    warnings.append(
                        f"Se utiliza '{test}' sin antes verificar los supuestos de "
                        f"{' / '.join(required_assumptions)}."
                    )

        # 2. Validacion de Secuencia Curricular (CRITICO: anacronismo)
        for unit_key, forbidden_terms in self.unit_forbidden_terms.items():
            if unit_key.lower() in unit_name.lower() or unit_key.lower() in lesson_text[:200].lower():
                for term in forbidden_terms:
                    if term.lower() in text_lower:
                        warnings.append(
                            f"🚨 [Error de Secuencia Curricular]: La '{unit_key}' contiene el tema de Inferencia Avanzada '{term}', el cual pertenece estrictamente a UNIDAD 7 y UNIDAD 8."
                        )
                        critical_flags.append(True)

        # 3. Validacion de Mismatch Tematico (CRITICO: contenido de otra unidad)
        for unit_key, required_terms in self.unit_required_terms.items():
            if unit_key.lower() in unit_name.lower() or unit_key.lower() in lesson_text[:200].lower():
                has_required = any(term.lower() in text_lower for term in required_terms)
                if not has_required:
                    warnings.append(
                        f"🚨 [Error de Mismatch Temático]: La '{unit_key}' no contiene ninguno de los términos esperados ({', '.join(required_terms)}); el contenido podría pertenecer a otra unidad."
                    )
                    critical_flags.append(True)

        return {
            "passed": len(warnings) == 0,
            "warnings": warnings,
            "critical": any(critical_flags),
        }
```

- [ ] **Step 4: Correr el test para confirmar que pasa**

Run: `pytest tests/council/test_safety_gate_agent.py -v`
Expected: PASS (5 tests, más 8 parametrizados = 13 total)

- [ ] **Step 5: Correr toda la suite existente para confirmar que nada se rompió**

Run: `pytest tests/ -v --tb=short`
Expected: Puede que `tests/test_pedagogical_pipeline.py::test_pedagogical_review_pipeline` falle aquí — se corrige en Task 5. Todo lo demás debe seguir en verde.

- [ ] **Step 6: Commit**

```bash
git add src/multiagent_core/council/safety_gate_agent.py tests/council/test_safety_gate_agent.py
git commit -m "feat: extender SafetyGateAgent a 8 unidades con distincion warning/critico"
```

---

## Task 2: `detect_duplicate_blocks` en `LayoutEditorialAgent`

**Files:**
- Modify: `src/multiagent_core/council/layout_editorial_agent.py`
- Test: `tests/council/test_layout_editorial_agent.py` (nuevo archivo)

**Interfaces:**
- Consumes: nada
- Produces: `LayoutEditorialAgent.detect_duplicate_blocks(lessons: Dict[str, str]) -> List[Dict[str, Any]]`, donde cada item es `{"hash": str, "locations": List[Tuple[str, int]]}` (unidad, número de bloque)

- [ ] **Step 1: Escribir el test que falla**

Crear `tests/council/test_layout_editorial_agent.py`:

```python
"""
Tests for LayoutEditorialAgent.detect_duplicate_blocks.
"""

from src.multiagent_core.council.layout_editorial_agent import LayoutEditorialAgent


INTRO_SCIPY = (
    "## TEMA: AJUSTE DE DISTRIBUCIONES\n\n"
    "Este es un bloque introductorio largo sobre SciPy que se repite igual "
    "en dos unidades distintas del curso, palabra por palabra, sin ningun "
    "cambio, para simular el caso real detectado en U1 y U6 del diagnostico "
    "original del proyecto de Probabilidad y Estadistica."
)


def test_no_duplicates_returns_empty_list():
    editor = LayoutEditorialAgent()
    lessons = {
        "UNIDAD 1": "## Estadistica Descriptiva\n\nContenido único de la unidad uno sobre medidas de tendencia central.",
        "UNIDAD 2": "## Probabilidad\n\nContenido único de la unidad dos sobre combinatoria y Bayes.",
    }
    result = editor.detect_duplicate_blocks(lessons)
    assert result == []


def test_detects_cross_unit_duplicate():
    editor = LayoutEditorialAgent()
    lessons = {
        "UNIDAD 1": INTRO_SCIPY + "\n\n## Resto de U1\n\nContenido propio de estadistica descriptiva.",
        "UNIDAD 6": INTRO_SCIPY + "\n\n## Resto de U6\n\nContenido propio de inferencia y estimacion.",
    }
    result = editor.detect_duplicate_blocks(lessons)
    assert len(result) >= 1
    involved_units = {loc[0] for dup in result for loc in dup["locations"]}
    assert "UNIDAD 1" in involved_units
    assert "UNIDAD 6" in involved_units


def test_detects_intra_file_duplicate():
    editor = LayoutEditorialAgent()
    lessons = {
        "UNIDAD 4": INTRO_SCIPY + "\n\n## Seccion intermedia\n\nAlgo distinto aqui.\n\n" + INTRO_SCIPY,
    }
    result = editor.detect_duplicate_blocks(lessons)
    assert len(result) >= 1
    locations = result[0]["locations"]
    assert len({loc[1] for loc in locations}) >= 2


def test_ignores_short_blocks():
    editor = LayoutEditorialAgent()
    lessons = {
        "UNIDAD 1": "## Titulo\n\nCorto.",
        "UNIDAD 2": "## Titulo\n\nCorto.",
    }
    result = editor.detect_duplicate_blocks(lessons)
    assert result == []
```

- [ ] **Step 2: Correr el test para confirmar que falla**

Run: `pytest tests/council/test_layout_editorial_agent.py -v`
Expected: FAIL con `AttributeError: 'LayoutEditorialAgent' object has no attribute 'detect_duplicate_blocks'`

- [ ] **Step 3: Implementar `detect_duplicate_blocks`**

Añadir al final de `src/multiagent_core/council/layout_editorial_agent.py` (después de `auto_fix_layout`, manteniendo el resto del archivo intacto):

```python
    def detect_duplicate_blocks(self, lessons: Dict[str, str]) -> List[Dict[str, Any]]:
        """Detecta bloques de texto (>=40 palabras) repetidos entre unidades o dentro
        de la misma unidad, via hash normalizado (whitespace colapsado, minusculas)."""
        import hashlib

        block_locations: Dict[str, List[Any]] = {}

        for unit_name, text in lessons.items():
            raw_blocks = re.split(r'\n\s*\n', text)
            for block_index, raw_block in enumerate(raw_blocks):
                words = raw_block.split()
                if len(words) < 40:
                    continue
                normalized = ' '.join(words).lower()
                block_hash = hashlib.sha256(normalized.encode('utf-8')).hexdigest()
                block_locations.setdefault(block_hash, []).append((unit_name, block_index))

        duplicates = [
            {"hash": block_hash, "locations": locations}
            for block_hash, locations in block_locations.items()
            if len(locations) >= 2
        ]
        return duplicates
```

Añadir el import de `Dict` si falta — verificar la línea de imports existente (`from typing import Dict, Any, List`, ya presente en el archivo).

- [ ] **Step 4: Correr el test para confirmar que pasa**

Run: `pytest tests/council/test_layout_editorial_agent.py -v`
Expected: PASS (4 tests)

- [ ] **Step 5: Commit**

```bash
git add src/multiagent_core/council/layout_editorial_agent.py tests/council/test_layout_editorial_agent.py
git commit -m "feat: detectar bloques duplicados cross-unit e intra-archivo en LayoutEditorialAgent"
```

---

## Task 3: Sanitización extendida en `NotebookCompilerAgent`

**Files:**
- Modify: `src/multiagent_core/notebook_compiler_agent.py:20-29` (método `_sanitize_text`)
- Test: `tests/test_notebook_compiler.py`

**Interfaces:**
- Consumes: nada
- Produces: `NotebookCompilerAgent._sanitize_text(text: str) -> str` (firma sin cambios, comportamiento extendido)

- [ ] **Step 1: Escribir los tests que fallan**

Añadir al final de `tests/test_notebook_compiler.py`:

```python
def test_sanitize_fixes_bar_without_backslash():
    compiler = NotebookCompilerAgent()
    result = compiler._sanitize_text("La media es ar{X} y tambien ar{Y}.")
    assert result == "La media es \\bar{X} y tambien \\bar{Y}."


def test_sanitize_preserves_existing_bar():
    compiler = NotebookCompilerAgent()
    result = compiler._sanitize_text("La media es \\bar{X}.")
    assert result == "La media es \\bar{X}."


def test_sanitize_fixes_mathbf_display_block():
    compiler = NotebookCompilerAgent()
    result = compiler._sanitize_text("Resultado: $$\\mathbf{0.45}$$ es el valor.")
    assert result == "Resultado: $\\mathbf{0.45}$ es el valor."


def test_sanitize_fixes_tilde_typo():
    compiler = NotebookCompilerAgent()
    result = compiler._sanitize_text("El estimador es \\ilde{X}.")
    assert result == "El estimador es \\tilde{X}."


def test_sanitize_fixes_alpha_typo():
    compiler = NotebookCompilerAgent()
    result = compiler._sanitize_text("El nivel de significancia es \\lpha = 0.05.")
    assert result == "El nivel de significancia es \\alpha = 0.05."


def test_sanitize_does_not_touch_matplotlib_alpha_kwarg():
    compiler = NotebookCompilerAgent()
    code = "plt.plot(x, y, alpha=0.6)"
    result = compiler._sanitize_text(code)
    assert result == code
```

- [ ] **Step 2: Correr los tests para confirmar que fallan**

Run: `pytest tests/test_notebook_compiler.py -v`
Expected: FAIL en los 5 tests nuevos de fixes (el de `matplotlib alpha` ya pasa porque `_sanitize_text` no lo toca hoy).

- [ ] **Step 3: Implementar — extender `_sanitize_text`**

Reemplazar el método `_sanitize_text` en `src/multiagent_core/notebook_compiler_agent.py` (líneas 20-29):

```python
    def _sanitize_text(self, text: str) -> str:
        # Sanitizar secuencias de escape ASCII sin dejar artefactos \f o \r
        text = text.replace('\x0crac', '\\frac').replace('\x0c', '')
        text = text.replace('\x0dight', '\\right').replace('\x0d', '')
        text = text.replace('\x08ar{', '\\bar{').replace('\x08', '')
        text = text.replace('\\f\\frac', '\\frac')
        text = text.replace('\\r\\right', '\\right')
        text = text.replace('\\b\\bar', '\\bar')
        text = text.replace('$ar{X}$', '$\\bar{X}$')

        # 'ar{X}' sin backslash previo -> '\bar{X}' (typo recurrente en lecciones)
        text = re.sub(r'(?<!\\)ar\{([A-Za-z])\}', r'\\bar{\1}', text)

        # '$$\mathbf{...}$$' (bloque display de solo negrita) -> '$\mathbf{...}$' inline
        text = re.sub(r'\$\$\\mathbf\{([^}]*)\}\$\$', r'$\\mathbf{\1}$', text)

        # Typos tipograficos puntuales confirmados en el diagnostico (p. ej. U7)
        text = text.replace('\\ilde{', '\\tilde{')
        text = text.replace('\\lpha', '\\alpha')

        return text
```

- [ ] **Step 4: Correr los tests para confirmar que pasan**

Run: `pytest tests/test_notebook_compiler.py -v`
Expected: PASS (todos, incluyendo el original `test_parse_markdown_to_cells`)

- [ ] **Step 5: Commit**

```bash
git add src/multiagent_core/notebook_compiler_agent.py tests/test_notebook_compiler.py
git commit -m "feat: sanear ar{X}, mathbf display, tilde y alpha rotos en NotebookCompilerAgent"
```

---

## Task 4: Medir longitud real del contexto nanotecnológico en `ContentAuditorAgent`

**Files:**
- Modify: `src/multiagent_core/content_auditor_agent.py:24-58`
- Test: `tests/test_content_auditor.py`

**Interfaces:**
- Consumes: nada
- Produces: `ContentAuditorAgent.audit_content(markdown_text: str) -> Dict[str, Any]` (firma sin cambios; el check `"Contexto Nanotecnológico"` ahora exige >=150 palabras alrededor de los términos nano, no solo presencia)

- [ ] **Step 1: Escribir los tests que fallan**

Añadir al final de `tests/test_content_auditor.py`:

```python
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
```

- [ ] **Step 2: Correr los tests para confirmar el estado inicial**

Run: `pytest tests/test_content_auditor.py -v`
Expected: `test_nano_context_fails_when_mention_is_too_short` FALLA (hoy pasa `True` con solo una mención corta); `test_nano_context_passes_with_150_plus_words` PASA ya (falso positivo por casualidad, no por diseño). También correr `test_content_auditor` original para confirmar que sigue en verde antes del cambio.

- [ ] **Step 3: Implementar — contar palabras reales de contexto nano**

Reemplazar el método `audit_content` en `src/multiagent_core/content_auditor_agent.py` (líneas 24-58):

```python
    NANO_TERMS = [
        "nanopartíc", "nanotub", "potencial zeta", "diámetro",
        "síntesis", "toxicid", "nanomater",
    ]
    NANO_MIN_WORDS = 150

    def _count_nano_context_words(self, markdown_text: str) -> int:
        """Cuenta las palabras de los parrafos que mencionan terminologia
        nanotecnologica (no el documento completo)."""
        paragraphs = markdown_text.split("\n\n")
        total = 0
        for paragraph in paragraphs:
            paragraph_lower = paragraph.lower()
            if any(term in paragraph_lower for term in self.NANO_TERMS):
                total += len(paragraph.split())
        return total

    def audit_content(self, markdown_text: str) -> Dict[str, Any]:
        words = len(markdown_text.split())
        latex_boxed = r"\boxed" in markdown_text or r"\boxed{" in markdown_text
        has_sympy = "sympy" in markdown_text.lower()
        has_scipy = "scipy" in markdown_text.lower() or "statsmodels" in markdown_text.lower()
        nano_context_words = self._count_nano_context_words(markdown_text)

        # Count matplotlib/seaborn figures or plots
        plot_count = markdown_text.lower().count("plt.") + markdown_text.lower().count("sns.") + markdown_text.lower().count("plotly")

        # Check component checks
        component_checks = {
            "Teoría Completa": words >= 800,
            "Ejemplo Analítico": "ejemplo" in markdown_text.lower() or "paso" in markdown_text.lower(),
            "Verificación SymPy": has_sympy,
            "Contexto Nanotecnológico": nano_context_words >= self.NANO_MIN_WORDS,
            "Solución en \\boxed{}": latex_boxed,
            "Solución Computacional SciPy": has_scipy,
            "Visualización Profesional": plot_count >= 2,
            "Interpretación & Diccionario": "interpret" in markdown_text.lower() or "diccionario" in markdown_text.lower() or "variables" in markdown_text.lower()
        }

        passed_components = [name for name, ok in component_checks.items() if ok]
        missing_components = [name for name, ok in component_checks.items() if not ok]

        score = (len(passed_components) / len(component_checks)) * 100.0

        return {
            "passed": score >= 75.0,
            "score": score,
            "total_words": words,
            "nano_context_words": nano_context_words,
            "component_checks": component_checks,
            "passed_components": passed_components,
            "missing_components": missing_components
        }
```

Nota: `NANO_TERMS` y `NANO_MIN_WORDS` se declaran como atributos de clase (no de instancia) porque no dependen de `__init__`; verificar que queden dentro del cuerpo de la clase `ContentAuditorAgent`, antes o después de `__init__`, indentados igual que los métodos.

- [ ] **Step 4: Correr los tests para confirmar que pasan**

Run: `pytest tests/test_content_auditor.py -v`
Expected: PASS (3 tests: el original + los 2 nuevos)

- [ ] **Step 5: Correr toda la suite para confirmar que no se rompió nada más**

Run: `pytest tests/ -v --tb=short`
Expected: Verde salvo `tests/test_pedagogical_pipeline.py` (pendiente de Task 5).

- [ ] **Step 6: Commit**

```bash
git add src/multiagent_core/content_auditor_agent.py tests/test_content_auditor.py
git commit -m "feat: exigir >=150 palabras reales de contexto nanotecnologico en ContentAuditorAgent"
```

---

## Task 5: Propagar `critical_block` en `PedagogicalReviewPipeline` y corregir test de riesgo

**Files:**
- Modify: `src/multiagent_core/pedagogical_pipeline.py:91-131` (método `review_and_auto_fix_lesson`)
- Modify: `tests/test_pedagogical_pipeline.py`
- Test: `tests/test_pedagogical_pipeline.py` (mismo archivo, casos nuevos + corrección del existente)

**Interfaces:**
- Consumes: `SafetyGateAgent.validate_assumptions(...)["critical"]` (Task 1)
- Produces: `PedagogicalReviewPipeline.review_and_auto_fix_lesson(lesson_text, unit_name, auto_fix) -> Dict[str, Any]` con clave nueva `critical_block: bool`

- [ ] **Step 1: Corregir el test de riesgo identificado en el spec**

En `tests/test_pedagogical_pipeline.py`, el test existente usa la unidad de prueba `"Unidad 1 Test"` con una lección que menciona "Prueba t de Student" — término ahora en `unit_forbidden_terms["UNIDAD 1"]` desde Task 1. Editar la línea 38 para usar una unidad neutra que no dispare el gate curricular:

```python
    report = pipeline.review_and_auto_fix_lesson(sample_lesson, "Unidad Genérica Test")
```

Y cambiar el encabezado de la lección en la línea 10 (que hoy es `"# UNIDAD 1 ESTADISTICA DESCRIPTIVA"`, y por lo tanto también dispara el match de `unit_key.lower() in lesson_text[:200].lower()` independientemente de `unit_name`) a un encabezado neutro:

```python
    sample_lesson = """# UNIDAD DE PRUEBA GENERICA
```

(mantener el resto del contenido del test igual — solo cambian esas dos líneas).

- [ ] **Step 2: Escribir el test nuevo que falla — `critical_block` se propaga**

Añadir al final de `tests/test_pedagogical_pipeline.py`:

```python
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
```

- [ ] **Step 3: Correr los tests para confirmar el estado**

Run: `pytest tests/test_pedagogical_pipeline.py -v`
Expected: El test original (`test_pedagogical_review_pipeline`) ahora PASA con el fix del Step 1. Los dos nuevos FALLAN con `KeyError: 'critical_block'`.

- [ ] **Step 4: Implementar — agregar `critical_block` al resultado**

Modificar `review_and_auto_fix_lesson` en `src/multiagent_core/pedagogical_pipeline.py` (dentro de la clase `PedagogicalReviewPipeline`, líneas 91-131). Cambiar la firma del método para aceptar `unit_name` ya usado, y agregar la clave al `return` final:

```python
    def review_and_auto_fix_lesson(self, lesson_text: str, unit_name: str = "Unidad", auto_fix: bool = True) -> Dict[str, Any]:
        # 1. Auditoría inicial de diseño editorial
        editorial_audit = self.editor.audit_layout(lesson_text)
        
        fixed_text = lesson_text
        if auto_fix and not editorial_audit["passed"]:
            fixed_text = self.editor.auto_fix_layout(lesson_text)
            editorial_audit = self.editor.audit_layout(fixed_text)

        # 2. Auditoría de estructura con ContentAuditorAgent
        content_audit = self.content_auditor.audit_content(fixed_text)

        # 3. Crítica de rigor teórico con @Scientist
        sci_critique = self.scientist.check_theory(fixed_text)

        # 4. Crítica de supuestos y flujo con @Safety_Gate
        safety_critique = self.safety_gate.validate_assumptions(fixed_text, unit_name)

        # 5. Generación de preguntas de reflexión pedagógica con SocraticDebugger
        socratic_questions = []
        if "normal" in fixed_text.lower() or "t-test" in fixed_text.lower():
            socratic_questions.append(self.socratic_debugger.generate_socratic_question("normality", unit_name))
        if "p-valor" in fixed_text.lower() or "p_value" in fixed_text.lower():
            socratic_questions.append(self.socratic_debugger.generate_socratic_question("p_value", unit_name))
        if "varianza" in fixed_text.lower() or "dispersión" in fixed_text.lower():
            socratic_questions.append(self.socratic_debugger.generate_socratic_question("variance", unit_name))

        # 6. Síntesis y debate del EvaluatorCriticAgent
        synthesis = self.critic_evaluator.synthesize_critique(
            content_audit, sci_critique, safety_critique, editorial_audit, socratic_questions
        )

        return {
            "unit_name": unit_name,
            "fixed_text": fixed_text,
            "editorial_audit": editorial_audit,
            "content_audit": content_audit,
            "scientist_critique": sci_critique,
            "safety_gate_critique": safety_critique,
            "synthesis": synthesis,
            "critical_block": safety_critique.get("critical", False),
        }
```

El único cambio funcional real es: (a) pasar `unit_name` a `self.safety_gate.validate_assumptions(fixed_text, unit_name)` — antes se llamaba sin ese argumento, por lo que el chequeo de `unit_forbidden_terms`/`unit_required_terms` dependía solo de que el propio texto mencionara el nombre de unidad en sus primeros 200 caracteres; y (b) agregar `"critical_block": safety_critique.get("critical", False)` al return.

- [ ] **Step 5: Correr los tests para confirmar que pasan**

Run: `pytest tests/test_pedagogical_pipeline.py -v`
Expected: PASS (3 tests)

- [ ] **Step 6: Commit**

```bash
git add src/multiagent_core/pedagogical_pipeline.py tests/test_pedagogical_pipeline.py
git commit -m "feat: propagar critical_block en PedagogicalReviewPipeline; corregir test de riesgo con SafetyGate 8 unidades"
```

---

## Task 6: `enforce_gate` en `OrchestratorAgent.run_full_pipeline`

**Files:**
- Modify: `src/multiagent_core/orchestrator_agent.py`
- Test: `tests/test_orchestrator_agent.py` (nuevo archivo)

**Interfaces:**
- Consumes: `LayoutEditorialAgent.detect_duplicate_blocks(lessons: Dict[str,str])` (Task 2), `SafetyGateAgent.validate_assumptions(text, unit_name)["critical"]` (Task 1)
- Produces: `OrchestratorAgent.run_full_pipeline(enforce_gate: bool = True) -> List[Dict[str, Any]]`, cada item con clave nueva `gate_blocked: bool` y `gate_reason: str` (vacío si no bloqueado)

- [ ] **Step 1: Escribir los tests que fallan**

Crear `tests/test_orchestrator_agent.py`:

```python
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

UNIDAD_1_CONTENIDO_OK = """# UNIDAD 1 ESTADISTICA DESCRIPTIVA
## Asignatura: Probabilidad y Estadística Inferencial

---

## 1. Fundamentación Teórica y Conceptos Clave
""" + ("teoría descriptiva " * 850) + """

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


@pytest.fixture
def temp_lecciones_dir():
    tmp_dir = tempfile.mkdtemp()
    lecciones_dir = os.path.join(tmp_dir, "lecciones")
    notebooks_dir = os.path.join(tmp_dir, "notebooks")
    os.makedirs(lecciones_dir)

    with open(os.path.join(lecciones_dir, "UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md"), "w", encoding="utf-8") as f:
        f.write(UNIDAD_1_CONTENIDO_OK)
    with open(os.path.join(lecciones_dir, "UNIDAD_2_PROBABILIDAD_COMBINATORIA.md"), "w", encoding="utf-8") as f:
        f.write(UNIDAD_2_CONTENIDO_MEZCLADO)

    yield lecciones_dir, notebooks_dir
    shutil.rmtree(tmp_dir)


def test_enforce_gate_true_blocks_critical_unit(temp_lecciones_dir):
    lecciones_dir, notebooks_dir = temp_lecciones_dir
    orchestrator = OrchestratorAgent(lecciones_dir=lecciones_dir, notebooks_dir=notebooks_dir)

    results = orchestrator.run_full_pipeline(enforce_gate=True)

    by_file = {os.path.basename(r["md_filename"]): r for r in results}
    u2_result = by_file["UNIDAD_2_PROBABILIDAD_COMBINATORIA.md"]
    u1_result = by_file["UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md"]

    assert u2_result["gate_blocked"] is True
    assert u2_result["gate_reason"] != ""
    assert not os.path.exists(os.path.join(notebooks_dir, "UNIDAD_2_PROBABILIDAD_COMBINATORIA.ipynb"))

    assert u1_result["gate_blocked"] is False
    assert os.path.exists(os.path.join(notebooks_dir, "UNIDAD_1_ESTADISTICA_DESCRIPTIVA.ipynb"))


def test_enforce_gate_false_compiles_everything(temp_lecciones_dir):
    lecciones_dir, notebooks_dir = temp_lecciones_dir
    orchestrator = OrchestratorAgent(lecciones_dir=lecciones_dir, notebooks_dir=notebooks_dir)

    results = orchestrator.run_full_pipeline(enforce_gate=False)

    for r in results:
        assert r["gate_blocked"] is False

    assert os.path.exists(os.path.join(notebooks_dir, "UNIDAD_1_ESTADISTICA_DESCRIPTIVA.ipynb"))
    assert os.path.exists(os.path.join(notebooks_dir, "UNIDAD_2_PROBABILIDAD_COMBINATORIA.ipynb"))
```

- [ ] **Step 2: Correr los tests para confirmar que fallan**

Run: `pytest tests/test_orchestrator_agent.py -v`
Expected: FAIL — `run_full_pipeline()` hoy no acepta `enforce_gate`, no retorna `gate_blocked`/`gate_reason`/`md_filename`.

- [ ] **Step 3: Implementar — `enforce_gate` en `OrchestratorAgent`**

Reemplazar el contenido completo de `src/multiagent_core/orchestrator_agent.py`:

```python
"""
OrchestratorAgent: Coordinates compilation, code auditing, content auditing, and evaluation pipeline.
"""

import os
from typing import Dict, Any, List

from .code_auditor_agent import CodeAuditorAgent
from .content_auditor_agent import ContentAuditorAgent
from .evaluator_agent import EvaluatorAgent
from .notebook_compiler_agent import NotebookCompilerAgent
from .council.safety_gate_agent import SafetyGateAgent
from .council.layout_editorial_agent import LayoutEditorialAgent


class OrchestratorAgent:
    """Orchestrator for the multiagent auditing and compilation pipeline."""

    def __init__(self, lecciones_dir: str = "lecciones", notebooks_dir: str = "notebooks"):
        self.compiler = NotebookCompilerAgent(lecciones_dir=lecciones_dir, notebooks_dir=notebooks_dir)
        self.code_auditor = CodeAuditorAgent()
        self.content_auditor = ContentAuditorAgent()
        self.evaluator = EvaluatorAgent()
        self.safety_gate = SafetyGateAgent()
        self.layout_editor = LayoutEditorialAgent()

    @staticmethod
    def _unit_name_from_filename(md_filename: str) -> str:
        if "UNIDAD_" in md_filename:
            return f"UNIDAD {md_filename.split('_')[1]}"
        return md_filename

    def _check_gate(self, md_filename: str, md_text: str, duplicate_unit_names: set) -> Dict[str, Any]:
        unit_name = self._unit_name_from_filename(md_filename)

        safety_result = self.safety_gate.validate_assumptions(md_text, unit_name)
        if safety_result["critical"]:
            reason = "; ".join(w for w in safety_result["warnings"] if "🚨" in w)
            return {"blocked": True, "reason": reason}

        if unit_name in duplicate_unit_names:
            return {"blocked": True, "reason": f"Bloque de texto duplicado detectado que involucra a {unit_name}."}

        return {"blocked": False, "reason": ""}

    def run_pipeline_on_file(self, md_filename: str, gate_decision: Dict[str, Any] = None) -> Dict[str, Any]:
        gate_decision = gate_decision or {"blocked": False, "reason": ""}

        md_path = os.path.join(self.compiler.lecciones_dir, md_filename)
        with open(md_path, "r", encoding="utf-8") as f:
            md_text = f.read()

        # 2. Content Audit
        content_results = self.content_auditor.audit_content(md_text)

        # 3. Code Audit
        code_results = self.code_auditor.audit_code(md_text)

        # 4. Evaluation
        evaluation = self.evaluator.evaluate_notebook(code_results, content_results)

        nb_path = None
        if not gate_decision["blocked"]:
            # 1. Compile Markdown to Notebook (solo si el gate no bloquea)
            nb_path = self.compiler.compile_file(md_filename)

        return {
            "md_filename": md_filename,
            "notebook_path": nb_path,
            "content_audit": content_results,
            "code_audit": code_results,
            "evaluation": evaluation,
            "approved": evaluation["passed"] and content_results["passed"],
            "gate_blocked": gate_decision["blocked"],
            "gate_reason": gate_decision["reason"],
        }

    def run_full_pipeline(self, enforce_gate: bool = True) -> List[Dict[str, Any]]:
        results = []
        if not os.path.exists(self.compiler.lecciones_dir):
            return results

        md_filenames = sorted(f for f in os.listdir(self.compiler.lecciones_dir) if f.endswith(".md"))

        lessons_text: Dict[str, str] = {}
        for fname in md_filenames:
            with open(os.path.join(self.compiler.lecciones_dir, fname), "r", encoding="utf-8") as f:
                lessons_text[self._unit_name_from_filename(fname)] = f.read()

        duplicate_unit_names: set = set()
        if enforce_gate:
            duplicates = self.layout_editor.detect_duplicate_blocks(lessons_text)
            for dup in duplicates:
                for unit_name, _block_index in dup["locations"]:
                    duplicate_unit_names.add(unit_name)

        for fname in md_filenames:
            if enforce_gate:
                unit_name = self._unit_name_from_filename(fname)
                gate_decision = self._check_gate(fname, lessons_text[unit_name], duplicate_unit_names)
            else:
                gate_decision = {"blocked": False, "reason": ""}

            results.append(self.run_pipeline_on_file(fname, gate_decision=gate_decision))

        return results
```

Nota importante: `run_pipeline_on_file` cambia de firma (gana el parámetro opcional `gate_decision`) y de comportamiento interno (ya no llama a `self.compiler.compile_file(...)` incondicionalmente al inicio, sino al final y solo si no está bloqueado). También corrige un bug preexistente menor: antes construía la ruta con `self.compiler.lecciones_dir + "/" + md_filename` (string concat), ahora usa `os.path.join`, más robusto en Windows.

- [ ] **Step 4: Correr los tests para confirmar que pasan**

Run: `pytest tests/test_orchestrator_agent.py -v`
Expected: PASS (2 tests)

- [ ] **Step 5: Correr toda la suite para confirmar que no se rompió nada**

Run: `pytest tests/ -v --tb=short`
Expected: Todo en verde. Si `tests/test_code_auditor.py` u otros referencian `run_pipeline_on_file` con la firma vieja, ajustar la llamada (no la implementación) para pasar sin `gate_decision` (usa el default).

- [ ] **Step 6: Commit**

```bash
git add src/multiagent_core/orchestrator_agent.py tests/test_orchestrator_agent.py
git commit -m "feat: hard-gate real en OrchestratorAgent.run_full_pipeline via enforce_gate"
```

---

## Task 7: Backup automático en `run_pedagogical_editorial_autofix.py`

**Files:**
- Modify: `run_pedagogical_editorial_autofix.py`
- Modify: `.gitignore` (excluir `lecciones/.backup/`)
- Test: manual (script de entrada, no tiene test unitario en `tests/` — se verifica por ejecución controlada en Step 3)

**Interfaces:**
- Consumes: `OrchestratorAgent.run_full_pipeline(enforce_gate: bool)` (Task 6)
- Produces: nada consumido por otras tasks (script terminal)

- [ ] **Step 1: Añadir `lecciones/.backup/` a `.gitignore`**

Añadir al final de `.gitignore`:

```
# Backups automaticos del pipeline de autofix editorial
lecciones/.backup/
```

- [ ] **Step 2: Modificar el script con backup y `enforce_gate=False` explícito**

Reemplazar el contenido completo de `run_pedagogical_editorial_autofix.py`:

```python
"""
Script para ejecutar el PedagogicalReviewPipeline con auto-fix editorial
del LayoutEditorialAgent (@Editor) sobre todas las lecciones y recompilar los notebooks.
"""

import os
import glob
import shutil
from datetime import datetime
from src.multiagent_core.pedagogical_pipeline import PedagogicalReviewPipeline
from src.multiagent_core.orchestrator_agent import OrchestratorAgent

lecciones_dir = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\lecciones'
backup_dir = os.path.join(lecciones_dir, '.backup')
os.makedirs(backup_dir, exist_ok=True)

pipeline = PedagogicalReviewPipeline()

print("=== EJECUTANDO AUTOCORRECCIÓN EDITORIAL DE @EDITOR EN TODAS LAS UNIDADES ===")

for filepath in sorted(glob.glob(os.path.join(lecciones_dir, '*.md'))):
    unit_name = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    unit_key = f"UNIDAD {unit_name.split('_')[1]}" if "UNIDAD_" in unit_name else unit_name
    res = pipeline.review_and_auto_fix_lesson(text, unit_key, auto_fix=True)
    fixed_text = res['fixed_text']

    if fixed_text != text:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = os.path.join(backup_dir, f"{unit_name}.{timestamp}.md")
        shutil.copy2(filepath, backup_path)
        print(f"[BACKUP] {unit_name} -> {os.path.basename(backup_path)}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_text)

    score = res['synthesis']['coherence_score']
    critical = res.get('critical_block', False)
    status = "BLOQUEO CRITICO" if critical else "OK"
    print(f"[EDITADO Y CORREGIDO {status}] {unit_name} | Coherencia Editorial: {score}/100.0")

print("\n=== RE-COMPILANDO NOTEBOOKS JUPYTER (notebooks/*.ipynb) ===")
# enforce_gate=False mientras dura la Fase 1 de reescritura de contenido
# (U2 reescrita desde cero, U5 dividida en U5/U6). Cambiar a enforce_gate=True
# (o quitar el argumento, ya que True es el default) cuando esa fase termine.
orchestrator = OrchestratorAgent(lecciones_dir='lecciones', notebooks_dir='notebooks')
results = orchestrator.run_full_pipeline(enforce_gate=False)

for r in results:
    if r["gate_blocked"]:
        print(f"[GATE BLOQUEADO] {r['md_filename']} | Motivo: {r['gate_reason']}")
        continue
    nb = os.path.basename(r['notebook_path'])
    score = r['evaluation']['total_score']
    print(f"[RECOMPILADO OK] {nb} | Score Final: {score}/100.0")
```

Cambio de fondo respecto al original: solo se crea backup si `fixed_text != text` (evita backups vacíos en lecciones que el auto-fix no tocó), y se imprime si la lección quedó con `critical_block=True` para visibilidad inmediata, aunque el compilado en sí siga corriendo con `enforce_gate=False`.

- [ ] **Step 3: Verificación manual controlada (no hay test automatizado para este script de entrada)**

Run:
```bash
cd "C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA"
python -c "
import os
print('lecciones/.backup existe antes:', os.path.exists('lecciones/.backup'))
"
```
Expected: `False` (aún no se ha corrido el script). No ejecutar el script completo en esta task — toca las 7 lecciones reales del curso y depende de que Task 1-6 ya estén commiteadas. Se ejecuta como parte de la Fase 1 de contenido (fuera de este plan), no aquí. Esta task solo verifica que el archivo compila sin errores de sintaxis:

Run: `python -m py_compile run_pedagogical_editorial_autofix.py`
Expected: sin salida (compila limpio).

- [ ] **Step 4: Commit**

```bash
git add run_pedagogical_editorial_autofix.py .gitignore
git commit -m "feat: backup automatico pre-escritura y enforce_gate=False explicito en autofix script"
```

---

## Task 8: Verificación final de la suite completa

**Files:** ninguno (task de verificación pura)

**Interfaces:** ninguna

- [ ] **Step 1: Correr toda la suite de tests**

Run: `pytest tests/ -v --tb=short`
Expected: Todos los tests en verde, incluyendo los preexistentes (`test_code_auditor.py`, `test_content_auditor.py`, `test_notebook_compiler.py`, `test_pedagogical_pipeline.py`, `tests/council/test_council_pipeline.py`) y los nuevos de este plan (`test_safety_gate_agent.py`, `test_layout_editorial_agent.py`, `test_orchestrator_agent.py`).

- [ ] **Step 2: Confirmar cobertura de las 8 unidades end-to-end**

Run:
```bash
python -c "
from src.multiagent_core.council.safety_gate_agent import SafetyGateAgent
gate = SafetyGateAgent()
for i in range(1, 9):
    key = f'UNIDAD {i}'
    print(key, '->', 'forbidden' if key in gate.unit_forbidden_terms else 'sin reglas forbidden', ',', 'required' if key in gate.unit_required_terms else 'sin reglas required')
"
```
Expected: imprime las 8 unidades sin errores (algunas sin reglas `required` es esperado — solo U2/U4/U6 las tienen según el diseño).

- [ ] **Step 3: Commit final si hubiera cambios pendientes de formateo**

```bash
git status --short
```
Si hay cambios sin commitear (no debería haberlos si cada task se commiteó), revisarlos antes de cerrar el plan.

---

## Fuera de alcance (recordatorio del spec)

- Reescritura de contenido de U2, división de U5→U5/U6, purga de hipótesis en U1/U3/U5.
- Renombrado físico de `lecciones/UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.md` para crear `UNIDAD_6_MODELADO_SIMULACION.md` (eso ocurre cuando se ejecute la Fase 1/4 de contenido, no en este plan de pipeline).
- Integración del material de `raw_student_notebooks/profesor/modelado_simulacion/`.
- Activar `enforce_gate=True` por default en producción (queda en `False` explícito en el script hasta que termine la reescritura de contenido).
