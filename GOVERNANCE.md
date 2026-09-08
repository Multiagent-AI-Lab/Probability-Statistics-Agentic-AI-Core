# GOVERNANCE.md

## 1. Propósito de este documento

Este archivo documenta el patrón pedagógico central que estructura el contenido de "Probabilidad y Estadística Inferencial", el estándar de calidad que cada unidad debe cumplir, y el modelo de gobernanza del Consejo de 8 Expertos (`src/multiagent_core/pipeline.py`) que audita ese contenido una vez escrito. La redacción del contenido en sí sigue sin ser generada por un pipeline automatizado — se escribe y revisa directamente (sesiones de trabajo con el profesor, sin agentes de IA orquestando la redacción) — pero la auditoría posterior sí es software real que corre y bloquea publicación: su alcance y límites exactos están en §2.1.

---

## 2. El Ciclo de Verificación Triple

Cada concepto nuevo del curso — cuando tiene forma cerrada verificable — sigue el mismo ciclo de cuatro fases:

1. **Teoría**: la definición formal del concepto, con notación LaTeX estricta.
2. **Verificación Simbólica (SymPy)**: la fórmula se expresa con símbolos algebraicos (`sympy.symbols`), se manipula simbólicamente, y solo entonces se sustituyen valores numéricos concretos — nunca se salta directo al número.
3. **Solución Computacional (SciPy/statsmodels)**: el mismo resultado se reproduce con las herramientas numéricas de producción (`scipy.stats`, `statsmodels`), confirmando que ambos caminos —simbólico y numérico— coinciden.
4. **Interpretación**: qué significa el resultado en el contexto de nanotecnología del ejemplo, en al menos un párrafo posterior a cualquier gráfico.

Este ciclo es el análogo, en este curso, del "Hilo de Oro" (Pseudocódigo→Mermaid→Python→pytest) del repo hermano de Lógica de Programación — mismo principio de verificación en capas sucesivas, adaptado a contenido matemático en vez de código imperativo.

**Excepción explícita**: técnicas intrínsecamente numéricas sin forma cerrada (simulación Monte Carlo, remuestreo Bootstrap, regularización Ridge/Lasso/Elastic Net, tests basados en rangos, ajuste de redes neuronales) NO requieren la fase de Verificación Simbólica — forzar SymPy sobre un método que no tiene solución cerrada sería relleno sin valor pedagógico. En esos casos el ciclo se reduce a Teoría → Solución Computacional → Interpretación.

---

### 2.1 Qué verifica el Consejo automáticamente (y qué no)

El Consejo de 8 Expertos (`src/multiagent_core/pipeline.py`) audita cada lección con verificación real, no con conteo de palabras clave:

| Agente | Qué verifica | Cómo |
|---|---|---|
| `@Scientist` | Fórmulas LaTeX con estructura real, solución en `\boxed{}`, invariantes de dominio | Parseo de bloques LaTeX; comprueba $P\in[0,1]$, $\sigma^2\ge0$, $\lvert\rho\rvert\le1$, $\sum P(x_i)=1$ |
| `@Engineer` | Que el código ejecutado reproduzca los valores `\boxed{}` del texto | Ejecuta la unidad completa en un subproceso aislado y contrasta su salida |
| `@Analyst` | Interpretación **posterior** a la visualización y con una afirmación contrastable | Posición real en el documento + presencia de magnitudes |
| `@Librarian` | Que cada DOI citado exista | Consulta a la API pública de Crossref |
| `@Safety_Gate` | Supuestos estadísticos y secuencia curricular | Reglas por unidad |
| `@Editor` | Maquetación y metadatos sueltos | Patrones de encabezado |
| `@QA` | Veredicto final sobre hallazgos tipados `{tipo, severidad, agente, mensaje}` | Bloquea solo ante hallazgos bloqueantes |

**Límites declarados** (lo que el Consejo NO puede afirmar):

* **`@Architect` es advisory-only en el flujo por lección.** Audita la completitud del curso completo (¿existen las 8 `UNIDAD_*`?), no la validez de una lección individual, así que `process_content()` no le pasa `file_tree` y el agente se reporta como `skipped`. Conectarlo por defecto bloquearía la auditoría de UNIDAD 1 solo porque UNIDAD 5 aún no existe. Un caller que necesite auditar completitud curricular debe invocar `ArchitectAgent.validate_structure(file_tree)` directamente, fuera del pipeline por lección.
* **No se verifica todo bloque de código.** Los que dependen del runtime de notebook (`ipytest`, magics `%pip`, escapes `!git`), de la red o de los propios agentes del repo se omiten deliberadamente; omitirlos no cuenta como error del contenido.
* **No se contrasta todo `\boxed{}`.** Un ejemplo analítico autocontenido, cuyos datos de entrada no aparecen en la salida de ningún bloque, no se reporta: sin evidencia de que el código pretendiera reproducirlo, marcarlo sería un falso positivo. El Consejo prefiere callar a inventar un hallazgo.
* **La verificación es numérica y estructural, no semántica.** El Consejo detecta que un número no cuadra o que un invariante se viola; no juzga si una explicación es pedagógicamente buena.

