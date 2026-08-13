# Plan de Corrección Integral: Notebooks y Sistema de Agentes

## Diagnóstico General

Análisis profundo del estado actual del repositorio **Probabilidad y Estadística / Modelado y Simulación** — UCEMICH IA & Nanotecnología.

---

## 1. Análisis del Contenido de las Lecciones Generadas

### Estado Actual (Post-proceso):

| Unidad | Palabras | Líneas | Problemas Críticos |
|---|---|---|---|
| U1 – Estadística Descriptiva | 10,519 | 1,714 | Intro genérica de SciPy copiada; hipótesis en U1; sección §9 (`SymPy`) fuera de orden (al final tras §11) |
| U2 – Probabilidad & Combinatoria | 21,042 | 3,163 | Contenido de **Distrib. Conjuntas (Caps. 5.3–5.4)** mezclado; 63 ocurrencias de `$$\mathbf{}$$` mal encapsulado; hipótesis presentes |
| U3 – Variables Aleatorias Discretas | 31,495 | 5,823 | Hipótesis presentes; estructura modular correcta pero excesiva para la unidad |
| U4 – Distribuciones Conjuntas | 19,187 | 5,653 | Sin intro duplicada ✅; sin hipótesis ✅; 24 ocurrencias de `$$\mathbf{}$$` |
| U5 – Variables Aleatorias Continuas | 68,329 | 10,495 | Hipótesis presentes; archivo enorme (489 KB); errores de `\bar{}` |
| U6 – Inferencia & Estimación | 24,581 | 3,684 | Intro genérica de SciPy copiada (idéntica a U1, líneas 8-68); hipótesis ✅ correcto aquí; 20 ocurrencias de `$$\mathbf{}$$` |
| U7 – Proyecto Integrador | 1,865 | 310 | Muy breve (14 KB); hipótesis ✅ correcto; numeración interna rota (`### 70.1`) |

### Problemas Transversales Detectados:

#### A. Bloque Introductorio Duplicado Genérico (Error Crítico de Identidad)
- **U1** y **U6** comienzan con el mismo bloque copiado: `## TEMA: AJUSTE DE DISTRIBUCIONES / ## Estadistica con SciPy: Guia Completa` (líneas 8–68 idénticas en ambas).
- Este bloque es el encabezado de `Copy_of_Estadística_SciPy_MEJORADA.ipynb` (raw), no pertenece a ninguna unidad como introducción pedagógica.

#### B. Mala Alineación Curricular (Anacronismos Pedagógicos)
- **U1** contiene `hipótesis` → el `SafetyGateAgent` detectó el problema pero el fix no eliminó todos los términos.
- **U2** tiene problemas más graves: el contenido es de *Distribuciones Conjuntas y Esperanza Condicional* (5.3–5.4), que corresponde a **U4**, no a U2 (Probabilidad & Combinatoria).
- **U3** y **U5** también contienen referencias a hipótesis que no corresponden.

#### C. Errores de LaTeX / KaTeX en Markdown
- **`$$\mathbf{...}$$`**: Bloque display de solo negrita → no renderiza bien en Jupyter/KaTeX. Debe usarse `$\mathbf{...}$` inline o dentro de `\boxed{}`.
- **`ar{X}`** (sin backslash): 3 instancias en U1, 5 en U2, 2 en U5, 3 en U6. Error recurrente de escapado.
- **`\tilde{X}`** escrito como `\ilde{X}`** (U7): error tipográfico literal en código Python de display.
- **Numeración rota en U7**: `### 70.1` y `### 70.2` en lugar de `### 10.1` y `### 10.2`.
- **`\lpha` y `\eta`** en lugar de `\alpha` y `\beta` en U7.

#### D. Errores de Estructura Narrativa en Notebooks `.ipynb`
- **U3 Notebook**: 679 celdas (602 markdown, solo 77 código) → casi sin separación código/texto.
- **U5 Notebook**: 1025 celdas (961 markdown, 64 código) → desequilibrio extremo.
- **U1 y U6 Notebooks**: Tienen el bloque introductorio genérico que no corresponde.

