# GOVERNANCE.md — Modelo de Gobernanza del Consejo de Expertos
## Probabilidad y Estadística Inferencial Agentic Core

## 1. Misión del Consejo

El objetivo primordial de este proyecto es el desarrollo de materiales pedagógicos y agénticos de **Probabilidad y Estadística Inferencial** aplicados a la **IA y Nanotecnología** bajo tres pilares inquebrantables:

1. **Rigor Matemático**: Demostraciones analíticas formales y notación LaTeX impecable.
2. **Excelencia Computacional**: Implementación estándar en Python (`scipy.stats`, `statsmodels`, `pandas`, `sympy`).
3. **Relevancia Nanotecnológica**: Todos los ejercicios e ilustraciones emplean datos reales de la física y química de nanoestructuras.

---

## 2. El Consejo de Expertos (8 Agentes)

### 🏗️ Lead Architect (@Architect)
* **Responsabilidad**: Guardián de la estructura del proyecto, la jerarquía curricular y las dependencias.
* **Estado en el pipeline (actualizado 2026-08): bloqueante en `run_full_pipeline`, advisory en cualquier otro caller.** `validate_structure(file_tree)` audita la completitud del *curso completo* (¿existen las 8 `UNIDAD_*`?), no la validez de una lección individual. `OrchestratorAgent.run_full_pipeline` es el único caller que conoce el listado completo de `.md` del directorio de lecciones en el momento de la auditoría, así que es el único que le pasa un `file_tree` real a `_check_gate` → `CouncilPipeline.process_content()`; con `file_tree` presente, `architect` se agrega a los reportes bloqueantes de esa corrida (ver §4). Cualquier otro caller que invoque `process_content()` por lección aislada (`PedagogicalReviewPipeline`, tests unitarios) sin pasar `file_tree` sigue recibiendo `architect_res = {"passed": True, "skipped": True}` — evita el falso-bloqueo de una unidad válida solo porque otra no está presente en ese contexto aislado.

### 🔬 Senior Researcher (@Scientist)
* **Responsabilidad**: **Dueño de la Teoría**. Fundamentación axiomática, derivaciones y expresiones LaTeX.

### ⚙️ Simulation Engineer (@Engineer)
* **Responsabilidad**: **Constructor del Código**. Implementación de librerías numéricas (`scipy`, `statsmodels`, `sympy`).

### 🛡️ Safety Gate (@Safety_Gate)
* **Responsabilidad**: **Guardián de Supuestos Estadísticos**. Validación de normalidad, homocedasticidad y pedagogía socrática.

### 📊 Data Analyst (@Analyst)
* **Responsabilidad**: **Visualización e Interpretación**. Gráficos Seaborn/Matplotlib y análisis post-gráfico ($\ge 150$ palabras).

### 📚 The Librarian (@Librarian)
* **Responsabilidad**: **Validación Bibliográfica**. Contraste con textos de referencia (Walpole, Montgomery).
* **Estado en el pipeline (actualizado 2026-08): lógica real, no bloqueante en el gate.** `verify_references(text)` ya no es un stub que siempre aprueba. Si el texto no cita ningún DOI, aprueba con la sola presencia de una palabra clave de referencia conocida (Walpole, Montgomery, SciPy, MIT, meta-analysis). Si cita uno o más DOIs (formato `DOI: [10.xxxx/yyyy](url)`), cada uno debe resolver contra la API pública de Crossref para que el reporte pase — un DOI que no resuelve (typo, retractado, inexistente) hace fallar `passed`. No se agregó a `OrchestratorAgent._BLOCKING_REPORTS`: a diferencia de los 5 reportes ya bloqueantes, este depende de una llamada de red externa en tiempo de auditoría, lo cual introduce fragilidad (timeout/caída de Crossref) que no es deseable en el gate que decide si una lección se publica. Queda disponible para quien invoque `CouncilPipeline` directamente o para promoverlo a bloqueante en el futuro si se decide aceptar esa dependencia de red.

### ✅ Quality Auditor (@QA)
* **Responsabilidad**: **Auditor Supremo**. Verificación estricta de los 8 Componentes del Protocolo Maestro.

### 🎨 Layout Editor (@Editor)
* **Responsabilidad**: **Maquetación y Diseño Editorial**. Limpieza de títulos descontextualizados, jerarquía de encabezados (H1/H2/H3), detección de bloques de texto duplicados entre unidades.

---

## 3. Los 3 Loops de Retroalimentación

- **Loop L1 (Fallo en Código / Supuestos)**: `@Safety_Gate` $\to$ `@Engineer` para corregir la implementación.
- **Loop L2 (Fallo Teórico / Consistencia)**: `@Librarian` $\to$ `@Scientist` para ajustar la fundamentación matemática.
- **Loop L3 (Protocolo Incompleto)**: `@QA` $\to$ `@Engineer` para agregar componentes faltantes.

