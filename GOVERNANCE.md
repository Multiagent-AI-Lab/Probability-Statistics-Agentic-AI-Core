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

1. **Teoría Completa**: al menos 800 palabras de desarrollo teórico formal.
2. **Ejemplo Analítico**: la sección contiene ejemplos desarrollados paso a paso con explicación.
3. **Verificación SymPy**: manipulación simbólica de fórmulas con `sympy.symbols` antes de sustituir valores numéricos.
4. **Contexto Nanotecnológico**: todo ejemplo usa datos o problemas de nanotecnología reales o realistas (nunca ejemplos genéricos de estadística).
5. **Solución en `\boxed{}`**: cualquier valor numérico final de un ejemplo analítico se resalta con `\boxed{...}`.
6. **Solución Computacional SciPy**: reproducción del resultado mediante `scipy.stats` o `statsmodels` ejecutado.
7. **Visualización Profesional**: al menos 2 gráficos (matplotlib/seaborn) por sección aplicada relevante.
8. **Interpretación Post-Gráfico**: explicación de qué significa el resultado en el contexto de nanotecnología, posterior a cualquier visualización.
9. **Diccionario de Variables**: cada unidad cierra con la notación completa usada, verificada contra el código/ejemplo real de la unidad.

---

## 4. Verificación de Símbolos en el Diccionario de Variables

Cada entrada del Diccionario de Variables debe corresponder a un símbolo o variable usada en un ejemplo REAL Y EJECUTADO de la propia unidad — una tabla de sintaxis genérica, un docstring en prosa, o una mención aislada en teoría sin ejemplo aplicado no cuentan como uso verificado. Antes de agregar o aprobar una entrada, releer el bloque de código o el ejemplo analítico que la usa.

---

*Este documento describe el estado real del proceso de este repositorio. El contenido se escribe y revisa directamente (sesiones con el profesor, sin agentes orquestando la redacción); lo que sí corre como software es el Consejo de 8 Expertos que audita el resultado, con el alcance y los límites declarados en §2.1. Cualquier cambio en lo que esos agentes verifican debe actualizarse aquí para reflejar exactamente lo que corre, no lo que se aspira a construir.*
