# GOVERNANCE.md

## 1. Propósito de este documento

Este archivo documenta el patrón pedagógico central que estructura el contenido de "Probabilidad y Estadística Inferencial" y el estándar de calidad que cada unidad debe cumplir. A diferencia de un pipeline de generación automatizada, el contenido de este curso se escribe y revisa directamente (sesiones de trabajo con el profesor, sin agentes de IA orquestando la redacción) — este documento es una guía de convenciones para quien escribe o revisa contenido, no la descripción de un sistema de software que ejecute el proceso.

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

*Este documento describe el estado real del proceso de este repositorio — no un sistema de agentes en ejecución. Cualquier automatización futura del proceso de generación de contenido debe actualizarlo para reflejar exactamente lo que corre, no lo que se aspira a construir.*
