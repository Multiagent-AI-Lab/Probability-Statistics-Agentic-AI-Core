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

  **Nota de vigencia (2026-09-19):** el pin es un workaround de ese crash puntual,
  no una decisión de vigencia del stack — a la fecha de esta nota, `scipy` va 2
  versiones minor por detrás de la estable real (1.18.1, ago-2026). Antes de subir
  la versión: reproducir el crash original con la nueva versión primero; si ya no
  ocurre, quitar el pin en el mismo commit que actualiza esta nota (declarado
  también en `environment.yml`/`requirements.txt`).

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

  Antes de este fix, los 4 falsos negativos restantes (`pos_u1`, `pos_u3`, `pos_u5`,
  `pos_u7`) tenían una causa raíz común: son `\boxed{}` en secciones sin código propio
  (ejemplos analíticos resueltos a mano, o secciones puramente gráficas sin ningún
  `print`), contrastados por `_contrastar_contra_la_unidad` contra la salida de **toda
  la unidad**, no de la sección — ese mecanismo acepta el valor si aparece en
  cualquier parte del stdout de la unidad completa, y sin ningún stdout que lo
  contenga (o sin ningún código que lo produzca) no había forma de detectar la
  desincronización.

  **Fix de `pos_u7` (2026-09-18, mismo día, investigación separada):** `pos_u7`
  resultó tener una causa raíz distinta de los otros 3, y barata de cerrar sin tocar
  el mecanismo de nivel de unidad: la lección real (`UNIDAD_7 §2.5`) ya escribe, en
  la oración inmediatamente posterior al `\boxed{}` de un ejemplo puramente
  analítico, el mismo valor en prosa normal ("Como $0.0108 < 0.05$, el p-valor
  confirma..."). Barrido completo de las 8 unidades reales confirmó que este patrón
  ("Como/Con `<número>`" repitiendo o comparando el valor del `\boxed{}` inmediato)
  ocurre solo 2 veces en todo el curso (`UNIDAD_7 §1.7` y `§2.5`) — raro pero real, y
  detectable sin ejecutar ningún código: la propia inconsistencia textual es la
  evidencia. Se agregó `_contradicho_por_prosa_inmediata` en `_contraste_boxed.py`,
  que corre ANTES del filtro `_es_valor_trivial` (un p-valor de 0.02 cae en el rango
  que ese filtro descarta por diseño para otros fines — índices, exponentes — pero
  aquí sí es un resultado con significado).

  Dos falsos positivos reales aparecieron durante el TDD de este fix, ambos
  detectados por el propio gate adversarial (`test_contenido_real_correcto_sigue_aprobando`)
  contra contenido real correcto, no en un caso sintético: (1) la primera versión
  solo miraba el PRIMER número tras "Como/Con", pero `UNIDAD_1 §2.4` tiene "Como
  $40.5 > 15.725$" con el valor del `\boxed{}` en la SEGUNDA posición — corregido
  exigiendo que el valor esperado coincida con CUALQUIERA de los números de la
  comparación, no específicamente el primero; (2) con dos `\boxed{}` seguidos en la
  misma sección (`UNIDAD_1 §2.4` de nuevo: 1.35 y 15.725), la ventana de búsqueda
  tras el primero alcanzaba a cruzar el segundo y capturaba SU confirmación (números
  sin relación con el primer valor) — corregido cortando la ventana en el próximo
  `\boxed{}` de `cuerpo`, no solo por longitud fija. Ambos casos quedaron como tests
  de regresión dedicados.

  Resultado re-medido con el runner real: **precisión 1.0, recall 0.625, κ de Cohen
  0.625 (VP=5, FN=3, FP=0, VN=8)** — sube de 4/8 a 5/8 alteraciones detectadas, sin
  introducir ningún falso positivo nuevo.

  Los 3 falsos negativos restantes (`pos_u1`, `pos_u3`, `pos_u5`) **no se tocaron**:
  no tienen el patrón "Como/Con" ni ningún stdout que los contraste — arreglarlos
  con el mismo rigor requeriría rediseñar `_contrastar_contra_la_unidad` para exigir
  un rótulo cercano en vez de "aparece en algún lado de la unidad", un cambio de
  diseño más amplio, con mayor riesgo de introducir falsos positivos en los 8
  negativos reales. Queda documentado aquí como el próximo candidato si se decide
  seguir subiendo el recall, no como una tarea pendiente de alcance menor.

  **Fix de `pos_u1` y `pos_u3` (2026-09-19/20, mismo día, investigación separada):**
  ambos resultaron tener una causa raíz común, distinta de `pos_u7` y barata de
  cerrar: son ejemplos analíticos sin código propio y sin patrón "Como/Con", pero la
  propia expresión matemática que precede al `\boxed{}` ya contiene una operación
  aritmética completa de 2 operandos (`UNIDAD_1 §2.4`: "13.70 - 12.35 =
  \boxed{1.35}"; `UNIDAD_3 §3.5`: "20 \times 0.05 = \boxed{1.0}"). Se agregó
  `_contradicho_por_aritmetica_propia` en `_contraste_boxed.py`, deliberadamente
  estrecho: solo evalúa cuando hay EXACTAMENTE 2 operandos numéricos (sin variables,
  fracciones ni paréntesis) y el `\boxed{}` tiene un único número — un barrido de
  las 8 unidades reales mostró que la mayoría de expresiones tienen 3+ operandos o
  formato compuesto, y ampliar el alcance a esos casos requeriría un evaluador
  aritmético real (tipo `sympy.sympify`) con su propio ciclo de TDD adversarial, no
  justificado solo para 1-2 unidades más.

  Dos falsos positivos reales aparecieron durante el desarrollo, ambos sobre
  contenido real correcto: (1) `neg_u5_variables_continuas.md` tiene
  `\boxed{0.86638 \quad (86.64\%)}` — dos números dentro del `\boxed{}` (el valor y
  su versión en porcentaje); el extractor existente toma "el último número"
  (86.64) como valor a contrastar, pero la operación real da 0.86638 (el
  *primero*) — corregido exigiendo un único número dentro del `\boxed{}` antes de
  evaluar, en vez de adivinar cuál usar; (2) `python-reviewer` encontró, evaluando
  la función en aislamiento (no solo vía A3-U), que el regex de 2 operandos podía
  matchear el *sufijo* de una expresión de 3+ operandos —"0.25 + 0.45 + 0.30 =
  \boxed{1.0}" (`UNIDAD_2 §1.3`, aritmética correcta) matcheaba solo "0.45 + 0.30 ="
  y reportaba 0.75 ≠ 1.0 como discrepancia falsa—. Esto no se manifestaba en A3-U
  porque esa sección real tiene código ejecutable propio (el mecanismo nunca se
  invoca ahí), una coincidencia del contenido actual, no una garantía de la
  función. Corregido verificando que nada preceda al operando izquierdo del match
  salvo espacio — un dígito, punto, `)` u operador aritmético justo antes es
  evidencia de un tercer operando. Ambos casos quedaron como tests de regresión
  dedicados, incluyendo el caso de 3+ operandos evaluado sin código acompañante
  (la condición exacta que antes ocultaba el bug).

  Resultado re-medido con el runner real tras ambos fixes: **precisión 1.0, recall
  0.75, κ de Cohen 0.75 (VP=6, FN=2, FP=0, VN=8)** — sube de 5/8 a 6/8 alteraciones
  detectadas, sin introducir ningún falso positivo nuevo. Verificación final:
  46/46 tests de `test_engineer_agent.py`, 150/150 de `tests/council/` (incluido el
  gate adversarial completo), sin regresiones.

  Los 2 falsos negativos restantes (`pos_u1` y `pos_u5`) tienen causas distintas
  de las que este fix cierra, ninguna cubierta por el mecanismo actual: `pos_u1`
  altera el `\boxed{}` de la MEDIA (`UNIDAD_1 §6.4`), una sección puramente
  gráfica (`plt.show()`, sin ningún `print`) — el mismo patrón "sin stdout que
  contrastar" de U1/U3/U5 antes de esta ronda de fixes, distinto del `\boxed{}`
  de IQR (`§2.4`) que sí quedó cubierto; `pos_u5` sigue excluido a propósito por
  su formato compuesto (ver el falso positivo (1) de arriba). El mismo criterio
  de costo/riesgo aplicado en cada ronda anterior sigue vigente: cada mejora
  adicional exige un evaluador más completo (aritmético o de otra naturaleza),
  con más superficie para el mismo tipo de falso positivo ya encontrado dos
  veces en este mecanismo.

  **Revisión de `python-reviewer` (mismo día, sin Critical ni Important):** confirmó
  el regex `_CONFIRMACION_EN_PROSA` seguro contra ReDoS (cuantificador `.{0,40}?`
  acotado, ventana pre-cortada a 300 caracteres, probado con entradas adversariales
  diseñadas para maximizar backtracking — <2ms). Dos Minor aplicados: (1) el prefijo
  `\boxed{` que corta la ventana de búsqueda se extrajo a `_PREFIJO_BOXED`, constante
  compartida con `_BOXED` de `engineer_agent.py` (que reconoce solo esa sintaxis
  exacta, sin espacio) — evita que ambos puntos se desincronicen en silencio si el
  patrón de `\boxed{}` se relaja en el futuro; (2) nuevo test dedicado para el caso
  del `\boxed{}` contradicho siendo el último de su sección (`proximo_boxed == -1`
  en `_contradicho_por_prosa_inmediata`), antes ejercitado solo de forma incidental.
  Límite conocido señalado y no cerrado (bajo riesgo, sin evidencia en las 8 unidades
  reales): `_CONFIRMACION_EN_PROSA` solo reconoce el operador de comparación en
  notación matemática (`<`, `>`, `=`), no en palabras ("es menor que") — el patrón
  real verificado en el curso usa siempre notación matemática, así que esto no
  afecta la cifra de recall citada arriba, pero limitaría la detección si una futura
  unidad escribe la comparación en prosa pura.

  **Fix de `pos_u5` (2026-09-23):** el falso negativo restante en el formato
  compuesto se cerró sin reabrir el falso positivo (1) que motivó excluirlo. La
  causa raíz era la misma en ambos casos — dos números dentro del `\boxed{}`
  ("`valor \quad (porcentaje\%)`") — pero la relación entre ambos números es
  distinguible: si el segundo es el primero multiplicado por 100 (con la misma
  tolerancia relativa que el resto del módulo), el formato es reconocible como
  "valor + su vista porcentual" y no hay ambigüedad sobre cuál contrastar contra
  la aritmética — es el primero. Se agregó `_valor_del_formato_porcentaje` en
  `_contraste_boxed.py`: con 2 números que cumplen esa relación, evalúa la
  aritmética contra el primero; con 2 números que no la cumplen (posible formato
  compuesto de naturaleza distinta, dos datos independientes en vez de un valor y
  su derivado), sigue absteniéndose igual que antes — el mismo principio
  conservador de toda la ronda anterior. `neg_u5` (contenido real, sin alterar)
  sigue en verde porque su relación SÍ se cumple (0.86638 × 100 ≈ 86.64) y la
  aritmética real coincide; el caso adversarial nuevo confirma que un valor
  alterado con esa misma relación consistente (0.90000/90.00%, pero la resta real
  da 0.86638) sí se detecta.

  Resultado re-medido con el runner real: **precisión 1.0, recall 0.875, κ de
  Cohen 0.875 (VP=7, FN=1, FP=0, VN=8)** — sube de 6/8 a 7/8 alteraciones
  detectadas, sin falsos positivos nuevos. Verificación: 48/48 tests de
  `test_engineer_agent.py`, 69/69 de engineer_agent + gate adversarial juntos,
  342/342 en la suite completa.

  Único falso negativo restante: `pos_u1` (`UNIDAD_1 §6.4`, la sección
  puramente gráfica sin `print` ni operación de 2 operandos en el texto — ver
  el párrafo anterior). Cerrarlo exigiría ejecutar el código real y contrastar
  contra su efecto (el propio gráfico), un cambio estructural fuera de
  proporción para 1 caso sintético del corpus; queda documentado como límite
  estructural, no como tarea pendiente.

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
