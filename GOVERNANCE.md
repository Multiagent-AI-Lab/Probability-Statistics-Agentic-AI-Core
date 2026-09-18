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
3. **Verificación SymPy**: manipulación simbólica real, reconocida por dos vías independientes: (a) `sp.Symbol`/`sp.symbols`/`sympy.symbols` seguido de un `.subs(` dentro del mismo bloque de código, o (b) `sp.Rational` combinado con una simplificación (`nsimplify`/`sp.nsimplify`/`sp.simplify`) en el mismo bloque — aritmética exacta sin sustitución de variable (patrón real de UNIDAD 1: `sp.Rational` + `sp.Add` + `sp.nsimplify`). La vía (b) se agregó el 2026-09-14 (D2, plan `camino-a-100-cierre-brechas`) porque la vía (a) sola daba falso negativo en UNIDAD 1, que usa SymPy real sin declarar símbolo ni llamar `.subs()`.
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
  de H-08) da **100% en las 8 de 8 unidades** sobre los 9 puntos del Gold Standard.
  `UNIDAD_1` marcaba 88.9% (fallaba solo el punto 3, Verificación SymPy) hasta que
  D2 (2026-09-14, plan `camino-a-100-cierre-brechas`) agregó la segunda vía de
  detección (`sp.Rational`+simplificación) que reconoce el patrón real de esa
  unidad — verificado, ahora 9/9.
* La suite de tests de la rama pasa completa: **248 passed, 0 failed** a la fecha del
  cierre de Task 4 (`pytest tests/ -v --tb=short`).