---

## 3. El Gold Standard de Calidad

Cada sección de contenido nuevo debe cumplir, verificable mediante `ContentAuditorAgent.audit_content()`:

1. **Teoría Completa**: al menos 800 palabras de desarrollo teórico formal (el conteo excluye el contenido de bloques de código fenced — no se cuentan líneas de código ni de tablas como prosa teórica).
2. **Ejemplo Analítico**: la sección contiene ejemplos desarrollados paso a paso con explicación.
3. **Verificación SymPy**: manipulación simbólica de fórmulas con `sp.Symbol`/`sp.symbols`/`sympy.symbols` seguida de un `.subs(` dentro del mismo bloque de código. **Límite conocido**: este patrón no reconoce otras formas legítimas de verificación simbólica en SymPy que no pasan por `Symbol`/`subs` — p. ej. aritmética exacta con `sp.Rational`/`sp.Add`/`sp.nsimplify` (como en UNIDAD 1) se audita como "False" pese a ser SymPy real. El chequeo automático es un piso conservador, no un juicio definitivo sobre si la unidad usa SymPy correctamente: un fallo en este punto debe revisarse manualmente antes de asumir que la unidad tiene una brecha real.
4. **Contexto Nanotecnológico**: todo ejemplo usa datos o problemas de nanotecnología reales o realistas (nunca ejemplos genéricos de estadística).
5. **Solución en `\boxed{}`**: cualquier valor numérico final de un ejemplo analítico se resalta con `\boxed{...}`.
6. **Solución Computacional SciPy**: reproducción del resultado mediante `scipy.stats` o `statsmodels` ejecutado.
7. **Visualización Profesional**: al menos 2 gráficos (matplotlib/seaborn) por sección aplicada relevante.
8. **Interpretación Post-Gráfico**: existe al menos un párrafo con la palabra "interpret..." que aparece, en el documento, después del cierre de algún bloque de código con `plt.`/`sns.`. **Límite conocido**: la verificación es posicional por texto plano (`str.find()` del bloque completo), no por AST ni por vínculo semántico real entre el párrafo y el gráfico que interpreta; si el mismo bloque de código apareciera repetido de forma textualmente idéntica más de una vez en el documento, la posición usada sería la de su primera aparición. No se ha observado este caso en las 8 unidades reales (0 bloques de código duplicados textualmente en cualquiera de ellas a la fecha de este documento), pero no está estructuralmente descartado por el código.
9. **Diccionario de Variables**: cada unidad cierra con la notación completa usada, verificada contra el código/ejemplo real de la unidad.

---

## 4. Verificación de Símbolos en el Diccionario de Variables

Cada entrada del Diccionario de Variables debe corresponder a un símbolo o variable usada en un ejemplo REAL Y EJECUTADO de la propia unidad — una tabla de sintaxis genérica, un docstring en prosa, o una mención aislada en teoría sin ejemplo aplicado no cuentan como uso verificado. Antes de agregar o aprobar una entrada, releer el bloque de código o el ejemplo analítico que la usa.

---

## 5. Fundamentación: por qué el Consejo y el Tutor están diseñados así

El diseño de este repositorio (Consejo de 8 Expertos, `@QA` como juez sobre hallazgos
tipados, `StatsTutorAgent` socrático, énfasis en verificar supuestos antes de correr
una prueba) no se adoptó por convención sino que coincide con evidencia 2025-2026 sobre
evaluación automática y aprendizaje asistido por IA. Las cuatro fuentes siguientes
fueron confirmadas de forma independiente (WebFetch/WebSearch sobre el DOI o abstract
original) durante la redacción de esta sección — no son citas de segunda mano.

