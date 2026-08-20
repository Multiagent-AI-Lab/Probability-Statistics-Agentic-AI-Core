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
* **Estado en el pipeline: advisory/opt-in por diseño.** `validate_structure(file_tree)` audita la completitud del *curso completo* (¿existen las 8 `UNIDAD_*`?), no la validez de una lección individual. `CouncilPipeline.process_content()` se invoca por lección (`OrchestratorAgent`, `PedagogicalReviewPipeline`), así que ningún caller de producción le pasa `file_tree` hoy — conectarlo ahí bloquearía la auditoría de una unidad válida solo porque otra unidad no está presente en ese momento. `architect_res` es `{"passed": True, "skipped": True}` por defecto; un caller que audite completitud curricular puede invocar `ArchitectAgent.validate_structure(file_tree)` directamente, fuera de este pipeline por-lección.

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

`CouncilPipeline.process_content()` calcula un reporte por cada uno de los 8 agentes y los agrega en `final_qa.approved` (`@QA.final_audit`, `all(passed)` sobre los 8). `OrchestratorAgent._check_gate` — el gate real que decide si una lección se compila a notebook (`enforce_gate=True`) — no consulta `final_qa.approved` directamente; en su lugar consulta explícitamente un subconjunto elegido de reportes, listado en `OrchestratorAgent._BLOCKING_REPORTS`.

**Bloqueantes hoy**: `@Safety_Gate` (siempre, vía `critical`) más `@Engineer`, `@Editor`, `@Scientist` y `@Analyst` (vía `passed`). Estos 5 son los únicos reportes del Consejo con lógica real de detección de un defecto — no un stub que siempre aprueba (`@Librarian.verify_references` devuelve `passed: True` incondicionalmente hoy) ni una señal de completitud de *curso* en vez de *lección* (`@Architect`, opt-in — ver arriba).

**Asesores, no bloqueantes**: `@Architect` (opt-in por diseño, ver arriba), `@Librarian` (stub sin lógica de fallo real) y `@QA` (agrega los 8 en `final_qa.approved`, pero ese agregado no se usa como gate — se calcula igual y queda disponible para quien invoque `CouncilPipeline` directamente).

**Por qué no se usa `final_qa.approved` tal cual**: agregar los 8 con `all(passed)` incluiría a `@Architect` (que siempre pasa por diseño salvo que se le pase `file_tree`, ver arriba) y a `@Librarian` (que siempre pasa, es un stub) sin aportar señal real, y dejaría a `@QA` evaluando su propio agregado como si fuera un reporte más. Consultar el subconjunto explícito en `_BLOCKING_REPORTS` es más preciso que confiar en el `all()` genérico.

**Verificación de no-regresión al ampliar el gate (2026-08)**: antes de promover `@Engineer`, `@Editor`, `@Scientist` y `@Analyst`, se ejecutó `CouncilPipeline.process_content()` sobre las 8 lecciones reales (`UNIDAD_1` a `UNIDAD_8`) y se confirmó que las 8 pasan los 4 reportes nuevos — el fix previo de `@Safety_Gate` (que corrigió falsos positivos de regresión en prosa vs. código) ya había dejado el contenido real en un estado limpio. Se confirmó además, ejecutando `OrchestratorAgent.run_full_pipeline(enforce_gate=True)` sobre las 8 lecciones reales, que ninguna se bloquea retroactivamente.

Si en el futuro se decide promover `@Librarian` (una vez tenga lógica real de verificación, no solo `passed: True` fijo) u otro reporte, la forma correcta es agregarlo a `OrchestratorAgent._BLOCKING_REPORTS` — nunca asumir que `final_qa.approved` ya lo cubre.