---

## 2. Análisis del Sistema de Agentes

### Consejo de 7 Expertos + Agentes de Auditoría:

| Agente | Archivo | Función | Problema Detectado |
|---|---|---|---|
| `ContentAuditorAgent` | `content_auditor_agent.py` | Verifica 8 componentes Protocolo Maestro | Funciona, pero criterios superficiales (busca "ejemplo" o "paso" como boolean) |
| `SafetyGateAgent` | `council/safety_gate_agent.py` | Detecta anacronismos curriculares | **Parcialmente funcional**: detecta pero no bloquea la generación; no detecta bloque introductorio duplicado |
| `LayoutEditorialAgent` | `council/layout_editorial_agent.py` | Detecta duplicados de encabezados | **No está detectando** el bloque duplicado de intro SciPy |
| `ScientistAgent` | `council/scientist_agent.py` | Valida rigor teórico | Solo cuenta palabras; no valida alineación temática |
| `EvaluatorCriticAgent` | `pedagogical_pipeline.py` | Sintetiza críticas cruzadas | Funciona como agregador pero no bloquea compilación |
| `NotebookCompilerAgent` | `notebook_compiler_agent.py` | Compila MD → .ipynb | **Compila sin validar**: ejecuta la compilación independientemente de las críticas |
| `PedagogicalReviewPipeline` | `pedagogical_pipeline.py` | Orquesta el pipeline completo | **El pipeline no tiene Gating**: si un agente falla, el compilador sigue adelante igualmente |

### Deficiencias Estructurales del Pipeline:

1. **Ausencia de Hard-Gate**: El `review_and_auto_fix_lesson()` devuelve resultados pero no impide que `run_pedagogical_editorial_autofix.py` compile el notebook si hay errores críticos.
2. **El `SafetyGateAgent` valida contenido pero no la fuente**: No detecta que U2 tiene contenido de U4 (el tema no coincide con el nombre del archivo).
3. **El `NotebookCompilerAgent._sanitize_text()`** solo corrige `\x08ar{` (backspace+ar) pero no `ar{X}` literal que persiste en el markdown.
4. **`LayoutEditorialAgent`** no detecta bloques de texto idénticos entre unidades (duplicate fingerprinting).
5. **El pipeline de auto-fix sobrescribe los archivos lección** sin backup, haciendo difícil revertir.

---

## 3. Análisis vs. Objetivos del Curso (Planeaciones Didácticas + ZIP de Referencias)

### Cursos Combinados:
1. **Probabilidad y Estadística Inferencial** (planeación 2025-2026-I)
2. **Modelado y Simulación** (notebooks en `raw_student_notebooks/profesor/modelado_simulacion/`)

### Mapeo Curricular Objetivo vs. Actual:

| Unidad | Tema Correcto (Plan Didáctico) | Contenido Actual | Alineación |
|---|---|---|---|
| U1 | Estadística Descriptiva (medidas de tendencia, dispersión, EDA, histogramas) | Intro genérica de SciPy + EDA básico + KDE + Materials Project API | ⚠️ Parcial |
| U2 | Probabilidad: Axiomas, Conjuntos, Combinatoria, Bayes, Probabilidad Condicional | Contenido de **Distrib. Conjuntas Cap. 5.3–5.4** (completamente equivocado) | ❌ Error grave |
| U3 | Variables Aleatorias Discretas: Bernoulli, Binomial, Poisson, Geométrica, Hipergeométrica | Contenido extenso VAD correcto pero con hipótesis anacrónicas | ✅ Correcto con defectos |
| U4 | Distribuciones Conjuntas: PMF/PDF conjunta, marginal, condicional, covarianza | Contenido parcialmente correcto | ✅ Mayormente correcto |
| U5 | Variables Aleatorias Continuas: Normal, Exponencial, Gamma, Beta, Weibull + Modelado | Archivo gigante (68K palabras) con múltiples distribuciones + MCS + KDE | ✅ Rico pero desbalanceado |
| U6 | Inferencia, Estimación Puntual, IC, Pruebas de Hipótesis | Intro duplicada + contenido de hipótesis correcto | ⚠️ Parcial (intro equivocada) |
| U7 | Proyecto Integrador: Aplicación completa de Pruebas de Hipótesis | Estructura correcta pero muy breve y con errores de numeración | ⚠️ Demasiado breve |

