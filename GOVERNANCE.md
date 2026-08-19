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

`CouncilPipeline.process_content()` calcula un reporte por cada uno de los 8 agentes y los agrega en `final_qa.approved` (`@QA.final_audit`, `all(passed)` sobre los 8). Sin embargo, `OrchestratorAgent._check_gate` — el gate real que decide si una lección se compila a notebook (`enforce_gate=True`) — consulta **únicamente** `reports["safety_gate"]["critical"]`, no `final_qa.approved`.

Esto es una decisión de diseño explícita, no un descuido: `@Safety_Gate` es el único de los 8 agentes cuyo fallo representa un riesgo real de contenido incorrecto o prematuro llegando al estudiante (supuestos estadísticos violados, terminología de unidades posteriores mencionada antes de tiempo). Los otros 7 reportes (`@Architect`, `@Scientist`, `@Engineer`, `@Analyst`, `@Librarian`, `@QA`, `@Editor`) son señales asesoras — se calculan, quedan disponibles en `final_qa.reports` para quien invoque `CouncilPipeline` directamente, pero no bloquean automáticamente la compilación de la lección.

**Por qué no se conectó `approved` al gate real**: al momento de escribir esto, U8 tiene un warning no crítico de `@Safety_Gate` (`critical=False`, supuestos de regresión no verificados) que haría fallar `final_qa.approved` si el gate lo consultara — bloquearía una lección que hoy compila y publica correctamente por un hallazgo asesor, no por un riesgo real de contenido. Conectar `approved` al gate requeriría primero resolver ese warning (y cualquier otro similar que surja de los 7 reportes asesores) para no introducir bloqueos retroactivos inesperados sobre contenido ya publicado.

Si en el futuro se decide que algún otro reporte del Consejo (p. ej. `@Engineer` tras el guardrail de convergencia Monte Carlo) debe ser bloqueante como `@Safety_Gate`, la forma correcta es promoverlo explícitamente en `_check_gate` — nunca asumir que `final_qa.approved` ya lo cubre.
