# UNIDAD 5: Variables Aleatorias Continuas y Modelos de Simulación
## Asignatura: Probabilidad y Estadística Inferencial
### UCEMICH — Ingeniería en IA y Nanotecnología
### Autor y Profesor: Mtro. Luis José Yudico Anaya

---

#### TEMA: DISTRIBUCIONES DE PROBABILIDAD CON PYTHON

## Modelos para Variables Aleatorias Continuas

### Listado de las distribuciones de probabilidad continuas más utilizadas

En las disciplinas de nanotecnología, ciencias de los materiales, inteligencia artificial, diseño de experimentos y pruebas de hipótesis, se destacan las siguientes distribuciones de probabilidad continuas:

##### Nanotecnología

1. **Distribución Normal**
   - **Uso**: Modelar variaciones en características físicas de nanopartículas, como tamaño y forma.
   - **Ejemplo**: La distribución del tamaño de partículas en una muestra de nanopartículas de sílice, donde la mayoría de las partículas presentan un tamaño cercano a la media, con algunas variaciones hacia los extremos.

2. **Distribución Log-Normal**
   - **Uso**: Representar la distribución de tamaños de nanopartículas que no pueden ser negativas.
   - **Ejemplo**: La distribución de la superficie específica de nanopartículas de metal, que resulta de procesos de síntesis en los que el tamaño de las partículas sigue una relación logarítmica.

3. **Distribución Beta**
   - **Uso**: Modelar proporciones y tasas en sistemas acotados, como la fracción de superficie cubierta en un proceso de recubrimiento.
   - **Ejemplo**: Proporciones de reacción en un sistema catalítico a nanoescala, donde se evalúa la efectividad de un catalizador en función de la superficie activa disponible.

4. **Distribución Gamma**
   - **Uso**: Modelar el tiempo hasta la falla en sistemas con múltiples etapas.
   - **Ejemplo**: Análisis del tiempo hasta la aparición de defectos en nanopartículas durante el proceso de fabricación, lo que permite optimizar el proceso de síntesis.

##### Ciencias de los Materiales

1. **Distribución Weibull**
   - **Uso**: Análisis de fiabilidad y duración de vida de materiales.
   - **Ejemplo**: Estudio de la duración de vida de componentes en pruebas de fatiga, donde se busca entender la probabilidad de fallo de un material bajo cargas cíclicas.

2. **Distribución Gamma**
   - **Uso**: Modelar tiempos de fallo y resistencia en materiales compuestos.
   - **Ejemplo**: Análisis del tiempo entre fracturas en materiales bajo estrés, lo cual es crucial para evaluar la durabilidad de componentes en aplicaciones industriales.

3. **Distribución Exponencial**
   - **Uso**: Modelar el tiempo entre eventos, como fallos en materiales.
   - **Ejemplo**: Evaluación del tiempo hasta la corrosión en materiales metálicos expuestos a ambientes agresivos, ayudando a predecir la vida útil de estructuras metálicas.

4. **Distribución Chi-Cuadrada**
   - **Uso**: Evaluar la varianza de una población y realizar pruebas de bondad de ajuste.
   - **Ejemplo**: Análisis de la variabilidad en pruebas de resistencia de materiales, permitiendo determinar si un nuevo material cumple con estándares de calidad.

5. **Distribución Log-Normal**
   - **Uso**: Modelar fenómenos donde las variables son el resultado de procesos multiplicativos.
   - **Ejemplo**: Distribución de la resistencia a la tracción de fibras compuestas, donde las variaciones en la producción generan una distribución log-normal de las resistencias observadas.

##### Inteligencia Artificial

1. **Distribución Normal**
   - **Uso**: Asumida en muchos algoritmos de aprendizaje automático, especialmente en la estimación de errores.
   - **Ejemplo**: Modelado de errores de predicción en regresiones, donde se espera que los errores sigan una distribución normal.

2. **Distribución Log-Normal**
   - **Uso**: Modelar características que resultan de procesos multiplicativos.
   - **Ejemplo**: Distribución de ingresos o propiedades de datos en análisis de mercado, donde las variables de ingresos no pueden ser negativas.

3. **Distribución Beta**
   - **Uso**: Modelar incertidumbres en probabilidades y proporciones.
   - **Ejemplo**: Asignación de probabilidades en modelos bayesianos, donde se utilizan distribuciones beta para representar la incertidumbre sobre las tasas de éxito.

4. **Distribución de Dirichlet**
   - **Uso**: Modelar distribuciones de probabilidad en múltiples categorías.
   - **Ejemplo**: Priorización de características en algoritmos de clasificación, donde se evalúan las probabilidades de cada clase en un modelo de clasificación.

5. **Distribución t-Student**
   - **Uso**: Realizar inferencias sobre la media de poblaciones pequeñas.
   - **Ejemplo**: Evaluación de errores en muestras pequeñas en aprendizaje automático, donde se requiere estimar la media y su incertidumbre.

##### Diseño de Experimentos y Pruebas de Hipótesis

1. **Distribución Normal**
   - **Uso**: Asumida en muchas pruebas de hipótesis y análisis de varianza.
   - **Ejemplo**: Pruebas t para comparar medias de grupos, donde se evalúa si las diferencias observadas son estadísticamente significativas.

2. **Distribución Chi-Cuadrada**
   - **Uso**: Pruebas de independencia y bondad de ajuste.
   - **Ejemplo**: Evaluar la relación entre variables categóricas en experimentos de diseño factorial.

3. **Distribución F (Fisher-Snedecor)**
   - **Uso**: Comparar varianzas entre grupos.
   - **Ejemplo**: Análisis de varianza (ANOVA) para determinar si hay diferencias significativas entre medias de varios grupos en experimentos.

4. **Distribución Exponencial**
   - **Uso**: Modelar el tiempo hasta el evento en estudios de supervivencia y fiabilidad.
   - **Ejemplo**: Análisis de tiempos hasta fallas en experimentos de durabilidad de materiales.

Cada una de estas distribuciones juega un papel crucial en la modelación, análisis y comprensión de datos en sus respectivos campos, permitiendo realizar inferencias precisas y fundamentadas en experimentos y estudios estadísticos.

### Distribución Uniforme

* **Descripción**: Modelo donde todos los valores en un intervalo \([a, b]\) son igualmente probables.

* **Parámetros**:
  - $ a $ (límite inferior)
  - $ b $ (límite superior)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x) =
\begin{cases}
\frac{1}{b-a} & \text{si } a \leq x \leq b \\
0 & \text{si } x < a \text{ o } x > b
\end{cases}
$$

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) =
\begin{cases}
0 & \text{si } x < a \\
\frac{x-a}{b-a} & \text{si } a \leq x < b \\
1 & \text{si } x \geq b
\end{cases}
$$

* **Valor Esperado**: $ E[X] = \frac{a + b}{2} $

* **Media**: $ \mu_X = \frac{a + b}{2} $

* **Desviación Estándar**: $ \sigma = \frac{b - a}{\sqrt{12}} $

* **Percentiles**:
$$
x_\alpha =
\begin{cases}
a & \text{si } \alpha = 0 \\
b & \text{si } \alpha = 1 \\
a + \alpha(b - a) & \text{si } 0 < \alpha < 1
\end{cases}
$$

**Comandos en R**:
```r
## PDF
dunif(x, min = a, max = b)

## CDF
punif(x, min = a, max = b)

## Simulación
runif(n, min = a, max = b)

#### Ejemplo de Gráfica de la Distribución Uniforme

La distribución uniforme describe un modelo en el que todos los resultados posibles en un intervalo dado tienen la misma probabilidad de ocurrir. Esta distribución se utiliza comúnmente en situaciones donde no hay una tendencia natural hacia un resultado particular.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad $ PDF$ de la distribución uniforme en el intervalo $[a, b]$. A medida que se ajustan los valores de $ a $ y $ b $, la altura de la función de densidad se mantiene constante, reflejando la igualdad de probabilidad de cada punto dentro del intervalo. Esta propiedad de uniformidad hace que la distribución uniforme sea un modelo sencillo pero efectivo para representar fenómenos aleatorios en situaciones controladas.

```python
"""
## Cargar librerías necesarias
library(ggplot2)

## Definir los parámetros de la distribución uniforme
a <- 0  # límite inferior
b <- 1  # límite superior

## Crear un rango de valores para x
x <- seq(a - 0.1, b + 0.1, by = 0.01)

## Calcular la PDF para la distribución uniforme
pdf <- dunif(x, min = a, max = b)

## Crear un data frame
data <- data.frame(x = x, pdf = pdf)

## Graficar la PDF de la distribución uniforme
ggplot(data, aes(x = x, y = pdf)) +
  geom_line(color = "blue", size = 1) +
  labs(title = "Gráfica de la Distribución Uniforme",
       x = "x",
       y = "Densidad de Probabilidad (PDF)") +
  theme_minimal()
"""
```

#### Descripción del Código

* **Cargar librerías**: Se utiliza `ggplot2 `para crear la gráfica.
* **Definir los parámetros**: Se establecen los límites del intervalo $ a $ y $ b$ para la distribución uniforme.
* **Crear un rango de valores para $ x $**: Se define un rango de valores posibles entre $a $ y $ b $ para representar la distribución.
* **Calcular la PDF**: Se utiliza `dunif()` para calcular la función de densidad de probabilidad en el intervalo definido.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $ x $ y sus correspondientes probabilidades.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $PDF $ de la distribución uniforme en el intervalo $[a, b]$.

**EJERCICIO 8**

La Distribución Uniforme, tanto en su versión **continua** como **discreta**, es la más sencilla de entender, ya que modela situaciones donde **todos los resultados posibles dentro de un rango específico tienen la misma probabilidad de ocurrir**.

Aquí tienes ejemplos y usos recomendados de cada tipo:

---

## I. Distribución Uniforme Discreta

Se aplica cuando una variable aleatoria solo puede tomar un **número finito de valores** y la probabilidad de cada uno de ellos es idéntica.

### Fórmula (Función de Masa de Probabilidad - PMF)

$$P(X = k) = \frac{1}{n}$$

Donde $n$ es el número total de resultados posibles.

### Ejemplos Típicos

| Escenario | Parámetros | Usos Recomendados |
| :--- | :--- | :--- |
| **Lanzamiento de un dado justo** | Resultados: $\{1, 2, 3, 4, 5, 6\}$ $n=6$ | **Modelar juegos de azar o procesos de selección totalmente equitativos** donde cada opción tiene el mismo peso. |
| **Seleccionar una carta** | Resultados: 52 cartas $n=52$ | Análisis de probabilidad en **juegos de cartas** (antes de que se revelen cartas). |
| **Números de Lotería Simples** | Resultados: $\{1, 2, \dots, 49\}$ $n=49$ | Modelar la probabilidad de que salga un número específico antes del sorteo. |
| **Selección aleatoria de un producto** | Resultados: $\{Producto \ 1, \dots, Producto \ n\}$ | Asignación aleatoria de participantes en un **estudio** o selección aleatoria de elementos en un **control de calidad**. |

### Usos Recomendados

1.  **Modelos de Sorteos y Juegos:** Es el modelo base para cualquier proceso de selección o experimento donde se garantiza la total aleatoriedad e igualdad de oportunidades.
2.  **Criptografía y Seguridad:** Se utiliza para generar secuencias de bits o claves criptográficas, donde es vital que cada bit tenga la misma probabilidad de ser 0 o 1 para evitar patrones predecibles.
3.  **Algoritmos de Hashing:** En informática, la distribución uniforme es el resultado ideal que se busca al diseñar una buena función hash, asegurando que las claves se dispersen de manera equitativa.

---

## II. Distribución Uniforme Continua

Se aplica cuando una variable aleatoria puede tomar **cualquier valor dentro de un intervalo fijo** (entre $a$ y $b$), y la probabilidad de que caiga en cualquier subintervalo de igual longitud es la misma.

### Fórmula (Función de Densidad de Probabilidad - PDF)

$$f(x) = \begin{cases} \frac{1}{b-a} & \text{si } a \le x \le b \\ 0 & \text{en otro caso} \end{cases}$$

Donde $a$ es el límite inferior y $b$ es el límite superior.

### Ejemplos Típicos

| Escenario | Parámetros | Usos Recomendados |
| :--- | :--- | :--- |
| **Tiempo de espera del autobús** | El autobús llega entre 8:00 y 8:10 ($a=0, b=10$ minutos) | **Modelar tiempos de espera** cuando se sabe un intervalo, pero no hay un horario fijo o factores que favorezcan un momento sobre otro. |
| **Error de redondeo/cuantificación** | Error entre $-0.5$ y $+0.5$ (al redondear al entero más cercano) | **Análisis de errores en mediciones digitales** o analógicas. Se asume que el error introducido es igualmente probable en todo el rango de error. |
| **Generación de Números Aleatorios** | Números generados entre $[0, 1]$ ($a=0, b=1$) | **Simulaciones (Método Monte Carlo)**. Es la distribución fundamental para generar números aleatorios que luego se transforman para obtener otras distribuciones (Normal, Exponencial, etc.). |
| **Proceso de fabricación** | El grosor de una pieza está entre $10.0$ y $10.2$ mm | Modelar **parámetros de calidad o duración** donde la única información conocida son los límites máximo y mínimo, sin evidencia de que los valores centrales sean más probables. |

#### Codigo en phyton

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # Opcional: para mejorar la estética de la gráfica

## ----------------------------------------------------
## 1. Cargar librerías necesarias (importaciones)
## Ya hecho arriba
## ----------------------------------------------------

## 2. Definir los parámetros de la distribución uniforme
a = 0  # Límite inferior
b = 1  # Límite superior

## 3. Crear un rango de valores para x
## Similar a seq(a - 0.1, b + 0.1, by = 0.01) en R
x = np.arange(a - 0.1, b + 0.1, 0.01)

## 4. Calcular la PDF para la distribución uniforme
## En la distribución uniforme, la PDF es 1/(b-a) dentro del rango [a, b] y 0 fuera.
## Definimos una función equivalente a dunif(x, min=a, max=b)
def uniform_pdf(x_val, a, b):
## La altura de la PDF dentro del rango
    height = 1 / (b - a)

## Crea un array de ceros para la misma forma que x_val
    pdf_val = np.zeros_like(x_val, dtype=float)

## Identifica los índices donde x_val está en el rango [a, b]
    in_range = (x_val >= a) & (x_val <= b)

## Asigna la altura a esos índices
    pdf_val[in_range] = height

    return pdf_val

pdf = uniform_pdf(x, a, b)

## 5. Crear un data frame (Aunque no es estrictamente necesario para la gráfica,
## la estructura de datos es similar a la creada por numpy)
## Los arrays 'x' y 'pdf' contienen los datos.

## 6. Graficar la PDF de la distribución uniforme (usando Matplotlib/Seaborn)
## Configuración de Seaborn para el estilo (Opcional)
sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 6))

## Trazar la línea (equivalente a geom_line en ggplot2)
plt.plot(x, pdf, color="blue", linewidth=2) # size=1 en R es linewidth=2 en Matplotlib para mejor visibilidad

## Añadir etiquetas y título (equivalente a labs)
plt.title("Gráfica de la Distribución Uniforme", fontsize=16)
plt.xlabel("x", fontsize=12)
plt.ylabel("Densidad de Probabilidad (PDF)", fontsize=12)

## Usar theme_minimal (ajustes de Matplotlib)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

## Mostrar la gráfica
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

## ----------------------------------------------------
## Nota: Si se quisiera usar la librería 'scipy.stats' para mayor fidelidad a R,
## el cálculo de la PDF sería:
## from scipy.stats import uniform
## pdf_scipy = uniform.pdf(x, loc=a, scale=b-a)
## (loc es el mínimo, scale es la longitud b-a)
## ----------------------------------------------------
```

## Descripción del Código Python para la Gráfica de la Distribución Uniforme

El código presentado en **Python** tiene el propósito de calcular y visualizar la **Función de Densidad de Probabilidad (PDF)** de una **Distribución Uniforme** en el intervalo $[0, 1]$. Utiliza la librería **NumPy** para operaciones numéricas y **Matplotlib/Seaborn** para la generación del gráfico.

---

### 1. Inicialización y Parámetros

| Código | Descripción |
| :--- | :--- |
| `import numpy as np` | **Librerías Numéricas**: Importa **NumPy** para manejar arrays y cálculos matemáticos. |
| `import matplotlib.pyplot as plt` | **Librerías de Gráficos**: Importa **Matplotlib**, el estándar de facto para la creación de gráficos. |
| `import seaborn as sns` | **Estética (Opcional)**: Importa **Seaborn** para aplicar un estilo visual mejorado a los gráficos de Matplotlib. |
| `a = 0` | **Límite Inferior ($a$)**: Define el valor inicial del intervalo para la distribución. |
| `b = 1` | **Límite Superior ($b$)**: Define el valor final del intervalo para la distribución. |
| `x = np.arange(a - 0.1, b + 0.1, 0.01)` | **Creación del Rango $x$**: Utiliza `np.arange` para generar una secuencia de puntos equidistantes desde $-0.1$ hasta $1.1$ con un paso de $0.01$. Esto asegura que la gráfica muestre claramente que la probabilidad es cero fuera del intervalo $[a, b]$. |

---

### 2. Cálculo de la Función de Densidad (PDF)

| Código | Descripción |
| :--- | :--- |
| `def uniform_pdf(x_val, a, b): ...` | **Definición de la Función PDF**: Se crea una función personalizada para replicar el comportamiento de la función `dunif()` de R (o `uniform.pdf` de `scipy`). |
| `height = 1 / (b - a)` | **Altura de la PDF**: Calcula la altura constante de la función, que es $1/(1-0) = 1$. |
| `in_range = (x_val >= a) & (x_val <= b)` | **Identificación del Rango**: Crea una máscara booleana (`in_range`) que es `True` solo para los valores de $x$ que se encuentran dentro del intervalo $[a, b]$. |
| `pdf_val[in_range] = height` | **Asignación de Valores**: Asigna la altura calculada (`1.0`) a todos los valores de $x$ que están dentro del rango, dejando los valores fuera del rango en $0$ (ya que `pdf_val` se inicializó con ceros). |
| `pdf = uniform_pdf(x, a, b)` | **Cálculo Final**: Ejecuta la función con los datos $x$ y los parámetros $a, b$ para obtener el array final de densidades. |

---

### 3. Visualización de la Gráfica

| Código | Descripción |
| :--- | :--- |
| `sns.set_theme(style="whitegrid")` | **Estilo Seaborn**: Aplica un tema visual con cuadrícula blanca que mejora la estética por defecto de Matplotlib. |
| `plt.figure(figsize=(8, 6))` | **Creación de Figura**: Inicializa la figura de Matplotlib, definiendo el tamaño del lienzo para la gráfica. |
| `plt.plot(x, pdf, color="blue", linewidth=2)` | **Trazado de la Línea**: Dibuja la línea que representa la PDF, usando los arrays $x$ y $pdf$. Esto es equivalente a `geom_line` en `ggplot2`. |
| `plt.title(...), plt.xlabel(...), plt.ylabel(...)` | **Etiquetas y Títulos**: Define el título principal y las etiquetas para los ejes $x$ y $y$. |
| `plt.gca().spines[...]` | **Ajustes Minimalistas**: Deshabilita los bordes superiores y derechos de la gráfica, contribuyendo a un estilo más limpio, similar a `theme_minimal()` de `ggplot2`. |
| `plt.grid(True, linestyle='--', alpha=0.6)` | **Cuadrícula**: Muestra una cuadrícula con líneas discontinuas y transparencia. |
| `plt.show()` | **Renderizado**: Muestra el gráfico final al usuario. |

El código genera un gráfico que visualiza la distribución de probabilidad de forma rectangular, con una altura de **1** constante entre $x=0$ y $x=1$, y **cero** fuera de ese rango.

### Distribución Exponencial

* **Descripción**: Modelo de tiempo hasta el próximo evento en un proceso de Poisson.

* **Parámetro**:
- $ \lambda$ (tasa de ocurrencia de eventos)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x) =
\begin{cases}
\lambda e^{-\lambda x} & \text{si } x \geq 0 \\
0 & \text{si } x < 0
\end{cases}
$$

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) =
\begin{cases}
1 - e^{-\lambda x} & \text{si } x \geq 0 \\
0 & \text{si } x < 0
\end{cases}
$$

* **Valor Esperado**: $ E[X] = \frac{1}{\lambda}$

* **Media**: $ \mu_X = \frac{1}{\lambda}$

* **Desviación Estándar**: $\sigma = \frac{1}{\lambda}$

* **Percentiles**: $x_\alpha = -\frac{\log(\alpha)}{\lambda}$

**Comandos en R**:
```r
## PDF
dexp(x, rate = lambda)

## CDF
pexp(x, rate = lambda)

## Simulación
rexp(n, rate = lambda)

#### Ejemplo de Gráfica de la Distribución Exponencial

La distribución exponencial describe el tiempo entre eventos en un proceso de Poisson. Es útil para modelar situaciones donde se necesita calcular el tiempo hasta que ocurra un evento, dado un promedio de eventos conocido.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad $PDF$ de la distribución exponencial para varios valores de $ \lambda$, que es la tasa de ocurrencia de eventos por unidad de tiempo. A medida que $ \lambda $aumenta, la distribución se vuelve más concentrada hacia la izquierda, indicando que los eventos ocurren más rápidamente.

```python
"""
## Instalar y cargar la librería necesaria
#install.packages('ggplot2')  # Descomentar si no está instalada
library(ggplot2)

## Aquí tienes un ejemplo de varios gráficos de la distribución exponencial
## con diferentes valores de lambda. El código incluye la configuración
## necesaria para generar los gráficos:

## Definir un rango de valores para x
x <- seq(0, 5, by = 0.01)

## Crear un data frame vacío para almacenar los resultados
data_list <- list()

## Valores de lambda a usar
lambda_values <- c(0.5, 1, 1.5)

## Calcular la PDF para cada valor de lambda y almacenar en el data frame
for (lambda in lambda_values) {
  pdf <- dexp(x, rate = lambda)
  data_list[[as.character(lambda)]] <- data.frame(x = x, pdf = pdf, lambda = lambda)
}

## Combinar todos los data frames en uno solo
data <- do.call(rbind, data_list)

## Graficar la distribución exponencial para diferentes valores de lambda
ggplot(data, aes(x = x, y = pdf, color = as.factor(lambda))) +
  geom_line() +
  labs(title = "Distribución Exponencial para Diferentes Valores de Lambda",
       x = "x",
       y = "Densidad de Probabilidad",
       color = "Lambda") +
  theme_minimal() +
  scale_color_manual(values = c("blue", "red", "green"))
"""
```

#### Descripción del Código

* **Cargar librerías**: Se utiliza `ggplot2` para crear las gráficas.
* **Definir un rango de valores para $ x $**: Se establece un rango de valores de $0 $ a $ 5 $.
* **Crear un data frame vacío**: Se inicializa una lista para almacenar los resultados de la $PDF$.
* **Valores de $ \lambda $**: Se definen diferentes valores de $ \lambda $ (en este caso, $ 0.5 $, $ 1 $ y $ 1.5 $).
* **Calcular la PDF**: Se utiliza `dexp()` para calcular la función de densidad de probabilidad para cada valor de $ \lambda $ y se almacena en el data frame.
* **Combinar data frames**: Se combinan todos los data frames en uno solo para facilitar la graficación.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $PDF$ de la distribución exponencial para diferentes valores de $\lambda$.

#### Usos de la Distribución Exponencial

La distribución exponencial se utiliza en la teoría de la fiabilidad como el modelo más simple para la vida útil de equipos. Además, como se discutirá a continuación, el tiempo hasta el siguiente evento de un proceso de Poisson sigue la distribución exponencial. Por lo tanto, la distribución exponencial modela una amplia gama de tiempos de espera, como el tiempo hasta que llegue el próximo cliente a una estación de servicio, el tiempo hasta el próximo fallo de un banco o firma de inversión, el tiempo hasta el siguiente brote de hostilidades, el tiempo hasta el próximo terremoto, o el tiempo hasta que falle el siguiente componente de un sistema multi-componente.

#### Propiedad de Memoria

Una variable aleatoria no negativa $X$ tiene la propiedad de memoria, también llamada propiedad de no envejecimiento, si para todos $ s, t > 0 $:

$$
P(X > s + t | X > s) = P(X > t)
$$

**Se puede demostrar que la variable aleatoria exponencial tiene esta propiedad, y de hecho, es la única distribución con esta propiedad.**

#### Conexión Poisson-Exponencial

Para un proceso de Poisson, sea $ T_1 $ el tiempo en que ocurre el primer evento, y para $ i = 2, 3, \ldots $, $ T_i $ denota el tiempo transcurrido entre la ocurrencia del $(i-1)$-ésimo y el $i$-ésimo evento. Los tiempos $T_1, T_2, \ldots $ se llaman tiempos entre llegadas.

**Proposición 3.5-1**: Si $ X(s)$, $s \geq 0$, es un proceso de Poisson con tasa $ \alpha$, los tiempos entre llegadas tienen la distribución exponencial con PDF:

$$
f(t) = \alpha e^{-\alpha t}, \quad t > 0
$$

**Ejemplo 3.5-2**: Los logins de usuario a la red informática de una universidad se pueden modelar como un proceso de Poisson con una tasa de $10$ por minuto. Si el administrador del sistema comienza a rastrear el número de logins a las 10:00 a.m., encuentra la probabilidad de que el primer login registrado ocurra entre $10$ y $20$ segundos después.

**Solución**: Con el tiempo cero establecido en $10:00 a.m.$, sea $ T_1 $ el tiempo, en minutos, del primer registro. Dado que $ T_1 \sim \text{Exp}(10) $, la fórmula de la CDF nos da:

$$
P\left(\frac{10}{60} < T < \frac{20}{60}\right) = e^{-10 \times \frac{10}{60}} - e^{-10 \times \frac{20}{60}} = 0.1532.
$$

**EJERCICIO 9**

La Distribución Normal (o Distribución Gaussiana) es la distribución de probabilidad más importante debido al **Teorema del Límite Central**, que establece que la suma o promedio de un gran número de variables aleatorias (independientes e idénticamente distribuidas) tiende a seguir una distribución normal. Esto la hace ideal para modelar fenómenos que resultan de la acumulación de muchos pequeños factores aleatorios.

Aquí tienes ejemplos y usos recomendados en Nanotecnología, Inteligencia Artificial y Diseño de Experimentos (DOE).

***

## ⚛️ Nanotecnología

En nanotecnología, la Distribución Normal se utiliza para modelar la variabilidad inherente en las estructuras y procesos a escala nanométrica.

### Ejemplos y Usos Recomendados

1.  **Distribución de Tamaño de Nanopartículas:**
    * **Ejemplo:** Al sintetizar **puntos cuánticos** o nanopartículas de oro, el tamaño promedio ($\mu$) y la desviación estándar ($\sigma$) del lote siguen una distribución normal.
    * **Uso Recomendado:** Se emplea para **control de calidad** y **caracterización**. Una $\sigma$ pequeña indica una distribución de tamaño estrecha (monodispersa), lo cual es crucial para aplicaciones que dependen de propiedades ópticas o electrónicas específicas (p. ej., nanomedicina o *displays* QLED).

2.  **Variabilidad en Nanodispositivos:**
    * **Ejemplo:** Las variaciones en la longitud de canal o el grosor de la capa aislante de un **nanotransistor** (FET) debido a imprecisiones en la litografía.
    * **Uso Recomendado:** Modelar el rendimiento de los dispositivos. La distribución normal permite predecir el **rendimiento** (o *yield*) de fabricación, estableciendo tolerancias aceptables para el diseño del dispositivo.

3.  **Mediciones Instrumentales:**
    * **Ejemplo:** Las mediciones repetidas del espesor de una **película delgada** utilizando un Microscopio de Fuerza Atómica (AFM).
    * **Uso Recomendado:** Se asume que el **ruido experimental** y el error de medición siguen una distribución normal. Esto permite calcular intervalos de confianza y determinar si las diferencias entre dos muestras son estadísticamente significativas.

***

## 🤖 Inteligencia Artificial (IA) y Aprendizaje Automático

La Distribución Normal es fundamental tanto en la teoría como en la aplicación de numerosos algoritmos de IA, especialmente en el aprendizaje automático (*Machine Learning*).

### Ejemplos y Usos Recomendados

1.  **Inicialización de Pesos en Redes Neuronales:**
    * **Ejemplo:** Al construir una red neuronal profunda, los **pesos sinápticos** se inicializan a menudo muestreándolos de una distribución normal con media cero y una desviación estándar pequeña (p. ej., Inicialización de Xavier o He).
    * **Uso Recomendado:** Asegurar que las neuronas en las primeras capas reciban entradas con una varianza adecuada, evitando que las señales se **saturen** o **desaparezcan** (problemas de *vanishing/exploding gradients*) durante el entrenamiento.

2.  **Algoritmos de Clasificación Gaussiana:**
    * **Ejemplo:** El clasificador **Naive Bayes**, que asume que las características numéricas, condicionadas a la clase, siguen una distribución normal.
    * **Uso Recomendado:** Se utiliza para la **clasificación de datos continuos**. Aunque la suposición de independencia ("naive") es fuerte, es simple y sorprendentemente efectivo.

3.  **Modelos de Densidad y Generación de Datos:**
    * **Ejemplo:** **Modelos de Mezclas Gaussianas (GMM)**, utilizados para agrupar (clustering) datos o modelar la distribución de probabilidad de conjuntos de datos complejos.
    * **Uso Recomendado:** Estimar la forma subyacente de los datos. También es la base para algunos **Modelos Generativos** (como los VAEs), donde el espacio latente de la información (el *código* de la imagen o dato) se modela con una distribución normal multivariada.

***

## 🧪 Diseño de Experimentos (DOE)

En DOE, la distribución normal no solo se usa para modelar los datos, sino que es una **suposición fundamental** para validar los resultados de las pruebas estadísticas más comunes.

### Ejemplos y Usos Recomendados

1.  **Análisis de Varianza (ANOVA):**
    * **Ejemplo:** Un experimento para determinar cómo dos factores (temperatura y presión) afectan la resistencia de un material.
    * **Uso Recomendado:** La validez de las pruebas $t$ y $F$ en el análisis ANOVA **depende de la suposición de que los errores (residuos)** del modelo siguen una distribución normal. Se realizan pruebas de normalidad (como Shapiro-Wilk) para confirmar esta suposición.

2.  **Cálculo de Intervalos de Confianza y Pruebas de Hipótesis:**
    * **Ejemplo:** Determinar si el rendimiento promedio de un nuevo proceso de síntesis ($\mu_{\text{nuevo}}$) es significativamente mayor que el proceso estándar ($\mu_{\text{estándar}}$).
    * **Uso Recomendado:** El **Teorema del Límite Central** permite usar la distribución normal para construir intervalos de confianza y realizar pruebas $Z$ o $t$ (basadas en la normal) sobre las medias muestrales, incluso si la población original no es perfectamente normal (si el tamaño de la muestra es grande).

3.  **Control Estadístico de Procesos (SPC):**
    * **Ejemplo:** Monitorear el peso promedio de tabletas en una línea farmacéutica o el voltaje de salida de una fuente de alimentación.
    * **Uso Recomendado:** Se utilizan **Gráficos de Control** basados en la normal (como los gráficos $\bar{X}$ y R) para establecer límites de control (generalmente $\mu \pm 3\sigma$). Si una muestra cae fuera de este rango, el proceso se considera "fuera de control" y requiere investigación.

#### Codigo en phyton

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import expon # Importamos la función de distribución exponencial

## ----------------------------------------------------
## 1. Definir un rango de valores para x
## Similar a seq(0, 5, by = 0.01) en R
x = np.arange(0, 5.01, 0.01) # Usamos 5.01 para asegurar que incluya el 5

## 2. Valores de lambda a usar (rate en scipy.stats)
lambda_values = [0.5, 1.0, 1.5]

## 3. Crear una lista para almacenar los DataFrames de cada lambda
data_list = []

## 4. Calcular la PDF para cada valor de lambda y almacenar
for lambda_val in lambda_values:
## La función .pdf() de scipy.stats es el equivalente a dexp() en R
## 'rate' es el parámetro lambda (tasa)
    pdf = expon.pdf(x, scale=1/lambda_val)

## Crear un DataFrame para este lambda
    df_temp = pd.DataFrame({
        'x': x,
        'pdf': pdf,
        'lambda': str(lambda_val) # Convertir a string para usar como categoría en la gráfica
    })
    data_list.append(df_temp)

## 5. Combinar todos los DataFrames en uno solo (equivalente a do.call(rbind, ...))
data = pd.concat(data_list, ignore_index=True)

## 6. Configurar Seaborn para una estética similar a ggplot2 y graficar
sns.set_theme(style="whitegrid")

## Definir colores manualmente
colores = {"0.5": "blue", "1.0": "red", "1.5": "green"}

plt.figure(figsize=(10, 6))

## Usar seaborn.lineplot para graficar (similar a ggplot + geom_line)
sns.lineplot(
    data=data,
    x='x',
    y='pdf',
    hue='lambda', # Usar 'lambda' para diferenciar las líneas por color
    palette=colores,
    linewidth=2
)

## Añadir etiquetas y título (equivalente a labs)
plt.title("Distribución Exponencial para Diferentes Valores de Lambda", fontsize=16)
plt.xlabel("x", fontsize=12)
plt.ylabel("Densidad de Probabilidad", fontsize=12)

## Configurar la leyenda (equivalente a color = "Lambda" en labs)
plt.legend(title='Lambda')

## Mostrar la gráfica
plt.show()
```

## Descripción del Código Python para la Gráfica de la Distribución Exponencial

El código en **Python** calcula y visualiza la **Función de Densidad de Probabilidad (PDF)** de la **Distribución Exponencial** para **múltiples valores del parámetro de tasa ($\lambda$)**. El objetivo es ilustrar cómo $\lambda$ afecta la forma de la distribución, utilizando **NumPy** para los cálculos, **Pandas** para la manipulación de datos y **Matplotlib/Seaborn** para la representación gráfica.

***

### 1. Inicialización y Preparación de Datos

| Código | Descripción |
| :--- | :--- |
| `import numpy as np`, `import pandas as pd`, etc. | **Carga de Librerías**: Importa las herramientas esenciales: **NumPy** (cálculo numérico), **Pandas** (estructuras de datos tipo *DataFrame*), **Matplotlib** y **Seaborn** (visualización), y **`expon`** de `scipy.stats` (funciones estadísticas para la distribución exponencial). |
| `x = np.arange(0, 5.01, 0.01)` | **Definición del Eje $x$**: Crea un rango de valores para la variable $x$ desde $0$ hasta $5.01$ con incrementos de $0.01$. La distribución exponencial solo está definida para $x \ge 0$. |
| `lambda_values = [0.5, 1.0, 1.5]` | **Parámetros $\lambda$**: Define los tres valores de la tasa ($\lambda$) que se usarán para generar las distintas curvas de densidad. |

***

### 2. Cálculo de la Función de Densidad (PDF)

| Código | Descripción |
| :--- | :--- |
| `for lambda_val in lambda_values: ...` | **Bucle de Cálculo**: Itera a través de cada valor de $\lambda$ para calcular la PDF correspondiente. |
| `pdf = expon.pdf(x, scale=1/lambda_val)` | **Cálculo de la PDF**: Utiliza la función **`expon.pdf()`** de `scipy.stats`. **Importante:** `scipy.stats` usa el parámetro **`scale`** (escala), que es el inverso de la tasa ($\lambda$). Por lo tanto, se establece $scale = 1/\lambda$. |
| `df_temp = pd.DataFrame({...})` | **Estructura de Datos Temporal**: Crea un *DataFrame* para cada valor de $\lambda$, que contiene las columnas $x$, $pdf$, y $\lambda$ (convertido a *string* para ser usado como variable categórica en la gráfica). |
| `data = pd.concat(data_list, ignore_index=True)` | **Combinación de Datos**: Concatena todos los *DataFrames* temporales en un único *DataFrame* llamado `data`. Este *DataFrame* unificado es el formato ideal para generar gráficas con múltiples grupos en Seaborn (similar a la estructura de datos que usaría `ggplot2`). |

***

### 3. Visualización y Estilizado

| Código | Descripción |
| :--- | :--- |
| `sns.set_theme(style="whitegrid")` | **Estilo de Gráfico**: Aplica un tema `whitegrid` de Seaborn para mejorar la estética visual. |
| `sns.lineplot(...)` | **Trazado de Múltiples Líneas**: Utiliza la función **`lineplot`** de Seaborn para dibujar las curvas. |
| | - `x='x', y='pdf'` : Define los ejes. |
| | - `hue='lambda'` : **Clave de Mapeo**: Indica que la variable $\lambda$ debe usarse para diferenciar las líneas por **color** y generar automáticamente la **leyenda**. |
| | - `palette=colores` : Asigna colores específicos a cada valor de $\lambda$. |
| `plt.title(...), plt.xlabel(...), plt.ylabel(...)` | **Etiquetas y Títulos**: Establece el título principal y las etiquetas de los ejes. |
| `plt.legend(title='Lambda')` | **Configuración de Leyenda**: Asigna el título "Lambda" a la leyenda generada por el argumento `hue`. |

El resultado es un gráfico que muestra tres curvas de densidad exponencial, todas comenzando en $\lambda$ en $x=0$ y decayendo a cero a medida que $x$ aumenta. Se observa que **a mayor valor de $\lambda$, mayor es la densidad inicial y más rápido es el decaimiento** de la probabilidad.

### Distribución Normal

* **Descripción**: La distribución normal es una distribución continua caracterizada por su forma simétrica y campaniforme. Se denota como $X \sim N(\mu, \sigma^2)$, donde $\mu$ es la media y $\sigma$ es la desviación estándar.

* **Parámetros**:
- $\mu $ (media)
- $\sigma $ (desviación estándar)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
$$

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) = \int_{-\infty}^{x} f(t) dt
$$

* **Valor Esperado**: $E[X] = \mu$

* **Media**:$\mu_X = \mu$

**Desviación Estándar**: $\sigma_X = \sigma$

* **Percentiles**: $x_\alpha = \mu + \sigma z_\alpha$

* **Propiedad del 68-95-99.7%**:
 - Aproximadamente el $68\%$ de los valores caen dentro de $ \mu \pm 1\sigma $.
 - Aproximadamente el $95\%$ de los valores caen dentro de $ \mu \pm 2\sigma $.
 - Aproximadamente el $99.7\%$ de los valores caen dentro de $\mu \pm 3\sigma $.

* **Comandos en R**:
```r
## PDF
 dnorm(x, mean = mu, sd = sigma)

## CDF
 pnorm(x, mean = mu, sd = sigma)

## Percentiles
 qnorm(s, mean = mu, sd = sigma)

## Simulación
 rnorm(n, mean = mu, sd = sigma)

#### Ejemplo de Gráfica de la Distribución Normal

La distribución normal es una de las distribuciones de probabilidad más importantes en estadística, describiendo la variabilidad de muchos fenómenos naturales. Se caracteriza por su forma de campana y es definida por dos parámetros: la media $\mu $ y la desviación estándar $ \sigma $.

En esta gráfica, se presentan diferentes funciones de densidad de probabilidad $ PDF$ de la distribución normal para varios valores de $ \mu $ y $ \sigma $. A medida que la media $ \mu $ se desplaza, el centro de la campana se mueve, mientras que un aumento en la desviación estándar $ \sigma $ ensancha la distribución, indicando una mayor dispersión de los datos. Esto permite modelar una amplia gama de fenómenos, desde la altura de las personas hasta los errores de medición.

```python
"""
## Cargar librerías necesarias
library(ggplot2)

## Definir un rango de valores para x
x <- seq(-10, 10, by = 0.1)

## Definir diferentes valores de media (mu) y desviación estándar (sigma)
params <- data.frame(mu = c(-2, 0, 2), sigma = c(1, 1, 1.5))

## Crear un data frame vacío para almacenar los resultados de la PDF
pdf_data <- data.frame()

## Calcular la PDF para cada combinación de mu y sigma
for (i in 1:nrow(params)) {
  mu <- params$mu[i]
  sigma <- params$sigma[i]

## Calcular la función de densidad de probabilidad
  pdf_values <- dnorm(x, mean = mu, sd = sigma)

## Almacenar los resultados en un data frame
  pdf_data <- rbind(pdf_data, data.frame(x = x, y = pdf_values, mu = mu, sigma = sigma))
}

## Graficar la distribución normal
ggplot(pdf_data, aes(x = x, y = y, color = as.factor(mu), linetype = as.factor(sigma))) +
  geom_line(size = 1) +
  labs(title = "Funciones de Densidad de Probabilidad de la Distribución Normal",
       x = "Valor",
       y = "Densidad",
       color = "Media (mu)",
       linetype = "Desviación Estándar (sigma)") +
  theme_minimal() +
  scale_color_manual(values = c("blue", "red", "green")) +
  theme(legend.position = "top")
  """
```

#### Descripción del Código

* **Cargar librerías**: Se utiliza `ggplot2` para crear las gráficas.
* **Definir un rango de valores para $ x $**: Se establece un rango de valores de $-10$ a $10$.
* **Definir los parámetros**: Se establecen diferentes valores de media $ \mu $ y desviación estándar $ \sigma $ para la distribución normal.
* **Crear un data frame vacío**: Se inicializa un data frame para almacenar los resultados de la $PDF$.
* **Calcular la PDF**: Se utiliza `dnorm()` para calcular la función de densidad de probabilidad para cada combinación de $ \mu $ y $ \sigma $.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $ PDF $ de la distribución normal para diferentes valores de $ \mu $ y $ \sigma $.

#### Otras Características de la DISTRIBUCIÓN NORMAL

Una variable aleatoria se dice que tiene la distribución normal estándar si su PDF y CDF, que se denotan (universalmente) por $\phi$ y $\Phi$, respectivamente, son

$$
\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2} \quad \text{y} \quad \Phi(z) = \int_{-\infty}^{z} \phi(x) \, dx
$$

para $-\infty < z < \infty$. Una variable aleatoria normal estándar se denota por $Z$.

Una variable aleatoria $X$ se dice que tiene la distribución normal, con parámetros $\mu$ y $\sigma$, denotada por $X \sim N(\mu, \sigma^2)$, si su PDF y CDF son

$$
f(x) = \frac{1}{\sigma} \phi\left(\frac{x - \mu}{\sigma}\right) \quad \text{y} \quad F(x) = \Phi\left(\frac{x - \mu}{\sigma}\right)
$$

para $-\infty < x < \infty$. Así,

$$
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}},
$$

que es simétrico respecto a $\mu$. Por lo tanto, $\mu$ es tanto la media, la mediana como la moda de $X$. El parámetro $\sigma$ es la desviación estándar de $X$. Para $\mu = 0$ y $\sigma = 1$, $X$ es normal estándar y se denota por $Z$.

El PDF normal es difícil de integrar y no se utilizará para calcular probabilidades mediante integración. Además, la CDF no tiene una expresión en forma cerrada.

En los comandos de R, tanto $x$ como $s$ pueden ser vectores. Por ejemplo, si $X \sim N(5, 16)$,
* `dnorm(6, 5, 4)` devuelve $0.09666703$ para el valor de la PDF de $X$ en $x = 6$.
* `pnorm(c(3, 6), 5, 4)` devuelve los valores de $P(X \leq 3)$ y $P(X \leq 6)$.
* `qnorm(c(0.9, 0.99), 5, 4)` devuelve $10.12621$ y $14.30539$ para el percentil $90$ y $99$ de $X$, respectivamente.

La PDF normal estándar $\Phi(z)$ se tabula en la **Tabla A.3** para valores de $z$ de $0$ a $3.09$ en incrementos de $0.01$. En el resto de esta sección aprenderemos a usar la **Tabla A.3** no solo para encontrar probabilidades y percentiles de la variable aleatoria normal estándar, sino para cualquier otra variable normal. La capacidad de usar solo una tabla, la de la normal estándar, para encontrar probabilidades y percentiles de cualquier variable normal se debe a una propiedad interesante de la distribución normal, que se presenta en la siguiente proposición.

**Proposición 3.5-2** Si $X \sim N(\mu, \sigma^2)$ y $a, b$ son números reales, entonces

$$
a + bX \sim N(a + b\mu, b^2\sigma^2). \tag{3.5.4}
$$

El nuevo elemento de esta proposición es que una transformación lineal de una variable aleatoria normal también es una variable aleatoria normal. Que el valor medio y la varianza de la variable transformada, $Y = a + bX$, son $a + b\mu$ y $b^2\sigma^2$, respectivamente, se sigue de las Proposiciones 3.3-1 y 3.3-2, por lo que no hay nada nuevo en estas fórmulas.

**Encontrando Probabilidades**

 Primero ilustramos el uso de la Tabla A.3 para encontrar probabilidades asociadas con la variable aleatoria normal estándar.

**Ejemplo 3.5-3** Sea $Z \sim N(0, 1)$. Encuentra

 (a) $P(-1 < Z < 1)$,

 (b) $P(-2 < Z < 2)$ y

 (c) $P(-3 < Z < 3)$.

**Solución** En la Tabla A.3, los valores de $z$ están listados con dos decimales, con el segundo decimal identificado en la fila superior de la tabla. Así, el valor $z$ igual a $1$ se identifica por $1.0$ en la columna izquierda de la tabla y $0.00$ en la fila superior de la tabla. La probabilidad $\Phi(1) = P(Z \leq 1)$ es el número que corresponde a la fila y la columna identificadas por $1.0$ y $0.00$, que es $0.8413$. Dado que los valores negativos no están listados en la Tabla A.3, $\Phi(-1) = P(Z \leq -1)$ se encuentra aprovechando el hecho de que la distribución normal estándar es simétrica respecto a cero. Esto significa que el área bajo la PDF de $N(0, 1)$ a la izquierda de $-1$ es igual al área bajo ella a la derecha de $1$. Por lo tanto,

$$
\Phi(-1) = 1 - \Phi(1),
$$

y la misma relación se mantiene con cualquier número positivo que sustituya a 1. Así, la respuesta a la parte (a) es

$$
P(-1 < Z < 1) = \Phi(1) - \Phi(-1) = 0.8413 - (1 - 0.8413) = 0.8413 - 0.1587 = 0.6826.
$$

Trabajando de manera similar, encontramos las siguientes respuestas para las partes (b) y (c):
$$
P(-2 < Z < 2) = \Phi(2) - \Phi(-2) = 0.9772 - 0.0228 = 0.9544,
$$
y
$$
P(-3 < Z < 3) = \Phi(3) - \Phi(-3) = 0.9987 - 0.0013 = 0.9974.
$$

Por lo tanto, aproximadamente el $68\%$ de los valores de una variable aleatoria normal estándar caen dentro de una desviación estándar de su media, aproximadamente el $95\%$ caen dentro de dos desviaciones estándar de su media, y aproximadamente el $99.7\%$ de sus valores caen dentro de tres desviaciones estándar de su media. Esto se conoce como la regla del $68-95-99.7\%.$

El uso de la Tabla A.3 para encontrar probabilidades asociadas con cualquier variable normal es posible a través del siguiente corolario de la Proposición 3.5-2.

**Corolario 3.5-1** Si $X \sim N(\mu, \sigma^2)$, entonces
* $X - \mu \sim N(0, \sigma^2)$, y
* $P(a \leq X \leq b) = \Phi\left(\frac{b - \mu}{\sigma}\right) - \Phi\left(\frac{a - \mu}{\sigma}\right)$.

Para mostrar cómo el corolario se deriva de la Proposición 3.5-2, primero aplicamos la fórmula (3.5.4) con $a = -\mu$ y $b = 1$ para ver que si $X \sim N(\mu, \sigma^2)$, entonces

$$
X - \mu \sim N(0, \sigma^2).
$$

Una segunda aplicación de la fórmula (3.5.4) con $a = 0$ y $b = \frac{1}{\sigma}$, para el resultado anterior, implica que $\frac{X - \mu}{\sigma} \sim N(0, 1)$ (la normal estándar, $Z$). Por lo tanto, al restarle su media y dividirla por su desviación estándar, esto implica que cualquier evento de la forma $a \leq X \leq b$ se puede expresar en términos de la variable estandarizada:

$$
[a \leq X \leq b] = \left[\frac{a - \mu}{\sigma} \leq \frac{X - \mu}{\sigma} \leq \frac{b - \mu}{\sigma}\right].
$$

Así, la parte (2) del Corolario 3.5-1 se sigue de

$$
P(a \leq X \leq b) = P\left(\frac{a - \mu}{\sigma} \leq \frac{X - \mu}{\sigma} \leq \frac{b - \mu}{\sigma}\right) = \Phi\left(\frac{b - \mu}{\sigma}\right) - \Phi\left(\frac{a - \mu}{\sigma}\right),
$$
donde la última igualdad se deriva del hecho de que $\frac{(X - \mu)}{\sigma}$ tiene la distribución normal estándar.

**Ejemplo 3.5-4** Sea $X \sim N(1.25, 0.462)$. Encuentra (a) $P(1 \leq X \leq 1.75)$ y (b) $P(X > 2)$.

**Solución** Una aplicación directa de la parte (2) del Corolario 3.5-1 da lugar a

$$
P(1 \leq X \leq 1.75) = \Phi\left(\frac{1.75 - 1.25}{0.46}\right) - \Phi\left(\frac{1 - 1.25}{0.46}\right) = \Phi(1.09) - \Phi(-0.54) = 0.8621 - 0.2946 = 0.5675.
$$

Trabajando de manera similar para el evento en la parte (b), tenemos

$$
P(X > 2) = P\left(Z > \frac{2 - 1.25}{0.46}\right) = 1 - \Phi(1.63) = 0.0516.
$$

Otra consecuencia del Corolario 3.5-1 es que la regla del 68-95-99.7\% de la normal estándar vista en el Ejemplo 3.5-3 se aplica para cualquier variable aleatoria normal $X \sim N(\mu, \sigma^2)$:

$$
P(\mu - 1\sigma < X < \mu + 1\sigma) = P(-1 < Z < 1) = 0.6826,
$$
$$
P(\mu - 2\sigma < X < \mu + 2\sigma) = P(-2 < Z < 2) = 0.9544,
$$
y
$$
P(\mu - 3\sigma < X < \mu + 3\sigma) = P(-3 < Z < 3) = 0.9974.
$$

**Encontrando Percentiles**

 De acuerdo con la notación introducida en la Definición 3.3-1, el percentil $(1-\alpha)$-100 de $Z$ se denotará como $z_\alpha$. Por lo tanto, el área bajo la PDF normal estándar a la derecha de $z_\alpha$ es $\alpha$, como se muestra en el panel derecho de la Figura 3-16. El panel izquierdo de esta figura ilustra la propiedad definitoria de $z_\alpha$, es decir,

$$
\Phi(z_\alpha) = 1 - \alpha,
$$

que se utiliza para encontrar $z_\alpha$. Dado que la función $\Phi$ no tiene una expresión en forma cerrada, usamos la Tabla A.3 para resolver esta ecuación, localizando primero $1 - \alpha$ en el cuerpo de la tabla y luego leyendo $z_\alpha$ de los márgenes. Si el valor exacto de $1 - \alpha$ no existe en el cuerpo de la tabla, se utiliza una aproximación. Este proceso se demuestra en el siguiente ejemplo.

**Ejemplo 3.5-5** Encuentra el percentil $95$ de $Z$.

**Solución**

Aquí $\alpha = 0.05$, así que $1 - \alpha = 0.95$. Sin embargo, el número exacto $0.95$ no existe en el cuerpo de la Tabla A.3. Así que usamos la entrada que es más cercana pero mayor que $0.95$ (que es $0.9505$), así como la entrada que es más cercana pero menor que $0.95$ (que es $0.9495$), y aproximamos $z_{0.05}$ promediando los valores de $z$ que corresponden a estas dos entradas más cercanas:

$$
z_{0.05} \approx \frac{1.64 + 1.65}{2} = 1.645.
$$

El uso de la Tabla A.3 para encontrar percentiles de cualquier variable normal se hace posible a través del siguiente corolario a la Proposición 3.5-2.

**Corolario 3.5-2** Sea $X \sim N(\mu, \sigma^2)$, y sea $x_\alpha$ el percentil $(1 - \alpha)$-100 de $X$. Entonces,

$$
x_\alpha = \mu + \sigma z_\alpha. \tag{3.5.5}
$$

Para la prueba de este corolario, debe mostrarse que $P(X \leq \mu + \sigma z_\alpha) = 1 - \alpha$. Pero esto sigue de la aplicación de la parte (2) del Corolario 3.5-1 con $a = -\infty$ y $b = \mu + \sigma z_\alpha$:

$$
P(X \leq \mu + \sigma z_\alpha) = \Phi(z_\alpha) - \Phi(-\infty) = 1 - \alpha - 0 = 1 - \alpha.
$$

**Ejemplo 3.5-6** Sea $X \sim N(1.25, 0.462)$. Encuentra el percentil $95$, $x_{0.05}$, de $X$.

**Solución** De (3.5.5) tenemos

$$
x_{0.05} = 1.25 + 0.46 z_{0.05} = 1.25 + (0.46)(1.645) = 2.01.
$$

**EJERCICIO 10**

La Distribución Normal (o Distribución Gaussiana) es la distribución de probabilidad más importante debido al **Teorema del Límite Central**, que establece que la suma o promedio de un gran número de variables aleatorias (independientes e idénticamente distribuidas) tiende a seguir una distribución normal. Esto la hace ideal para modelar fenómenos que resultan de la acumulación de muchos pequeños factores aleatorios.

***

## ⚛️ Nanotecnología

En nanotecnología, la Distribución Normal se utiliza para modelar la variabilidad inherente en las estructuras y procesos a escala nanométrica.

### Ejemplos y Usos Recomendados

1.  **Distribución de Tamaño de Nanopartículas:**
    * **Ejemplo:** Al sintetizar **puntos cuánticos** o nanopartículas de oro, el tamaño promedio ($\mu$) y la desviación estándar ($\sigma$) del lote siguen una distribución normal.
    * **Uso Recomendado:** Se emplea para **control de calidad** y **caracterización**. Una $\sigma$ pequeña indica una distribución de tamaño estrecha (monodispersa), lo cual es crucial para aplicaciones que dependen de propiedades ópticas o electrónicas específicas (p. ej., nanomedicina o *displays* QLED).

2.  **Variabilidad en Nanodispositivos:**
    * **Ejemplo:** Las variaciones en la longitud de canal o el grosor de la capa aislante de un **nanotransistor** (FET) debido a imprecisiones en la litografía.
    * **Uso Recomendado:** Modelar el rendimiento de los dispositivos. La distribución normal permite predecir el **rendimiento** (o *yield*) de fabricación, estableciendo tolerancias aceptables para el diseño del dispositivo.

3.  **Mediciones Instrumentales:**
    * **Ejemplo:** Las mediciones repetidas del espesor de una **película delgada** utilizando un Microscopio de Fuerza Atómica (AFM).
    * **Uso Recomendado:** Se asume que el **ruido experimental** y el error de medición siguen una distribución normal. Esto permite calcular intervalos de confianza y determinar si las diferencias entre dos muestras son estadísticamente significativas.

***

## 🤖 Inteligencia Artificial (IA) y Aprendizaje Automático

La Distribución Normal es fundamental tanto en la teoría como en la aplicación de numerosos algoritmos de IA, especialmente en el aprendizaje automático (*Machine Learning*).

### Ejemplos y Usos Recomendados

1.  **Inicialización de Pesos en Redes Neuronales:**
    * **Ejemplo:** Al construir una red neuronal profunda, los **pesos sinápticos** se inicializan a menudo muestreándolos de una distribución normal con media cero y una desviación estándar pequeña (p. ej., Inicialización de Xavier o He).
    * **Uso Recomendado:** Asegurar que las neuronas en las primeras capas reciban entradas con una varianza adecuada, evitando que las señales se **saturen** o **desaparezcan** (problemas de *vanishing/exploding gradients*) durante el entrenamiento.

2.  **Algoritmos de Clasificación Gaussiana:**
    * **Ejemplo:** El clasificador **Naive Bayes**, que asume que las características numéricas, condicionadas a la clase, siguen una distribución normal.
    * **Uso Recomendado:** Se utiliza para la **clasificación de datos continuos**. Aunque la suposición de independencia ("naive") es fuerte, es simple y sorprendentemente efectivo.

3.  **Modelos de Densidad y Generación de Datos:**
    * **Ejemplo:** **Modelos de Mezclas Gaussianas (GMM)**, utilizados para agrupar (clustering) datos o modelar la distribución de probabilidad de conjuntos de datos complejos.
    * **Uso Recomendado:** Estimar la forma subyacente de los datos. También es la base para algunos **Modelos Generativos** (como los VAEs), donde el espacio latente de la información (el *código* de la imagen o dato) se modela con una distribución normal multivariada.

***

## 🧪 Diseño de Experimentos (DOE)

En DOE, la distribución normal no solo se usa para modelar los datos, sino que es una **suposición fundamental** para validar los resultados de las pruebas estadísticas más comunes.

### Ejemplos y Usos Recomendados

1.  **Análisis de Varianza (ANOVA):**
    * **Ejemplo:** Un experimento para determinar cómo dos factores (temperatura y presión) afectan la resistencia de un material.
    * **Uso Recomendado:** La validez de las pruebas $t$ y $F$ en el análisis ANOVA **depende de la suposición de que los errores (residuos)** del modelo siguen una distribución normal. Se realizan pruebas de normalidad (como Shapiro-Wilk) para confirmar esta suposición.

2.  **Cálculo de Intervalos de Confianza y Pruebas de Hipótesis:**
    * **Ejemplo:** Determinar si el rendimiento promedio de un nuevo proceso de síntesis ($\mu_{\text{nuevo}}$) es significativamente mayor que el proceso estándar ($\mu_{\text{estándar}}$).
    * **Uso Recomendado:** El **Teorema del Límite Central** permite usar la distribución normal para construir intervalos de confianza y realizar pruebas $Z$ o $t$ (basadas en la normal) sobre las medias muestrales, incluso si la población original no es perfectamente normal (si el tamaño de la muestra es grande).

3.  **Control Estadístico de Procesos (SPC):**
    * **Ejemplo:** Monitorear el peso promedio de tabletas en una línea farmacéutica o el voltaje de salida de una fuente de alimentación.
    * **Uso Recomendado:** Se utilizan **Gráficos de Control** basados en la normal (como los gráficos $\bar{X}$ y R) para establecer límites de control (generalmente $\mu \pm 3\sigma$). Si una muestra cae fuera de este rango, el proceso se considera "fuera de control" y requiere investigación.

### Codigo en phyton

```python
"""
## Cargar librerías necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

## Definir un rango de valores para x
## Se usa np.linspace para replicar la secuencia de valores
x = np.linspace(-10, 10, num=201) # 201 puntos para tener el mismo paso de 0.1

## Definir diferentes valores de media (mu) y desviación estándar (sigma)
params = pd.DataFrame({
    'mu': [-2, 0, 2],
    'sigma': [1, 1, 1.5]
})

## Crear un data frame vacío para almacenar los resultados de la PDF
pdf_data = pd.DataFrame()

## Calcular la PDF para cada combinación de mu y sigma
for index, row in params.iterrows():
    mu = row['mu']
    sigma = row['sigma']

## Calcular la función de densidad de probabilidad
## norm.pdf(x, loc=mu, scale=sigma) es el equivalente a dnorm(x, mean = mu, sd = sigma)
    pdf_values = norm.pdf(x, loc=mu, scale=sigma)

## Almacenar los resultados en un data frame
    temp_df = pd.DataFrame({
        'x': x,
        'y': pdf_values,
## Convertir mu y sigma a string para que seaborn los trate como variables categóricas
        'mu': str(mu),
        'sigma': str(sigma)
    })
    pdf_data = pd.concat([pdf_data, temp_df], ignore_index=True)

## ----------------------------------------------------------------------
## Graficar la distribución normal
plt.figure(figsize=(10, 6))

## Usar seaborn para trazar las líneas
sns.lineplot(
    data=pdf_data,
    x='x',
    y='y',
    hue='mu',           # Mapea 'mu' a color
    style='sigma',      # Mapea 'sigma' al estilo de línea (linetype)
    linewidth=2,
## Definir los colores manualmente, asegurando que coincidan con los valores string de 'mu'
    palette={' -2': 'blue', ' 0': 'red', ' 2': 'green'}
)

## Configurar etiquetas y título (usando notación LaTeX para mu y sigma)
plt.title("Funciones de Densidad de Probabilidad de la Distribución Normal", fontsize=16)
plt.xlabel("Valor", fontsize=12)
plt.ylabel("Densidad", fontsize=12)

## Ajustar la leyenda
## Seaborn crea la leyenda automáticamente. Se ajustan los títulos.
legend = plt.legend(title='Media ($\mu$)', loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=5)

## Iterar sobre los elementos de la leyenda para renombrar el título de 'sigma' si es necesario
for text in legend.get_texts():
    if text.get_text() in ['sigma', '1', '1.5']:
        text.set_text(text.get_text().replace('sigma', 'Desviación Estándar ($\sigma$)'))

## Configurar estilo y mostrar la gráfica
sns.despine(trim=True) # Similar a theme_minimal()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
"""
```

## Descripción del Código Python para la Gráfica de la Distribución Normal

El código en **Python** tiene como objetivo ilustrar la **Función de Densidad de Probabilidad (PDF)** de la **Distribución Normal (Gaussiana)**, también conocida como la curva de campana, para **múltiples combinaciones de media ($\mu$) y desviación estándar ($\sigma$)**. Esto se logra mediante el uso de **NumPy** para operaciones numéricas, **Pandas** para estructurar los datos y **SciPy** para la función estadística, con **Matplotlib** y **Seaborn** para la visualización.

***

 1. Inicialización y Definición de Parámetros

| Código | Descripción |
| :--- | :--- |
| `import numpy as np`, `import pandas as pd`, etc. | **Carga de Librerías**: Importa las librerías estándar: **NumPy** (cálculos de arrays), **Pandas** (manejo de datos tabulares), **Matplotlib** y **Seaborn** (gráficos), y **`norm`** de `scipy.stats` (funciones estadísticas para la distribución normal). |
| `x = np.linspace(-10, 10, num=201)` | **Definición del Eje $x$**: Crea un array de 201 puntos uniformemente espaciados entre $-10$ y $10$. Esto define el rango de la variable aleatoria a graficar, abarcando gran parte de la probabilidad para las combinaciones de $\mu$ y $\sigma$ definidas. |
| `params = pd.DataFrame({...})` | **Combinaciones de Parámetros**: Define las tres combinaciones ($\mu$, $\sigma$) que se desean graficar: $( -2, 1)$, $(0, 1)$, y $(2, 1.5)$. Estas combinaciones exploran el efecto de cambiar la **media** (posición de la campana) y la **desviación estándar** (ancho y altura de la campana). |

***

 2. Cálculo de la Función de Densidad (PDF)

| Código | Descripción |
| :--- | :--- |
| `for index, row in params.iterrows(): ...` | **Bucle de Cálculo**: Itera sobre cada fila (combinación de parámetros) en el DataFrame `params`. |
| `pdf_values = norm.pdf(x, loc=mu, scale=sigma)` | **Cálculo de la PDF**: Utiliza la función **`norm.pdf()`** de SciPy. Los parámetros de la distribución normal son: **`loc`** (localización), que corresponde a la media ($\mu$), y **`scale`** (escala), que corresponde a la desviación estándar ($\sigma$). |
| `temp_df = pd.DataFrame({...})` | **Almacenamiento Temporal**: Crea un DataFrame para los resultados de la iteración. Las columnas `mu` y `sigma` se convierten a *string* para que Seaborn las pueda usar como **variables categóricas** de agrupación para el color y el estilo. |
| `pdf_data = pd.concat(...)` | **Combinación de Datos**: Combina los DataFrames temporales en el DataFrame final `pdf_data`. Este conjunto de datos unificado es esencial para graficar múltiples líneas usando las capacidades de mapeo de Seaborn. |

***

 3. Visualización y Estilizado del Gráfico

| Código | Descripción |
| :--- | :--- |
| `sns.lineplot(...)` | **Trazado de Múltiples Líneas**: Utiliza la función **`lineplot`** de Seaborn para dibujar las curvas, aprovechando el mapeo de variables: |
| | - `hue='mu'` : Mapea la media ($\mu$) al **color** de la línea. |
| | - `style='sigma'` : Mapea la desviación estándar ($\sigma$) al **estilo de la línea** (sólida, punteada, etc.). Esto permite distinguir las curvas que tienen diferente dispersión. |
| | - `palette` : Asigna colores específicos para los valores de $\mu$ (por ejemplo, $\mu=-2$ es azul, $\mu=0$ es rojo, etc.). |
| `plt.title(...)`, `plt.xlabel(...)`, `plt.ylabel(...)` | **Etiquetas y Títulos**: Establece el título principal (usando texto claro) y las etiquetas de los ejes. |
| `legend = plt.legend(...)` | **Configuración de Leyenda**: Mueve la leyenda a una posición fuera del área de trazado y asigna el título "Media ($\mu$)" a la leyenda de color. |
| `for text in legend.get_texts(): ...` | **Ajuste de Leyenda Secundaria**: Itera sobre los elementos de la leyenda para corregir manualmente el título de la leyenda de estilo, asegurando que se muestre como "Desviación Estándar ($\sigma$)", ya que Seaborn no permite nombrar dos leyendas fácilmente. |
| `sns.despine(trim=True)` y `plt.grid(axis='y', ...)` | **Estilo Final**: Elimina los bordes superior y derecho (`despine`) y añade una cuadrícula horizontal suave para un estilo limpio, similar a `theme_minimal()` de R. |

El resultado es un gráfico que muestra tres curvas de campana:
1.  **Curvas $( -2, 1)$ y $(0, 1)$**: Tienen la misma forma (misma $\sigma$), pero están **desplazadas** horizontalmente, demostrando el efecto de $\mu$.
2.  **Curvas $(0, 1)$ y $(2, 1.5)$**: Tienen diferentes $\sigma$. La curva con $\sigma=1.5$ es más **ancha** y **baja** que la curva con $\sigma=1$, lo que ilustra cómo $\sigma$ afecta la dispersión de los datos.

### Distribución Log-Normal

* **Descripción**: Modelo de variables aleatorias cuyo logaritmo sigue una distribución normal. Es útil para modelar variables que no pueden ser negativas y que tienen una distribución sesgada a la derecha.

* **Parámetros**:
  - $ \mu $ (media del logaritmo de la variable)
  - $ \sigma $ (desviación estándar del logaritmo de la variable)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x) =
\begin{cases}
\frac{1}{x \sigma \sqrt{2\pi}} e^{-\frac{(\log x - \mu)^2}{2\sigma^2}} & \text{si } x > 0 \\
0 & \text{si } x \leq 0
\end{cases}
$$

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) =
\begin{cases}
0 & \text{si } x \leq 0 \\
\Phi\left(\frac{\log x - \mu}{\sigma}\right) & \text{si } x > 0
\end{cases}
$$
donde $ \Phi $ es la función de distribución acumulativa de la distribución normal estándar.

* **Valor Esperado**: $ E[X] = e^{\mu + \frac{\sigma^2}{2}} $

* **Media**: $ \mu_X = e^{\mu + \frac{\sigma^2}{2}} $

* **Desviación Estándar**: $ \sigma_X = e^{\mu + \frac{\sigma^2}{2}} \sqrt{e^{\sigma^2} - 1} $

* **Percentiles**: $ x_\alpha = e^{\mu + \sigma \Phi^{-1}(\alpha)} $

**Comandos en R**:
```r
## PDF
dlnorm(x, meanlog = mu, sdlog = sigma)

## CDF
plnorm(x, meanlog = mu, sdlog = sigma)

## Simulación
rlnorm(n, meanlog = mu, sdlog = sigma)

#### Ejemplo de Gráfica de la Distribución Log-Normal

La distribución log-normal describe un modelo en el que la variable aleatoria se distribuye normalmente en el logaritmo de sus valores. Esto significa que, si una variable $ X $ es log-normales, entonces $ \log(X) $ sigue una distribución normal. Esta distribución es útil en situaciones donde los datos son multiplicativos y no pueden ser negativos, como en la modelación de precios de activos o tiempos de vida de productos.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad $ PDF$ de la distribución log-normal para varios valores de los parámetros $ \mu $ y $ \sigma $, que representan la media y la desviación estándar de la distribución normal subyacente. A medida que se ajustan los valores de $ \mu $ y $\sigma $, la forma de la distribución cambia, reflejando cómo la variabilidad de los datos puede influir en su comportamiento.

La distribución log-normal es especialmente relevante en campos como la economía y la biología, donde se pueden observar fenómenos de crecimiento exponencial.

```python
"""
## Cargar librerías
library(ggplot2)

## Definir un rango de valores para x
x <- seq(0, 10, by = 0.01)

## Definir diferentes valores de mu y sigma
params <- data.frame(
  mu = c(0, 1, 2),
  sigma = c(0.5, 1, 1.5)
)

## Crear un data frame vacío para almacenar los resultados
results <- data.frame()

## Calcular la PDF para cada combinación de mu y sigma
for (i in 1:nrow(params)) {
  mu <- params$mu[i]
  sigma <- params$sigma[i]

  pdf_values <- dlnorm(x, meanlog = mu, sdlog = sigma)

  temp_df <- data.frame(x = x, PDF = pdf_values,
                        mu = mu, sigma = sigma)
  results <- rbind(results, temp_df)
}

## Graficar la PDF de la distribución log-normal
ggplot(results, aes(x = x, y = PDF, color = interaction(mu, sigma))) +
  geom_line(size = 1) +
  labs(title = "Distribución Log-Normal para Diferentes Parámetros",
       x = "x",
       y = "Densidad de Probabilidad (PDF)",
       color = "Parámetros (mu, sigma)") +
  theme_minimal()
  """
```

#### Descripción del Código

* **Cargar librerías**: Se utiliza `ggplot2` para crear la gráfica.
* **Definir un rango de valores para $ x $**: Se establece un rango de valores de $ 0 $ a $ 10 $.
* **Definir diferentes valores de $ \mu $ y $ \sigma $**: Se crean combinaciones de parámetros para la distribución log-normal.
* **Crear un data frame vacío**: Se inicializa un data frame para almacenar los resultados de la $PDF$.
* **Calcular la PDF**: Se utiliza `dlnorm()` para calcular la función de densidad de probabilidad para cada combinación de $ \mu $ y $ \sigma $.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $ PDF $ de la distribución log-normal para diferentes parámetros.

**EJERCICIO 11**

La **Distribución Log-Normal** es la distribución de probabilidad de una variable aleatoria cuyo logaritmo sigue una distribución normal. Se utiliza para modelar cantidades que son inherentemente **positivas** (como tamaños, duraciones, ingresos) y cuyos valores son el resultado de la **multiplicación de muchos factores aleatorios independientes**, a diferencia de la normal, que modela la suma de factores.

A continuación, se presentan ejemplos y usos recomendados en Nanotecnología, Ciencia de Materiales e Inteligencia Artificial.

***

## ⚛️ Nanotecnología y Ciencia de Materiales

En estos campos, la Log-Normal es fundamental para modelar la **distribución de tamaños** y los **tiempos de vida o fatiga**, ya que estas variables no pueden ser negativas y tienden a concentrarse cerca de cero con una larga cola positiva.

### Ejemplos y Usos Recomendados

### 1. Distribución de Tamaño de Partículas

* **Ejemplo:** El **diámetro de las nanopartículas** (metálicas, de óxido o poliméricas) o el **tamaño de grano** en materiales policristalinos.
* **Uso Recomendado:** La formación de nanopartículas (nucleación y crecimiento) es un proceso multiplicativo. La Log-Normal es el **modelo estándar preferido** para describir la dispersión del tamaño de las partículas. Esto es crucial para predecir las propiedades ópticas, catalíticas o magnéticas que dependen críticamente del tamaño.

### 2. Tiempos de Vida y Fatiga

* **Ejemplo:** La **vida útil** o el **tiempo hasta la falla** de ciertos recubrimientos, películas delgadas o materiales sujetos a procesos de degradación multiplicativa (como el crecimiento de grietas por fatiga).
* **Uso Recomendado:** Se utiliza en **análisis de fiabilidad** (confiabilidad) cuando la tasa de fallo de un componente no es constante (como en la exponencial) sino que **aumenta con el tiempo**. Proporciona una estimación más precisa de la supervivencia en el largo plazo que la Distribución de Weibull en ciertos contextos.

### 3. Distribución de Defectos y Dispersión

* **Ejemplo:** La dispersión en el **espesor** o la **conductividad** de películas depositadas por técnicas estocásticas, donde la variación no es simétrica alrededor de la media.
* **Uso Recomendado:** Modelar la **variabilidad intrínseca** de los materiales. Permite a los ingenieros establecer límites de especificación basados en la probabilidad (por ejemplo, asegurar que el 99% de los granos son más pequeños que un tamaño dado).

***

## 🤖 Inteligencia Artificial (IA) y Aprendizaje Automático

Aunque la Distribución Normal es más común en la IA (por el Teorema del Límite Central), la Log-Normal aparece en el modelado de datos del mundo real que exhiben asimetría y en sistemas complejos.

### Ejemplos y Usos Recomendados

### 1. Distribución de Atributos Asimétricos

* **Ejemplo:** El **tiempo de respuesta** de un servidor, la **latencia** de red, el **número de comentarios** en una publicación, o el **ingreso** de los usuarios en un conjunto de datos. Todas estas variables son positivas y están sesgadas hacia la derecha.
* **Uso Recomendado:** **Preprocesamiento de datos** y **selección de modelos**. Antes de aplicar algoritmos que asumen normalidad (como la Regresión Lineal o algunas pruebas estadísticas), se recomienda aplicar una **transformación logarítmica** a estas variables para hacerlas más "normales". Si el logaritmo transformado se ajusta bien a una normal, se dice que el atributo original sigue una Log-Normal.

### 2. Modelos Generativos (Log-Normal VAEs)

* **Ejemplo:** En el desarrollo de **Modelos Variacionales Auto-Codificadores (VAEs)** o en otros modelos generativos, se puede utilizar una distribución Log-Normal para modelar el **espacio latente** (el "código" interno) de datos que tienen una naturaleza intrínsecamente positiva y asimétrica.
* **Uso Recomendado:** Mejorar la **calidad de la generación** de datos no negativos y sesgados, como el tamaño de las imágenes o la duración de los eventos en series temporales.

### 3. Aprendizaje por Refuerzo y Modelado de Riesgo

* **Ejemplo:** El **tamaño de las recompensas** o las **pérdidas financieras** en simulaciones de aprendizaje por refuerzo aplicadas a escenarios económicos o de gestión de riesgos.
* **Uso Recomendado:** Modelar la incertidumbre en sistemas donde los efectos son multiplicativos. La Log-Normal es esencial en modelos de finanzas matemáticas (como el modelo Black-Scholes), lo cual se extrapola a los modelos de IA que gestionan carteras de inversión o riesgos operativos, ya que asume que los retornos son Log-Normales.

#### Codigo en phyton

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import lognorm # Importamos la función de distribución log-normal

## ----------------------------------------------------
## 1. Definir un rango de valores para x
## Similar a seq(0, 10, by = 0.01) en R
x = np.arange(0.01, 10.01, 0.01) # Empezamos ligeramente arriba de 0 para evitar log(0)

## 2. Definir diferentes valores de mu (media del log) y sigma (desviación del log)
params = pd.DataFrame({
    'mu': [0, 1, 2],
    'sigma': [0.5, 1, 1.5]
})

## 3. Crear una lista para almacenar los DataFrames de los resultados
results_list = []

## 4. Calcular la PDF para cada combinación de mu y sigma
for index, row in params.iterrows():
    mu = row['mu']
    sigma = row['sigma']

## La función lognorm.pdf() de scipy.stats es el equivalente a dlnorm() en R.
## Los parámetros son:
## 's' es la desviación estándar del log (sdlog/sigma).
## 'scale' es el valor de exp(mu) (antilogaritmo de meanlog).
    pdf_values = lognorm.pdf(x, s=sigma, scale=np.exp(mu))

## Crear una etiqueta combinada para la leyenda, similar a interaction(mu, sigma)
    label = f"({mu}, {sigma})"

## Almacenar los resultados en un DataFrame temporal
    temp_df = pd.DataFrame({
        'x': x,
        'PDF': pdf_values,
        'mu': mu,
        'sigma': sigma,
        'label': label
    })
    results_list.append(temp_df)

## 5. Concatenar todos los DataFrames
results = pd.concat(results_list, ignore_index=True)

## 6. Graficar la PDF de la distribución log-normal usando Seaborn

## Configuración de Seaborn para el estilo
sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))

## Usar seaborn.lineplot
sns.lineplot(
    data=results,
    x='x',
    y='PDF',
    hue='label', # Usar la etiqueta combinada para el color de la línea
    linewidth=2
)

## Añadir etiquetas y título (equivalente a labs)
plt.title("Distribución Log-Normal para Diferentes Parámetros", fontsize=16)
plt.xlabel("x", fontsize=12)
plt.ylabel("Densidad de Probabilidad (PDF)", fontsize=12)

## Configurar la leyenda
plt.legend(title='Parámetros (mu, sigma)', loc='upper right')

## Mostrar la gráfica
plt.show()
```

## Descripción del Código Python para la Gráfica de la Distribución Log-Normal

El código en **Python** calcula y visualiza la **Función de Densidad de Probabilidad (PDF)** de la **Distribución Log-Normal** para múltiples combinaciones de sus parámetros. La distribución Log-Normal se utiliza a menudo para modelar variables aleatorias que son el resultado de la exponenciación de una variable con distribución Normal, por lo que solo toma valores positivos ($x > 0$) y está sesgada positivamente.

El código emplea **SciPy** para la función estadística, **NumPy** para operaciones numéricas y **Pandas** para estructurar los datos, con **Matplotlib** y **Seaborn** para la representación gráfica.

***

### 1. Inicialización y Preparación de Parámetros

| Código | Descripción |
| :--- | :--- |
| `from scipy.stats import lognorm` | **Librería Estadística**: Importa la clase `lognorm` de SciPy, que contiene la función `pdf()` equivalente a `dlnorm()` en R. |
| `x = np.arange(0.01, 10.01, 0.01)` | **Definición del Eje $x$**: Crea un rango de valores para la variable $x$ desde $0.01$ hasta $10.01$ con incrementos de $0.01$. Se comienza ligeramente por encima de cero porque la distribución Log-Normal solo está definida para $x > 0$. |
| `params = pd.DataFrame({...})` | **Combinaciones de Parámetros**: Define tres combinaciones de los parámetros de la distribución Normal subyacente: **`mu`** (media del log, *meanlog* en R) y **`sigma`** (desviación estándar del log, *sdlog* en R). Las combinaciones son: $(0, 0.5)$, $(1, 1)$, y $(2, 1.5)$. |

***
| Código | Parámetro `lognorm.pdf` | Parámetro R (`dlnorm`) | Significado Estadístico |
| :--- | :--- | :--- | :--- |
| `s` | **`s`** | `sdlog` ($\sigma$) | La desviación estándar de $\ln(X)$. Controla la **forma y el sesgo**. |
| `scale` | **`scale`** | $\exp(\mu)$ | El antilogaritmo de la media del log. Controla la **escala** de la distribución. |

### 2. Cálculo de la Función de Densidad (PDF)

| Código | Descripción |
| :--- | :--- |
| `for index, row in params.iterrows(): ...` | **Bucle de Cálculo**: Itera sobre cada combinación de $\mu$ y $\sigma$ definida en el DataFrame `params`. |
| `pdf_values = lognorm.pdf(x, s=sigma, scale=np.exp(mu))` | **Cálculo de la PDF**: Llama a la función `lognorm.pdf()`. Es crucial mapear correctamente los parámetros de SciPy: $s$ es $\sigma$, y $scale$ es $\exp(\mu)$. |
| `label = f"({mu}, {sigma})"` | **Etiqueta de Leyenda**: Crea una etiqueta de texto combinada con los valores de $\mu$ y $\sigma$. Esto permite usar una sola variable categórica (`label`) para diferenciar las tres curvas en la gráfica. |
| `results = pd.concat(results_list, ignore_index=True)` | **Estructura de Datos Final**: Combina todos los DataFrames temporales en un único DataFrame (`results`), listo para la visualización. |

***

### 3. Visualización del Gráfico

| Código | Descripción |
| :--- | :--- |
| `sns.set_theme(style="whitegrid")` | **Estilo de Gráfico**: Configura un estilo limpio de cuadrícula blanca de Seaborn. |
| `sns.lineplot(...)` | **Trazado de Múltiples Líneas**: Utiliza la función `lineplot` de Seaborn para dibujar las curvas de densidad. |
| | - `x='x', y='PDF'` : Define los ejes. |
| | - `hue='label'` : Mapea la etiqueta combinada (ej: "(0, 0.5)") al **color** de la línea. |
| `plt.title(...)`, `plt.xlabel(...)`, `plt.ylabel(...)` | **Etiquetas y Títulos**: Establece el título principal, especificando claramente la distribución y las etiquetas de los ejes. |

El resultado final es un gráfico con tres curvas de densidad, todas con un sesgo positivo pronunciado (cola larga a la derecha) y que comienzan en cero en el eje $x$. La gráfica ilustra que:
1.  **Incrementar $\mu$** (manteniendo $\sigma$ constante) desplaza el pico de la distribución más a la derecha y reduce su altura.
2.  **Incrementar $\sigma$** (manteniendo $\mu$ constante o no) aumenta el sesgo, haciendo que la curva sea más ancha y más plana, lo que indica una mayor dispersión de los datos.

### Distribución Gamma

* **Descripción**: Modelo de tiempo hasta el k-ésimo evento en un proceso de Poisson. Se utiliza en diversos campos, como la teoría de colas y la fiabilidad.

* **Parámetros**:
  - $ k $ (forma, número de eventos)
  - $ \theta $ (escala)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x) =
\begin{cases}
\frac{x^{k-1} e^{-\frac{x}{\theta}}}{\theta^k \Gamma(k)} & \text{si } x \geq 0 \\
0 & \text{si } x < 0
\end{cases}
$$
donde $ \Gamma(k) $ es la función gamma.

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) = \int_0^x f(t) \, dt
$$

* **Valor Esperado**: $ E[X] = k \theta $

* **Media**: $ \mu_X = k \theta $

* **Desviación Estándar**:
$$
\sigma = \sqrt{k} \theta
$$

* **Percentiles**: $ x_\alpha $ se obtiene usando la función inversa de la CDF.

**Comandos en R**:
```r
## PDF
dgamma(x, shape = k, scale = theta)

## CDF
pgamma(x, shape = k, scale = theta)

## Simulación
rgamma(n, shape = k, scale = theta)

#### Función Gamma $Γ()$

La **función gamma** es una extensión del factorial a los números reales y complejos. Se utiliza ampliamente en matemáticas, estadísticas y teoría de la probabilidad.

##### Definición

La función gamma se define como:

$$
\Gamma(z) = \int_0^{\infty} t^{z-1} e^{-t} \, dt
$$

donde:
- $ z $ es un número complejo con parte real positiva. Este parámetro puede ser un número entero, fraccionario o complejo. En el contexto de la función gamma,$ z $ se puede interpretar como un "número de elementos" que se están evaluando.

##### Propiedades

1. **Relación con el factorial**:
   Para números enteros positivos $ n $, la función gamma se relaciona con el factorial de la siguiente manera:

   $$
   \Gamma(n) = (n-1)!
   $$

   Por ejemplo:
   - $\Gamma(1) = 0! = 1 $
   - $\Gamma(2) = 1! = 1 $
   - $\Gamma(3) = 2! = 2 $

2. **Relación de recurrencia**:
   La función gamma satisface la relación:

   $$
   \Gamma(z + 1) = z \Gamma(z)
   $$

   Esta propiedad permite calcular valores de la función gamma a partir de otros valores.

3. **Valores específicos**:
   - $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi} $

**Usos en Estadística**

- La función gamma es fundamental en la definición de varias distribuciones, como la distribución gamma, la distribución Chi-cuadrada y la distribución F.
- Se utiliza en el cálculo de funciones de densidad y en la estadística bayesiana.

**Ejemplo de Cálculo**

Para calcular $ \Gamma(5) $:

$$
\Gamma(5) = \int_0^{\infty} t^{5-1} e^{-t} \, dt = \int_0^{\infty} t^4 e^{-t} \, dt = 4! = 24
$$

**Cálculo de la Función Gamma en R**

La función gamma se puede calcular en R utilizando la función `gamma()`. Aquí te muestro cómo hacerlo:

```r
## Cálculo de la función gamma
gamma_value <- gamma(z)

```python
"""
## Cálculo de Gamma(5)
z <- 5
gamma_value <- gamma(z)
print(gamma_value)
"""
```

Gráfica de la función Gamma $Γ$

```python
"""
## Cargar la librería necesaria
library(ggplot2)

## Crear un rango de valores para z
z_values <- seq(0.1, 5, by = 0.1)

## Calcular los valores de la función gamma
gamma_values <- gamma(z_values)

## Crear un data frame para ggplot
data <- data.frame(z = z_values, gamma = gamma_values)

## Graficar la función gamma
ggplot(data, aes(x = z, y = gamma)) +
  geom_line(color = "blue") +
  labs(title = "Gráfico de la Función Gamma",
       x = "z",
       y = expression(gamma(z))) +
  theme_minimal()
"""
```

#### Ejemplo de Gráfica de la Distribución Gamma

La distribución gamma es una distribución continua que describe el tiempo hasta que ocurren un número específico de eventos en un proceso de Poisson. Es útil en situaciones donde se modelan fenómenos como el tiempo de espera hasta un evento, donde la variable aleatoria puede ser positiva y no tiene un límite superior.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad $PDF $ de la distribución gamma para varios valores de los parámetros $ k $ (forma) y $\theta$ (escala). A medida que se ajustan los valores de $ k $ y $ \theta $, la forma de la distribución cambia, mostrando cómo la variabilidad en los parámetros influye en la probabilidad de que ocurran diferentes resultados.

La distribución gamma es especialmente relevante en áreas como la ingeniería, la economía y la investigación científica, donde se modelan tiempos de espera y otras variables continuas.

```python
"""
## Cargar la librería necesaria
library(ggplot2)

## Definir los parámetros de la distribución gamma
shape1 <- 2  # Parámetro de forma (k)
scale1 <- 1  # Parámetro de escala (theta)

shape2 <- 5  # Otro parámetro de forma
scale2 <- 1  # Mismo parámetro de escala

## Crear un rango de valores para x
x_values <- seq(0, 20, by = 0.1)

## Calcular la función de densidad de la distribución gamma
gamma_density1 <- dgamma(x_values, shape = shape1, scale = scale1)
gamma_density2 <- dgamma(x_values, shape = shape2, scale = scale2)

## Crear un data frame para ggplot
data <- data.frame(x = x_values,
                   density1 = gamma_density1,
                   density2 = gamma_density2)

## Graficar la distribución gamma
ggplot(data, aes(x = x)) +
  geom_line(aes(y = density1), color = "blue", linewidth = 1) +
  geom_line(aes(y = density2), color = "red", linewidth = 1) +
  labs(title = "Gráfico de la Distribución Gamma",
       x = "x",
       y = "Densidad") +
  theme_minimal() +
  scale_y_continuous(expand = expansion(mult = c(0, 0.1))) +
  theme(legend.position = "top") +
  geom_area(aes(y = density1), fill = "blue", alpha = 0.1) +
  geom_area(aes(y = density2), fill = "red", alpha = 0.1) +
  scale_color_manual(name = "Distribución",
                     values = c("Gamma(2, 1)" = "blue", "Gamma(5, 1)" = "red")) +
  geom_line(aes(y = density1, color = "Gamma(2, 1)")) +
  geom_line(aes(y = density2, color = "Gamma(5, 1)"))
"""
```

#### Descripción del Código

* **Cargar librerías**: Se utiliza `ggplot2` para crear la gráfica.
* **Definir los parámetros**: Se establecen los parámetros de forma $ k $ y escala $\theta $ para la distribución gamma.
* **Crear un rango de valores para $x $**: Se define un rango de valores de $ 0 $ a $ 20 $ para representar la distribución.
* **Calcular la PDF**: Se utiliza `dgamma()` para calcular la función de densidad de probabilidad para los valores de $x$ con los parámetros definidos.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $x$ y sus correspondientes probabilidades para las dos configuraciones de la distribución gamma.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $ PDF $ de la distribución gamma para los diferentes parámetros, incluyendo áreas sombreadas para visualizar mejor las densidades.

**EJERCICIO 12**

La **Distribución Gamma** es una distribución de probabilidad continua muy flexible que se utiliza para modelar tiempos de espera, duraciones, cantidades sumadas y variables positivas y asimétricas. Es una generalización de la Distribución Exponencial (cuando el parámetro de forma, $k$, es 1) y se relaciona estrechamente con la Distribución Chi-cuadrado.

Se caracteriza por dos parámetros clave: el **parámetro de forma** ($k$ o $\alpha$) y el **parámetro de escala** ($\theta$ o $\beta$).

## ⚛️ Nanotecnología y Ciencia de Materiales

En estos campos, la Distribución Gamma es valiosa porque puede modelar la **variabilidad de los procesos de crecimiento** y la **acumulación de daño** que ocurren en múltiples etapas.

***

### 1. Modelado de Procesos de Crecimiento de Materiales

Cuando una variable (como el tamaño de una partícula) es el resultado de una **suma de varias etapas de crecimiento exponencial**, la Distribución Gamma es el modelo ideal.

| Escenario | Uso Recomendado | Concepto Clave |
| :--- | :--- | :--- |
| **Crecimiento de Nanocristales** | Modelar el **tiempo total** necesario para que un nanocristal alcance un tamaño crítico, asumiendo que el crecimiento ocurre en **múltiples etapas de reacción** independientes (nucleación, crecimiento capa por capa, etc.). | El parámetro de **forma ($k$)** se interpreta como el **número de pasos** o la complejidad del proceso de crecimiento. Si un proceso tiene $k$ etapas de duración exponencial con la misma tasa ($\lambda = 1/\theta$), la duración total sigue una Gamma. |
| **Distribución del Tamaño de Grano** | En ciertos procesos de sinterización o recocido de metales y cerámicas, el tamaño de grano es una **variable positiva y sesgada**. | La Log-Normal es común para el tamaño de partícula, pero la Gamma puede ofrecer un **mejor ajuste** en casos donde el proceso de formación implica una **acumulación secuencial de incrementos** (suma de efectos) en lugar de un proceso multiplicativo. |

***

### 2. Análisis de Fiabilidad y Durabilidad

La Distribución Gamma se utiliza para modelar el tiempo de vida o la acumulación de daño, especialmente cuando el fallo es el resultado de superar un umbral de daño.

| Escenario | Uso Recomendado | Concepto Clave |
| :--- | :--- | :--- |
| **Daño por Radiación o Fatiga** | Modelar la **acumulación de daño** en polímeros o semiconductores por exposición continua a la radiación. El daño se considera un proceso que **se acumula linealmente** con el tiempo, y el fallo ocurre cuando el daño alcanza un nivel $k$ (umbral). | El tiempo de fallo sigue una distribución Gamma. El parámetro de **escala ($\theta$)** se relaciona con la **tasa de daño** por unidad de tiempo. |
| **Tiempo de Vida de Baterías/Celdas** | Modelar el tiempo hasta que una batería de nanoestructuras (p. ej., nanohilos) alcanza una capacidad residual crítica. | Es una alternativa a la Distribución de Weibull y la Log-Normal en la **ingeniería de fiabilidad**, ya que permite que la **tasa de fallo cambie con el tiempo**. Si la tasa de fallo es constante, $k=1$ (Exponencial). Si la tasa aumenta, $k>1$ (más común en el desgaste). |

***

### 3. Modelado de Variables de Proceso

La Gamma puede modelar variables de proceso que son el resultado de la acumulación de muchos eventos aleatorios y son inherentemente no negativas.

| Escenario | Uso Recomendado | Concepto Clave |
| :--- | :--- | :--- |
| **Rugosidad Superficial** | En la deposición de películas delgadas, la rugosidad superficial es una variable positiva y está influenciada por muchos depósitos aleatorios. | La Gamma es efectiva para modelar la **distribución de la altura de los picos** en una superficie rugosa, que no puede ser negativa y presenta asimetría. |
| **Análisis de Colas de Procesos** | En una instalación de procesamiento de materiales, modelar el **tiempo de espera total** que una muestra pasa a través de una secuencia de $k$ estaciones de trabajo, donde cada estación tiene un tiempo de procesamiento exponencial. | La distribución Gamma modela el tiempo de espera total acumulado, permitiendo optimizar el flujo de trabajo y la programación de la producción. |

#### Codigo en phyton

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.special import gamma # Importamos la función gamma de SciPy

## ----------------------------------------------------
## 1. Crear un rango de valores para z
## Similar a seq(0.1, 5, by = 0.1) en R
z_values = np.arange(0.1, 5.1, 0.1) # Usamos 5.1 para asegurar que incluya el 5

## 2. Calcular los valores de la función gamma
## gamma() de numpy/scipy.special es el equivalente a gamma() en R
gamma_values = gamma(z_values)

## 3. Crear un data frame (opcional, pero ayuda a estructurar)
## Aquí usamos directamente los arrays de NumPy
## data = pd.DataFrame({'z': z_values, 'gamma': gamma_values})

## 4. Graficar la función gamma
sns.set_theme(style="whitegrid") # Similar a theme_minimal()

plt.figure(figsize=(8, 6))

## Trazar la línea (equivalente a geom_line)
plt.plot(z_values, gamma_values, color="blue", linewidth=2)

## Añadir etiquetas y título (equivalente a labs)
plt.title("Gráfico de la Función Gamma", fontsize=16)
plt.xlabel("z", fontsize=12)

## Para usar notación matemática para gamma(z)
plt.ylabel(r"$\Gamma(z)$", fontsize=14)

## Configuración de estética adicional de Matplotlib (simulando theme_minimal)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
```

## Descripción del Código Python para la Gráfica de la Función Gamma

El código en **Python** está diseñado para calcular y visualizar la **Función Gamma, $\Gamma(z)$**, en un rango específico de valores. La **Función Gamma** es una extensión del concepto de factorial a los números reales y complejos, donde $\Gamma(n) = (n-1)!$ para enteros positivos $n$.

El código utiliza **NumPy** para generar el rango de valores, **`scipy.special`** para el cálculo de la función, y **Matplotlib/Seaborn** para la representación gráfica.

***

### 1. Inicialización y Preparación de Valores

| Código | Descripción |
| :--- | :--- |
| `import numpy as np`, `import matplotlib.pyplot as plt`... | **Carga de Librerías**: Importa **NumPy** para el manejo de arrays, **Matplotlib** y **Seaborn** para la visualización, y **`gamma`** de `scipy.special` para el cálculo de la función. |
| `from scipy.special import gamma` | **Función Gamma**: Importa específicamente la función matemática $\Gamma(z)$. |
| `z_values = np.arange(0.1, 5.1, 0.1)` | **Definición del Eje $z$**: Crea un array de valores que irán en el eje horizontal (eje $z$) desde $0.1$ hasta $5.0$, con pasos de $0.1$. Se comienza en $0.1$ porque la Función Gamma tiene una asíntota vertical en $z=0$ (y en los enteros negativos). |

***

### 2. Cálculo de la Función Gamma

| Código | Descripción |
| :--- | :--- |
| `gamma_values = gamma(z_values)` | **Cálculo de $\Gamma(z)$**: Aplica la función `gamma()` de SciPy a cada valor del array `z_values`. Esto genera un nuevo array que contiene los valores de $\Gamma(z)$ correspondientes. |
| `# data = pd.DataFrame(...)` | **Estructura de Datos**: Aunque se podría usar Pandas para crear un DataFrame (como se hace en los ejemplos anteriores), este paso se omite para demostrar que Matplotlib y NumPy pueden graficar directamente los dos arrays resultantes (`z_values` y `gamma_values`). |

***

### 3. Visualización del Gráfico

| Código | Descripción |
| :--- | :--- |
| `sns.set_theme(style="whitegrid")` | **Estilo de Gráfico**: Aplica el estilo `whitegrid` de Seaborn para un fondo limpio con cuadrícula. |
| `plt.figure(figsize=(8, 6))` | **Creación de Figura**: Define el tamaño del lienzo de la gráfica. |
| `plt.plot(z_values, gamma_values, color="blue", linewidth=2)` | **Trazado de la Línea**: Dibuja la curva, mapeando $z\_values$ al eje $x$ y $gamma\_values$ al eje $y$. Se utiliza un color azul y un grosor de línea de 2. |
| `plt.xlabel("z", fontsize=12)` | **Etiqueta del Eje $z$**: Define la etiqueta del eje horizontal. |
| `plt.ylabel(r"$\Gamma(z)$", fontsize=14)` | **Etiqueta del Eje $y$**: Define la etiqueta del eje vertical, utilizando la sintaxis de **LaTeX (`r"$\Gamma(z)$"`)** para mostrar la notación matemática correcta de la Función Gamma. |
| `plt.title(...)` | **Título Principal**: Establece el título "Gráfico de la Función Gamma". |
| `plt.show()` | **Renderizado Final**: Muestra el gráfico, que representa la curva de la función. |

El gráfico resultante muestra la forma característica de la **Función Gamma** para valores positivos: un valle alrededor de $z=1.46$ y un crecimiento rápido a medida que $z$ se incrementa.

#### Codigo en phyton

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import gamma # Importamos la función de distribución Gamma

## ----------------------------------------------------
## 1. Definir los parámetros de la distribución gamma
shape1 = 2    # Parámetro de forma (k)
scale1 = 1    # Parámetro de escala (theta)

shape2 = 5    # Otro parámetro de forma
scale2 = 1    # Mismo parámetro de escala

## 2. Crear un rango de valores para x
## Similar a seq(0, 20, by = 0.1) en R
x_values = np.arange(0, 20.1, 0.1) # Incluimos 20.1 para asegurar que el 20 esté incluido

## 3. Calcular la función de densidad de la distribución gamma
## En SciPy, el parámetro 'a' es la forma (shape) y 'scale' es la escala.
gamma_density1 = gamma.pdf(x_values, a=shape1, scale=scale1)
gamma_density2 = gamma.pdf(x_values, a=shape2, scale=scale2)

## 4. Crear un data frame combinado (similar a la estructura final de ggplot)
## Esto facilita el uso de Seaborn para las leyendas y colores
data1 = pd.DataFrame({
    'x': x_values,
    'Density': gamma_density1,
    'Distribution': f'Gamma({shape1}, {scale1})'
})
data2 = pd.DataFrame({
    'x': x_values,
    'Density': gamma_density2,
    'Distribution': f'Gamma({shape2}, {scale2})'
})

data = pd.concat([data1, data2], ignore_index=True)

## 5. Graficar la distribución gamma usando Matplotlib y Seaborn
sns.set_theme(style="whitegrid") # Similar a theme_minimal()
plt.figure(figsize=(10, 6))

## Definir colores manualmente para la leyenda
colors = {
    f'Gamma({shape1}, {scale1})': 'blue',
    f'Gamma({shape2}, {scale2})': 'red'
}

## 5a. Dibujar áreas sombreadas (equivalente a geom_area)
plt.fill_between(data1['x'], data1['Density'], color='blue', alpha=0.1)
plt.fill_between(data2['x'], data2['Density'], color='red', alpha=0.1)

## 5b. Dibujar las líneas (equivalente a geom_line)
sns.lineplot(
    data=data,
    x='x',
    y='Density',
    hue='Distribution',  # Usa la columna 'Distribution' para el color y la leyenda
    palette=colors,
    linewidth=2
)

## 5c. Añadir etiquetas y título (equivalente a labs)
plt.title("Gráfico de la Distribución Gamma", fontsize=16)
plt.xlabel("x", fontsize=12)
plt.ylabel("Densidad", fontsize=12)

## Configurar la leyenda y su posición (equivalente a theme(legend.position = "top"))
plt.legend(title="Distribución", loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)

## Mostrar la gráfica
plt.show()
```

## Descripción del Código Python para la Gráfica de la Distribución Gamma

El código en **Python** tiene como propósito calcular y visualizar la **Función de Densidad de Probabilidad (PDF)** de la **Distribución Gamma** para **dos conjuntos de parámetros diferentes**. La Distribución Gamma se utiliza comúnmente en estadística para modelar tiempos de espera, procesos de conteo y variables aleatorias no negativas.

El script utiliza **SciPy** para la función estadística, **NumPy** para operaciones numéricas y **Pandas/Seaborn/Matplotlib** para estructurar y presentar los datos gráficamente.

***

### 1. Inicialización y Definición de Parámetros

| Código | Descripción |
| :--- | :--- |
| `from scipy.stats import gamma` | **Librería Estadística**: Importa la clase `gamma` de SciPy, que proporciona la función `pdf()` (equivalente a `dgamma()` en R). |
| `shape1 = 2`, `scale1 = 1` | **Parámetros Set 1**: Define el primer conjunto de parámetros: **forma** ($k=2$) y **escala** ($\theta=1$). |
| `shape2 = 5`, `scale2 = 1` | **Parámetros Set 2**: Define el segundo conjunto, manteniendo la escala ($\theta=1$) pero cambiando la forma ($k=5$). Esto permite visualizar cómo el parámetro de forma **modifica la silueta** de la distribución. |
| `x_values = np.arange(0, 20.1, 0.1)` | **Definición del Eje $x$**: Crea un rango de valores para la variable $x$ desde $0$ hasta $20$ con pasos de $0.1$. Se elige este rango para capturar una porción significativa de la probabilidad de ambas distribuciones. |

***

### 2. Cálculo de la Función de Densidad (PDF)

| Código | Parámetro `gamma.pdf` | Parámetro Estadístico | Significado |
| :--- | :--- | :--- | :--- |
| `a` | **`a`** | Forma ($k$ o $\alpha$) | Determina la **forma** de la curva; a mayor valor, más simétrica. |
| `scale` | **`scale`** | Escala ($\theta$ o $\beta^{-1}$) | Controla el **estiramiento** horizontal de la curva. |

| Código | Descripción |
| :--- | :--- |
| `gamma_density1 = gamma.pdf(x_values, a=shape1, scale=scale1)` | **Cálculo de la PDF (Set 1)**: Calcula los valores de densidad para la distribución $\text{Gamma}(k=2, \theta=1)$. |
| `gamma_density2 = gamma.pdf(x_values, a=shape2, scale=scale2)` | **Cálculo de la PDF (Set 2)**: Calcula los valores de densidad para la distribución $\text{Gamma}(k=5, \theta=1)$. |
| `data1 = pd.DataFrame(...)`, `data2 = pd.DataFrame(...)` | **Estructura de Datos**: Crea DataFrames individuales con las columnas $x$, $Density$ y una etiqueta combinada (`Distribution`) que identifica la distribución, como $\text{Gamma}(2, 1)$. |
| `data = pd.concat([data1, data2], ignore_index=True)` | **Combinación de Datos**: Une los dos DataFrames en uno solo. Este formato (*long format*) es ideal para que Seaborn mapee automáticamente el color y la leyenda a la variable `Distribution`. |

***

### 3. Visualización y Estilizado del Gráfico

| Código | Descripción |
| :--- | :--- |
| `plt.fill_between(...)` | **Sombreado de Área**: Dibuja un **área semitransparente** (`alpha=0.1`) bajo cada curva de densidad. Esto es un buen recurso visual, similar a `geom_area` o `geom_ribbon` en R, para resaltar la región de probabilidad. |
| `sns.lineplot(...)` | **Trazado de Líneas**: Dibuja las dos curvas principales. El parámetro `hue='Distribution'` indica a Seaborn que use la columna de etiquetas para asignar colores y generar la leyenda. |
| `plt.title(...)`, `plt.xlabel(...)`, `plt.ylabel(...)` | **Etiquetas y Títulos**: Establece el título principal y las etiquetas de los ejes. |
| `plt.legend(title="Distribución", ...)` | **Configuración de Leyenda**: Mueve la leyenda a la parte superior de la gráfica (`bbox_to_anchor`) y le asigna el título "Distribución". |

El gráfico resultante muestra dos curvas sesgadas a la derecha. La distribución $\text{Gamma}(5, 1)$ alcanza su pico en un valor mayor y es visualmente más simétrica que la distribución $\text{Gamma}(2, 1)$, que está más sesgada hacia el origen, ilustrando claramente el **efecto del parámetro de forma ($k$)** en la distribución Gamma.

### Distribución Beta

* **Descripción**: Modelo de variables aleatorias que se distribuyen en el intervalo $[0, 1]$. Es útil para modelar fenómenos aleatorios que están restringidos a ese intervalo.

* **Parámetros**:
  - $ \alpha $ (parámetro de forma)
  - $ \beta $ (parámetro de forma)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x) =
\begin{cases}
\frac{x^{\alpha - 1} (1 - x)^{\beta - 1}}{B(\alpha, \beta)} & \text{si } 0 < x < 1 \\
0 & \text{si } x \leq 0 \text{ o } x \geq 1
\end{cases}
$$
donde $ B(\alpha, \beta) $es **la función beta**.

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) = \int_0^x f(t) \, dt
$$

* **Valor Esperado**: $E[X] = \frac{\alpha}{\alpha + \beta} $

* **Media**: $ \mu_X = \frac{\alpha}{\alpha + \beta} $

* **Desviación Estándar**:
$$
\sigma = \sqrt{\frac{\alpha \beta}{(\alpha + \beta)^2 (\alpha + \beta + 1)}}
$$

* **Percentiles**: $ x_\alpha $ se obtiene usando la función inversa de la CDF.

**Comandos en R**:
```r
## PDF
dbeta(x, shape1 = alpha, shape2 = beta)

## CDF
pbeta(x, shape1 = alpha, shape2 = beta)

## Simulación
rbeta(n, shape1 = alpha, shape2 = beta)

#### Función Beta

La **función beta** es una función especial que se utiliza en diversas áreas de las matemáticas, especialmente en teoría de la probabilidad y estadística. Es fundamental en el cálculo de distribuciones de probabilidad, como la distribución beta y la distribución F.

##### Definición

La función beta se define como:

$$
B(x, y) = \int_0^1 t^{x-1} (1-t)^{y-1} \, dt
$$

donde:
- $ x > 0 $ y $ y > 0$ son parámetros que determinan la forma de la función beta. Representan "números de éxito" y "números de fracaso" en el contexto de probabilidades. En muchos casos, $x$ se interpreta como el número de éxitos en un experimento y $y$ como el número de fracasos.

#### Propiedades

1. **Relación con la función gamma**:
   La función beta está relacionada con la función gamma mediante la siguiente relación:

   $$
   B(x, y) = \frac{\Gamma(x) \Gamma(y)}{\Gamma(x+y)}
   $$

   donde \( \Gamma(n) \) es la función gamma, que generaliza el factorial para números no enteros.

2. **Simetría**:
   La función beta tiene la propiedad de ser simétrica, lo que significa que:

   $$
   B(x, y) = B(y, x)
   $$

3. **Valores específicos**:
   - $ B(1, 1) = 1 $
   - $ B\left(\frac{1}{2}, \frac{1}{2}\right) = \pi $

**Usos en Estadística**

- **Distribución Beta**: La función beta se utiliza para definir la función de densidad de probabilidad de la distribución beta:

  $$
  f(x) = \frac{1}{B(\alpha, \beta)} x^{\alpha - 1} (1 - x)^{\beta - 1} \quad \text{para } 0 < x < 1
  $$

- **Distribución F**: La función beta también se emplea en la definición de la distribución F.

**Ejemplo de Cálculo**

Para calcular $B(2, 3) $:

$$
B(2, 3) = \int_0^1 t^{2-1} (1-t)^{3-1} \, dt = \int_0^1 t^{1} (1-t)^{2} \, dt
$$

Resolviendo la integral:

$$
= \left[ \frac{t^2}{2} \cdot \frac{(1-t)^3}{3} \right]_0^1 = \frac{1}{2 \cdot 3} = \frac{1}{6}
$$

**Cálculo de la Función Beta en R**

La función beta se puede calcular en R utilizando la función `beta()`. Aquí te muestro cómo hacerlo:

```r
## Cálculo de la función beta
beta_value <- beta(x, y)

```python
"""
#Ejemplo en R
#Supongamos que deseas calcular 𝐵(2,3)

x <- 2
y <- 3

## Usando la función beta
beta_value <- beta(x, y)
print(beta_value)

## Usando la relación con la función gamma
beta_value_gamma <- gamma(x) * gamma(y) / gamma(x + y)
print(beta_value_gamma)
"""
```

#### Ejemplo de Gráfica de la Distribución Beta

La distribución beta es un modelo de probabilidad que describe variables aleatorias que se encuentran en el intervalo $[0, 1]$. Esta distribución es especialmente útil para modelar proporciones y probabilidades, ya que puede adoptar diferentes formas dependiendo de sus parámetros. Los parámetros de la distribución beta, $ \alpha $ y $ \beta $, determinan la forma de la función de densidad, permitiendo que la distribución sea simétrica, sesgada hacia la izquierda o hacia la derecha.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad $ PDF $ de la distribución beta para varios valores de $ \alpha $ y $ \beta $. A medida que se ajustan estos parámetros, la forma de la distribución varía, lo que refleja cómo las diferentes combinaciones de $ \alpha $ y $ \beta $ influyen en la concentración de probabilidad.

La distribución beta es particularmente valiosa en campos como la estadística bayesiana y la teoría de decisiones, donde se requiere modelar incertidumbres en intervalos restringidos.

```python
"""
## Cargar la librería necesaria
library(ggplot2)

## Crear un rango de valores para x
x_values <- seq(0, 1, by = 0.01)

## Definir los parámetros de la función beta
shape1 <- 2  # Parámetro x
shape2 <- 5  # Parámetro y

## Calcular la función beta
beta_density <- dbeta(x_values, shape1, shape2)

## Crear un data frame para ggplot
data <- data.frame(x = x_values, density = beta_density)

## Graficar la función beta
ggplot(data, aes(x = x, y = density)) +
  geom_line(color = "blue", linewidth = 1) +
  labs(title = "Gráfico de la Función Beta",
       x = "x",
       y = "Densidad") +
  theme_minimal() +
  scale_y_continuous(expand = expansion(mult = c(0, 0.1)))
"""
```

**Gráfico de la distribució beta**

```python
"""
## Cargar la librería necesaria
library(ggplot2)

## Crear un rango de valores para x
x_values <- seq(0, 1, by = 0.01)

## Definir los parámetros de la distribución beta
alpha1 <- 2  # Parámetro alpha
beta1 <- 5   # Parámetro beta

alpha2 <- 5  # Otro parámetro alpha
beta2 <- 2   # Otro parámetro beta

## Calcular la función de densidad de la distribución beta
beta_density1 <- dbeta(x_values, shape1 = alpha1, shape2 = beta1)
beta_density2 <- dbeta(x_values, shape1 = alpha2, shape2 = beta2)

## Crear un data frame para ggplot
data <- data.frame(x = x_values,
                   density1 = beta_density1,
                   density2 = beta_density2)

## Graficar la distribución beta
ggplot(data, aes(x = x)) +
  geom_line(aes(y = density1), color = "blue", linewidth = 1) +
  geom_line(aes(y = density2), color = "red", linewidth = 1) +
  labs(title = "Gráfico de la Distribución Beta",
       x = "x",
       y = "Densidad") +
  theme_minimal() +
  scale_y_continuous(expand = expansion(mult = c(0, 0.1))) +
  theme(legend.position = "top") +
  geom_area(aes(y = density1), fill = "blue", alpha = 0.1) +
  geom_area(aes(y = density2), fill = "red", alpha = 0.1)
"""
```

#### Descripción del Código

* **Cargar librerías**: Se utiliza `ggplot2 `para crear la gráfica.
* **Crear un rango de valores para $x$**: Se define un rango de valores de $ 0 $ a $ 1 $ para representar la distribución beta.
* **Definir los parámetros**: Se establecen los parámetros $ \alpha $ y $ \beta $ para las dos configuraciones de la distribución beta.
* **Calcular la PDF**: Se utiliza `dbeta()` para calcular la función de densidad de probabilidad para los valores de $ x $ con los parámetros definidos.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $ x$ y sus correspondientes probabilidades para las dos configuraciones de la distribución beta.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $ PDF $ de la distribución beta para los diferentes parámetros, incluyendo áreas sombreadas para visualizar mejor las densidades.

**EJERCICIO 13**

La **Distribución Beta** es una distribución de probabilidad continua definida sobre el intervalo $[0, 1]$. Es extremadamente versátil porque sus dos parámetros de forma, $\alpha$ y $\beta$, permiten modelar una gran variedad de formas, desde distribuciones uniformes hasta curvas con sesgo a la izquierda, a la derecha, o bimodales (en forma de "U"). Su principal utilidad es modelar la probabilidad de una probabilidad, proporciones, tasas o porcentajes.

A continuación, se detallan ejemplos y usos recomendados en Nanotecnología e Inteligencia Artificial.

***

## ⚛️ Nanotecnología y Ciencia de Materiales

En estos campos, la Distribución Beta es ideal para modelar la **variabilidad de proporciones y rendimientos** en procesos de síntesis y fabricación a escala nanométrica.

### 1. Modelado de Rendimiento de Síntesis (Yield)

| Escenario | Uso Recomendado | Concepto Clave |
| :--- | :--- | :--- |
| **Rendimiento de Producción** | Modelar el **porcentaje de nanopartículas** o nanocables funcionalizados con éxito en un lote químico, o el porcentaje de materiales que cumplen con una especificación crítica. | Los parámetros $\alpha$ y $\beta$ se ajustan a datos históricos del rendimiento de síntesis. Si $\alpha > \beta$, el rendimiento es alto (sesgado a 1); si $\alpha < \beta$, el rendimiento es bajo (sesgado a 0). |
| **Pureza de Materiales** | Estimar la **proporción de un contaminante** o la fracción de un material deseado en una mezcla purificada. | Permite cuantificar la incertidumbre en la pureza de un lote. Se usa a menudo para **pruebas de hipótesis Bayesianas** sobre si la pureza excede un umbral (por ejemplo, 99%). |

### 2. Eficiencia Cuántica y Absorción

| Escenario | Uso Recomendado | Concepto Clave |
| :--- | :--- | :--- |
| **Eficiencia de Celdas Solares** | Modelar la distribución de la **eficiencia cuántica** ($\eta$, un valor entre 0 y 1) de una serie de nanoceldas solares o fotodetectores fabricados con nanoestructuras. | La Log-Normal modela el tamaño de la nanopartícula; la Beta modela el rendimiento final o la eficiencia operativa. Es útil para **tolerancias de diseño** y predecir la variabilidad del producto final. |
| **Porosidad de Filtros Nanoporosos** | Estimar la **fracción de área efectiva de poro** en filtros de membrana o materiales porosos, crucial para aplicaciones de separación. | Permite tratar la porosidad como una **probabilidad de paso** en lugar de un valor fijo, incorporando la incertidumbre en la estructura del material. |

***

## 🤖 Inteligencia Artificial (IA) y Aprendizaje Automático

La Distribución Beta es la **conjugada a priori** de la Distribución Binomial, lo que la hace indispensable en la estadística Bayesiana y en el modelado de proporciones de éxito o tasas de error.

### 1. Inferencia Bayesiana y A/B Testing

| Escenario | Uso Recomendado | Concepto Clave |
| :--- | :--- | :--- |
| **Tasa de Conversión (A/B Testing)** | Modelar la distribución de probabilidad de la **tasa de éxito** (o tasa de clics/conversión) de dos algoritmos de IA o dos versiones de una interfaz (A y B). | Si se observa $k$ éxitos en $n$ ensayos (Binomial), la distribución *a posteriori* de la probabilidad de éxito $p$ es una Beta($\alpha_{\text{priori}} + k$, $\beta_{\text{priori}} + n - k$). Esto permite decidir qué versión es mejor con incertidumbre cuantificada. |
| **Clasificación Binaria** | En tareas de clasificación (p. ej., determinar si una imagen contiene un defecto o no), modelar la **incertidumbre sobre la verdadera tasa de precisión** del modelo. | Utiliza la Beta para representar nuestro conocimiento sobre la precisión real, actualizándolo con cada nuevo lote de datos evaluados. |

### 2. Asignación Dinámica de Recursos y *Bandit Problems*

| Escenario | Uso Recomendado | Concepto Clave |
| :--- | :--- | :--- |
| **Aprendizaje por Refuerzo (Bandidos)** | Se utiliza en el algoritmo **Thompson Sampling** para problemas de *multi-armed bandit* (como la optimización de *feeds* de noticias o anuncios). | La Beta se usa para modelar la **probabilidad de recompensa** de cada "brazo" (opción). En cada paso, el algoritmo muestrea una probabilidad de éxito de la distribución Beta de cada brazo y elige el que muestre el valor más alto, equilibrando automáticamente la exploración y la explotación.  |

### 3. Representación de Variables Normalizadas

| Escenario | Uso Recomendado | Concepto Clave |
| :--- | :--- | :--- |
| **Características Normalizadas** | Modelar la distribución de una característica de entrada de un modelo de IA después de haber sido **normalizada** al intervalo $[0, 1]$. | Si la característica normalizada está sesgada, la Beta es una opción más flexible que la Uniforme para representar la densidad de probabilidad de esos valores, lo que puede mejorar la precisión de modelos generativos o discriminativos basados en densidad. |

#### Codigo en phyton

```python
import numpy as np
from scipy.special import beta, gamma # Importamos las funciones Beta y Gamma

## 1. Definir los parámetros (equivalente a x <- 2, y <- 3 en R)
x = 2
y = 3

## ----------------------------------------------------
## 2. Usando la función beta (equivalente a beta_value <- beta(x, y))
## La función beta(a, b) calcula B(a, b)
beta_value = beta(x, y)

print(f"Resultado usando la función beta (B({x}, {y})):")
print(beta_value)

## ----------------------------------------------------
## 3. Usando la relación con la función gamma (equivalente a beta_value_gamma <- gamma(x) * gamma(y) / gamma(x + y))
## Relación: B(x, y) = [Gamma(x) * Gamma(y)] / Gamma(x + y)
beta_value_gamma = (gamma(x) * gamma(y)) / gamma(x + y)

print(f"\nResultado usando la relación con la función gamma:")
print(beta_value_gamma)

## ----------------------------------------------------
## Verificación (para B(2, 3))
## La integral de B(2, 3) es 1 / (2 + 3) * C(2 + 3 - 1, 2 - 1) = 1/5 * C(4, 1) = 1/5 * 4 = 4/5?
## Incorrecto. B(x, y) = (x-1)! * (y-1)! / (x+y-1)!
## B(2, 3) = (2-1)! * (3-1)! / (2+3-1)! = 1! * 2! / 4! = 1 * 2 / 24 = 2/24 = 1/12
print(f"\nVerificación matemática (1/12): {1/12}")
## Ambos resultados deberían ser 0.08333...
```

## Descripción del Código Python para el Cálculo de la Función Beta

El código en **Python** demuestra dos métodos para calcular el valor de la **Función Beta, $B(x, y)$**, para un par de argumentos dados ($x=2$ y $y=3$). El propósito principal es verificar la **relación fundamental** entre las funciones Beta y Gamma.

El script utiliza **NumPy** para operaciones básicas y la sublibrería **`scipy.special`** para acceder a las funciones $\Gamma(z)$ y $B(x, y)$ directamente.

***

### 1. Inicialización y Definición de Parámetros

| Código | Descripción |
| :--- | :--- |
| `from scipy.special import beta, gamma` | **Librerías Funcionales**: Importa directamente las funciones $\Gamma(z)$ (`gamma`) y $B(x, y)$ (`beta`) de SciPy. |
| `x = 2`, `y = 3` | **Parámetros**: Define los valores para los argumentos de la función, $x$ y $y$. En este caso, $x=2$ y $y=3$. |

***

### 2. Cálculo Directo con la Función Beta

| Código | Descripción |
| :--- | :--- |
| `beta_value = beta(x, y)` | **Cálculo Directo**: Llama a la función $\mathbf{beta(x, y)}$ de SciPy para obtener el valor de $B(2, 3)$. |
| `print(f"Resultado...: {beta_value}")` | **Resultado**: Muestra el valor numérico calculado directamente. |

***

### 3. Cálculo Usando la Relación con la Función Gamma

| Código | Fórmula | Descripción |
| :--- | :--- | :--- |
| `beta_value_gamma = ...` | $B(x, y) = \frac{\Gamma(x) \Gamma(y)}{\Gamma(x+y)}$ | **Cálculo Indirecto**: Aplica la relación fundamental que conecta la Función Beta con la Función Gamma. Se calcula $\Gamma(2)$, $\Gamma(3)$ y $\Gamma(2+3) = \Gamma(5)$, y se realiza la división. |
| `print(f"\nResultado...: {beta_value_gamma}")` | **Resultado**: Muestra el valor numérico obtenido a través de la relación con $\Gamma(z)$. |

***

### 4. Verificación Matemática

| Código | Cálculo Factorial | Explicación |
| :--- | :--- | :--- |
| `# B(2, 3) = 1! * 2! / 4! = 2/24 = 1/12` | $\mathbf{B(x, y) = \frac{(x-1)!(y-1)!}{(x+y-1)!}}$ | Dado que $x$ y $y$ son enteros positivos, la Función Beta se relaciona con los factoriales. El código verifica que $B(2, 3) = 1/12$, lo cual es aproximadamente $0.08333...$ |

**Conclusión:** Ambos métodos de cálculo (directo con $B(x, y)$ e indirecto con $\Gamma(x)$) producen el mismo resultado, verificando la identidad matemática.

#### Codigo en phyton

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import beta # Importamos la función de distribución Beta

## ----------------------------------------------------
## 1. Crear un rango de valores para x
## Similar a seq(0, 1, by = 0.01) en R
x_values = np.arange(0, 1.01, 0.01) # Aseguramos incluir el 1

## 2. Definir los parámetros de la distribución beta
shape1 = 2  # Parámetro alpha (equivalente a 'shape1' o 'a' en R)
shape2 = 5  # Parámetro beta (equivalente a 'shape2' o 'b' en R)

## 3. Calcular la función de densidad de la distribución beta
## En SciPy, beta.pdf(x, a, b) es el equivalente a dbeta(x, shape1, shape2) en R
beta_density = beta.pdf(x_values, a=shape1, b=shape2)

## 4. Crear un data frame para los datos (opcional, pero útil para seaborn)
data = pd.DataFrame({'x': x_values, 'density': beta_density})

## 5. Graficar la función beta
sns.set_theme(style="whitegrid") # Similar a theme_minimal()

plt.figure(figsize=(8, 6))

## Usar seaborn.lineplot para graficar (similar a ggplot + geom_line)
sns.lineplot(
    data=data,
    x='x',
    y='density',
    color='blue',
    linewidth=2 # Corresponde a 'linewidth=1' en R para visibilidad
)

## Añadir etiquetas y título (equivalente a labs)
plt.title("Gráfico de la Distribución Beta", fontsize=16)
plt.xlabel("x", fontsize=12)
plt.ylabel("Densidad", fontsize=12)

## Ajustar el eje y (equivalente a scale_y_continuous(expand = ...))
plt.ylim(bottom=0) # Asegura que el eje Y comience en 0

## Mostrar la gráfica
plt.show()
```

## Descripción del Código Python para la Gráfica de la Distribución Beta

El código en **Python** tiene como finalidad calcular y visualizar la **Función de Densidad de Probabilidad (PDF)** de una **Distribución Beta** específica. La Distribución Beta es fundamental en la inferencia Bayesiana, ya que modela probabilidades o proporciones, y solo está definida en el intervalo $[0, 1]$.

El script utiliza **SciPy** para la función estadística, **NumPy** para operaciones numéricas y **Pandas/Seaborn/Matplotlib** para la estructuración y presentación de los datos.

***

### 1. Inicialización y Definición de Parámetros

| Código | Descripción |
| :--- | :--- |
| `from scipy.stats import beta` | **Librería Estadística**: Importa la clase `beta` de SciPy, que proporciona la función `pdf()` (equivalente a `dbeta()` en R). |
| `x_values = np.arange(0, 1.01, 0.01)` | **Definición del Eje $x$**: Crea un rango de valores para la variable $x$ desde $0$ hasta $1$ con incrementos de $0.01$. Este rango es el dominio natural de la distribución Beta. |
| `shape1 = 2` (`a`) | **Parámetro $\alpha$ (Forma 1)**: Define el primer parámetro de forma, que influye en la forma de la curva cerca de $x=0$. |
| `shape2 = 5` (`b`) | **Parámetro $\beta$ (Forma 2)**: Define el segundo parámetro de forma, que influye en la forma de la curva cerca de $x=1$. |

***

### 2. Cálculo de la Función de Densidad (PDF)

| Código | Parámetro `beta.pdf` | Parámetro Estadístico | Significado |
| :--- | :--- | :--- | :--- |
| `a` | **`a`** | $\alpha$ | Controla el peso de la distribución cerca de 0. |
| `b` | **`b`** | $\beta$ | Controla el peso de la distribución cerca de 1. |

| Código | Descripción |
| :--- | :--- |
| `beta_density = beta.pdf(x_values, a=shape1, b=shape2)` | **Cálculo de la PDF**: Llama a la función $\mathbf{beta.pdf()}$ de SciPy. La función calcula la densidad de probabilidad para la distribución $\text{Beta}(\alpha=2, \beta=5)$ en todos los puntos de $x$. |
| `data = pd.DataFrame(...)` | **Estructura de Datos**: Combina los valores de $x$ y sus densidades correspondientes en un DataFrame llamado `data`, facilitando su uso en Seaborn. |

***

### 3. Visualización del Gráfico

| Código | Descripción |
| :--- | :--- |
| `sns.set_theme(style="whitegrid")` | **Estilo de Gráfico**: Configura un estilo limpio de cuadrícula blanca de Seaborn. |
| `sns.lineplot(...)` | **Trazado de la Línea**: Dibuja la curva de densidad. Se utiliza **`lineplot`** para representar la relación continua entre $x$ y $density$. |
| | - `color='blue', linewidth=2` : Define el estilo visual de la línea. |
| `plt.title(...)`, `plt.xlabel(...)`, `plt.ylabel(...)` | **Etiquetas y Títulos**: Establece el título principal y las etiquetas de los ejes. |
| `plt.ylim(bottom=0)` | **Ajuste del Eje Y**: Asegura que el eje de densidad comience estrictamente en cero, lo que es apropiado para una función de densidad de probabilidad. |
| `plt.show()` | **Renderizado Final**: Muestra el gráfico. |

El gráfico resultante muestra una curva unimodal (con un solo pico) que está **sesgada hacia la izquierda**, ya que el parámetro $\beta=5$ es significativamente mayor que $\alpha=2$. Esto indica que la mayor concentración de probabilidad se encuentra en valores bajos de $x$ (más cerca de 0).

#### Codigo en phyton

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import beta # Importamos la función de distribución Beta

## ----------------------------------------------------
## 1. Crear un rango de valores para x
## Similar a seq(0, 1, by = 0.01) en R
x_values = np.arange(0, 1.01, 0.01) # Aseguramos incluir el 1

## 2. Definir los parámetros de la distribución beta
alpha1 = 2  # Parámetro a (shape1)
beta1 = 5   # Parámetro b (shape2)

alpha2 = 5  # Otro parámetro a
beta2 = 2   # Otro parámetro b

## 3. Calcular la función de densidad de la distribución beta
## En SciPy, beta.pdf(x, a, b) es el equivalente a dbeta(x, shape1, shape2) en R
beta_density1 = beta.pdf(x_values, a=alpha1, b=beta1)
beta_density2 = beta.pdf(x_values, a=alpha2, b=beta2)

## 4. Crear un data frame combinado y etiquetar las distribuciones
data1 = pd.DataFrame({
    'x': x_values,
    'Density': beta_density1,
    'Distribution': f'Beta({alpha1}, {beta1})' # Etiqueta para la leyenda
})
data2 = pd.DataFrame({
    'x': x_values,
    'Density': beta_density2,
    'Distribution': f'Beta({alpha2}, {beta2})' # Etiqueta para la leyenda
})

data = pd.concat([data1, data2], ignore_index=True)

## 5. Graficar la distribución beta usando Matplotlib y Seaborn
sns.set_theme(style="whitegrid") # Similar a theme_minimal()
plt.figure(figsize=(10, 6))

## Definir colores manualmente
colors = {
    f'Beta({alpha1}, {beta1})': 'blue',
    f'Beta({alpha2}, {beta2})': 'red'
}

## 5a. Dibujar áreas sombreadas (equivalente a geom_area)
plt.fill_between(data1['x'], data1['Density'], color='blue', alpha=0.1)
plt.fill_between(data2['x'], data2['Density'], color='red', alpha=0.1)

## 5b. Dibujar las líneas (equivalente a geom_line)
sns.lineplot(
    data=data,
    x='x',
    y='Density',
    hue='Distribution', # Usa la columna 'Distribution' para el color y la leyenda
    palette=colors,
    linewidth=2
)

## 5c. Añadir etiquetas y título (equivalente a labs)
plt.title("Gráfico de la Distribución Beta", fontsize=16)
plt.xlabel("x", fontsize=12)
plt.ylabel("Densidad", fontsize=12)

## Configurar el eje y (equivalente a scale_y_continuous(expand = ...))
plt.ylim(bottom=0)

## Configurar la leyenda y su posición (equivalente a theme(legend.position = "top"))
plt.legend(title="Distribución", loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=2)

## Mostrar la gráfica
plt.show()
```

## Descripción del Código Python para la Gráfica de la Distribución Beta (Comparativa)

El código en **Python** tiene el propósito de calcular y visualizar la **Función de Densidad de Probabilidad (PDF)** de **dos distribuciones Beta diferentes** para mostrar cómo la **simetría de los parámetros** ($\alpha$ y $\beta$) afecta la forma de la curva.

Al igual que en ejemplos anteriores, el script utiliza **SciPy** para la función estadística, **NumPy** para operaciones numéricas, y **Pandas/Seaborn/Matplotlib** para la estructuración y presentación visual de los datos.

***

### 1. Inicialización y Definición de Parámetros

| Código | Descripción |
| :--- | :--- |
| `from scipy.stats import beta` | **Librería Estadística**: Importa la clase `beta` de SciPy, fundamental para calcular la densidad. |
| `x_values = np.arange(0, 1.01, 0.01)` | **Definición del Eje $x$**: Crea un rango de valores de $0$ a $1$ con pasos de $0.01$, el dominio de la Distribución Beta. |
| `alpha1 = 2`, `beta1 = 5` | **Parámetros Set 1 ($\text{Beta}(2, 5)$)**: Distribución sesgada a la **izquierda** (hacia $x=0$) porque $\alpha < \beta$. |
| `alpha2 = 5`, `beta2 = 2` | **Parámetros Set 2 ($\text{Beta}(5, 2)$)**: Distribución sesgada a la **derecha** (hacia $x=1$) porque $\alpha > \beta$. |

***

### 2. Cálculo de la Función de Densidad (PDF)

| Código | Descripción |
| :--- | :--- |
| `beta_density1 = beta.pdf(x_values, a=alpha1, b=beta1)` | **Cálculo de la PDF (Set 1)**: Calcula la densidad para $\text{Beta}(2, 5)$. |
| `beta_density2 = beta.pdf(x_values, a=alpha2, b=beta2)` | **Cálculo de la PDF (Set 2)**: Calcula la densidad para $\text{Beta}(5, 2)$. |
| `data = pd.concat([data1, data2], ignore_index=True)` | **Estructura de Datos**: Combina los datos de ambas distribuciones en un único DataFrame en formato *long*, utilizando la columna `Distribution` como etiqueta única (por ejemplo, "Beta(2, 5)"). |

***

### 3. Visualización y Estilizado del Gráfico

| Código | Descripción |
| :--- | :--- |
| `plt.fill_between(...)` | **Sombreado de Área**: Dibuja un **área semitransparente** bajo cada curva (azul y rojo) para mejorar el impacto visual del área total bajo la densidad. |
| `sns.lineplot(...)` | **Trazado de Líneas**: Dibuja ambas curvas de densidad. El parámetro `hue='Distribution'` permite a Seaborn asignar el color y generar la leyenda automáticamente basándose en las etiquetas de la columna. |
| `plt.title(...)`, `plt.xlabel(...)`, `plt.ylabel(...)` | **Etiquetas y Títulos**: Establece el título principal y las etiquetas de los ejes. |
| `plt.ylim(bottom=0)` | **Ajuste del Eje Y**: Asegura que el eje de densidad comience en cero. |
| `plt.legend(...)` | **Configuración de Leyenda**: Coloca la leyenda en la parte superior central de la gráfica. |

El gráfico resultante muestra dos curvas de campana **invertidas** entre sí:
1.  La curva $\text{Beta}(2, 5)$ (azul) alcanza su pico cerca de $x=0$, mostrando un fuerte **sesgo a la izquierda**.
2.  La curva $\text{Beta}(5, 2)$ (roja) alcanza su pico cerca de $x=1$, mostrando un fuerte **sesgo a la derecha**.

Esta visualización demuestra cómo la Distribución Beta puede modelar una amplia variedad de formas en el intervalo $[0, 1]$, dependiendo de la relación entre sus parámetros $\alpha$ y $\beta$.

### Distribución Weibull

* **Descripción**: Modelo utilizado para analizar el tiempo hasta el fallo de un sistema o un componente. Es especialmente útil en el análisis de fiabilidad y en estudios de vida.

* **Parámetros**:
  - \( \lambda \) (escala)
  - \( k \) (forma)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x) =
\begin{cases}
\frac{k}{\lambda} \left( \frac{x}{\lambda} \right)^{k-1} e^{-\left( \frac{x}{\lambda} \right)^k} & \text{si } x \geq 0 \\
0 & \text{si } x < 0
\end{cases}
$$

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) =
\begin{cases}
1 - e^{-\left( \frac{x}{\lambda} \right)^k} & \text{si } x \geq 0 \\
0 & \text{si } x < 0
\end{cases}
$$

* **Valor Esperado**:
$$
E[X] = \lambda \Gamma\left(1 + \frac{1}{k}\right)
$$

* **Media**:
$$
\mu_X = \lambda \Gamma\left(1 + \frac{1}{k}\right)
$$

* **Desviación Estándar**:
$$
\sigma = \lambda \sqrt{\Gamma\left(1 + \frac{2}{k}\right) - \left(\Gamma\left(1 + \frac{1}{k}\right)\right)^2}
$$

* **Percentiles**: \( x_\alpha = \lambda \left( -\log(1 - \alpha) \right)^{\frac{1}{k}} \)

**Comandos en R**:
```r
## PDF
dweibull(x, shape = k, scale = lambda)

## CDF
pweibull(x, shape = k, scale = lambda)

## Simulación
rweibull(n, shape = k, scale = lambda)

#### Ejemplo de Gráfica de la Distribución Weibull

La distribución Weibull es un modelo de probabilidad utilizado para describir el tiempo hasta un evento, como el tiempo de vida de un producto o el tiempo hasta el fallo de un sistema. Es especialmente útil en análisis de confiabilidad y en la modelación de datos de supervivencia. La distribución se define por dos parámetros: la forma $ k $ y la escala $ \lambda $.

El parámetro de forma $ k $ determina la naturaleza de la distribución:
- Si $ k < 1 $, la distribución tiene una alta tasa de fallo inicial, lo que indica que los fallos son más comunes al principio.
- Si $ k = 1 $, la distribución se convierte en una distribución exponencial, indicando una tasa de fallo constante.
- Si $ k > 1 $, la tasa de fallo aumenta con el tiempo, lo que sugiere un desgaste.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad (PDF) de la distribución Weibull para varios valores de $ k $ y $ \lambda $. A medida que se ajustan estos parámetros, la forma de la distribución varía, reflejando cómo diferentes combinaciones de $ k $ y $ \lambda $ influyen en la concentración de probabilidad y en la forma de la curva.

La distribución Weibull es valiosa en diversas áreas, como la ingeniería y la economía, donde se requiere modelar la vida útil de productos o la duración de ciertos procesos.

```python
"""
## Cargar la librería necesaria
library(ggplot2)

## Definir los parámetros de la distribución Weibull
k_values <- c(0.5, 1, 2)  # Parámetro de forma
lambda_values <- c(1, 1, 1)  # Parámetro de escala

## Crear un rango de valores para x
x <- seq(0, 3, length.out = 100)

## Crear un data frame vacío para almacenar los resultados
data <- data.frame()

## Calcular la PDF para cada combinación de k y lambda
for (i in 1:length(k_values)) {
  k <- k_values[i]
  lambda <- lambda_values[i]
  pdf_values <- dweibull(x, shape = k, scale = lambda)

## Añadir los resultados al data frame
  data <- rbind(data, data.frame(x = x, pdf = pdf_values, k = factor(k), lambda = lambda))
}

## Graficar las distribuciones
ggplot(data, aes(x = x, y = pdf, color = k)) +
  geom_line() +
  labs(title = "Funciones de Densidad de la Distribución Weibull",
       x = "x",
       y = "Densidad de Probabilidad (PDF)",
       color = "Parámetro k") +
  theme_minimal()
"""
```

#### Descripción del Código

* **Cargar librerías**: Se utiliza `ggplot2` para crear la gráfica.
* **Crear un rango de valores para $x$**: Se define un rango de valores de $ 0 $ a $ 3 $ para representar la distribución Weibull.
* **Definir los parámetros**: Se establecen los parámetros $ k $ y $ \lambda $ para tres configuraciones diferentes de la distribución Weibull.
* **Calcular la PDF**: Se utiliza `dweibull()` para calcular la función de densidad de probabilidad para los valores de $ x $ con los parámetros definidos.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $ x $ y sus correspondientes probabilidades para las configuraciones de la distribución Weibull.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $ PDF $ de la distribución Weibull para los diferentes parámetros, permitiendo observar cómo varía la forma de la distribución.

**EJERCICIO 14**

La **Distribución de Weibull** es la herramienta estadística más crucial en **Ciencia de Materiales** y **Fiabilidad (Confiabilidad)**, especialmente cuando se modela el **tiempo hasta el fallo** o la **resistencia a la fractura** de los materiales. Su gran ventaja es el parámetro de forma ($k$ o $\beta$), que permite modelar diferentes tipos de mecanismos de fallo.

## 🔬 Usos en la Resistencia a la Fractura

La Weibull es el modelo estándar para la resistencia mecánica de los **materiales frágiles** (cerámicas, vidrio, compuestos y fibras).

* **Fundamento:** La falla de un material frágil es gobernada por la presencia de un **defecto crítico** (grieta, poro o inclusión) dentro del volumen sometido a tensión (la "teoría del eslabón más débil"). La resistencia del material es una variable aleatoria que depende del tamaño y la distribución de estos defectos.
* **Ejemplo:** Medir la resistencia a la flexión de barras de **cerámica** ($\text{SiC}, \text{Al}_2\text{O}_3$) o la resistencia a la tracción de **fibras de carbono**.
* **Usos Recomendados:**
    * **Determinación del Módulo de Weibull ($k$):** Este parámetro es crucial. Cuanto mayor sea el valor de $k$, **menor es la dispersión** en la resistencia del material. Un $k$ alto (p. ej., $k>10$) indica un material de alta calidad con defectos muy uniformes, mientras que un $k$ bajo indica alta variabilidad y riesgo.
    * **Escalamiento de Volumen (Size Effect):** La distribución Weibull permite predecir cómo cambia la resistencia promedio de un material cuando se cambia el **volumen** o el **área** sometida a tensión. Es decir, predecir que un componente más grande será estadísticamente más débil que uno pequeño, ya que tiene mayor probabilidad de contener un defecto crítico.

***

## ⚙️ Usos en Fiabilidad y Vida Útil

En ingeniería, la Weibull se utiliza para modelar el **tiempo de vida** de los componentes, ya que puede describir las tres fases de la **curva de la bañera**.

| Mecanismo de Fallo (Parámetro $k$ o $\beta$) | Implicación en el Material | Ejemplo Típico |
| :--- | :--- | :--- |
| **$k < 1$ (Tasa de fallo decreciente)** | **Fallos Iniciales o "Mortalidad Infantil"**. Causados por defectos intrínsecos de fabricación o procesamiento. | Fallos en la primera hora de uso de un **componente electrónico o nano-dispositivo** debido a imperfecciones en el *chip* o capa delgada. |
| **$k = 1$ (Tasa de fallo constante)** | **Fallos Aleatorios** (Comportamiento Exponencial). El fallo no depende de la edad del material. | Fallos por sobrecarga inesperada o eventos externos que actúan sobre un material con **propiedades nanoestructurales estables**. |
| **$k > 1$ (Tasa de fallo creciente)** | **Desgaste o Envejecimiento**. Fallo debido a la acumulación de daño, corrosión o fatiga. | **Degradación de recubrimientos protectores**, crecimiento de grietas por **fatiga en metales** o envejecimiento de **polímeros**. |

### Usos Recomendados

* **Predicción de la Vida a Fatiga:** Modelar la relación entre el **número de ciclos** (tiempo) y la probabilidad de fallo de materiales sometidos a tensión cíclica. Es esencial en el diseño aeronáutico y automotriz.
* **Cualificación de Materiales:** Comparar la durabilidad de nuevos **materiales compuestos o aleaciones** bajo condiciones extremas. Un mejor material tendrá una vida característica ($\eta$, el parámetro de escala) mayor para el mismo valor de forma ($k$).
* **Modelado de la Corrosión:** Si la corrosión lleva al fallo mecánico, la distribución Weibull modela el **tiempo hasta que el espesor residual** (no corroído) es insuficiente.

En resumen, la Distribución de Weibull es indispensable para cuantificar la **incertidumbre** y la **variabilidad** de las propiedades críticas de los materiales, permitiendo a los ingenieros y científicos tomar decisiones robustas sobre diseño, seguridad y mantenimiento.

#### Codigo en phyton

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import weibull_min # Importamos la distribución Weibull

## ----------------------------------------------------
## 1. Definir los parámetros de la distribución Weibull
k_values = [0.5, 1, 2]       # Parámetro de forma (c en SciPy)
lambda_values = [1, 1, 1]    # Parámetro de escala (scale en SciPy)

## 2. Crear un rango de valores para x
## Similar a seq(0, 3, length.out = 100) en R
x = np.linspace(0, 3, 100)

## 3. Crear una lista para almacenar los DataFrames de los resultados
data_list = []

## 4. Calcular la PDF para cada combinación de k y lambda
for k, lambda_val in zip(k_values, lambda_values):
## En SciPy, weibull_min.pdf(x, c, scale) es el equivalente a dweibull(x, shape=c, scale=lambda) en R
## c es la forma (k) y scale es la escala (lambda)
    pdf_values = weibull_min.pdf(x, c=k, scale=lambda_val)

## Crear un DataFrame temporal
    df_temp = pd.DataFrame({
        'x': x,
        'pdf': pdf_values,
## Convertir k a string para usarlo como categoría discreta en la gráfica (color)
        'k': str(k),
        'lambda': lambda_val
    })
    data_list.append(df_temp)

## 5. Concatenar todos los DataFrames
data = pd.concat(data_list, ignore_index=True)

## 6. Graficar la distribución Weibull usando Seaborn
sns.set_theme(style="whitegrid") # Similar a theme_minimal()

plt.figure(figsize=(10, 6))

## Usar seaborn.lineplot
sns.lineplot(
    data=data,
    x='x',
    y='pdf',
    hue='k', # Usar el parámetro k para diferenciar el color
    palette='viridis', # Un buen esquema de colores
    linewidth=2
)

## Añadir etiquetas y título (equivalente a labs)
plt.title("Funciones de Densidad de la Distribución Weibull", fontsize=16)
plt.xlabel("x", fontsize=12)
plt.ylabel("Densidad de Probabilidad (PDF)", fontsize=12)

## Configurar la leyenda
plt.legend(title="Parámetro k", loc='upper right')

## Mostrar la gráfica
plt.show()
```

## Descripción del Código Python para la Gráfica de la Distribución Weibull

El código en **Python** calcula y visualiza la **Función de Densidad de Probabilidad (PDF)** de la **Distribución Weibull** para **diferentes valores del parámetro de forma ($k$)**, manteniendo el parámetro de escala ($\lambda$) constante. La Distribución Weibull es muy utilizada en ingeniería de confiabilidad y análisis de fallas para modelar la vida útil de componentes.

El script emplea **SciPy** para la función estadística, **NumPy** para operaciones numéricas, y **Pandas/Seaborn/Matplotlib** para la estructuración y presentación visual de los datos.

***

### 1. Inicialización y Definición de Parámetros

| Código | Descripción |
| :--- | :--- |
| `from scipy.stats import weibull_min` | **Librería Estadística**: Importa la clase `weibull_min` de SciPy. Esta es la implementación estándar para la distribución Weibull de dos parámetros. |
| `k_values = [0.5, 1, 2]` | **Parámetro de Forma ($k$)**: Define los tres valores del parámetro de forma a comparar. Este valor afecta la pendiente y la concavidad de la PDF. |
| `lambda_values = [1, 1, 1]` | **Parámetro de Escala ($\lambda$)**: Define el parámetro de escala, que se mantiene constante en $1$ para el análisis. |
| `x = np.linspace(0, 3, 100)` | **Definición del Eje $x$**: Crea $100$ puntos espaciados uniformemente desde $0$ hasta $3$. La Distribución Weibull solo se define para $x \ge 0$. |

***

### 2. Cálculo de la Función de Densidad (PDF)

| Parámetro SciPy | Parámetro Estadístico | Explicación |
| :--- | :--- | :--- |
| **`c`** | Forma ($k$) | Determina la **forma** de la curva. Si $k=1$, es una Distribución Exponencial. |
| **`scale`** | Escala ($\lambda$) | Es un factor de **estiramiento** a lo largo del eje $x$. |

| Código | Descripción |
| :--- | :--- |
| `for k, lambda_val in zip(...): ...` | **Bucle de Cálculo**: Itera a través de las combinaciones de $k$ y $\lambda$. |
| `pdf_values = weibull_min.pdf(x, c=k, scale=lambda_val)` | **Cálculo de la PDF**: Utiliza la función `weibull_min.pdf()`. Mapea la forma $k$ al parámetro `c` y la escala $\lambda$ al parámetro `scale`. |
| `data = pd.concat(data_list, ignore_index=True)` | **Estructura de Datos Final**: Combina todos los resultados en un único DataFrame en formato *long*, utilizando la columna `k` (como *string*) para etiquetar las distintas curvas en la gráfica. |

***

### 3. Visualización y Estilizado del Gráfico

| Código | Descripción |
| :--- | :--- |
| `sns.set_theme(style="whitegrid")` | **Estilo de Gráfico**: Configura un estilo limpio de cuadrícula blanca de Seaborn. |
| `sns.lineplot(...)` | **Trazado de Múltiples Líneas**: Dibuja las tres curvas de densidad. El parámetro `hue='k'` indica a Seaborn que use el valor de $k$ para asignar el color y generar la leyenda. |
| `palette='viridis'` | **Esquema de Color**: Usa una paleta de colores continua y visualmente agradable para distinguir los valores de $k$. |
| `plt.title(...)`, `plt.xlabel(...)`, `plt.ylabel(...)` | **Etiquetas y Títulos**: Define el título principal y las etiquetas de los ejes. |
| `plt.legend(title="Parámetro k", ...)` | **Configuración de Leyenda**: Coloca la leyenda en la esquina superior derecha. |

El gráfico resultante muestra tres curvas con formas distintas, ilustrando el impacto de $k$:
* **$k=0.5$ (Azul):** La densidad es alta cerca de $x=0$ y decae rápidamente (típica de alta tasa de fallas iniciales).
* **$k=1$ (Verde):** La curva es una línea decreciente (coincide con la **Distribución Exponencial**).
* **$k=2$ (Amarillo):** La curva es unimodal y se asemeja a una forma sesgada, con su pico alejado de cero.

### Distribución de Dirichlet

* **Descripción**: Modelo de distribuciones de probabilidad sobre un conjunto de variables aleatorias que suman uno. Se utiliza comúnmente en la teoría bayesiana y en el análisis de composiciones.

* **Parámetros**:
$\alpha_1, \alpha_2, \ldots, \alpha_k $ (parámetros de forma, donde $k $ es el número de variables)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x_1, x_2, \ldots, x_k) =
\begin{cases}
\frac{1}{B(\alpha)} \prod_{i=1}^{k} x_i^{\alpha_i - 1} & \text{si } x_i \geq 0 \text{ y } \sum_{i=1}^{k} x_i = 1 \\
0 & \text{en otro caso}
\end{cases}
$$
donde $ B(\alpha)$ es la función beta multivariada:

$$
B(\alpha) = \frac{\prod_{i=1}^{k} \Gamma(\alpha_i)}{\Gamma\left(\sum_{i=1}^{k} \alpha_i\right)}
$$

* **Valor Esperado**:
$$
E[X_i] = \frac{\alpha_i}{\sum_{j=1}^{k} \alpha_j}
$$

* **Media**:
$$
\mu_{X_i} = \frac{\alpha_i}{\sum_{j=1}^{k} \alpha_j}
$$

* **Desviación Estándar**:
$$
\text{Var}(X_i) = \frac{\alpha_i (\sum_{j=1}^{k} \alpha_j - \alpha_i)}{\left(\sum_{j=1}^{k} \alpha_j\right)^2 \left(\sum_{j=1}^{k} \alpha_j + 1\right)}
$$

* **Comandos en R**:

```r
## PDF
ddirichlet(x, alpha)

## CDF
pdirichlet(x, alpha)

## Simulación
rdirichlet(n, alpha)

#### Ejemplo de Gráfica de la Distribución de Dirichlet

La distribución de Dirichlet es una distribución de probabilidad multivariada que se utiliza para modelar vectores de proporciones que suman 1. Se define mediante un vector de parámetros $\boldsymbol{\alpha} = (\alpha_1, \alpha_2, \ldots, \alpha_k)$, donde $k$ es el número de variables aleatorias. Esta distribución es especialmente útil en estadística bayesiana y en la teoría de juegos.

La forma de la distribución de Dirichlet se determina por los valores de los parámetros $\alpha_i$:
- Si todos los $\alpha_i$ son iguales, la distribución es simétrica.
- Si los $\alpha_i$ son diferentes, la distribución puede ser sesgada hacia alguna de las proporciones.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad (PDF) de la distribución de Dirichlet para varios conjuntos de valores de $\boldsymbol{\alpha}$. A medida que se ajustan estos parámetros, la forma de la distribución varía, lo que refleja cómo las diferentes combinaciones de $\boldsymbol{\alpha}$ influyen en la concentración de probabilidad.

La distribución de Dirichlet es valiosa en campos como el aprendizaje automático, la inferencia estadística y la teoría de mezclas.

```python
"""
## Cargar las librerías necesarias
library(ggplot2)
library(dplyr)
library(MCMCpack)  # Asegúrate de que MCMCpack esté instalado

## Definir los parámetros de la distribución Dirichlet
alpha_values <- list(c(1, 1, 1), c(2, 5, 3), c(5, 1, 1))  # Diferentes vectores de parámetros

## Inicializar una lista para almacenar los gráficos
plots <- list()

## Generar muestras para cada conjunto de parámetros
for (alpha in alpha_values) {
## Generar muestras aleatorias de la distribución Dirichlet
  n_points <- 1000  # Número de muestras
  samples <- rdirichlet(n_points, alpha)

## Convertir las muestras en un data frame
  sample_data <- as.data.frame(samples)
  colnames(sample_data) <- c("x1", "x2", "x3")  # Nombrar columnas

## Graficar para cada conjunto de parámetros
  p <- ggplot(sample_data, aes(x = x1, y = x2)) +
    geom_point(alpha = 0.5) +
    labs(title = paste("Distribución Dirichlet (α = (", paste(alpha, collapse = ", "), "))", sep = ""),
         x = "$x_1$",
         y = "$x_2$") +
    theme_minimal() +
    xlim(0, 1) + ylim(0, 1)  # Limitar ejes a [0,1]

## Almacenar el gráfico en la lista
  plots[[length(plots) + 1]] <- p
}

## Mostrar los gráficos
for (plot in plots) {
  print(plot)
}
"""
```

#### Interpretación de los Resultados

1. **Ejes del Gráfico**:
   - El eje X representa la proporción de la primera variable ($x_1$).
   - El eje Y representa la proporción de la segunda variable ($x_2$).
   - La tercera variable ($x_3$) se infiere como $1 - x_1 - x_2$, lo que significa que la suma de las tres proporciones siempre es igual a 1.

2. **Forma de la Distribución**:
   - **Distribuciones Simétricas**: Cuando se utilizan valores de $\alpha$ iguales (como en el caso de $\alpha = (1, 1, 1)$), los puntos se distribuyen de manera uniforme dentro del triángulo delimitado por los ejes, mostrando una forma simétrica. Esto indica que todas las proporciones tienen la misma probabilidad de ocurrir.
   - **Distribuciones Asimétricas**: En contraste, cuando los valores de $\alpha$ son diferentes (por ejemplo, $\alpha = (2, 5, 3)$), los puntos tienden a agruparse más cerca de ciertos vértices del triángulo. Esto muestra que algunas proporciones son más probables que otras, reflejando la asimetría de la distribución.

3. **Concentración de Puntos**:
   - La densidad de los puntos en ciertas áreas del gráfico indica dónde es más probable encontrar combinaciones de proporciones. Por ejemplo, si hay un área donde hay muchos puntos, eso sugiere que las combinaciones de proporciones que corresponden a esos puntos son más comunes.
   - Si se observan áreas vacías, significa que esas combinaciones de proporciones son menos probables.

4. **Variabilidad**:
   - Las muestras generadas reflejan la variabilidad de las proporciones que se pueden obtener para un conjunto dado de parámetros $\alpha$. Por ejemplo, para valores de $\alpha$ muy diferentes entre sí, la variabilidad en las proporciones puede ser mayor, mientras que para valores más homogéneos, la variabilidad es menor.

### Resumen
Los diagramas de dispersión te permiten visualizar cómo la distribución Dirichlet modela combinaciones de proporciones en un contexto donde estas deben sumar 1. A medida que cambian los parámetros $\alpha$, la forma y la concentración de las muestras cambian, lo que refleja la influencia de esos parámetros en la distribución de probabilidad de las proporciones. Estos gráficos son útiles en campos como la estadística bayesiana, el aprendizaje automático y la teoría de juegos, donde entender la relación entre variables proporcionales es clave.

#### Descripción del Código

* **Cargar las librerías**: Se utilizan `ggplot2`, `dplyr` y `MCMCpack` para crear las gráficas y manejar datos. Asegúrate de que `MCMCpack` esté instalado en tu entorno de R.

* **Definir los parámetros**: Se establece una lista de vectores de parámetros $ \boldsymbol{\alpha} $ para diferentes configuraciones de la distribución Dirichlet. En este caso, se consideran tres conjuntos de parámetros: $(1, 1, 1)$, $(2, 5, 3)$ y $(5, 1, 1)$.

* **Inicializar una lista para almacenar los gráficos**: Se crea una lista vacía `plots` que se utilizará para guardar los gráficos generados.

* **Generar muestras**: Para cada conjunto de parámetros:
  - Se generan muestras aleatorias de la distribución Dirichlet utilizando la función `rdirichlet()` con un número especificado de muestras (1000 en este caso).
  - Las muestras se convierten en un data frame, y se nombran las columnas como $x_1$, $x_2$ y $x_3$ para representar las proporciones.

* **Graficar**: Se utiliza `ggplot` para crear un gráfico de dispersión de las muestras generadas:
  - Se mapea $x_1$ en el eje X y $x_2$ en el eje Y.
  - Se ajusta la transparencia de los puntos para mejorar la visualización.
  - Se añaden etiquetas al gráfico y se limitan los ejes a un rango de [0, 1].

* **Almacenar y mostrar los gráficos**: Cada gráfico generado se almacena en la lista `plots`, y posteriormente se imprimen todos los gráficos utilizando un bucle.

### Resumen
Este código ilustra cómo generar y visualizar muestras de la distribución Dirichlet para diferentes configuraciones de parámetros. Los gráficos resultantes permiten observar la distribución de las proporciones en un espacio de probabilidades, lo que es útil en contextos de modelado estadístico y análisis de datos.

**EJERCICIO 15**

La **Distribución de Dirichlet** es una distribución de probabilidad multivariada continua que es la generalización de la Distribución Beta. Se utiliza para modelar la distribución de probabilidades o proporciones sobre $K$ categorías distintas, donde la suma de estas proporciones siempre es igual a 1.

Su principal utilidad en Inteligencia Artificial (IA) y Aprendizaje Automático radica en su función como **distribución a priori conjugada** de la distribución Multinomial, lo que la hace indispensable en los modelos bayesianos para el **modelado de temas y clasificaciones probabilísticas**.

---

## 🤖 Usos Recomendados en Inteligencia Artificial

### 1. Modelado de Temas (Topic Modeling)

Este es el uso más famoso de la Distribución de Dirichlet, siendo el corazón del modelo **Latent Dirichlet Allocation (LDA)**, un algoritmo clave en el Procesamiento del Lenguaje Natural (NLP).

* **Ejemplo:** Analizar un gran corpus de documentos (p. ej., artículos científicos, correos electrónicos, o *tweets*) para descubrir los temas subyacentes.
* **Mecanismo:** El LDA utiliza la Distribución de Dirichlet en dos niveles para inferir una estructura probabilística:
    1.  **Distribución de Temas por Documento:** Se utiliza una Dirichlet para modelar la **proporción de temas** presentes en un documento. Es decir, un documento puede ser 70% "Nanotecnología", 20% "Materiales" y 10% "IA".
    2.  **Distribución de Palabras por Tema:** Se utiliza otra Dirichlet para modelar la **proporción de palabras** que componen cada tema. Por ejemplo, el tema "Nanotecnología" puede estar compuesto por 10% la palabra "quantum", 5% "graphene", 3% "synthesis", etc.
* **Parámetros:** Los parámetros $\alpha$ de la Dirichlet controlan la **dispersión** de estas distribuciones. Un valor bajo (cercano a 0) promueve distribuciones más dispersas (los documentos tratan sobre pocos temas), mientras que un valor alto promueve distribuciones más uniformes.

### 2. Clasificación Bayesiana y Mezclas (Clustering)

La Beta y su generalización, la Dirichlet, son fundamentales en la estadística bayesiana.

* **Ejemplo:** Modelar la incertidumbre sobre la **probabilidad de que un *pixel* pertenezca a una de $K$ clases** (p. ej., cielo, bosque, agua) en la segmentación de imágenes.
* **Uso Recomendado (Inferencia Bayesiana):** La distribución de Dirichlet es la **conjugada a priori** de la Distribución Multinomial. Esto significa que si se tienen datos de recuento (Multinomiales) y se usa una Dirichlet como *a priori* para la probabilidad de cada categoría, la distribución *a posteriori* también será una Dirichlet. Esto hace que la actualización del conocimiento (aprendizaje) sea matemáticamente simple y eficiente.
* **Modelos de Mezclas Dirichlet (DPM):** Se utiliza para realizar *clustering* (agrupación) no paramétrico, donde el número de *clusters* o grupos **no tiene que ser especificado de antemano**. La Dirichlet permite que el modelo decida dinámicamente cuántos componentes (clusters) son necesarios para modelar los datos.

### 3. Asignación de Recursos y Toma de Decisiones

En campos relacionados con la optimización y la toma de decisiones probabilísticas, la Dirichlet ayuda a modelar la incertidumbre sobre las preferencias o recompensas.

* **Ejemplo:** En **Aprendizaje por Refuerzo** aplicado a la publicidad, modelar la **proporción de clics** que recibirá cada uno de los $K$ anuncios disponibles.
* **Mecanismo:** Es una alternativa o complemento al uso de la Distribución Beta en problemas de **Multi-Armed Bandit** (como el Thompson Sampling). En lugar de modelar la probabilidad de éxito de cada "brazo" de forma independiente (con la Beta), la Dirichlet puede modelar la **distribución conjunta de las preferencias** de los usuarios entre $K$ opciones.

### 4. Generación de Datos Sintéticos

* **Ejemplo:** Generar datos sintéticos para entrenamiento de modelos donde las entradas son **proporciones** que deben sumar a la unidad (p. ej., proporciones de diferentes tipos de células en un tejido, proporciones de ingredientes en una receta, o distribuciones de tráfico de red entre $K$ protocolos).
* **Uso Recomendado:** Se utiliza como una herramienta de muestreo para crear **datos realistas y variados** que respetan la restricción de suma a uno, lo cual es fundamental para validar modelos de aprendizaje automático en entornos simulados.

#### Codigo en phyton

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import gamma

## ----------------------------------------------------
## Función para generar muestras de la Distribución Dirichlet (basada en Gamma)
def rdirichlet(alpha, size=1):
    """
    Genera muestras aleatorias de la Distribución Dirichlet.
    alpha: Vector de parámetros (list o array)
    size: Número de muestras a generar
    """
## Generar variables Gamma independientes para cada dimensión
## La escala (scale) se fija a 1
## La forma (shape/a) es el vector alpha
    gamma_samples = np.array([gamma.rvs(a=a, scale=1, size=size) for a in alpha]).T

## Normalizar las muestras sumando a 1 (X_i = Y_i / sum(Y_j))
    dirichlet_samples = gamma_samples / np.sum(gamma_samples, axis=1, keepdims=True)
    return dirichlet_samples

## ----------------------------------------------------
## 1. Definir los parámetros de la distribución Dirichlet (alpha)
alpha_values = [[1, 1, 1], [2, 5, 3], [5, 1, 1]]

## 2. Configuración de la figura para mostrar múltiples gráficos
n_plots = len(alpha_values)
fig, axes = plt.subplots(1, n_plots, figsize=(5 * n_plots, 5))
## Si solo hay un gráfico, axes no es un array, lo convertimos para el bucle
if n_plots == 1:
    axes = [axes]

n_points = 1000  # Número de muestras

## 3. Generar muestras y graficar para cada conjunto de parámetros
for i, alpha in enumerate(alpha_values):
## Generar muestras (K=3 dimensiones: x1, x2, x3)
    samples = rdirichlet(alpha, size=n_points)

## Convertir a DataFrame para facilitar el uso de Seaborn y etiquetas
    sample_data = pd.DataFrame(samples, columns=["x1", "x2", "x3"])

## Usar Seaborn o Matplotlib para graficar x1 vs x2
    ax = axes[i]
    sns.scatterplot(
        data=sample_data,
        x="x1",
        y="x2",
        alpha=0.5,
        s=10, # Tamaño de los puntos
        ax=ax
    )

## Configurar títulos y límites
    alpha_str = ", ".join(map(str, alpha))
    ax.set_title(f"Distribución Dirichlet (α = ({alpha_str}))")
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal', adjustable='box') # Hace que los ejes sean iguales

## Ajustar el diseño para evitar superposiciones
plt.tight_layout()
plt.show()
```

## Descripción del Código Python para la Gráfica de la Distribución Dirichlet

El código en **Python** tiene como objetivo simular y visualizar la **Distribución Dirichlet** para diferentes conjuntos de parámetros $\boldsymbol{\alpha} = (\alpha_1, \alpha_2, \ldots, \alpha_K)$. La Distribución Dirichlet es una **distribución de probabilidad multivariada** sobre una distribución de probabilidades, es decir, genera vectores $\mathbf{x}=(x_1, \ldots, x_K)$ donde $x_i \ge 0$ y $\sum x_i = 1$.

El método utilizado para la simulación es la relación fundamental entre la Dirichlet y la **Distribución Gamma**, utilizando **SciPy** para la generación de números aleatorios y **Matplotlib/Seaborn** para la visualización. Dado que es una distribución tridimensional ($K=3$), la visualización se presenta en un plano 2D mostrando la relación entre $x_1$ y $x_2$.

***

### 1. Función de Generación de Muestras (`rdirichlet`)

| Código | Concepto Matemático | Descripción |
| :--- | :--- | :--- |
| `gamma_samples = np.array([...])` | $Y_i \sim \text{Gamma}(\alpha_i, 1)$ | Define la función clave, que genera $K$ **variables aleatorias Gamma independientes**. Para cada dimensión ($i$), la variable Gamma se genera con el parámetro de **forma** igual a $\alpha_i$ y el parámetro de **escala** (o tasa inversa) fijo en $1$. |
| `dirichlet_samples = gamma_samples / np.sum(...)` | $x_i = Y_i / \sum_{j=1}^K Y_j$ | **Normalización**: Divide cada muestra de Gamma por la suma de todas las muestras de Gamma en esa iteración (fila). Esta normalización asegura que $\sum x_i = 1$, cumpliendo la restricción del simplex. |

***
***

### 2. Parámetros y Simulación

| Código | Descripción |
| :--- | :--- |
| `alpha_values = [[1, 1, 1], [2, 5, 3], [5, 1, 1]]` | **Parámetros $\boldsymbol{\alpha}$**: Define los tres conjuntos de parámetros a simular. Estos conjuntos ilustran diferentes formas: **Simétrica** ($[1, 1, 1]$), **Sesgada a $x_2$** ($[2, 5, 3]$), y **Sesgada a $x_1$** ($[5, 1, 1]$). |
| `n_plots = len(alpha_values)` | **Configuración del Lienzo**: Define el número de subgráficos. Se utiliza `plt.subplots(1, n_plots, ...)` para crear una fila con $N$ columnas. |
| `n_points = 1000` | **Tamaño de Muestra**: Define la cantidad de vectores (puntos) a generar para cada distribución. |
| `samples = rdirichlet(alpha, size=n_points)` | **Generación de Muestras**: Llama a la función personalizada para generar $1000$ muestras Dirichlet. |
| `sample_data = pd.DataFrame(...)` | **Estructura de Datos**: Las muestras se convierten a un DataFrame de Pandas con columnas $x_1$, $x_2$ y $x_3$, facilitando el uso de Seaborn. |

***

### 3. Visualización de los Resultados

La Distribución Dirichlet $K=3$ se representa en un **simplex 2D** (un triángulo equilátero), pero el código opta por graficar las coordenadas $x_1$ vs $x_2$ en un cuadrado $[0, 1] \times [0, 1]$, ya que $x_3$ se determina automáticamente por $x_3 = 1 - x_1 - x_2$.

| Código | Descripción |
| :--- | :--- |
| `sns.scatterplot(...)` | **Trazado de Puntos**: Utiliza `scatterplot` de Seaborn para dibujar cada muestra $(x_1, x_2)$ como un punto. La restricción $x_1 + x_2 \le 1$ limita los puntos a la región triangular inferior izquierda. |
| `ax.set_title(...)` | **Etiquetado**: Asigna un título a cada subgráfico que incluye los valores específicos de $\boldsymbol{\alpha}$. |
| `ax.set_aspect('equal', adjustable='box')` | **Ajuste de Aspecto**: Asegura que el eje $x$ y el eje $y$ tengan la misma escala visual, lo cual es crucial para la interpretación geométrica de los datos en el simplex. |
| `plt.tight_layout()` | **Disposición Final**: Ajusta automáticamente los parámetros de la subtrama para dar espacio a los títulos y etiquetas. |

**Interpretación de las Gráficas:**

1.  **$\boldsymbol{\alpha} = (1, 1, 1)$:** Los puntos se distribuyen **uniformemente** en todo el simplex (la región triangular).
2.  **$\boldsymbol{\alpha} = (2, 5, 3)$:** La densidad de puntos se concentra donde $x_2$ es alto (hacia el eje $y$), ya que $\alpha_2=5$ es el parámetro dominante.
3.  **$\boldsymbol{\alpha} = (5, 1, 1)$:** La densidad de puntos se concentra donde $x_1$ es alto (hacia el eje $x$), ya que $\alpha_1=5$ es el parámetro dominante.

### Distribución de Chi-cuadrada $\chi^2$ o de Pearson

* **Descripción**: Modelo de distribuciones que se utiliza en pruebas de hipótesis y en la construcción de intervalos de confianza para varianzas. Se deriva de la suma de los cuadrados de variables aleatorias normales estándar.

* **Parámetros**:
  - $ k $ (grados de libertad)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x) =
\begin{cases}
\displaystyle{\frac{1}{2^{k/2} \Gamma(k/2)} x^{(k/2) - 1} e^{-x/2}} & \text{si } x \geq 0 \\
0 & \text{si } x < 0
\end{cases}
$$

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) = \int_0^x f(t) \, dt
$$

* **Valor Esperado**:
$$
E[X] = k
$$

* **Media**:
$$
\mu_X = k
$$

* **Desviación Estándar**:
$$
\sigma = \sqrt{2k}
$$

* **Percentiles**: Los percentiles se pueden calcular utilizando la función inversa de la CDF.

* **Comandos en R**:

```r
## PDF
dchisq(x, df = k)

## CDF
pchisq(x, df = k)

## Simulación
rchisq(n, df = k)

#### Ejemplo de Gráfica de la Distribución Chi-Cuadrada

La distribución Chi-cuadrada $\chi^2$ es una distribución de probabilidad que se utiliza comúnmente en inferencia estadística, especialmente en pruebas de hipótesis y en la construcción de intervalos de confianza. Se define como la distribución de la suma de los cuadrados de $k$ variables aleatorias independientes, cada una con una distribución normal estándar. El parámetro $k$ representa los grados de libertad de la distribución.

La forma de la distribución Chi-cuadrada se determina por el número de grados de libertad:
- Si $k = 1$, la distribución tiene una forma sesgada hacia la derecha.
- A medida que $k$ aumenta, la distribución se aproxima a una distribución normal, volviéndose más simétrica.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad (PDF) de la distribución Chi-cuadrada para varios valores de $k$. A medida que se ajusta este parámetro, la forma de la distribución varía, reflejando cómo diferentes valores de $k$ influyen en la concentración de probabilidad.

La distribución Chi-cuadrada es valiosa en diversas áreas, como la teoría de la estadística, la biología y las ciencias sociales, donde se requiere analizar la variabilidad y la relación entre variables.

```python
"""
## Cargar las librerías necesarias
library(ggplot2)
library(tidyr)

## Definir los grados de libertad
k_values <- c(1, 2, 5, 10)  # Diferentes valores de k

## Crear un rango de valores para x
x <- seq(0, 30, length.out = 500)

## Calcular la PDF para cada valor de k
pdf_data <- data.frame(x = x)

for (k in k_values) {
  pdf_data[[paste("PDF_k", k, sep = "_")]] <- dchisq(x, df = k)
}

## Convertir el data frame a formato largo para graficar
pdf_long <- pivot_longer(pdf_data, cols = starts_with("PDF_k"),
                          names_to = "k", values_to = "density")

## Graficar las distribuciones Chi-cuadrada
ggplot(pdf_long, aes(x = x, y = density, color = k)) +
  geom_line(linewidth = 1) +  # Cambiado size por linewidth
  labs(title = "Distribución Chi-Cuadrada para Diferentes Valores de k",
       x = "$x$",
       y = "Densidad de Probabilidad (PDF)",
       color = "Grados de Libertad (k)") +
  theme_minimal() +
  scale_color_discrete(labels = c("k = 1", "k = 2", "k = 5", "k = 10"))
"""
```

#### Descripción del Código

* **Cargar librerías**: Se utilizan `ggplot2` y `tidyr` para crear la gráfica y manipular datos.
* **Definir los parámetros**: Se establecen varios valores de grados de libertad $k$ para diferentes configuraciones de la distribución Chi-cuadrada.
* **Crear un rango de valores para $x$**: Se define un rango de valores desde 0 hasta 30 para representar la distribución Chi-cuadrada.
* **Calcular la PDF**: Se utiliza `dchisq()` para calcular la función de densidad de probabilidad para los valores de $x$ con los grados de libertad definidos.
* **Convertir a formato largo**: Se transforma el data frame a un formato largo utilizando `pivot_longer()` para facilitar la graficación.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $ PDF $ de la distribución Chi-cuadrada para los diferentes valores de $k$.

**EJERCICIO 16**

La **Distribución Chi-Cuadrada ($\chi^2$)** es una distribución de probabilidad continua que surge como la distribución de la **suma de los cuadrados de $k$ variables aleatorias normales estándar independientes**. Sus únicos parámetros son los **grados de libertad ($k$)**. Su principal uso es en el ámbito de las pruebas de hipótesis y la inferencia estadística.

A continuación, se presentan sus ejemplos y usos recomendados en Ciencia de Materiales y Diseño de Experimentos (DOE).

***

## ⚛️ Ciencia de Materiales: Variabilidad y Ajuste de Modelos

En Ciencia de Materiales, la distribución $\chi^2$ es fundamental para evaluar la calidad del ajuste entre los datos experimentales y los modelos teóricos, y para analizar la variabilidad de las mediciones.

### 1. Bondad de Ajuste de Distribuciones de Vida Útil

* **Uso Recomendado:** Determinar si un conjunto de datos de vida útil (tiempo hasta la falla) de un material o componente sigue realmente una distribución específica (como Weibull, Log-Normal o Exponencial).
* **Mecanismo (Prueba de $\chi^2$):** Se aplica la **Prueba de Bondad de Ajuste de Chi-Cuadrada**. Se comparan las **frecuencias de fallo observadas** en diferentes intervalos de tiempo (datos experimentales) con las **frecuencias esperadas** según la distribución teórica propuesta. La estadística $\chi^2$ resultante cuantifica la discrepancia total. Si el valor $\chi^2$ es bajo, se acepta que el modelo teórico se ajusta bien a los datos del material.

### 2. Análisis de Dispersión en Mediciones

* **Uso Recomendado:** Analizar si la **varianza** ($\sigma^2$) en las mediciones de una propiedad del material (p. ej., resistencia, dureza, espesor de una capa delgada) es significativamente mayor o menor que un valor estándar o esperado.
* **Mecanismo:** La distribución $\chi^2$ se utiliza para construir **Intervalos de Confianza para la Varianza Poblacional** o para realizar la **Prueba de Hipótesis sobre una Única Varianza**. Esto es crucial para el control de calidad, ya que la varianza excesiva a menudo indica problemas en el proceso de fabricación del material (p. ej., falta de homogeneidad).

### 3. Ajuste de Modelos por Mínimos Cuadrados Ponderados

* **Uso Recomendado:** Evaluar la calidad general del ajuste en técnicas como la **Reflectividad de Rayos X (XRR)** o la **Elipsometría** (usadas para caracterizar películas delgadas y nanoláminas).
* **Mecanismo:** Los programas de ajuste de datos que utilizan el método de Mínimos Cuadrados suelen reportar una estadística **$\chi^2$ reducida** (a menudo denominada *Goodness-of-Fit*). Este valor mide la suma de los errores cuadrados normalizados por la varianza experimental (el ruido). Un $\chi^2$ cercano a la unidad indica un ajuste excelente.

***

## 🧪 Diseño de Experimentos (DOE): Categóricos y Varianza

En DOE, la distribución $\chi^2$ es esencial para tomar decisiones sobre los resultados experimentales, especialmente cuando se trabaja con datos categóricos o se comparan varianzas.

### 4. Independencia de Factores Experimentales

* **Uso Recomendado:** Determinar si la **efectividad de un factor experimental** (p. ej., el tipo de catalizador: A, B o C) es independiente del resultado categórico (p. ej., el producto final fue "Éxito" o "Fallo").
* **Mecanismo (Prueba de $\chi^2$ de Independencia):** Se utiliza una **Tabla de Contingencia** para organizar las frecuencias observadas. La prueba $\chi^2$ evalúa si las desviaciones entre las frecuencias observadas y las frecuencias que se esperarían bajo el supuesto de independencia son estadísticamente significativas. Es fundamental para el análisis de experimentos donde la variable de respuesta es cualitativa.

### 5. Comparación de Varianzas entre Tratamientos

* **Uso Recomendado:** En un DOE, verificar el **supuesto de homocedasticidad** (varianzas iguales) antes de aplicar un ANOVA (Análisis de Varianza).
* **Mecanismo (Prueba de Bartlett o Levene):** La mayoría de las pruebas para homocedasticidad se basan en la distribución $\chi^2$ (o la distribución F, que se relaciona con ella). Si la varianza del resultado es significativamente diferente entre los distintos grupos de tratamiento, el ANOVA puede no ser válido. La prueba $\chi^2$ ayuda a confirmar si las varianzas de los diferentes "lotes" de materiales o procesos son iguales.

### 6. Diseño de Experimentos Factoriales con Datos Categóricos

* **Uso Recomendado:** Analizar los efectos de múltiples factores en un diseño factorial cuando la respuesta es binaria o nominal.
* **Mecanismo:** Se utiliza la prueba $\chi^2$ para analizar si los **efectos de interacción** entre los factores son significativos, basándose en la proporción de éxitos o fracasos en cada combinación de tratamiento. Esto permite identificar qué combinaciones de factores (p. ej., Temperatura alta Y Catalizador X) tienen un impacto desproporcionado en el resultado categórico.

#### Codigo en phyton

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2 # Importamos la distribución Chi-cuadrada

## ----------------------------------------------------
## 1. Definir los grados de libertad
k_values = [1, 2, 5, 10]  # Diferentes valores de k (df)

## 2. Crear un rango de valores para x
## Similar a seq(0, 30, length.out = 500) en R
x = np.linspace(0, 30, 500)

## 3. Crear un diccionario para almacenar los resultados de la PDF
pdf_data_dict = {'x': x}

## Calcular la PDF para cada valor de k
for k in k_values:
## chi2.pdf(x, df=k) es el equivalente a dchisq(x, df = k) en R
    pdf_values = chi2.pdf(x, df=k)
    pdf_data_dict[f"k = {k}"] = pdf_values

## Convertir el diccionario a un DataFrame
pdf_data = pd.DataFrame(pdf_data_dict)

## 4. Convertir el DataFrame a formato largo para graficar (similar a pivot_longer)
pdf_long = pdf_data.melt(
    id_vars='x',                                      # Columna de identificación
    value_vars=[f"k = {k}" for k in k_values],        # Columnas de valores
    var_name="Grados de Libertad (k)",                # Nueva columna para las etiquetas
    value_name="density"                              # Nueva columna para los valores de densidad
)

## 5. Graficar las distribuciones Chi-cuadrada
sns.set_theme(style="whitegrid") # Similar a theme_minimal()

plt.figure(figsize=(10, 6))

## Usar seaborn.lineplot
sns.lineplot(
    data=pdf_long,
    x='x',
    y='density',
    hue='Grados de Libertad (k)',  # Usar k para diferenciar el color
    linewidth=2
)

## Añadir etiquetas y título (equivalente a labs)
plt.title("Distribución Chi-Cuadrada para Diferentes Valores de k", fontsize=16)
plt.xlabel("$x$", fontsize=14)
plt.ylabel("Densidad de Probabilidad (PDF)", fontsize=12)

## Configurar la leyenda
plt.legend(title="Grados de Libertad (k)", loc='upper right')

## Mostrar la gráfica
plt.show()
```

## Descripción del Código Python para la Gráfica de la Distribución Chi-Cuadrada

El código en **Python** tiene el propósito de calcular y visualizar la **Función de Densidad de Probabilidad (PDF)** de la **Distribución Chi-Cuadrada ($\chi^2$)** para diferentes valores de sus **grados de libertad ($k$)**. La distribución Chi-Cuadrada es fundamental en la inferencia estadística, especialmente en pruebas de bondad de ajuste y análisis de varianza.

El script utiliza la función $\mathbf{chi2}$ de **SciPy** para el cálculo estadístico, **NumPy** para operaciones numéricas, y **Pandas/Seaborn/Matplotlib** para la estructuración de datos y la visualización comparativa de las curvas.

***

### 1. Inicialización y Parámetros

| Código | Descripción |
| :--- | :--- |
| `from scipy.stats import chi2` | **Librería Estadística**: Importa la clase `chi2` de SciPy, que contiene la función `pdf()` (equivalente a `dchisq()` en R). |
| `k_values = [1, 2, 5, 10]` | **Grados de Libertad ($k$)**: Define los cuatro valores de $k$ que se utilizarán para generar las curvas. El parámetro $k$ es el único parámetro de la distribución $\chi^2$. |
| `x = np.linspace(0, 30, 500)` | **Definición del Eje $x$**: Crea $500$ puntos uniformemente espaciados entre $0$ y $30$. El dominio de la distribución $\chi^2$ es $x \ge 0$. |

***

### 2. Cálculo de la Función de Densidad (PDF) y Estructuración de Datos

| Código | Parámetro `chi2.pdf` | Parámetro Estadístico | Significado |
| :--- | :--- | :--- | :--- |
| `df` | **`df`** | Grados de Libertad ($k$) | Determina la **forma** de la curva. Es igual al número de variables Normales estándar independientes elevadas al cuadrado que se suman. |

| Código | Descripción |
| :--- | :--- |
| `pdf_values = chi2.pdf(x, df=k)` | **Cálculo de la PDF**: Llama a la función $\mathbf{chi2.pdf()}$ para calcular los valores de densidad. El parámetro `df` (degrees of freedom) es el $k$ de la distribución. |
| `pdf_data_dict[f"k = {k}"] = pdf_values` | **Almacenamiento Temporal**: Almacena las densidades calculadas en un diccionario, etiquetando la columna con su valor de $k$ (ej: `"k = 5"`). |
| `pdf_long = pdf_data.melt(...)` | **Transformación a Formato Largo**: Utiliza el método `melt` de Pandas para **pivotar** el DataFrame. Las columnas de densidad se transforman en dos nuevas columnas: `Grados de Libertad (k)` (etiqueta) y `density` (valor). Este formato es **obligatorio** para usar la función `hue` de Seaborn de manera eficiente y generar automáticamente la leyenda. |

***

### 3. Visualización y Estilizado del Gráfico

| Código | Descripción |
| :--- | :--- |
| `sns.lineplot(...)` | **Trazado de Múltiples Líneas**: Dibuja las cuatro curvas de densidad en el mismo gráfico. El parámetro **`hue='Grados de Libertad (k)'`** le indica a Seaborn que use la columna de etiquetas como variable categórica para asignar diferentes colores y generar la leyenda correspondiente. |
| `plt.title(...)`, `plt.xlabel(...)`, `plt.ylabel(...)` | **Etiquetas y Títulos**: Establece el título principal y las etiquetas de los ejes. Se utiliza la notación LaTeX (`$x$`) para el eje $x$. |
| `plt.legend(title="Grados de Libertad (k)", ...)` | **Configuración de Leyenda**: Coloca la leyenda en la esquina superior derecha. |

El gráfico resultante muestra que:
1.  Todas las curvas comienzan en $x=0$.
2.  La distribución está **fuertemente sesgada a la derecha** para valores pequeños de $k$ (especialmente $k=1$ y $k=2$).
3.  A medida que los **grados de libertad ($k$) aumentan**, la curva se vuelve más **simétrica** y se **desplaza** hacia la derecha, acercándose a la forma de una distribución Normal.

### Distribución t-Student

* **Descripción**: Modelo utilizado para estimar la media de una población cuando el tamaño de la muestra es pequeño y la varianza poblacional es desconocida. Es útil en pruebas de hipótesis y en intervalos de confianza.

* **Parámetros**:
$ \nu $ (grados de libertad)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x) = \displaystyle{\frac{\Gamma\left(\frac{\nu + 1}{2}\right)}{\sqrt{\nu \pi} \Gamma\left(\frac{\nu}{2}\right)} \left(1 + \frac{x^2}{\nu}\right)^{-\frac{\nu + 1}{2}}} \quad \text{si } -\infty < x < \infty
$$

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) = \int_{-\infty}^x f(t) \, dt
$$

* **Valor Esperado**: $ E[X] = 0 $ (para 4 \nu > 1 $)

* **Media**: $\mu_X = 0 $ (para $\nu > 1 $)

* **Desviación Estándar**:  $\sigma = \sqrt{\frac{\nu}{\nu - 2}} $(para $ \nu > 2 $)

* **Percentiles**: Los percentiles se pueden calcular utilizando la función inversa de la CDF.

**Comandos en R**:
```r
## PDF
dt(x, df = nu)

## CDF
pt(x, df = nu)

## Simulación
rt(n, df = nu)

#### Ejemplo de Gráfica de la Distribución t-Student

La distribución t-Student es una distribución de probabilidad que se utiliza principalmente en inferencia estadística, especialmente para estimar la media de una población cuando la muestra es pequeña y la varianza es desconocida. Se define como la distribución de una variable aleatoria que es el cociente de una variable normal estándar y la raíz cuadrada de una variable Chi-cuadrada dividida por sus grados de libertad. El parámetro $k$ representa los grados de libertad de la distribución.

La forma de la distribución t-Student se determina por el número de grados de libertad:
- Si $k$ es pequeño, la distribución es más ancha y presenta colas más pesadas en comparación con la distribución normal.
- A medida que $k$ aumenta, la distribución se aproxima a la normal estándar, volviéndose más simétrica y estrecha.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad (PDF) de la distribución t-Student para varios valores de $k$. A medida que se ajusta este parámetro, la forma de la distribución varía, reflejando cómo diferentes valores de $k$ influyen en la concentración de probabilidad.

La distribución t-Student es valiosa en campos como la estadística, la investigación social y la psicología, donde se requiere realizar inferencias sobre medias poblacionales con muestras pequeñas.

```python
"""
## Cargar la librería necesaria
library(ggplot2)

## Definir los grados de libertad
k_values <- c(1, 2, 5, 10)  # Diferentes valores de k

## Crear un rango de valores para x
x <- seq(-5, 5, length.out = 500)

## Calcular la PDF para cada valor de k
pdf_data <- data.frame(x = x)

for (k in k_values) {
  pdf_data[[paste("PDF_k", k, sep = "_")]] <- dt(x, df = k)
}

## Convertir el data frame a formato largo para graficar
pdf_long <- tidyr::pivot_longer(pdf_data, cols = starts_with("PDF_k"),
                                  names_to = "k", values_to = "density")

## Graficar las distribuciones t-Student
ggplot(pdf_long, aes(x = x, y = density, color = k)) +
  geom_line(linewidth = 1) +
  labs(title = "Distribución t-Student para Diferentes Valores de k",
       x = "$x$",
       y = "Densidad de Probabilidad (PDF)",
       color = "Grados de Libertad (k)") +
  theme_minimal() +
  scale_color_discrete(labels = c("k = 1", "k = 2", "k = 5", "k = 10"))
"""
```

#### Descripción del Código

* **Cargar librería**: Se utiliza `ggplot2` y `tidyr` para crear la gráfica y manipular datos.
* **Definir los parámetros**: Se establecen varios valores de grados de libertad $k$ para diferentes configuraciones de la distribución t-Student.
* **Crear un rango de valores para $x$**: Se define un rango de valores desde -5 hasta 5 para representar la distribución t-Student.
* **Calcular la PDF**: Se utiliza `dt()` para calcular la función de densidad de probabilidad para los valores de $x$ con los grados de libertad definidos.
* **Convertir a formato largo**: Se transforma el data frame a un formato largo utilizando `pivot_longer()` para facilitar la graficación.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $ PDF $ de la distribución t-Student para los diferentes valores de $k$.

### Distribución F (Fisher-Snedecor)

* **Descripción**: Modelo utilizado para comparar dos varianzas a través de la relación entre dos variables aleatorias independientes que siguen distribuciones Chi-cuadrada. Se usa comúnmente en el análisis de varianza (ANOVA).

* **Parámetros**:
  - $d_1 $(grados de libertad del numerador)
  - $ d_2 $ (grados de libertad del denominador)

* **Función de Densidad de Probabilidad (PDF)**:

$$
\displaystyle{f(x) = \frac{\left(\frac{d_1}{d_2}\right)^{\frac{d_1}{2}} \frac{x^{\frac{d_1}{2} - 1}}{\left(1 + \frac{d_1}{d_2} x\right)^{\frac{d_1 + d_2}{2}}}}{B\left(\frac{d_1}{2}, \frac{d_2}{2}\right)}} \quad \text{si } x \geq 0
$$
donde $ B $ es la función beta.

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) = \int_0^x f(t) \, dt
$$

* **Valor Esperado**:
$$
E[X] = \frac{d_1}{d_1 - 2} \quad \text{(para } d_1 > 2\text{)}
$$

* **Media**:
$$
\mu_X = \frac{d_1}{d_1 - 2} \quad \text{(para } d_1 > 2\text{)}
$$

* **Desviación Estándar**:
$$
\sigma = \sqrt{\frac{2d_2^2(d_1 + d_1 - 2)}{d_1(d_2 - 2)^2(d_2 - 4)}} \quad \text{(para } d_2 > 4\text{)}
$$

* **Percentiles**: Los percentiles se pueden calcular utilizando la función inversa de la CDF.

**Comandos en R**:
```r
## PDF
df(x, df1 = d1, df2 = d2)

## CDF
pf(x, df1 = d1, df2 = d2)

## Simulación
rf(n, df1 = d1, df2 = d2)

#### Ejemplo de Gráfica de la Distribución F (Fisher-Snedecor)

La distribución F (Fisher-Snedecor) es una distribución de probabilidad que se utiliza principalmente en análisis de varianza y pruebas de hipótesis. Se define como la distribución de la razón de dos variables aleatorias independientes que siguen una distribución Chi-cuadrada, cada una dividida por sus grados de libertad. Los parámetros de la distribución F son $d_1$ y $d_2$, que representan los grados de libertad del numerador y el denominador, respectivamente.

La forma de la distribución F se determina por los grados de libertad:
- Si $d_1$ y $d_2$ son pequeños, la distribución es asimétrica y tiene colas más pesadas.
- A medida que ambos grados de libertad aumentan, la distribución se aproxima a una distribución normal, volviéndose más simétrica.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad (PDF) de la distribución F para varios pares de grados de libertad $(d_1, d_2)$. A medida que se ajustan estos parámetros, la forma de la distribución varía, reflejando cómo diferentes combinaciones de $d_1$ y $d_2$ influyen en la concentración de probabilidad.

La distribución F es valiosa en campos como la estadística, la ingeniería y las ciencias sociales, donde se requiere comparar varianzas y realizar análisis de varianza (ANOVA).

```python
"""
## Cargar la librería necesaria
library(ggplot2)

## Definir los grados de libertad
df_values <- list(c(2, 5), c(5, 2), c(5, 10), c(10, 5))  # Diferentes pares (d1, d2)

## Crear un rango de valores para x
x <- seq(0, 5, length.out = 500)

## Calcular la PDF para cada par de grados de libertad
pdf_data <- data.frame(x = x)

for (df in df_values) {
  pdf_data[[paste("PDF_d1", df[1], "_d2", df[2], sep = "")]] <- df(x, df = df[1], df2 = df[2])
}

## Convertir el data frame a formato largo para graficar
pdf_long <- tidyr::pivot_longer(pdf_data, cols = starts_with("PDF_d1"),
                                  names_to = "Degrees_of_Freedom", values_to = "density")

## Graficar las distribuciones F
ggplot(pdf_long, aes(x = x, y = density, color = Degrees_of_Freedom)) +
  geom_line(linewidth = 1) +
  labs(title = "Distribución F (Fisher-Snedecor) para Diferentes Pares de Grados de Libertad",
       x = "$x$",
       y = "Densidad de Probabilidad (PDF)",
       color = "Grados de Libertad $(d_1, d_2)$") +
  theme_minimal() +
  scale_color_discrete(labels = c("(2, 5)", "(5, 2)", "(5, 10)", "(10, 5)"))
  """
```

#### Descripción del Código

* **Cargar librería**: Se utiliza `ggplot2` y `tidyr` para crear la gráfica y manipular datos.
* **Definir los grados de libertad**: Se establecen varios pares de grados de libertad $(d_1, d_2)$ para diferentes configuraciones de la distribución F (Fisher-Snedecor).
* **Crear un rango de valores para $x$**: Se define un rango de valores desde 0 hasta 5 para representar la distribución F.
* **Calcular la PDF**: Se utiliza `df()` para calcular la función de densidad de probabilidad para los valores de $x$ con los grados de libertad definidos.
* **Convertir a formato largo**: Se transforma el data frame a un formato largo utilizando `pivot_longer()` para facilitar la graficación.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $ PDF $ de la distribución F para los diferentes pares de grados de libertad $(d_1, d_2)$.

**EJERCICIO 17**

La **Distribución F (Fisher-Snedecor)** es fundamental en el **Diseño de Experimentos (DOE)** porque es la base estadística del **Análisis de Varianza (ANOVA)**. Se define como la distribución del cociente de dos variables aleatorias Chi-Cuadrada ($\chi^2$) independientes, cada una dividida por sus respectivos grados de libertad:

$$F = \frac{\chi^2_1 / d_1}{\chi^2_2 / d_2}$$

Donde $d_1$ y $d_2$ son los grados de libertad del numerador y del denominador, respectivamente.

***

## 🧪 Usos Clave en el Diseño de Experimentos (DOE)

La distribución F se utiliza principalmente para **comparar varianzas** y determinar si los efectos de diferentes **factores de tratamiento** son estadísticamente significativos.

### 1. Análisis de Varianza (ANOVA)

Este es el uso primordial de la distribución F en el DOE. El ANOVA se utiliza para probar si las medias de dos o más grupos son iguales, analizando la variación dentro de los grupos y entre ellos.

* **Mecanismo:** La prueba F en ANOVA calcula el cociente entre la **Varianza Explicada (MS Tratamiento)** y la **Varianza No Explicada (MS Error)**.
    $$F_{\text{calculada}} = \frac{\text{MS Tratamiento}}{\text{MS Error}}$$
* **Interpretación:**
    * **Numerador (MS Tratamiento):** Representa la variación **entre** las medias de los diferentes grupos de tratamiento (efecto del factor).
    * **Denominador (MS Error):** Representa la variación **dentro** de cada grupo (varianza residual o ruido experimental).
* **Decisión:** Si los tratamientos no tienen ningún efecto, ambas varianzas deberían ser aproximadamente iguales, y $F$ sería cercano a 1. Si $F_{\text{calculada}}$ es significativamente mayor que 1, se **rechaza la hipótesis nula** (que las medias son iguales) y se concluye que **el factor de tratamiento tiene un efecto significativo** en la variable de respuesta.

### 2. Pruebas de Hipótesis en Regresión Lineal

En los modelos de regresión lineal (que son una forma de ANOVA), la distribución F se utiliza para evaluar la bondad de ajuste del modelo.

* **Uso Recomendado:** Determinar si el modelo de regresión en su conjunto explica una **proporción significativa** de la variabilidad total de los datos.
* **Mecanismo:** La prueba F compara la varianza explicada por la regresión con la varianza no explicada (residual). Si la $F$ calculada es significativa, se concluye que **al menos una de las variables predictoras** está relacionada con la variable de respuesta.

### 3. Comparación de Varianzas de Dos Poblaciones

Aunque el ANOVA compara múltiples medias, la prueba F también se utiliza en un caso más simple: la comparación directa de las varianzas de dos poblaciones.

* **Uso Recomendado:** Determinar si la **variabilidad** de un nuevo proceso es significativamente diferente de la variabilidad del proceso estándar.
* **Mecanismo:** Se calcula el cociente de las dos varianzas muestrales: $F = s^2_1 / s^2_2$. Esto es fundamental para verificar el supuesto de **homocedasticidad** (varianzas iguales) antes de realizar una Prueba $t$ para dos muestras.

***

## 📊 Ejemplos Aplicados al Diseño Experimental

| Escenario DOE | Variable de Respuesta | Hipótesis Nula ($H_0$) | Uso de la Distribución F |
| :--- | :--- | :--- | :--- |
| **Experimento Factorial** | Resistencia de un polímero | La media de resistencia es la misma para todos los niveles de temperatura (el factor Temperatura no tiene efecto). | Se usa ANOVA (prueba F) para determinar si la variación debida al factor Temperatura es mayor que la variación del error aleatorio. |
| **Diseño de Bloques** | Tiempo de curado de un adhesivo | Las medias de los tiempos de curado son las mismas entre los diferentes tipos de lotes de material (Bloques). | La prueba F evalúa el efecto del factor (p. ej., tipo de aditivo) y el efecto de los bloques (p. ej., lote de materia prima), separando la varianza. |
| **Prueba de Homocedasticidad** | Variabilidad de la rugosidad superficial | La varianza de la rugosidad es la misma para el Proceso A y el Proceso B. | Se usa la prueba $F$ para varianzas (cociente de varianzas muestrales) para verificar la igualdad del ruido experimental. |

#### Codigo en phyton

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f # Importamos la distribución F

## ----------------------------------------------------
## 1. Definir los grados de libertad
df_values = [(2, 5), (5, 2), (5, 10), (10, 5)]  # Diferentes pares (d1, d2)

## 2. Crear un rango de valores para x
## Similar a seq(0, 5, length.out = 500) en R
x = np.linspace(0.01, 5, 500) # Empezamos ligeramente arriba de 0

## 3. Crear un diccionario para almacenar los resultados de la PDF
pdf_data_dict = {'x': x}

## Calcular la PDF para cada par de grados de libertad
for d1, d2 in df_values:
## f.pdf(x, dfn=d1, dfd=d2) es el equivalente a df(x, df1=d1, df2=d2) en R
    pdf_values = f.pdf(x, dfn=d1, dfd=d2)
## Usar una etiqueta clara para el diccionario
    label = f"({d1}, {d2})"
    pdf_data_dict[label] = pdf_values

## Convertir el diccionario a un DataFrame
pdf_data = pd.DataFrame(pdf_data_dict)

## 4. Convertir el DataFrame a formato largo para graficar (similar a pivot_longer)
## Nota: La lista de columnas a fundir es la lista de etiquetas de grados de libertad
label_columns = [f"({d1}, {d2})" for d1, d2 in df_values]

pdf_long = pdf_data.melt(
    id_vars='x',
    value_vars=label_columns,
    var_name="Grados de Libertad $(d_1, d_2)$", # Nombre de la columna para las etiquetas
    value_name="density"                        # Nombre de la columna para los valores de densidad
)

## 5. Graficar las distribuciones F
sns.set_theme(style="whitegrid") # Similar a theme_minimal()

plt.figure(figsize=(10, 6))

## Usar seaborn.lineplot
sns.lineplot(
    data=pdf_long,
    x='x',
    y='density',
    hue='Grados de Libertad $(d_1, d_2)$', # Usar la columna creada para la leyenda
    linewidth=2
)

## Añadir etiquetas y título (equivalente a labs)
plt.title("Distribución F (Fisher-Snedecor) para Diferentes Pares de Grados de Libertad", fontsize=16)
plt.xlabel("$x$", fontsize=14)
plt.ylabel("Densidad de Probabilidad (PDF)", fontsize=12)

## Configurar la leyenda
plt.legend(title="Grados de Libertad $(d_1, d_2)$", loc='upper right')

## Mostrar la gráfica
plt.show()
```

## Descripción del Código Python para la Gráfica de la Distribución F

El código en **Python** tiene el propósito de calcular y visualizar la **Función de Densidad de Probabilidad (PDF)** de la **Distribución F (Fisher-Snedecor)** para diferentes pares de **grados de libertad** ($d_1$, $d_2$). La Distribución F es crucial en el **Análisis de Varianza (ANOVA)** y se define como la razón de dos variables aleatorias Chi-Cuadrada independientes divididas por sus respectivos grados de libertad.

El script utiliza la función $\mathbf{f}$ de **SciPy** para el cálculo estadístico, **NumPy** para operaciones numéricas, y **Pandas/Seaborn/Matplotlib** para la estructuración de datos y la visualización comparativa de las curvas.

***

### 1. Inicialización y Parámetros

| Código | Descripción |
| :--- | :--- |
| `from scipy.stats import f` | **Librería Estadística**: Importa la clase `f` de SciPy, que contiene la función `pdf()` (equivalente a `df()` en R). |
| `df_values = [(2, 5), (5, 2), (5, 10), (10, 5)]` | **Grados de Libertad ($d_1, d_2$)**: Define los cuatro pares de grados de libertad a comparar. $d_1$ es el numerador y $d_2$ es el denominador. El orden es importante, como se ve en la comparación de $(2, 5)$ vs $(5, 2)$. |
| `x = np.linspace(0.01, 5, 500)` | **Definición del Eje $x$**: Crea $500$ puntos espaciados entre $0.01$ y $5$. El dominio de la Distribución F es $x > 0$. |

***

### 2. Cálculo de la Función de Densidad (PDF) y Estructuración de Datos

| Parámetro SciPy | Parámetro Estadístico | Significado |
| :--- | :--- | :--- |
| **`dfn`** | Grados de Libertad del **Numerador** ($d_1$) | Determina la primera forma de la distribución. |
| **`dfd`** | Grados de Libertad del **Denominador** ($d_2$) | Determina la segunda forma de la distribución. |

| Código | Descripción |
| :--- | :--- |
| `pdf_values = f.pdf(x, dfn=d1, dfd=d2)` | **Cálculo de la PDF**: Llama a la función $\mathbf{f.pdf()}$. El parámetro `dfn` (degrees of freedom numerator) es $d_1$ y `dfd` (degrees of freedom denominator) es $d_2$. |
| `label = f"({d1}, {d2})"` | **Etiquetado Temporal**: Crea una etiqueta de texto para la leyenda, como `"(2, 5)"`. |
| `pdf_long = pdf_data.melt(...)` | **Transformación a Formato Largo**: Utiliza el método `melt` de Pandas para reestructurar el DataFrame. Las densidades se funden en la columna `density`, mientras que las etiquetas de grados de libertad se agrupan en la columna `Grados de Libertad $(d_1, d_2)$`. Este formato es crucial para el trazado de múltiples líneas con Seaborn. |

***

### 3. Visualización y Estilizado del Gráfico

| Código | Descripción |
| :--- | :--- |
| `sns.lineplot(...)` | **Trazado de Múltiples Líneas**: Dibuja las cuatro curvas de densidad en un solo gráfico. El parámetro **`hue='Grados de Libertad $(d_1, d_2)$'`** utiliza las etiquetas para asignar colores distintos a cada curva y construir la leyenda. |
| `plt.title(...)`, `plt.xlabel(...)`, `plt.ylabel(...)` | **Etiquetas y Títulos**: Define el título principal y las etiquetas de los ejes. Se utiliza notación LaTeX para la leyenda y las etiquetas. |
| `plt.legend(...)` | **Configuración de Leyenda**: Coloca la leyenda en la esquina superior derecha. |

El gráfico resultante muestra curvas sesgadas positivamente (cola larga a la derecha). La forma de la distribución es muy sensible a los valores de $d_1$ y $d_2$:
* Los pares **inversos** (ej. $(2, 5)$ vs $(5, 2)$) resultan en curvas con picos en posiciones notablemente diferentes.
* A medida que los grados de libertad del denominador ($d_2$) aumentan, la curva se vuelve más **compacta** y se acerca a una Distribución Normal.

---

##**UCEMICH** 20/10/2025

## TEMA: VARIABLES ALEATORIAS CONTINUAS

20/10/2025

## Ejercicios de Variables Aleatorias Continuas (V.A.C.) - Fundamentos

### Bloque I: Función de Densidad (PDF), Momentos y Varianza (4.1 & 4.2)

**Ejercicio 1: Verificación de PDF (Constante de Normalización)**

*(Contexto: El tiempo de procesamiento ($X$, en minutos) de una transacción bancaria tiene una PDF definida por $\displaystyle f(x) = kx$ para $\displaystyle 0 \le x \le 4$, y $\displaystyle 0$ en otro caso.)*

1.  **Planteamiento/Fórmula:** Determina el valor de la constante $\displaystyle k$ que asegura que $\displaystyle f(x)$ es una PDF válida. (4.1.2)
2.  **Código/Gráfico:** Utiliza Python (ej., `scipy.integrate`) para verificar tu resultado y **graficar** la forma de la PDF.
3.  **Interpretación:** ¿Qué representa el área total bajo la curva en el contexto del tiempo de procesamiento?

**Ejercicio 2: Probabilidad por Integración**

*(Contexto: El voltaje ($X$, en voltios) de una fuente de alimentación sigue la PDF del Ejercicio 1 (con $\displaystyle k$ ya encontrado).)*

1.  **Planteamiento/Fórmula:** Calcula la probabilidad de que el voltaje esté **entre 1 y 3 voltios**, $\displaystyle P(1 < X < 3)$. (4.1.2)
2.  **Código/Gráfico:** Utiliza Python para calcular la integral definida y **graficar** la PDF, sombreando la región de la probabilidad solicitada.
3.  **Interpretación:** Si $\displaystyle P(1 < X < 3)$ fuera muy bajo, ¿qué implicación práctica tendría esto para la estabilidad de la fuente de alimentación?

**Ejercicio 3: Valor Esperado (Media)**

*(Contexto: Utiliza la variable $X$ (voltaje) del Ejercicio 2.)*

1.  **Planteamiento/Fórmula:** Calcula el **Valor Esperado** del voltaje, $\displaystyle E[X]$. (4.2.1)
2.  **Código/Gráfico:** Utiliza Python para calcular la integral de $\displaystyle E[X]$ y marca este valor en el gráfico de la PDF.
3.  **Interpretación:** ¿Cómo se interpreta el $\displaystyle E[X]$ para el ingeniero eléctrico que monitorea el voltaje promedio?

**Ejercicio 4: Varianza y Desviación Estándar**

*(Contexto: Utiliza la variable $X$ (voltaje) del Ejercicio 2.)*

1.  **Planteamiento/Fórmula:** Calcula la **Varianza** $\displaystyle \text{Var}(X)$, usando la fórmula $\displaystyle \text{Var}(X) = E[X^2] - (E[X])^2$. (4.2.3)
2.  **Código/Gráfico:** Utiliza Python para calcular el segundo momento $\displaystyle E[X^2]$ y luego la Varianza.
3.  **Interpretación:** ¿Qué indica la **Desviación Estándar** ($\sigma$) sobre la fiabilidad y dispersión del voltaje de la fuente?

**Ejercicio 5: Esperanza de una Función de $X$ (Transformación Lineal)**

*(Contexto: El beneficio ($X$, en miles de USD) de una inversión tiene la PDF $\displaystyle f(x) = \frac{3}{64}x^2$ para $\displaystyle 0 \le x \le 4$. Si el inversor decide aplicar un cargo fijo, el beneficio ajustado es $\displaystyle Y = 3X - 5$.)*

1.  **Planteamiento/Fórmula:** Calcula el **Valor Esperado** del beneficio ajustado, $\displaystyle E[Y]$, usando las propiedades de la esperanza. (4.2.1)
2.  **Código/Gráfico:** Utiliza Python para calcular $\displaystyle E[X]$ primero, y luego aplica la transformación.
3.  **Interpretación:** Explica cómo la transformación lineal afecta la media original de la inversión.

---

### Bloque II: Función de Distribución Acumulativa (CDF), Medidas de Tendencia Central (4.3 & 4.4)

**Ejercicio 6: Obtención de CDF a partir de PDF y Gráfico**

*(Contexto: La vida útil ($X$, en años) de un componente sigue la PDF $\displaystyle f(x) = \frac{1}{9}x$ para $\displaystyle 0 \le x \le 3$, y $\displaystyle f(x) = \frac{2}{3} - \frac{1}{9}x$ para $\displaystyle 3 < x \le 6$.)*

1.  **Planteamiento/Fórmula:** Determina la **Función de Distribución Acumulativa (CDF)**, $\displaystyle F(x)$, para todos los intervalos, particularmente para $\displaystyle x \in (3, 6]$. (4.3.1)
2.  **Código/Gráfico:** Utiliza Python para **graficar** la PDF $\displaystyle f(x)$ y su correspondiente CDF $\displaystyle F(x)$ en dos gráficos adyacentes.
3.  **Interpretación:** ¿Qué representa el punto donde las funciones se "doblan" (en $\displaystyle x=3$)?

**Ejercicio 7: Recuperación de PDF a partir de CDF**

*(Contexto: La CDF del tiempo de respuesta ($T$, en segundos) de un servidor es $\displaystyle F(t) = 1 - e^{-2t}$ para $\displaystyle t \ge 0$.)*

1.  **Planteamiento/Fórmula:** Recupera la **Función de Densidad de Probabilidad (PDF)**, $\displaystyle f(t)$, mediante la diferenciación de $\displaystyle F(t)$. (4.3.3)
2.  **Código/Gráfico:** **Grafica** la CDF $\displaystyle F(t)$ y la PDF $\displaystyle f(t)$.
3.  **Interpretación:** ¿Qué significado tiene que la pendiente de la CDF sea cero al inicio ($t=0$)?

**Ejercicio 8: Cálculo de la Mediana**

*(Contexto: Utiliza la PDF del beneficio $X$ (en miles de USD) del Ejercicio 5: $\displaystyle f(x) = \frac{3}{64}x^2$ para $\displaystyle 0 \le x \le 4$.)*

1.  **Planteamiento/Fórmula:** Calcula la **Mediana** de $\displaystyle X$, $\displaystyle m$, resolviendo la ecuación $\displaystyle F(m) = 0.5$. (4.4.1)
2.  **Código/Gráfico:** Marca la Mediana ($\displaystyle m$) y la Media ($\displaystyle E[X]$) en tu gráfico de la PDF.
3.  **Interpretación:** ¿Cómo se interpreta el valor de la Mediana para el inversor? (Pista: el 50% de las veces, el beneficio será menor o igual a este valor).

**Ejercicio 9: Cálculo de la Moda**

*(Contexto: Utiliza la PDF de la vida útil del componente del Ejercicio 6.)*

1.  **Planteamiento/Fórmula:** Calcula la **Moda** de $\displaystyle X$ encontrando el valor de $x$ que maximiza la PDF. (4.4.2)
2.  **Código/Gráfico:** Señala la Moda en el gráfico de la PDF.
3.  **Interpretación:** ¿Cuál es la "vida útil" más probable para el componente, y qué implicación tiene esto para la planificación del mantenimiento?

**Ejercicio 10: Propiedades de la CDF y Probabilidades**

*(Contexto: La resistencia de un cable (R, en Ohmios) tiene una CDF $\displaystyle F(r)$. Sabemos que $\displaystyle F(5) = 0.15$ y $\displaystyle F(10) = 0.85$.)*

1.  **Planteamiento/Fórmula:** Utiliza las propiedades de la CDF para calcular $\displaystyle P(R > 10)$ y $\displaystyle P(5 < R \le 10)$. (4.3.2)
2.  **Código/Gráfico:** (Conceptual) Esboza una posible forma de la CDF y explica cómo se obtienen las probabilidades en ella.
3.  **Interpretación:** Si $\displaystyle P(5 < R \le 10)$ representa el rango de resistencia aceptable, ¿qué porcentaje de cables cumplen con la especificación?

---

### Bloque III: Distribuciones Típicas (Uniforme, Exponencial, Gaussiana) (4.5 & 4.6)

**Ejercicio 11: Distribución Uniforme (Error de Medición)**

*(Contexto: El error de redondeo ($X$) en una medición sigue una distribución Uniforme en el intervalo $\displaystyle [-0.05, 0.05]$ metros.)*

1.  **Planteamiento/Fórmula:** Calcula la **Media** $\displaystyle E[X]$ y la **PDF** $\displaystyle f(x)$. (4.5.1)
2.  **Código/Gráfico:** Utiliza Python (`scipy.stats.uniform`) para calcular la probabilidad de que el error sea **menor a 0.02 metros** ($\displaystyle P(X < 0.02)$) y **grafica** la PDF.
3.  **Interpretación:** ¿Por qué es la Media ($\displaystyle E[X]$) igual a cero en este contexto, y qué significa esto para la precisión de la medición?

**Ejercicio 12: Distribución Exponencial (Tiempo de Espera)**

*(Contexto: El tiempo de espera ($T$, en minutos) en una línea de producción sigue una distribución Exponencial con una tasa media $\displaystyle \lambda = 0.4$ esperas por minuto.)*

1.  **Planteamiento/Fórmula:** Calcula la probabilidad de que la espera sea **mayor a 10 minutos** ($\displaystyle P(T > 10)$). (4.5.2)
2.  **Código/Gráfico:** Utiliza Python (`scipy.stats.expon.sf`) para calcular la probabilidad y **graficar** la PDF, marcando el área de interés.
3.  **Interpretación:** Si la media de espera es $\displaystyle E[T]$, explica por qué $\displaystyle P(T > E[T])$ no es igual a 0.5 en la distribución Exponencial.

**Ejercicio 13: Distribución Gaussiana General (Calificación de Proyectos)**

*(Contexto: Las calificaciones de un proyecto ($X$) siguen una distribución Normal con $\displaystyle \mu=75$ y $\displaystyle \sigma=8$.)*

1.  **Planteamiento/Fórmula:** Calcula la probabilidad de que una calificación esté **entre 65 y 90** ($\displaystyle P(65 < X < 90)$), estandarizando los valores. (4.6.1)
2.  **Código/Gráfico:** Utiliza Python (`scipy.stats.norm`) para calcular la probabilidad y **graficar** la Normal, sombreando la región de interés.
3.  **Interpretación:** Si la calificación de aprobación es 60, ¿cuál es el porcentaje de estudiantes que aprueban el proyecto?

**Ejercicio 14: Distribución Gaussiana Estándar (Cálculo de Percentiles)**

*(Contexto: Se utiliza la distribución $\displaystyle Z \sim N(0, 1)$ para definir los niveles de riesgo en un análisis financiero.)*

1.  **Planteamiento/Fórmula:** Calcula el **Percentil 95** ($\displaystyle z_{0.95}$), el valor tal que $\displaystyle P(Z \le z_{0.95}) = 0.95$. (4.6.2)
2.  **Código/Gráfico:** Utiliza Python (`scipy.stats.norm.ppf`) para calcular el valor y **grafica** la Normal Estándar marcando este punto crítico.
3.  **Interpretación:** ¿Qué representa este valor ($z_{0.95}$) en el contexto de la "cola" de la distribución de riesgo?

**Ejercicio 15: Función de Variables Aleatorias (Transformación No Lineal)**

*(Contexto: La temperatura de un reactor ($X$, en °C) sigue una Uniforme en $\displaystyle [0, 100]$. La energía generada es $\displaystyle Y = g(X) = X^2$.)*

1.  **Planteamiento/Fórmula:** Calcula la **Media** de la energía generada, $\displaystyle E[Y] = E[X^2]$. (4.7.1)
2.  **Código/Gráfico:** Utiliza Python para calcular la integral de $\displaystyle E[Y]$. **Grafica** la PDF de $X$. (Opcional avanzado: intenta derivar y graficar la PDF de $Y$).
3.  **Interpretación:** ¿Por qué $\displaystyle E[Y]$ **no es** igual a $(E[X])^2$? Explica la diferencia en términos de la distribución de la energía.

## 1

## Ejercicio 1: Verificación de PDF

## 1. Planteamiento/Fórmula

Para que $ f(x) = kx $ sea una función de densidad de probabilidad válida en el intervalo $[0,4]$, debe cumplir dos condiciones:

1. $ f(x) \geq 0 $ para todo $ x $
2. El área total bajo la curva debe ser igual a 1

La segunda condición se expresa como:
$
\int_{0}^{4} f(x) \, dx = 1
$

Sustituyendo $ f(x) = kx $:
$
\int_{0}^{4} kx \, dx = 1
$

Resolviendo la integral:
$
k \int_{0}^{4} x \, dx = k \left[\frac{x^2}{2}\right]_{0}^{4} = k \left(\frac{16}{2} - 0\right) = 8k = 1
$

Despejando $ k $:
$
k = \frac{1}{8}
$

**Por lo tanto, la PDF válida es:** $ f(x) = \frac{x}{8} $ para $ 0 \le x \le 4 $

## 2. Interpretación

El área total bajo la curva de la PDF, que es exactamente igual a 1, representa:

- **La probabilidad total**: La certeza de que el tiempo de procesamiento de una transacción bancaria estará dentro del rango posible [0,4] minutos
- **Normalización**: Garantiza que todas las probabilidades calculadas posteriormente serán válidas y sumarán 1
- **Contexto práctico**: Confirma que el modelo matemático describe completamente el comportamiento del tiempo de procesamiento

**La constante $ k = \frac{1}{8} $ asegura que la función esté correctamente normalizada y pueda ser utilizada para calcular probabilidades válidas.**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

## Definir la PDF con k = 1/8
def pdf(x):
    return x/8

## Verificar que la integral desde 0 a 4 es igual a 1
integral, error = integrate.quad(pdf, 0, 4)
print(f"La integral de 0 a 4 es: {integral:.6f}")
print(f"Error de integración: {error:.2e}")

## Crear array para graficar
x = np.linspace(-1, 5, 1000)
y = np.piecewise(x, [x < 0, (x >= 0) & (x <= 4), x > 4], [0, pdf, 0])

## Graficar la PDF
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='PDF: f(x) = x/8')
plt.fill_between(x, y, alpha=0.3, color='blue')
plt.title('Función de Densidad de Probabilidad (PDF)')
plt.xlabel('Tiempo de procesamiento (minutos)')
plt.ylabel('f(x)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(bottom=0)
plt.show()
```

## 2

## Ejercicio 2: Probabilidad por Integración

## 1. Planteamiento/Fórmula

Usando la PDF del Ejercicio 1: $ f(x) = \frac{x}{8} $ para $ 0 \le x \le 4 $

Queremos calcular $ P(1 < X < 3) $, que corresponde al área bajo la curva entre x=1 y x=3:

$
P(1 < X < 3) = \int_{1}^{3} f(x) \, dx = \int_{1}^{3} \frac{x}{8} \, dx
$

Resolviendo la integral:
$
P(1 < X < 3) = \frac{1}{8} \int_{1}^{3} x \, dx = \frac{1}{8} \left[\frac{x^2}{2}\right]_{1}^{3}
$

$
= \frac{1}{8} \left(\frac{9}{2} - \frac{1}{2}\right) = \frac{1}{8} \times \frac{8}{2} = \frac{1}{8} \times 4 = 0.5
$

**Resultado:** $ P(1 < X < 3) = 0.5 $

## 3. Interpretación

**Significado práctico:** $ P(1 < X < 3) = 0.5 $ significa que hay un 50% de probabilidad de que el voltaje esté entre 1 y 3 voltios.

**Implicaciones si fuera muy bajo:**

- **Inestabilidad del sistema**: Un valor bajo indicaría que el voltaje rara vez se mantiene en el rango deseado
- **Problemas de calidad**: Sugeriría fluctuaciones extremas frecuentes
- **Riesgo operacional**: Los equipos conectados podrían sufrir daños por voltajes fuera de rango
- **Necesidad de mantenimiento**: Indicaría que la fuente de alimentación requiere reparación o reemplazo

**En este caso específico:** Con 50% de probabilidad, la fuente tiene una estabilidad moderada, pero idealmente se buscaría una probabilidad más alta en el rango operativo óptimo.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

## Definir la PDF
def pdf(x):
    return x/8

## Calcular probabilidad P(1 < X < 3)
prob, error = integrate.quad(pdf, 1, 3)
print(f"P(1 < X < 3) = {prob:.4f}")
print(f"Esto representa un {prob*100:.1f}% de probabilidad")

## Crear arrays para graficar
x = np.linspace(-1, 5, 1000)
y = np.piecewise(x, [x < 0, (x >= 0) & (x <= 4), x > 4], [0, pdf, 0])

## Graficar con región sombreada
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='PDF: f(x) = x/8')

## Sombrear región de interés (1 < X < 3)
x_region = np.linspace(1, 3, 100)
y_region = pdf(x_region)
plt.fill_between(x_region, y_region, alpha=0.5, color='red',
                 label=f'P(1 < X < 3) = {prob:.3f}')

## Configuraciones del gráfico
plt.title('Probabilidad P(1 < X < 3) - Voltaje entre 1 y 3 voltios')
plt.xlabel('Voltaje (voltios)')
plt.ylabel('f(x)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(bottom=0)
plt.show()

## Verificación adicional
print(f"\nVerificación manual: (3² - 1²)/(2×8) = {(9-1)/16} = {8/16}")
```

## 3

## Ejercicio 3: Valor Esperado (Media)

## 1. Planteamiento/Fórmula

Usando la PDF del Ejercicio 1: $ f(x) = \frac{x}{8} $ para $ 0 \le x \le 4 $

El valor esperado (media) se calcula como:
$
E[X] = \int_{-\infty}^{\infty} x \cdot f(x) \, dx
$

Para nuestra PDF específica:
$
E[X] = \int_{0}^{4} x \cdot \frac{x}{8} \, dx = \frac{1}{8} \int_{0}^{4} x^2 \, dx
$

Resolviendo la integral:
$
E[X] = \frac{1}{8} \left[\frac{x^3}{3}\right]_{0}^{4} = \frac{1}{8} \left(\frac{64}{3} - 0\right) = \frac{64}{24} = \frac{8}{3} \approx 2.667
$

**Resultado:** $ E[X] = \frac{8}{3} \approx 2.667 $ voltios

## 2. Interpretación

**Para el ingeniero eléctrico que monitorea el voltaje promedio:**

- **Valor de referencia**: $ E[X] = 2.667 $ voltios representa el voltaje promedio esperado a largo plazo
- **Centro de la distribución**: Es el valor alrededor del cual se centran las mediciones de voltaje
- **Tendencia central**: Indica el comportamiento típico de la fuente de alimentación
- **Toma de decisiones**:
  - Si el valor esperado está dentro de las especificaciones del equipo, la fuente es adecuada
  - Si se desvía significativamente del valor nominal, puede indicar problemas
  - Sirve como base para comparar diferentes fuentes de alimentación

**En contexto práctico:** El ingeniero esperaría que, en promedio, la fuente proporcione aproximadamente 2.667 voltios, lo que ayuda a determinar si cumple con los requisitos del sistema eléctrico.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

## Definir la PDF
def pdf(x):
    return x/8

## Calcular E[X] - Valor Esperado
def x_times_pdf(x):
    return x * pdf(x)

E_X, error = integrate.quad(x_times_pdf, 0, 4)
print(f"E[X] = {E_X:.4f} voltios")
print(f"En forma fraccionaria: 8/3 = {8/3:.4f}")

## Crear arrays para graficar
x = np.linspace(-1, 5, 1000)
y = np.piecewise(x, [x < 0, (x >= 0) & (x <= 4), x > 4], [0, pdf, 0])

## Graficar con marca del valor esperado
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='PDF: f(x) = x/8')

## Marcar el valor esperado
plt.axvline(E_X, color='red', linestyle='--', linewidth=2,
            label=f'E[X] = {E_X:.3f} voltios')

## Destacar el área que contribuye al valor esperado
x_area = np.linspace(0, 4, 100)
y_area = x_times_pdf(x_area)
plt.fill_between(x_area, y_area, alpha=0.3, color='green',
                 label='x·f(x) para E[X]')

plt.title('Valor Esperado E[X] del Voltaje')
plt.xlabel('Voltaje (voltios)')
plt.ylabel('f(x)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(bottom=0)
plt.show()

## Verificación adicional
print(f"\nVerificación manual:")
print(f"∫x·f(x)dx de 0 a 4 = ∫x²/8 dx de 0 a 4")
print(f"= [x³/24] de 0 a 4 = 64/24 = 8/3 = {8/3:.4f}")
```

## 4

## Ejercicio 4: Varianza y Desviación Estándar

## 1. Planteamiento/Fórmula

Usando la PDF: $ f(x) = \frac{x}{8} $ para $ 0 \le x \le 4 $

Del Ejercicio 3 sabemos: $ E[X] = \frac{8}{3} $

**Fórmula de la varianza:**
$
\text{Var}(X) = E[X^2] - (E[X])^2
$

**Paso 1: Calcular $ E[X^2] $**
$
E[X^2] = \int_{0}^{4} x^2 \cdot f(x) \, dx = \int_{0}^{4} x^2 \cdot \frac{x}{8} \, dx = \frac{1}{8} \int_{0}^{4} x^3 \, dx
$

$
E[X^2] = \frac{1}{8} \left[\frac{x^4}{4}\right]_{0}^{4} = \frac{1}{8} \left(\frac{256}{4} - 0\right) = \frac{1}{8} \times 64 = 8
$

**Paso 2: Calcular la varianza**
$
\text{Var}(X) = E[X^2] - (E[X])^2 = 8 - \left(\frac{8}{3}\right)^2 = 8 - \frac{64}{9} = \frac{72}{9} - \frac{64}{9} = \frac{8}{9} \approx 0.8889
$

**Paso 3: Calcular la desviación estándar**
$
\sigma = \sqrt{\text{Var}(X)} = \sqrt{\frac{8}{9}} = \frac{\sqrt{8}}{3} = \frac{2\sqrt{2}}{3} \approx 0.9428
$

**Resultados:**
- $ E[X^2] = 8 $
- $ \text{Var}(X) = \frac{8}{9} \approx 0.8889 $
- $ \sigma \approx 0.9428 $ voltios

## 2. Interpretación

**Significado de la desviación estándar $ \sigma \approx 0.943 $ voltios:**

- **Dispersión típica**: Indica cuánto se desvían típicamente los voltajes del valor promedio de 2.667 voltios
- **Medida de fiabilidad**: Un valor menor indicaría mayor consistencia y estabilidad del voltaje
- **Rango de operación normal**: Aproximadamente el 68% de las mediciones estarán entre $ 2.667 \pm 0.943 $ voltios, es decir, entre 1.724 y 3.610 voltios

**Implicaciones prácticas:**
- **Fiabilidad moderada**: La desviación de 0.943 voltios sugiere variaciones significativas alrededor del valor medio
- **Estabilidad**: Indica que la fuente tiene fluctuaciones considerables en su voltaje de salida
- **Riesgo operacional**: Los equipos sensibles podrían verse afectados por estas variaciones
- **Necesidad de regulación**: Podría requerir circuitos estabilizadores adicionales para aplicaciones críticas

**En contexto**: Una desviación estándar que representa aproximadamente el 35% del valor medio sugiere una variabilidad relativamente alta en el voltaje de salida.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

## Definir la PDF
def pdf(x):
    return x/8

## Calcular E[X] (ya conocido)
def x_times_pdf(x):
    return x * pdf(x)

E_X, _ = integrate.quad(x_times_pdf, 0, 4)

## Calcular E[X^2]
def x_squared_times_pdf(x):
    return (x**2) * pdf(x)

E_X2, error = integrate.quad(x_squared_times_pdf, 0, 4)

## Calcular varianza y desviación estándar
var_X = E_X2 - E_X**2
std_X = np.sqrt(var_X)

print(f"E[X] = {E_X:.4f} voltios")
print(f"E[X²] = {E_X2:.4f}")
print(f"Var(X) = E[X²] - (E[X])² = {E_X2:.4f} - ({E_X:.4f})² = {var_X:.4f}")
print(f"Desviación estándar σ = √{var_X:.4f} = {std_X:.4f} voltios")

## Graficar distribución con media ± desviación estándar
x = np.linspace(-1, 5, 1000)
y = np.piecewise(x, [x < 0, (x >= 0) & (x <= 4), x > 4], [0, pdf, 0])

plt.figure(figsize=(12, 6))

## Gráfico principal
plt.plot(x, y, 'b-', linewidth=2, label='PDF: f(x) = x/8')

## Marcar la media
plt.axvline(E_X, color='red', linestyle='--', linewidth=2,
            label=f'E[X] = {E_X:.3f} voltios')

## Marcar intervalo E[X] ± σ
plt.axvline(E_X - std_X, color='orange', linestyle=':', linewidth=2,
            label=f'E[X] ± σ = [{E_X-std_X:.3f}, {E_X+std_X:.3f}]')
plt.axvline(E_X + std_X, color='orange', linestyle=':', linewidth=2)

## Sombrear región dentro de ±1σ
x_1sigma = np.linspace(max(0, E_X - std_X), min(4, E_X + std_X), 100)
y_1sigma = pdf(x_1sigma)
plt.fill_between(x_1sigma, y_1sigma, alpha=0.3, color='orange',
                 label=f'Región E[X] ± σ')

plt.title('Distribución con Media y Desviación Estándar')
plt.xlabel('Voltaje (voltios)')
plt.ylabel('f(x)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(bottom=0)

plt.tight_layout()
plt.show()

## Información adicional
print(f"\n--- Información Adicional ---")
print(f"Coeficiente de variación: {std_X/E_X*100:.2f}%")
print(f"Rango E[X] ± σ: [{E_X-std_X:.3f}, {E_X+std_X:.3f}] voltios")
print(f"Rango total posible: [0, 4] voltios")
```

## 5

## Ejercicio 5: Esperanza de una Función de X (Transformación Lineal)

## 1. Planteamiento/Fórmula

**Datos:**
- PDF: $ f(x) = \frac{3}{64}x^2 $ para $ 0 \le x \le 4 $
- Transformación: $ Y = 3X - 5 $
- Queremos: $ E[Y] $

**Paso 1: Verificar que es PDF válida**
$
\int_{0}^{4} \frac{3}{64}x^2 \, dx = \frac{3}{64} \left[\frac{x^3}{3}\right]_{0}^{4} = \frac{3}{64} \times \frac{64}{3} = 1 \quad \checkmark
$

**Paso 2: Calcular $ E[X] $**
$
E[X] = \int_{0}^{4} x \cdot \frac{3}{64}x^2 \, dx = \frac{3}{64} \int_{0}^{4} x^3 \, dx
$
$
E[X] = \frac{3}{64} \left[\frac{x^4}{4}\right]_{0}^{4} = \frac{3}{64} \times \frac{256}{4} = \frac{3}{64} \times 64 = 3
$

**Paso 3: Aplicar propiedad de linealidad de la esperanza**
$
E[Y] = E[3X - 5] = 3E[X] - 5 = 3 \times 3 - 5 = 9 - 5 = 4
$

**Resultados:**
- $ E[X] = 3 $ miles de USD
- $ E[Y] = 4 $ miles de USD

## 3. Interpretación

**Efecto de la transformación lineal $ Y = 3X - 5 $:**

- **Escalamiento (×3)**: Multiplica el beneficio bruto por 3
  - $ E[X] = 3 \rightarrow 3E[X] = 9 $
  - Representa una amplificación o crecimiento del negocio

- **Cargo fijo (-5)**: Resta 5 miles de USD
  - $ 9 - 5 = 4 $
  - Representa costos fijos, impuestos, o cargos operativos

**Análisis del resultado:**
- **Beneficio neto positivo**: $ E[Y] = 4 > 0 $ indica que, en promedio, la inversión es rentable
- **Margen de seguridad**: Hay un colchón de 4,000 USD sobre el punto de equilibrio
- **Impacto del cargo fijo**: Aunque el beneficio bruto esperado es 9,000 USD, los costos reducen el neto a 4,000 USD

**Implicaciones prácticas:**
- La inversión sigue siendo viable a pesar del cargo fijo
- El negocio genera suficiente beneficio bruto para absorber los costos fijos
- El inversor puede esperar un retorno neto promedio de 4,000 USD

**Conclusión:** La transformación lineal preserva la linealidad de la esperanza, permitiendo calcular fácilmente el efecto de cambios escalares y traslaciones en el valor esperado.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

## Definir la PDF del beneficio
def pdf_beneficio(x):
    return (3/64) * x**2

## Verificar que es PDF válida
integral_verif, _ = integrate.quad(pdf_beneficio, 0, 4)
print(f"Verificación PDF: ∫f(x)dx de 0 a 4 = {integral_verif:.6f}")

## Calcular E[X]
def x_times_pdf_beneficio(x):
    return x * pdf_beneficio(x)

E_X_beneficio, _ = integrate.quad(x_times_pdf_beneficio, 0, 4)

## Calcular E[Y] usando propiedad de linealidad
E_Y = 3 * E_X_beneficio - 5

print(f"\n--- Resultados ---")
print(f"E[X] = {E_X_beneficio:.4f} miles de USD")
print(f"E[Y] = E[3X - 5] = 3 × {E_X_beneficio:.1f} - 5 = {E_Y:.1f} miles de USD")

## Graficar ambas distribuciones conceptualmente
x_beneficio = np.linspace(0, 4, 100)
y_beneficio = pdf_beneficio(x_beneficio)

plt.figure(figsize=(12, 6))

## Gráfico 1: Distribución original X
plt.subplot(1, 2, 1)
plt.plot(x_beneficio, y_beneficio, 'g-', linewidth=2, label='f(x) = (3/64)x²')
plt.axvline(E_X_beneficio, color='red', linestyle='--', linewidth=2,
            label=f'E[X] = {E_X_beneficio:.1f}')
plt.fill_between(x_beneficio, y_beneficio, alpha=0.3, color='green')
plt.title('Distribución Original X\n(Beneficio Bruto)')
plt.xlabel('X (miles USD)')
plt.ylabel('f(x)')
plt.grid(True, alpha=0.3)
plt.legend()

## Gráfico 2: Valor esperado transformado
plt.subplot(1, 2, 2)
## Crear una representación conceptual de Y
y_values = [E_Y]
plt.axvline(E_Y, color='blue', linestyle='--', linewidth=3,
            label=f'E[Y] = {E_Y:.1f} miles USD')
plt.scatter([E_Y], [0.1], color='blue', s=100, zorder=5)

## Anotaciones explicativas
plt.text(E_Y, 0.15, 'Transformación:\nY = 3X - 5',
         ha='center', va='bottom', fontsize=10,
         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue"))

plt.title('Valor Esperado Transformado\nE[Y] = E[3X - 5]')
plt.xlabel('Y (miles USD)')
plt.ylabel('Valor Esperado')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(0, 0.2)
plt.xlim(0, 10)

plt.tight_layout()
plt.show()

## Cálculo directo alternativo para verificación
print(f"\n--- Verificación Alternativa ---")
print(f"Cálculo directo de E[Y]:")
def y_pdf(x):
    return (3*x - 5) * pdf_beneficio(x)

E_Y_direct, _ = integrate.quad(y_pdf, 0, 4)
print(f"E[Y] = ∫(3x-5)·f(x)dx = {E_Y_direct:.4f} miles USD")
```

## 6

## Ejercicio 6: Obtención de CDF a partir de PDF y Gráfico

## 1. Planteamiento/Fórmula

**PDF dada:**
- $ f(x) = \frac{1}{9}x $ para $ 0 \le x \le 3 $
- $ f(x) = \frac{2}{3} - \frac{1}{9}x $ para $ 3 < x \le 6 $

**Para $ 0 \le x \le 3 $:**
$
F(x) = \int_{0}^{x} \frac{1}{9}t \, dt = \frac{1}{9} \left[\frac{t^2}{2}\right]_{0}^{x} = \frac{x^2}{18}
$
En $ x = 3 $: $ F(3) = \frac{9}{18} = 0.5 $

**Para $ 3 < x \le 6 $:**
$
F(x) = F(3) + \int_{3}^{x} \left(\frac{2}{3} - \frac{1}{9}t\right) dt = 0.5 + \left[\frac{2}{3}t - \frac{1}{18}t^2\right]_{3}^{x}
$
$
= 0.5 + \left(\frac{2}{3}x - \frac{1}{18}x^2\right) - \left(2 - \frac{1}{2}\right) = \frac{2}{3}x - \frac{1}{18}x^2 - 1
$

**CDF completa:**
$
F(x) = \begin{cases}
0 & x < 0 \\
\frac{x^2}{18} & 0 \le x \le 3 \\
\frac{2}{3}x - \frac{1}{18}x^2 - 1 & 3 < x \le 6 \\
1 & x > 6
\end{cases}
$

## 3. Interpretación

**El punto x = 3 representa:**
- **Cambio en el patrón de desgaste**: La tasa de falla cambia en este punto
- **Punto de inflexión**: Donde la PDF alcanza su máximo y comienza a decrecer
- **Mediana de la distribución**: F(3) = 0.5 indica que el 50% de los componentes fallan antes de los 3 años
- **Transición operacional**: Posiblemente marca el fin de la vida útil "óptima" y el inicio del desgaste acelerado

```python
import numpy as np
import matplotlib.pyplot as plt

## Definir PDF
def pdf(x):
    if x < 0:
        return 0
    elif x <= 3:
        return (1/9) * x
    elif x <= 6:
        return (2/3) - (1/9) * x
    else:
        return 0

## Definir CDF
def cdf(x):
    if x < 0:
        return 0
    elif x <= 3:
        return (x**2) / 18
    elif x <= 6:
        return (2/3)*x - (1/18)*x**2 - 1
    else:
        return 1

## Crear arrays
x = np.linspace(-1, 7, 1000)
y_pdf = [pdf(xi) for xi in x]
y_cdf = [cdf(xi) for xi in x]

## Graficar
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

## PDF
ax1.plot(x, y_pdf, 'b-', linewidth=2, label='PDF')
ax1.axvline(3, color='red', linestyle='--', alpha=0.7, label='x = 3 (punto de inflexión)')
ax1.set_title('Función de Densidad de Probabilidad (PDF)')
ax1.set_xlabel('Vida útil (años)')
ax1.set_ylabel('f(x)')
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.set_ylim(bottom=0)

## CDF
ax2.plot(x, y_cdf, 'r-', linewidth=2, label='CDF')
ax2.axvline(3, color='red', linestyle='--', alpha=0.7, label='x = 3')
ax2.axhline(0.5, color='green', linestyle=':', alpha=0.7, label='F(3) = 0.5')
ax2.set_title('Función de Distribución Acumulativa (CDF)')
ax2.set_xlabel('Vida útil (años)')
ax2.set_ylabel('F(x)')
ax2.grid(True, alpha=0.3)
ax2.legend()
ax2.set_ylim(0, 1)

plt.tight_layout()
plt.show()

## Verificación en puntos clave
print("Verificación de la CDF:")
print(f"F(0) = {cdf(0):.4f}")
print(f"F(3) = {cdf(3):.4f}")
print(f"F(6) = {cdf(6):.4f}")
```

## 7

## Ejercicio 7: Recuperación de PDF a partir de CDF

## 1. Planteamiento/Fórmula

**CDF dada:** $ F(t) = 1 - e^{-2t} $ para $ t \ge 0 $

**Diferenciación para obtener PDF:**
$
f(t) = \frac{d}{dt}F(t) = \frac{d}{dt}(1 - e^{-2t}) = 0 - (-2e^{-2t}) = 2e^{-2t}
$

**PDF resultante:** $ f(t) = 2e^{-2t} $ para $ t \ge 0 $

## 3. Interpretación

**La pendiente cero de la CDF en t=0 significa:**
- **Probabilidad instantánea cero**: La probabilidad de que el tiempo de respuesta sea exactamente 0 es cero
- **Comportamiento suave**: El sistema no puede responder instantáneamente
- **Distribución continua**: Confirma que estamos trabajando con una variable aleatoria continua
- **Tiempo mínimo realista**: Refleja que siempre hay algún retardo, por pequeño que sea, en la respuesta del servidor

```python
import numpy as np
import matplotlib.pyplot as plt

## Definir CDF y PDF
def cdf(t):
    return 1 - np.exp(-2*t)

def pdf(t):
    return 2 * np.exp(-2*t)

## Crear arrays
t = np.linspace(0, 3, 1000)
y_cdf = cdf(t)
y_pdf = pdf(t)

## Graficar
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

## CDF
ax1.plot(t, y_cdf, 'r-', linewidth=2, label='F(t) = 1 - e⁻²ᵗ')
ax1.set_title('Función de Distribución Acumulativa (CDF)')
ax1.set_xlabel('Tiempo de respuesta (segundos)')
ax1.set_ylabel('F(t)')
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.set_ylim(0, 1)

## PDF
ax2.plot(t, y_pdf, 'b-', linewidth=2, label='f(t) = 2e⁻²ᵗ')
ax2.set_title('Función de Densidad de Probabilidad (PDF)')
ax2.set_xlabel('Tiempo de respuesta (segundos)')
ax2.set_ylabel('f(t)')
ax2.grid(True, alpha=0.3)
ax2.legend()
ax2.set_ylim(bottom=0)

plt.tight_layout()
plt.show()

## Análisis de la pendiente en t=0
print("Análisis de la pendiente en t=0:")
print(f"f(0) = {pdf(0):.4f}")
print(f"Pendiente de F(t) en t=0: {pdf(0):.4f}")
```

## 8

## Ejercicio 8: Cálculo de la Mediana

## 1. Planteamiento/Fórmula

**PDF:** $ f(x) = \frac{3}{64}x^2 $ para $ 0 \le x \le 4 $

**Primero encontramos la CDF:**
$
F(x) = \int_{0}^{x} \frac{3}{64}t^2 \, dt = \frac{3}{64} \left[\frac{t^3}{3}\right]_{0}^{x} = \frac{x^3}{64}
$

**Resolvemos F(m) = 0.5 para la mediana:**
$
\frac{m^3}{64} = 0.5 \implies m^3 = 32 \implies m = \sqrt[3]{32} = 2\sqrt[3]{4} \approx 3.1748
$

**Del Ejercicio 5:** $ E[X] = 3 $

## 3. Interpretación

**Para el inversor, la mediana de 3.175 miles USD significa:**
- **Punto de referencia robusto**: El 50% de las inversiones generarán beneficios menores o iguales a 3,175 USD
- **Medida resistente a valores extremos**: A diferencia de la media, no se ve afectada por beneficios excepcionalmente altos o bajos
- **Expectativa realista**: Proporciona una visión más conservadora del rendimiento esperado
- **Toma de decisiones**: Si el inversor requiere un beneficio mínimo, la mediana indica la probabilidad de alcanzarlo

```python
import numpy as np
import matplotlib.pyplot as plt

## Definir PDF
def pdf(x):
    return (3/64) * x**2

## Definir CDF
def cdf(x):
    return (x**3) / 64

## Calcular mediana y media
median = (32)**(1/3)
mean = 3  # Del Ejercicio 5

## Crear arrays
x = np.linspace(0, 4, 1000)
y_pdf = pdf(x)

## Graficar
plt.figure(figsize=(10, 6))
plt.plot(x, y_pdf, 'g-', linewidth=2, label='f(x) = (3/64)x²')

## Marcar mediana y media
plt.axvline(median, color='red', linestyle='--', linewidth=2,
            label=f'Mediana = {median:.3f}')
plt.axvline(mean, color='blue', linestyle=':', linewidth=2,
            label=f'Media E[X] = {mean:.1f}')

plt.title('PDF del Beneficio con Mediana y Media')
plt.xlabel('Beneficio (miles USD)')
plt.ylabel('f(x)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(bottom=0)

plt.show()

print(f"Resultados:")
print(f"Mediana m = ³√32 = {median:.4f} miles USD")
print(f"Media E[X] = {mean:.1f} miles USD")
print(f"Verificación: F({median:.4f}) = {cdf(median):.4f} ≈ 0.5")
```

## 9

## Ejercicio 9: Cálculo de la Moda

## 1. Planteamiento/Fórmula

**PDF del Ejercicio 6:**
- $ f(x) = \frac{1}{9}x $ para $ 0 \le x \le 3 $ (creciente)
- $ f(x) = \frac{2}{3} - \frac{1}{9}x $ para $ 3 < x \le 6 $ (decreciente)

**Análisis:**
- En [0,3]: La función es creciente → máximo en x = 3, f(3) = 1/3
- En (3,6]: La función es decreciente → máximo en x = 3⁺, pero en x = 3 es mayor

**Moda:** x = 3 (valor donde la PDF alcanza su máximo)

## 3. Interpretación

**La moda en x = 3 años indica:**
- **Vida útil más probable**: El componente tiene mayor probabilidad de fallar alrededor de los 3 años
- **Planificación de mantenimiento**:
  - Se deben programar revisiones preventivas antes de los 3 años
  - El riesgo de falla aumenta significativamente al acercarse a los 3 años
  - Considerar reemplazo preventivo alrededor de los 2.5-3 años
- **Gestión de inventario**: Mantener stock de repuestos sincronizado con este patrón de falla

```python
import numpy as np
import matplotlib.pyplot as plt

## Definir PDF del Ejercicio 6
def pdf(x):
    if x < 0:
        return 0
    elif x <= 3:
        return (1/9) * x
    elif x <= 6:
        return (2/3) - (1/9) * x
    else:
        return 0

## Crear arrays
x = np.linspace(0, 6, 1000)
y_pdf = [pdf(xi) for xi in x]

## Encontrar moda (máximo de PDF)
mode = 3
max_pdf = pdf(mode)

## Graficar
plt.figure(figsize=(10, 6))
plt.plot(x, y_pdf, 'b-', linewidth=2, label='PDF')

## Marcar moda
plt.axvline(mode, color='red', linestyle='--', linewidth=2,
            label=f'Moda = {mode} años')
plt.plot(mode, max_pdf, 'ro', markersize=8, label=f'f({mode}) = {max_pdf:.3f}')

plt.title('PDF de la Vida Útil con Moda')
plt.xlabel('Vida útil (años)')
plt.ylabel('f(x)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(bottom=0)

plt.show()

print(f"Resultados:")
print(f"Moda = {mode} años")
print(f"Valor máximo de PDF: f({mode}) = {max_pdf:.4f}")
```

## 10

## Ejercicio 10: Propiedades de la CDF y Probabilidades

## 1. Planteamiento/Fórmula

**Datos:**
- $ F(5) = 0.15 $
- $ F(10) = 0.85 $

**Cálculo de probabilidades:**

$
P(R > 10) = 1 - P(R \le 10) = 1 - F(10) = 1 - 0.85 = 0.15
$

$
P(5 < R \le 10) = F(10) - F(5) = 0.85 - 0.15 = 0.70
$

## 3. Interpretación

**El 70% de los cables cumplen con la especificación (5 < R ≤ 10 Ohmios):**

- **Alta tasa de aceptación**: 70% es un porcentaje bueno pero mejorable
- **15% de cables defectuosos por baja resistencia**: R ≤ 5 Ohmios
- **15% de cables fuera de especificación por alta resistencia**: R > 10 Ohmios
- **Implicaciones de calidad**:
  - Se podría mejorar el proceso de fabricación para reducir el 30% de cables no conformes
  - El rango aceptable está bien centrado en la distribución
  - Considerar si las especificaciones pueden ajustarse para aumentar el porcentaje aceptable

```python
import numpy as np
import matplotlib.pyplot as plt

## Crear una CDF conceptual que cumpla con los puntos dados
r = np.array([0, 5, 10, 15])
F_r = np.array([0, 0.15, 0.85, 1.0])

plt.figure(figsize=(10, 6))
plt.plot(r, F_r, 'b-', linewidth=3, marker='o', markersize=8, label='CDF F(r)')

## Marcar puntos importantes
plt.axhline(0.15, color='red', linestyle=':', alpha=0.7, label='F(5) = 0.15')
plt.axhline(0.85, color='green', linestyle=':', alpha=0.7, label='F(10) = 0.85')
plt.axvline(5, color='red', linestyle=':', alpha=0.7)
plt.axvline(10, color='green', linestyle=':', alpha=0.7)

## Anotar probabilidades
plt.annotate('P(R ≤ 5) = 0.15', xy=(5, 0.15), xytext=(2, 0.3),
             arrowprops=dict(arrowstyle='->', color='red'))
plt.annotate('P(5 < R ≤ 10) = 0.70', xy=(7.5, 0.5), xytext=(3, 0.7),
             arrowprops=dict(arrowstyle='->', color='blue'))
plt.annotate('P(R > 10) = 0.15', xy=(12, 0.9), xytext=(11, 0.6),
             arrowprops=dict(arrowstyle='->', color='green'))

plt.title('CDF Conceptual de la Resistencia del Cable')
plt.xlabel('Resistencia R (Ohmios)')
plt.ylabel('F(r)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(0, 1)

plt.show()

print("Cálculo de probabilidades:")
print(f"P(R > 10) = 1 - F(10) = 1 - 0.85 = {1-0.85:.2f}")
print(f"P(5 < R ≤ 10) = F(10) - F(5) = 0.85 - 0.15 = {0.85-0.15:.2f}")
```

## 11

## Ejercicio 11: Distribución Uniforme (Error de Medición)

## 1. Planteamiento/Fórmula

**Distribución Uniforme en [-0.05, 0.05]:**
- Parámetros: a = -0.05, b = 0.05
- Longitud del intervalo: b - a = 0.1

**PDF:**
$
f(x) = \frac{1}{b-a} = \frac{1}{0.1} = 10 \quad \text{para } -0.05 \le x \le 0.05
$

**Media:**
$
E[X] = \frac{a + b}{2} = \frac{-0.05 + 0.05}{2} = 0
$

## 3. Interpretación

**La media E[X] = 0 significa:**
- **Error sistemático cero**: No hay sesgo en las mediciones
- **Precisión centrada**: Los errores se distribuyen simétricamente alrededor del valor verdadero
- **Compensación de errores**: A largo plazo, los errores positivos y negativos se cancelan
- **Calibración correcta**: El instrumento está bien calibrado sin tendencia a sobreestimar o subestimar

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

## Parámetros de la distribución uniforme
a, b = -0.05, 0.05
loc = a
scale = b - a

## Calcular P(X < 0.02)
prob_less_than_002 = uniform.cdf(0.02, loc=loc, scale=scale)
print(f"P(X < 0.02) = {prob_less_than_002:.4f}")

## Crear arrays para graficar
x = np.linspace(-0.1, 0.1, 1000)
pdf_values = uniform.pdf(x, loc=loc, scale=scale)

## Graficar
plt.figure(figsize=(10, 6))
plt.plot(x, pdf_values, 'b-', linewidth=2, label=f'Uniforme[{a}, {b}]')

## Sombrear región P(X < 0.02)
x_region = np.linspace(a, 0.02, 100)
y_region = uniform.pdf(x_region, loc=loc, scale=scale)
plt.fill_between(x_region, y_region, alpha=0.5, color='red',
                 label=f'P(X < 0.02) = {prob_less_than_002:.3f}')

## Marcar la media
plt.axvline(0, color='green', linestyle='--', linewidth=2,
            label='Media E[X] = 0')

plt.title('Distribución Uniforme del Error de Medición')
plt.xlabel('Error de redondeo (metros)')
plt.ylabel('f(x)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(bottom=0)
plt.show()

print(f"Media E[X] = {uniform.mean(loc=loc, scale=scale):.4f}")
print(f"Desviación estándar = {uniform.std(loc=loc, scale=scale):.4f}")
```

## 12

## Ejercicio 12: Distribución Exponencial (Tiempo de Espera)

## 1. Planteamiento/Fórmula

**Distribución Exponencial con λ = 0.4:**
- PDF: $ f(t) = λe^{-λt} = 0.4e^{-0.4t} $ para $ t \ge 0 $
- CDF: $ F(t) = 1 - e^{-λt} = 1 - e^{-0.4t} $

**Probabilidad P(T > 10):**
$
P(T > 10) = 1 - F(10) = 1 - (1 - e^{-0.4 \times 10}) = e^{-4} \approx 0.0183
$

**Media:**
$
E[T] = \frac{1}{λ} = \frac{1}{0.4} = 2.5 \text{ minutos}
$

**P(T > E[T]):**
$
P(T > 2.5) = e^{-0.4 \times 2.5} = e^{-1} \approx 0.3679
$

## 3. Interpretación

**P(T > E[T]) ≈ 0.3679 ≠ 0.5 porque:**

- **Asimetría positiva**: La distribución exponencial es altamente asimétrica a la derecha
- **Cola larga**: Hay una probabilidad significativa de tiempos de espera muy largos
- **Propiedad de falta de memoria**: La distribución no "recuerda" el tiempo ya esperado
- **Interpretación práctica**: Aunque el tiempo promedio de espera es 2.5 minutos, hay un 36.79% de probabilidad de esperar más que este promedio debido a la asimetría

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

## Parámetros de la distribución exponencial
lambda_rate = 0.4
scale = 1 / lambda_rate  # scipy usa scale = 1/λ

## Calcular P(T > 10)
prob_greater_than_10 = expon.sf(10, scale=scale)
print(f"P(T > 10) = {prob_greater_than_10:.4f}")

## Crear arrays para graficar
t = np.linspace(0, 15, 1000)
pdf_values = expon.pdf(t, scale=scale)

## Graficar
plt.figure(figsize=(10, 6))
plt.plot(t, pdf_values, 'b-', linewidth=2, label=f'Exponencial(λ={lambda_rate})')

## Sombrear región P(T > 10)
t_region = np.linspace(10, 15, 100)
pdf_region = expon.pdf(t_region, scale=scale)
plt.fill_between(t_region, pdf_region, alpha=0.5, color='red',
                 label=f'P(T > 10) = {prob_greater_than_10:.4f}')

## Marcar la media
mean_time = expon.mean(scale=scale)
plt.axvline(mean_time, color='green', linestyle='--', linewidth=2,
            label=f'Media E[T] = {mean_time:.1f} min')

plt.title('Distribución Exponencial del Tiempo de Espera')
plt.xlabel('Tiempo de espera (minutos)')
plt.ylabel('f(t)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(bottom=0)
plt.show()

## Verificación adicional
print(f"\nVerificación:")
print(f"Media E[T] = 1/λ = {mean_time:.1f} minutos")
print(f"P(T > E[T]) = P(T > {mean_time}) = {expon.sf(mean_time, scale=scale):.4f}")
```

## 13

## Ejercicio 13: Distribución Gaussiana General (Calificación de Proyectos)

## 1. Planteamiento/Fórmula

**Distribución Normal con μ = 75, σ = 8**

**Estandarización para P(65 < X < 90):**
$
Z_1 = \frac{65 - 75}{8} = -1.25, \quad Z_2 = \frac{90 - 75}{8} = 1.875
$

**Usando tablas de distribución normal estándar:**
$
P(65 < X < 90) = P(-1.25 < Z < 1.875) = Φ(1.875) - Φ(-1.25)
$
$
= 0.9696 - 0.1056 = 0.8640
$

**Probabilidad de aprobar (X ≥ 60):**
$
Z = \frac{60 - 75}{8} = -1.875
$
$
P(X ≥ 60) = 1 - Φ(-1.875) = Φ(1.875) = 0.9696
$

## 3. Interpretación

**96.96% de estudiantes aprueban el proyecto:**

- **Alto rendimiento**: La mayoría de los estudiantes supera el umbral de aprobación
- **Distribución favorable**: La media está bien por encima del mínimo requerido
- **Bajo riesgo de fracaso**: Solo ≈3% de estudiantes podrían no aprobar
- **Diseño adecuado**: El proyecto está bien calibrado para el nivel de los estudiantes

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

## Parámetros de la distribución normal
mu, sigma = 75, 8

## Calcular P(65 < X < 90)
prob_between = norm.cdf(90, mu, sigma) - norm.cdf(65, mu, sigma)
print(f"P(65 < X < 90) = {prob_between:.4f}")

## Calcular porcentaje de aprobación (X ≥ 60)
prob_aprobacion = norm.sf(60, mu, sigma)  # sf = 1 - cdf
print(f"Porcentaje que aprueba (X ≥ 60) = {prob_aprobacion:.4f} = {prob_aprobacion*100:.1f}%")

## Crear arrays para graficar
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
pdf_values = norm.pdf(x, mu, sigma)

## Graficar
plt.figure(figsize=(12, 6))
plt.plot(x, pdf_values, 'b-', linewidth=2, label=f'N(μ={mu}, σ={sigma})')

## Sombrear región P(65 < X < 90)
x_region = np.linspace(65, 90, 100)
pdf_region = norm.pdf(x_region, mu, sigma)
plt.fill_between(x_region, pdf_region, alpha=0.5, color='green',
                 label=f'P(65 < X < 90) = {prob_between:.3f}')

## Marcar puntos importantes
plt.axvline(60, color='red', linestyle=':', alpha=0.7,
            label=f'Umbral aprobación = 60')
plt.axvline(mu, color='orange', linestyle='--', alpha=0.7,
            label=f'Media μ = {mu}')

plt.title('Distribución Normal de Calificaciones del Proyecto')
plt.xlabel('Calificación')
plt.ylabel('f(x)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(bottom=0)
plt.show()

## Verificación con estandarización
z1 = (65 - mu) / sigma
z2 = (90 - mu) / sigma
z_aprob = (60 - mu) / sigma
print(f"\nEstandarización:")
print(f"Z₁ = (65-75)/8 = {z1:.3f}, Z₂ = (90-75)/8 = {z2:.3f}")
print(f"Z_aprobación = (60-75)/8 = {z_aprob:.3f}")
```

## 14

## Ejercicio 14: Distribución Gaussiana Estándar (Cálculo de Percentiles)

## 1. Planteamiento/Fórmula

**Percentil 95 de Z ~ N(0,1):**
- Buscamos $ z_{0.95} $ tal que $ P(Z ≤ z_{0.95}) = 0.95 $
- De tablas normales estándar: $ z_{0.95} ≈ 1.645 $

**Interpretación:**
- 95% de los valores están por debajo de 1.645
- 5% de los valores están por encima de 1.645 (cola derecha)

## 3. Interpretación

**En análisis de riesgo financiero, z₀.₉₅ = 1.645 representa:**

- **Valor en Riesgo (VaR)**: El máximo pérdida/ganancia esperada con 95% de confianza
- **Umbral de riesgo**: Valores por encima de este percentil se consideran eventos extremos
- **Gestión de colas**: Ayuda a cuantificar el riesgo de eventos raros pero catastróficos
- **Decisiones de inversión**: Se usa para establecer límites de exposición al riesgo
- **Regulación financiera**: Múltiples normas requieren monitoreo de percentiles altos

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

## Calcular percentil 95
percentil_95 = norm.ppf(0.95)
print(f"Percentil 95 (z₀.₉₅) = {percentil_95:.4f}")

## Crear arrays para graficar
z = np.linspace(-4, 4, 1000)
pdf_values = norm.pdf(z)

## Graficar
plt.figure(figsize=(12, 6))
plt.plot(z, pdf_values, 'b-', linewidth=2, label='N(0,1)')

## Marcar percentil 95 y región de cola
plt.axvline(percentil_95, color='red', linestyle='--', linewidth=2,
            label=f'Percentil 95 = {percentil_95:.3f}')

## Sombrear cola del 5%
z_tail = np.linspace(percentil_95, 4, 100)
pdf_tail = norm.pdf(z_tail)
plt.fill_between(z_tail, pdf_tail, alpha=0.5, color='red',
                 label='Cola superior 5%')

## Anotaciones
plt.annotate(f'95% de los valores\nz ≤ {percentil_95:.3f}',
             xy=(-1, 0.2), xytext=(-3.5, 0.3),
             arrowprops=dict(arrowstyle='->', color='blue'))
plt.annotate('5% de los valores\nen cola superior',
             xy=(2, 0.05), xytext=(1.8, 0.2),
             arrowprops=dict(arrowstyle='->', color='red'))

plt.title('Distribución Normal Estándar - Percentil 95')
plt.xlabel('z')
plt.ylabel('φ(z)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(bottom=0)
plt.show()

## Otros percentiles comunes
percentiles = [0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99]
print(f"\nOtros percentiles importantes:")
for p in percentiles:
    z_val = norm.ppf(p)
    print(f"Percentil {p*100:2.0f}%: z = {z_val:7.3f}")
```

## 15

## Ejercicio 15: Función de Variables Aleatorias (Transformación No Lineal)

## 1. Planteamiento/Fórmula

**X ~ Uniforme[0, 100], Y = X²**

**PDF de X:**
$
f_X(x) = \frac{1}{100} \quad \text{para } 0 \le x \le 100
$

**E[Y] = E[X²]:**
$
E[Y] = \int_{0}^{100} x^2 \cdot f_X(x) \, dx = \frac{1}{100} \int_{0}^{100} x^2 \, dx
$
$
= \frac{1}{100} \left[\frac{x^3}{3}\right]_{0}^{100} = \frac{1}{100} \cdot \frac{1,000,000}{3} = \frac{10,000}{3} \approx 3333.33
$

**Comparación con (E[X])²:**
$
E[X] = \frac{0 + 100}{2} = 50, \quad (E[X])^2 = 2500
$
$
E[Y] = 3333.33 \neq 2500 = (E[X])^2
$

## 3. Interpretación

**E[Y] ≠ (E[X])² debido a:**

- **No linealidad de la transformación**: Y = X² es una función convexa
- **Desigualdad de Jensen**: Para funciones convexas, E[g(X)] ≥ g(E[X])
- **Variabilidad de X**: La energía responde más que proporcionalmente a temperaturas altas
- **Distribución asimétrica de Y**: Aunque X es uniforme, Y está sesgada hacia valores altos
- **Impacto práctico**: La energía promedio esperada (3333) es mayor que el cuadrado de la temperatura promedio (2500) debido a la amplificación de temperaturas altas

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
from scipy import integrate

## Parámetros de la distribución uniforme
a, b = 0, 100
loc = a
scale = b - a

## Calcular E[Y] = E[X²] por integración
def x_squared_times_pdf(x):
    return (x**2) * uniform.pdf(x, loc=loc, scale=scale)

E_Y, error = integrate.quad(x_squared_times_pdf, a, b)
E_X = uniform.mean(loc=loc, scale=scale)
E_X_squared = E_X ** 2

print(f"E[X] = {E_X:.2f} °C")
print(f"(E[X])² = {E_X_squared:.2f}")
print(f"E[Y] = E[X²] = {E_Y:.2f}")
print(f"Diferencia: E[X²] - (E[X])² = {E_Y - E_X_squared:.2f}")

## Crear arrays para graficar PDF de X
x = np.linspace(-10, 110, 1000)
pdf_x = uniform.pdf(x, loc=loc, scale=scale)

## Graficar
plt.figure(figsize=(12, 6))
plt.plot(x, pdf_x, 'b-', linewidth=2, label=f'X ~ Uniforme[{a}, {b}]')

## Marcar valores importantes
plt.axvline(E_X, color='red', linestyle='--', linewidth=2,
            label=f'E[X] = {E_X:.1f}')

plt.title('Distribución de la Temperatura del Reactor')
plt.xlabel('Temperatura X (°C)')
plt.ylabel('f_X(x)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(bottom=0)
plt.show()

## Visualización conceptual de la transformación
print(f"\nTransformación Y = X²:")
temperaturas = [0, 25, 50, 75, 100]
energias = [t**2 for t in temperaturas]
for t, e in zip(temperaturas, energias):
    print(f"Temperatura {t:3}°C → Energía {e:5} unidades")
```

---

## 🏫 Universidad de La Ciénega del Estado de Michoacán de Ocampo 🏫

## 🔬 Ingenieria en Nanotecnología 🔬

3° "A"

🧑🏻‍🏫 Profesor: Luis José Yudico Anaya 🧑🏻‍🏫

📍 Sahuayo, Michoacán a 15 de octubre del 2025 📍

## 📝Resumen del capitulo 4 "Variables Aleatorias Continuas"

El Capítulo 4 del texto, titulado **"Variables Aleatorias Continuas"**, marca la transición del estudio de eventos discretos a eventos donde la **aleatoriedad es continua**. El cambio conceptual más significativo es que la suma se reemplaza por la **integración**.

El capítulo aborda los siguientes temas principales:

### ⚙️ 4.1 Función de Densidad de Probabilidad (PDF)

El desafío de las variables continuas es definir su probabilidad, ya que no se pueden contar. La probabilidad se define como una **medida del tamaño de un conjunto** mediante integración.

*   **Definición de PDF ($\boldsymbol{f_X(x)}$):** La PDF es una función que, al integrarse en un intervalo $[a, b]$, produce la probabilidad de que $X$ caiga en ese intervalo: $P[a \leq X \leq b] = \int_{a}^{b} f_X(x) dx$.
*   **Propiedades Fundamentales:** Toda PDF debe satisfacer la **no negatividad** ($f_X(x) \geq 0$ para todo $x$) y la **unidad** ($\int_{\Omega} f_X(x) dx = 1$).
*   **Densidad:** $f_X(x)$ se denomina densidad porque representa la **probabilidad por unidad de longitud**. A diferencia de la PMF, $f_X(x)$ puede tomar valores mayores que 1, siempre que la integral se mantenga unitaria.
*   **Probabilidad de un punto:** Para una variable continua, evaluar la probabilidad en un punto aislado resulta en **cero** ($P[X = x_0] = 0$).
*   **Conexión con PMF:** Una PMF se puede representar como una PDF utilizando un tren de **funciones delta**.

### 4.2 Esperanza, Momento y Varianza

Para las variables continuas, la expectativa, el momento y la varianza se definen de forma análoga a las discretas, utilizando la integración en lugar de la sumatoria.

*   **Expectativa (Media):** Se define como $E[X] = \int_{\Omega} x f_X(x) dx$.
*   **Expectativa de una Función:** La expectativa de una función $g(X)$ es $E[g(X)] = \int_{\Omega} g(x) f_X(x) dx$.
*   **Existencia:** Una variable $X$ tiene expectativa si es **absolutamente integrable**, es decir, si $E[|X|] = \int_{\Omega} |x|f_X(x) dx < \infty$.
*   **Momento $\boldsymbol{k}$:** $E[X^k] = \int_{\Omega} x^k f_X(x) dx$.
*   **Varianza:** Se define como $Var[X] = E[(X - \mu)^2] = \int_{\Omega} (x - \mu)^2 f_X(x) dx$ o $Var[X] = E[X^2] - \mu^2$.

### 4.3 Función de Distribución Acumulada (CDF)

La CDF ($F_X(x)$) es una función siempre bien definida, útil para unificar las variables aleatorias discretas y continuas.

*   **Definición:** $F_X(x) = P[X \leq x] = \int_{x}^{−\infty} f_X(x') dx'$.
*   **Propiedades:** La CDF es **no decreciente**. Su mínimo es $F_X(-\infty) = 0$ y su máximo es $F_X(+\infty) = 1$.
*   **Continuidad:** La CDF es siempre **continua a la derecha** (*right-continuous*).
*   **Cálculo de Probabilidad:** Para variables continuas, $P[a \leq X \leq b] = F_X(b) - F_X(a)$.
*   **Recuperación del PDF:** El PDF es la **derivada** del CDF: $f_X(x) = dF_X(x)/dx$, siempre que $F_X$ sea diferenciable en $x$. Si $F_X$ es discontinua en $x=x_0$, el PDF incluye una delta: $f_X(x_0) = P[X=x_0]\delta(x-x_0)$.
*   **Unificación:** La CDF es continua para variables continuas y una función escalonada para variables discretas.

### 4.4 Mediana, Moda y Media

El capítulo define estos cuantificadores estadísticos desde la perspectiva de la distribución subyacente.

*   **Mediana ($c$):** El punto $c$ tal que divide la distribución en dos áreas iguales, cumpliendo $F_X(c) = 1/2$.
*   **Moda ($c$):** El punto donde $f_X(x)$ es maximizado ($c = \text{argmax}_x f_X(x)$). También es el punto donde la CDF tiene la **pendiente más pronunciada**.
*   **Media (Expectativa):** Puede calcularse a partir del CDF mediante la fórmula (menos común) que involucra la integración del complemento del CDF (para $X>0$).

### 4.5 Variables Aleatorias Uniformes y Exponenciales

Se detallan dos distribuciones continuas fundamentales:

| Distribución | PDF ($f_X(x)$) | Media ($E[X]$) | Varianza ($Var[X]$) |
| :--- | :--- | :--- | :--- |
| **Uniforme** $X \sim \text{Uniform}(a, b)$ | $1/(b-a)$, para $a \leq x \leq b$ | $(a+b)/2$ | $(b-a)^2/12$ |
| **Exponencial** $X \sim \text{Exponential}(\lambda)$ | $\lambda e^{-\lambda x}$, para $x \geq 0$ | $1/\lambda$ | $1/\lambda^2$ |

La **variable exponencial** se utiliza a menudo para modelar el tiempo de inter-llegada entre eventos consecutivos de Poisson.

### 4.6 Variables Aleatorias Gaussianas

*   **Definición:** La PDF de una variable **Gaussiana** $X \sim \text{Gaussian}(\mu, \sigma^2)$ tiene parámetros $\mu$ (media) y $\sigma^2$ (varianza). El PDF tiene una forma simétrica de campana.
*   **Gaussiana Estándar:** $X \sim N(0, 1)$. Su CDF especial se denota $\Phi(\cdot)$.
*   **CDF General:** La CDF de una Gaussiana arbitraria se relaciona con $\Phi(\cdot)$ mediante $F_X(x) = \Phi((x-\mu)/\sigma)$.
*   **Momentos Superiores (Forma):**
    *   **Asimetría (Skewness $\boldsymbol{\gamma}$):** Tercer momento central. Mide la asimetría de la distribución. Una Gaussiana tiene asimetría cero ($\gamma=0$).
    *   **Curtosis (Kurtosis $\boldsymbol{\kappa}$):** Cuarto momento central. Mide cuán pesada es la cola de la distribución. La Gaussiana tiene curtosis $\kappa=3$ (o exceso de curtosis 0).
*   **Origen:** Las Gaussianas son omnipresentes debido al **Teorema del Límite Central (TLC)**. El TLC establece que la suma de muchas variables aleatorias independientes (que es equivalente a la convolución de sus PDFs) converge en distribución a una Gaussiana.

### 4.7 Funciones de Variables Aleatorias (Transformación)

Esta sección aborda el problema de encontrar la PDF ($f_Y(y)$) y CDF ($F_Y(y)$) de una nueva variable $Y = g(X)$, dada la distribución de $X$.

*   **Principio de la CDF:** Se comienza encontrando la CDF de $Y$: $F_Y(y) = P[Y \leq y] = P[g(X) \leq y]$. Si $g$ es monótona creciente e invertible, esto se simplifica a $F_Y(y) = F_X(g^{-1}(y))$.
*   **Principio del PDF:** La PDF se obtiene derivando la CDF y aplicando la regla de la cadena: $f_Y(y) = \left(\frac{d g^{-1}(y)}{dy}\right) \cdot f_X(g^{-1}(y))$.
*   La clave es visualizar cómo la transformación $g$ *comprime* o *estira* las muestras, lo que afecta la densidad y la pendiente del CDF.

### 4.8 Generación de Números Aleatorios

La técnica de transformación se aplica a la generación de números aleatorios a partir de una distribución deseada $F_X$, utilizando una variable uniforme $U \sim \text{Uniform}(0, 1)$.

*   **Teorema de la Transformación Inversa:** La transformación $g$ que convierte $U$ en una variable $X$ con distribución $F_X(x)$ es la **inversa del CDF**: $X = g(U) = F_X^{-1}(U)$. Esto permite generar, por ejemplo, números Gaussianos o exponenciales a partir de números uniformes.

### Resumen del Capítulo 4

En resumen, el Capítulo 4 establece que las variables continuas se definen mediante **integraciones**. La **CDF** es la herramienta de unificación entre lo discreto (función escalonada) y lo continuo (función suave). El origen de las variables **Gaussianas** se encuentra en la suma de muchas variables independientes (TLC). Finalmente, la **transformación de variables** se realiza en el espacio CDF, donde la transformación inversa del CDF ($g = F_X^{-1}$) permite generar números aleatorios según cualquier distribución predefinida.

### ➗Detallado de los símbolos y las fórmulas matemáticas

El **principio fundamental** de las variables continuas es que la probabilidad se calcula mediante la **integración** ($\int$) en lugar de la sumatoria ($\sum$).

La PDF, $f_X(x)$, es la función central para definir una variable continua.

| Símbolo/Fórmula | Significado | Fuente |
| :--- | :--- | :--- |
| $\boldsymbol{X}$ | Variable aleatoria continua (es la función). | |
| $\boldsymbol{x}$ | El estado o valor que toma la variable aleatoria $X$. | |
| $\boldsymbol{f_X(x)}$ | **Función de Densidad de Probabilidad (PDF)**. Representa la "densidad" o probabilidad por unidad de longitud. | |
| $P[a \leq X \leq b] = \int_{a}^{b} f_X(x) dx$ | La probabilidad de que $X$ caiga en el intervalo $[a, b]$ es el **área bajo la curva** de la PDF en ese rango. | |
| $\int_{\Omega} f_X(x) dx = 1$ | **Condición de Normalización**. La integral de la PDF sobre todo el espacio de muestra ($\Omega$) debe ser igual a uno. | |

### 4.2 Esperanza, Momento y Varianza

La expectativa se calcula reemplazando la sumatoria por la integral en la definición discreta.

| Símbolo/Fórmula | Significado | Fuente |
| :--- | :--- | :--- |
| $\boldsymbol{E[X]}$ o $\boldsymbol{\mu}$ | **Esperanza (Media)**. Representa el promedio ponderado de los posibles valores de $X$. | |
| $E[X] = \int_{\Omega} x f_X(x) dx$ | **Fórmula de la Expectativa**. $x$ se pondera por la densidad $f_X(x)$ e integra sobre el espacio $\Omega$. | |
| $E[g(X)] = \int_{\Omega} g(x) f_X(x) dx$ | **Expectativa de una Función $g(X)$**. Se usa para calcular momentos superiores. | |
| $\boldsymbol{E[X^k]}$ | **Momento $k$**. Es la expectativa de $X$ elevada a la potencia $k$. | |
| $\boldsymbol{Var[X]}$ o $\boldsymbol{\sigma^2}$ | **Varianza**. Mide la dispersión de $X$ alrededor de su media $\mu$. | |
| $Var[X] = E[(X - \mu)^2]$ | **Fórmula de la Varianza**. Se define como el momento central de segundo orden. | |
| $Var[X] = E[X^2] - \mu^2$ | Fórmula alternativa que relaciona la varianza con el segundo momento ($E[X^2]$) y la media. | |

### 4.3 Función de Distribución Acumulada (CDF)

La CDF, $F_X(x)$, unifica el tratamiento de variables discretas y continuas.

| Símbolo/Fórmula | Significado | Fuente |
| :--- | :--- | :--- |
| $\boldsymbol{F_X(x)}$ | **Función de Distribución Acumulada**. Es la probabilidad de que $X$ tome un valor menor o igual a $x$. | |
| $F_X(x) = \int_{-\infty}^{x} f_X(x') dx'$ | **Fórmula de Definición del CDF**. El CDF es la integral de la PDF desde $-\infty$ hasta $x$. | |
| $f_X(x) = \frac{d F_X(x)}{dx}$ | **Recuperación del PDF**. La PDF es la derivada del CDF, aplicando el Teorema Fundamental del Cálculo. | |
| $P[a \leq X \leq b] = F_X(b) - F_X(a)$ | Cálculo de probabilidad para un intervalo usando el CDF. | |

### 4.5 Distribuciones Comunes

| Distribución | Símbolos | Función de Densidad ($f_X(x)$) | Parámetros | Fuente |
| :--- | :--- | :--- | :--- | :--- |
| **Uniforme** | $X \sim \text{Uniform}(a, b)$ | $\frac{1}{b-a}$, para $a \leq x \leq b$ | $a$: Límite inferior. $b$: Límite superior. | |
| **Exponencial** | $X \sim \text{Exponential}(\lambda)$ | $\lambda e^{-\lambda x}$, para $x \geq 0$ | $\lambda$: Tasa (Rate Parameter). | |

### 4.6 Variable Aleatoria Gaussiana

La distribución Gaussiana es fundamental, especialmente por el **Teorema del Límite Central (TLC)**.

| Símbolo/Fórmula | Significado | Fuente |
| :--- | :--- | :--- |
| $X \sim \text{Gaussian}(\mu, \sigma^2)$ | Notación para una Gaussiana con media $\mu$ y varianza $\sigma^2$. | |
| $f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left\{ -\frac{(x-\mu)^2}{2\sigma^2} \right\}$ | **PDF Gaussiana**. Función simétrica de campana. | |
| $\boldsymbol{\Phi}(\cdot)$ | **CDF de la Gaussiana Estándar** ($N(0, 1)$). La $\mu=0$ y $\sigma^2=1$. | |

### 4.7 Funciones de Variables Aleatorias (Transformación)

Se busca encontrar la distribución de $Y = g(X)$, dada la distribución de $X$.

| Símbolo/Fórmula | Significado | Fuente |
| :--- | :--- | :--- |
| $Y = g(X)$ | Transformación donde $X$ es la variable de entrada y $g(\cdot)$ es la función de transformación. | |
| $F_Y(y) = F_X(g^{-1}(y))$ | **CDF de la Variable Transformada**. Válida si $g$ es invertible y monótona creciente. | |
| $f_Y(y) = \left(\frac{d g^{-1}(y)}{dy}\right) \cdot f_X(g^{-1}(y))$ | **PDF de la Variable Transformada**. Se obtiene derivando el CDF y aplicando la regla de la cadena. | |

#🧪**INGENIERÍA EN NANOTECNOLOGÍA**
##**UCEMICH** 13/10/25

## TEMA: DISTRIBUCIONES DE PROBABILIDAD CON PYTHON

## 🧠Modelos para Variables Aleatorias Continuas

### 📋Listado de las distribuciones de probabilidad continuas más utilizadas

En las disciplinas de nanotecnología, ciencias de los materiales, inteligencia artificial, diseño de experimentos y pruebas de hipótesis, se destacan las siguientes distribuciones de probabilidad continuas:

##### Nanotecnología

1. **Distribución Normal**
   - **Uso**: Modelar variaciones en características físicas de nanopartículas, como tamaño y forma.
   - **Ejemplo**: La distribución del tamaño de partículas en una muestra de nanopartículas de sílice, donde la mayoría de las partículas presentan un tamaño cercano a la media, con algunas variaciones hacia los extremos.

2. **Distribución Log-Normal**
   - **Uso**: Representar la distribución de tamaños de nanopartículas que no pueden ser negativas.
   - **Ejemplo**: La distribución de la superficie específica de nanopartículas de metal, que resulta de procesos de síntesis en los que el tamaño de las partículas sigue una relación logarítmica.

3. **Distribución Beta**
   - **Uso**: Modelar proporciones y tasas en sistemas acotados, como la fracción de superficie cubierta en un proceso de recubrimiento.
   - **Ejemplo**: Proporciones de reacción en un sistema catalítico a nanoescala, donde se evalúa la efectividad de un catalizador en función de la superficie activa disponible.

4. **Distribución Gamma**
   - **Uso**: Modelar el tiempo hasta la falla en sistemas con múltiples etapas.
   - **Ejemplo**: Análisis del tiempo hasta la aparición de defectos en nanopartículas durante el proceso de fabricación, lo que permite optimizar el proceso de síntesis.

##### Ciencias de los Materiales

1. **Distribución Weibull**
   - **Uso**: Análisis de fiabilidad y duración de vida de materiales.
   - **Ejemplo**: Estudio de la duración de vida de componentes en pruebas de fatiga, donde se busca entender la probabilidad de fallo de un material bajo cargas cíclicas.

2. **Distribución Gamma**
   - **Uso**: Modelar tiempos de fallo y resistencia en materiales compuestos.
   - **Ejemplo**: Análisis del tiempo entre fracturas en materiales bajo estrés, lo cual es crucial para evaluar la durabilidad de componentes en aplicaciones industriales.

3. **Distribución Exponencial**
   - **Uso**: Modelar el tiempo entre eventos, como fallos en materiales.
   - **Ejemplo**: Evaluación del tiempo hasta la corrosión en materiales metálicos expuestos a ambientes agresivos, ayudando a predecir la vida útil de estructuras metálicas.

4. **Distribución Chi-Cuadrada**
   - **Uso**: Evaluar la varianza de una población y realizar pruebas de bondad de ajuste.
   - **Ejemplo**: Análisis de la variabilidad en pruebas de resistencia de materiales, permitiendo determinar si un nuevo material cumple con estándares de calidad.

5. **Distribución Log-Normal**
   - **Uso**: Modelar fenómenos donde las variables son el resultado de procesos multiplicativos.
   - **Ejemplo**: Distribución de la resistencia a la tracción de fibras compuestas, donde las variaciones en la producción generan una distribución log-normal de las resistencias observadas.

##### Inteligencia Artificial

1. **Distribución Normal**
   - **Uso**: Asumida en muchos algoritmos de aprendizaje automático, especialmente en la estimación de errores.
   - **Ejemplo**: Modelado de errores de predicción en regresiones, donde se espera que los errores sigan una distribución normal.

2. **Distribución Log-Normal**
   - **Uso**: Modelar características que resultan de procesos multiplicativos.
   - **Ejemplo**: Distribución de ingresos o propiedades de datos en análisis de mercado, donde las variables de ingresos no pueden ser negativas.

3. **Distribución Beta**
   - **Uso**: Modelar incertidumbres en probabilidades y proporciones.
   - **Ejemplo**: Asignación de probabilidades en modelos bayesianos, donde se utilizan distribuciones beta para representar la incertidumbre sobre las tasas de éxito.

4. **Distribución de Dirichlet**
   - **Uso**: Modelar distribuciones de probabilidad en múltiples categorías.
   - **Ejemplo**: Priorización de características en algoritmos de clasificación, donde se evalúan las probabilidades de cada clase en un modelo de clasificación.

5. **Distribución t-Student**
   - **Uso**: Realizar inferencias sobre la media de poblaciones pequeñas.
   - **Ejemplo**: Evaluación de errores en muestras pequeñas en aprendizaje automático, donde se requiere estimar la media y su incertidumbre.

##### Diseño de Experimentos y Pruebas de Hipótesis

1. **Distribución Normal**
   - **Uso**: Asumida en muchas pruebas de hipótesis y análisis de varianza.
   - **Ejemplo**: Pruebas t para comparar medias de grupos, donde se evalúa si las diferencias observadas son estadísticamente significativas.

2. **Distribución Chi-Cuadrada**
   - **Uso**: Pruebas de independencia y bondad de ajuste.
   - **Ejemplo**: Evaluar la relación entre variables categóricas en experimentos de diseño factorial.

3. **Distribución F (Fisher-Snedecor)**
   - **Uso**: Comparar varianzas entre grupos.
   - **Ejemplo**: Análisis de varianza (ANOVA) para determinar si hay diferencias significativas entre medias de varios grupos en experimentos.

4. **Distribución Exponencial**
   - **Uso**: Modelar el tiempo hasta el evento en estudios de supervivencia y fiabilidad.
   - **Ejemplo**: Análisis de tiempos hasta fallas en experimentos de durabilidad de materiales.

Cada una de estas distribuciones juega un papel crucial en la modelación, análisis y comprensión de datos en sus respectivos campos, permitiendo realizar inferencias precisas y fundamentadas en experimentos y estudios estadísticos.

### ✨Distribución Uniforme

* **Descripción**: Modelo donde todos los valores en un intervalo \([a, b]\) son igualmente probables.

* **Parámetros**:
  - $ a $ (límite inferior)
  - $ b $ (límite superior)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x) =
\begin{cases}
\frac{1}{b-a} & \text{si } a \leq x \leq b \\
0 & \text{si } x < a \text{ o } x > b
\end{cases}
$$

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) =
\begin{cases}
0 & \text{si } x < a \\
\frac{x-a}{b-a} & \text{si } a \leq x < b \\
1 & \text{si } x \geq b
\end{cases}
$$

* **Valor Esperado**: $ E[X] = \frac{a + b}{2} $

* **Media**: $ \mu_X = \frac{a + b}{2} $

* **Desviación Estándar**: $ \sigma = \frac{b - a}{\sqrt{12}} $

* **Percentiles**:
$$
x_\alpha =
\begin{cases}
a & \text{si } \alpha = 0 \\
b & \text{si } \alpha = 1 \\
a + \alpha(b - a) & \text{si } 0 < \alpha < 1
\end{cases}
$$

**Comandos en R**:
```r
## PDF
dunif(x, min = a, max = b)

## CDF
punif(x, min = a, max = b)

## Simulación
runif(n, min = a, max = b)

```python
import numpy as np
from scipy.stats import uniform

## Definición de parámetros
a = 0  # min
b = 10 # max
x = 5  # valor para PDF/CDF
n = 10 # número de muestras para simulación

## ----------------------------------------
## PDF (Función de Densidad de Probabilidad)
## dunif(x, min = a, max = b)
## scipy.stats.uniform.pdf(x, loc=a, scale=b-a)
pdf_value = uniform.pdf(x, loc=a, scale=b-a)
print(f"PDF (uniform.pdf) para x={x}: {pdf_value}")

## ----------------------------------------
## CDF (Función de Distribución Acumulada)
## punif(x, min = a, max = b)
## scipy.stats.uniform.cdf(x, loc=a, scale=b-a)
cdf_value = uniform.cdf(x, loc=a, scale=b-a)
print(f"CDF (uniform.cdf) para x={x}: {cdf_value}")

## ----------------------------------------
## Simulación/Muestreo
## runif(n, min = a, max = b)
## np.random.uniform(low=a, high=b, size=n)
samples = np.random.uniform(low=a, high=b, size=n)
print(f"Muestras (np.random.uniform) n={n}: {samples}")
```

#### 🔍Ejemplo de Gráfica de la Distribución Uniforme

La distribución uniforme describe un modelo en el que todos los resultados posibles en un intervalo dado tienen la misma probabilidad de ocurrir. Esta distribución se utiliza comúnmente en situaciones donde no hay una tendencia natural hacia un resultado particular.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad $ PDF$ de la distribución uniforme en el intervalo $[a, b]$. A medida que se ajustan los valores de $ a $ y $ b $, la altura de la función de densidad se mantiene constante, reflejando la igualdad de probabilidad de cada punto dentro del intervalo. Esta propiedad de uniformidad hace que la distribución uniforme sea un modelo sencillo pero efectivo para representar fenómenos aleatorios en situaciones controladas.

```python
"""

## Cargar librerías necesarias
library(ggplot2)

## Definir los parámetros de la distribución uniforme
a <- 0  # límite inferior
b <- 1  # límite superior

## Crear un rango de valores para x
x <- seq(a - 0.1, b + 0.1, by = 0.01)

## Calcular la PDF para la distribución uniforme
pdf <- dunif(x, min = a, max = b)

## Crear un data frame
data <- data.frame(x = x, pdf = pdf)

## Graficar la PDF de la distribución uniforme
ggplot(data, aes(x = x, y = pdf)) +
  geom_line(color = "blue", size = 1) +
  labs(title = "Gráfica de la Distribución Uniforme",
       x = "x",
       y = "Densidad de Probabilidad (PDF)") +
  theme_minimal()

  """
```

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import uniform
import pandas as pd

## ----------------------------------------
## 1. Definir los parámetros de la distribución uniforme
a = 0  # límite inferior (loc)
b = 1  # límite superior (loc + scale)
scale = b - a # Rango (b-a) requerido por scipy

## ----------------------------------------
## 2. Crear un rango de valores para x (equivalente a seq() en R)
## Se usa np.linspace para crear un arreglo de puntos espaciados uniformemente
x = np.linspace(a - 0.1, b + 0.1, 500)

## ----------------------------------------
## 3. Calcular la PDF para la distribución uniforme (equivalente a dunif() en R)
## El parámetro 'loc' es a, y 'scale' es (b-a)
pdf = uniform.pdf(x, loc=a, scale=scale)

## ----------------------------------------
## 4. Crear un DataFrame (opcional, pero ayuda a replicar el flujo de R)
data = pd.DataFrame({'x': x, 'pdf': pdf})

## ----------------------------------------
## 5. Graficar la PDF de la distribución uniforme (equivalente a ggplot2)
## Usaremos matplotlib junto con seaborn para un estilo moderno (theme_minimal)

plt.figure(figsize=(10, 6))

## Graficar la línea (equivalente a geom_line())
## Se usa el DataFrame para graficar de forma similar a ggplot
sns.lineplot(x='x', y='pdf', data=data, color="blue", linewidth=2)

## Añadir títulos y etiquetas (equivalente a labs())
plt.title("Gráfica de la Distribución Uniforme", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("Densidad de Probabilidad (PDF)", fontsize=14)

## Aplicar un estilo minimalista (equivalente a theme_minimal())
sns.set_style("whitegrid")
plt.grid(True, linestyle='--', alpha=0.6)

## Mostrar la gráfica
plt.show()
```

#### 📜**Descripción del Código**

* **Cargar librerías**: Se utiliza `ggplot2 `para crear la gráfica.
* **Definir los parámetros**: Se establecen los límites del intervalo $ a $ y $ b$ para la distribución uniforme.
* **Crear un rango de valores para $ x $**: Se define un rango de valores posibles entre $a $ y $ b $ para representar la distribución.
* **Calcular la PDF**: Se utiliza `dunif()` para calcular la función de densidad de probabilidad en el intervalo definido.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $ x $ y sus correspondientes probabilidades.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $PDF $ de la distribución uniforme en el intervalo $[a, b]$.

**EJERCICIO 8**

Agrega ejemplos y los usos recomendados.

### 🎯 Usos Recomendados de la Distribución Uniforme (Continua)

La **Distribución Uniforme Continua** $\text{U}(a, b)$ describe una situación donde **todos los valores dentro de un rango definido son igualmente probables**.

1.  **Simulación y Generación de Números Aleatorios**
    Es la distribución fundamental para generar números aleatorios. Todos los lenguajes de programación y paquetes estadísticos utilizan una distribución uniforme (a menudo entre 0 y 1) como base para generar datos aleatorios que luego pueden transformarse en otras distribuciones más complejas (como la Normal o Exponencial).

    * **Ejemplo:** Un simulador de tráfico necesita generar un valor aleatorio para el tiempo de reacción de los conductores. Si se asume que este tiempo puede ser cualquier valor entre **0.5 y 1.5 segundos** ($a=0.5, b=1.5$), y que ningún tiempo es inherentemente más probable que otro dentro de ese rango, se usa $\text{U}(0.5, 1.5)$.
    * **Aplicación:** Modelar el error de redondeo en cálculos digitales, donde el error puede ser cualquier valor entre $-\varepsilon$ y $\varepsilon$ con igual probabilidad.

2.  **Modelado de la Ignorancia o Falta de Información**
    Se utiliza como un **modelo "por defecto"** o una "distribución no informativa" en estadística bayesiana y modelado cuando no hay datos previos o conocimiento para favorecer un valor sobre otro dentro de un intervalo.

    * **Ejemplo:** Un ingeniero está diseñando un nuevo componente y estima que su vida útil será, como mínimo, de **30 meses** y, como máximo, de **50 meses**. Al no tener datos de prueba, asume que cualquier vida útil dentro de ese rango es igualmente probable, por lo que utiliza $\text{U}(30, 50)$ para sus cálculos iniciales.
    * **Aplicación:** La hora a la que llega un autobús a una parada, si se sabe que pasa entre las **7:00 AM y 7:10 AM**, pero no hay información sobre la frecuencia o si está sujeto a retrasos. La probabilidad de que llegue en cualquier momento de esos 10 minutos es la misma.

3.  **Procesos de Muestreo y Producción con Tolerancias**
    Aplica en escenarios donde una medición o resultado puede caer en cualquier punto dentro de los límites de tolerancia o precisión de un equipo.

    * **Ejemplo:** Una máquina corta piezas de metal y está calibrada para tener un error de medición máximo de $\pm 0.01$ mm. El error real de cualquier corte se asume uniformemente distribuido entre **$-0.01$ y $0.01$ mm**. La probabilidad de que el error sea exactamente $-0.005$ es la misma que la probabilidad de que sea $0.003$.
    * **Aplicación:** El ángulo al que una rueda se detiene en un juego de ruleta idealizada. La posición final (el ángulo de $0^\circ$ a $360^\circ$) es uniforme.

---

## 🎲 Distribución Uniforme Discreta

Aunque la **Distribución Uniforme Continua** es la más común, existe su contraparte **Discreta**, donde un número **finito** de valores tiene la misma probabilidad.

* **Ejemplo:** **Lanzamiento de un dado estándar de seis caras.** El conjunto de valores posibles es $\{1, 2, 3, 4, 5, 6\}$. La probabilidad de obtener cualquiera de estos valores es $\frac{1}{6}$ (es decir, la probabilidad es constante para cada resultado).
* **Ejemplo:** Elegir al azar a **un empleado de una lista de 50** para una encuesta. La probabilidad de que sea elegido cualquier empleado en específico es $\frac{1}{50}$.

### 💻Ejemplos en codigo

Distribucion uniforme continua

Ejemplo 1

```python
import numpy as np
import matplotlib.pyplot as plt

## Parámetros de la distribución U(a, b)
a = 0.5  # Límite inferior (mínimo tiempo de reacción)
b = 1.5  # Límite superior (máximo tiempo de reacción)
n_simulaciones = 1000

## Generar 1000 tiempos de reacción aleatorios
tiempos_reaccion = np.random.uniform(low=a, high=b, size=n_simulaciones)

## Imprimir los primeros 10 resultados simulados y la media
print(f"Parámetros: U({a}, {b})")
print(f"Primeros 10 tiempos de reacción simulados (segundos): {tiempos_reaccion[:10].round(3)}")
print(f"Media de la simulación: {np.mean(tiempos_reaccion):.3f} segundos")

## Opcional: Visualización de la distribución
plt.hist(tiempos_reaccion, bins=20, density=True, color='skyblue', edgecolor='black')
plt.title(f'Simulación de Tiempos de Reacción U({a}, {b})')
plt.xlabel('Tiempo de Reacción (segundos)')
plt.ylabel('Densidad de Probabilidad')
plt.show()
```

Ejemplo 2

```python
from scipy.stats import uniform

## Parámetros de la distribución U(a, b)
a = 30  # Mínimo de vida útil (meses)
b = 50  # Máximo de vida útil (meses)

## Rango de interés: Vida útil entre 35 y 45 meses
x1 = 35
x2 = 45

## Calcular la probabilidad P(35 < X < 45)
## CDF (Cumulative Distribution Function) es P(X <= x)
probabilidad = uniform.cdf(x2, loc=a, scale=b-a) - uniform.cdf(x1, loc=a, scale=b-a)

## Para la distribución uniforme, la probabilidad también es (x2 - x1) / (b - a)
probabilidad_simple = (x2 - x1) / (b - a)

print(f"Parámetros: U({a}, {b}) meses")
print(f"La probabilidad de que la vida útil esté entre {x1} y {x2} meses es: {probabilidad:.4f}")
print(f"(Cálculo simple: ({x2}-{x1})/({b}-{a}) = {probabilidad_simple:.4f})")
```

Ejemplo 3

```python
from scipy.stats import uniform

## Parámetros de la distribución U(a, b)
a = -0.01  # Error mínimo (mm)
b = 0.01   # Error máximo (mm)

## Punto de interés
x_punto = 0.003  # Error de 0.003 mm

## Calcular la PDF (Probability Density Function) en el rango
## La densidad es 1 / (b - a) dentro del rango [a, b]
densidad = uniform.pdf(x_punto, loc=a, scale=b-a)
## Nota: La probabilidad de un punto específico en una distribución continua es 0,
## pero la densidad (altura) es constante.

print(f"Parámetros: U({a}, {b}) mm")
print(f"El rango del error de medición es: {b - a} mm")
print(f"La densidad de probabilidad para cualquier punto dentro del rango es: {densidad:.4f}")
print(f"Esto significa que la densidad es constante en todo el intervalo.")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, randint
from collections import Counter

## Configuración de los gráficos
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(3, 1, figsize=(10, 15))
fig.suptitle('Ejemplos de la Distribución Uniforme', fontsize=16, y=1.02)

## ====================================================================
## 1. Simulación y Generación de Tiempos de Reacción (Continua)
## ====================================================================

a_cont = 0.5  # Límite inferior
b_cont = 1.5  # Límite superior
n_simulaciones = 1000

## Generar 1000 tiempos de reacción aleatorios U(0.5, 1.5)
tiempos_reaccion = np.random.uniform(low=a_cont, high=b_cont, size=n_simulaciones)

## Calcular la densidad teórica (altura del rectángulo)
densidad_teorica = 1 / (b_cont - a_cont)

ax = axes[0]
ax.hist(tiempos_reaccion, bins=25, density=True, color='skyblue', edgecolor='black', alpha=0.7)
ax.hlines(densidad_teorica, a_cont, b_cont, color='red', linestyle='--', label=f'Densidad Teórica: {densidad_teorica:.2f}')
ax.set_title(f'1. Simulación de Tiempos de Reacción U({a_cont}, {b_cont})')
ax.set_xlabel('Tiempo de Reacción (segundos)')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## ====================================================================
## 2. Modelado de la Ignorancia (Vida Útil) y Probabilidad de Rango (Continua)
## ====================================================================

a_vida = 30  # Mínimo de vida útil (meses)
b_vida = 50  # Máximo de vida útil (meses)
x1_rango = 35
x2_rango = 45

## Calcular la probabilidad P(35 < X < 45)
probabilidad = uniform.cdf(x2_rango, loc=a_vida, scale=b_vida-a_vida) - \
               uniform.cdf(x1_rango, loc=a_vida, scale=b_vida-a_vida)

## Generar puntos para la PDF (función de densidad)
x_pdf = np.linspace(25, 55, 200)
y_pdf = uniform.pdf(x_pdf, loc=a_vida, scale=b_vida-a_vida)

ax = axes[1]
ax.plot(x_pdf, y_pdf, color='red', label='PDF Uniforme')
ax.fill_between(x_pdf, y_pdf, where=((x_pdf > x1_rango) & (x_pdf < x2_rango)),
                color='lightgreen', alpha=0.6,
                label=f'P({x1_rango}<X<{x2_rango}) = {probabilidad:.2f}')
ax.set_title(f'2. Probabilidad de la Vida Útil U({a_vida}, {b_vida})')
ax.set_xlabel('Vida Útil (meses)')
ax.set_ylabel('Densidad de Probabilidad')
ax.set_ylim(0, 0.06)
ax.legend()

## ====================================================================
## 3. Lanzamiento de un Dado (Uniforme Discreta)
## ====================================================================

low_d = 1
high_d = 7 # Exclusivo
n_lanzamientos_d = 1000

## Simular lanzamientos de dado
resultados_dado = np.random.randint(low=low_d, high=high_d, size=n_lanzamientos_d)

## Contar la frecuencia de cada resultado
frecuencias = Counter(resultados_dado)
caras = np.arange(1, 7)
prob_teorica_d = 1 / 6

## Calcular probabilidades observadas para el gráfico
probabilidades_obs = [frecuencias.get(cara, 0) / n_lanzamientos_d for cara in caras]

ax = axes[2]
ax.bar(caras, probabilidades_obs, color='orange', edgecolor='black', alpha=0.7, label='Probabilidad Observada')
ax.hlines(prob_teorica_d, 0.5, 6.5, color='red', linestyle='--', label=f'Probabilidad Teórica: {prob_teorica_d:.3f}')
ax.set_title(f'3. Lanzamiento de un Dado (Uniforme Discreta)')
ax.set_xlabel('Resultado del Dado')
ax.set_ylabel('Probabilidad')
ax.set_xticks(caras)
ax.set_ylim(0, 0.25)
ax.legend()

## Ajustar diseño y mostrar
plt.tight_layout()
plt.show()
```

Distribución Uniforme Discreta

Ejemplo 1

```python
import numpy as np
from collections import Counter

## Parámetros: Los valores posibles (1 a 6)
caras_dado = np.arange(1, 7)
n_lanzamientos = 100

## Simular 100 lanzamientos de dado. El 'high' es exclusivo, por eso usamos 7.
resultados = np.random.randint(low=1, high=7, size=n_lanzamientos)

## Contar la frecuencia de cada resultado
frecuencias = Counter(resultados)

## Calcular la probabilidad teórica (constante)
prob_teorica = 1 / 6

print(f"Valores posibles del dado: {caras_dado}")
print(f"Probabilidad teórica de cada cara: {prob_teorica:.4f}")
print("-" * 30)

print("Frecuencias observadas en 100 lanzamientos:")
for cara in caras_dado:
    frecuencia_observada = frecuencias.get(cara, 0)
    prob_observada = frecuencia_observada / n_lanzamientos
    print(f"Cara {cara}: {frecuencia_observada} veces | P. Observada: {prob_observada:.4f}")
```

### ✨Distribución Exponencial

* **Descripción**: Modelo de tiempo hasta el próximo evento en un proceso de Poisson.

* **Parámetro**:
- $ \lambda$ (tasa de ocurrencia de eventos)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x) =
\begin{cases}
\lambda e^{-\lambda x} & \text{si } x \geq 0 \\
0 & \text{si } x < 0
\end{cases}
$$

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) =
\begin{cases}
1 - e^{-\lambda x} & \text{si } x \geq 0 \\
0 & \text{si } x < 0
\end{cases}
$$

* **Valor Esperado**: $ E[X] = \frac{1}{\lambda}$

* **Media**: $ \mu_X = \frac{1}{\lambda}$

* **Desviación Estándar**: $\sigma = \frac{1}{\lambda}$

* **Percentiles**: $x_\alpha = -\frac{\log(\alpha)}{\lambda}$

**Comandos en R**:
```r
## PDF
dexp(x, rate = lambda)

## CDF
pexp(x, rate = lambda)

## Simulación
rexp(n, rate = lambda)

```python
import numpy as np
from scipy.stats import expon

## ----------------------------------------
## Definición de parámetros (usando la notación de R)
lambda_rate = 0.5 # Tasa (rate) en R (lambda)
x = 2             # valor para PDF/CDF
n = 10            # número de muestras para simulación

## ----------------------------------------
## Conversión de parámetros para Scipy
## Scipy usa 'scale' (beta), que es el inverso de 'rate' (lambda)
beta_scale = 1 / lambda_rate # scale = 1 / lambda

## ----------------------------------------
## PDF (Función de Densidad de Probabilidad)
## dexp(x, rate = lambda)
## scipy.stats.expon.pdf(x, scale=1/lambda)
pdf_value = expon.pdf(x, scale=beta_scale)
print(f"PDF (expon.pdf) para x={x}: {pdf_value}")

## ----------------------------------------
## CDF (Función de Distribución Acumulada)
## pexp(x, rate = lambda)
## scipy.stats.expon.cdf(x, scale=1/lambda)
cdf_value = expon.cdf(x, scale=beta_scale)
print(f"CDF (expon.cdf) para x={x}: {cdf_value}")

## ----------------------------------------
## Simulación/Muestreo
## rexp(n, rate = lambda)
## np.random.exponential(scale=1/lambda, size=n)
## Nota: numpy también usa 'scale' (beta)
samples = np.random.exponential(scale=beta_scale, size=n)
print(f"Muestras (np.random.exponential) n={n}: {samples}")
```

#### 🔍Ejemplo de Gráfica de la Distribución Exponencial

La distribución exponencial describe el tiempo entre eventos en un proceso de Poisson. Es útil para modelar situaciones donde se necesita calcular el tiempo hasta que ocurra un evento, dado un promedio de eventos conocido.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad $PDF$ de la distribución exponencial para varios valores de $ \lambda$, que es la tasa de ocurrencia de eventos por unidad de tiempo. A medida que $ \lambda $aumenta, la distribución se vuelve más concentrada hacia la izquierda, indicando que los eventos ocurren más rápidamente.

```python
"""

## Instalar y cargar la librería necesaria
#install.packages('ggplot2')  # Descomentar si no está instalada
library(ggplot2)

## Aquí tienes un ejemplo de varios gráficos de la distribución exponencial
## con diferentes valores de lambda. El código incluye la configuración
## necesaria para generar los gráficos:

## Definir un rango de valores para x
x <- seq(0, 5, by = 0.01)

## Crear un data frame vacío para almacenar los resultados
data_list <- list()

## Valores de lambda a usar
lambda_values <- c(0.5, 1, 1.5)

## Calcular la PDF para cada valor de lambda y almacenar en el data frame
for (lambda in lambda_values) {
  pdf <- dexp(x, rate = lambda)
  data_list[[as.character(lambda)]] <- data.frame(x = x, pdf = pdf, lambda = lambda)
}

## Combinar todos los data frames en uno solo
data <- do.call(rbind, data_list)

## Graficar la distribución exponencial para diferentes valores de lambda
ggplot(data, aes(x = x, y = pdf, color = as.factor(lambda))) +
  geom_line() +
  labs(title = "Distribución Exponencial para Diferentes Valores de Lambda",
       x = "x",
       y = "Densidad de Probabilidad",
       color = "Lambda") +
  theme_minimal() +
  scale_color_manual(values = c("blue", "red", "green"))

"""
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import expon

## ----------------------------------------
## 1. Definir un rango de valores para x (equivalente a seq() en R)
x = np.linspace(0, 5, 501) # 501 puntos para tener una línea suave

## ----------------------------------------
## 2. Valores de lambda (tasa) a usar
lambda_values = [0.5, 1, 1.5]

## ----------------------------------------
## 3. Crear una lista para almacenar los DataFrames
data_list = []

## 4. Calcular la PDF para cada valor de lambda y almacenar (equivalente al bucle for en R)
for lambda_rate in lambda_values:
## Convertir lambda (tasa) a scale (escala) para scipy
    beta_scale = 1 / lambda_rate

## Calcular la PDF (equivalente a dexp() en R)
    pdf = expon.pdf(x, scale=beta_scale)

## Crear un DataFrame para este lambda
    df_temp = pd.DataFrame({
        'x': x,
        'pdf': pdf,
        'lambda': lambda_rate
    })
    data_list.append(df_temp)

## 5. Combinar todos los DataFrames en uno solo (equivalente a do.call(rbind, ...))
data = pd.concat(data_list)

## ----------------------------------------
## 6. Graficar la distribución exponencial (equivalente a ggplot2)

## Configurar el estilo de Seaborn (similar a theme_minimal())
sns.set_style("whitegrid")

plt.figure(figsize=(10, 6))

## Diccionario para mapear valores de lambda a colores (equivalente a scale_color_manual)
color_map = {0.5: "blue", 1.0: "red", 1.5: "green"}

## Crear la gráfica con Seaborn (similar a ggplot con geom_line)
## Se usa 'hue' para diferenciar las líneas por el valor de 'lambda'
sns.lineplot(
    data=data,
    x='x',
    y='pdf',
    hue='lambda',
    palette=color_map,
    linewidth=2
)

## Añadir títulos y etiquetas (equivalente a labs())
plt.title("Distribución Exponencial para Diferentes Valores de Lambda", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("Densidad de Probabilidad", fontsize=14)

## Ajustar la leyenda (título) y mostrar la gráfica
plt.legend(title='Lambda')
plt.show()
```

#### 📜**Descripción del Código**

* **Cargar librerías**: Se utiliza `ggplot2` para crear las gráficas.
* **Definir un rango de valores para $ x $**: Se establece un rango de valores de $0 $ a $ 5 $.
* **Crear un data frame vacío**: Se inicializa una lista para almacenar los resultados de la $PDF$.
* **Valores de $ \lambda $**: Se definen diferentes valores de $ \lambda $ (en este caso, $ 0.5 $, $ 1 $ y $ 1.5 $).
* **Calcular la PDF**: Se utiliza `dexp()` para calcular la función de densidad de probabilidad para cada valor de $ \lambda $ y se almacena en el data frame.
* **Combinar data frames**: Se combinan todos los data frames en uno solo para facilitar la graficación.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $PDF$ de la distribución exponencial para diferentes valores de $\lambda$.

#### 🛠️Usos de la Distribución Exponencial

La distribución exponencial se utiliza en la teoría de la fiabilidad como el modelo más simple para la vida útil de equipos. Además, como se discutirá a continuación, el tiempo hasta el siguiente evento de un proceso de Poisson sigue la distribución exponencial. Por lo tanto, la distribución exponencial modela una amplia gama de tiempos de espera, como el tiempo hasta que llegue el próximo cliente a una estación de servicio, el tiempo hasta el próximo fallo de un banco o firma de inversión, el tiempo hasta el siguiente brote de hostilidades, el tiempo hasta el próximo terremoto, o el tiempo hasta que falle el siguiente componente de un sistema multi-componente.

#### Propiedad de Memoria

Una variable aleatoria no negativa $X$ tiene la propiedad de memoria, también llamada propiedad de no envejecimiento, si para todos $ s, t > 0 $:

$$
P(X > s + t | X > s) = P(X > t)
$$

**Se puede demostrar que la variable aleatoria exponencial tiene esta propiedad, y de hecho, es la única distribución con esta propiedad.**

#### Conexión Poisson-Exponencial

Para un proceso de Poisson, sea $ T_1 $ el tiempo en que ocurre el primer evento, y para $ i = 2, 3, \ldots $, $ T_i $ denota el tiempo transcurrido entre la ocurrencia del $(i-1)$-ésimo y el $i$-ésimo evento. Los tiempos $T_1, T_2, \ldots $ se llaman tiempos entre llegadas.

**Proposición 3.5-1**: Si $ X(s)$, $s \geq 0$, es un proceso de Poisson con tasa $ \alpha$, los tiempos entre llegadas tienen la distribución exponencial con PDF:

$$
f(t) = \alpha e^{-\alpha t}, \quad t > 0
$$

**Ejemplo 3.5-2**: Los logins de usuario a la red informática de una universidad se pueden modelar como un proceso de Poisson con una tasa de $10$ por minuto. Si el administrador del sistema comienza a rastrear el número de logins a las 10:00 a.m., encuentra la probabilidad de que el primer login registrado ocurra entre $10$ y $20$ segundos después.

**Solución**: Con el tiempo cero establecido en $10:00 a.m.$, sea $ T_1 $ el tiempo, en minutos, del primer registro. Dado que $ T_1 \sim \text{Exp}(10) $, la fórmula de la CDF nos da:

$$
P\left(\frac{10}{60} < T < \frac{20}{60}\right) = e^{-10 \times \frac{10}{60}} - e^{-10 \times \frac{20}{60}} = 0.1532.
$$

**EJERCICIO 9**

Agrega ejemplos y los usos recomendados.

### ⏳ Usos Recomendados de la Distribución Exponencial

La **Distribución Exponencial** modela el **tiempo** que transcurre antes de que ocurra un evento, en un proceso donde los eventos ocurren de forma **continua e independiente a una tasa constante** ($\lambda$). Es la única distribución continua "sin memoria", lo que significa que el tiempo que ya ha transcurrido no afecta la probabilidad del tiempo restante hasta el próximo evento.

1.  **Fiabilidad y Tiempos de Vida Útil**
    Es fundamental en ingeniería de fiabilidad para modelar el tiempo de vida de productos o componentes que **no sufren desgaste** (es decir, la probabilidad de fallo es constante, independientemente de cuánto tiempo hayan estado funcionando).

    * **Ejemplo:** El tiempo de vida de un **componente electrónico** (como un chip o un condensador) antes de que falle. Si la tasa de fallo ($\lambda$) es constante, la Distribución Exponencial calcula la probabilidad de que el componente dure **más de 5 años**.
    * **Aplicación:** Modelar el tiempo que un **servidor de red** funciona sin caerse o el tiempo de funcionamiento de una bombilla LED que no se ve afectada por el encendido y apagado constante.

2.  **Teoría de Colas y Atención al Cliente**
    Se utiliza para modelar el **tiempo entre llegadas** de clientes o el **tiempo de servicio** requerido, asumiendo un proceso de Poisson subyacente (donde las llegadas o servicios ocurren a una tasa promedio constante).

    * **Ejemplo:** En un centro de llamadas, si los clientes llegan a una tasa promedio de $\lambda = 5$ llamadas por hora, la Distribución Exponencial calcula la probabilidad de que el **tiempo de espera entre dos llamadas consecutivas** sea **menor a 5 minutos** (o $\frac{1}{12}$ de hora).
    * **Aplicación:** El tiempo que pasa entre el momento en que dos coches llegan a un peaje o el tiempo que un cajero tarda en atender a un cliente.

3.  **Procesos Aleatorios en Física y Biología**
    Aplica en cualquier fenómeno donde los eventos ocurren al azar, de manera independiente y a una tasa constante.

    * **Ejemplo:** Modelar el **tiempo que transcurre entre dos desintegraciones radioactivas** consecutivas de un material.
    * **Aplicación:** El tiempo entre la llegada de dos **partículas cósmicas** a un detector o el tiempo entre dos **mutaciones** en una secuencia de ADN.

---

## 🔗 Relación con la Distribución de Poisson

La **Distribución Exponencial** y la **Distribución de Poisson** están íntimamente ligadas:

* La **Distribución de Poisson** modela el **número de eventos** ($k$) que ocurren en un intervalo de tiempo fijo (por ejemplo, el número de clientes que llegan en 1 hora).
* La **Distribución Exponencial** modela el **tiempo de espera** ($t$) hasta el primer evento, o el tiempo entre eventos sucesivos, en ese mismo proceso.

Si una **tasa de eventos promedio** de Poisson es $\lambda$ (eventos por unidad de tiempo), la distribución exponencial utiliza $\lambda$ como su parámetro de tasa para modelar la duración del tiempo entre esos eventos.

### 💻Ejemplos en codigo

```python
from scipy.stats import expon

## ====================================================================
## 1. Fiabilidad y Tiempos de Vida Útil (Componente Electrónico)
## ====================================================================
print("--- 1. Fiabilidad (Vida Útil) ---")

## Tasa de fallo (lambda) de un componente: 0.1 fallos por año
tasa_lambda = 0.1
## El parámetro de escala (beta o 1/lambda) es 1 / 0.1 = 10 años
escala_beta = 1 / tasa_lambda
tiempo_interes = 5  # Queremos P(X > 5 años)

## Calcular P(X > 5) = 1 - CDF(5)
## La función .sf() (Survival Function) es equivalente a 1 - CDF(x)
prob_mayor_5_años = expon.sf(tiempo_interes, scale=escala_beta)

print(f"Parámetros: Tasa (λ) = {tasa_lambda} por año")
print(f"Escala (β) = {escala_beta} años")
print(f"Probabilidad de que el componente dure más de {tiempo_interes} años (P(X > 5)): {prob_mayor_5_años:.4f}")

## ====================================================================
## 2. Teoría de Colas (Tiempo entre Llamadas Consecutivas)
## ====================================================================
print("\n--- 2. Teoría de Colas (Tiempo entre Llamadas) ---")

## Tasa de llegada (lambda): 5 llamadas por hora
tasa_lambda_hr = 5
## Escala (beta) en horas: 1 / 5 = 0.2 horas
escala_beta_hr = 1 / tasa_lambda_hr

## Tiempo de interés: 5 minutos. Convertir a horas: 5 / 60 = 1/12 horas ≈ 0.0833 horas
tiempo_interes_min = 5
tiempo_interes_hr = tiempo_interes_min / 60

## Queremos P(X < 5 minutos) = CDF(1/12 horas)
prob_menor_5_min = expon.cdf(tiempo_interes_hr, scale=escala_beta_hr)

print(f"Parámetros: Tasa (λ) = {tasa_lambda_hr} por hora")
print(f"Tiempo de interés: {tiempo_interes_min} minutos ({tiempo_interes_hr:.4f} horas)")
print(f"Probabilidad de que el tiempo entre llamadas sea menor a {tiempo_interes_min} minutos (P(X < 1/12)): {prob_menor_5_min:.4f}")

## ====================================================================
## 3. Procesos Aleatorios (Tiempo entre Desintegraciones Radioactivas)
## ====================================================================
print("\n--- 3. Procesos Aleatorios (Tiempo entre Desintegraciones) ---")

## Tasa de desintegración (ejemplo): 0.05 desintegraciones por segundo
tasa_lambda_radio = 0.05
## Escala (beta) en segundos: 1 / 0.05 = 20 segundos
escala_beta_radio = 1 / tasa_lambda_radio

## Calculemos el tiempo medio entre desintegraciones
media_exponencial = escala_beta_radio

## Calculemos la probabilidad de que el tiempo entre desintegraciones sea mayor a 30 segundos
tiempo_interes_radio = 30
prob_mayor_30_seg = expon.sf(tiempo_interes_radio, scale=escala_beta_radio)

print(f"Parámetros: Tasa (λ) = {tasa_lambda_radio} por segundo")
print(f"Tiempo medio esperado entre desintegraciones (E[X]): {media_exponencial:.2f} segundos")
print(f"Probabilidad de que el tiempo entre desintegraciones sea mayor a {tiempo_interes_radio} segundos (P(X > 30)): {prob_mayor_30_seg:.4f}")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

## Configuración de los gráficos
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(3, 1, figsize=(10, 15))
fig.suptitle('Ejemplos de la Distribución Exponencial', fontsize=16, y=1.02)

## ====================================================================
## 1. Fiabilidad y Tiempos de Vida Útil (Componente Electrónico)
## ====================================================================

## Tasa de fallo (lambda) de un componente: 0.1 fallos por año
tasa_lambda = 0.1
## El parámetro de escala (beta o 1/lambda) es 1 / 0.1 = 10 años
escala_beta = 1 / tasa_lambda
tiempo_interes = 5  # Queremos P(X > 5 años)

## Calcular la probabilidad P(X > 5)
## P(X > x) = 1 - CDF(x)
prob_mayor_5_años = 1 - expon.cdf(tiempo_interes, scale=escala_beta)

## Generar puntos para la PDF (función de densidad)
x_pdf = np.linspace(0, 40, 200)
y_pdf = expon.pdf(x_pdf, scale=escala_beta)

ax = axes[0]
ax.plot(x_pdf, y_pdf, color='blue', label=f'PDF Exponencial (λ={tasa_lambda})')

## Rellenar el área de interés P(X > 5)
ax.fill_between(x_pdf, y_pdf, where=(x_pdf > tiempo_interes),
                color='lightblue', alpha=0.6,
                label=f'P(X > {tiempo_interes}) = {prob_mayor_5_años:.3f}')

ax.set_title('1. Probabilidad de que un Componente Dure más de 5 años')
ax.set_xlabel('Vida Útil (años)')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## ====================================================================
## 2. Teoría de Colas (Tiempo entre Llamadas Consecutivas)
## ====================================================================

## Tasa de llegada (lambda): 5 llamadas por hora
tasa_lambda_hr = 5
## Escala (beta) en horas: 1 / 5 = 0.2 horas
escala_beta_hr = 1 / tasa_lambda_hr

## Tiempo de interés: 5 minutos. Convertir a horas: 5 / 60 = 1/12 horas
tiempo_interes_hr = 5 / 60
## Queremos P(X < 1/12 horas)

## Calcular la probabilidad P(X < 1/12)
prob_menor_5_min = expon.cdf(tiempo_interes_hr, scale=escala_beta_hr)

## Generar puntos para la PDF (en minutos para la gráfica)
x_min = np.linspace(0, 40, 200) # De 0 a 40 minutos
x_hr_pdf = x_min / 60
y_pdf_min = expon.pdf(x_hr_pdf, scale=escala_beta_hr)

ax = axes[1]
ax.plot(x_min, y_pdf_min, color='green', label=f'PDF Exponencial (λ={tasa_lambda_hr} por hr)')

## Rellenar el área de interés P(X < 5 minutos)
ax.fill_between(x_min, y_pdf_min, where=(x_min < 5),
                color='lightgreen', alpha=0.6,
                label=f'P(Tiempo < 5 min) = {prob_menor_5_min:.3f}')

ax.set_title('2. Probabilidad del Tiempo de Espera entre dos Llamadas (λ=5/hr)')
ax.set_xlabel('Tiempo entre Llamadas (minutos)')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## ====================================================================
## 3. Simulación de Tiempos de Desintegración Radioactiva (Proceso Aleatorio)
## ====================================================================

## Tasa de desintegración (ejemplo): 0.05 desintegraciones por segundo
tasa_lambda_radio = 0.05
escala_beta_radio = 1 / tasa_lambda_radio
n_simulaciones_radio = 1000

## Simular 1000 tiempos entre desintegraciones
tiempos_desintegracion = expon.rvs(scale=escala_beta_radio, size=n_simulaciones_radio)

ax = axes[2]
ax.hist(tiempos_desintegracion, bins=50, density=True, color='purple', edgecolor='black', alpha=0.7,
        label='Simulación de Tiempos')
ax.plot(x_pdf, expon.pdf(x_pdf, scale=escala_beta_radio),
        color='red', linestyle='--', linewidth=2, label='PDF Teórica')

ax.set_title(f'3. Simulación del Tiempo entre Desintegraciones (λ={tasa_lambda_radio}/seg)')
ax.set_xlabel('Tiempo entre Eventos (segundos)')
ax.set_ylabel('Densidad de Probabilidad')
ax.set_xlim(0, 40)
ax.legend()

## Ajustar diseño y mostrar
plt.tight_layout()
plt.show()
```

### ✨Distribución Normal

* **Descripción**: La distribución normal es una distribución continua caracterizada por su forma simétrica y campaniforme. Se denota como $X \sim N(\mu, \sigma^2)$, donde $\mu$ es la media y $\sigma$ es la desviación estándar.

* **Parámetros**:
- $\mu $ (media)
- $\sigma $ (desviación estándar)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
$$

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) = \int_{-\infty}^{x} f(t) dt
$$

* **Valor Esperado**: $E[X] = \mu$

* **Media**:$\mu_X = \mu$

**Desviación Estándar**: $\sigma_X = \sigma$

* **Percentiles**: $x_\alpha = \mu + \sigma z_\alpha$

* **Propiedad del 68-95-99.7%**:
 - Aproximadamente el $68\%$ de los valores caen dentro de $ \mu \pm 1\sigma $.
 - Aproximadamente el $95\%$ de los valores caen dentro de $ \mu \pm 2\sigma $.
 - Aproximadamente el $99.7\%$ de los valores caen dentro de $\mu \pm 3\sigma $.

* **Comandos en R**:
```r
## PDF
 dnorm(x, mean = mu, sd = sigma)

## CDF
 pnorm(x, mean = mu, sd = sigma)

## Percentiles
 qnorm(s, mean = mu, sd = sigma)

## Simulación
 rnorm(n, mean = mu, sd = sigma)

```python
import numpy as np
from scipy.stats import norm

## ----------------------------------------
## Definición de parámetros
mu = 5     # media (mean en R, loc en Python)
sigma = 2  # desviación estándar (sd en R, scale en Python)
x = 7      # valor para PDF/CDF
s = 0.95   # percentil (quantile)
n = 10     # número de muestras para simulación

## ----------------------------------------
## PDF (Función de Densidad de Probabilidad)
## dnorm(x, mean = mu, sd = sigma)
## scipy.stats.norm.pdf(x, loc=mu, scale=sigma)
pdf_value = norm.pdf(x, loc=mu, scale=sigma)
print(f"PDF (norm.pdf) para x={x}: {pdf_value}")

## ----------------------------------------
## CDF (Función de Distribución Acumulada)
## pnorm(x, mean = mu, sd = sigma)
## scipy.stats.norm.cdf(x, loc=mu, scale=sigma)
cdf_value = norm.cdf(x, loc=mu, scale=sigma)
print(f"CDF (norm.cdf) para x={x}: {cdf_value}")

## ----------------------------------------
## Percentiles (Función Cuantil)
## qnorm(s, mean = mu, sd = sigma)
## scipy.stats.norm.ppf(s, loc=mu, scale=sigma)
percentile_value = norm.ppf(s, loc=mu, scale=sigma)
print(f"Percentil (norm.ppf) para s={s}: {percentile_value}")

## ----------------------------------------
## Simulación/Muestreo
## rnorm(n, mean = mu, sd = sigma)
## np.random.normal(loc=mu, scale=sigma, size=n)
samples = np.random.normal(loc=mu, scale=sigma, size=n)
print(f"Muestras (np.random.normal) n={n}: {samples}")
```

#### 🔍Ejemplo de Gráfica de la Distribución Normal

La distribución normal es una de las distribuciones de probabilidad más importantes en estadística, describiendo la variabilidad de muchos fenómenos naturales. Se caracteriza por su forma de campana y es definida por dos parámetros: la media $\mu $ y la desviación estándar $ \sigma $.

En esta gráfica, se presentan diferentes funciones de densidad de probabilidad $ PDF$ de la distribución normal para varios valores de $ \mu $ y $ \sigma $. A medida que la media $ \mu $ se desplaza, el centro de la campana se mueve, mientras que un aumento en la desviación estándar $ \sigma $ ensancha la distribución, indicando una mayor dispersión de los datos. Esto permite modelar una amplia gama de fenómenos, desde la altura de las personas hasta los errores de medición.

```python
"""

## Cargar librerías necesarias
library(ggplot2)

## Definir un rango de valores para x
x <- seq(-10, 10, by = 0.1)

## Definir diferentes valores de media (mu) y desviación estándar (sigma)
params <- data.frame(mu = c(-2, 0, 2), sigma = c(1, 1, 1.5))

## Crear un data frame vacío para almacenar los resultados de la PDF
pdf_data <- data.frame()

## Calcular la PDF para cada combinación de mu y sigma
for (i in 1:nrow(params)) {
  mu <- params$mu[i]
  sigma <- params$sigma[i]

## Calcular la función de densidad de probabilidad
  pdf_values <- dnorm(x, mean = mu, sd = sigma)

## Almacenar los resultados en un data frame
  pdf_data <- rbind(pdf_data, data.frame(x = x, y = pdf_values, mu = mu, sigma = sigma))
}

## Graficar la distribución normal
ggplot(pdf_data, aes(x = x, y = y, color = as.factor(mu), linetype = as.factor(sigma))) +
  geom_line(size = 1) +
  labs(title = "Funciones de Densidad de Probabilidad de la Distribución Normal",
       x = "Valor",
       y = "Densidad",
       color = "Media (mu)",
       linetype = "Desviación Estándar (sigma)") +
  theme_minimal() +
  scale_color_manual(values = c("blue", "red", "green")) +
  theme(legend.position = "top")

"""
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

## ----------------------------------------
## 1. Definir un rango de valores para x (equivalente a seq() en R)
x = np.linspace(-10, 10, 201) # 201 puntos para tener una línea suave

## ----------------------------------------
## 2. Definir diferentes valores de media (mu) y desviación estándar (sigma)
## Se usa un diccionario para crear el DataFrame de parámetros
params_data = {'mu': [-2, 0, 2], 'sigma': [1, 1, 1.5]}
params = pd.DataFrame(params_data)

## ----------------------------------------
## 3. Crear una lista para almacenar los DataFrames de PDF
pdf_data_list = []

## 4. Calcular la PDF para cada combinación de mu y sigma (equivalente al bucle for)
for index, row in params.iterrows():
    mu = row['mu']      # Media (loc en Python)
    sigma = row['sigma']  # Desviación Estándar (scale en Python)

## Calcular la función de densidad de probabilidad (equivalente a dnorm() en R)
## loc=mu y scale=sigma
    pdf_values = norm.pdf(x, loc=mu, scale=sigma)

## Almacenar los resultados en un DataFrame temporal
    df_temp = pd.DataFrame({
        'x': x,
        'y': pdf_values,
        'mu': mu,
        'sigma': sigma
    })
    pdf_data_list.append(df_temp)

## 5. Combinar todos los DataFrames en uno solo (equivalente a rbind() en R)
pdf_data = pd.concat(pdf_data_list, ignore_index=True)

## ----------------------------------------
## 6. Graficar la distribución normal (equivalente a ggplot2)

## Configurar el estilo (similar a theme_minimal())
sns.set_style("whitegrid")

plt.figure(figsize=(10, 6))

## Diccionario para mapear mu a colores (equivalente a scale_color_manual)
color_map = {-2: "blue", 0: "red", 2: "green"}

## Crear la gráfica con Seaborn. Se usan 'hue' y 'style' para mapear estéticas:
## hue: mapea a color (mu)
## style: mapea a estilo de línea (sigma)
sns.lineplot(
    data=pdf_data,
    x='x',
    y='y',
    hue='mu',
    style='sigma',  # Usamos 'style' para linetype
    palette=color_map # Corrected palette argument
)

## Añadir titles and labels (equivalent to labs())
plt.title("Funciones de Densidad de Probabilidad de la Distribución Normal", fontsize=16)
plt.xlabel("Valor", fontsize=14)
plt.ylabel("Densidad", fontsize=14)

## Position the legend at the top (equivalent to theme(legend.position = "top"))
plt.legend(title="Parámetros (mu, sigma)")

## Show the plot
plt.show()
```

#### 📜**Descripción del Código**

* **Cargar librerías**: Se utiliza `ggplot2` para crear las gráficas.
* **Definir un rango de valores para $ x $**: Se establece un rango de valores de $-10$ a $10$.
* **Definir los parámetros**: Se establecen diferentes valores de media $ \mu $ y desviación estándar $ \sigma $ para la distribución normal.
* **Crear un data frame vacío**: Se inicializa un data frame para almacenar los resultados de la $PDF$.
* **Calcular la PDF**: Se utiliza `dnorm()` para calcular la función de densidad de probabilidad para cada combinación de $ \mu $ y $ \sigma $.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $ PDF $ de la distribución normal para diferentes valores de $ \mu $ y $ \sigma $.

#### ⭐Otras Características de la DISTRIBUCIÓN NORMAL

Una variable aleatoria se dice que tiene la distribución normal estándar si su PDF y CDF, que se denotan (universalmente) por $\phi$ y $\Phi$, respectivamente, son

$$
\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2} \quad \text{y} \quad \Phi(z) = \int_{-\infty}^{z} \phi(x) \, dx
$$

para $-\infty < z < \infty$. Una variable aleatoria normal estándar se denota por $Z$.

Una variable aleatoria $X$ se dice que tiene la distribución normal, con parámetros $\mu$ y $\sigma$, denotada por $X \sim N(\mu, \sigma^2)$, si su PDF y CDF son

$$
f(x) = \frac{1}{\sigma} \phi\left(\frac{x - \mu}{\sigma}\right) \quad \text{y} \quad F(x) = \Phi\left(\frac{x - \mu}{\sigma}\right)
$$

para $-\infty < x < \infty$. Así,

$$
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}},
$$

que es simétrico respecto a $\mu$. Por lo tanto, $\mu$ es tanto la media, la mediana como la moda de $X$. El parámetro $\sigma$ es la desviación estándar de $X$. Para $\mu = 0$ y $\sigma = 1$, $X$ es normal estándar y se denota por $Z$.

El PDF normal es difícil de integrar y no se utilizará para calcular probabilidades mediante integración. Además, la CDF no tiene una expresión en forma cerrada.

En los comandos de R, tanto $x$ como $s$ pueden ser vectores. Por ejemplo, si $X \sim N(5, 16)$,
* `dnorm(6, 5, 4)` devuelve $0.09666703$ para el valor de la PDF de $X$ en $x = 6$.
* `pnorm(c(3, 6), 5, 4)` devuelve los valores de $P(X \leq 3)$ y $P(X \leq 6)$.
* `qnorm(c(0.9, 0.99), 5, 4)` devuelve $10.12621$ y $14.30539$ para el percentil $90$ y $99$ de $X$, respectivamente.

La PDF normal estándar $\Phi(z)$ se tabula en la **Tabla A.3** para valores de $z$ de $0$ a $3.09$ en incrementos de $0.01$. En el resto de esta sección aprenderemos a usar la **Tabla A.3** no solo para encontrar probabilidades y percentiles de la variable aleatoria normal estándar, sino para cualquier otra variable normal. La capacidad de usar solo una tabla, la de la normal estándar, para encontrar probabilidades y percentiles de cualquier variable normal se debe a una propiedad interesante de la distribución normal, que se presenta en la siguiente proposición.

**Proposición 3.5-2** Si $X \sim N(\mu, \sigma^2)$ y $a, b$ son números reales, entonces

$$
a + bX \sim N(a + b\mu, b^2\sigma^2). \tag{3.5.4}
$$

El nuevo elemento de esta proposición es que una transformación lineal de una variable aleatoria normal también es una variable aleatoria normal. Que el valor medio y la varianza de la variable transformada, $Y = a + bX$, son $a + b\mu$ y $b^2\sigma^2$, respectivamente, se sigue de las Proposiciones 3.3-1 y 3.3-2, por lo que no hay nada nuevo en estas fórmulas.

**Encontrando Probabilidades**

 Primero ilustramos el uso de la Tabla A.3 para encontrar probabilidades asociadas con la variable aleatoria normal estándar.

**Ejemplo 3.5-3** Sea $Z \sim N(0, 1)$. Encuentra

 (a) $P(-1 < Z < 1)$,

 (b) $P(-2 < Z < 2)$ y

 (c) $P(-3 < Z < 3)$.

**Solución** En la Tabla A.3, los valores de $z$ están listados con dos decimales, con el segundo decimal identificado en la fila superior de la tabla. Así, el valor $z$ igual a $1$ se identifica por $1.0$ en la columna izquierda de la tabla y $0.00$ en la fila superior de la tabla. La probabilidad $\Phi(1) = P(Z \leq 1)$ es el número que corresponde a la fila y la columna identificadas por $1.0$ y $0.00$, que es $0.8413$. Dado que los valores negativos no están listados en la Tabla A.3, $\Phi(-1) = P(Z \leq -1)$ se encuentra aprovechando el hecho de que la distribución normal estándar es simétrica respecto a cero. Esto significa que el área bajo la PDF de $N(0, 1)$ a la izquierda de $-1$ es igual al área bajo ella a la derecha de $1$. Por lo tanto,

$$
\Phi(-1) = 1 - \Phi(1),
$$

y la misma relación se mantiene con cualquier número positivo que sustituya a 1. Así, la respuesta a la parte (a) es

$$
P(-1 < Z < 1) = \Phi(1) - \Phi(-1) = 0.8413 - (1 - 0.8413) = 0.8413 - 0.1587 = 0.6826.
$$

Trabajando de manera similar, encontramos las siguientes respuestas para las partes (b) y (c):
$$
P(-2 < Z < 2) = \Phi(2) - \Phi(-2) = 0.9772 - 0.0228 = 0.9544,
$$
y
$$
P(-3 < Z < 3) = \Phi(3) - \Phi(-3) = 0.9987 - 0.0013 = 0.9974.
$$

Por lo tanto, aproximadamente el $68\%$ de los valores de una variable aleatoria normal estándar caen dentro de una desviación estándar de su media, aproximadamente el $95\%$ caen dentro de dos desviaciones estándar de su media, y aproximadamente el $99.7\%$ de sus valores caen dentro de tres desviaciones estándar de su media. Esto se conoce como la regla del $68-95-99.7\%.$

El uso de la Tabla A.3 para encontrar probabilidades asociadas con cualquier variable normal es posible a través del siguiente corolario de la Proposición 3.5-2.

**Corolario 3.5-1** Si $X \sim N(\mu, \sigma^2)$, entonces
* $X - \mu \sim N(0, \sigma^2)$, y
* $P(a \leq X \leq b) = \Phi\left(\frac{b - \mu}{\sigma}\right) - \Phi\left(\frac{a - \mu}{\sigma}\right)$.

Para mostrar cómo el corolario se deriva de la Proposición 3.5-2, primero aplicamos la fórmula (3.5.4) con $a = -\mu$ y $b = 1$ para ver que si $X \sim N(\mu, \sigma^2)$, entonces

$$
X - \mu \sim N(0, \sigma^2).
$$

Una segunda aplicación de la fórmula (3.5.4) con $a = 0$ y $b = \frac{1}{\sigma}$, para el resultado anterior, implica que $\frac{X - \mu}{\sigma} \sim N(0, 1)$ (la normal estándar, $Z$). Por lo tanto, al restarle su media y dividirla por su desviación estándar, esto implica que cualquier evento de la forma $a \leq X \leq b$ se puede expresar en términos de la variable estandarizada:

$$
[a \leq X \leq b] = \left[\frac{a - \mu}{\sigma} \leq \frac{X - \mu}{\sigma} \leq \frac{b - \mu}{\sigma}\right].
$$

Así, la parte (2) del Corolario 3.5-1 se sigue de

$$
P(a \leq X \leq b) = P\left(\frac{a - \mu}{\sigma} \leq \frac{X - \mu}{\sigma} \leq \frac{b - \mu}{\sigma}\right) = \Phi\left(\frac{b - \mu}{\sigma}\right) - \Phi\left(\frac{a - \mu}{\sigma}\right),
$$
donde la última igualdad se deriva del hecho de que $\frac{(X - \mu)}{\sigma}$ tiene la distribución normal estándar.

**Ejemplo 3.5-4** Sea $X \sim N(1.25, 0.462)$. Encuentra (a) $P(1 \leq X \leq 1.75)$ y (b) $P(X > 2)$.

**Solución** Una aplicación directa de la parte (2) del Corolario 3.5-1 da lugar a

$$
P(1 \leq X \leq 1.75) = \Phi\left(\frac{1.75 - 1.25}{0.46}\right) - \Phi\left(\frac{1 - 1.25}{0.46}\right) = \Phi(1.09) - \Phi(-0.54) = 0.8621 - 0.2946 = 0.5675.
$$

Trabajando de manera similar para el evento en la parte (b), tenemos

$$
P(X > 2) = P\left(Z > \frac{2 - 1.25}{0.46}\right) = 1 - \Phi(1.63) = 0.0516.
$$

Otra consecuencia del Corolario 3.5-1 es que la regla del 68-95-99.7\% de la normal estándar vista en el Ejemplo 3.5-3 se aplica para cualquier variable aleatoria normal $X \sim N(\mu, \sigma^2)$:

$$
P(\mu - 1\sigma < X < \mu + 1\sigma) = P(-1 < Z < 1) = 0.6826,
$$
$$
P(\mu - 2\sigma < X < \mu + 2\sigma) = P(-2 < Z < 2) = 0.9544,
$$
y
$$
P(\mu - 3\sigma < X < \mu + 3\sigma) = P(-3 < Z < 3) = 0.9974.
$$

**Encontrando Percentiles**

 De acuerdo con la notación introducida en la Definición 3.3-1, el percentil $(1-\alpha)$-100 de $Z$ se denotará como $z_\alpha$. Por lo tanto, el área bajo la PDF normal estándar a la derecha de $z_\alpha$ es $\alpha$, como se muestra en el panel derecho de la Figura 3-16. El panel izquierdo de esta figura ilustra la propiedad definitoria de $z_\alpha$, es decir,

$$
\Phi(z_\alpha) = 1 - \alpha,
$$

que se utiliza para encontrar $z_\alpha$. Dado que la función $\Phi$ no tiene una expresión en forma cerrada, usamos la Tabla A.3 para resolver esta ecuación, localizando primero $1 - \alpha$ en el cuerpo de la tabla y luego leyendo $z_\alpha$ de los márgenes. Si el valor exacto de $1 - \alpha$ no existe en el cuerpo de la tabla, se utiliza una aproximación. Este proceso se demuestra en el siguiente ejemplo.

**Ejemplo 3.5-5** Encuentra el percentil $95$ de $Z$.

**Solución**

Aquí $\alpha = 0.05$, así que $1 - \alpha = 0.95$. Sin embargo, el número exacto $0.95$ no existe en el cuerpo de la Tabla A.3. Así que usamos la entrada que es más cercana pero mayor que $0.95$ (que es $0.9505$), así como la entrada que es más cercana pero menor que $0.95$ (que es $0.9495$), y aproximamos $z_{0.05}$ promediando los valores de $z$ que corresponden a estas dos entradas más cercanas:

$$
z_{0.05} \approx \frac{1.64 + 1.65}{2} = 1.645.
$$

El uso de la Tabla A.3 para encontrar percentiles de cualquier variable normal se hace posible a través del siguiente corolario a la Proposición 3.5-2.

**Corolario 3.5-2** Sea $X \sim N(\mu, \sigma^2)$, y sea $x_\alpha$ el percentil $(1 - \alpha)$-100 de $X$. Entonces,

$$
x_\alpha = \mu + \sigma z_\alpha. \tag{3.5.5}
$$

Para la prueba de este corolario, debe mostrarse que $P(X \leq \mu + \sigma z_\alpha) = 1 - \alpha$. Pero esto sigue de la aplicación de la parte (2) del Corolario 3.5-1 con $a = -\infty$ y $b = \mu + \sigma z_\alpha$:

$$
P(X \leq \mu + \sigma z_\alpha) = \Phi(z_\alpha) - \Phi(-\infty) = 1 - \alpha - 0 = 1 - \alpha.
$$

**Ejemplo 3.5-6** Sea $X \sim N(1.25, 0.462)$. Encuentra el percentil $95$, $x_{0.05}$, de $X$.

**Solución** De (3.5.5) tenemos

$$
x_{0.05} = 1.25 + 0.46 z_{0.05} = 1.25 + (0.46)(1.645) = 2.01.
$$

### 🔔 Usos Recomendados de la Distribución Normal (Campana de Gauss)

La **Distribución Normal** $\text{N}(\mu, \sigma^2)$, también conocida como la **Campana de Gauss**, es la distribución de probabilidad continua más importante. Modela el comportamiento de muchas variables aleatorias donde la mayoría de los valores se agrupan alrededor de un valor **central (la media $\mu$)** y los valores extremos son progresivamente menos probables. Esta concentración de datos ocurre debido al **Teorema del Límite Central**, que establece que la media de muchas variables aleatorias independientes y con idéntica distribución tiende a distribuirse normalmente, independientemente de la forma original de la distribución.

1.  **Modelado de Fenómenos Naturales y Biológicos**
    Es el modelo fundamental para cualquier característica física o biológica que resulta de la acumulación de muchos factores aleatorios e independientes, donde los valores se agrupan en torno a un promedio.

    * **Ejemplo:** La **estatura** de los hombres adultos en un país. La mayoría tendrá una altura cercana al promedio ($\mu$), y muy pocos serán extremadamente altos o extremadamente bajos. La distribución calcula, por ejemplo, el porcentaje de la población que mide **más de 1.90 metros**.
    * **Aplicación:** El **peso al nacer** de los bebés, el **coeficiente intelectual (CI)** de una población, la **presión sanguínea** en adultos, o el **diámetro** de las mandarinas cosechadas en una finca.

2.  **Control de Calidad y Procesos de Fabricación**
    Se utiliza para establecer límites de tolerancia y evaluar la consistencia en la producción, asumiendo que las variaciones o errores de medición son aleatorios.

    * **Ejemplo:** Una máquina de llenado está configurada para llenar botellas con un promedio ($\mu$) de **500 ml** y una desviación estándar ($\sigma$) de **2 ml**. La distribución Normal calcula la probabilidad de que una botella individual sea **rechazada** porque contiene **menos de 495 ml** (fuera de la tolerancia aceptada).
    * **Aplicación:** Evaluar la **precisión** de una máquina que corta piezas metálicas o el **tiempo medio** que le toma a un empleado realizar una tarea.

3.  **Inferencia Estadística y Análisis de Muestras**
    Es la base de la mayoría de los métodos de **inferencia estadística** (intervalos de confianza y pruebas de hipótesis), ya que las distribuciones de muchas estadísticas de muestra (como la media muestral) tienden a ser Normales, incluso si la población original no lo es (por el Teorema del Límite Central).

    * **Ejemplo:** Un investigador toma una muestra de 100 estudiantes y encuentra una **nota promedio** de 7.5. Usando la distribución Normal (o la t-Student, que se basa en ella), el investigador puede construir un **intervalo de confianza** para estimar la verdadera nota promedio de **todos los estudiantes** en el país.
    * **Aplicación:** Analizar los **errores de medición** en experimentos científicos, modelar el **rendimiento de los activos financieros** a corto plazo (asumiendo que los cambios son aleatorios) o la distribución de las **puntuaciones de un examen estandarizado**.

---
### 📏 La Regla Empírica (68-95-99.7)

Una propiedad clave de la Distribución Normal es la **Regla Empírica**, que permite una interpretación rápida de la dispersión de los datos:

* Aproximadamente el **68%** de los datos se encuentran dentro de **1 desviación estándar** ($\mu \pm 1\sigma$) de la media.
* Aproximadamente el **95%** de los datos se encuentran dentro de **2 desviaciones estándar** ($\mu \pm 2\sigma$) de la media.
* Aproximadamente el **99.7%** de los datos se encuentran dentro de **3 desviaciones estándar** ($\mu \pm 3\sigma$) de la media.

**EJERCICIO 10**

Agrega ejemplos y los usos recomendados.

### 💻Ejemplos en codigo

```python
from scipy.stats import norm
import numpy as np

## ====================================================================
## 1. Modelado de Estatura (Fenómenos Biológicos)
## ====================================================================
print("--- 1. Modelado de Estatura ---")

## Parámetros: Estatura media (μ) y Desviación estándar (σ) en metros
mu_estatura = 1.75
sigma_estatura = 0.08  # 8 cm
estatura_interes = 1.90  # Queremos P(X > 1.90m)

## 1a. Calcular P(X > 1.90) = 1 - CDF(1.90)
## Usamos .sf() (Survival Function) que es 1 - CDF
prob_mas_de_1_90 = norm.sf(estatura_interes, loc=mu_estatura, scale=sigma_estatura)

## 1b. Calcular el valor Z para 1.90m
valor_z = (estatura_interes - mu_estatura) / sigma_estatura

print(f"Media (μ) = {mu_estatura}m, Desv. Est. (σ) = {sigma_estatura}m")
print(f"Probabilidad de medir más de {estatura_interes}m (P(X > 1.90)): {prob_mas_de_1_90:.4f}")
print(f"El valor Z correspondiente a 1.90m es: {valor_z:.2f}")

## ====================================================================
## 2. Control de Calidad (Volumen de Llenado)
## ====================================================================
print("\n--- 2. Control de Calidad (Volumen de Llenado) ---")

## Parámetros: Volumen medio (μ) y Desviación estándar (σ) en ml
mu_volumen = 500
sigma_volumen = 2
volumen_rechazo = 495  # Queremos P(X < 495 ml)

## 2a. Calcular P(X < 495) = CDF(495)
prob_rechazo = norm.cdf(volumen_rechazo, loc=mu_volumen, scale=sigma_volumen)

## 2b. Calcular el volumen que corresponde al percentil 1 (el 1% más bajo)
percentil_rechazo = 0.01
volumen_percentil_1 = norm.ppf(percentil_rechazo, loc=mu_volumen, scale=sigma_volumen)

print(f"Media (μ) = {mu_volumen} ml, Desv. Est. (σ) = {sigma_volumen} ml")
print(f"Probabilidad de rechazo (P(X < {volumen_rechazo} ml)): {prob_rechazo:.4f}")
print(f"Para mantener el rechazo al 1%, el volumen de corte debería ser: {volumen_percentil_1:.2f} ml")

## ====================================================================
## 3. Inferencia y Regla Empírica
## ====================================================================
print("\n--- 3. Inferencia y Regla Empírica (68-95-99.7) ---")

## Se usa la Normal Estándar N(0, 1) para la regla empírica
mu_std = 0
sigma_std = 1

## 3a. P(μ - 1σ < X < μ + 1σ) -> P(-1 < Z < 1)
prob_1_sigma = norm.cdf(1, loc=mu_std, scale=sigma_std) - norm.cdf(-1, loc=mu_std, scale=sigma_std)

## 3b. P(μ - 2σ < X < μ + 2σ) -> P(-2 < Z < 2)
prob_2_sigma = norm.cdf(2, loc=mu_std, scale=sigma_std) - norm.cdf(-2, loc=mu_std, scale=sigma_std)

print(f"Porcentaje dentro de ±1 Desviación Estándar (μ ± 1σ): {prob_1_sigma * 100:.2f}% (Regla: 68%)")
print(f"Porcentaje dentro de ±2 Desviaciones Estándar (μ ± 2σ): {prob_2_sigma * 100:.2f}% (Regla: 95%)")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

## Configuración de los gráficos
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(3, 1, figsize=(10, 15))
fig.suptitle('Visualización de la Distribución Normal (Campana de Gauss)', fontsize=16, y=1.02)

## ====================================================================
## 1. Modelado de Estatura (P(X > 1.90m))
## ====================================================================
mu_estatura = 1.75
sigma_estatura = 0.08
estatura_interes = 1.90

## Generar puntos X (estatura)
x_estatura = np.linspace(mu_estatura - 4*sigma_estatura, mu_estatura + 4*sigma_estatura, 500)
## Calcular la PDF (altura de la campana)
y_pdf = norm.pdf(x_estatura, loc=mu_estatura, scale=sigma_estatura)

ax = axes[0]
ax.plot(x_estatura, y_pdf, color='blue')
ax.fill_between(x_estatura, y_pdf, where=(x_estatura > estatura_interes),
                color='lightblue', alpha=0.6,
                label='P(X > 1.90m)')
ax.axvline(mu_estatura, color='gray', linestyle='--', label=f'Media: {mu_estatura}m')
ax.axvline(estatura_interes, color='red', linestyle='-', label=f'Límite: {estatura_interes}m')

ax.set_title(f'1. Estatura de Hombres N({mu_estatura}, {sigma_estatura**2:.4f})')
ax.set_xlabel('Estatura (metros)')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## ====================================================================
## 2. Control de Calidad (P(X < 495ml))
## ====================================================================
mu_volumen = 500
sigma_volumen = 2
volumen_rechazo = 495

## Generar puntos X (volumen)
x_volumen = np.linspace(mu_volumen - 4*sigma_volumen, mu_volumen + 4*sigma_volumen, 500)
## Calcular la PDF
y_pdf_volumen = norm.pdf(x_volumen, loc=mu_volumen, scale=sigma_volumen)

ax = axes[1]
ax.plot(x_volumen, y_pdf_volumen, color='green')
ax.fill_between(x_volumen, y_pdf_volumen, where=(x_volumen < volumen_rechazo),
                color='lightgreen', alpha=0.6,
                label='P(Rechazo: X < 495ml)')
ax.axvline(mu_volumen, color='gray', linestyle='--', label=f'Media: {mu_volumen}ml')
ax.axvline(volumen_rechazo, color='red', linestyle='-', label=f'Tolerancia Mínima: {volumen_rechazo}ml')

ax.set_title(f'2. Control de Calidad (Llenado de Botellas) N({mu_volumen}, {sigma_volumen**2:.0f})')
ax.set_xlabel('Volumen (ml)')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## ====================================================================
## 3. Regla Empírica (68-95-99.7) - Normal Estándar
## ====================================================================
mu_std = 0
sigma_std = 1

## Generar puntos Z (Normal Estándar)
x_std = np.linspace(-4, 4, 500)
y_pdf_std = norm.pdf(x_std, loc=mu_std, scale=sigma_std)

ax = axes[2]
ax.plot(x_std, y_pdf_std, color='purple')

## Marcar el área de ±1σ (68%)
ax.fill_between(x_std, y_pdf_std, where=((x_std >= -1) & (x_std <= 1)),
                color='gold', alpha=0.4,
                label='±1σ (68.27%)')
## Marcar el área de ±2σ (95%)
ax.fill_between(x_std, y_pdf_std, where=((x_std >= -2) & (x_std <= 2)),
                color='orange', alpha=0.2,
                label='±2σ (95.45%)')

ax.axvline(mu_std, color='gray', linestyle='--', label='Media (Z=0)')
ax.axvline(1, color='red', linestyle=':', label='Z=1')
ax.axvline(-1, color='red', linestyle=':')

ax.set_title('3. Regla Empírica (68-95-99.7) en la Normal Estándar N(0, 1)')
ax.set_xlabel('Desviaciones Estándar (Z-Score)')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## Ajustar diseño y mostrar
plt.tight_layout()
plt.show()
```

### ✨Distribución Log-Normal

* **Descripción**: Modelo de variables aleatorias cuyo logaritmo sigue una distribución normal. Es útil para modelar variables que no pueden ser negativas y que tienen una distribución sesgada a la derecha.

* **Parámetros**:
  - $ \mu $ (media del logaritmo de la variable)
  - $ \sigma $ (desviación estándar del logaritmo de la variable)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x) =
\begin{cases}
\frac{1}{x \sigma \sqrt{2\pi}} e^{-\frac{(\log x - \mu)^2}{2\sigma^2}} & \text{si } x > 0 \\
0 & \text{si } x \leq 0
\end{cases}
$$

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) =
\begin{cases}
0 & \text{si } x \leq 0 \\
\Phi\left(\frac{\log x - \mu}{\sigma}\right) & \text{si } x > 0
\end{cases}
$$
donde $ \Phi $ es la función de distribución acumulativa de la distribución normal estándar.

* **Valor Esperado**: $ E[X] = e^{\mu + \frac{\sigma^2}{2}} $

* **Media**: $ \mu_X = e^{\mu + \frac{\sigma^2}{2}} $

* **Desviación Estándar**: $ \sigma_X = e^{\mu + \frac{\sigma^2}{2}} \sqrt{e^{\sigma^2} - 1} $

* **Percentiles**: $ x_\alpha = e^{\mu + \sigma \Phi^{-1}(\alpha)} $

**Comandos en R**:
```r
## PDF
dlnorm(x, meanlog = mu, sdlog = sigma)

## CDF
plnorm(x, meanlog = mu, sdlog = sigma)

## Simulación
rlnorm(n, meanlog = mu, sdlog = sigma)

```python
import numpy as np
from scipy.stats import lognorm

## ----------------------------------------
## Definición de parámetros (Log-espacio)
mu = 1.5      # media logarítmica (meanlog en R, loc en Python si no es 0)
sigma = 0.5   # desviación estándar logarítmica (sdlog en R, s en Python)
x = 10        # valor para PDF/CDF (en el espacio original)
n = 10        # número de muestras para simulación

## ----------------------------------------
## PDF (Función de Densidad de Probabilidad)
## dlnorm(x, meanlog = mu, sdlog = sigma)
## scipy.stats.lognorm.pdf(x, s=sigma, scale=np.exp(mu))
## NOTA: En scipy, 's' es sdlog, y 'scale' es exp(meanlog) para la media logarítmica.
pdf_value = lognorm.pdf(x, s=sigma, scale=np.exp(mu))
print(f"PDF (lognorm.pdf) para x={x}: {pdf_value}")

## ----------------------------------------
## CDF (Función de Distribución Acumulada)
## plnorm(x, meanlog = mu, sdlog = sigma)
## scipy.stats.lognorm.cdf(x, s=sigma, scale=np.exp(mu))
cdf_value = lognorm.cdf(x, s=sigma, scale=np.exp(mu))
print(f"CDF (lognorm.cdf) para x={x}: {cdf_value}")

## ----------------------------------------
## Simulación/Muestreo
## rlnorm(n, meanlog = mu, sdlog = sigma)
## np.random.lognormal(mean=mu, sigma=sigma, size=n)
## NOTA: np.random.lognormal usa 'mean' y 'sigma' directamente.
samples = np.random.lognormal(mean=mu, sigma=sigma, size=n)
print(f"Muestras (np.random.lognormal) n={n}: {samples}")
```

#### 🔍Ejemplo de Gráfica de la Distribución Log-Normal

La distribución log-normal describe un modelo en el que la variable aleatoria se distribuye normalmente en el logaritmo de sus valores. Esto significa que, si una variable $ X $ es log-normales, entonces $ \log(X) $ sigue una distribución normal. Esta distribución es útil en situaciones donde los datos son multiplicativos y no pueden ser negativos, como en la modelación de precios de activos o tiempos de vida de productos.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad $ PDF$ de la distribución log-normal para varios valores de los parámetros $ \mu $ y $ \sigma $, que representan la media y la desviación estándar de la distribución normal subyacente. A medida que se ajustan los valores de $ \mu $ y $\sigma $, la forma de la distribución cambia, reflejando cómo la variabilidad de los datos puede influir en su comportamiento.

La distribución log-normal es especialmente relevante en campos como la economía y la biología, donde se pueden observar fenómenos de crecimiento exponencial.

```python
"""

## Cargar librerías
library(ggplot2)

## Definir un rango de valores para x
x <- seq(0, 10, by = 0.01)

## Definir diferentes valores de mu y sigma
params <- data.frame(
  mu = c(0, 1, 2),
  sigma = c(0.5, 1, 1.5)
)

## Crear un data frame vacío para almacenar los resultados
results <- data.frame()

## Calcular la PDF para cada combinación de mu y sigma
for (i in 1:nrow(params)) {
  mu <- params$mu[i]
  sigma <- params$sigma[i]

  pdf_values <- dlnorm(x, meanlog = mu, sdlog = sigma)

  temp_df <- data.frame(x = x, PDF = pdf_values,
                        mu = mu, sigma = sigma)
  results <- rbind(results, temp_df)
}

## Graficar la PDF de la distribución log-normal
ggplot(results, aes(x = x, y = PDF, color = interaction(mu, sigma))) +
  geom_line(size = 1) +
  labs(title = "Distribución Log-Normal para Diferentes Parámetros",
       x = "x",
       y = "Densidad de Probabilidad (PDF)",
       color = "Parámetros (mu, sigma)") +
  theme_minimal()

"""
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import lognorm

## ----------------------------------------
## 1. Definir un rango de valores para x (equivalente a seq() en R)
x = np.linspace(0.01, 10, 1000) # Se inicia en 0.01 para evitar problemas con log(0)

## ----------------------------------------
## 2. Definir diferentes valores de mu (meanlog) y sigma (sdlog)
params_data = {
    'mu': [0, 1, 2],      # meanlog (mu)
    'sigma': [0.5, 1, 1.5] # sdlog (sigma)
}
params = pd.DataFrame(params_data)

## ----------------------------------------
## 3. Crear una lista para almacenar los DataFrames de PDF
results_list = []

## 4. Calcular la PDF para cada combinación de mu y sigma (bucle for)
for index, row in params.iterrows():
    mu = row['mu']
    sigma = row['sigma']

## Conversión de parámetros para Scipy:
## 's' es sigma (sdlog)
## 'scale' es exp(mu) (exp(meanlog))
    scale_param = np.exp(mu)

## Calcular la PDF (equivalente a dlnorm() en R)
    pdf_values = lognorm.pdf(x, s=sigma, scale=scale_param)

## Almacenar los resultados en un DataFrame temporal
    temp_df = pd.DataFrame({
        'x': x,
        'PDF': pdf_values,
        'mu': mu,
        'sigma': sigma,
## Crear una columna de interacción para el color (similar a R interaction(mu, sigma))
        'params_label': f"mu={mu}, sigma={sigma}"
    })
    results_list.append(temp_df)

## 5. Combinar todos los DataFrames en uno solo (equivalente a rbind() en R)
results = pd.concat(results_list, ignore_index=True)

## ----------------------------------------
## 6. Graficar la PDF de la distribución log-normal (equivalente a ggplot2)

## Configurar el estilo (theme_minimal)
sns.set_style("whitegrid")

plt.figure(figsize=(10, 6))

## Crear la gráfica con Seaborn, usando 'params_label' para el color
## 'hue' mapea los diferentes sets de parámetros al color de la línea
sns.lineplot(
    data=results,
    x='x',
    y='PDF',
    hue='params_label', # Usa la columna de interacción para el color
    linewidth=2
)

## Añadir títulos y etiquetas (labs)
plt.title("Distribución Log-Normal para Diferentes Parámetros", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("Densidad de Probabilidad (PDF)", fontsize=14)

## Ajustar la leyenda (el título se define con el parámetro 'hue' en lineplot)
plt.legend(title="Parámetros (mu, sigma)", loc='upper right', frameon=True)

## Mostrar la gráfica
plt.show()
```

#### 📜**Descripción del Código**

* **Cargar librerías**: Se utiliza `ggplot2` para crear la gráfica.
* **Definir un rango de valores para $ x $**: Se establece un rango de valores de $ 0 $ a $ 10 $.
* **Definir diferentes valores de $ \mu $ y $ \sigma $**: Se crean combinaciones de parámetros para la distribución log-normal.
* **Crear un data frame vacío**: Se inicializa un data frame para almacenar los resultados de la $PDF$.
* **Calcular la PDF**: Se utiliza `dlnorm()` para calcular la función de densidad de probabilidad para cada combinación de $ \mu $ y $ \sigma $.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $ PDF $ de la distribución log-normal para diferentes parámetros.

**EJERCICIO 11**

Agrega ejemplos y los usos recomendados.

### 📈 Usos Recomendados de la Distribución Log-Normal

La **Distribución Log-Normal** es la distribución de una variable aleatoria cuyo **logaritmo natural** sigue una Distribución Normal. Se caracteriza por ser **asimétrica a la derecha** (sesgada positivamente), es decir, tiene una cola larga a la derecha, y por no permitir valores negativos. Es ideal para modelar fenómenos que crecen de forma multiplicativa (en lugar de aditiva) o que están limitados por cero en el extremo inferior.

1.  **Economía y Finanzas (Rendimientos y Riqueza)**
    Es la distribución más utilizada para modelar variables que no pueden ser negativas y que tienen una alta variabilidad, como los precios de activos y los ingresos.

    * **Ejemplo:** El **precio de las acciones** a lo largo del tiempo. Los modelos financieros a menudo asumen que el **rendimiento logarítmico** de las acciones es Normal, lo que implica que el precio de las acciones en sí mismo sigue una distribución Log-Normal. Esto asegura que el precio de las acciones nunca caiga por debajo de cero, pero permite aumentos potencialmente muy grandes.
    * **Aplicación:** La **distribución de la riqueza** o el **ingreso salarial** en una población. La mayoría de las personas tienen ingresos modestos o medios, pero un pequeño número de individuos tiene ingresos extremadamente altos, creando el sesgo a la derecha característico de esta distribución.

2.  **Modelado de la Vida Útil y Fiabilidad (Desgaste)**
    A diferencia de la Distribución Exponencial (que modela fallos sin desgaste), la Log-Normal se utiliza cuando la **tasa de fallo de un componente aumenta con el tiempo** (hay un proceso de envejecimiento o fatiga).

    * **Ejemplo:** La **vida útil de componentes mecánicos o eléctricos** que se deterioran con el uso, como los motores, los rodamientos o los neumáticos. La distribución Log-Normal calcula la probabilidad de que un componente falle **después** de cierto número de horas de operación debido al desgaste acumulado.
    * **Aplicación:** Modelar el **tiempo hasta el fallo por fatiga** de materiales bajo estrés repetido.

3.  **Procesos Biológicos y Ambientales**
    Aplica a cualquier variable natural o biológica que está limitada en su valor inferior (cero) y que tiene una dispersión que aumenta con el valor promedio.

    * **Ejemplo:** La **concentración de contaminantes** o **minerales** en muestras ambientales. Las concentraciones no pueden ser negativas y a menudo presentan valores altos ocasionales, lo que produce el sesgo a la derecha.
    * **Aplicación:** La **duración de las conversaciones** telefónicas o las **reacciones químicas**. La duración no puede ser negativa, y la mayoría de las llamadas son cortas, mientras que muy pocas son extremadamente largas.

---
### 📐 Relación Clave

Si $X$ es una variable aleatoria Log-Normal, entonces $Y = \ln(X)$ sigue una Distribución Normal:

$$X \sim \text{Log-Normal}(\mu, \sigma^2) \implies Y = \ln(X) \sim \text{N}(\mu, \sigma^2)$$

Donde $\mu$ y $\sigma^2$ son la media y la varianza del **logaritmo de la variable**, no de la variable $X$ original. El uso del logaritmo transforma la asimetría y el límite inferior de cero en una distribución simétrica y sin límites (la Normal).

### 💻Ejemplos en codigo

```python
from scipy.stats import lognorm
import numpy as np

## NOTA: En scipy.stats.lognorm, los parámetros son:
## 's' es la desviación estándar del logaritmo (sigma).
## 'loc' es la ubicación (generalmente 0 para Log-Normal estándar).
## 'scale' es el valor exponencial de la media del logaritmo (exp(mu)).
## Sin embargo, es más común en ingeniería usar (mu_log, sigma_log).

## Usaremos la parametrización: sigma_log (s), exp(mu_log) (scale)

## ====================================================================
## 1. Finanzas (Precio de Acciones)
## ====================================================================
print("--- 1. Finanzas (Precio de Acciones) ---")

## Parámetros del rendimiento logarítmico (Normal subyacente):
mu_log = 0.05      # Media del logaritmo del precio (loc=0)
sigma_log = 0.20   # Desviación estándar del logaritmo (s)

## El precio actual (o escala) es exp(mu_log)
scale_price = np.exp(mu_log)

precio_objetivo = 150  # Queremos P(Precio > 150)
precio_inicial = 100   # Precio base (solo para referencia, el modelo se ajusta a la escala)

## Calcular P(Precio > 150)
## Usamos .sf() (Survival Function) que es 1 - CDF(x)
prob_precio_alto = lognorm.sf(precio_objetivo, s=sigma_log, scale=scale_price)

## Calcular el valor que separa el 5% más alto (Percentil 95)
percentil_alto = 0.95
precio_percentil_95 = lognorm.ppf(percentil_alto, s=sigma_log, scale=scale_price)

print(f"Parámetros del logaritmo: μ = {mu_log}, σ = {sigma_log}")
print(f"Probabilidad de que el precio de la acción sea > ${precio_objetivo}: {prob_precio_alto:.4f}")
print(f"El 5% más alto de precios comienza en: ${precio_percentil_95:.2f}")

## ====================================================================
## 2. Fiabilidad (Vida Útil de Componente por Desgaste)
## ====================================================================
print("\n--- 2. Fiabilidad (Vida Útil por Desgaste) ---")

## Parámetros de la vida útil logarítmica (en horas):
mu_log_vida = 7.0   # Corresponde a exp(7.0) ≈ 1097 horas
sigma_log_vida = 0.5

## Escala: exp(7.0)
scale_vida = np.exp(mu_log_vida)

tiempo_fallo = 1500  # Queremos P(X > 1500 horas)
tiempo_garantia = 800 # Queremos P(X < 800 horas)

## 2a. Calcular P(X > 1500)
prob_dure_mas_1500 = lognorm.sf(tiempo_fallo, s=sigma_log_vida, scale=scale_vida)

## 2b. Calcular P(X < 800)
prob_falle_antes_800 = lognorm.cdf(tiempo_garantia, s=sigma_log_vida, scale=scale_vida)

print(f"Parámetros del logaritmo: μ = {mu_log_vida}, σ = {sigma_log_vida}")
print(f"Tiempo medio (geométrico) ≈ {scale_vida:.0f} horas")
print(f"Probabilidad de que el componente dure más de {tiempo_fallo}h: {prob_dure_mas_1500:.4f}")
print(f"Probabilidad de que el componente falle antes de {tiempo_garantia}h: {prob_falle_antes_800:.4f}")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

## Configuración de los gráficos
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(2, 1, figsize=(10, 10))
fig.suptitle('Visualización de la Distribución Log-Normal (Asimétrica)', fontsize=16, y=1.02)

## ====================================================================
## 1. Finanzas (Precio de Acciones)
## ====================================================================
mu_log_fin = 0.05
sigma_log_fin = 0.20
scale_fin = np.exp(mu_log_fin)
precio_objetivo = 150

## Rango de X para el gráfico (Precios)
x_fin = np.linspace(lognorm.ppf(0.001, s=sigma_log_fin, scale=scale_fin),
                    lognorm.ppf(0.999, s=sigma_log_fin, scale=scale_fin), 500)
## Calcular la PDF
y_pdf_fin = lognorm.pdf(x_fin, s=sigma_log_fin, scale=scale_fin)

ax = axes[0]
ax.plot(x_fin, y_pdf_fin, color='blue', label=f'Log-Normal (μ={mu_log_fin}, σ={sigma_log_fin})')
ax.fill_between(x_fin, y_pdf_fin, where=(x_fin > precio_objetivo),
                color='lightblue', alpha=0.6,
                label='P(Precio > 150)')
ax.axvline(scale_fin, color='red', linestyle='--', label=f'Media geométrica: ${scale_fin:.2f}')

ax.set_title('1. Distribución de Precios de Acciones')
ax.set_xlabel('Precio del Activo ($)')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## ====================================================================
## 2. Fiabilidad (Vida Útil de Componente por Desgaste)
## ====================================================================
mu_log_vida = 7.0
sigma_log_vida = 0.5
scale_vida = np.exp(mu_log_vida)
tiempo_garantia = 800

## Rango de X para el gráfico (Horas)
x_vida = np.linspace(lognorm.ppf(0.001, s=sigma_log_vida, scale=scale_vida),
                     lognorm.ppf(0.999, s=sigma_log_vida, scale=scale_vida), 500)
## Calcular la PDF
y_pdf_vida = lognorm.pdf(x_vida, s=sigma_log_vida, scale=scale_vida)

ax = axes[1]
ax.plot(x_vida, y_pdf_vida, color='green', label=f'Log-Normal (μ={mu_log_vida}, σ={sigma_log_vida})')
ax.fill_between(x_vida, y_pdf_vida, where=(x_vida < tiempo_garantia),
                color='lightgreen', alpha=0.6,
                label='P(Fallo antes de 800h)')
ax.axvline(scale_vida, color='red', linestyle='--', label=f'Media geométrica: {scale_vida:.0f} horas')

ax.set_title('2. Distribución de Vida Útil de Componentes (Horas)')
ax.set_xlabel('Tiempo de Vida Útil (horas)')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## Ajustar diseño y mostrar
plt.tight_layout()
plt.show()
```

### ✨Distribución Gamma

* **Descripción**: Modelo de tiempo hasta el k-ésimo evento en un proceso de Poisson. Se utiliza en diversos campos, como la teoría de colas y la fiabilidad.

* **Parámetros**:
  - $ k $ (forma, número de eventos)
  - $ \theta $ (escala)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x) =
\begin{cases}
\frac{x^{k-1} e^{-\frac{x}{\theta}}}{\theta^k \Gamma(k)} & \text{si } x \geq 0 \\
0 & \text{si } x < 0
\end{cases}
$$
donde $ \Gamma(k) $ es la función gamma.

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) = \int_0^x f(t) \, dt
$$

* **Valor Esperado**: $ E[X] = k \theta $

* **Media**: $ \mu_X = k \theta $

* **Desviación Estándar**:
$$
\sigma = \sqrt{k} \theta
$$

* **Percentiles**: $ x_\alpha $ se obtiene usando la función inversa de la CDF.

**Comandos en R**:
```r
## PDF
dgamma(x, shape = k, scale = theta)

## CDF
pgamma(x, shape = k, scale = theta)

## Simulación
rgamma(n, shape = k, scale = theta)

```python
import numpy as np
from scipy.stats import gamma

## ----------------------------------------
## Definición de parámetros
k = 2.0     # Parámetro de forma (shape en R, a en Python)
theta = 1.5 # Parámetro de escala (scale en R y Python)
x = 4.0     # valor para PDF/CDF
n = 10      # número de muestras para simulación

## ----------------------------------------
## PDF (Función de Densidad de Probabilidad)
## dgamma(x, shape = k, scale = theta)
## scipy.stats.gamma.pdf(x, a=k, scale=theta)
pdf_value = gamma.pdf(x, a=k, scale=theta)
print(f"PDF (gamma.pdf) para x={x}: {pdf_value}")

## ----------------------------------------
## CDF (Función de Distribución Acumulada)
## pgamma(x, shape = k, scale = theta)
## scipy.stats.gamma.cdf(x, a=k, scale=theta)
cdf_value = gamma.cdf(x, a=k, scale=theta)
print(f"CDF (gamma.cdf) para x={x}: {cdf_value}")

## ----------------------------------------
## Simulación/Muestreo
## rgamma(n, shape = k, scale = theta)
## np.random.gamma(shape=k, scale=theta, size=n)
samples = np.random.gamma(shape=k, scale=theta, size=n)
print(f"Muestras (np.random.gamma) n={n}: {samples}")
```

#### 🧮Función Gamma $Γ()$

La **función gamma** es una extensión del factorial a los números reales y complejos. Se utiliza ampliamente en matemáticas, estadísticas y teoría de la probabilidad.

##### Definición

La función gamma se define como:

$$
\Gamma(z) = \int_0^{\infty} t^{z-1} e^{-t} \, dt
$$

donde:
- $ z $ es un número complejo con parte real positiva. Este parámetro puede ser un número entero, fraccionario o complejo. En el contexto de la función gamma,$ z $ se puede interpretar como un "número de elementos" que se están evaluando.

##### Propiedades

1. **Relación con el factorial**:
   Para números enteros positivos $ n $, la función gamma se relaciona con el factorial de la siguiente manera:

   $$
   \Gamma(n) = (n-1)!
   $$

   Por ejemplo:
   - $\Gamma(1) = 0! = 1 $
   - $\Gamma(2) = 1! = 1 $
   - $\Gamma(3) = 2! = 2 $

2. **Relación de recurrencia**:
   La función gamma satisface la relación:

   $$
   \Gamma(z + 1) = z \Gamma(z)
   $$

   Esta propiedad permite calcular valores de la función gamma a partir de otros valores.

3. **Valores específicos**:
   - $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi} $

**Usos en Estadística**

- La función gamma es fundamental en la definición de varias distribuciones, como la distribución gamma, la distribución Chi-cuadrada y la distribución F.
- Se utiliza en el cálculo de funciones de densidad y en la estadística bayesiana.

**Ejemplo de Cálculo**

Para calcular $ \Gamma(5) $:

$$
\Gamma(5) = \int_0^{\infty} t^{5-1} e^{-t} \, dt = \int_0^{\infty} t^4 e^{-t} \, dt = 4! = 24
$$

**Cálculo de la Función Gamma en R**

La función gamma se puede calcular en R utilizando la función `gamma()`. Aquí te muestro cómo hacerlo:

```r
## Cálculo de la función gamma
gamma_value <- gamma(z)

```python
import numpy as np
from scipy.special import gamma

## Definición del valor 'z' (el argumento de la función Gamma)
z = 5

## ----------------------------------------
## Cálculo de la función Gamma
## gamma_value <- gamma(z)
## scipy.special.gamma(z)
gamma_value = gamma(z)
print(f"El valor de gamma({z}) es: {gamma_value}")

## Ejemplo con un número no entero
z_float = 3.5
gamma_value_float = gamma(z_float)
print(f"El valor de gamma({z_float}) es: {gamma_value_float}")
```

```python
## Cálculo de Gamma(5)
z <- 5
gamma_value <- gamma(z)
print(gamma_value)
```

```python
from scipy.special import gamma
import numpy as np

## ----------------------------------------
## Definición del valor 'z'
z = 5

## ----------------------------------------
## Cálculo de la función Gamma(z) (equivalente a gamma(z) en R)
gamma_value = gamma(z)

print(f"El valor de z es: {z}")
print(f"El valor de Gamma({z}) es: {gamma_value}")

## Verificación: Para enteros positivos, Gamma(z) = (z-1)!
## Gamma(5) = 4! = 24
```

Gráfica de la función Gamma $Γ$

```python
"""

## Cargar la librería necesaria
library(ggplot2)

## Crear un rango de valores para z
z_values <- seq(0.1, 5, by = 0.1)

## Calcular los valores de la función gamma
gamma_values <- gamma(z_values)

## Crear un data frame para ggplot
data <- data.frame(z = z_values, gamma = gamma_values)

## Graficar la función gamma
ggplot(data, aes(x = z, y = gamma)) +
  geom_line(color = "blue") +
  labs(title = "Gráfico de la Función Gamma",
       x = "z",
       y = expression(gamma(z))) +
  theme_minimal()

"""
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.special import gamma # Importar la función gamma

## ----------------------------------------
## 1. Crear un rango de valores para z (equivalente a seq() en R)
z_values = np.linspace(0.1, 5, 50)
## np.linspace(inicio, fin, número_de_puntos). 50 puntos para una línea suave.

## ----------------------------------------
## 2. Calcular los valores de la función gamma
## gamma_values <- gamma(z_values)
gamma_values = gamma(z_values)

## ----------------------------------------
## 3. Crear un DataFrame (equivalente a data.frame() en R)
data = pd.DataFrame({'z': z_values, 'gamma': gamma_values})

## ----------------------------------------
## 4. Graficar la función gamma (equivalente a ggplot2)

## Configurar el estilo (similar a theme_minimal())
sns.set_style("whitegrid")

plt.figure(figsize=(10, 6))

## Graficar la línea (equivalente a geom_line())
sns.lineplot(x='z', y='gamma', data=data, color="blue", linewidth=2)

## Añadir títulos y etiquetas (equivalente a labs())
plt.title("Gráfico de la Función Gamma", fontsize=16)
plt.xlabel("z", fontsize=14)
## Usamos LaTeX para la etiqueta del eje Y (equivalente a expression(gamma(z)))
plt.ylabel(r"$\Gamma(z)$", fontsize=18)

## Mostrar la gráfica
plt.show()
```

#### 🔍Ejemplo de Gráfica de la Distribución Gamma

La distribución gamma es una distribución continua que describe el tiempo hasta que ocurren un número específico de eventos en un proceso de Poisson. Es útil en situaciones donde se modelan fenómenos como el tiempo de espera hasta un evento, donde la variable aleatoria puede ser positiva y no tiene un límite superior.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad $PDF $ de la distribución gamma para varios valores de los parámetros $ k $ (forma) y $\theta$ (escala). A medida que se ajustan los valores de $ k $ y $ \theta $, la forma de la distribución cambia, mostrando cómo la variabilidad en los parámetros influye en la probabilidad de que ocurran diferentes resultados.

La distribución gamma es especialmente relevante en áreas como la ingeniería, la economía y la investigación científica, donde se modelan tiempos de espera y otras variables continuas.

```python
"""

## Cargar la librería necesaria
library(ggplot2)

## Definir los parámetros de la distribución gamma
shape1 <- 2  # Parámetro de forma (k)
scale1 <- 1  # Parámetro de escala (theta)

shape2 <- 5  # Otro parámetro de forma
scale2 <- 1  # Mismo parámetro de escala

## Crear un rango de valores para x
x_values <- seq(0, 20, by = 0.1)

## Calcular la función de densidad de la distribución gamma
gamma_density1 <- dgamma(x_values, shape = shape1, scale = scale1)
gamma_density2 <- dgamma(x_values, shape = shape2, scale = scale2)

## Crear un data frame para ggplot
data <- data.frame(x = x_values,
                   density1 = gamma_density1,
                   density2 = gamma_density2)

## Graficar la distribución gamma
ggplot(data, aes(x = x)) +
  geom_line(aes(y = density1), color = "blue", linewidth = 1) +
  geom_line(aes(y = density2), color = "red", linewidth = 1) +
  labs(title = "Gráfico de la Distribución Gamma",
       x = "x",
       y = "Densidad") +
  theme_minimal() +
  scale_y_continuous(expand = expansion(mult = c(0, 0.1))) +
  theme(legend.position = "top") +
  geom_area(aes(y = density1), fill = "blue", alpha = 0.1) +
  geom_area(aes(y = density2), fill = "red", alpha = 0.1) +
  scale_color_manual(name = "Distribución",
                     values = c("Gamma(2, 1)" = "blue", "Gamma(5, 1)" = "red")) +
  geom_line(aes(y = density1, color = "Gamma(2, 1)")) +
  geom_line(aes(y = density2, color = "Gamma(5, 1)"))

"""
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import gamma

## ----------------------------------------
## 1. Definir los parámetros de la distribución gamma
params = [
    {'k': 2, 'theta': 1, 'label': 'Gamma(k=2, \u03B8=1)', 'color': 'blue'},
    {'k': 5, 'theta': 1, 'label': 'Gamma(k=5, \u03B8=1)', 'color': 'red'}
]

## ----------------------------------------
## 2. Crear un rango de valores para x (equivalente a seq() en R)
x_values = np.linspace(0, 20, 201)

## ----------------------------------------
## 3. Calcular la PDF y consolidar en un solo DataFrame (similar a Tidy Data)
data_list = []

for p in params:
    k = p['k']      # Parámetro de forma (shape -> 'a' en scipy)
    theta = p['theta']  # Parámetro de escala (scale -> 'scale' en scipy)
    label = p['label']

## Calcular la función de densidad (equivalente a dgamma() en R)
    gamma_density = gamma.pdf(x_values, a=k, scale=theta)

## Crear DataFrame temporal
    df_temp = pd.DataFrame({
        'x': x_values,
        'Densidad': gamma_density,
        'Distribucion': label,
        'Color': p['color']
    })
    data_list.append(df_temp)

## Combinar todos los DataFrames
data = pd.concat(data_list, ignore_index=True)

## ----------------------------------------
## 4. Graficar la distribución gamma (equivalente a ggplot2)

## Configurar el estilo (theme_minimal)
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

## Mapear los colores manualmente
color_map = {p['label']: p['color'] for p in params}

## Graficar áreas (geom_area)
for label, color in color_map.items():
    subset = data[data['Distribucion'] == label]
    plt.fill_between(subset['x'], subset['Densidad'],
                     color=color, alpha=0.1)

## Graficar líneas (geom_line)
sns.lineplot(
    data=data,
    x='x',
    y='Densidad',
    hue='Distribucion', # Mapeo para la leyenda
    palette=color_map, # Mapeo de colores
    linewidth=2
)

## Añadir títulos y etiquetas (labs)
plt.title("Gráfico de la Distribución Gamma", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("Densidad", fontsize=14)

## Ajustar leyenda (similar a scale_color_manual y theme(legend.position = "top"))
plt.legend(title="Distribución", loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=2)

## Mostrar la gráfica
plt.show()
```

#### 📜**Descripción del Código**

* **Cargar librerías**: Se utiliza `ggplot2` para crear la gráfica.
* **Definir los parámetros**: Se establecen los parámetros de forma $ k $ y escala $\theta $ para la distribución gamma.
* **Crear un rango de valores para $x $**: Se define un rango de valores de $ 0 $ a $ 20 $ para representar la distribución.
* **Calcular la PDF**: Se utiliza `dgamma()` para calcular la función de densidad de probabilidad para los valores de $x$ con los parámetros definidos.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $x$ y sus correspondientes probabilidades para las dos configuraciones de la distribución gamma.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $ PDF $ de la distribución gamma para los diferentes parámetros, incluyendo áreas sombreadas para visualizar mejor las densidades.

**EJERCICIO 12**

Agrega ejemplos y los usos recomendados.

### ⏳ Usos Recomendados de la Distribución Gamma

La **Distribución Gamma** $\text{Gamma}(\alpha, \beta)$ es una distribución continua y asimétrica que se utiliza para modelar **tiempos de espera**, duraciones y cantidades no negativas, especialmente cuando son la suma de varios procesos exponenciales independientes. Es notablemente flexible gracias a sus dos parámetros: **forma** ($\alpha$, a menudo denotado como $k$) y **escala** ($\beta$ o $1/\lambda$).

1.  **Teoría de Colas y Tiempos de Espera (Distribución de Erlang)**
    Cuando el parámetro de forma ($\alpha$ o $k$) es un **entero positivo**, la Distribución Gamma se convierte en la **Distribución de Erlang**. Esta es ideal para modelar la suma de $k$ tiempos de espera exponenciales.

    * **Ejemplo:** En un proceso de servicio (como una fila de banco), si el tiempo que toma atender a cada cliente sigue una distribución Exponencial con tasa $\lambda$, la Distribución Gamma (Erlang) calcula el tiempo total que tomará atender a **exactamente 3 clientes** ($k=3$). Es el tiempo de espera hasta que ocurre el **$k$-ésimo evento**.
    * **Aplicación:** Modelar el tiempo total de procesamiento de una tarea que requiere pasar por **$k$ etapas secuenciales** o el tiempo de espera hasta que el **tercer avión** aterriza en un aeropuerto.

2.  **Fiabilidad, Seguros y Análisis de Vida Útil**
    Se utiliza para modelar la vida útil de componentes o sistemas, ofreciendo más flexibilidad que la Distribución Exponencial o Log-Normal para ajustarse a datos empíricos de fallos. También es común en ciencia actuarial para modelar reclamaciones financieras.

    * **Ejemplo:** El **tiempo de vida** de un motor o una máquina compleja. A diferencia de la Exponencial, la Gamma puede modelar una tasa de fallo que **aumenta o disminuye** con el tiempo, dependiendo de los parámetros de forma. Permite calcular la probabilidad de que el componente funcione por **más de 10,000 horas**.
    * **Aplicación:** Modelar la **magnitud de las pérdidas aseguradas** o el **tamaño de las reclamaciones de seguros**. Las reclamaciones no pueden ser negativas y a menudo tienen una distribución sesgada a la derecha.

3.  **Hidrología y Climatología**
    Su asimetría y el hecho de estar restringida a valores positivos la hacen adecuada para variables ambientales.

    * **Ejemplo:** La **cantidad de lluvia** acumulada en una cuenca en un periodo de tiempo determinado. No puede ser negativa y generalmente tiene un sesgo a la derecha, con muchos días de poca lluvia y pocos días de lluvia extrema.
    * **Aplicación:** El **consumo diario de energía** en una ciudad o la **demanda de recursos** (agua, electricidad).

---
### ⚙️ Casos Particulares

La Distribución Gamma es una familia de distribuciones que incluye otras importantes como casos especiales:

* **Distribución Exponencial:** Es el caso particular de la Gamma cuando el parámetro de forma es $\alpha=1$. Esto confirma que el tiempo hasta el primer evento (Exponencial) es un subconjunto del tiempo hasta el $k$-ésimo evento (Gamma).
    $$\text{Gamma}(1, \beta) \equiv \text{Exponencial}(\lambda=1/\beta)$$
* **Distribución Chi-Cuadrado ($\chi^2$):** Es un caso particular de la Gamma utilizado en inferencia estadística cuando $\alpha=v/2$ (donde $v$ son los grados de libertad) y $\beta=2$.
    $$\chi^2(v) \equiv \text{Gamma}(v/2, 2)$$

### 💻Ejemplos en codigo

```python
from scipy.stats import gamma

## ====================================================================
## 1. Teoría de Colas (Tiempo de Espera para el 3er Cliente - Erlang)
## ====================================================================
print("--- 1. Teoría de Colas (Tiempo de Espera - Erlang) ---")

## Tasa de servicio (lambda): 0.25 clientes/min (1 cliente cada 4 minutos)
tasa_lambda = 0.25
## Parámetro de escala (beta): 1 / lambda = 4 minutos
escala_beta = 1 / tasa_lambda

## Parámetro de forma (k): Tiempo hasta el 3er evento (3 clientes)
forma_k = 3

tiempo_interes = 20  # Queremos P(X > 20 minutos)

## 1a. Calcular P(X > 20 minutos)
## Usamos .sf() (Survival Function) que es 1 - CDF(x)
prob_mas_de_20_min = gamma.sf(tiempo_interes, a=forma_k, scale=escala_beta)

## 1b. Calcular el tiempo medio esperado para atender a 3 clientes (E[X] = k * beta)
tiempo_medio_esperado = forma_k * escala_beta

print(f"Parámetros: Forma (k) = {forma_k}, Escala (β) = {escala_beta} min")
print(f"Tiempo medio esperado para 3 clientes: {tiempo_medio_esperado:.2f} minutos")
print(f"Probabilidad de que tarde más de {tiempo_interes} min (P(X > 20)): {prob_mas_de_20_min:.4f}")

## ====================================================================
## 2. Fiabilidad (Vida Útil de un Motor)
## ====================================================================
print("\n--- 2. Fiabilidad (Vida Útil de un Motor) ---")

## Parámetros ajustados (ejemplo típico para modelar desgaste):
forma_alfa = 5.0  # k > 1 implica tasa de fallo creciente (desgaste)
escala_beta_horas = 2500  # Escala en horas

tiempo_interes_horas = 10000  # Queremos P(X > 10,000 horas)

## 2a. Calcular P(X > 10,000 horas)
prob_dure_mas_10k_h = gamma.sf(tiempo_interes_horas, a=forma_alfa, scale=escala_beta_horas)

## 2b. Calcular el tiempo medio de vida útil (E[X] = alfa * beta)
tiempo_medio_vida = forma_alfa * escala_beta_horas

print(f"Parámetros: Forma (α) = {forma_alfa}, Escala (β) = {escala_beta_horas} horas")
print(f"Tiempo medio de vida útil: {tiempo_medio_vida:.0f} horas")
print(f"Probabilidad de que dure más de {tiempo_interes_horas}h (P(X > 10000)): {prob_dure_mas_10k_h:.4f}")

## ====================================================================
## 3. Hidrología (Cantidad de Lluvia Acumulada)
## ====================================================================
print("\n--- 3. Hidrología (Cantidad de Lluvia) ---")

## Parámetros para lluvia (ejemplo sesgado a la derecha):
forma_lluvia = 1.8
escala_lluvia = 100  # Escala en mm

lluvia_extrema = 350  # Queremos P(X > 350 mm)

## 3a. Calcular P(X > 350 mm)
prob_lluvia_extrema = gamma.sf(lluvia_extrema, a=forma_lluvia, scale=escala_lluvia)

print(f"Parámetros: Forma (α) = {forma_lluvia}, Escala (β) = {escala_lluvia} mm")
print(f"Probabilidad de acumular más de {lluvia_extrema} mm de lluvia (P(X > 350)): {prob_lluvia_extrema:.4f}")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

## Configuración de los gráficos
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(3, 1, figsize=(10, 15))
fig.suptitle('Visualización de la Distribución Gamma (Tiempos y Cantidades)', fontsize=16, y=1.02)

## ====================================================================
## 1. Teoría de Colas (Tiempo de Espera para el 3er Cliente - Erlang)
## ====================================================================
forma_k = 3
escala_beta = 4
tiempo_interes = 20

## Rango de X (tiempo en minutos)
x_col = np.linspace(0, 50, 500)
## Calcular la PDF
y_pdf_col = gamma.pdf(x_col, a=forma_k, scale=escala_beta)

ax = axes[0]
ax.plot(x_col, y_pdf_col, color='blue', label=f'Gamma(k={forma_k}, β={escala_beta})')
ax.fill_between(x_col, y_pdf_col, where=(x_col > tiempo_interes),
                color='lightblue', alpha=0.6,
                label='P(Tiempo > 20 min)')
ax.axvline(tiempo_interes, color='red', linestyle='--', label=f'Límite: {tiempo_interes} min')

ax.set_title('1. Tiempo de Espera para 3 Clientes (Teoría de Colas)')
ax.set_xlabel('Tiempo (minutos)')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## ====================================================================
## 2. Fiabilidad (Vida Útil de un Motor)
## ====================================================================
forma_alfa = 5.0
escala_beta_horas = 2500
tiempo_interes_horas = 10000

## Rango de X (tiempo en horas)
x_vida = np.linspace(0, 30000, 500)
## Calcular la PDF
y_pdf_vida = gamma.pdf(x_vida, a=forma_alfa, scale=escala_beta_horas)

ax = axes[1]
ax.plot(x_vida, y_pdf_vida, color='green', label=f'Gamma(α={forma_alfa}, β={escala_beta_horas})')
ax.fill_between(x_vida, y_pdf_vida, where=(x_vida > tiempo_interes_horas),
                color='lightgreen', alpha=0.6,
                label='P(Vida Útil > 10,000 h)')
ax.axvline(tiempo_interes_horas, color='red', linestyle='--', label=f'Límite: {tiempo_interes_horas} h')
ax.axvline(forma_alfa * escala_beta_horas, color='gray', linestyle=':', label=f'Media: {forma_alfa * escala_beta_horas:.0f} h')

ax.set_title('2. Tiempo de Vida Útil de un Motor (Fiabilidad)')
ax.set_xlabel('Tiempo de Vida Útil (horas)')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## ====================================================================
## 3. Hidrología (Cantidad de Lluvia Acumulada)
## ====================================================================
forma_lluvia = 1.8
escala_lluvia = 100
lluvia_extrema = 350

## Rango de X (cantidad de lluvia en mm)
x_lluvia = np.linspace(0, 700, 500)
## Calcular la PDF
y_pdf_lluvia = gamma.pdf(x_lluvia, a=forma_lluvia, scale=escala_lluvia)

ax = axes[2]
ax.plot(x_lluvia, y_pdf_lluvia, color='purple', label=f'Gamma(α={forma_lluvia}, β={escala_lluvia})')
ax.fill_between(x_lluvia, y_pdf_lluvia, where=(x_lluvia > lluvia_extrema),
                color='violet', alpha=0.6,
                label='P(Lluvia > 350 mm)')
ax.axvline(lluvia_extrema, color='red', linestyle='--', label=f'Límite: {lluvia_extrema} mm')

ax.set_title('3. Cantidad de Lluvia Acumulada (Hidrología)')
ax.set_xlabel('Cantidad de Lluvia (mm)')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## Ajustar diseño y mostrar
plt.tight_layout()
plt.show()
```

### ✨Distribución Beta

* **Descripción**: Modelo de variables aleatorias que se distribuyen en el intervalo $[0, 1]$. Es útil para modelar fenómenos aleatorios que están restringidos a ese intervalo.

* **Parámetros**:
  - $ \alpha $ (parámetro de forma)
  - $ \beta $ (parámetro de forma)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x) =
\begin{cases}
\frac{x^{\alpha - 1} (1 - x)^{\beta - 1}}{B(\alpha, \beta)} & \text{si } 0 < x < 1 \\
0 & \text{si } x \leq 0 \text{ o } x \geq 1
\end{cases}
$$
donde $ B(\alpha, \beta) $es **la función beta**.

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) = \int_0^x f(t) \, dt
$$

* **Valor Esperado**: $E[X] = \frac{\alpha}{\alpha + \beta} $

* **Media**: $ \mu_X = \frac{\alpha}{\alpha + \beta} $

* **Desviación Estándar**:
$$
\sigma = \sqrt{\frac{\alpha \beta}{(\alpha + \beta)^2 (\alpha + \beta + 1)}}
$$

* **Percentiles**: $ x_\alpha $ se obtiene usando la función inversa de la CDF.

**Comandos en R**:
```r
## PDF
dbeta(x, shape1 = alpha, shape2 = beta)

## CDF
pbeta(x, shape1 = alpha, shape2 = beta)

## Simulación
rbeta(n, shape1 = alpha, shape2 = beta)

```python
import numpy as np
from scipy.stats import beta

## ----------------------------------------
## Definición de parámetros
alpha = 2.0  # Parámetro de forma 1 (shape1 en R, a en Python)
beta_param = 5.0 # Parámetro de forma 2 (shape2 en R, b en Python)
x = 0.4      # valor para PDF/CDF (debe estar entre 0 y 1)
n = 10       # número de muestras para simulación

## ----------------------------------------
## PDF (Función de Densidad de Probabilidad)
## dbeta(x, shape1 = alpha, shape2 = beta_param)
## scipy.stats.beta.pdf(x, a=alpha, b=beta_param)
pdf_value = beta.pdf(x, a=alpha, b=beta_param)
print(f"PDF (beta.pdf) para x={x}: {pdf_value}")

## ----------------------------------------
## CDF (Función de Distribución Acumulada)
## pbeta(x, shape1 = alpha, shape2 = beta_param)
## scipy.stats.beta.cdf(x, a=alpha, b=beta_param)
cdf_value = beta.cdf(x, a=alpha, b=beta_param)
print(f"CDF (beta.cdf) para x={x}: {cdf_value}")

## ----------------------------------------
## Simulación/Muestreo
## rbeta(n, shape1 = alpha, shape2 = beta_param)
## np.random.beta(a=alpha, b=beta_param, size=n)
samples = np.random.beta(a=alpha, b=beta_param, size=n)
print(f"Muestras (np.random.beta) n={n}: {samples}")
```

#### 🧮Función Beta

La **función beta** es una función especial que se utiliza en diversas áreas de las matemáticas, especialmente en teoría de la probabilidad y estadística. Es fundamental en el cálculo de distribuciones de probabilidad, como la distribución beta y la distribución F.

##### Definición

La función beta se define como:

$$
B(x, y) = \int_0^1 t^{x-1} (1-t)^{y-1} \, dt
$$

donde:
- $ x > 0 $ y $ y > 0$ son parámetros que determinan la forma de la función beta. Representan "números de éxito" y "números de fracaso" en el contexto de probabilidades. En muchos casos, $x$ se interpreta como el número de éxitos en un experimento y $y$ como el número de fracasos.

#### Propiedades

1. **Relación con la función gamma**:
   La función beta está relacionada con la función gamma mediante la siguiente relación:

   $$
   B(x, y) = \frac{\Gamma(x) \Gamma(y)}{\Gamma(x+y)}
   $$

   donde \( \Gamma(n) \) es la función gamma, que generaliza el factorial para números no enteros.

2. **Simetría**:
   La función beta tiene la propiedad de ser simétrica, lo que significa que:

   $$
   B(x, y) = B(y, x)
   $$

3. **Valores específicos**:
   - $ B(1, 1) = 1 $
   - $ B\left(\frac{1}{2}, \frac{1}{2}\right) = \pi $

**Usos en Estadística**

- **Distribución Beta**: La función beta se utiliza para definir la función de densidad de probabilidad de la distribución beta:

  $$
  f(x) = \frac{1}{B(\alpha, \beta)} x^{\alpha - 1} (1 - x)^{\beta - 1} \quad \text{para } 0 < x < 1
  $$

- **Distribución F**: La función beta también se emplea en la definición de la distribución F.

**Ejemplo de Cálculo**

Para calcular $B(2, 3) $:

$$
B(2, 3) = \int_0^1 t^{2-1} (1-t)^{3-1} \, dt = \int_0^1 t^{1} (1-t)^{2} \, dt
$$

Resolviendo la integral:

$$
= \left[ \frac{t^2}{2} \cdot \frac{(1-t)^3}{3} \right]_0^1 = \frac{1}{2 \cdot 3} = \frac{1}{6}
$$

**Cálculo de la Función Beta en R**

La función beta se puede calcular en R utilizando la función `beta()`. Aquí te muestro cómo hacerlo:

```r
## Cálculo de la función beta
beta_value <- beta(x, y)

```python
from scipy.special import beta
import numpy as np

## ----------------------------------------
## Definición de los argumentos 'x' y 'y'
x = 2.0
y = 3.0

## ----------------------------------------
## Cálculo de la función Beta (equivalente a beta(x, y) en R)
## B(x, y) = Gamma(x) * Gamma(y) / Gamma(x + y)
beta_value = beta(x, y)
print(f"El valor de Beta({x}, {y}) es: {beta_value}")

## Verificación manual: B(2, 3) = Gamma(2) * Gamma(3) / Gamma(5)
## B(2, 3) = 1! * 2! / 4! = 1 * 2 / 24 = 2/24 = 0.08333...
```

```python
"""

#Ejemplo en R
#Supongamos que deseas calcular 𝐵(2,3)

x <- 2
y <- 3

## Usando la función beta
beta_value <- beta(x, y)
print(beta_value)

## Usando la relación con la función gamma
beta_value_gamma <- gamma(x) * gamma(y) / gamma(x + y)
print(beta_value_gamma)

"""
```

```python
from scipy.special import beta, gamma
import numpy as np

## ----------------------------------------
## Definición de los argumentos 'x' y 'y'
x = 2
y = 3

## ----------------------------------------
## 1. Usando la función beta (equivalente a beta(x, y) en R)
beta_value = beta(x, y)
print(f"El valor de Beta({x}, {y}) usando scipy.special.beta es: {beta_value}")

## ----------------------------------------
## 2. Usando la relación con la función gamma
## beta_value_gamma <- gamma(x) * gamma(y) / gamma(x + y)
beta_value_gamma = gamma(x) * gamma(y) / gamma(x + y)
print(f"El valor de Beta({x}, {y}) usando la relación con Gamma es: {beta_value_gamma}")
```

#### 🔍Ejemplo de Gráfica de la Distribución Beta

La distribución beta es un modelo de probabilidad que describe variables aleatorias que se encuentran en el intervalo $[0, 1]$. Esta distribución es especialmente útil para modelar proporciones y probabilidades, ya que puede adoptar diferentes formas dependiendo de sus parámetros. Los parámetros de la distribución beta, $ \alpha $ y $ \beta $, determinan la forma de la función de densidad, permitiendo que la distribución sea simétrica, sesgada hacia la izquierda o hacia la derecha.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad $ PDF $ de la distribución beta para varios valores de $ \alpha $ y $ \beta $. A medida que se ajustan estos parámetros, la forma de la distribución varía, lo que refleja cómo las diferentes combinaciones de $ \alpha $ y $ \beta $ influyen en la concentración de probabilidad.

La distribución beta es particularmente valiosa en campos como la estadística bayesiana y la teoría de decisiones, donde se requiere modelar incertidumbres en intervalos restringidos.

```python
"""

## Cargar la librería necesaria
library(ggplot2)

## Crear un rango de valores para x
x_values <- seq(0, 1, by = 0.01)

## Definir los parámetros de la función beta
shape1 <- 2  # Parámetro x
shape2 <- 5  # Parámetro y

## Calcular la función beta
beta_density <- dbeta(x_values, shape1, shape2)

## Crear un data frame para ggplot
data <- data.frame(x = x_values, density = beta_density)

## Graficar la función beta
ggplot(data, aes(x = x, y = density)) +
  geom_line(color = "blue", linewidth = 1) +
  labs(title = "Gráfico de la Función Beta",
       x = "x",
       y = "Densidad") +
  theme_minimal() +
  scale_y_continuous(expand = expansion(mult = c(0, 0.1)))

"""
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import beta

## ----------------------------------------
## 1. Crear un rango de valores para x (equivalente a seq() en R)
## La distribución Beta está definida en el intervalo [0, 1]
x_values = np.linspace(0.001, 0.999, 100)
## Usamos un rango ligeramente ajustado para evitar posibles divisiones por cero en los límites

## ----------------------------------------
## 2. Definir los parámetros de la función beta
shape1 = 2  # Parámetro a (alpha)
shape2 = 5  # Parámetro b (beta)

## ----------------------------------------
## 3. Calcular la función de densidad de la distribución beta (equivalente a dbeta() en R)
## scipy.stats.beta.pdf(x, a=shape1, b=shape2)
beta_density = beta.pdf(x_values, a=shape1, b=shape2)

## ----------------------------------------
## 4. Crear un DataFrame (equivalente a data.frame() en R)
data = pd.DataFrame({'x': x_values, 'density': beta_density})

## ----------------------------------------
## 5. Graficar la función beta (equivalente a ggplot2)

## Configurar el estilo (similar a theme_minimal())
sns.set_style("whitegrid")

plt.figure(figsize=(10, 6))

## Graficar la línea (equivalente a geom_line())
sns.lineplot(x='x', y='density', data=data, color="blue", linewidth=2)

## Añadir títulos y etiquetas (equivalente a labs())
plt.title(f"Gráfico de la Distribución Beta (a={shape1}, b={shape2})", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("Densidad", fontsize=14)

## Ajustar el eje Y para que comience en 0 (similar a scale_y_continuous con expand)
plt.ylim(0, max(beta_density) * 1.1)

## Mostrar la gráfica
plt.show()
```

**Gráfico de la distribució beta**

```python
"""

## Cargar la librería necesaria
library(ggplot2)

## Crear un rango de valores para x
x_values <- seq(0, 1, by = 0.01)

## Definir los parámetros de la distribución beta
alpha1 <- 2  # Parámetro alpha
beta1 <- 5   # Parámetro beta

alpha2 <- 5  # Otro parámetro alpha
beta2 <- 2   # Otro parámetro beta

## Calcular la función de densidad de la distribución beta
beta_density1 <- dbeta(x_values, shape1 = alpha1, shape2 = beta1)
beta_density2 <- dbeta(x_values, shape1 = alpha2, shape2 = beta2)

## Crear un data frame para ggplot
data <- data.frame(x = x_values,
                   density1 = beta_density1,
                   density2 = beta_density2)

## Graficar la distribución beta
ggplot(data, aes(x = x)) +
  geom_line(aes(y = density1), color = "blue", linewidth = 1) +
  geom_line(aes(y = density2), color = "red", linewidth = 1) +
  labs(title = "Gráfico de la Distribución Beta",
       x = "x",
       y = "Densidad") +
  theme_minimal() +
  scale_y_continuous(expand = expansion(mult = c(0, 0.1))) +
  theme(legend.position = "top") +
  geom_area(aes(y = density1), fill = "blue", alpha = 0.1) +
  geom_area(aes(y = density2), fill = "red", alpha = 0.1)

"""
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import beta

## ----------------------------------------
## 1. Crear un rango de valores para x (equivalente a seq() en R)
## La distribución Beta está definida en [0, 1]
x_values = np.linspace(0.001, 0.999, 200) # 200 puntos

## ----------------------------------------
## 2. Definir los parámetros de las dos distribuciones Beta
params = [
    {'a': 2, 'b': 5, 'label': 'Beta(\u03B1=2, \u03B2=5)', 'color': 'blue'},
    {'a': 5, 'b': 2, 'label': 'Beta(\u03B1=5, \u03B2=2)', 'color': 'red'}
]
## Nota: alpha en R es 'a' en Python, beta en R es 'b' en Python

## ----------------------------------------
## 3. Calcular la PDF y consolidar en un solo DataFrame
data_list = []

for p in params:
## Calcular la función de densidad (equivalente a dbeta() en R)
## En scipy, dbeta(x, shape1, shape2) -> beta.pdf(x, a=shape1, b=shape2)
    beta_density = beta.pdf(x_values, a=p['a'], b=p['b'])

## Crear DataFrame temporal
    df_temp = pd.DataFrame({
        'x': x_values,
        'Densidad': beta_density,
        'Distribucion': p['label'],
        'Color': p['color']
    })
    data_list.append(df_temp)

## Combinar todos los DataFrames
data = pd.concat(data_list, ignore_index=True)

## ----------------------------------------
## 4. Graficar la distribución Beta (equivalente a ggplot2)

## Configurar el estilo (theme_minimal)
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

## Mapear los colores manualmente para geom_area y geom_line
color_map = {p['label']: p['color'] for p in params}

## Graficar áreas (geom_area)
for label, color in color_map.items():
    subset = data[data['Distribucion'] == label]
    plt.fill_between(subset['x'], subset['Densidad'],
                     color=color, alpha=0.1, label=f'Área {label}')

## Graficar líneas (geom_line)
sns.lineplot(
    data=data,
    x='x',
    y='Densidad',
    hue='Distribucion', # Mapeo para la leyenda
    palette=color_map, # Mapeo de colores
    linewidth=2
)

## Añadir títulos y etiquetas (labs)
plt.title("Gráfico de la Distribución Beta para Diferentes Parámetros", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("Densidad", fontsize=14)

## Ajustar el eje Y para
```

#### 📜**Descripción del Código**

* **Cargar librerías**: Se utiliza `ggplot2 `para crear la gráfica.
* **Crear un rango de valores para $x$**: Se define un rango de valores de $ 0 $ a $ 1 $ para representar la distribución beta.
* **Definir los parámetros**: Se establecen los parámetros $ \alpha $ y $ \beta $ para las dos configuraciones de la distribución beta.
* **Calcular la PDF**: Se utiliza `dbeta()` para calcular la función de densidad de probabilidad para los valores de $ x $ con los parámetros definidos.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $ x$ y sus correspondientes probabilidades para las dos configuraciones de la distribución beta.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $ PDF $ de la distribución beta para los diferentes parámetros, incluyendo áreas sombreadas para visualizar mejor las densidades.

**EJERCICIO 13**

Agrega ejemplos y los usos recomendados.

### 📐 Usos Recomendados de la Distribución Beta

La **Distribución Beta** $\text{Beta}(\alpha, \beta)$ es una distribución continua y flexible definida exclusivamente para valores en el intervalo $[0, 1]$. Sus dos parámetros de forma, $\alpha$ y $\beta$, controlan la forma de la distribución, permitiéndole modelar una amplia variedad de formas: uniforme, sesgada, en forma de U y en forma de campana (Normal). Su uso principal es modelar la **probabilidad de una probabilidad** o la **proporción** de un evento.

1.  **Modelado de Proporciones y Porcentajes**
    Es ideal para variables que representan una fracción, un porcentaje o una proporción, ya que su dominio se ajusta perfectamente al rango $[0, 1]$.

    * **Ejemplo:** La **proporción de tiempo** que una máquina está operativa. Si se sabe que la máquina pasa la mayor parte del tiempo funcionando (cercano a 1), pero ocasionalmente tiene fallas largas (cercano a 0), la Distribución Beta puede modelar esta proporción de operatividad basándose en datos históricos.
    * **Aplicación:** El **porcentaje de votos** que recibirá un candidato en una elección, la **proporción de productos defectuosos** en un lote o la **fracción de días** soleados en un año.

2.  **Inferencia Bayesiana (Distribución Conjugada)**
    Este es el uso más importante y extendido de la Distribución Beta. Actúa como la **distribución a priori conjugada** para el parámetro de probabilidad ($p$) de la Distribución Binomial.

    * **Ejemplo:** Queremos estimar la **probabilidad real ($p$)** de que una moneda caiga cara.
        * **A Priori:** Antes de lanzar la moneda, asumimos que $p$ podría ser cualquier valor, y lo modelamos con una Beta no informativa, como $\text{Beta}(1, 1)$ (que es una Uniforme).
        * **Datos:** Lanzamos la moneda 10 veces y obtenemos 7 caras (7 éxitos, 3 fracasos).
        * **A Posteriori:** La probabilidad actualizada de $p$ se convierte en una nueva Distribución Beta: $\text{Beta}(1+7, 1+3) = \text{Beta}(8, 4)$. Esta distribución posterior encapsula toda la incertidumbre sobre la probabilidad real de la moneda.

3.  **Gestión de Proyectos (Análisis PERT)**
    Se utiliza en la técnica de Evaluación y Revisión de Programas (PERT) para modelar la incertidumbre en la duración de las tareas.

    * **Ejemplo:** Estimar el **tiempo de finalización** de una fase de proyecto, donde la duración está acotada por un tiempo **mínimo** ($a$), un tiempo **máximo** ($b$) y un tiempo **más probable** ($m$). El modelo PERT a menudo utiliza una forma de la Distribución Beta para calcular la duración esperada y su variabilidad dentro de estos límites.

---
### ✏️ Flexibilidad de la Forma

La Distribución Beta puede tomar diversas formas controlando los parámetros $\alpha$ y $\beta$:

| Parámetros ($\alpha, \beta$) | Forma de la Distribución | Uso Común |
| :--------------------------- | :----------------------- | :-------- |
| $\alpha = 1, \beta = 1$      | Uniforme                 | A priori no informativa |
| $\alpha < 1, \beta > 1$      | Sesgada a la derecha     | Modelar eventos raros |
| $\alpha > 1, \beta < 1$      | Sesgada a la izquierda   | Modelar eventos casi seguros |
| $\alpha = \beta > 1$         | Simétrica (Campana)      | Modelar estimaciones cercanas a 0.5 |

### 💻Ejemplos en codigo

```python
from scipy.stats import beta
import numpy as np

## ====================================================================
## 1. Modelado de Proporciones (Proporción de Tiempo Operativo)
## ====================================================================
print("--- 1. Proporción de Tiempo Operativo (Beta) ---")

## Parámetros basados en datos históricos (Beta(9, 2))
## Esto implica que la máquina está operativa la mayor parte del tiempo
alpha_op = 9
beta_op = 2
proporcion_interes = 0.85  # Queremos P(X < 0.85)

## 1a. Calcular P(X < 0.85)
## Usamos .cdf() (Cumulative Distribution Function)
prob_menor_85 = beta.cdf(proporcion_interes, a=alpha_op, b=beta_op)

## 1b. Calcular la media de la proporción (E[X] = alpha / (alpha + beta))
media_proporcion = alpha_op / (alpha_op + beta_op)

## 1c. Calcular la moda (Si alpha, beta > 1, Moda = (alpha - 1) / (alpha + beta - 2))
moda_proporcion = (alpha_op - 1) / (alpha_op + beta_op - 2)

print(f"Parámetros: Beta({alpha_op}, {beta_op})")
print(f"Media de la proporción operativa: {media_proporcion:.4f}")
print(f"Moda de la proporción operativa: {moda_proporcion:.4f}")
print(f"Probabilidad de que la proporción sea menor a {proporcion_interes} (P(X < 0.85)): {prob_menor_85:.4f}")

## ====================================================================
## 2. Inferencia Bayesiana (Moneda Sesgada - Distribución Posterior)
## ====================================================================
print("\n--- 2. Inferencia Bayesiana (Distribución Posterior) ---")

## A Priori: Uniforme Beta(1, 1).
## Datos: 7 Caras (éxitos), 3 Cruces (fracasos).
alpha_post = 1 + 7  # 8
beta_post = 1 + 3   # 4
probabilidad_rango = 0.6  # Queremos P(p < 0.6)

## 2a. Calcular P(p < 0.6) para la probabilidad real de la moneda
prob_posterior = beta.cdf(probabilidad_rango, a=alpha_post, b=beta_post)

## 2b. Calcular un Intervalo de Credibilidad del 95% para p (la probabilidad real)
## Usamos .ppf() (Percent Point Function) o función cuantil
limite_inferior = beta.ppf(0.025, a=alpha_post, b=beta_post)
limite_superior = beta.ppf(0.975, a=alpha_post, b=beta_post)

print(f"Distribución Posterior: Beta({alpha_post}, {beta_post})")
print(f"Probabilidad de que la probabilidad real 'p' sea menor a {probabilidad_rango} (P(p < 0.6)): {prob_posterior:.4f}")
print(f"Intervalo de Credibilidad 95% para 'p': [{limite_inferior:.3f}, {limite_superior:.3f}]")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

## Configuración de los gráficos
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(3, 1, figsize=(10, 15))
fig.suptitle('Visualización de la Distribución Beta (Proporciones y Probabilidades)', fontsize=16, y=1.02)

## Rango de la variable X (siempre [0, 1])
x_beta = np.linspace(0.01, 0.99, 500)

## ====================================================================
## 1. Modelado de Proporciones (Tiempo Operativo: Beta(9, 2))
## ====================================================================
alpha_op, beta_op = 9, 2
proporcion_interes = 0.85

y_pdf_op = beta.pdf(x_beta, a=alpha_op, b=beta_op)

ax = axes[0]
ax.plot(x_beta, y_pdf_op, color='blue', label=f'Beta({alpha_op}, {beta_op})')
ax.fill_between(x_beta, y_pdf_op, where=(x_beta < proporcion_interes),
                color='lightblue', alpha=0.6,
                label='P(Proporción < 0.85)')
ax.axvline(proporcion_interes, color='red', linestyle='--', label=f'Límite: {proporcion_interes}')
ax.set_title('1. Proporción de Tiempo Operativo (Sesgada a la Izquierda)')
ax.set_xlabel('Proporción')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## ====================================================================
## 2. Inferencia Bayesiana (Moneda Sesgada - Posterior: Beta(8, 4))
## ====================================================================
alpha_post, beta_post = 8, 4
lim_inf, lim_sup = beta.ppf([0.025, 0.975], a=alpha_post, b=beta_post)

y_pdf_post = beta.pdf(x_beta, a=alpha_post, b=beta_post)

ax = axes[1]
ax.plot(x_beta, y_pdf_post, color='green', label=f'Beta({alpha_post}, {beta_post}) Posterior')
ax.fill_between(x_beta, y_pdf_post, where=((x_beta >= lim_inf) & (x_beta <= lim_sup)),
                color='lightgreen', alpha=0.6,
                label='Intervalo de Credibilidad del 95%')
ax.axvline(lim_inf, color='gray', linestyle=':')
ax.axvline(lim_sup, color='gray', linestyle=':')
ax.axvline(alpha_post / (alpha_post + beta_post), color='red', linestyle='--', label='Media Posterior')
ax.set_title('2. Distribución Posterior de la Probabilidad de Cara (Bayesiana)')
ax.set_xlabel('Probabilidad Real (p)')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## ====================================================================
## 3. Flexibilidad de la Forma (Visualización de casos)
## ====================================================================
params = [
    (1, 1, 'Uniforme (Beta(1, 1))', 'black'),     # Uniforme
    (0.5, 5, 'Sesgada a la derecha (Beta(0.5, 5))', 'red'), # Sesgada a la derecha
    (3, 3, 'Simétrica (Campana) (Beta(3, 3))', 'blue')  # Simétrica
]

ax = axes[2]
for a, b, label, color in params:
    y_pdf_flex = beta.pdf(x_beta, a=a, b=b)
    ax.plot(x_beta, y_pdf_flex, color=color, linestyle='-', label=label, linewidth=2)

ax.set_title('3. Flexibilidad de la Forma de la Distribución Beta')
ax.set_xlabel('Proporción o Probabilidad')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()
ax.set_ylim(0, 4) # Ajuste para mejor visualización de formas

## Ajustar diseño y mostrar
plt.tight_layout()
plt.show()
```

### ✨Distribución Weibull

* **Descripción**: Modelo utilizado para analizar el tiempo hasta el fallo de un sistema o un componente. Es especialmente útil en el análisis de fiabilidad y en estudios de vida.

* **Parámetros**:
  - \( \lambda \) (escala)
  - \( k \) (forma)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x) =
\begin{cases}
\frac{k}{\lambda} \left( \frac{x}{\lambda} \right)^{k-1} e^{-\left( \frac{x}{\lambda} \right)^k} & \text{si } x \geq 0 \\
0 & \text{si } x < 0
\end{cases}
$$

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) =
\begin{cases}
1 - e^{-\left( \frac{x}{\lambda} \right)^k} & \text{si } x \geq 0 \\
0 & \text{si } x < 0
\end{cases}
$$

* **Valor Esperado**:
$$
E[X] = \lambda \Gamma\left(1 + \frac{1}{k}\right)
$$

* **Media**:
$$
\mu_X = \lambda \Gamma\left(1 + \frac{1}{k}\right)
$$

* **Desviación Estándar**:
$$
\sigma = \lambda \sqrt{\Gamma\left(1 + \frac{2}{k}\right) - \left(\Gamma\left(1 + \frac{1}{k}\right)\right)^2}
$$

* **Percentiles**: \( x_\alpha = \lambda \left( -\log(1 - \alpha) \right)^{\frac{1}{k}} \)

**Comandos en R**:
```r
## PDF
dweibull(x, shape = k, scale = lambda)

## CDF
pweibull(x, shape = k, scale = lambda)

## Simulación
rweibull(n, shape = k, scale = lambda)

```python
import numpy as np
from scipy.stats import weibull_min

## ----------------------------------------
## Definición de parámetros
k = 2.0     # Parámetro de forma (shape en R, c en Python)
lambda_scale = 1.5 # Parámetro de escala (scale en R y Python)
x = 3.0     # valor para PDF/CDF
n = 10      # número de muestras para simulación

## ----------------------------------------
## PDF (Función de Densidad de Probabilidad)
## dweibull(x, shape = k, scale = lambda_scale)
## scipy.stats.weibull_min.pdf(x, c=k, scale=lambda_scale)
## Nota: La función en scipy es weibull_min
pdf_value = weibull_min.pdf(x, c=k, scale=lambda_scale)
print(f"PDF (weibull_min.pdf) para x={x}: {pdf_value}")

## ----------------------------------------
## CDF (Función de Distribución Acumulada)
## pweibull(x, shape = k, scale = lambda_scale)
## scipy.stats.weibull_min.cdf(x, c=k, scale=lambda_scale)
cdf_value = weibull_min.cdf(x, c=k, scale=lambda_scale)
print(f"CDF (weibull_min.cdf) para x={x}: {cdf_value}")

## ----------------------------------------
## Simulación/Muestreo
## rweibull(n, shape = k, scale = lambda_scale)
## np.random.weibull(a=k, size=n) * lambda_scale
## NOTA: np.random.weibull solo toma 'a' (forma) y asume scale=1.
## Se debe multiplicar por el parámetro de escala (lambda_scale).
## (Esto es equivalente a usar rweibull(n, shape=k, scale=lambda_scale) en R)
## Para coincidir con la parametrización de R:
samples_standard = np.random.weibull(a=k, size=n)
samples = samples_standard * lambda_scale
print(f"Muestras (np.random.weibull * scale) n={n}: {samples}")
```

#### 🔍Ejemplo de Gráfica de la Distribución Weibull

La distribución Weibull es un modelo de probabilidad utilizado para describir el tiempo hasta un evento, como el tiempo de vida de un producto o el tiempo hasta el fallo de un sistema. Es especialmente útil en análisis de confiabilidad y en la modelación de datos de supervivencia. La distribución se define por dos parámetros: la forma $ k $ y la escala $ \lambda $.

El parámetro de forma $ k $ determina la naturaleza de la distribución:
- Si $ k < 1 $, la distribución tiene una alta tasa de fallo inicial, lo que indica que los fallos son más comunes al principio.
- Si $ k = 1 $, la distribución se convierte en una distribución exponencial, indicando una tasa de fallo constante.
- Si $ k > 1 $, la tasa de fallo aumenta con el tiempo, lo que sugiere un desgaste.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad (PDF) de la distribución Weibull para varios valores de $ k $ y $ \lambda $. A medida que se ajustan estos parámetros, la forma de la distribución varía, reflejando cómo diferentes combinaciones de $ k $ y $ \lambda $ influyen en la concentración de probabilidad y en la forma de la curva.

La distribución Weibull es valiosa en diversas áreas, como la ingeniería y la economía, donde se requiere modelar la vida útil de productos o la duración de ciertos procesos.

```python
"""

## Cargar la librería necesaria
library(ggplot2)

## Definir los parámetros de la distribución Weibull
k_values <- c(0.5, 1, 2)  # Parámetro de forma
lambda_values <- c(1, 1, 1)  # Parámetro de escala

## Crear un rango de valores para x
x <- seq(0, 3, length.out = 100)

## Crear un data frame vacío para almacenar los resultados
data <- data.frame()

## Calcular la PDF para cada combinación de k y lambda
for (i in 1:length(k_values)) {
  k <- k_values[i]
  lambda <- lambda_values[i]
  pdf_values <- dweibull(x, shape = k, scale = lambda)

## Añadir los resultados al data frame
  data <- rbind(data, data.frame(x = x, pdf = pdf_values, k = factor(k), lambda = lambda))
}

## Graficar las distribuciones
ggplot(data, aes(x = x, y = pdf, color = k)) +
  geom_line() +
  labs(title = "Funciones de Densidad de la Distribución Weibull",
       x = "x",
       y = "Densidad de Probabilidad (PDF)",
       color = "Parámetro k") +
  theme_minimal()

"""
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import weibull_min

## ----------------------------------------
## 1. Definir los parámetros de la distribución Weibull
k_values = [0.5, 1, 2]     # Parámetro de forma (k, se mapea a 'c' en scipy)
lambda_values = [1, 1, 1]  # Parámetro de escala (lambda, se mapea a 'scale' en scipy)

## ----------------------------------------
## 2. Crear un rango de valores para x (equivalente a seq() en R)
x = np.linspace(0.01, 3, 100) # Se usa 0.01 como inicio para evitar problemas en el límite

## ----------------------------------------
## 3. Calcular la PDF y consolidar en un solo DataFrame
data_list = []

## Iterar sobre las combinaciones de parámetros
for k, lambda_scale in zip(k_values, lambda_values):
## Calcular la PDF (equivalente a dweibull() en R)
## scipy.stats.weibull_min.pdf(x, c=k, scale=lambda_scale)
    pdf_values = weibull_min.pdf(x, c=k, scale=lambda_scale)

## Crear DataFrame temporal y almacenar
    df_temp = pd.DataFrame({
        'x': x,
        'pdf': pdf_values,
## Convertir 'k' a string para usarlo en la leyenda (similar a factor(k) en R)
        'k': str(k),
        'lambda': lambda_scale
    })
    data_list.append(df_temp)

## Combinar todos los DataFrames
data = pd.concat(data_list, ignore_index=True)

## ----------------------------------------
## 4. Graficar las distribuciones (equivalente a ggplot2)

## Configurar el estilo (theme_minimal)
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

## Crear la gráfica con Seaborn, usando 'k' para el color
## 'hue' mapea los diferentes valores de k al color de la línea
sns.lineplot(
    data=data,
    x='x',
    y='pdf',
    hue='k',
    linewidth=2
)

## Añadir títulos y etiquetas (labs)
plt.title("Funciones de Densidad de la Distribución Weibull", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("Densidad de Probabilidad (PDF)", fontsize=14)

## Ajustar leyenda
plt.legend(title="Parámetro k", loc='upper right', frameon=True)

## Mostrar la gráfica
plt.show()
```

#### 📜**Descripción del Código**

* **Cargar librerías**: Se utiliza `ggplot2` para crear la gráfica.
* **Crear un rango de valores para $x$**: Se define un rango de valores de $ 0 $ a $ 3 $ para representar la distribución Weibull.
* **Definir los parámetros**: Se establecen los parámetros $ k $ y $ \lambda $ para tres configuraciones diferentes de la distribución Weibull.
* **Calcular la PDF**: Se utiliza `dweibull()` para calcular la función de densidad de probabilidad para los valores de $ x $ con los parámetros definidos.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $ x $ y sus correspondientes probabilidades para las configuraciones de la distribución Weibull.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $ PDF $ de la distribución Weibull para los diferentes parámetros, permitiendo observar cómo varía la forma de la distribución.

**EJERCICIO 14**

Agrega ejemplos y los usos recomendados.

### ⚙️ Usos Recomendados de la Distribución Weibull

La **Distribución Weibull** es una distribución continua y positiva que se utiliza casi exclusivamente en el campo de la **fiabilidad y el análisis de vida útil**. Es una de las distribuciones más versátiles para modelar el tiempo hasta el fallo de un sistema o componente, ya que puede adaptarse a diferentes tasas de fallo (constante, creciente o decreciente) mediante su parámetro clave de **forma**.

La distribución Weibull se define por tres parámetros: **forma** ($\beta$ o $k$), **escala** ($\eta$ o $\lambda$) y **ubicación** ($\gamma$, a menudo asumido como 0).

1.  **Análisis de Fiabilidad e Ingeniería de Fallos**
    Es el modelo dominante para predecir la vida útil y la tasa de fallos de productos en ingeniería, ya que el parámetro de forma ($\beta$) permite modelar el modo de fallo subyacente.

    * **Ejemplo:** La **vida útil** de los **rodamientos de bolas, motores** o **equipos hidráulicos**. Al ajustar la distribución Weibull a los datos de fallo, los ingenieros pueden determinar si los fallos ocurren al principio de la vida útil (fallos infantiles, $\beta < 1$) o debido al desgaste (fallos por envejecimiento, $\beta > 1$).
    * **Aplicación:** Determinar los **intervalos de mantenimiento preventivo** para que los componentes sean reemplazados antes de que entren en la fase de desgaste acelerado.

2.  **Modelado de la Tasa de Fallo (Función de Peligro)**
    La flexibilidad clave de Weibull radica en su capacidad para representar diferentes comportamientos de la **tasa de fallo (o función de riesgo)** a lo largo del tiempo, algo esencial en el diseño de productos.

    | Parámetro de Forma ($\beta$) | Implicación de la Tasa de Fallo | Modo de Fallo |
    | :--------------------------- | :------------------------------ | :------------ |
    | $\beta < 1$                  | Tasa de fallo **decreciente** | Fallos iniciales (infantiles); defectos de fabricación que se "purgan". |
    | $\beta = 1$                  | Tasa de fallo **constante** | **Distribución Exponencial**; fallos aleatorios o por choques externos. |
    | $\beta > 1$                  | Tasa de fallo **creciente** | Fallos por desgaste o envejecimiento; la probabilidad de fallo aumenta con el tiempo. |

3.  **Ciencias Ambientales y Fenómenos Extremos**
    Aunque menos común que en ingeniería, su flexibilidad permite modelar variables donde la intensidad o la magnitud varía con el tiempo.

    * **Ejemplo:** La **velocidad del viento** en una región. Es crucial para el diseño de turbinas eólicas. La Distribución Weibull proporciona un ajuste muy preciso para la distribución de la velocidad del viento a lo largo de un período de tiempo.
    * **Aplicación:** Modelar las **intensidades de inundaciones** o la **resistencia a la rotura** de materiales.

---
### 🧪 Relación Clave

* La **Distribución Weibull** es una generalización de la **Distribución Exponencial**.
* Cuando el parámetro de **forma** es $\beta = 1$, la Distribución Weibull se simplifica a la **Distribución Exponencial**.

$$\text{Weibull}(\beta=1, \eta) \equiv \text{Exponencial}(\lambda=1/\eta)$$

### 💻Ejemplos en codigo

```python
from scipy.stats import weibull_min

## ====================================================================
## 1. Ingeniería de Fallos (Rodamientos con Desgaste)
## ====================================================================
print("--- 1. Ingeniería de Fallos (Rodamientos) ---")

## Parámetros (ejemplo de desgaste, beta > 1)
forma_beta = 2.5
escala_eta = 8000  # Horas (vida característica)

tiempo_mantenimiento = 5000  # Queremos P(X < 5000 horas)
tiempo_garantia = 1000  # Queremos P(X < 1000 horas)

## 1a. Calcular la probabilidad de fallo P(X < 5000)
## Usamos .cdf() (Cumulative Distribution Function)
prob_fallo_5k = weibull_min.cdf(tiempo_mantenimiento, c=forma_beta, scale=escala_eta)

## 1b. Calcular la probabilidad de fallo durante la garantía P(X < 1000)
prob_fallo_1k = weibull_min.cdf(tiempo_garantia, c=forma_beta, scale=escala_eta)

## 1c. Calcular la vida útil donde solo el 10% ha fallado (Percentil 10)
percentil_10 = weibull_min.ppf(0.10, c=forma_beta, scale=escala_eta)

print(f"Parámetros: Forma (β) = {forma_beta}, Escala (η) = {escala_eta} h")
print(f"Probabilidad de fallo antes de 5000h: {prob_fallo_5k:.4f}")
print(f"Probabilidad de fallo en garantía (antes de 1000h): {prob_fallo_1k:.4f}")
print(f"El 10% de los rodamientos fallará antes de: {percentil_10:.0f} horas")

## ====================================================================
## 2. Modelado de la Tasa de Fallo (Comparación de Modos de Fallo)
## ====================================================================
print("\n--- 2. Tasa de Fallo (Modos de Fallo) ---")

## Parámetros para un componente con fallos iniciales (infantiles, beta < 1)
forma_infantil = 0.8
escala_infantil = 200  # Días

## Probabilidad de fallo en los primeros 50 días: P(X < 50)
tiempo_corto = 50
prob_fallo_infantil = weibull_min.cdf(tiempo_corto, c=forma_infantil, scale=escala_infantil)

## Parámetros para un fallo aleatorio (Exponencial, beta = 1)
forma_aleatorio = 1.0
escala_aleatorio = 200  # Mismo tiempo característico

## Probabilidad de fallo en los primeros 50 días: P(X < 50)
prob_fallo_aleatorio = weibull_min.cdf(tiempo_corto, c=forma_aleatorio, scale=escala_aleatorio)

print(f"Fallo Infantil (β={forma_infantil}): P(X < 50 días) = {prob_fallo_infantil:.4f}")
print(f"Fallo Aleatorio (β={forma_aleatorio}): P(X < 50 días) = {prob_fallo_aleatorio:.4f}")

## ====================================================================
## 3. Ciencias Ambientales (Velocidad del Viento)
## ====================================================================
print("\n--- 3. Velocidad del Viento (Ciencias Ambientales) ---")

## Parámetros de la velocidad del viento (ejemplo típico)
forma_viento = 1.9
escala_viento = 7.0  # m/s (velocidad promedio)

velocidad_corte_turbina = 15  # Velocidad para generación óptima
## Calcular la probabilidad de que la velocidad sea > 15 m/s
prob_viento_fuerte = weibull_min.sf(velocidad_corte_turbina, c=forma_viento, scale=escala_viento)

print(f"Parámetros: Forma (β) = {forma_viento}, Escala (η) = {escala_viento} m/s")
print(f"Probabilidad de que la velocidad del viento sea > {velocidad_corte_turbina} m/s: {prob_viento_fuerte:.4f}")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

## Configuración de los gráficos
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(3, 1, figsize=(10, 15))
fig.suptitle('Visualización de la Distribución Weibull (Fiabilidad y Tasa de Fallo)', fontsize=16, y=1.02)

## ====================================================================
## 1. Ingeniería de Fallos (Rodamientos con Desgaste)
## ====================================================================
forma_beta = 2.5
escala_eta = 8000
tiempo_mantenimiento = 5000

## Rango de X (tiempo en horas)
x_fallo = np.linspace(0, 25000, 500)
## Calcular la PDF
y_pdf_fallo = weibull_min.pdf(x_fallo, c=forma_beta, scale=escala_eta)

ax = axes[0]
ax.plot(x_fallo, y_pdf_fallo, color='blue', label=f'Weibull(β={forma_beta}, η={escala_eta})')
ax.fill_between(x_fallo, y_pdf_fallo, where=(x_fallo < tiempo_mantenimiento),
                color='lightblue', alpha=0.6,
                label='P(Fallo antes de 5000h)')
ax.axvline(escala_eta, color='green', linestyle=':', label=f'Escala (η): {escala_eta} h')
ax.axvline(tiempo_mantenimiento, color='red', linestyle='--', label=f'Mantenimiento: {tiempo_mantenimiento} h')

ax.set_title('1. Vida Útil de Componentes (Desgaste, β > 1)')
ax.set_xlabel('Tiempo de Vida Útil (horas)')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## ====================================================================
## 2. Modelado de la Tasa de Fallo (Comparación de Modos)
## ====================================================================
escala_comun = 100 # Días, simplificado para la gráfica

## Diferentes formas (modos de fallo)
formas = [
    (0.8, 'Fallos Iniciales (β < 1)', 'red'),
    (1.0, 'Fallos Aleatorios (β = 1, Exponencial)', 'green'),
    (2.0, 'Fallos por Desgaste (β > 1)', 'blue')
]

x_modos = np.linspace(0, 300, 500)
ax = axes[1]
for beta, label, color in formas:
    y_pdf_modos = weibull_min.pdf(x_modos, c=beta, scale=escala_comun)
    ax.plot(x_modos, y_pdf_modos, color=color, label=label, linewidth=2)

ax.set_title(f'2. Flexibilidad de Weibull según la Tasa de Fallo (η={escala_comun})')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## ====================================================================
## 3. Ciencias Ambientales (Velocidad del Viento)
## ====================================================================
forma_viento = 1.9
escala_viento = 7.0
velocidad_corte = 15

## Rango de X (velocidad en m/s)
x_viento = np.linspace(0, 25, 500)
## Calcular la PDF
y_pdf_viento = weibull_min.pdf(x_viento, c=forma_viento, scale=escala_viento)

ax = axes[2]
ax.plot(x_viento, y_pdf_viento, color='purple', label=f'Weibull(β={forma_viento}, η={escala_viento})')
ax.fill_between(x_viento, y_pdf_viento, where=(x_viento > velocidad_corte),
                color='violet', alpha=0.6,
                label='P(Viento > 15 m/s)')
ax.axvline(escala_viento, color='gray', linestyle=':', label=f'Escala: {escala_viento} m/s')
ax.axvline(velocidad_corte, color='red', linestyle='--', label=f'Corte: {velocidad_corte} m/s')

ax.set_title('3. Distribución de la Velocidad del Viento')
ax.set_xlabel('Velocidad del Viento (m/s)')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## Ajustar diseño y mostrar
plt.tight_layout()
plt.show()
```

### ✨Distribución de Dirichlet

* **Descripción**: Modelo de distribuciones de probabilidad sobre un conjunto de variables aleatorias que suman uno. Se utiliza comúnmente en la teoría bayesiana y en el análisis de composiciones.

* **Parámetros**:
$\alpha_1, \alpha_2, \ldots, \alpha_k $ (parámetros de forma, donde $k $ es el número de variables)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x_1, x_2, \ldots, x_k) =
\begin{cases}
\frac{1}{B(\alpha)} \prod_{i=1}^{k} x_i^{\alpha_i - 1} & \text{si } x_i \geq 0 \text{ y } \sum_{i=1}^{k} x_i = 1 \\
0 & \text{en otro caso}
\end{cases}
$$
donde $ B(\alpha)$ es la función beta multivariada:

$$
B(\alpha) = \frac{\prod_{i=1}^{k} \Gamma(\alpha_i)}{\Gamma\left(\sum_{i=1}^{k} \alpha_i\right)}
$$

* **Valor Esperado**:
$$
E[X_i] = \frac{\alpha_i}{\sum_{j=1}^{k} \alpha_j}
$$

* **Media**:
$$
\mu_{X_i} = \frac{\alpha_i}{\sum_{j=1}^{k} \alpha_j}
$$

* **Desviación Estándar**:
$$
\text{Var}(X_i) = \frac{\alpha_i (\sum_{j=1}^{k} \alpha_j - \alpha_i)}{\left(\sum_{j=1}^{k} \alpha_j\right)^2 \left(\sum_{j=1}^{k} \alpha_j + 1\right)}
$$

* **Comandos en R**:

```r
## PDF
ddirichlet(x, alpha)

## CDF
pdirichlet(x, alpha)

## Simulación
rdirichlet(n, alpha)

```python
import numpy as np

## ----------------------------------------
## Definición de parámetros
alpha = [0.5, 0.5, 0.5] # Vector de parámetros alpha (e.g., para K=3 dimensiones)
n = 5                   # número de muestras para simulación

## ----------------------------------------
## Simulación/Muestreo
## rdirichlet(n, alpha)
## np.random.dirichlet(alpha=alpha, size=n)
samples = np.random.dirichlet(alpha=alpha, size=n)
print(f"Muestras (np.random.dirichlet) n={n}:")
print(samples)
```

```python
from scipy.special import gamma
import numpy as np

def ddirichlet_py(x, alpha):
    """Calcula la PDF de la distribución de Dirichlet."""

## x debe ser un array con K elementos (componentes)
    x = np.array(x)
    alpha = np.array(alpha)
    K = len(alpha)

## 1. Calcular el denominador (Función Beta Multivariada, B(alpha))
## B(alpha) = [Producto(Gamma(alpha_i))] / [Gamma(Suma(alpha_i))]
    B_alpha = np.prod(gamma(alpha)) / gamma(np.sum(alpha))

## 2. Calcular el numerador (Producto(x_i^(alpha_i - 1)))
## Nota: np.prod y np.power manejan arrays de forma eficiente
    numerator = np.prod(np.power(x, alpha - 1))

## 3. PDF
    pdf_value = numerator / B_alpha
    return pdf_value

## ----------------------------------------
## Ejemplo de uso de la PDF
alpha = [0.5, 0.5, 0.5] # Parámetros (alpha_1, alpha_2, alpha_3)
## x debe ser un punto en el simplex (sum(x) = 1)
x = [0.2, 0.5, 0.3]

## Comprobación del simplex:
if np.isclose(sum(x), 1.0) and all(val > 0 for val in x):
    pdf_value = ddirichlet_py(x, alpha)
    print(f"\nPDF (ddirichlet_py) para x={x}: {pdf_value}")
else:
    print("\nEl vector x no es un punto válido en el simplex (la suma debe ser 1).")
```

#### 🔍Ejemplo de Gráfica de la Distribución de Dirichlet

La distribución de Dirichlet es una distribución de probabilidad multivariada que se utiliza para modelar vectores de proporciones que suman 1. Se define mediante un vector de parámetros $\boldsymbol{\alpha} = (\alpha_1, \alpha_2, \ldots, \alpha_k)$, donde $k$ es el número de variables aleatorias. Esta distribución es especialmente útil en estadística bayesiana y en la teoría de juegos.

La forma de la distribución de Dirichlet se determina por los valores de los parámetros $\alpha_i$:
- Si todos los $\alpha_i$ son iguales, la distribución es simétrica.
- Si los $\alpha_i$ son diferentes, la distribución puede ser sesgada hacia alguna de las proporciones.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad (PDF) de la distribución de Dirichlet para varios conjuntos de valores de $\boldsymbol{\alpha}$. A medida que se ajustan estos parámetros, la forma de la distribución varía, lo que refleja cómo las diferentes combinaciones de $\boldsymbol{\alpha}$ influyen en la concentración de probabilidad.

La distribución de Dirichlet es valiosa en campos como el aprendizaje automático, la inferencia estadística y la teoría de mezclas.

```python
"""

## Cargar las librerías necesarias
library(ggplot2)
library(dplyr)
library(MCMCpack)  # Asegúrate de que MCMCpack esté instalado

## Definir los parámetros de la distribución Dirichlet
alpha_values <- list(c(1, 1, 1), c(2, 5, 3), c(5, 1, 1))  # Diferentes vectores de parámetros

## Inicializar una lista para almacenar los gráficos
plots <- list()

## Generar muestras para cada conjunto de parámetros
for (alpha in alpha_values) {
## Generar muestras aleatorias de la distribución Dirichlet
  n_points <- 1000  # Número de muestras
  samples <- rdirichlet(n_points, alpha)

## Convertir las muestras en un data frame
  sample_data <- as.data.frame(samples)
  colnames(sample_data) <- c("x1", "x2", "x3")  # Nombrar columnas

## Graficar para cada conjunto de parámetros
  p <- ggplot(sample_data, aes(x = x1, y = x2)) +
    geom_point(alpha = 0.5) +
    labs(title = paste("Distribución Dirichlet (α = (", paste(alpha, collapse = ", "), "))", sep = ""),
         x = "$x_1$",
         y = "$x_2$") +
    theme_minimal() +
    xlim(0, 1) + ylim(0, 1)  # Limitar ejes a [0,1]

## Almacenar el gráfico en la lista
  plots[[length(plots) + 1]] <- p
}

## Mostrar los gráficos
for (plot in plots) {
  print(plot)
}

"""
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## ----------------------------------------
## 1. Definir los parámetros de la distribución Dirichlet
## Diferentes vectores de parámetros alpha (equivalente a la list en R)
alpha_values = [[1, 1, 1], [2, 5, 3], [5, 1, 1]]

## ----------------------------------------
## 2. Configuración de la simulación
n_points = 1000  # Número de muestras (equivalente a n_points en R)
all_data = [] # Lista para almacenar los DataFrames de las muestras

## 3. Generar muestras para cada conjunto de parámetros (equivalente al bucle for en R)
for alpha in alpha_values:
## Generar muestras aleatorias (equivalente a rdirichlet() en R)
    samples = np.random.dirichlet(alpha=alpha, size=n_points)

## Convertir las muestras en un DataFrame
    sample_data = pd.DataFrame(samples, columns=["x1", "x2", "x3"])

## Añadir una etiqueta para identificar el conjunto de parámetros
    alpha_label = f"α = ({', '.join(map(str, alpha))})"
    sample_data['alpha_set'] = alpha_label

    all_data.append(sample_data)

## 4. Combinar todos los data frames para la graficación (opcional, pero limpio)
## En este caso, graficaremos de forma individual para replicar el 'print(plot)' de R.

## ----------------------------------------
## 5. Graficar las distribuciones (equivalente a ggplot2)
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (15, 5) # Configurar tamaño de las figuras

fig, axes = plt.subplots(1, len(alpha_values), figsize=(18, 6))
axes = axes.flatten() # Asegurar que es un array, incluso si es un solo gráfico

for i, (alpha, data_df) in enumerate(zip(alpha_values, all_data)):
## Crear el gráfico de dispersión (equivalente a geom_point())
    sns.scatterplot(
        x='x1',
        y='x2',
        data=data_df,
        ax=axes[i],
        alpha=0.6, # Transparencia de los puntos
        edgecolor=None,
        s=10 # Tamaño del punto
    )

## Añadir títulos y etiquetas (equivalente a labs())
    axes[i].set_title(f"Distribución Dirichlet (α = ({', '.join(map(str, alpha))}))", fontsize=14)
    axes[i].set_xlabel(r'$x_1$', fontsize=12) # Uso de LaTeX para subíndices
    axes[i].set_ylabel(r'$x_2$', fontsize=12)

## Limitar ejes a [0,1] (equivalente a xlim y ylim)
    axes[i].set_xlim(0, 1)
    axes[i].set_ylim(0, 1)

## Opcional: Graficar el simplex 2D (x1 + x2 <= 1)
    axes[i].plot([0, 1], [1, 0], 'k--', alpha=0.5, linewidth=1)
    axes[i].plot([0, 0], [0, 1], 'k--', alpha=0.5, linewidth=1)
    axes[i].plot([0, 1], [0, 0], 'k--', alpha=0.5, linewidth=1)

plt.tight_layout(rect=[0, 0, 1, 0.95]) # Ajustar diseño para evitar superposiciones
plt.suptitle("Visualización de Muestras de la Distribución Dirichlet (3D proyectada)", fontsize=16, y=1.02)
plt.show()
```

#### 🤔**Interpretación de los Resultados**

1. **Ejes del Gráfico**:
   - El eje X representa la proporción de la primera variable ($x_1$).
   - El eje Y representa la proporción de la segunda variable ($x_2$).
   - La tercera variable ($x_3$) se infiere como $1 - x_1 - x_2$, lo que significa que la suma de las tres proporciones siempre es igual a 1.

2. **Forma de la Distribución**:
   - **Distribuciones Simétricas**: Cuando se utilizan valores de $\alpha$ iguales (como en el caso de $\alpha = (1, 1, 1)$), los puntos se distribuyen de manera uniforme dentro del triángulo delimitado por los ejes, mostrando una forma simétrica. Esto indica que todas las proporciones tienen la misma probabilidad de ocurrir.
   - **Distribuciones Asimétricas**: En contraste, cuando los valores de $\alpha$ son diferentes (por ejemplo, $\alpha = (2, 5, 3)$), los puntos tienden a agruparse más cerca de ciertos vértices del triángulo. Esto muestra que algunas proporciones son más probables que otras, reflejando la asimetría de la distribución.

3. **Concentración de Puntos**:
   - La densidad de los puntos en ciertas áreas del gráfico indica dónde es más probable encontrar combinaciones de proporciones. Por ejemplo, si hay un área donde hay muchos puntos, eso sugiere que las combinaciones de proporciones que corresponden a esos puntos son más comunes.
   - Si se observan áreas vacías, significa que esas combinaciones de proporciones son menos probables.

4. **Variabilidad**:
   - Las muestras generadas reflejan la variabilidad de las proporciones que se pueden obtener para un conjunto dado de parámetros $\alpha$. Por ejemplo, para valores de $\alpha$ muy diferentes entre sí, la variabilidad en las proporciones puede ser mayor, mientras que para valores más homogéneos, la variabilidad es menor.

### Resumen
Los diagramas de dispersión te permiten visualizar cómo la distribución Dirichlet modela combinaciones de proporciones en un contexto donde estas deben sumar 1. A medida que cambian los parámetros $\alpha$, la forma y la concentración de las muestras cambian, lo que refleja la influencia de esos parámetros en la distribución de probabilidad de las proporciones. Estos gráficos son útiles en campos como la estadística bayesiana, el aprendizaje automático y la teoría de juegos, donde entender la relación entre variables proporcionales es clave.

#### 📜**Descripción del Código**

* **Cargar las librerías**: Se utilizan `ggplot2`, `dplyr` y `MCMCpack` para crear las gráficas y manejar datos. Asegúrate de que `MCMCpack` esté instalado en tu entorno de R.

* **Definir los parámetros**: Se establece una lista de vectores de parámetros $ \boldsymbol{\alpha} $ para diferentes configuraciones de la distribución Dirichlet. En este caso, se consideran tres conjuntos de parámetros: $(1, 1, 1)$, $(2, 5, 3)$ y $(5, 1, 1)$.

* **Inicializar una lista para almacenar los gráficos**: Se crea una lista vacía `plots` que se utilizará para guardar los gráficos generados.

* **Generar muestras**: Para cada conjunto de parámetros:
  - Se generan muestras aleatorias de la distribución Dirichlet utilizando la función `rdirichlet()` con un número especificado de muestras (1000 en este caso).
  - Las muestras se convierten en un data frame, y se nombran las columnas como $x_1$, $x_2$ y $x_3$ para representar las proporciones.

* **Graficar**: Se utiliza `ggplot` para crear un gráfico de dispersión de las muestras generadas:
  - Se mapea $x_1$ en el eje X y $x_2$ en el eje Y.
  - Se ajusta la transparencia de los puntos para mejorar la visualización.
  - Se añaden etiquetas al gráfico y se limitan los ejes a un rango de [0, 1].

* **Almacenar y mostrar los gráficos**: Cada gráfico generado se almacena en la lista `plots`, y posteriormente se imprimen todos los gráficos utilizando un bucle.

### Resumen
Este código ilustra cómo generar y visualizar muestras de la distribución Dirichlet para diferentes configuraciones de parámetros. Los gráficos resultantes permiten observar la distribución de las proporciones en un espacio de probabilidades, lo que es útil en contextos de modelado estadístico y análisis de datos.

**EJERCICIO 15**

Agrega ejemplos y los usos recomendados.

### 🧬 Usos Recomendados de la Distribución Dirichlet

La **Distribución Dirichlet** $\text{Dir}(\alpha_1, \alpha_2, \ldots, \alpha_K)$ es la generalización multivariante de la Distribución Beta. Modela la **distribución de probabilidades** sobre $K$ categorías, donde cada categoría es una proporción positiva y la suma de todas las proporciones es igual a 1. Se define sobre un **símplex estándar** de $K-1$ dimensiones.

1.  **Modelado de Proporciones Categóricas (Composiciones)**
    Es fundamental para modelar cómo se distribuyen las partes de un todo, es decir, las composiciones de un conjunto limitado.

    * **Ejemplo:** La **proporción de géneros (o *tags*)** que un usuario individual usa para categorizar su biblioteca de música (e.g., Rock: 30%, Jazz: 15%, Clásica: 55%). La Dirichlet genera un vector de proporciones $(p_1, p_2, \ldots, p_K)$ donde $\sum p_i = 1$, asegurando que las proporciones son coherentes.
    * **Aplicación:** La proporción de **nutrientes** (carbohidratos, grasas, proteínas) en la dieta de una persona o la proporción de **especies de árboles** en un ecosistema.

2.  **Modelado de Temas en Procesamiento de Lenguaje Natural (NLP)**
    Su uso más famoso es en el modelo de tópicos **Latent Dirichlet Allocation (LDA)**, donde modela las distribuciones de probabilidades subyacentes.

    * **Ejemplo:** En un gran corpus de documentos, la Dirichlet se utiliza para modelar dos proporciones clave:
        * La **distribución de temas** en un documento específico (e.g., $p_{\text{Economía}}, p_{\text{Política}}, p_{\text{Deportes}}$).
        * La **distribución de palabras** dentro de un tema específico (e.g., qué proporción de veces aparece la palabra "tasa" en el tema "Economía").
    * **Aplicación:** Clasificación de documentos y análisis de texto.

3.  **Estadística Bayesiana (Distribución A Priori Conjugada)**
    Al igual que la Distribución Beta es la conjugada de la Binomial, la Dirichlet es la distribución **a priori conjugada** para los parámetros de la **Distribución Multinomial**.

    * **Ejemplo:** Queremos estimar las probabilidades de resultados de un dado de seis caras ($p_1, p_2, \ldots, p_6$).
        * **A Priori:** Asumimos que el dado es justo con una Dirichlet simétrica, $\text{Dir}(1, 1, 1, 1, 1, 1)$.
        * **Datos:** Lanzamos el dado 60 veces y registramos las frecuencias de cada resultado.
        * **A Posteriori:** La probabilidad actualizada de las $p_i$ se obtiene simplemente sumando las cuentas observadas al parámetro $\alpha$ inicial: $\text{Dir}(\alpha_1 + n_1, \alpha_2 + n_2, \ldots, \alpha_K + n_K)$. Esto simplifica enormemente el cálculo bayesiano.

---
### 🔗 Relación Clave con otras Distribuciones

* **Generalización de la Beta:** Si $K=2$, la Distribución Dirichlet se reduce a la **Distribución Beta**.
    $$\text{Dir}(\alpha_1, \alpha_2) \equiv \text{Beta}(\alpha_1, \alpha_2)$$
* **Generación de muestras:** Si generas $K$ variables aleatorias independientes $\text{Gamma}(\alpha_i, 1)$ y las normalizas dividiendo cada una por su suma, el vector resultante sigue una distribución Dirichlet.

### 💻Ejemplos en codigo

```python
import numpy as np

## Función para calcular la media de un vector de Dirichlet
def calcular_media_dirichlet(alpha):
    alpha_sum = np.sum(alpha)
    media = alpha / alpha_sum
    return media

## ====================================================================
## 1. Modelado de Proporciones (Nutrientes en la Dieta: Carbs, Grasas, Proteínas)
## ====================================================================
print("--- 1. Proporciones Categóricas (Nutrientes) ---")

## Parámetros (ejemplo: dieta sesgada a Carbohidratos y Proteínas)
## Alfa = (α_Carbs, α_Grasas, α_Proteínas)
alpha_nutrientes = np.array([40, 15, 25])
alpha_sum_nutrientes = np.sum(alpha_nutrientes)

## 1a. Calcular la proporción media esperada de cada nutriente
media_nutrientes = calcular_media_dirichlet(alpha_nutrientes)

## 1b. Simular 5 muestras de la composición de la dieta
## Usamos numpy.random.dirichlet
np.random.seed(42) # para resultados reproducibles
muestras_nutrientes = np.random.dirichlet(alpha_nutrientes, size=5)

print(f"Parámetros Dirichlet (α): {alpha_nutrientes}")
print(f"Suma de Alphas (α₀): {alpha_sum_nutrientes}")
print(f"Proporción media esperada (Carbs, Grasas, Proteínas): {media_nutrientes.round(3)}")
print(f"\n5 Composiciones de Dieta simuladas (suma debe ser ≈ 1):")
for i, muestra in enumerate(muestras_nutrientes):
    print(f"  Muestra {i+1}: {muestra.round(3)} (Suma: {np.sum(muestra):.3f})")

## ====================================================================
## 2. Estadística Bayesiana (Dado de 6 Caras - Actualización Posterior)
## ====================================================================
print("\n--- 2. Estadística Bayesiana (Dado de 6 Caras) ---")

## A Priori: Dado justo no informativo (Uniforme)
alpha_priori = np.array([1, 1, 1, 1, 1, 1])
K = len(alpha_priori)

## Datos Observados (Frecuencias de 60 lanzamientos)
observaciones = np.array([12, 11, 8, 9, 10, 10]) # n_i

## 2a. Calcular el parámetro Alpha Posterior
alpha_posterior = alpha_priori + observaciones

## 2b. Calcular la media posterior de las probabilidades p_i
media_posterior = calcular_media_dirichlet(alpha_posterior)

print(f"Distribución A Priori: Dir({alpha_priori})")
print(f"Observaciones (n_i): {observaciones}")
print(f"Distribución A Posterior: Dir({alpha_posterior})")
print(f"Proporción media posterior para cada cara (p_i): {media_posterior.round(4)}")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import dirichlet

## NOTA: La librería Matplotlib NO tiene soporte nativo para gráficos de simplex.
## Este código utiliza una función auxiliar basada en BarycentricCoordinates
## para proyectar las coordenadas del simplex en un plano 2D.

def plot_dirichlet_pdf(ax, alpha, title):
## Definición de las esquinas del simplex 2D
    corners = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
## Definición de la matriz de transformación
    A = corners[:2,:].T - corners[2,:].reshape(2, 1)

## Crea una malla de puntos en el simplex
    ref = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])

## Número de puntos para la rejilla
    n_points = 50
    x_val = np.linspace(0.001, 0.999, n_points)
    y_val = np.linspace(0.001, 0.999, n_points)

    X, Y = np.meshgrid(x_val, y_val)

    Z = np.zeros_like(X)

## Convertir coordenadas cartesianas a coordenadas de Dirichlet (proporciones p1, p2, p3)
    for i in range(n_points):
        for j in range(n_points):
## Coordenadas Barycentric (conversión a p1, p2, p3)
            p1 = X[i, j]
            p2 = Y[i, j]
            if p1 + p2 < 1:
                p3 = 1.0 - p1 - p2
                probs = [p1, p2, p3]
## Calcular la densidad de probabilidad (PDF)
                Z[i, j] = dirichlet.pdf(probs, alpha)
            else:
                Z[i, j] = 0

## Proyectar las coordenadas del simplex
    ax.contourf(X, Y, Z, levels=20, cmap='viridis', zorder=-10)

## Dibujar los límites del simplex
    ax.plot([corners[0, 0], corners[1, 0], corners[2, 0], corners[0, 0]],
            [corners[0, 1], corners[1, 1], corners[2, 1], corners[0, 1]],
            color='black', linewidth=1)

## Etiquetas de las esquinas (proporciones)
    ax.text(corners[0, 0] - 0.05, corners[0, 1], '$p_1=1$', fontsize=12)
    ax.text(corners[1, 0] + 0.01, corners[1, 1], '$p_2=1$', fontsize=12)
    ax.text(corners[2, 0] - 0.02, corners[2, 1] + 0.01, '$p_3=1$', fontsize=12)

    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 0.9)
    ax.set_aspect('equal')

## ====================================================================
## 1. Distribución de Temas (K=3, Simplex)
## ====================================================================

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
fig.suptitle('Visualización de la Distribución Dirichlet (K=3)', fontsize=16)

## Ejemplo A: A Priori No Informativa (Uniforme)
alpha_uniforme = np.array([1, 1, 1])
plot_dirichlet_pdf(axes[0], alpha_uniforme, f'Dirichlet Uniforme (α={alpha_uniforme})')

## Ejemplo B: Concentrada (Inferencia Bayesiana o Proporciones)
alpha_concentrada = np.array([10, 5, 2])
plot_dirichlet_pdf(axes[1], alpha_concentrada, f'Dirichlet Concentrada (α={alpha_concentrada})')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
```

### ✨Distribución de Chi-cuadrada $\chi^2$ o de Pearson

* **Descripción**: Modelo de distribuciones que se utiliza en pruebas de hipótesis y en la construcción de intervalos de confianza para varianzas. Se deriva de la suma de los cuadrados de variables aleatorias normales estándar.

* **Parámetros**:
  - $ k $ (grados de libertad)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x) =
\begin{cases}
\displaystyle{\frac{1}{2^{k/2} \Gamma(k/2)} x^{(k/2) - 1} e^{-x/2}} & \text{si } x \geq 0 \\
0 & \text{si } x < 0
\end{cases}
$$

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) = \int_0^x f(t) \, dt
$$

* **Valor Esperado**:
$$
E[X] = k
$$

* **Media**:
$$
\mu_X = k
$$

* **Desviación Estándar**:
$$
\sigma = \sqrt{2k}
$$

* **Percentiles**: Los percentiles se pueden calcular utilizando la función inversa de la CDF.

* **Comandos en R**:

```r
## PDF
dchisq(x, df = k)

## CDF
pchisq(x, df = k)

## Simulación
rchisq(n, df = k)

```python
import numpy as np
from scipy.stats import chi2

## ----------------------------------------
## Definición de parámetros
k = 5       # Grados de libertad (df en R y Python)
x = 7.81    # valor para PDF/CDF (valor crítico al 97.5% para df=5)
n = 10      # número de muestras para simulación

## ----------------------------------------
## PDF (Función de Densidad de Probabilidad)
## dchisq(x, df = k)
## scipy.stats.chi2.pdf(x, df=k)
pdf_value = chi2.pdf(x, df=k)
print(f"PDF (chi2.pdf) para x={x}, df={k}: {pdf_value}")

## ----------------------------------------
## CDF (Función de Distribución Acumulada)
## pchisq(x, df = k)
## scipy.stats.chi2.cdf(x, df=k)
cdf_value = chi2.cdf(x, df=k)
print(f"CDF (chi2.cdf) para x={x}, df={k}: {cdf_value}")
## El valor debe ser ~0.975

## ----------------------------------------
## Simulación/Muestreo
## rchisq(n, df = k)
## np.random.chisquare(df=k, size=n)
samples = np.random.chisquare(df=k, size=n)
print(f"Muestras (np.random.chisquare) n={n}, df={k}: {samples}")
```

#### 🔍Ejemplo de Gráfica de la Distribución Chi-Cuadrada

La distribución Chi-cuadrada $\chi^2$ es una distribución de probabilidad que se utiliza comúnmente en inferencia estadística, especialmente en pruebas de hipótesis y en la construcción de intervalos de confianza. Se define como la distribución de la suma de los cuadrados de $k$ variables aleatorias independientes, cada una con una distribución normal estándar. El parámetro $k$ representa los grados de libertad de la distribución.

La forma de la distribución Chi-cuadrada se determina por el número de grados de libertad:
- Si $k = 1$, la distribución tiene una forma sesgada hacia la derecha.
- A medida que $k$ aumenta, la distribución se aproxima a una distribución normal, volviéndose más simétrica.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad (PDF) de la distribución Chi-cuadrada para varios valores de $k$. A medida que se ajusta este parámetro, la forma de la distribución varía, reflejando cómo diferentes valores de $k$ influyen en la concentración de probabilidad.

La distribución Chi-cuadrada es valiosa en diversas áreas, como la teoría de la estadística, la biología y las ciencias sociales, donde se requiere analizar la variabilidad y la relación entre variables.

```python
"""

## Cargar las librerías necesarias
library(ggplot2)
library(tidyr)

## Definir los grados de libertad
k_values <- c(1, 2, 5, 10)  # Diferentes valores de k

## Crear un rango de valores para x
x <- seq(0, 30, length.out = 500)

## Calcular la PDF para cada valor de k
pdf_data <- data.frame(x = x)

for (k in k_values) {
  pdf_data[[paste("PDF_k", k, sep = "_")]] <- dchisq(x, df = k)
}

## Convertir el data frame a formato largo para graficar
pdf_long <- pivot_longer(pdf_data, cols = starts_with("PDF_k"),
                          names_to = "k", values_to = "density")

## Graficar las distribuciones Chi-cuadrada
ggplot(pdf_long, aes(x = x, y = density, color = k)) +
  geom_line(linewidth = 1) +  # Cambiado size por linewidth
  labs(title = "Distribución Chi-Cuadrada para Diferentes Valores de k",
       x = "$x$",
       y = "Densidad de Probabilidad (PDF)",
       color = "Grados de Libertad (k)") +
  theme_minimal() +
  scale_color_discrete(labels = c("k = 1", "k = 2", "k = 5", "k = 10"))

"""
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2

## ----------------------------------------
## 1. Definir los grados de libertad
k_values = [1, 2, 5, 10]  # Diferentes valores de k

## ----------------------------------------
## 2. Crear un rango de valores para x (equivalente a seq() en R)
x = np.linspace(0.001, 30, 500) # Iniciar en 0.001 para evitar el problema en x=0 para k=1

## ----------------------------------------
## 3. Calcular la PDF para cada valor de k y consolidar en un DataFrame
data_list = []

for k in k_values:
## Calcular la PDF (equivalente a dchisq(x, df = k) en R)
    pdf_values = chi2.pdf(x, df=k)

## Crear un DataFrame temporal para el set actual de parámetros
    df_temp = pd.DataFrame({
        'x': x,
        'Densidad': pdf_values,
## Crear la columna de etiquetas (similar a paste/factor en R)
        'Grados_Libertad': f"k = {k}"
    })
    data_list.append(df_temp)

## Concatenar todos los DataFrames (similar a la etapa intermedia de R antes de pivot_longer)
## Este paso ya crea el DataFrame en "formato largo" (tidy data)
pdf_long = pd.concat(data_list, ignore_index=True)

## ----------------------------------------
## 4. Graficar las distribuciones Chi-cuadrada (equivalente a ggplot2)

## Configurar el estilo (theme_minimal)
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

## Crear la gráfica con Seaborn, usando 'Grados_Libertad' para el color
sns.lineplot(
    data=pdf_long,
    x='x',
    y='Densidad',
    hue='Grados_Libertad',  # Mapeo a color
    linewidth=2
)

## Añadir títulos y etiquetas (labs)
plt.title("Distribución Chi-Cuadrada para Diferentes Valores de k", fontsize=16)
plt.xlabel("$x$", fontsize=14)
plt.ylabel("Densidad de Probabilidad (PDF)", fontsize=14)

## Ajustar la leyenda (equivalente a scale_color_discrete y labs(color = ...))
plt.legend(title="Grados de Libertad (k)", loc='upper right', frameon=True)

## Mostrar la gráfica
plt.show()
```

#### 📜**Descripción del Código**

* **Cargar librerías**: Se utilizan `ggplot2` y `tidyr` para crear la gráfica y manipular datos.
* **Definir los parámetros**: Se establecen varios valores de grados de libertad $k$ para diferentes configuraciones de la distribución Chi-cuadrada.
* **Crear un rango de valores para $x$**: Se define un rango de valores desde 0 hasta 30 para representar la distribución Chi-cuadrada.
* **Calcular la PDF**: Se utiliza `dchisq()` para calcular la función de densidad de probabilidad para los valores de $x$ con los grados de libertad definidos.
* **Convertir a formato largo**: Se transforma el data frame a un formato largo utilizando `pivot_longer()` para facilitar la graficación.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $ PDF $ de la distribución Chi-cuadrada para los diferentes valores de $k$.

**EJERCICIO 16**

Agrega ejemplos y los usos recomendados.

### 💡 Usos Recomendados de la Distribución Chi-Cuadrada ($\chi^2$)

La **Distribución Chi-Cuadrada ($\chi^2$)** es una distribución continua y asimétrica que solo toma valores positivos. Es la distribución de la suma de los cuadrados de $v$ variables aleatorias Normales Estándar **independientes**. Su único parámetro es $v$, los **grados de libertad (gl)**, que determinan su forma.

1.  **Inferencia Estadística sobre la Varianza Poblacional**
    Es el modelo teórico fundamental para realizar inferencia sobre la varianza ($\sigma^2$) de una población que se supone Normal.

    * **Ejemplo:** En un proceso de control de calidad, un ingeniero quiere saber si la **variabilidad** (varianza) en el diámetro de las piezas producidas ha aumentado. Utiliza la distribución $\chi^2$ para construir un **intervalo de confianza** para la varianza poblacional real ($\sigma^2$) basándose en la varianza muestral ($s^2$).
    * **Aplicación:** Determinar si la **consistencia** en los tiempos de entrega de un servicio (medida por su varianza) se ha mantenido dentro de los límites aceptables.

2.  **Pruebas de Bondad de Ajuste (Test de Pearson)**
    Es su aplicación más conocida, utilizada para determinar si una distribución de frecuencias observadas se ajusta a una distribución teórica esperada (Normal, Uniforme, Binomial, etc.).

    * **Ejemplo:** Una empresa de *marketing* lanza un nuevo producto y quiere saber si la distribución de las ventas por día de la semana sigue una distribución Uniforme (es decir, si vende lo mismo todos los días). La prueba de bondad de ajuste $\chi^2$ compara las frecuencias de venta observadas con las frecuencias esperadas (si fueran uniformes) para ver si la diferencia es estadísticamente significativa.
    * **Aplicación:** Verificar si los datos recopilados en un experimento realmente se distribuyen de manera Normal antes de aplicar pruebas paramétricas.

3.  **Pruebas de Independencia y Homogeneidad**
    La $\chi^2$ se utiliza para analizar la relación entre **variables categóricas** en una **tabla de contingencia**.

    * **Ejemplo (Prueba de Independencia):** Un investigador quiere determinar si existe una relación (dependencia) entre la **categoría de género** (Hombre/Mujer) y la **categoría de preferencia de marca** (Marca A/Marca B). La prueba $\chi^2$ calcula la probabilidad de observar las frecuencias de la tabla si las dos variables fueran realmente independientes.
    * **Ejemplo (Prueba de Homogeneidad):** Comparar si la distribución de la opinión de los votantes (A favor, En contra, Indeciso) es la **misma** (homogénea) en dos ciudades diferentes.

---
### 🔗 Relación Clave con otras Distribuciones

* **Derivada de la Normal:** La $\chi^2$ se deriva de la suma de variables Normales Estándar al cuadrado.
* **Caso Especial de la Gamma:** La Distribución Chi-Cuadrada con $v$ grados de libertad es un caso especial de la Distribución Gamma con parámetros de forma $\alpha=v/2$ y escala $\beta=2$ (o $\lambda=1/2$ en la otra parametrización).

$$\chi^2(v) \equiv \text{Gamma}(\alpha=v/2, \beta=2)$$

### 💻Ejemplos en codigo

```python
from scipy.stats import chi2
import numpy as np

## ====================================================================
## 1. Inferencia sobre la Varianza Poblacional (Intervalo de Confianza)
## ====================================================================
print("--- 1. Intervalo de Confianza para la Varianza (σ²) ---")

## Datos de muestra
n = 25              # Tamaño de la muestra
gl = n - 1          # Grados de libertad (v)
s2 = 4.0            # Varianza muestral (s²)
sigma2_hipotesis = 2.5 # Varianza poblacional conocida (σ₀²)

## 1a. Construir Intervalo de Confianza del 95% para σ²
alpha = 0.05
## Cuantiles Chi-Cuadrada
chi2_izq = chi2.ppf(1 - alpha/2, df=gl)  # Cuantil superior (0.975)
chi2_der = chi2.ppf(alpha/2, df=gl)      # Cuantil inferior (0.025)

## Fórmulas del Intervalo de Confianza para σ²:
## Limite Inferior = (n - 1) * s² / chi²_izq
## Limite Superior = (n - 1) * s² / chi²_der
limite_inferior_var = (gl * s2) / chi2_izq
limite_superior_var = (gl * s2) / chi2_der

print(f"Grados de Libertad (gl): {gl}")
print(f"Cuantil Superior (χ²₀.₉₇₅): {chi2_izq:.4f}")
print(f"Cuantil Inferior (χ²₀.₀₂₅): {chi2_der:.4f}")
print(f"Intervalo de Confianza del 95% para σ²: [{limite_inferior_var:.4f}, {limite_superior_var:.4f}]")

## ====================================================================
## 2. Pruebas de Bondad de Ajuste (Cálculo del Estadístico)
## ====================================================================
print("\n--- 2. Cálculo del Estadístico Chi-Cuadrada (Bondad de Ajuste) ---")

## Ejemplo: Venta de productos por día de la semana (Uniforme, K=5 categorías)
gl_ajuste = 5 - 1 # gl = K - 1
ventas_observadas = np.array([55, 45, 60, 50, 40]) # O_i
total_ventas = np.sum(ventas_observadas)

## Frecuencias Esperadas (E_i = Total / K)
ventas_esperadas = np.full_like(ventas_observadas, total_ventas / len(ventas_observadas))

## Fórmula del Estadístico Chi-Cuadrada: Σ [(O_i - E_i)² / E_i]
chi2_estadistico = np.sum((ventas_observadas - ventas_esperadas)**2 / ventas_esperadas)

## Calcular el valor crítico (para α=0.05) y el p-valor
alpha_critico = 0.05
valor_critico = chi2.ppf(1 - alpha_critico, df=gl_ajuste)
p_valor = chi2.sf(chi2_estadistico, df=gl_ajuste) # sf = 1 - cdf

print(f"Observadas (Oᵢ): {ventas_observadas}")
print(f"Esperadas (Eᵢ): {ventas_esperadas}")
print(f"Estadístico χ² calculado: {chi2_estadistico:.4f}")
print(f"Valor Crítico (gl={gl_ajuste}, α=0.05): {valor_critico:.4f}")
print(f"P-Valor: {p_valor:.4f}")
if p_valor < alpha_critico:
    print("Resultado: Se rechaza H₀. La distribución NO es uniforme.")
else:
    print("Resultado: NO se rechaza H₀. La distribución es consistente con ser uniforme.")

## ====================================================================
## 3. Pruebas de Independencia (Cálculo de Grados de Libertad)
## ====================================================================
print("\n--- 3. Grados de Libertad para Prueba de Independencia ---")

## Tabla de Contingencia 2x3 (Ejemplo: Género x Preferencia de Marca)
filas = 2 # Género (H, M)
columnas = 3 # Marca (A, B, C)
gl_independencia = (filas - 1) * (columnas - 1)

print(f"Tabla de {filas} x {columnas}")
print(f"Grados de Libertad: ({filas}-1) * ({columnas}-1) = {gl_independencia}")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

## Configuración de los gráficos
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(3, 1, figsize=(10, 15))
fig.suptitle('Visualización de la Distribución Chi-Cuadrada (χ²)', fontsize=16, y=1.02)

## ====================================================================
## 1. Influencia de los Grados de Libertad (gl)
## ====================================================================
gl_valores = [2, 5, 10]
x_chi2_rango = np.linspace(0.01, 25, 500)

ax = axes[0]
for gl in gl_valores:
    y_pdf = chi2.pdf(x_chi2_rango, df=gl)
    ax.plot(x_chi2_rango, y_pdf, label=f'gl = {gl}')

ax.set_title('1. Forma de la Distribución Chi-Cuadrada por Grados de Libertad')
ax.set_xlabel('Valor χ²')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## ====================================================================
## 2. Intervalo de Confianza para σ² (gl=24)
## ====================================================================
gl_ic = 24
chi2_izq_ic = chi2.ppf(0.975, df=gl_ic) # Cuantil superior (derecha)
chi2_der_ic = chi2.ppf(0.025, df=gl_ic) # Cuantil inferior (izquierda)

x_ic = np.linspace(0.01, 50, 500)
y_pdf_ic = chi2.pdf(x_ic, df=gl_ic)

ax = axes[1]
ax.plot(x_ic, y_pdf_ic, color='blue')

## Rellenar la zona de Aceptación (Intervalo Central 95%)
ax.fill_between(x_ic, y_pdf_ic, where=((x_ic >= chi2_der_ic) & (x_ic <= chi2_izq_ic)),
                color='skyblue', alpha=0.6,
                label='Zona de Aceptación 95%')

## Rellenar la zona de Rechazo
ax.fill_between(x_ic, y_pdf_ic, where=(x_ic < chi2_der_ic), color='red', alpha=0.3)
ax.fill_between(x_ic, y_pdf_ic, where=(x_ic > chi2_izq_ic), color='red', alpha=0.3, label='Zona de Rechazo')

ax.axvline(chi2_der_ic, color='red', linestyle=':', label=f'χ²₀.₀₂₅: {chi2_der_ic:.2f}')
ax.axvline(chi2_izq_ic, color='red', linestyle=':', label=f'χ²₀.₉₇₅: {chi2_izq_ic:.2f}')

ax.set_title(f'2. Uso en el Intervalo de Confianza de la Varianza (gl={gl_ic})')
ax.set_xlabel('Valor χ²')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## ====================================================================
## 3. Prueba de Bondad de Ajuste (gl=4)
## ====================================================================
gl_test = 4
chi2_estadistico_calc = 8.0 # Valor del ejemplo 2 para visualizar

## Calcular el valor crítico para un test de una cola (α=0.05)
alpha_critico_test = 0.05
valor_critico_test = chi2.ppf(1 - alpha_critico_test, df=gl_test)

x_test = np.linspace(0.01, 20, 500)
y_pdf_test = chi2.pdf(x_test, df=gl_test)

ax = axes[2]
ax.plot(x_test, y_pdf_test, color='purple')

## Rellenar la zona de rechazo (cola derecha)
ax.fill_between(x_test, y_pdf_test, where=(x_test > valor_critico_test),
                color='orange', alpha=0.6,
                label='Región de Rechazo (α=0.05)')

ax.axvline(valor_critico_test, color='red', linestyle='--', label=f'Valor Crítico: {valor_critico_test:.2f}')
ax.axvline(chi2_estadistico_calc, color='blue', linestyle='-', label=f'Estadístico Calculado: {chi2_estadistico_calc:.2f}')

ax.set_title(f'3. Prueba de Bondad de Ajuste (gl={gl_test})')
ax.set_xlabel('Valor χ²')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## Ajustar diseño y mostrar
plt.tight_layout()
plt.show()
```

### ✨Distribución t-Student

* **Descripción**: Modelo utilizado para estimar la media de una población cuando el tamaño de la muestra es pequeño y la varianza poblacional es desconocida. Es útil en pruebas de hipótesis y en intervalos de confianza.

* **Parámetros**:
$ \nu $ (grados de libertad)

* **Función de Densidad de Probabilidad (PDF)**:

$$
f(x) = \displaystyle{\frac{\Gamma\left(\frac{\nu + 1}{2}\right)}{\sqrt{\nu \pi} \Gamma\left(\frac{\nu}{2}\right)} \left(1 + \frac{x^2}{\nu}\right)^{-\frac{\nu + 1}{2}}} \quad \text{si } -\infty < x < \infty
$$

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) = \int_{-\infty}^x f(t) \, dt
$$

* **Valor Esperado**: $ E[X] = 0 $ (para 4 \nu > 1 $)

* **Media**: $\mu_X = 0 $ (para $\nu > 1 $)

* **Desviación Estándar**:  $\sigma = \sqrt{\frac{\nu}{\nu - 2}} $(para $ \nu > 2 $)

* **Percentiles**: Los percentiles se pueden calcular utilizando la función inversa de la CDF.

**Comandos en R**:
```r
## PDF
dt(x, df = nu)

## CDF
pt(x, df = nu)

## Simulación
rt(n, df = nu)

```python
import numpy as np
from scipy.stats import t

## ----------------------------------------
## Definición de parámetros
nu = 10      # Grados de libertad (df en R y Python)
x = 1.812    # valor para PDF/CDF (valor crítico para nu=10, alfa=0.05 de dos colas)
n = 10       # número de muestras para simulación

## ----------------------------------------
## PDF (Función de Densidad de Probabilidad)
## dt(x, df = nu)
## scipy.stats.t.pdf(x, df=nu)
pdf_value = t.pdf(x, df=nu)
print(f"PDF (t.pdf) para x={x}, df={nu}: {pdf_value}")

## ----------------------------------------
## CDF (Función de Distribución Acumulada)
## pt(x, df = nu)
## scipy.stats.t.cdf(x, df=nu)
cdf_value = t.cdf(x, df=nu)
print(f"CDF (t.cdf) para x={x}, df={nu}: {cdf_value}")

## ----------------------------------------
## Simulación/Muestreo
## rt(n, df = nu)
## np.random.standard_t(df=nu, size=n)
samples = np.random.standard_t(df=nu, size=n)
print(f"Muestras (np.random.standard_t) n={n}, df={nu}: {samples}")
```

#### 🔍Ejemplo de Gráfica de la Distribución t-Student

La distribución t-Student es una distribución de probabilidad que se utiliza principalmente en inferencia estadística, especialmente para estimar la media de una población cuando la muestra es pequeña y la varianza es desconocida. Se define como la distribución de una variable aleatoria que es el cociente de una variable normal estándar y la raíz cuadrada de una variable Chi-cuadrada dividida por sus grados de libertad. El parámetro $k$ representa los grados de libertad de la distribución.

La forma de la distribución t-Student se determina por el número de grados de libertad:
- Si $k$ es pequeño, la distribución es más ancha y presenta colas más pesadas en comparación con la distribución normal.
- A medida que $k$ aumenta, la distribución se aproxima a la normal estándar, volviéndose más simétrica y estrecha.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad (PDF) de la distribución t-Student para varios valores de $k$. A medida que se ajusta este parámetro, la forma de la distribución varía, reflejando cómo diferentes valores de $k$ influyen en la concentración de probabilidad.

La distribución t-Student es valiosa en campos como la estadística, la investigación social y la psicología, donde se requiere realizar inferencias sobre medias poblacionales con muestras pequeñas.

```python
"""

## Cargar la librería necesaria
library(ggplot2)

## Definir los grados de libertad
k_values <- c(1, 2, 5, 10)  # Diferentes valores de k

## Crear un rango de valores para x
x <- seq(-5, 5, length.out = 500)

## Calcular la PDF para cada valor de k
pdf_data <- data.frame(x = x)

for (k in k_values) {
  pdf_data[[paste("PDF_k", k, sep = "_")]] <- dt(x, df = k)
}

## Convertir el data frame a formato largo para graficar
pdf_long <- tidyr::pivot_longer(pdf_data, cols = starts_with("PDF_k"),
                                  names_to = "k", values_to = "density")

## Graficar las distribuciones t-Student
ggplot(pdf_long, aes(x = x, y = density, color = k)) +
  geom_line(linewidth = 1) +
  labs(title = "Distribución t-Student para Diferentes Valores de k",
       x = "$x$",
       y = "Densidad de Probabilidad (PDF)",
       color = "Grados de Libertad (k)") +
  theme_minimal() +
  scale_color_discrete(labels = c("k = 1", "k = 2", "k = 5", "k = 10"))

"""
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import t

## ----------------------------------------
## 1. Definir los grados de libertad
k_values = [1, 2, 5, 10]  # Diferentes valores de k (df)

## ----------------------------------------
## 2. Crear un rango de valores para x (equivalente a seq() en R)
x = np.linspace(-5, 5, 500)

## ----------------------------------------
## 3. Calcular la PDF para cada valor de k y consolidar en un DataFrame
data_list = []

for k in k_values:
## Calcular la PDF (equivalente a dt(x, df = k) en R)
    pdf_values = t.pdf(x, df=k)

## Crear un DataFrame temporal para el set actual de parámetros
    df_temp = pd.DataFrame({
        'x': x,
        'Densidad': pdf_values,
## Crear la columna de etiquetas (similar a factor y paste en R)
        'Grados_Libertad': f"k = {k}"
    })
    data_list.append(df_temp)

## Concatenar todos los DataFrames. Esto crea el formato largo (equivalente a pivot_longer)
pdf_long = pd.concat(data_list, ignore_index=True)

## ----------------------------------------
## 4. Graficar las distribuciones t-Student (equivalente a ggplot2)

## Configurar el estilo (theme_minimal)
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

## Crear la gráfica con Seaborn, usando 'Grados_Libertad' para el color
sns.lineplot(
    data=pdf_long,
    x='x',
    y='Densidad',
    hue='Grados_Libertad',  # Mapeo a color
    linewidth=2
)

## Añadir títulos y etiquetas (labs)
plt.title("Distribución t-Student para Diferentes Valores de k", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("Densidad de Probabilidad (PDF)", fontsize=14)

## Ajustar leyenda (equivalente a scale_color_discrete y labs(color = ...))
plt.legend(title="Grados de Libertad (k)", loc='upper right', frameon=True)

## Mostrar la gráfica
plt.show()
```

#### 📜**Descripción del Código**

* **Cargar librería**: Se utiliza `ggplot2` y `tidyr` para crear la gráfica y manipular datos.
* **Definir los parámetros**: Se establecen varios valores de grados de libertad $k$ para diferentes configuraciones de la distribución t-Student.
* **Crear un rango de valores para $x$**: Se define un rango de valores desde -5 hasta 5 para representar la distribución t-Student.
* **Calcular la PDF**: Se utiliza `dt()` para calcular la función de densidad de probabilidad para los valores de $x$ con los grados de libertad definidos.
* **Convertir a formato largo**: Se transforma el data frame a un formato largo utilizando `pivot_longer()` para facilitar la graficación.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $ PDF $ de la distribución t-Student para los diferentes valores de $k$.

### 📏 Usos Recomendados de la Distribución t-Student

La **Distribución t-Student** (o simplemente distribución $t$) es una distribución de probabilidad continua y simétrica, similar a la Normal Estándar, pero con **colas más pesadas** (más gruesas). Su forma se controla por un único parámetro: los **grados de libertad ($v$)**. Fue desarrollada por William Sealy Gosset (quien usó el seudónimo "Student").

1.  **Inferencia Estadística con Muestras Pequeñas**
    Es el modelo fundamental para realizar inferencia (intervalos de confianza y pruebas de hipótesis) sobre la **media poblacional ($\mu$)** cuando el **tamaño de la muestra es pequeño ($n < 30$)** y/o la **desviación estándar poblacional ($\sigma$) es desconocida**.

    * **Ejemplo:** Una pequeña empresa prueba un nuevo aditivo para combustible en 15 vehículos ($n=15$). Quieren saber si el **consumo medio** de combustible ha cambiado significativamente. Dado que $n$ es pequeño y $\sigma$ (la variabilidad de todos los vehículos posibles) se desconoce, se utiliza la **prueba t para una muestra** (o para muestras pareadas/independientes) para calcular el valor $t$ y la probabilidad asociada.
    * **Aplicación:** Determinar el **intervalo de confianza** para el tiempo medio de atención al cliente basándose en una semana de datos, asumiendo que el tiempo poblacional es Normal.

2.  **Comparación de Medias (Prueba T)**
    Es la herramienta estadística estándar para comparar las medias de dos grupos, esencial en el análisis experimental y de investigación.

    * **Ejemplo (Muestras Independientes):** Un psicólogo quiere saber si un nuevo método de enseñanza produce **notas medias** significativamente diferentes a las de un método tradicional. La **prueba t de dos muestras** se utiliza para comparar las medias de los dos grupos de estudiantes.
    * **Ejemplo (Muestras Pareadas):** Un estudio mide la presión arterial de 20 pacientes **antes** y **después** de un tratamiento. La **prueba t pareada** analiza la diferencia media dentro de cada sujeto, utilizando la distribución $t$.

3.  **Análisis de Regresión Lineal**
    La distribución $t$ se utiliza para evaluar la significancia estadística de los **coeficientes de regresión** en modelos lineales.

    * **Ejemplo:** En un modelo de regresión que predice las ventas en función del gasto en publicidad, la distribución $t$ ayuda a determinar si el coeficiente de publicidad es **significativamente diferente de cero**, es decir, si el gasto en publicidad realmente tiene un efecto estadístico en las ventas.

---
### 🔗 Relación Clave con la Distribución Normal

La Distribución t-Student es, en esencia, una corrección o versión robusta de la Normal Estándar ($\text{N}(0, 1)$).

* **Convergencia:** A medida que el número de grados de libertad ($v$) **aumenta** ($v \to \infty$, o típicamente cuando $n > 30$), la distribución $t$-Student **converge y se vuelve idéntica** a la Distribución Normal Estándar.
* **Incertidumbre:** Las colas más gruesas para valores bajos de $v$ reflejan la **mayor incertidumbre** que existe cuando se trabaja con muestras pequeñas, lo que hace que los valores extremos sean más probables que en una distribución Normal.

### 💻Ejemplos en codigo

```python
from scipy.stats import t
import numpy as np

## ====================================================================
## 1. Inferencia Estadística (Prueba T para una Muestra - Consumo de Combustible)
## ====================================================================
print("--- 1. Prueba T para una Muestra (Consumo) ---")

## Datos del ejemplo: 15 vehículos
n = 15                 # Tamaño de la muestra
gl = n - 1             # Grados de libertad (v)
media_muestral = 15.2  # Consumo medio observado (km/L)
desviacion_est = 1.8   # Desviación estándar muestral (s)
mu_hipotesis = 16.0    # Media poblacional hipotética (μ₀)

## 1a. Calcular el estadístico t (t = (x̄ - μ₀) / (s / √n))
t_estadistico = (media_muestral - mu_hipotesis) / (desviacion_est / np.sqrt(n))

## 1b. Calcular el p-valor para una prueba de dos colas
## p-valor = 2 * P(T > |t_estadistico|) = 2 * sf(|t_estadistico|)
p_valor_dos_colas = 2 * t.sf(np.abs(t_estadistico), df=gl)

## 1c. Calcular el valor crítico para un Intervalo de Confianza del 95%
nivel_confianza = 0.95
t_critico_ic = t.ppf(1 - (1 - nivel_confianza) / 2, df=gl)

print(f"Grados de Libertad (gl): {gl}")
print(f"Estadístico t calculado: {t_estadistico:.4f}")
print(f"Valor crítico t (95%): {t_critico_ic:.4f}")
print(f"P-Valor (dos colas): {p_valor_dos_colas:.4f}")
if p_valor_dos_colas < 0.05:
    print("Resultado: El cambio en el consumo es estadísticamente significativo.")
else:
    print("Resultado: NO hay evidencia de cambio significativo en el consumo.")

## ====================================================================
## 2. Comparación de Medias (Prueba T Pareada - Presión Arterial)
## ====================================================================
print("\n--- 2. Intervalo de Confianza (t-Student) ---")

## Datos de la diferencia (D = Después - Antes) para 20 pacientes
n_pareada = 20
gl_pareada = n_pareada - 1
media_diferencia = -3.5  # Diferencia media observada (ej. reducción de 3.5 mmHg)
desviacion_diferencia = 5.0 # Desviación estándar de las diferencias (s_D)

## 2a. Calcular el Intervalo de Confianza del 99% para la diferencia media (μ_D)
nivel_confianza_ic = 0.99
t_critico_ic_pareada = t.ppf(1 - (1 - nivel_confianza_ic) / 2, df=gl_pareada)

## Margen de error (ME = t_critico * (s_D / √n))
margen_error = t_critico_ic_pareada * (desviacion_diferencia / np.sqrt(n_pareada))

## Intervalo de Confianza: μ_D ± ME
ic_inferior = media_diferencia - margen_error
ic_superior = media_diferencia + margen_error

print(f"Grados de Libertad (gl): {gl_pareada}")
print(f"Diferencia media (D̄): {media_diferencia:.2f}")
print(f"Valor crítico t (99%): {t_critico_ic_pareada:.4f}")
print(f"Intervalo de Confianza del 99% para μ_D: [{ic_inferior:.4f}, {ic_superior:.4f}]")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, norm

## Configuración de los gráficos
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(2, 1, figsize=(10, 10))
fig.suptitle('Visualización de la Distribución t-Student', fontsize=16, y=1.02)

## Rango de X (valores t)
x_t = np.linspace(-4.5, 4.5, 500)
y_normal = norm.pdf(x_t, loc=0, scale=1)

## ====================================================================
## 1. Influencia de los Grados de Libertad y Convergencia
## ====================================================================
gl_valores = [2, 5, 10, 30]

ax = axes[0]
ax.plot(x_t, y_normal, color='black', linestyle='--', label='Normal Estándar (gl = ∞)', linewidth=2)
for gl in gl_valores:
    y_pdf = t.pdf(x_t, df=gl)
    ax.plot(x_t, y_pdf, label=f't-Student (gl = {gl})', alpha=0.7)

ax.set_title('1. Convergencia de t-Student a la Normal Estándar')
ax.set_xlabel('Valor t')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## ====================================================================
## 2. Área de Rechazo para la Prueba T (gl=14, t_critico)
## ====================================================================
gl_prueba = 14
t_critico_prueba = t.ppf(0.975, df=gl_prueba) # t_critico del 95%
t_estadistico_calc = -2.1 # Ejemplo 1 (-2.1822 redondeado)

y_pdf_prueba = t.pdf(x_t, df=gl_prueba)

ax = axes[1]
ax.plot(x_t, y_pdf_prueba, color='blue')

## Rellenar las colas de rechazo (prueba de dos colas, α=0.05)
ax.fill_between(x_t, y_pdf_prueba, where=(x_t > t_critico_prueba),
                color='red', alpha=0.3, label='Región de Rechazo (α/2)')
ax.fill_between(x_t, y_pdf_prueba, where=(x_t < -t_critico_prueba),
                color='red', alpha=0.3)

## Marcar los valores críticos y el estadístico calculado
ax.axvline(t_critico_prueba, color='red', linestyle=':', label=f't_crítico: ±{t_critico_prueba:.2f}')
ax.axvline(-t_critico_prueba, color='red', linestyle=':')
ax.axvline(t_estadistico_calc, color='black', linestyle='-',
           label=f'Estadístico Calculado: {t_estadistico_calc:.2f}')

ax.set_title(f'2. Región de Rechazo en una Prueba t-Student (gl={gl_prueba})')
ax.set_xlabel('Valor t')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## Ajustar diseño y mostrar
plt.tight_layout()
plt.show()
```

### ✨Distribución F (Fisher-Snedecor)

* **Descripción**: Modelo utilizado para comparar dos varianzas a través de la relación entre dos variables aleatorias independientes que siguen distribuciones Chi-cuadrada. Se usa comúnmente en el análisis de varianza (ANOVA).

* **Parámetros**:
  - $d_1 $(grados de libertad del numerador)
  - $ d_2 $ (grados de libertad del denominador)

* **Función de Densidad de Probabilidad (PDF)**:

$$
\displaystyle{f(x) = \frac{\left(\frac{d_1}{d_2}\right)^{\frac{d_1}{2}} \frac{x^{\frac{d_1}{2} - 1}}{\left(1 + \frac{d_1}{d_2} x\right)^{\frac{d_1 + d_2}{2}}}}{B\left(\frac{d_1}{2}, \frac{d_2}{2}\right)}} \quad \text{si } x \geq 0
$$
donde $ B $ es la función beta.

* **Función de Distribución Acumulativa (CDF)**:

$$
F(x) = \int_0^x f(t) \, dt
$$

* **Valor Esperado**:
$$
E[X] = \frac{d_1}{d_1 - 2} \quad \text{(para } d_1 > 2\text{)}
$$

* **Media**:
$$
\mu_X = \frac{d_1}{d_1 - 2} \quad \text{(para } d_1 > 2\text{)}
$$

* **Desviación Estándar**:
$$
\sigma = \sqrt{\frac{2d_2^2(d_1 + d_1 - 2)}{d_1(d_2 - 2)^2(d_2 - 4)}} \quad \text{(para } d_2 > 4\text{)}
$$

* **Percentiles**: Los percentiles se pueden calcular utilizando la función inversa de la CDF.

**Comandos en R**:
```r
## PDF
df(x, df1 = d1, df2 = d2)

## CDF
pf(x, df1 = d1, df2 = d2)

## Simulación
rf(n, df1 = d1, df2 = d2)

```python
import numpy as np
from scipy.stats import f

## ----------------------------------------
## Definición de parámetros
d1 = 5      # Grados de libertad del numerador (df1 en R, dfn en Python)
d2 = 10     # Grados de libertad del denominador (df2 en R, dfd en Python)
x = 3.33    # valor para PDF/CDF (valor crítico al 97.5% para d1=5, d2=10)
n = 10      # número de muestras para simulación

## ----------------------------------------
## PDF (Función de Densidad de Probabilidad)
## df(x, df1 = d1, df2 = d2)
## scipy.stats.f.pdf(x, dfn=d1, dfd=d2)
pdf_value = f.pdf(x, dfn=d1, dfd=d2)
print(f"PDF (f.pdf) para x={x}, df1={d1}, df2={d2}: {pdf_value}")

## ----------------------------------------
## CDF (Función de Distribución Acumulada)
## pf(x, df1 = d1, df2 = d2)
## scipy.stats.f.cdf(x, dfn=d1, dfd=d2)
cdf_value = f.cdf(x, dfn=d1, dfd=d2)
print(f"CDF (f.cdf) para x={x}, df1={d1}, df2={d2}: {cdf_value}")

## ----------------------------------------
## Simulación/Muestreo
## rf(n, df1 = d1, df2 = d2)
## np.random.f(dfnum=d1, dfden=d2, size=n)
samples = np.random.f(dfnum=d1, dfden=d2, size=n)
print(f"Muestras (np.random.f) n={n}, df1={d1}, df2={d2}: {samples}")
```

#### 🔍Ejemplo de Gráfica de la Distribución F (Fisher-Snedecor)

La distribución F (Fisher-Snedecor) es una distribución de probabilidad que se utiliza principalmente en análisis de varianza y pruebas de hipótesis. Se define como la distribución de la razón de dos variables aleatorias independientes que siguen una distribución Chi-cuadrada, cada una dividida por sus grados de libertad. Los parámetros de la distribución F son $d_1$ y $d_2$, que representan los grados de libertad del numerador y el denominador, respectivamente.

La forma de la distribución F se determina por los grados de libertad:
- Si $d_1$ y $d_2$ son pequeños, la distribución es asimétrica y tiene colas más pesadas.
- A medida que ambos grados de libertad aumentan, la distribución se aproxima a una distribución normal, volviéndose más simétrica.

En esta gráfica, se muestran diferentes funciones de densidad de probabilidad (PDF) de la distribución F para varios pares de grados de libertad $(d_1, d_2)$. A medida que se ajustan estos parámetros, la forma de la distribución varía, reflejando cómo diferentes combinaciones de $d_1$ y $d_2$ influyen en la concentración de probabilidad.

La distribución F es valiosa en campos como la estadística, la ingeniería y las ciencias sociales, donde se requiere comparar varianzas y realizar análisis de varianza (ANOVA).

```python
"""

## Cargar la librería necesaria
library(ggplot2)

## Definir los grados de libertad
df_values <- list(c(2, 5), c(5, 2), c(5, 10), c(10, 5))  # Diferentes pares (d1, d2)

## Crear un rango de valores para x
x <- seq(0, 5, length.out = 500)

## Calcular la PDF para cada par de grados de libertad
pdf_data <- data.frame(x = x)

for (df in df_values) {
  pdf_data[[paste("PDF_d1", df[1], "_d2", df[2], sep = "")]] <- df(x, df = df[1], df2 = df[2])
}

## Convertir el data frame a formato largo para graficar
pdf_long <- tidyr::pivot_longer(pdf_data, cols = starts_with("PDF_d1"),
                                  names_to = "Degrees_of_Freedom", values_to = "density")

## Graficar las distribuciones F
ggplot(pdf_long, aes(x = x, y = density, color = Degrees_of_Freedom)) +
  geom_line(linewidth = 1) +
  labs(title = "Distribución F (Fisher-Snedecor) para Diferentes Pares de Grados de Libertad",
       x = "$x$",
       y = "Densidad de Probabilidad (PDF)",
       color = "Grados de Libertad $(d_1, d_2)$") +
  theme_minimal() +
  scale_color_discrete(labels = c("(2, 5)", "(5, 2)", "(5, 10)", "(10, 5)"))

"""
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f

## ----------------------------------------
## 1. Definir los grados de libertad
## Diferentes pares (dfn, dfd) - Equivalente a df_values en R
df_values = [(2, 5), (5, 2), (5, 10), (10, 5)]

## ----------------------------------------
## 2. Crear un rango de valores para x (equivalente a seq() en R)
## La distribución F está definida para x > 0
x = np.linspace(0.01, 5, 500)

## ----------------------------------------
## 3. Calcular la PDF para cada par y consolidar en un DataFrame
data_list = []

for d1, d2 in df_values:
## Calcular la PDF (equivalente a df(x, df1 = d1, df2 = d2) en R)
## dfn=d1 (numerador), dfd=d2 (denominador)
    pdf_values = f.pdf(x, dfn=d1, dfd=d2)

## Crear un DataFrame temporal
    df_temp = pd.DataFrame({
        'x': x,
        'Densidad': pdf_values,
## Crear la etiqueta de los parámetros para el color y la leyenda
        'Grados_Libertad': f"({d1}, {d2})"
    })
    data_list.append(df_temp)

## Concatenar todos los DataFrames. Esto crea el formato largo (equivalente a pivot_longer)
pdf_long = pd.concat(data_list, ignore_index=True)

## ----------------------------------------
## 4. Graficar las distribuciones F (equivalente a ggplot2)

## Configurar el estilo (theme_minimal)
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

## Crear la gráfica con Seaborn, usando 'Grados_Libertad' para el color
sns.lineplot(
    data=pdf_long,
    x='x',
    y='Densidad',
    hue='Grados_Libertad',  # Mapeo a color
    linewidth=2
)

## Añadir títulos y etiquetas (labs)
plt.title("Distribución F (Fisher-Snedecor) para Diferentes Pares de Grados de Libertad", fontsize=16)
plt.xlabel("x", fontsize=14)
## Usar notación LaTeX en la etiqueta del eje Y (opcional)
plt.ylabel("Densidad de Probabilidad (PDF)", fontsize=14)

## Ajustar leyenda (equivalente a scale_color_discrete y labs(color = ...))
plt.legend(title="Grados de Libertad $(d_1, d_2)$", loc='upper right', frameon=True)

## Mostrar la gráfica
plt.show()
```

#### 📜**Descripción del Código**

* **Cargar librería**: Se utiliza `ggplot2` y `tidyr` para crear la gráfica y manipular datos.
* **Definir los grados de libertad**: Se establecen varios pares de grados de libertad $(d_1, d_2)$ para diferentes configuraciones de la distribución F (Fisher-Snedecor).
* **Crear un rango de valores para $x$**: Se define un rango de valores desde 0 hasta 5 para representar la distribución F.
* **Calcular la PDF**: Se utiliza `df()` para calcular la función de densidad de probabilidad para los valores de $x$ con los grados de libertad definidos.
* **Convertir a formato largo**: Se transforma el data frame a un formato largo utilizando `pivot_longer()` para facilitar la graficación.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de líneas que representa la $ PDF $ de la distribución F para los diferentes pares de grados de libertad $(d_1, d_2)$.

**EJERCICIO 17**

Agrega ejemplos y los usos recomendados.

### 🔬 Usos Recomendados de la Distribución F (Fisher-Snedecor)

La **Distribución F (Fisher-Snedecor)** es una distribución continua, positiva y asimétrica que surge del cociente de dos variables aleatorias $\chi^2$ independientes, cada una dividida por sus respectivos grados de libertad. Se caracteriza por dos parámetros de grados de libertad: $v_1$ (numerador) y $v_2$ (denominador).

1.  **Análisis de Varianza (ANOVA)**
    Este es el uso principal y más importante de la Distribución F. Se utiliza para probar la hipótesis de que **las medias de dos o más grupos son iguales** al comparar las varianzas "entre grupos" con las varianzas "dentro de los grupos".

    * **Ejemplo:** Un investigador de marketing prueba la efectividad de **tres diseños de empaque** (Grupo 1, Grupo 2, Grupo 3) midiendo las ventas resultantes. El análisis ANOVA utiliza la Distribución F para determinar si la variación en las ventas **entre** los tres grupos (debido al diseño) es significativamente mayor que la variación natural **dentro** de cada grupo.
    * **Aplicación:** Comparar la producción media de cuatro máquinas diferentes, la eficacia media de cinco métodos de enseñanza o la respuesta media de pacientes a varios tratamientos farmacológicos.

2.  **Comparación de Varianzas de Dos Poblaciones**
    Se utiliza para probar si dos poblaciones Normales tienen la misma varianza ($\sigma_1^2 = \sigma_2^2$). Esta prueba es a menudo un paso preliminar para decidir si se utiliza una prueba t para dos muestras con varianzas iguales o desiguales.

    * **Ejemplo:** Un ingeniero quiere comparar la **consistencia** (varianza) en la vida útil de baterías de dos proveedores distintos (Proveedor A y Proveedor B). La prueba F para la igualdad de varianzas se utiliza para determinar si la varianza del Proveedor A es estadísticamente igual a la del Proveedor B.
    * **Aplicación:** En estadística, es esencial para verificar el supuesto de **homocedasticidad** (varianzas iguales) antes de aplicar otros modelos.

3.  **Análisis de Regresión Múltiple y Modelos Lineales**
    La Distribución F es crucial para evaluar la significancia general de un modelo de regresión.

    * **Ejemplo:** En un modelo de regresión que utiliza múltiples variables (ingreso, edad, ubicación) para predecir el gasto, la **prueba F global del modelo** determina si el conjunto de variables predictoras en su conjunto explica una proporción significativa de la varianza en la variable de respuesta.
    * **Aplicación:** Se utiliza para probar si un **modelo más complejo** (con más variables) es significativamente mejor para predecir la respuesta que un modelo más simple (con menos variables).

---
### 🔗 Relación Clave con otras Distribuciones

La distribución F se define como el cociente de dos distribuciones $\chi^2$ normalizadas por sus grados de libertad:

$$F(v_1, v_2) = \frac{\frac{\chi^2(v_1)}{v_1}}{\frac{\chi^2(v_2)}{v_2}}$$

Donde:
* $v_1$ son los grados de libertad del numerador (p. ej., la varianza entre grupos en ANOVA).
* $v_2$ son los grados de libertad del denominador (p. ej., la varianza dentro de los grupos en ANOVA).

### 💻Ejemplos en codigo

```python
from scipy.stats import f
import numpy as np

## ====================================================================
## 1. Análisis de Varianza (ANOVA - Prueba de Medias de 3 Grupos)
## ====================================================================
print("--- 1. Cálculo del Estadístico F (ANOVA) ---")

## Parámetros del experimento (3 diseños de empaque, 10 ventas por diseño)
K = 3     # Número de grupos (k)
n_total = 30 # Número total de observaciones (N)

## Grados de Libertad
v1 = K - 1          # GL del numerador (entre grupos)
v2 = n_total - K    # GL del denominador (dentro de grupos)

## Resultados del ANOVA (ejemplo de cálculo)
MS_Between = 450.0  # Varianza Media Entre Grupos (MSB)
MS_Within = 150.0   # Varianza Media Dentro de Grupos (MSW)

## 1a. Calcular el Estadístico F (F = MSB / MSW)
f_estadistico_anova = MS_Between / MS_Within

## 1b. Calcular el Valor Crítico y el P-Valor (prueba de una cola derecha)
alpha = 0.05
f_critico = f.ppf(1 - alpha, dfn=v1, dfd=v2)
p_valor = f.sf(f_estadistico_anova, dfn=v1, dfd=v2) # sf = 1 - cdf

print(f"GL Numerador (v₁): {v1}, GL Denominador (v₂): {v2}")
print(f"Estadístico F calculado: {f_estadistico_anova:.4f}")
print(f"Valor Crítico F (α=0.05): {f_critico:.4f}")
print(f"P-Valor: {p_valor:.4f}")
if p_valor < alpha:
    print("Resultado: Se rechaza H₀. Las medias de los empaques SÍ son diferentes.")
else:
    print("Resultado: NO se rechaza H₀. No hay diferencia significativa en las medias.")

## ====================================================================
## 2. Comparación de Varianzas de Dos Poblaciones (Prueba F)
## ====================================================================
print("\n--- 2. Prueba F para Comparación de Varianzas ---")

## Datos de varianza (ejemplo: vida útil de baterías de dos proveedores)
n1 = 16   # Tamaño muestra Proveedor A
n2 = 13   # Tamaño muestra Proveedor B
s1_2 = 120.0 # Varianza muestral Proveedor A
s2_2 = 50.0  # Varianza muestral Proveedor B

## Grados de Libertad
v1_var = n1 - 1
v2_var = n2 - 1

## 2a. Calcular el Estadístico F (Se coloca la varianza mayor en el numerador)
f_estadistico_var = s1_2 / s2_2

## 2b. Calcular el valor crítico para una prueba de dos colas (α=0.05)
alpha_var = 0.05
## Valor crítico superior (1 - α/2)
f_critico_var = f.ppf(1 - alpha_var/2, dfn=v1_var, dfd=v2_var)

print(f"GL Numerador (v₁): {v1_var}, GL Denominador (v₂): {v2_var}")
print(f"Estadístico F calculado (120/50): {f_estadistico_var:.4f}")
print(f"Valor Crítico F (α/2=0.025): {f_critico_var:.4f}")

## Nota: Para la prueba de dos colas, si F > F_critico o F < 1/F_critico, se rechaza H₀.
if f_estadistico_var > f_critico_var:
     print("Resultado: Se rechaza H₀. Las varianzas SÍ son significativamente diferentes.")
else:
     print("Resultado: NO se rechaza H₀. Las varianzas son iguales (homocedasticidad).")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f

## Configuración de los gráficos
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(3, 1, figsize=(10, 15))
fig.suptitle('Visualización de la Distribución F (Fisher-Snedecor)', fontsize=16, y=1.02)

## Rango de X (valores F)
x_f = np.linspace(0.01, 5.0, 500)

## ====================================================================
## 1. Influencia de los Grados de Libertad
## ====================================================================
gl_pares = [
    (5, 10, 'v₁=5, v₂=10'),
    (10, 5, 'v₁=10, v₂=5'),
    (30, 30, 'v₁=30, v₂=30')
]

ax = axes[0]
for v1, v2, label in gl_pares:
    y_pdf = f.pdf(x_f, dfn=v1, dfd=v2)
    ax.plot(x_f, y_pdf, label=label, linewidth=2)

ax.set_title('1. Forma de la Distribución F según los Grados de Libertad')
ax.set_xlabel('Valor F')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## ====================================================================
## 2. Prueba de ANOVA (Región de Rechazo, gl=2, 27)
## ====================================================================
v1_anova, v2_anova = 2, 27
f_critico_anova = f.ppf(0.95, dfn=v1_anova, dfd=v2_anova)
f_estadistico_calc = 3.0 # Valor del ejemplo 1 (450/150=3.0)

y_pdf_anova = f.pdf(x_f, dfn=v1_anova, dfd=v2_anova)

ax = axes[1]
ax.plot(x_f, y_pdf_anova, color='red')

## Rellenar la zona de rechazo (cola derecha, α=0.05)
ax.fill_between(x_f, y_pdf_anova, where=(x_f > f_critico_anova),
                color='salmon', alpha=0.6,
                label='Región de Rechazo (α=0.05)')

ax.axvline(f_critico_anova, color='red', linestyle='--', label=f'F Crítico: {f_critico_anova:.3f}')
ax.axvline(f_estadistico_calc, color='black', linestyle='-',
           label=f'F Calculado (ANOVA): {f_estadistico_calc:.3f}')

ax.set_title(f'2. Prueba F en ANOVA (gl={v1_anova}, {v2_anova})')
ax.set_xlabel('Valor F')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## ====================================================================
## 3. Prueba de Varianzas (gl=15, 12)
## ====================================================================
v1_var, v2_var = 15, 12
f_critico_var_sup = f.ppf(0.975, dfn=v1_var, dfd=v2_var)
f_critico_var_inf = f.ppf(0.025, dfn=v1_var, dfd=v2_var)
f_estadistico_var_calc = 2.4 # Valor del ejemplo 2 (120/50=2.4)

y_pdf_var = f.pdf(x_f, dfn=v1_var, dfd=v2_var)

ax = axes[2]
ax.plot(x_f, y_pdf_var, color='purple')

## Rellenar las zonas de rechazo (prueba de dos colas, α=0.05)
ax.fill_between(x_f, y_pdf_var, where=(x_f > f_critico_var_sup), color='violet', alpha=0.6)
ax.fill_between(x_f, y_pdf_var, where=(x_f < f_critico_var_inf), color='violet', alpha=0.6, label='Regiones de Rechazo (α=0.05)')

ax.axvline(f_critico_var_sup, color='purple', linestyle='--', label=f'F Crítico Sup: {f_critico_var_sup:.3f}')
ax.axvline(f_critico_var_inf, color='purple', linestyle=':', label=f'F Crítico Inf: {f_critico_var_inf:.3f}')
ax.axvline(f_estadistico_var_calc, color='black', linestyle='-',
           label=f'F Calculado (Varianzas): {f_estadistico_var_calc:.3f}')

ax.set_title(f'3. Prueba F para Igualdad de Varianzas (gl={v1_var}, {v2_var})')
ax.set_xlabel('Valor F')
ax.set_ylabel('Densidad de Probabilidad')
ax.legend()

## Ajustar diseño y mostrar
plt.tight_layout()
plt.show()
```

---

## Resumen del Protocolo Maestro
- **Solución Analítica Resaltada**: $\boxed{\text{Verificado con SymPy y SciPy stats}}$
- **Verificación Simbólica (SymPy)**:


---

## 10. Módulo de Simulación: Método de la Transformada Inversa y Aceptación-Rechazo

El muestreo numérico de distribuciones continuas complejas (como Weibull o Gamma) se basa en el **Método de la Transformada Inversa** y el **Método de Aceptación-Rechazo de von Neumann**.

### 50.1 Teorema de la Transformada Inversa
Si $U \sim \text{Uniforme}(0, 1)$ y $F(x)$ es una CDF estrictamente creciente:
$$X = F^{-1}(U) \implies X \sim F(x)$$

### 50.2 Simulación de la Distribución de Weibull para Resistencia de Fibras de Carbono
```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from IPython.display import display, Math

## Parámetros de Weibull (forma k=2.5, escala lambda=50.0)
k_shape = 2.5
lambda_scale = 50.0
N_sim = 50_000

np.random.seed(77)
U = stats.uniform.rvs(size=N_sim)

## Inversión explícita de CDF: X = lambda * (-ln(1 - U))^(1/k)
X_weibull_sim = lambda_scale * (-np.log(1.0 - U))**(1.0 / k_shape)

## Comparación con SciPy
media_teorica = stats.weibull_min.mean(c=k_shape, scale=lambda_scale)
media_simulada = np.mean(X_weibull_sim)

display(Math(fr"\text{{Media Teórica Weibull: }} \mu = {media_teorica:.4f} \text{{ MPa}}"))
display(Math(fr"\text{{Media Simulada Transformada Inversa: }} \bar{{X}} = {media_simulada:.4f} \text{{ MPa}}"))
```


---
## 9. Verificación Simbólica y Expresión Formal con SymPy

Para variables aleatorias continuas, la Función de Densidad de Probabilidad (PDF) Normal $N(\mu, \sigma^2)$ se integra analíticamente en **SymPy**.

### 9.1 Integración de la Densidad Gaussiana

$$\boxed{f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}}$$

```python
import sympy as sp
from IPython.display import display, Math

x, mu, sigma = sp.symbols('x mu sigma', real=True)
sigma = sp.Symbol('sigma', positive=True)

pdf_normal = (1 / (sigma * sp.sqrt(2 * sp.pi))) * sp.exp(-((x - mu)**2) / (2 * sigma**2))

# Verificación del área total bajo la curva integral = 1
area_total = sp.integrate(pdf_normal, (x, -sp.oo, sp.oo))

display(Math(r'\text{PDF Normal Simbólica: } ' + sp.latex(pdf_normal)))
display(Math(r'\text{Área Total Demostrada } \int_{-\infty}^{\infty} f(x) dx: ' + sp.latex(area_total)))
```