### Material de Modelado y Simulación (de los ZIPs):
Los notebooks de la carpeta `modelado_simulacion/` contienen:
- `MODELOS_PARA_VARIABLES_ALEATORIAS.ipynb` → Modelos para VA: Poisson, Exponencial, Gamma (muy rico)
- `Investigación_VAD.ipynb` → Investigación de Variables Aleatorias Discretas (3.7 MB)
- `Investigación_VADC.ipynb` → Variables Continuas completo (7.3 MB - el más completo)
- `Proyecto_final_Modelado1.ipynb` → Proyecto Final de Modelado (5.6 MB)
- `Proyecto_final_MyS.ipynb` → Proyecto Final Modelado y Simulación completo (6.2 MB)

**Este material de M&S no ha sido integrado correctamente en las lecciones generadas**, especialmente los módulos de simulación Monte Carlo y generación de números aleatorios que son centrales al curso.

---

## 4. Plan de Corrección Detallado (Priorizado)

### FASE 1: Correcciones Críticas de Contenido (Debe hacerse antes de recompilar)

#### 4.1 Reconstruir U2 con Contenido Correcto de Probabilidad & Combinatoria
- **Problema**: U2 tiene contenido de distribuciones conjuntas.
- **Acción**: Reescribir U2 con: Axiomas de Kolmogorov, Álgebra de Conjuntos, Combinatoria (permutaciones, combinaciones), Probabilidad Condicional, Teorema de Bayes, con ejemplos nanotecnológicos.
- **Fuentes**: Notebooks de referencia del profesor (raw), planeación didáctica.

#### 4.2 Eliminar Bloque Introductorio Duplicado en U1 y U6
- **Problema**: Ambas unidades inician con la misma introducción genérica de SciPy (líneas 8-68).
- **Acción**: Reemplazar por introducciones específicas al tema de cada unidad.
  - U1: Introducción a Estadística Descriptiva y Análisis Exploratorio de Datos.
  - U6: Introducción a la Inferencia Estadística y Estimación.

#### 4.3 Purgar Términos de Hipótesis Restantes en U1, U3, U5
- **Problema**: Términos como `hipótesis`, `H_0`, `Error Tipo I`, `p-valor` siguen apareciendo en unidades donde no corresponden.
- **Acción**: Script de limpieza quirúrgica que preserve el contexto descriptivo pero elimine las referencias a pruebas formales de hipótesis.

### FASE 2: Correcciones de LaTeX / KaTeX

#### 4.4 Corrección de `$$\mathbf{...}$$` mal encapsulado (187 ocurrencias totales)
- U2: 63 ocurrencias → Reemplazar por `$\mathbf{...}$` inline o `$$\boxed{\mathbf{...}}$$`
- U4: 24 ocurrencias
- U6: 20 ocurrencias
- U3: 7 ocurrencias
- U5: 4 ocurrencias

#### 4.5 Corrección de `ar{X}` sin backslash (13 total)
- Script regex: `(?<![\\])ar\{([A-Za-z])\}` → `\\bar{\1}`

#### 4.6 Corrección de errores tipográficos en U7
- `\ilde{X}` → `\tilde{X}`
- `\lpha` → `\alpha` (U7 líneas 226-228)
- `\eta` → `\beta` cuando se refiere a error Tipo II
- `### 70.1` y `### 70.2` → `### 10.1` y `### 10.2`

### FASE 3: Refactorización del Sistema de Agentes

#### 4.7 Añadir Hard-Gate al Pipeline de Compilación
- Modificar `run_pedagogical_editorial_autofix.py` para que si `SafetyGateAgent` reporta anacronismos críticos, el `NotebookCompilerAgent` **NO ejecute** la compilación.
- Output: log de errores bloqueantes + confirmación de compilación solo si `coherence_score >= 80`.