* **[*Reliability without Validity*, arXiv 2606.19544](https://arxiv.org/abs/2606.19544)**
  — la mayor evaluación sistemática de LLM-as-a-judge hasta la fecha: 21 jueces de 9
  proveedores, 118 corridas, ~541 000 juicios individuales sobre 3 benchmarks. Su
  hallazgo central: *"high test–retest reliability (>0.95) coexists with severe
  position bias (>0.10)"* — un evaluador puede ser perfectamente consistente y aun así
  no discriminar contenido bueno de malo. Documenta además *kappa deflation* de 33.8–41.3
  puntos porcentuales entre acuerdo exacto y $\kappa$ de Cohen corregido por azar.
  **Relación con este repo**: es el marco teórico exacto de por qué H-01 era un riesgo
  real y no una preocupación teórica. Los 8 agentes originales (conteo de subcadenas)
  eran máximamente consistentes — la misma entrada producía siempre el mismo veredicto
  — y mínimamente válidos: el experimento de H-01 midió 0/2 de detección sobre
  documentos deliberadamente falsos. La reconstrucción del Consejo (Task 1 de este
  plan) responde directamente a esto: reemplaza conteo por verificación que puede
  fallar, y `@QA` pasa de `all(passed)` a un juez sobre hallazgos tipados con severidad
  — el equivalente estructural del *Judge Agent* que el paper de la fuente siguiente
  describe.

* **Scaffolding guiado en estadística universitaria, arXiv 2606.01375** (*Beyond
  Access: Guided LLM Scaffolding for Independent Learning in Undergraduate
  Statistics*) — estudio experimental en un curso de Probabilidad y Estadística de
  licenciatura, comparando tres condiciones: sin acceso a LLM, acceso irrestricto, y
  acceso guiado con entrenamiento explícito en estrategias de ayuda efectivas. Hallazgo
  confirmado: *"guided use was associated with a clearer learning-oriented interaction
  pattern than unrestricted access"* — el grupo guiado mostró mejor desempeño
  independiente en quiz sin asistencia de LLM; el grupo de acceso irrestricto no mostró
  ganancias equivalentes. **Relación con este repo**: aplica directamente porque el
  estudio se hizo en la misma disciplina (estadística, no genérico) que este curso.
  Valida el diseño de `StatsTutorAgent` (`src/multiagent_core/stats_tutor_agent.py`,
  método `_diagnose_error`): cuando detecta un error del alumno devuelve una pista
  socrática — una pregunta que guía el razonamiento — en vez de la respuesta directa.
  Es la misma distinción que el paper encuentra determinante: no el acceso a la
  herramienta, sino si la interacción prioriza razonamiento sobre respuesta inmediata.

* **Schwarz 2025**, *The use of generative AI in statistical data analysis and its
  impact on teaching statistics at universities of applied sciences*, [*Teaching
  Statistics* 47, 118–128](https://onlinelibrary.wiley.com/doi/10.1111/test.12398)
  — confirmado por búsqueda independiente (Wiley bloquea WebFetch directo con 403;
  el abstract se confirmó vía búsqueda web sobre el DOI). Hallazgo: la IA generativa
  facilita el análisis estadístico a quien tiene poco conocimiento del área
  *"mainly by generating appropriate code, but only partly by following standard
  procedures"* — el fallo típico está en el **procedimiento** (elegir la prueba
  correcta, verificar sus supuestos), no en la sintaxis del código. **Relación con
  este repo**: fundamenta por qué el Ciclo de Verificación Triple (§2) y `@Safety_Gate`
  (§2.1, verificación de supuestos estadísticos) son un punto de énfasis deliberado del
  curso y no un paso burocrático — es exactamente el punto donde el paper documenta que
  la asistencia de IA falla con mayor frecuencia.

* **Auditoría multiagente de producción con Judge Agent, arXiv 2607.11276** (*AI
  Textbook Auditor: Automated Textbook Auditing with Multi-Agent LLM Systems*, iTextbooks
  2026 @ AIED'2026) — confirmado: sistema multiagente de QA sobre libros de texto reales,
  con agentes especializados por categoría de error, un **Judge Agent** que filtra falsos
  positivos con reglas explícitas, y una taxonomía de error de dominio. Cifra reportada:
  **56 hallazgos técnicos en 7 categorías sobre un libro de texto real, con precisión
  validada por expertos de 62.5%** — y una declaración ética explícita de que ningún
  hallazgo se aplica sin validación humana. **Relación con este repo**: es el referente
  directo del diseño de `@QA` reconstruido en Task 1 — hallazgos tipados
  `{tipo, severidad, agente, mensaje}` con 9 categorías de dominio en vez de un booleano
  plano, y la política explícita en `@Engineer` de *"esta auditoría prefiere callar a
  inventar un hallazgo"* replica el mismo principio de precisión-sobre-cobertura que
  justifica el 62.5% del referente en vez de intentar 100% de cobertura con más ruido.
  La cifra 62.5% del referente es también la vara con la que medir al Consejo de este
  repo el día en que se mida su propia precisión contra un corpus etiquetado — ejercicio
  que §5.1 declara todavía pendiente.

### 5.1 Qué comprueba hoy la verificación automática, con cifras — y qué no

Esta sección declara el alcance real, no aspiracional, a la fecha de esta redacción
(commits de Task 1 y Task 4 de este mismo plan, rama `sdd/cierre-brechas-rubric-15`).

**Lo que sí comprueba, con evidencia:**

* El Consejo reconstruido (Task 1) corrido contra las 8 unidades reales sin corregir
  aprueba **6/8** limpias (0 hallazgos) y reprueba **2/8** con el hallazgo bloqueante
  exacto — `UNIDAD_6` (H-05, desajuste ejemplo↔salida: el texto declara 12.3957, el
  código produce 6.8447) y `UNIDAD_7` (H-02, aritmética inconsistente: el `\boxed{}`
  declara 0.75, la fórmula cierra en 0.8880) — sin que se le indicara dónde buscar.
  0 falsos positivos en las 6 unidades correctas.
* `ContentAuditorAgent.audit_content()` (Task 4, tras corregir sus 3 falsos positivos
  de H-08) da **100% en 7 de 8 unidades** sobre los 9 puntos del Gold Standard.
  `UNIDAD_1` marca 88.9% (falla solo el punto 3, Verificación SymPy) por un límite de
  detección declarado abajo, no por una brecha real de contenido.
* La suite de tests de la rama pasa completa: **248 passed, 0 failed** a la fecha del
  cierre de Task 4 (`pytest tests/ -v --tb=short`).

**Lo que NO comprueba — límites conocidos, con la causa exacta:**

* **Interpretación semántica del contenido (H-03).** El Consejo detecta que un número
  no cierra o que un invariante se viola; no juzga si una afirmación en prosa tiene el
  sentido físico correcto. `UNIDAD_4` aprueba con 0 hallazgos pese a contener H-03 (una
  frase que invierte el sentido de una correlación negativa: "menos negativo" en vez de
  "más negativo") porque el número $\rho=-0.75$ es matemáticamente válido y ninguna
  salida de código lo contradice — el defecto es puramente de lenguaje natural. Es la
  fase 4 ("Interpretación") del Ciclo de Verificación Triple, la única de las cuatro que
  ningún agente puede verificar hoy. Requiere revisión humana; perseguirlo con
  heurísticos de texto sería la fuente de falsos positivos que el propio diseño de
  `@Engineer` evita deliberadamente ("prefiere callar a inventar un hallazgo").
* **Verificación SymPy con formas legítimas fuera del patrón `Symbol`/`subs`**
  (`ContentAuditorAgent`, punto 3 del Gold Standard, §3). El patrón implementado exige
  `sp.Symbol`/`sp.symbols` seguido de `.subs(` en el mismo bloque; no reconoce aritmética
  exacta con `sp.Rational`/`sp.Add`/`sp.nsimplify` — el caso real es `UNIDAD_1:189-203`,
  que usa SymPy genuino para construir media y varianza como fracciones exactas antes de
  convertir a float, y aun así se audita como "False". Un fallo en este punto es un piso
  conservador del detector, no evidencia de que la unidad tenga una brecha real.
* **`@Architect` es advisory-only en el flujo por lección** (§2.1) — la completitud
  curricular de las 8 `UNIDAD_*` no se audita en el pipeline automático por defecto.
* **Bloques de código que dependen del runtime de notebook, la red, o los propios
  agentes del repo se omiten** de la ejecución de `@Engineer` (§2.1) — no se ejecutan
  ni se cuentan como error por no ejecutarse.
* **La precisión del Consejo nunca se ha medido contra un corpus etiquetado más allá
  de los 2 documentos adversariales de Task 1** (0/2 de detección era el estado
  anterior a la reconstrucción; el 6/8 y 2/8 de arriba es la primera medición contra
  contenido real, no una tasa de precisión validada por un tercero). No existe todavía
  el equivalente al 62.5% con validación experta que reporta arXiv 2607.11276.

---

*Este documento describe el estado real del proceso de este repositorio. El contenido se escribe y revisa directamente (sesiones con el profesor, sin agentes orquestando la redacción); lo que sí corre como software es el Consejo de 8 Expertos que audita el resultado, con el alcance y los límites declarados en §2.1 y, con cifras concretas, en §5.1. Cualquier cambio en lo que esos agentes verifican debe actualizarse aquí para reflejar exactamente lo que corre, no lo que se aspira a construir.*