---

## 4. Qué gate realmente bloquea la compilación (por diseño, no por omisión)

`CouncilPipeline.process_content()` calcula un reporte por cada uno de los 8 agentes y los agrega en `final_qa.approved` (`@QA.final_audit`, `all(passed)` sobre los 8). `OrchestratorAgent._check_gate` — el gate real que decide si una lección se compila a notebook (`enforce_gate=True`) — no consulta `final_qa.approved` directamente; en su lugar consulta explícitamente un subconjunto elegido de reportes, listado en `OrchestratorAgent._BLOCKING_REPORTS`, más `@Architect` cuando el caller le pasa `file_tree` (ver abajo).

**Bloqueantes hoy**: `@Safety_Gate` (siempre, vía `critical`) más `@Engineer`, `@Editor`, `@Scientist` y `@Analyst` (vía `passed`, listados en `_BLOCKING_REPORTS`) — estos 5 se evalúan sin importar el caller. `@Architect` se suma como bloqueante **solo cuando `_check_gate` recibe `file_tree`** — hoy únicamente `OrchestratorAgent.run_full_pipeline`, que sí conoce el listado completo de `.md` del curso en ese momento (ver la entrada de `@Architect` arriba).

**Asesor, no bloqueante**: `@Librarian` — desde 2026-08 tiene lógica real (ver su entrada arriba: aprueba por palabra clave si no hay DOIs citados, o exige que cada DOI citado resuelva en Crossref), pero no se agregó a `_BLOCKING_REPORTS` porque su verificación depende de una llamada de red externa (Crossref) que introduce fragilidad (timeout, caída del servicio) no deseable en el gate de publicación. `@QA` sigue igual: agrega los 8 en `final_qa.approved`, pero ese agregado no se usa como gate — se calcula igual y queda disponible para quien invoque `CouncilPipeline` directamente.

**Por qué no se usa `final_qa.approved` tal cual**: agregar los 8 con `all(passed)` dejaría a `@QA` evaluando su propio agregado como si fuera un reporte más, y haría bloqueante a `@Librarian` (dependencia de red no deseada en el gate) y a `@Architect` incluso en contextos donde `process_content()` se invoca por lección aislada sin `file_tree` (falso-bloqueo). Consultar el subconjunto explícito en `_BLOCKING_REPORTS` (más `@Architect` condicionado a `file_tree`) es más preciso que confiar en el `all()` genérico.

**Verificación de no-regresión al ampliar el gate (2026-08)**: antes de promover `@Engineer`, `@Editor`, `@Scientist` y `@Analyst`, se ejecutó `CouncilPipeline.process_content()` sobre las 8 lecciones reales (`UNIDAD_1` a `UNIDAD_8`) y se confirmó que las 8 pasan los 4 reportes nuevos — el fix previo de `@Safety_Gate` (que corrigió falsos positivos de regresión en prosa vs. código) ya había dejado el contenido real en un estado limpio. Esta verificación ya **no es manual**: `tests/test_orchestrator_agent.py::test_ninguna_leccion_real_del_curso_es_bloqueada_por_el_gate` corre `OrchestratorAgent.run_full_pipeline(enforce_gate=True)` contra las 8 lecciones reales en cada ejecución de la suite, y falla si una edición futura hace caer alguna por debajo de los umbrales de `_BLOCKING_REPORTS` (incluyendo `@Architect` en esa corrida) — no hace falta volver a ejecutar el pipeline a mano para confirmarlo.

Si en el futuro se decide promover `@Librarian` a bloqueante (aceptando la dependencia de red en el gate) u otro reporte, la forma correcta es agregarlo a `OrchestratorAgent._BLOCKING_REPORTS` — nunca asumir que `final_qa.approved` ya lo cubre.

**Sobre la cita repetida de SciPy (Virtanen et al. 2020, decisión 2026-08)**: `@Engineer.check_code_implementation` detecta `has_scipy_or_statsmodels` en el código de cada unidad, y las 8 lecciones citan el paper de SciPy como referencia de esa librería. Se evaluó y se decidió **mantener la repetición**: cada unidad usa scipy/statsmodels en su propio código de ejemplo, así que citar la fuente del software en cada una es válido académicamente (no es relleno ni plagio) — es equivalente a citar el mismo libro de texto en cada capítulo que lo usa. La variedad bibliográfica real se atacó agregando una referencia específica adicional por unidad (un DOI de aplicación en nanotecnología distinto en cada una), no quitando la cita de SciPy.