* **A3 (auditoría 2026-09-15, actualizada 2026-09-16 tras M2): la precisión del
  Consejo se midió contra un corpus etiquetado de 47 casos** (20 negativos reales
  tomados de fragmentos de las 8 unidades, 12 positivos confirmados de rondas de
  auditoría previas —N-01, N-03, N-05, N-08—, 15 sintéticos de falsedad semántica)
  — ver `docs/superpowers/audits/2026-09-16-precision-consejo-corpus.md` para la
  matriz de confusión completa (`scripts/medir_precision_consejo.py`, 46 casos
  evaluados; 1 excluido por Crossref inaccesible durante la corrida). Cifra vigente:
  **precisión 54.5%, recall 44.4%, κ de Cohen -0.079** — mejora real y verificada
  sobre la medición inicial (41.4%/44.4%/-0.457, `docs/superpowers/audits/2026-09-15-
  precision-consejo-corpus.md`), pero todavía por debajo del 62.5% con validación
  experta de arXiv 2607.11276 (§5), y un κ apenas negativo sigue indicando acuerdo
  no mejor que el esperable solo por azar.

  M2 (2026-09-16, dos rondas) rehizo los 20 fragmentos negativos con el cierre
  completo del ciclo (gráfico + interpretación) donde el contenido original lo
  permitía sin cruzar a un tema distinto — 13 de 20 se extendieron, 2 ya estaban
  completos. El mismo trabajo destapó una causa raíz *distinta* de la fragmentación:
  `@Analyst` (`_AFIRMACION_VERIFICABLE` en `analyst_agent.py`) no reconocía dos
  formas reales de citar una magnitud — la unidad tras el espacio forzado de LaTeX
  (`$12.9\ \text{nm}$`) y un número con separador de miles seguido de una palabra
  suelta (`$100,000$ réplicas`) — bloqueando interpretaciones que sí citan cifras
  concretas. Corregido con dos alternativas nuevas en el regex (revisado por
  `python-reviewer` y `security-reviewer` sin hallazgos críticos; el regex ya tenía
  un hallazgo CRITICAL de ReDoS en un ciclo anterior, así que ambas alternativas
  nuevas mantienen la misma disciplina de cuantificadores acotados, con test de
  regresión de constante de tiempo agregado).

  Una segunda ronda de diagnóstico sobre los residuales encontró una tercera causa,
  también de fragmentación pero en `@Librarian` en vez de `@Analyst`: 3 fragmentos
  (`neg_01`, `neg_03`, `neg_19`) no incluían el DOI que la unidad completa sí cita
  en otro punto del documento (`@Librarian` exige al menos un DOI que resuelva
  contra Crossref, `librarian_agent.py::verify_references`) — corregido pegando la
  entrada bibliográfica real de la unidad al final de esos 3 fragmentos, igual que
  ya tenían los `neg_0X_ejemplo_doi.md`. `neg_03` queda totalmente resuelto
  (verdadero negativo). Esa misma ronda confirmó dos límites estructurales
  genuinos que **no son bugs y no se corrigieron**: (1) 4 fragmentos (`neg_01`,
  `neg_02`, `neg_17`, `neg_18`) recortan una sub-sección que en el contenido real
  nunca tiene fase gráfica propia (LET continua, Método de Momentos, MLE/MAP) —
  `@Analyst` exige ≥2 gráficos por el Gold Standard §3 punto 7 ("Visualización
  Profesional... por sección aplicada relevante"), una regla real de producción que
  bajar rompería para las 8 unidades, no solo para el corpus; (2) `neg_19` (Familias
  de Distribuciones, §2.9 de U3) nunca tiene `\boxed{}` en ninguna de sus 8
  sub-secciones en la unidad real — verificado por conteo exhaustivo — porque es un
  catálogo teórico de referencia, no un ejemplo resuelto; `@Scientist` exige
  `\boxed{}` (Gold Standard §3 punto 5), también correcto en producción. Ambos
  casos son fragmentos que, por construcción, no pueden probar un estándar que el
  Gold Standard aplica a nivel de sección aplicada completa, no de sub-fragmento
  arbitrario — la misma limitación que ya reconoce D6 más abajo, aplicada ahora
  también a `@Analyst`/`@Scientist`, no solo a `@Librarian`.

  De los 10 falsos positivos restantes en la cifra de hoy, 9 son estos negativos
  reales sin corregir por ser límite estructural del corpus (no arreglables sin
  fusionar fragmentos que el corpus ya trata como casos separados), documentados
  caso por caso en `etiquetas.json`. Los 15 casos sintéticos de falsedad semántica
  se comportan exactamente como predice el diseño (§2.1, "verificación numérica y
  estructural, no semántica"): el Consejo no los detecta, 15/15 falsos negativos —
  sin cambio respecto a la medición anterior, como se esperaba (M2 no tocó esa
  dimensión). El runner actúa como el juez de segunda pasada que antes faltaba (D5,
  auditoría 2026-09-15), pero la cifra real obliga a matizar D6: el κ referenciado
  aquí mide el Consejo contra fragmentos de corpus, no contra unidades de
  producción completas, y no debe citarse como la precisión del Consejo en
  producción sin esa salvedad.

  **A3-U (medición contra unidades completas, complementaria a A3, 2026-09-17):**
  para responder directamente la salvedad de D6 de arriba, se añadió un segundo
  experimento independiente que no reemplaza a A3
  (`docs/superpowers/specs/2026-09-16-a3-unidades-completas-design.md`,
  `docs/superpowers/audits/2026-09-17-precision-consejo-unidades.md`): 8 unidades
  completas de producción sin modificar (negativos) más 8 copias con exactamente un
  `\boxed{}` alterado (`boxed_desincronizado`, el único tipo de fallo del catálogo
  de A3 con mecanismo real confirmado en `_contraste_boxed.py`). Resultado:
  precisión 1.0, recall 0.375, κ de Cohen 0.375 (VP=3, FN=5, FP=0, VN=8). El
  desarrollo de A3-U destapó además un bug de infraestructura no relacionado con el
  Consejo (crash nativo de `scipy`/OpenBLAS vía `seaborn.histplot(kde=True)`, que
  bloqueaba `@Engineer` en unidades reales y afectaba 14-15 tests preexistentes del
  repo); se resolvió fijando `scipy==1.14.1` en el entorno `ia_stats`, sin tocar
  código del Consejo.

  A3 mide detección fina por 17 tipos de fallo contra fragmentos aislados; A3-U
  mide específicamente detección de `boxed_desincronizado` contra unidades
  completas de producción con exactamente 1 valor alterado. Difieren en dos ejes:
  A3 fuerza al Consejo a evaluar fragmentos que, por construcción, no siempre
  pueden cumplir un criterio de sección completa (gráfico, `\boxed{}`); y A3
  mezcla tipos de fallo que el Consejo detecta con tipos que no detecta por diseño
  (falsedad semántica sin LLM, ver H-03 más abajo), mientras A3-U aísla el tipo que
  sí detecta. A3-U no es comparable 1:1 con la cifra global de A3 — es una
  medición más estrecha, pensada para aislar si el artefacto de fragmentación (y
  no una limitación real de detección) es lo que deprime la cifra de A3: los 0
  falsos positivos (VN=8/8) confirman que el Consejo aprueba limpio las unidades
  completas reales sin el artefacto de recorte de A3. El resultado, sin embargo,
  matiza también el optimismo de esa hipótesis: recall 0.375 (3 de 8 alteraciones
  detectadas) muestra que ni siquiera dentro de una unidad completa el mecanismo de
  contraste `\boxed{}`↔código detecta todo `boxed_desincronizado` real — depende de
  que el rótulo de la cantidad coincida con lo que el código imprime literalmente
  (`_el_codigo_apunta_al_valor`), condición que no todas las unidades cumplen para
  cualquier `\boxed{}` arbitrario. A3-U demuestra precisión perfecta sin falsos
  positivos en unidades completas, no que el Consejo "detecte todo" — la cifra
  correcta a citar es esa, no una lectura más fuerte. Esto cierra D6 por completo:
  ya no hace falta la salvedad de "verificar si hay un reporte más reciente antes
  de citar la cifra de A3 como la precisión del Consejo en producción" — A3-U es
  esa cifra de producción, con sus propios límites ya documentados aquí mismo.

  **Fix de recall (2026-09-18, auditoría comparativa externa post-A3-U):** de los 5
  falsos negativos originales, `pos_u2_probabilidad_combinatoria.md` tenía una causa
  raíz distinta de los otros 4 y arreglable sin riesgo: el código de esa sección
  imprime `print(f"P(A) = |A|/|Omega| = {p_A:.4f}")` — una línea con DOS `=`
  (rótulo = expresión intermedia = valor final). `_ROTULO_INLINE` solo reconocía
  `identificador = número` en el mismo segmento; el primer `=` dejaba `|A|/|Omega|`
  de un lado (no es un número ni cabe en la clase de caracteres del identificador,
  que no admite `/` ni `|`), así que la línea completa no producía ningún emparejamiento
  y el rótulo "P(A)" quedaba sin valor con el que contrastarse. Se agregó
  `_ROTULO_CADENA` (mismo archivo, `_contraste_boxed.py`) como fallback exclusivo de
  `_valores_junto_al_rotulo` — solo se evalúa cuando `_ROTULO_INLINE` no encontró nada
  en la línea, así que no cambia ningún caso ya cubierto — con la misma disciplina de
  acotamiento contra ReDoS que `_ROTULO_INLINE` (identificador `{1,40}`, sin `\s*` sin
  cota, verificado con test de rendimiento dedicado). TDD completo: test RED que
  reproduce el caso real de `pos_u2` (`test_rotulo_con_doble_asignacion_en_cadena_se_reconoce`,
  `tests/council/test_engineer_agent.py`), GREEN tras el fix.

  **Important de revisión (`python-reviewer`, mismo día):** la primera versión del
  fallback se activaba solo "si `_ROTULO_INLINE` no encontró ningún par en la línea"
  — con 3+ signos `=` (`rótulo = intermedio = intermedio2 = valor`), el ÚLTIMO
  segmento por sí solo (`intermedio2 = valor`) sí cumple el patrón de `_ROTULO_INLINE`,
  así que `pares` nunca quedaba vacío y el fallback no se activaba: el rótulo real
  seguía sin compararse, reproduciendo en silencio el mismo defecto que el fix
  pretendía cerrar. Corregido cambiando la condición de activación de "la lista está
  vacía" a "ningún par ya encontrado tiene el nombre que se busca" — decidido dentro
  de `_valores_junto_al_rotulo`, que es quien conoce `nombre`. Test RED nuevo
  (`test_rotulo_con_triple_asignacion_en_cadena_se_reconoce`) reproduce el caso de 3
  `=`, verificado como extensión natural del caso real (agregar una variable
  intermedia rotulada al mismo `print`), no hipotético.

  Verificación final: 34/34 tests de `test_engineer_agent.py`, 138/138 de
  `tests/council/`, 325/325 de la suite completa, sin regresiones. Resultado
  re-medido con el runner real tras ambos fixes: **precisión 1.0, recall 0.5, κ de
  Cohen 0.5 (VP=4, FN=4, FP=0, VN=8)** — sube de 3/8 a 4/8 alteraciones detectadas,
  sin introducir ningún falso positivo nuevo (los 8 negativos siguen en 0 hallazgos).

  Los 4 falsos negativos restantes (`pos_u1`, `pos_u3`, `pos_u5`, `pos_u7`) tienen una
  causa raíz distinta y **no se tocaron**: son `\boxed{}` en secciones sin código
  propio (ejemplos analíticos resueltos a mano, o secciones puramente gráficas sin
  ningún `print`), contrastados por `_contrastar_contra_la_unidad` contra la salida de
  **toda la unidad**, no de la sección. Ese mecanismo acepta el valor si aparece en
  cualquier parte del stdout de la unidad completa — no exige que esté junto a un
  rótulo reconocible como sí lo hace `_el_codigo_apunta_al_valor` a nivel de sección.
  Arreglarlo con el mismo rigor requeriría rediseñar ese contraste para exigir
  también un rótulo cercano, un cambio de diseño más amplio que el fix de línea de
  arriba, con mayor riesgo de introducir falsos positivos en los 8 negativos reales.
  Queda documentado aquí como el próximo candidato si se decide seguir subiendo el
  recall, no como una tarea pendiente de alcance menor.

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
* **`@Architect` es advisory-only en el flujo por lección** (§2.1) — la completitud
  curricular de las 8 `UNIDAD_*` no se audita en el pipeline automático por defecto.
* **Bloques de código que dependen del runtime de notebook, la red, o los propios
  agentes del repo se omiten** de la ejecución de `@Engineer` (§2.1) — no se ejecutan
  ni se cuentan como error por no ejecutarse.
* **Un valor numéricamente correcto con un nombre semánticamente incorrecto no se
  detecta (N-04, auditoría 2026-09-13).** `_el_codigo_apunta_al_valor` (en
  `_contraste_boxed.py`) contrasta cifras, no el nombre en prosa que las acompaña:
  un `\boxed{0.1281}` que el código produce como p-valor pero que el texto etiqueta
  "significancia crítica" no genera discrepancia -el número coincide-. Distinguir
  esto exige comprensión semántica del lenguaje natural, no solo del valor numérico;
  es el mismo límite que H-03 (interpretación semántica del contenido, arriba) pero
  aplicado a la etiqueta de un resultado en vez de a una afirmación completa.
* **El gate de producción de `@Safety_Gate` solo bloquea por hallazgos críticos, no
  por cualquier violación de supuestos detectada (I-3, auditoría 2026-09-13).**
  `SafetyGateAgent` devuelve `{"passed", "warnings", "critical"}` -`passed` es
  `False` en cuanto hay un solo *warning*, sin llegar a crítico-, pero
  `orchestrator_agent.py:160` consulta únicamente `safety_result["critical"]`
  antes de aprobar una unidad; `passed` (`False` con supuestos no verificados
  pero no críticos) nunca se consulta en ese punto del pipeline de producción.
  Es una decisión de diseño ya tomada -no todo hallazgo de supuestos debe
  bloquear la publicación-, pero no estaba declarada explícitamente como tal
  en esta sección hasta ahora. Nota de verificación: el commit `559627d`
  (2026-08-19, no 2026-09-04 como se asumió al
  redactar este hallazgo) corrigió dos falsos positivos reales de `SafetyGateAgent`
  (identificadores de código como "regression" y falta de alias en español) — no es
  el origen de esta brecha, que es estructural al diseño del gate, no una regresión
  introducida por ese fix.

### 5.2 Hallazgos cerrados en rondas posteriores (registro, I-6)

Esta subsección existe porque la auditoría 2026-09-14 (96.4/100) señaló
que `GOVERNANCE.md` no registraba los hallazgos cerrados en el plan
`cierre-n05-n06-n07` (I-6, hallazgo de higiene sin descuento de
puntaje). Registro mínimo para no repetir la brecha:

* **N-05** (ALTO): marca simbólica decorativa con valor real desactivaba
  el fix de N-03. Cerrado en `_contraste_boxed.py::_es_formula_simbolica`.
* **N-06** (MEDIO): `subprocess.run(["npx", ...])` fallaba en Windows sin
  `shell=True`. Cerrado en `mermaid_renderer.py` con `shutil.which("npx")`.
* **N-07** (MEDIO): afirmación sin artefacto versionado sobre el
  recálculo de `\boxed{}`. Cerrado con
  `docs/superpowers/audits/2026-09-14-recalculo-boxed-completo.md`.
* **I-5** (INFO): notebooks sin `kernelspec`, `nbconvert --execute` caía
  al Python del sistema. Cerrado en `notebook_compiler_agent.py`.
* **N-08** (ALTO): cuarta evasión adversarial, misma causa raíz que
  protegía a U7 §6.2. Cerrado por la vía estructural en
  `_contraste_boxed.py::_valor_final_declarado` (ver este mismo ciclo).

---

*Este documento describe el estado real del proceso de este repositorio. El contenido se escribe y revisa directamente (sesiones con el profesor, sin agentes orquestando la redacción); lo que sí corre como software es el Consejo de 8 Expertos que audita el resultado, con el alcance y los límites declarados en §2.1 y, con cifras concretas, en §5.1. Cualquier cambio en lo que esos agentes verifican debe actualizarse aquí para reflejar exactamente lo que corre, no lo que se aspira a construir.*