#### 4.8 Añadir Detección de Bloque Introductorio Duplicado al `LayoutEditorialAgent`
- Fingerprint SHA-256 de los primeros 500 tokens de cada lección.
- Comparación cruzada entre unidades para detectar texto idéntico al inicio.

#### 4.9 Mejorar `SafetyGateAgent`: Detección de Mismatch Temático
- Añadir diccionario de términos **requeridos** por unidad (no solo prohibidos).
- Ejemplo: U2 debe contener "combinatoria" / "permutación" / "Bayes" para ser válido como unidad de probabilidad.

#### 4.10 Mejorar `NotebookCompilerAgent._sanitize_text()`
- Añadir regex para `ar{X}` → `\\bar{X}` y `$$\mathbf{` → `$\mathbf{` directamente en el compilador.

### FASE 4: Integración de Material de Modelado y Simulación

#### 4.11 Integrar Módulos de Simulación en U3, U4, U5
- Extraer los módulos de simulación Monte Carlo de `MODELOS_PARA_VARIABLES_ALEATORIAS.ipynb`.
- Integrar simulación de VA discretas en U3 (Poisson, Binomial con MCS).
- Integrar simulación de VA continuas en U5 (Normal, Exponencial, Weibull con MCS).
- Integrar simulación conjunta y correlación en U4.

#### 4.12 Expandir U7 (Proyecto Integrador) con Material de Modelado y Simulación
- Incorporar pipeline de `Proyecto_final_MyS.ipynb` como plantilla del proyecto.
- Añadir módulo de simulación de tamaño de muestra y potencia.
- Objetivo: U7 debe tener al menos 5,000 palabras.

### FASE 5: Recompilación y Verificación Final

#### 4.13 Recompilar todos los Notebooks
- Ejecutar `run_pedagogical_editorial_autofix.py` con el nuevo hard-gate.
- Verificar que todos los notebooks pasen el `ContentAuditorAgent` con score ≥ 87.5%.

#### 4.14 Verificación Final de Calidad
- Audit KaTeX: 0 errores de `ar{X}`, 0 `\lpha`, 0 `$$\mathbf{}$$` mal formateado.
- Verificación curricular: U2 contiene probabilidad correcta, U1 sin hipótesis.
- Verificación de tamaños: U7 ≥ 5,000 palabras, todos los demás ≥ 15,000.

---

## 5. Verificación del Plan

### Tests Automatizados a Ejecutar:
```bash
pytest tests/ -v
python audit_katex_cleanliness.py
python run_pedagogical_editorial_autofix.py
```

### Criterios de Éxito:
- [ ] U2 contiene "combinatoria" + "Bayes" como temas principales
- [ ] U1 y U6 sin bloque introductorio duplicado
- [ ] 0 ocurrencias de `ar{X}` en todos los .md
- [ ] 0 ocurrencias de `$$\mathbf{...}$$` mal encapsulado
- [ ] U7 ≥ 5,000 palabras con numeración correcta
- [ ] Hard-gate funcional: pipeline rechaza compilación si hay anacronismos
- [ ] Todos los notebooks compilados exitosamente
- [ ] Material de M&S integrado en U3, U4, U5

---

## Preguntas Abiertas — Resueltas (2026-08-13)

> **P1: Reconstrucción de U2** — **Decisión: descartar y reescribir desde cero.**
> Verificación fragmento por fragmento contra U4 (líneas 1-845 de U2 vs. estructura completa de U4): el 100% de U2 es el mismo tema 5.3-5.4 (PMF/PDF condicional, esperanza condicional, LET, convolución/suma de variables) que U4 ya cubre con mejor estructura (secciones 1-8 numeradas) y con los mismos ejemplos de nanotecnología o equivalentes. Ni un solo ejemplo de U2 aporta contenido ausente en U4. Nota lateral: U4 tiene su propia duplicación interna (la sección 5.3-5.4 aparece dos veces, en línea ~650 y de nuevo en ~946) — limpiarla es parte del ítem 4.2/4.8 (fingerprinting de duplicados), no exclusivo de U2.
> **Acción**: reescribir U2 desde cero con Axiomas de Kolmogorov, Álgebra de Conjuntos, Combinatoria, Probabilidad Condicional, Teorema de Bayes (como ya indicaba 4.1).

