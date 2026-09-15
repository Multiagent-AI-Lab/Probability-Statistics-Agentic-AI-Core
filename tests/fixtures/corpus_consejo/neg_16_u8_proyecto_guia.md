## 2. Guía Estructurada del Proyecto Integrador (Paso a Paso)

El Proyecto Integrador **no es un ejercicio más con dataset dado** — es un proyecto abierto donde cada estudiante elige o construye su propio conjunto de datos sobre un sistema nanotecnológico real, y lo somete a las cinco fases metodológicas del curso. A diferencia de los ejercicios de la §12 (dataset fijo, solución numérica única verificable por script), aquí **no existe una respuesta numérica de referencia**: el criterio de éxito de cada fase es un conjunto de invariantes estructurales (¿está la sección? ¿tiene el número mínimo de elementos que exige el método?) más una rúbrica cualitativa que un humano aplica sobre el razonamiento — igual que evaluaría un reporte técnico real de laboratorio.

**Fuente de datos.** La vía recomendada es la **Materials Project API** (§8, ya usada en esta unidad para comparar band gaps): el estudiante elige 2 o más materiales, propiedades o condiciones de síntesis a comparar, y extrae sus propios valores (`mp-api`, documentado en [materialsproject.org/api](https://next-gen.materialsproject.org/api) con registro gratuito). Alternativas igualmente válidas si el estudiante ya tiene acceso a ellas: datos de un laboratorio de la propia carrera (síntesis, caracterización), un dataset público de Kaggle/UCI sobre nanomateriales, o mediciones simuladas con un generador aleatorio **siempre que el estudiante justifique por escrito los parámetros elegidos** (p. ej. "$\sigma=1.8$ nm porque el método de síntesis reportado en [DOI] tiene ese CV%") — lo que no se acepta es un dataset copiado sin elección propia ni justificación, porque eso es exactamente el ejercicio de dataset fijo que este proyecto reemplaza.

### 2.1 Las Cinco Fases, con Entregable Verificable y Fecha Sugerida

El proyecto se entrega **por fases a lo largo del semestre**, no de un solo golpe en la última semana — cada checkpoint se apoya en la unidad que se está cursando en ese momento, así que la fase se entrega cuando el curso ya dio las herramientas para hacerla bien, y un problema de planteamiento (Fase 1) se detecta en la semana 2, no en la semana 16 cuando ya es tarde para cambiar de pregunta.

| Fase | Qué produce el estudiante | Entregable verificable | Semana sugerida (curso de 16 semanas) |
|---|---|---|---|
| **Fase 1: Planteamiento del Problema** | Elige su sistema nanotecnológico, extrae o diseña su dataset propio, define variables físicas y formula $H_0$/$H_1$ | Documento de 1 página: fuente de datos citada (URL/DOI), tabla de variables con unidades, $H_0$ y $H_1$ en notación formal, justificación de por qué la pregunta es relevante en nanotecnología | Semana 2-3 (tras U1, con Fundamentos de Estadística Descriptiva ya vistos) |
| **Fase 2: Análisis Exploratorio Descriptivo (EDA)** | Estadísticos descriptivos de su propio dataset y al menos un gráfico exploratorio (histograma o boxplot); la verificación formal de supuestos (normalidad, homocedasticidad) se pospone a la Fase 3, cuando esas pruebas ya se han enseñado | Notebook con celdas ejecutadas: $\bar{X}$, $S^2$, IQR por grupo + ≥1 figura | Semana 6-7 (tras U1, con las medidas descriptivas y la visualización exploratoria ya vistas) |
| **Fase 3: Verificación de Supuestos y Derivación Simbólica en SymPy** | Verifica formalmente normalidad y homogeneidad de varianzas con Shapiro-Wilk y Levene, y deriva en SymPy la expresión exacta del estadístico de prueba que va a usar según lo que esos supuestos indiquen (no solo la ejecuta con SciPy: la deriva primero) | Notebook con `stats.shapiro` + `stats.levene` con sus $p$-valores impresos, y una celda de SymPy que define los símbolos, construye la fórmula del estadístico (p. ej. $t$, $F$, o $\chi^2$ según la prueba elegida) y evalúa la expresión simbólica con los valores numéricos de su propio dataset — coherente con el Ciclo de Verificación Triple de `GOVERNANCE.md` | Semana 12-13 (tras U6, con Shapiro-Wilk, Levene y el Ciclo de Verificación Triple ya vistos y practicados varias veces) |
| **Fase 4: Solución Computacional** | Ejecuta la prueba de hipótesis con SciPy/statsmodels sobre su propio dataset y simula la curva de potencia por Monte Carlo | Notebook con `scipy.stats.ttest_ind`/`f_oneway`/equivalente + gráfico de la curva de potencia simulada, con el resultado simbólico de la Fase 3 contrastado numéricamente contra este resultado computacional (tolerancia relativa razonable, no exacta — son dos rutas de cómputo distintas) | Semana 15 (tras U7, con la metodología completa de pruebas de hipótesis ya vista) |
| **Fase 5: Conclusiones e Interpretación** | Traduce el resultado estadístico en una decisión técnica industrial, discute limitaciones de su propio dataset (tamaño de muestra, supuestos no verificados, generalización) | Reporte final (2-3 páginas o notebook con celdas Markdown de cierre): decisión de $H_0$, interpretación en lenguaje de la aplicación (nunca solo "$p<\alpha$"), y una sección explícita de **limitaciones** propias del dataset elegido | Semana 15-16 (cierre, dentro de U8) |

El siguiente DAG resume la dependencia secuencial entre las cinco fases de la tabla anterior — cada fase consume el entregable verificado de la anterior, nunca al revés:

```mermaid
graph TD
    F1["Fase 1: Planteamiento (dataset propio + H0/H1)"]
    F1 --> F2["Fase 2: Analisis Exploratorio Descriptivo (EDA)"]
    F2 --> F3["Fase 3: Verificacion de Supuestos y Derivacion Simbolica (modelo)"]
    F3 --> F4["Fase 4: Solucion Computacional (validacion numerica vs simbolica)"]
    F4 --> F5["Fase 5: Conclusiones e Interpretacion (reporte final)"]
```

Las cuatro primeras fases son **checkpoints intermedios** que el profesor revisa y retroalimenta antes de que el estudiante avance a la siguiente — así un error de planteamiento (p. ej. una $H_1$ mal formulada, o un dataset sin varianza suficiente para ninguna prueba con potencia razonable) se corrige en la Fase 1 o 2, no se descubre en la Fase 4 cuando ya no hay tiempo de recolectar datos nuevos. La Fase 5 integra las cuatro anteriores en el entregable final.

### 2.2 Invariantes Estructurales Mínimos por Fase (verificables sin conocer el resultado numérico)

Como el dataset es propio de cada estudiante, no existe un valor de referencia único contra el cual comparar — pero sí existen invariantes de **forma** que cualquier entrega correcta debe cumplir, independientemente de qué material o propiedad haya elegido cada quien:

- **Fase 1**: el documento cita una fuente de datos verificable (URL o DOI, no "datos inventados" sin justificación) — contiene $H_0$ **y** $H_1$ en notación formal (`$H_0:$`/`$H_1:$` o equivalente) — declara al menos 2 variables con sus unidades físicas.
- **Fase 2**: contiene al menos 1 figura (`plt.`/`sns.`) — reporta medias y varianzas/desviaciones estándar de cada grupo.
- **Fase 3**: el notebook contiene al menos una llamada a `stats.shapiro` **y** una a `stats.levene` (o su justificación explícita de por qué no aplican, p. ej. una sola muestra) — usa `sympy` (import y al menos un `sp.Symbol`/`sp.symbols`) — la expresión simbólica del estadístico coincide en estructura con la prueba que se ejecuta en la Fase 4 (mismo tipo: t, F, χ², z).
- **Fase 4**: el notebook ejecuta una función de `scipy.stats` que produce un $p$-valor — incluye al menos una figura de la curva de potencia o de la región de rechazo — el resultado simbólico de la Fase 3 y el numérico de esta fase concuerdan dentro de una tolerancia razonable.
- **Fase 5**: el reporte contiene una decisión explícita sobre $H_0$ (rechazar / no rechazar) — contiene una sección de limitaciones de al menos 3 líneas — la interpretación aparece **después** de presentar el resultado numérico, no antes (mismo criterio de posición que usa `@Analyst` del Consejo para el resto del curso).

Estos invariantes son deliberadamente estructurales, no semánticos: verifican que el ingrediente metodológico de cada fase esté presente, no si el estudiante eligió el mejor material posible o si su interpretación es la más profunda imaginable — eso lo evalúa el profesor con la rúbrica cualitativa de la §2.3. Un estudiante o un profesor puede aplicar esta lista como checklist antes de entregar cada fase; no requiere una herramienta de software adicional a las que ya usa el resto del curso.

### 2.3 Rúbrica de Evaluación del Proyecto Integrador

Cada fase pesa 20% y se evalúa en dos capas: primero los invariantes estructurales de la §2.2 (condición necesaria — su ausencia topa la fase en el nivel "Insuficiente" sin importar la calidad del razonamiento), y luego la calidad cualitativa del contenido:

| Fase | Insuficiente (0-9%) | Aceptable (10-15%) | Sobresaliente (16-20%) |
|---|---|---|---|
| **1. Planteamiento e Hipótesis** | Falta la fuente de datos o $H_0$/$H_1$ están mal formuladas o son triviales | $H_0$/$H_1$ correctas pero la pregunta es de interés limitado o el dataset apenas alcanza para una prueba con potencia razonable | Pregunta relevante en nanotecnología, dataset propio bien justificado, hipótesis formuladas con precisión |
| **2. Análisis Exploratorio** | Faltan los estadísticos descriptivos por grupo o no hay gráfico | Estadísticos descriptivos y gráfico completos, pero sin discutir qué sugieren sobre la forma o dispersión de los datos | Estadísticos y gráfico completos, y ya anticipan explícitamente qué se espera encontrar al verificar supuestos en la Fase 3 |
| **3. Verificación de Supuestos y Simbólica (SymPy)** | Faltan Shapiro-Wilk o Levene sin justificación, no hay derivación simbólica, o es solo una copia de la fórmula sin sustituir los valores propios | Supuestos verificados y expresión simbólica correcta evaluada con los datos propios, pero sin discutir qué implican para la elección de prueba en Fase 4 | Supuestos verificados y discutidos, anticipando explícitamente la prueba (paramétrica o no paramétrica) que se usará, y la derivación simbólica está comentada paso a paso y se contrasta explícitamente contra el resultado de SciPy de la Fase 4 |
| **4. Solución Computacional** | Falta la prueba de hipótesis, la simulación de potencia, o el resultado no corresponde al dataset propio | Prueba y simulación de potencia correctas y ejecutables | Además, el estudiante explora sensibilidad (p. ej. cómo cambia la potencia con $n$ o con $\alpha$) más allá del mínimo pedido |
| **5. Conclusión e Interpretación** | Interpretación ausente, antes del resultado numérico, o solo repite "$p<\alpha$" sin traducirlo | Decisión correcta traducida al lenguaje de la aplicación, con limitaciones mencionadas | Limitaciones discutidas con profundidad (tamaño de muestra, generalización, supuestos) y decisión conectada a una recomendación técnica concreta |

---

## 3. Ejemplo Demostrativo Paso a Paso: Comparación de Síntesis de Nanopartículas