> **P2: Balance U5** — **Decisión: dividir en U5a y U5b.**
> Punto de corte identificado: línea 10436 de `UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.md`, sección `## 10. Módulo de Simulación: Método de la Transformada Inversa y Aceptación-Rechazo`. Todo lo anterior (líneas 1-10435, ≈ mayoría de las 68,329 palabras) es distribuciones continuas clásicas (Uniforme, Normal, Exponencial, Gamma, Beta, Weibull, F de Fisher-Snedecor, etc., con duplicados a depurar — p. ej. Distribución Uniforme aparece dos veces, una con "Codigo en phyton" traducido de R). Todo lo posterior es simulación (transformada inversa, aceptación-rechazo, SymPy). Esa sección ya tiene la misma numeración rota que U7 (`### 50.1`/`### 50.2` en vez de `### 10.1`/`### 10.2`) — mismo bug, debe corregirse junto con el de U7 (ítem 4.6).
> **Acción**: `UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.md` → **U5: Variables Aleatorias Continuas** (líneas 1-10435, depurado de duplicados). Contenido de simulación (línea 10436+) se fusiona con P3.

> **P3: Material M&S** — **Decisión: unidad(es) separada(s), no repartido en U3/U4/U5.**
> Consistente con P2: la sección de simulación ya extraída de U5 (transformada inversa, aceptación-rechazo) más el material rico de `raw_student_notebooks/profesor/modelado_simulacion/` (`MODELOS_PARA_VARIABLES_ALEATORIAS.ipynb`, `Investigación_VAD.ipynb`, `Investigación_VADC.ipynb`, `Proyecto_final_Modelado1.ipynb`, `Proyecto_final_MyS.ipynb`) forman una nueva **U6: Modelado y Simulación** dedicada, en vez de diluirse como fragmentos dentro de las unidades teóricas. Esto reemplaza el ítem 4.11 del plan original (que proponía repartir M&S en U3/U4/U5).
>
> **Renumeración resultante de unidades** (7 → 8):
> | Nueva | Contenido | Origen |
> |---|---|---|
> | U1 | Estadística Descriptiva | U1 actual, sin intro SciPy duplicada (4.2) |
> | U2 | Probabilidad, Conjuntos y Combinatoria | Reescrita desde cero (P1) |
> | U3 | Variables Aleatorias Discretas | U3 actual, purgada de hipótesis (4.3) |
> | U4 | Distribuciones Conjuntas | U4 actual, deduplicada internamente |
> | U5 | Variables Aleatorias Continuas | U5 actual líneas 1-10435 |
> | U6 | Modelado y Simulación | Sección 10 de U5 (líneas 10436+) + material `modelado_simulacion/` (nueva unidad) |
> | U7 | Inferencia y Estimación | U6 actual, sin intro SciPy duplicada (4.2) |
> | U8 | Proyecto Integrador | U7 actual, expandido (4.12), numeración corregida (4.6) |
>
> **Impacto en el plan**: los ítems 4.11-4.12 (Fase 4) se reemplazan por "construir U6 nueva"; el pipeline (`convert_to_notebooks_smart.py` o equivalente en este repo) debe actualizar su lista de archivos a compilar de 7 a 8 unidades.

> **P4: Idioma de Corrección** — **Decisión: uniformizar todo a español.**
> Consistente con el resto del curso (lecciones y docstrings ya en español) y con la convención del repo hermano de Lógica de Programación. Aplica a todos los bloques de código en U1-U8, incluyendo los fragmentos con comentarios en inglés o traducidos de R detectados en U5 (p. ej. "Codigo en phyton", comentarios paso a paso estilo tutorial de R).
