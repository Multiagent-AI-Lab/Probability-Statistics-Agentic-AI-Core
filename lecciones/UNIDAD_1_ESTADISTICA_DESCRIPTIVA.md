# UNIDAD 1: Estadística Descriptiva y Análisis Exploratorio de Datos
> **Asignatura: Probabilidad y Estadística Inferencial**
> **UCEMICH — Ingeniería en IA y Nanotecnología**
> **Autor y Profesor: Mtro. Luis José Yudico Anaya**

---

## 1. Fundamentación Teórica y Conceptos Clave

La **Estadística Descriptiva** y el **Análisis Exploratorio de Datos (EDA)** constituyen los cimientos fundamentales para caracterizar e interpretar conjuntos de datos experimentales en ciencias e ingeniería, particularmente en el estudio de sistemas nanotecnológicos y modelos de Inteligencia Artificial.

El análisis descriptivo permite resumir la tendencia central, dispersión, simetría y forma de una distribución muestral mediante medidas numéricas y representaciones gráficas cuantitativas.

En esta unidad abordamos:
* Cálculo de estadísticas descriptivas cuantitativas (media, mediana, varianza, desviación estándar, cuantiles).
* Análisis exploratorio visual mediante diagramas de caja (boxplots), histogramas de frecuencias y estimación de densidad de kernel (KDE).
* Aplicaciones computacionales en Python utilizando las bibliotecas `scipy.stats`, `numpy`, `pandas`, `matplotlib` y `seaborn`.

### 1.1 IMPORTANDO MÓDULOS

```python
import scipy.stats as stats
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(style="whitegrid")
```

Otros estilos de `sns.set()`:

Seaborn también ofrece varios otros estilos de gráficos que puedes usar:

* `"darkgrid"`: Fondo oscuro con cuadrícula en líneas claras (ideal para gráficos con contraste alto).
* `"white"`: Fondo blanco sin cuadrícula (minimalista).
* `"ticks"`: Estilo con cuadrícula ligera y marcas de los ejes más prominentes.

### 1.2 Revisión de estadística y probabilidad.

Comenzamos con una breve revisión de la estadística, para introducir algunos de los conceptos clave y la notación que utilizamos en este y los siguientes capítulos.

La estadística se ocupa de la recopilación y el análisis de datos con el propósito de obtener información, sacar conclusiones y apoyar la toma de decisiones. Los métodos estadísticos son necesarios cuando tenemos información incompleta sobre un fenómeno. Generalmente, tenemos información incompleta porque no podemos recopilar datos de todos los miembros de una población o si existe incertidumbre en las observaciones que realizamos (por ejemplo, debido al ruido de medición). Cuando no podemos encuestar a toda una población, podemos estudiar una muestra elegida aleatoriamente, y utilizar métodos estadísticos para calcular estadísticas descriptivas (parámetros como la media $ \mu $ y las varianzas $ \sigma^2 $) con el fin de hacer inferencias sobre las propiedades de toda la población (también llamada espacio muestral) de manera sistemática y con riesgos controlados de error.

Los métodos estadísticos se construyen sobre la base proporcionada por la teoría de la probabilidad, con la cual podemos modelar la incertidumbre y la información incompleta utilizando variables aleatorias probabilísticas.

Por ejemplo, con muestras seleccionadas aleatoriamente de una población, podemos esperar obtener muestras representativas cuyas propiedades pueden ser usadas para inferir propiedades de toda la población.

En la teoría de la probabilidad, a cada posible resultado de una observación se le asigna una probabilidad, y la probabilidad de todos los resultados posibles constituye la distribución de probabilidad. Dada la distribución de probabilidad, podemos calcular las propiedades de la población, como su media $ \mu $ y su varianza $ \sigma^2 $, pero para muestras seleccionadas aleatoriamente, solo conocemos los resultados esperados o promedio.

En el análisis estadístico es importante **distinguir entre las estadísticas de población y las de muestra**. Aquí denotamos los parámetros de la población con símbolos griegos y los parámetros de una muestra con el símbolo correspondiente de la población, añadiendo el subíndice $x$ (o el símbolo que se utiliza para representar la muestra). Por ejemplo, la media y la varianza de una población se denotan como $ \mu $ y $ \sigma^2 $, mientras que la media y la varianza de una muestra $ x $ se denotan como $ \mu_x $ y $ s_x^2 $.

Además, denotamos las variables que representan una población (variables aleatorias) con letras mayúsculas, por ejemplo, $X$, y un conjunto de elementos de muestra se denota con una letra minúscula, por ejemplo, $x$. Una barra sobre un símbolo denota el promedio o la media, así que:

$$
\overline{X} = \frac{1}{N} \sum_{i=1}^N x_i
$$

y

$$
\overline{x} = \frac{1}{n} \sum_{i=1}^n x_i
$$

donde $N$ es el número de elementos en la población $X$ y $n$ es el número de elementos en la muestra $x$. La única diferencia entre estas dos expresiones es el número de elementos en la suma ($N \geq n$).

La situación es un poco más compleja para la varianza: la varianza de la población es la media de la distancia al cuadrado de la media,

$$
\sigma^2 = \frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2
$$

y la varianza de la muestra correspondiente es

$$
s_x^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \mu_x)^2
$$

En esta última expresión, hemos reemplazado la media de la población $ \mu $ por la media de la muestra $ \mu_x $ y dividido la suma por $n - 1$ en lugar de $n$. La razón de esto es que se ha eliminado un grado de libertad del conjunto de la muestra al calcular la media de la muestra $ \mu_x $, por lo que, al calcular la varianza de la muestra, solo quedan $n - 1$ grados de libertad. En consecuencia, la forma de calcular la varianza para una población y para una muestra es ligeramente diferente. Esto se refleja en las funciones que podemos utilizar para calcular estas estadísticas en Python.

Podemos calcular estadísticas descriptivas para datos utilizando funciones NumPy o los métodos `ndarray` correspondientes. Por ejemplo, a
calcular la media y la mediana de un conjunto de datos, podemos usar las funciones NumPy media y mediana:

```python
x = np.array([3.5, 1.1, 3.2, 2.8, 6.7, 4.4, 0.9, 2.2])
```

```python
np.mean(x)
```

```python
np.median(x)
```

De manera similar, podemos usar funciones `min` y `max` o métodos `ndarray` para calcular los valores mínimo y máximo en la matriz:

```python
x.min(), x.max()
```

Para calcular la varianza y la desviación estándar de un conjunto de datos, utilizamos `var`y métodos estándar. Por defecto, la fórmula para la varianza de la población y el estándar.
Se utiliza la desviación (es decir, se supone que el conjunto de datos es toda la población).

```python
x.var()
```

```python
x.std()
```

Sin embargo, para cambiar este comportamiento, podemos usar el argumento `ddof` (grados delta de libertad). El denominador en la expresión de la varianza es el número de elementos en la matriz menos `ddof`, por lo que para calcular la estimación insesgada de la varianza y desviación estándar de una muestra, debemos establecer` ddof=1`:

```python
x.var(ddof=1)
```

```python
x.std(ddof=1)
```

### 1.3 Números Casi- Aleatorios

La biblioteca estándar de Python contiene el módulo `random`, que proporciona funciones para generar números aleatorios individuales con algunas distribuciones básicas. El módulo `random` en el módulo NumPy proporciona una funcionalidad similar, pero ofrece funciones que generan arreglos de NumPy con números aleatorios, y tiene soporte para una selección más amplia de distribuciones de probabilidad. Los arreglos con números aleatorios son a menudo prácticos para fines computacionales, por lo que aquí nos centramos en el módulo `random` de NumPy, y más adelante también en las funciones y clases de mayor nivel en `scipy.stats`, que se basan en NumPy y lo extienden.

Anteriormente en este libro, ya hemos utilizado `np.random.rand`, que genera números de punto flotante distribuidos uniformemente en el intervalo semiabierto $[0, 1)$ (es decir, $0.0$ es un resultado posible, pero $1.0$ no lo es).

Además de esta función, el módulo `np.random` también contiene una gran colección de otras funciones para generar números aleatorios que cubren diferentes intervalos, tienen diferentes distribuciones y toman valores de diferentes tipos (por ejemplo, números de punto flotante y enteros). Por ejemplo:
* la función `randn` produce números aleatorios distribuidos según la distribución normal estándar (la distribución normal con media $0$ y desviación estándar $1$),
* y la función `randint` genera enteros distribuidos uniformemente entre un valor bajo (inclusive) y un valor alto (exclusive).

Cuando las funciones `rand` y `randn` se llaman sin argumentos, producen un único número aleatorio:

```python
np.random.rand()
```

```python
np.random.randn()
```

Sin embargo, pasar la forma del arreglo como argumentos a estas funciones produce arreglos de números aleatorios. Por ejemplo, aquí generamos un vector de longitud $5$ usando `rand` pasando un solo argumento $5$ y un arreglo de $2 \times 4$ usando `randn` pasando los argumentos $2$ y $4$ (los arreglos de mayor dimensión se generan pasando la longitud de cada dimensión como argumentos):

```python
np.random.rand(5)
```

```python
np.random.randn(2, 4)
```

Para generar enteros aleatorios utilizando `randint` (ver también `random_integers`), necesitamos proporcionar ya sea el límite superior para los números aleatorios (en cuyo caso el límite inferior es implícitamente cero) o ambos límites, el inferior y el superior. El tamaño del arreglo generado se especifica utilizando el argumento clave `size`, y puede ser un entero o una tupla que especifica la forma de un arreglo multidimensional:

```python
np.random.randint(10, size=10)
```

```python
np.random.randint(low=10, high=20, size=(2, 10))
```

Cabe destacar que la función `randint` genera enteros aleatorios en el intervalo semiabierto $[low, high)$.

Para demostrar que los números aleatorios producidos por `rand`, `randn` y `randint` están distribuidos de manera diferente, podemos trazar los histogramas de, por ejemplo, $10000$ números aleatorios producidos por cada función.
El resultado se muestra en la Figura 13-1. Observamos que las distribuciones de `rand` y `randint` parecen ser uniformes pero tienen rangos y tipos diferentes, mientras que la distribución de los números producidos por `randn` se asemeja a una curva gaussiana centrada en cero, como se esperaba.

**GRÁFICO CON MATPLOTLIB**

```python
fig, axes = plt.subplots(1, 3, figsize=(18, 3))
...: axes[0].hist(np.random.rand(10000))
...: axes[0].set_title("rand")
...: axes[1].hist(np.random.randn(10000))
...: axes[1].set_title("randn")
...: axes[2].hist(np.random.randint(low=1, high=10, size=10000),

bins=9, align='left')

...: axes[2].set_title("randint(low=1, high=10)")

plt.show()
```

**GRÁFICO CON SEABORN**

```python
from pickle import TRUE
## Crear la figura con 3 subgráficos
fig, axes = plt.subplots(1, 3, figsize=(18, 3))

## Histograma usando Seaborn
sns.histplot(np.random.rand(10000), ax=axes[0], kde=True)
axes[0].set_title("rand")

sns.histplot(np.random.randn(10000), ax=axes[1], kde=False)
axes[1].set_title("randn")

sns.histplot(np.random.randint(low=1, high=10, size=10000), ax=axes[2], bins=9, kde=False)
axes[2].set_title("randint(low=1, high=10)")

## Mostrar el gráfico
plt.show()
```

En el análisis estadístico, a menudo es necesario generar una lista única de enteros. Esto corresponde a realizar un muestreo (selección aleatoria) de elementos de un conjunto (población) sin reposición (de modo que no obtenemos el mismo elemento dos veces). Desde el módulo aleatorio de NumPy, podemos utilizar la función `choice` para generar este tipo de números aleatorios. Como primer argumento, podemos proporcionar una lista (o arreglo) con los valores de la población o un número entero que corresponde al número de elementos en la población. Como segundo argumento, damos el número de valores que se van a muestrear. Si los valores deben ser muestreados con o sin reposición se puede especificar utilizando el argumento clave `replace`, que toma los valores booleanos $True$ o $False$.

Por ejemplo, para muestrear cinco elementos únicos (sin reposición) del conjunto de enteros entre $0$ (inclusive) y $10$ (exclusive), podemos usar:

```python
np.random.choice(10, 5, replace=False)
```

Cuando se trabaja con generación de números aleatorios, puede ser útil "sembrar" el generador de números aleatorios. La semilla es un número que inicializa el generador de números aleatorios a un estado específico, de modo que, una vez que ha sido sembrado con un número específico, siempre genera la misma secuencia de números aleatorios. Esto puede ser útil cuando se realiza pruebas y para reproducir resultados previos, y ocasionalmente en aplicaciones que requieren volver a sembrar el generador de números aleatorios (por ejemplo, después de haber bifurcado un proceso).

Para sembrar el generador de números aleatorios en NumPy, podemos usar la función `seed`, que toma un número entero como argumento:

```python
np.random.seed(123456789)
np.random.rand()
```

```python
np.random.rand()
```

Cabe destacar que, después de haber sembrado el generador de números aleatorios con un número específico, aquí $123456789$, las siguientes llamadas a los generadores de números aleatorios siempre producen los mismos resultados. La semilla del generador de números aleatorios es un estado global del módulo `np.random`.

Un nivel más fino de control sobre el estado del generador de números aleatorios se puede lograr utilizando la clase `RandomState`, que opcionalmente toma un número entero como argumento para su inicializador. El objeto `RandomState` mantiene un registro del estado del generador de números aleatorios y permite mantener varios generadores de números aleatorios independientes en el mismo programa (lo cual puede ser útil, por ejemplo, cuando se trabaja con aplicaciones multihilo).

Una vez que se ha creado un objeto `RandomState`, podemos utilizar los métodos de este objeto para generar números aleatorios. La clase `RandomState` tiene métodos que corresponden a las funciones disponibles en el módulo `np.random`. Por ejemplo, podemos usar el método `randn` de la clase `RandomState` para generar números aleatorios distribuidos según la normal estándar:

```python
prng = np.random.RandomState(123456789)
prng.randn(2, 4)
```

De manera similar, existen métodos como `rand`, `randint`, `rand_integers` y `choice`, que también corresponden a las funciones en el módulo `np.random` con el mismo nombre. Se considera una buena práctica de programación utilizar una instancia de `RandomState` en lugar de usar directamente las funciones en el módulo `np.random`, porque evita depender de una variable de estado global y mejora el aislamiento del código. Esto es una consideración importante al desarrollar funciones de biblioteca que usan números aleatorios, pero quizás sea menos relevante en aplicaciones y cálculos más pequeños.

### 1.4 Simulando Distribuciones

Además de las distribuciones fundamentales de números aleatorios que hemos visto hasta ahora (distribuciones uniformes discretas y continuas, `randint` y `rand`, y la distribución normal estándar, `randn`), también existen funciones y métodos de `RandomState` para una gran cantidad de distribuciones de probabilidad que ocurren en estadística. Por mencionar solo algunas, están la distribución continua $ \chi^2 $ (chi-cuadrado, `chisquare`), la distribución de Student $t$ (distribución `standard_t`), y la distribución $F$ (distribución `f`):

```python
prng.chisquare(1, size=(2, 2))
```

```python
prng.standard_t(1, size=(2, 3))
```

```python
prng.f(5, 2, size=(2, 4))
```

y la distribución binomial discreta (binomial) y la distribución de Poisson (poisson):

```python
prng.binomial(10, 0.5, size=10)
```

```python
prng.poisson(5, size=10)
```

Lista de distribuciones disponibles dentro de la clase `RandomState` en NumPy:

### 1.5 Distribuciones continuas:

- **beta(a, b, size=None)**: Distribución Beta.
- **chisquare(df, size=None)**: Distribución chi-cuadrado.
- **dirichlet(alpha, size=None)**: Distribución Dirichlet.
- **exponential(scale=1.0, size=None)**: Distribución Exponencial.
- **f(dfnum, dfden, size=None)**: Distribución $F$.
- **gamma(shape, scale=1.0, size=None)**: Distribución Gamma.
- **gumbel(loc=0.0, scale=1.0, size=None)**: Distribución Gumbel.
- **laplace(loc=0.0, scale=1.0, size=None)**: Distribución Laplace.
- **logistic(loc=0.0, scale=1.0, size=None)**: Distribución Logística.
- **lognormal(mean=0.0, sigma=1.0, size=None)**: Distribución Log-normal.
- **multivariate_normal(mean, cov, size=None, check_valid='warn', tol=1e-8)**: Distribución normal multivariante.
- **noncentral_chisquare(df, nonc, size=None)**: Distribución chi-cuadrado no central.
- **noncentral_f(dfnum, dfden, nonc, size=None)**: Distribución $F$ no central.
- **normal(loc=0.0, scale=1.0, size=None)**: Distribución Normal (Gaussiana).
- **pareto(a, size=None)**: Distribución Pareto II o Lomax.
- **power(a, size=None)**: Distribución de Potencia.
- **rayleigh(scale=1.0, size=None)**: Distribución Rayleigh.
- **standard_cauchy(size=None)**: Distribución de Cauchy estándar.
- **standard_exponential(size=None)**: Distribución exponencial estándar.
- **standard_gamma(shape, size=None)**: Distribución Gamma estándar.
- **standard_normal(size=None)**: Distribución normal estándar.
- **standard_t(df, size=None)**: Distribución t de Student estándar.
- **triangular(left, mode, right, size=None)**: Distribución Triangular.
- **uniform(low=0.0, high=1.0, size=None)**: Distribución Uniforme.
- **vonmises(mu, kappa, size=None)**: Distribución Von Mises.
- **wald(mean, scale, size=None)**: Distribución Wald.
- **weibull(a, size=None)**: Distribución Weibull.

### 1.6 Distribuciones discretas:

- **binomial(n, p, size=None)**: Distribución Binomial.
- **geometric(p, size=None)**: Distribución Geométrica.
- **hypergeometric(ngood, nbad, nsample, size=None)**: Distribución Hipergeométrica.
- **logseries(p, size=None)**: Distribución Logarítmica.
- **multinomial(n, pvals, size=None)**: Distribución Multinomial.
- **negative_binomial(n, p, size=None)**: Distribución Binomial negativa.
- **poisson(lam=1.0, size=None)**: Distribución Poisson.
- **zipf(a, size=None)**: Distribución Zipf.

[random — Generate pseudo-random numbers](https://docs.python.org/es/3/library/random.html)

https://docs.python.org/es/3/library/random.html

Para obtener una lista completa de las funciones de distribución disponibles, consulta las docstrings del módulo `np.random`, usa `help(np.random)` y la clase `RandomState`. Aunque es posible usar las funciones de `np.random` y los métodos de `RandomState` para extraer números aleatorios de muchas distribuciones estadísticas diferentes, cuando se trabaja con distribuciones, existe una interfaz de más alto nivel en el módulo `scipy.stats` que combina el muestreo de números aleatorios con muchas otras funciones convenientes para distribuciones de probabilidad. En la siguiente sección, exploramos esto con más detalle.

```python
help(np.random)
```

```python
import scipy as sc
from scipy import stats
```

```python
help(stats)
```

### 1.7 Variables Aleatorias y Distribuciones

En la teoría de la probabilidad, el conjunto de posibles resultados de un proceso aleatorio se llama **espacio muestral**. A cada elemento del espacio muestral (es decir, un resultado de un experimento o una observación) se le puede asignar una probabilidad, y las probabilidades de todos los posibles resultados definen la **distribución de probabilidad**.

Una **variable aleatoria** es una asignación del espacio muestral a los números reales o a los enteros. Por ejemplo, los posibles resultados de un lanzamiento de moneda son cara y cruz, por lo que el espacio muestral es $\{\text{cara}, \text{cruz}\}$, y una posible variable aleatoria toma el valor $0$ para cara y $1$ para cruz.

En general, hay muchas maneras de definir variables aleatorias para los posibles resultados de un proceso aleatorio dado. Las variables aleatorias son una representación independiente del problema de un proceso aleatorio. Es más fácil trabajar con variables aleatorias porque están descritas por números en lugar de resultados de espacios muestrales específicos del problema.

Un paso común en la resolución de problemas estadísticos es, por lo tanto, mapear los resultados a valores numéricos y determinar la distribución de probabilidad de esos valores.

En consecuencia, una **variable aleatoria** se caracteriza por sus posibles valores y su **distribución de probabilidad**, que asigna una probabilidad a cada valor posible. Cada observación de la variable aleatoria resulta en un número aleatorio, y la distribución de los valores observados se describe mediante la distribución de probabilidad. Existen dos tipos principales de distribuciones: **discretas** y **continuas**, que corresponden a valores enteros y valores reales, respectivamente.

Al trabajar con estadísticas, tratar con variables aleatorias es de gran importancia, y en la práctica esto a menudo significa trabajar con distribuciones de probabilidad. El módulo `scipy.stats` proporciona clases para representar variables aleatorias con una gran cantidad de distribuciones de probabilidad. Existen dos clases base para variables aleatorias discretas y continuas: `rv_discrete` y `rv_continuous`.

Estas clases no se utilizan directamente, sino como clases base para variables aleatorias con distribuciones específicas, y definen una interfaz común para todas las clases de variables aleatorias en `scipy.stats`. Un resumen de los métodos seleccionados para variables aleatorias discretas y continuas se presenta en la Tabla 13-1.

### 1.8 Tabla 13-1. Métodos seleccionados para variables aleatorias discretas y continuas en el módulo `scipy.stats`

| Métodos     | Descripción |
|-------------|-------------|
| **pdf/pmf** | Función de distribución de probabilidad (para variables continuas) o función de masa de probabilidad (para variables discretas). |
| **cdf**     | Función de distribución acumulada. |
| **sf**      | Función de supervivencia ($1 - \text{cdf}$). |
| **ppf**     | Función percentil (inversa de la cdf). |
| **moment**  | Momentos no centrales de orden $n$. |
| **stats**   | Estadísticas de la distribución (típicamente la media y la varianza, a veces estadísticas adicionales). |
| **fit**     | Ajuste de la distribución a los datos utilizando una optimización de máxima verosimilitud numérica (para distribuciones continuas). |
| **expect**  | Valor de la expectativa de una función con respecto a la distribución. |
| **interval**| Los puntos finales del intervalo que contiene un porcentaje dado de la distribución (intervalo de confianza). |
| **rvs**     | Muestras de la variable aleatoria. Toma como argumento el tamaño del array resultante de las muestras. |
| **mean, median, std, var** | Estadísticas descriptivas: media, mediana, desviación estándar y varianza de la distribución. |

### 1.9 Métodos adicionales para variables aleatorias discretas:

| Métodos     | Descripción |
|-------------|-------------|
| **entropy** | Calcula la entropía de la distribución. |
| **support** | Devuelve una tupla que contiene el límite inferior y superior del soporte de la distribución. |

### 1.10 Métodos adicionales para variables aleatorias continuas:

| Métodos     | Descripción |
|-------------|-------------|
| **isf**     | Función de cuantil inversa de supervivencia (inversa de la sf). |
| **logpdf/logpmf** | Logaritmo de la función de densidad de probabilidad o función de masa de probabilidad. |
| **logcdf**  | Logaritmo de la función de distribución acumulada. |
| **logsf**   | Logaritmo de la función de supervivencia. |

Además de estos métodos, también hay varios otros métodos específicos para ciertas distribuciones. Para obtener una lista completa de todos los métodos disponibles para una distribución específica, consulta la documentación de `scipy.stats` usando `help(stats.<distribution_name>)`.

```python
help(stats.norm)
```

**Referencia**:

[Statistical functions (scipy.stats)](https://docs.scipy.org/doc/scipy/reference/stats.html)

https://docs.scipy.org/doc/scipy/reference/stats.html

Existen una gran cantidad de clases para variables aleatorias discretas y continuas en el módulo `scipy.stats`. En el momento de escribir este texto, hay clases para 13 distribuciones discretas y 98 distribuciones continuas, que incluyen las distribuciones más comúnmente encontradas (y muchas menos comunes). Para una referencia completa, consulta la docstring del módulo `stats`: `help(stats)`.

A continuación, exploramos algunas de las distribuciones más comunes, pero el uso de todas las demás distribuciones sigue el mismo patrón.

Las clases de variables aleatorias en el módulo `scipy.stats` tienen varios casos de uso. Son representaciones de la distribución, que pueden utilizarse para calcular estadísticas descriptivas y para graficar, y también pueden usarse para generar números aleatorios siguiendo la distribución dada, utilizando el método `rvs` (muestra de variable aleatoria). Este último caso de uso es similar al que utilizamos con el módulo `np.random` anteriormente en este capítulo.

Como demostración de cómo utilizar las clases de variables aleatorias en `scipy.stats`, consideremos el siguiente ejemplo en el que creamos una variable aleatoria distribuida normalmente con una media de $1.0$ y una desviación estándar de $0.5$:

```python
X = stats.norm(1, 0.5)
```

Ahora $X$ es un objeto que representa una variable aleatoria y podemos calcular
estadística descriptiva de esta variable aleatoria utilizando, por ejemplo, la media, mediana, estándar y métodos var:

```python
X.mean()
```

```python
X.median()
```

```python
X.std()
```

```python
X.var()
```

Los momentos no centrales de orden arbitrario se pueden calcular con el método del momento:

```python
[X.moment(n) for n in range(5)]
```

**NOTA**

`X.moment(n)` calcula momentos crudos, no momentos centrales.

El método `.moment(n)` de un objeto de distribución de `scipy.stats` calcula los momentos crudos o no centrales. Los momentos crudos se definen como:

$$
E[X^n] \quad \text{ Valor esperado de } X \text{ elevado a la potencia de } n
$$

Por otro lado, los momentos centrales se definen como:

$$
E[(X - \mu)^n] \quad \text{ Valor esperado de } (X - \mu) \text{ elevado a la potencia de } n
$$

**¿Por qué el primer momento crudo no es 0?**

El primer momento crudo ($n=1$) es simplemente el valor esperado (media) de la distribución, que en tu caso es $1.0$. No es el momento central, que se calcularía como:

$$
E[(X - \mu)^1]
$$

Y que, en efecto, sería igual a 0.

En teoría de probabilidad y estadística, los momentos centrales se utilizan para caracterizar la forma de una distribución de probabilidad. Se calculan como el valor esperado de la diferencia entre una variable aleatoria y su media, elevada a una determinada potencia. Los momentos centrales proporcionan información sobre el centro, la dispersión, la asimetría y la curtosis de la distribución.

### 1.11 Momentos Centrales

Para una variable aleatoria $X$ con una media denotada por $\mu$, el momento central de orden $n$ se define como:

$$
E\left[(X - \mu)^n\right]
$$

donde $E[\cdot]$ denota el operador de valor esperado.

### 1.12 Entendiendo los Momentos Centrales

- **Momento Central de orden 0**: Siempre es igual a 1.
- **Momento Central de orden 1**: Siempre es igual a 0 (ya que es la desviación esperada de la media).
- **Momento Central de orden 2**: Este es la varianza ($\sigma^2$), que mide la dispersión o la extensión de la distribución.
- **Momento Central de orden 3**: Se usa para calcular la asimetría (skewness), que indica la falta de simetría de la distribución.
- **Momento Central de orden 4**: Se usa para calcular la curtosis (kurtosis), que mide la "apuntamiento" de la distribución (qué tan concentrada está la probabilidad alrededor de la media y en las colas).

### 1.13 El código:

El fragmento de código:

$$
[X.moment(n) \text{ for } n \text{ en el rango de } 5]
$$

está calculando los primeros cinco momentos no centrales (momentos crudos) de la distribución normal representada por la variable $X$. El método `.moment(n)` del objeto `scipy.stats.norm` te da el $n$-ésimo momento crudo, no el momento central.

### 1.14 Diferencia clave

Los momentos crudos usan $E[X^n]$ en lugar de $E[(X - \mu)^n]$ en sus cálculos.

Para calcular momentos centrales en tu código, primero deberías calcular la media $X.\text{mean}()$ y luego aplicar manualmente la fórmula del momento central usando las funciones de NumPy.

```python
X = stats.norm(1, 0.5)
```

```python
mean = X.mean()
```

```python
data = X.rvs(size=1000)  # Generate 1000 samples
```

```python
import numpy as np

## 1erd central moment (variance)
first_central_moment = np.mean((data - mean)**1)
first_central_moment
```

```python
## 2nd central moment (variance)
second_central_moment = np.mean((data - mean)**2)
second_central_moment
```

#### ¿Por qué 0.23999821698807636?

#### Varianza de la muestra:
Este valor es una estimación de la varianza basada en tu muestra de 1000 puntos de datos.

#### Varianza teórica:
La varianza teórica de tu distribución normal ($X$) es 0.25 (ya que la desviación estándar es 0.5 y la varianza se calcula como la desviación estándar al cuadrado: $\sigma^2 = 0.5^2 = 0.25$).

#### Variabilidad de muestreo:
Dado que estás utilizando una muestra finita (1000 puntos de datos) para estimar la varianza de una distribución infinita, habrá algo de variación aleatoria. Tu varianza calculada ($0.239998...$) está cerca del valor teórico pero no es exactamente la misma debido a esta variabilidad de muestreo.

#### Ley de los grandes números:
Si aumentaras significativamente el tamaño de tu muestra (por ejemplo, a 10,000 o 100,000), la varianza calculada probablemente se acercaría aún más a la varianza teórica de 0.25. Esto se debe a la ley de los grandes números, que establece que a medida que el tamaño de la muestra aumenta, la media y la varianza muestrales convergen hacia la verdadera media y varianza de la población.

#### En resumen:
El valor calculado de $0.239998...$ es una estimación de la varianza, y su ligera desviación del valor teórico es esperada debido a la naturaleza aleatoria del proceso de muestreo.

```python
## 3rd central moment
third_central_moment = np.mean((data - mean)**3)

## 4th central moment
fourth_central_moment = np.mean((data - mean)**4)

## etc...
```

Y podemos obtener una lista de estadísticas dependiente de la distribución utilizando el método `stats`.
(aquí, para una variable aleatoria distribuida normal, obtenemos la media y la varianza):

```python
X.stats()
```

### 1.15 Evaluación de funciones de distribución

Podemos evaluar la función de densidad de probabilidad (pdf), la función de distribución acumulada (cdf), la función de supervivencia (sf), etc., utilizando los métodos `pdf`, `cdf`, `sf`, entre otros. Todos estos métodos toman un valor o un arreglo de valores en los que evaluar la función:

```python
X.pdf([0, 1, 2])
```

```python
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

## Asumiendo que X ya está definido como stats.norm(1, 0.5)
x_values = [0, 1, 2]
pdf_values = X.pdf(x_values)

## Crear un rango de valores de x para la curva suave
x_range = np.linspace(X.ppf(0.01), X.ppf(0.99), 100)
pdf_range = X.pdf(x_range)

## Crear el gráfico con Seaborn
sns.lineplot(x=x_range, y=pdf_range) # Curva suave
plt.stem(x_values, pdf_values, linefmt='r-', markerfmt='ro', basefmt='k-') # Puntos específicos
plt.title('Función de Densidad de Probabilidad (PDF)')
plt.xlabel('x')
plt.ylabel('PDF(x)')
plt.grid(True)
plt.show()
```

```python
X.cdf([0, 1, 2, 3, 4])
```

```python
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

## Asumiendo que X ya está definido como stats.norm(1, 0.5)
x_values = [0, 1, 2, 3, 4]
cdf_values = X.cdf(x_values)

## Crear el gráfico con Seaborn
sns.lineplot(x=x_values, y=cdf_values, marker='o')
plt.title('Función de Distribución Acumulada (CDF)')
plt.xlabel('x')
plt.ylabel('CDF(x)')
plt.grid(True)
plt.show()
```

### 1.16 Método de intervalo

El método `interval` puede ser utilizado para calcular los valores inferiores y superiores de $x$ tales que un porcentaje dado de la distribución de probabilidad cae dentro del intervalo $(\text{lower}, \text{upper})$. Este método es útil para calcular intervalos de confianza y para seleccionar un rango de valores de $x$ para graficar.

```python
X.interval(0.95)
```

```python
X.interval(0.99)
```

```python
X = stats.norm(1, 0.5)  # Mean = 1, Standard Deviation = 0.5
lower_bound, upper_bound = X.interval(0.99)

x = np.linspace(X.ppf(0.001), X.ppf(0.999), 100)
plt.plot(x, X.pdf(x), 'b-', lw=2, label='PDF')
plt.fill_between(x, X.pdf(x), where=(lower_bound < x) & (x < upper_bound),
                 color='skyblue', alpha=0.6, label='99% Interval')
plt.title('Normal Distribution with 99% Interval')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.show()
```

### 1.17 Graficar una distribución de probabilidad

Para construir una intuición sobre las propiedades de una distribución de probabilidad, es útil graficarla, junto con la correspondiente función de probabilidad acumulada (CDF) y la función de percentiles (PPF). Para facilitar la repetición de este proceso con varias distribuciones, primero creamos una función `plot_rv_distribution` que grafica el resultado de los métodos `pdf` o `pmf`, `cdf`, `sf`, y `ppf` de los objetos de variables aleatorias del módulo `SciPy stats`, sobre un intervalo que contiene el 99.9% de la función de distribución de probabilidad. También resaltamos el área que contiene el 95% de la distribución de probabilidad utilizando el método de dibujo `fill_between`.

```python
def plot_rv_distribution(X, axes=None):
    """Plot the PDF or PMF, CDF, SF and PPF of a given random
    variable"""
    if axes is None:
        fig, axes = plt.subplots(1, 3, figsize=(12, 3))

    x_min_999, x_max_999 = X.interval(0.999)
    x999 = np.linspace(x_min_999, x_max_999, 1000)
    x_min_95, x_max_95 = X.interval(0.95)
    x95 = np.linspace(x_min_95, x_max_95, 1000)

    if hasattr(X.dist, "pdf"):
        axes[0].plot(x999, X.pdf(x999), label="PDF")
        axes[0].fill_between(x95, X.pdf(x95), alpha=0.25)
    else:
## discrete random variables do not have a pdf method, instead we use pmf:
        x999_int = np.unique(x999.astype(int))
        axes[0].bar(x999_int, X.pmf(x999_int), label="PMF")
    axes[1].plot(x999, X.cdf(x999), label="CDF")
    axes[1].plot(x999, X.sf(x999), label="SF")
    axes[2].plot(x999, X.ppf(x999), label="PPF")

    for ax in axes:
        ax.legend()

import matplotlib.pyplot as plt
import scipy.stats as stats

fig, axes = plt.subplots(3, 3, figsize=(12, 9))
## Assuming plot_rv_distribution is defined elsewhere
## and takes X and axes as arguments.
X = stats.norm()
plot_rv_distribution(X, axes=axes[0, :])
axes[0, 0].set_ylabel("Normal dist.")
X = stats.f(2, 50)
plot_rv_distribution(X, axes=axes[1, :])
axes[1, 0].set_ylabel("F dist.")
X = stats.poisson(5)
plot_rv_distribution(X, axes=axes[2, :])
axes[2, 0].set_ylabel("Poisson dist.")
```

```python
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import pandas as pd # Import pandas for creating a DataFrame

def plot_rv_distribution(X, axes=None):
    """Plot the PDF or PMF, CDF, SF and PPF of a given random variable using Seaborn"""
    if axes is None:
        fig, axes = plt.subplots(1, 3, figsize=(12, 3))

    x_min_999, x_max_999 = X.interval(0.999)
    x999 = np.linspace(x_min_999, x_max_999, 1000)
    x_min_95, x_max_95 = X.interval(0.95)
    x95 = np.linspace(x_min_95, x_max_95, 1000)

    if hasattr(X.dist, "pdf"):
## PDF plot using Seaborn
        axes[0].plot(x999, X.pdf(x999), label="PDF")
        axes[0].fill_between(x95, X.pdf(x95), alpha=0.25)

    else:
## PMF plot using Seaborn (for Poisson)
        x999_int = np.unique(x999.astype(int))

## Create a DataFrame for Seaborn barplot (easier to work with)
        df = pd.DataFrame({'x': x999_int, 'pmf': X.pmf(x999_int)})
        sns.barplot(x='x', y='pmf', data=df, ax=axes[0], label="PMF", color="skyblue")
        axes[0].set_xticks(x999_int)

## CDF and SF plot using Seaborn
    axes[1].plot(x999, X.cdf(x999), label="CDF")
    axes[1].plot(x999, X.sf(x999), label="SF")

## PPF plot using Seaborn
    axes[2].plot(x999, X.ppf(x999), label="PPF")

    for ax in axes:
        ax.legend()

fig, axes = plt.subplots(3, 3, figsize=(12, 9))
X = stats.norm()
plot_rv_distribution(X, axes=axes[0, :])
axes[0, 0].set_ylabel("Normal dist.")
X = stats.f(2, 50)
plot_rv_distribution(X, axes=axes[1, :])
axes[1, 0].set_ylabel("F dist.")
X = stats.poisson(5)
plot_rv_distribution(X, axes=axes[2, :])
axes[2, 0].set_ylabel("Poisson dist.")

plt.tight_layout()
plt.show()
```

### 1.18 Algunas funciones de distribución

Ejemplos de funciones de distribución de probabilidad (PDF), funciones de masa de probabilidad (PMF), funciones de distribución acumulada (CDF), funciones de supervivencia (SF) y funciones de punto porcentual (PPF)

A continuación se presentan ejemplos de las funciones mencionadas para tres distribuciones comunes: una distribución normal (parte superior), una distribución F (parte media) y una distribución de Poisson (parte inferior).

### 1.19 Distribución Normal

### 1.20 Función de Distribución de Probabilidad (PDF)
La función de densidad de probabilidad para una distribución normal es:

$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
$$

donde:
- $\mu$ es la media,
- $\sigma$ es la desviación estándar.

### 1.21 Función de Distribución Acumulada (CDF)
La función de distribución acumulada para una distribución normal es:

$$
F(x) = \frac{1}{2} \left[ 1 + \text{erf}\left( \frac{x - \mu}{\sigma \sqrt{2}} \right) \right]
$$

donde $\text{erf}$ es la función de error.

### 1.22 Función de Supervivencia (SF)
La función de supervivencia es:

$$
S(x) = 1 - F(x)
$$

### 1.23 Función de Punto Porcentual (PPF)
La función de punto porcentual es la inversa de la CDF y se denota como $F^{-1}$:

$$
\text{PPF}(p) = \mu + \sigma \sqrt{2} \, \text{erf}^{-1}(2p - 1)
$$

### 1.24 Distribución F

### 1.25 Función de Distribución de Probabilidad (PDF)
La función de densidad de probabilidad para una distribución F con parámetros $d_1$ y $d_2$ es:

$$
f(x) = \frac{\sqrt{\frac{(d_1 x)^{d_1}}{d_2^{d_2} (d_1 x + d_2)^{d_1 + d_2}}}}{B\left( \frac{d_1}{2}, \frac{d_2}{2} \right)}
$$

donde $B$ es la función beta y $d_1$ y $d_2$ son los grados de libertad.

### 1.26 Función de Distribución Acumulada (CDF)
La CDF para una distribución F es:

$$
F(x; d_1, d_2) = I_{\frac{d_1 x}{d_1 x + d_2}}\left( \frac{d_1}{2}, \frac{d_2}{2} \right)
$$

donde $I$ es la función de distribución incompleta beta.

### 1.27 Distribución de Poisson

### 1.28 Función de Masa de Probabilidad (PMF)
La función de masa de probabilidad para una distribución de Poisson es:

$$
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}
$$

donde $\lambda$ es el parámetro de la distribución, que representa la tasa de ocurrencia del evento.

### 1.29 Función de Distribución Acumulada (CDF)
La CDF de una distribución de Poisson es:

$$
F(k; \lambda) = P(X \leq k) = \sum_{i=0}^{k} \frac{\lambda^i e^{-\lambda}}{i!}
$$

### 1.30 Función de Supervivencia (SF)
La función de supervivencia para una distribución de Poisson es:

$$
S(k; \lambda) = 1 - F(k; \lambda) = 1 - \sum_{i=0}^{k} \frac{\lambda^i e^{-\lambda}}{i!}
$$

### 1.31 Función de Punto Porcentual (PPF)
La función de punto porcentual no tiene una forma cerrada simple para la distribución de Poisson, pero se puede aproximar numéricamente a partir de la CDF inversa.

$$
\text{PPF}(p; \lambda) = \min\{ k \mid F(k; \lambda) \geq p \}
$$

**Recomendación**:

* Si prioriza la concisión, las estimaciones estadísticas y, en general, gráficos atractivos con opciones de personalización razonables, Seaborn es una buena opción para este tipo de gráficos. Aún puede usar las funciones de Matplotlib directamente para personalizaciones específicas dentro de un gráfico de Seaborn si es necesario.

* Si necesita un control absoluto sobre cada elemento de la trama y tiene necesidades de estilo muy específicas que Seaborn no proporciona fácilmente, entonces Matplotlib podría ser una mejor opción, pero podría requerir más codificación.

### 1.32 Uso de Métodos de Clase en las Distribuciones Aleatorias de SciPy

En los ejemplos anteriores, hemos creado instancias de una clase de variables aleatorias y calculado estadísticas y otras propiedades utilizando llamadas a métodos. Sin embargo, una alternativa para utilizar las clases de variables aleatorias en el módulo `stats` de SciPy es usar los métodos de clase directamente.

Por ejemplo, podemos calcular la media de una distribución normal utilizando el método de clase `mean` de `stats.norm`, y pasar los parámetros de la distribución como argumentos (usualmente `loc` y `scale`, como en este caso para valores distribuidos normalmente):

```python
stats.norm.stats(loc=2, scale=0.5)
```

lo que da el mismo resultado que crear primero una instancia y luego llamar al
método correspondiente:

```python
stats.norm(loc=1, scale=0.5).stats()
```

La mayoría de los métodos en las clases `rv_discrete` y `rv_continuous` pueden ser utilizados como métodos de clase de esta manera.

Hasta ahora, hemos visto solo propiedades de la función de distribución de variables aleatorias. Es importante notar que, aunque una función de distribución describe una variable aleatoria, la distribución en sí misma es completamente determinista. Para generar números aleatorios que estén distribuidos según una distribución de probabilidad dada, podemos usar el método `rvs` (muestra de variable aleatoria). Este método toma como argumento la forma del arreglo requerido (puede ser un número entero para un vector o una tupla con las longitudes de las dimensiones para un arreglo de más de una dimensión).

A continuación, utilizamos `rvs(10)` para generar un arreglo unidimensional con diez valores:

```python
X = stats.norm(1, 0.5)
```

```python
X.rvs(10)
```

Para ver que los números aleatorios generados están efectivamente distribuidos según la función de distribución de probabilidad correspondiente, podemos graficar un histograma de una gran cantidad de muestras de una variable aleatoria y compararlo con la función de distribución de probabilidad.

Una vez más, para poder hacer esto fácilmente para muestras de varias variables aleatorias, creamos una función `plot_dist_samples` con este propósito. Esta función utiliza el método de intervalo para obtener un rango adecuado de la gráfica para un objeto de variable aleatoria dado.

```python
def plot_dist_samples(X, X_samples, title=None, ax=None):
    """
    Grafica la PDF y el histograma de muestras de una variable aleatoria continua.
    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(8, 4))

## Obtener el rango adecuado para la gráfica utilizando el método de intervalo
    x_lim = X.interval(.99)
    x = np.linspace(*x_lim, num=100)

## Graficar la PDF de la distribución
    ax.plot(x, X.pdf(x), label="PDF", lw=3)

## Graficar el histograma de las muestras
    ax.hist(X_samples, label="samples", density=1, bins=75)

## Establecer el rango del eje x
    ax.set_xlim(*x_lim)

## Agregar la leyenda
    ax.legend()

## Establecer el título de la gráfica si se proporciona
    if title:
        ax.set_title(title)

    return ax
```

Cabe destacar que en esta función hemos utilizado la sintaxis de desempaquetado de tuplas `*x_lim`, que distribuye los elementos de la tupla `x_lim` en los diferentes argumentos de la función. En este caso, es equivalente a `np.linspace(x_lim[0], x_lim[1], num=100)`.

A continuación, usamos esta función para visualizar 2000 muestras de tres variables aleatorias con diferentes distribuciones: aquí utilizamos la distribución t de Student, la distribución $\chi^2$ y la distribución exponencial, y los resultados se muestran en la Figura 13-3. Dado que 2000 es una muestra bastante grande, los gráficos del histograma de las muestras coinciden bien con la función de distribución de probabilidad. Con un número aún mayor de muestras, se puede esperar que la concordancia sea aún mejor.

```python
## Crear una figura con 3 subgráficas
fig, axes = plt.subplots(1, 3, figsize=(12, 3))

## Número de muestras
N = 2000

## Distribución t de Student
X = stats.t(7.0)
plot_dist_samples(X, X.rvs(N), "Distribución t de Student", ax=axes[0])

## Distribución chi-cuadrada
X = stats.chi2(5.0)
plot_dist_samples(X, X.rvs(N), r"$\chi^2$ dist.", ax=axes[1])

## Distribución exponencial
X = stats.expon(0.5)
plot_dist_samples(X, X.rvs(N), "Distribución exponencial", ax=axes[2])

plt.show()
```

### 1.33 Ajuste de Maxima Verosimilitud: Analisis Completo

El **ajuste de maxima verosimilitud (MLE)** estima parametros que maximizan la probabilidad de observar los datos.

### 1.34 Visualizaciones:
1. **Histograma vs PDF**: Compara distribucion empirica con ajustada
2. **CDF**: Funcion acumulada empirica vs teorica
3. **Q-Q Plot**: Puntos cerca de diagonal indican buen ajuste
4. **Residuos**: Identifica sesgos sistematicos

### 1.35 Tests de Bondad:
- **Kolmogorov-Smirnov**: p-valor > 0.05 indica buen ajuste
- **Anderson-Darling**: Mas sensible en las colas de la distribucion

```python
## Ajuste de Maxima Verosimilitud - Analisis Completo
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

print('='*70)
print('AJUSTE DE MAXIMA VEROSIMILITUD')
print('='*70)
print('\n1. Generando datos...')
datos_reales = stats.chi2.rvs(df=5, size=500)
print(f'   Muestras: {len(datos_reales)}')
print(f'   Media: {datos_reales.mean():.4f}')

print('\n2. Ajustando distribucion...')
parametros_ajustados = stats.chi2.fit(datos_reales)
df_aj, loc_aj, scale_aj = parametros_ajustados
print(f'   df: {df_aj:.4f}, loc: {loc_aj:.4f}, scale: {scale_aj:.4f}')

dist_ajustada = stats.chi2(df=df_aj, loc=loc_aj, scale=scale_aj)
dist_teorica = stats.chi2(df=5)

print('\n3. Generando visualizaciones...')
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

## Histograma vs PDF
ax1 = axes[0, 0]
ax1.hist(datos_reales, bins=50, density=True, alpha=0.6, color='skyblue',
         edgecolor='black', label='Datos reales')
x = np.linspace(0, datos_reales.max(), 1000)
ax1.plot(x, dist_ajustada.pdf(x), 'r-', lw=3, label=f'PDF ajustada (df={df_aj:.2f})')
ax1.plot(x, dist_teorica.pdf(x), 'g--', lw=2, label='PDF teorica (df=5)')
ax1.set_xlabel('Valor', fontsize=12)
ax1.set_ylabel('Densidad', fontsize=12)
ax1.set_title('Comparacion: Datos vs Distribuciones', fontsize=14, fontweight='bold')
ax1.legend()
ax1.grid(True, alpha=0.3)

## CDF
ax2 = axes[0, 1]
datos_ord = np.sort(datos_reales)
cdf_emp = np.arange(1, len(datos_ord)+1) / len(datos_ord)
ax2.plot(datos_ord, cdf_emp, 'b-', alpha=0.7, label='CDF empirica', lw=2.5)
ax2.plot(x, dist_ajustada.cdf(x), 'r-', lw=2.5, label='CDF ajustada')
ax2.plot(x, dist_teorica.cdf(x), 'g--', lw=2, label='CDF teorica')
ax2.set_xlabel('Valor', fontsize=12)
ax2.set_ylabel('Probabilidad acumulada', fontsize=12)
ax2.set_title('Funciones de Distribucion Acumulada', fontsize=14, fontweight='bold')
ax2.legend()
ax2.grid(True, alpha=0.3)

## Q-Q Plot
ax3 = axes[1, 0]
stats.probplot(datos_reales, dist=stats.chi2, sparams=parametros_ajustados, plot=ax3)
ax3.get_lines()[0].set_marker('o')
ax3.get_lines()[0].set_markersize(4)
ax3.get_lines()[1].set_color('red')
ax3.get_lines()[1].set_linewidth(2)
ax3.set_title('Q-Q Plot: Validacion del Ajuste', fontsize=14, fontweight='bold')
ax3.grid(True, alpha=0.3)

## Residuos
ax4 = axes[1, 1]
valores_esp = dist_ajustada.ppf(cdf_emp)
residuos = datos_ord - valores_esp
ax4.scatter(valores_esp, residuos, alpha=0.6, s=30, c=residuos, cmap='coolwarm')
ax4.axhline(y=0, color='red', linestyle='--', lw=2, label='Residuo = 0')
ax4.set_xlabel('Valores esperados', fontsize=12)
ax4.set_ylabel('Residuos', fontsize=12)
ax4.set_title('Analisis de Residuos', fontsize=14, fontweight='bold')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print('\n4. Pruebas de bondad de ajuste...')
print('='*70)
ks_stat, ks_pval = stats.kstest(datos_reales, lambda x: dist_ajustada.cdf(x))
print(f'\nTest Kolmogorov-Smirnov:')
print(f'  Estadistico: {ks_stat:.6f}')
print(f'  p-valor: {ks_pval:.6f}')
if ks_pval > 0.05:
    print(f'  RESULTADO: Buen ajuste (no rechazamos H0 al 95%)')
else:
    print(f'  RESULTADO: Ajuste cuestionable')

print('\n' + '='*70)
print('Analisis completado')
print('='*70)
```

### 1.36 Usos de la Distribución Ajustada (Y)

El objeto $Y$ es una herramienta poderosa para diversas tareas estadísticas. A continuación se detallan algunos de los usos clave:

### 1.37 Cálculo de Probabilidades
Puedes usar Y para calcular probabilidades asociadas con la distribución Chi-cuadrada ajustada. Por ejemplo:

- **Y.pdf(x)**: Calcula la función de densidad de probabilidad (PDF) en un valor dado $x$.
- **Y.cdf(x)**: Calcula la función de distribución acumulada (CDF) en un valor dado $x$, representando la probabilidad de que una variable aleatoria sea menor o igual a $x$.
- **Y.sf(x)**: Calcula la función de supervivencia (SF) en un valor dado $x$, representando la probabilidad de que una variable aleatoria sea mayor que $x$.

### 1.38 Generación de Nuevas Muestras Aleatorias
Puedes generar nuevas muestras aleatorias que sigan la distribución Chi-cuadrada ajustada utilizando **Y.rvs(size)**. Esto puede ser útil para simulaciones o análisis posteriores.

### 1.39 Ejemplos de Escenarios

Aquí tienes algunos ejemplos para ilustrar cómo podrías usar la distribución Chi-cuadrada ajustada en la práctica:

### 1.40 Prueba de Bondad de Ajuste
Si tienes datos observados y deseas probar si siguen una distribución Chi-cuadrada, podrías usar el método `fit` para estimar los parámetros y luego comparar los datos observados con la distribución ajustada mediante una prueba de bondad de ajuste.

### 1.41 Predicción de Valores Futuros
Si tienes un proceso que genera datos que parecen seguir una distribución Chi-cuadrada, podrías usar la distribución ajustada Y para predecir la probabilidad de observar ciertos valores en el futuro.

### 1.42 Simulación de Experimentos
Podrías usar **Y.rvs()** para generar datos aleatorios que sigan la distribución ajustada para simulaciones o análisis de Monte Carlo.

### 1.43 En Resumen

La distribución Chi-cuadrada ajustada Y proporciona una forma de modelar y entender tus datos al ajustarlos a una distribución de probabilidad conocida. Este modelo ajustado se puede usar para diversas tareas estadísticas, como calcular probabilidades, hacer predicciones y realizar inferencias descriptivas sobre la variabilidad del proceso nanotecnológico. Es una herramienta fundamental para el análisis estadístico y la ciencia de datos. ¡Espero que esto ayude a clarificar su propósito y cómo puedes usarlo de manera efectiva!

```python
x=5
## Y=parametros_ajustados # This was a tuple of parameters, not a distribution object
## Create the chi-squared distribution object using the fitted parameters
df_aj, loc_aj, scale_aj = parametros_ajustados
Y = stats.chi2(df=df_aj, loc=loc_aj, scale=scale_aj)
Y.pdf(x)
```

```python
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

def plot_rv_distribution(rv):
    """
    Plots the PDF, CDF, SF, and PPF of a given random variable.

    Args:
        rv: A SciPy stats random variable object.
    """
## Create x-axis values for plotting
    x = np.linspace(rv.ppf(0.01), rv.ppf(0.99), 100)

## Create subplots for PDF, CDF, SF, and PPF
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

## Plot PDF
    axes[0, 0].plot(x, rv.pdf(x), 'r-', lw=2, label='PDF')
    axes[0, 0].set_title('Probability Density Function (PDF)')

## Plot CDF
    axes[0, 1].plot(x, rv.cdf(x), 'b-', lw=2, label='CDF')
    axes[0, 1].set_title('Cumulative Distribution Function (CDF)')

## Plot SF (Survival Function)
    axes[1, 0].plot(x, rv.sf(x), 'g-', lw=2, label='SF')
    axes[1, 0].set_title('Survival Function (SF)')

## Plot PPF (Percent Point Function)
    axes[1, 1].plot(x, rv.ppf(x), 'm-', lw=2, label='PPF')
    axes[1, 1].set_title('Percent Point Function (PPF)')

## Add legends and grid to subplots
    for ax in axes.flatten():
        ax.legend(loc='best', frameon=False)
        ax.grid(True)

## Adjust spacing between subplots
    plt.tight_layout()

## Define Y as a normal random variable with mean 1 and standard deviation 0.5
Y = stats.norm(1, 0.5)

## Generate the plots (PDF, CDF, SF, PPF)
plot_rv_distribution(Y)

## Show the plot
plt.show()
```

### 1.44 Otros Métodos para determinar la distribución de una muestra

Existen métodos para intentar determinar la distribución de una muestra sin necesidad de identificar visualmente una posible distribución de antemano. Estos métodos se basan en algoritmos que exploran un conjunto de distribuciones candidatas y seleccionan la que mejor se ajusta a los datos según ciertos criterios.

Aquí dos enfoques:

### 1.45 **Algoritmos de selección de distribuciones**:

Existen bibliotecas en Python que implementan algoritmos para la selección automática de distribuciones, como `distfit` y `best_fit`.
Estas bibliotecas suelen utilizar una combinación de pruebas de bondad de ajuste, criterios de información (**AIC, BIC**) y otras métricas para evaluar el ajuste de diferentes distribuciones a los datos.
El usuario proporciona la muestra de datos y el algoritmo devuelve la distribución que mejor se ajusta según los criterios especificados.

```python
!pip install distfit

from distfit import distfit

## Generar una muestra de datos
data = np.random.normal(loc=0, scale=1, size=1000)

## Instanciar el objeto distfit
dist = distfit()

## Ajustar las distribuciones a los datos
dist.fit_transform(data)

## Mostrar la mejor distribución encontrada
print(dist.model)

## Visualizar el ajuste
dist.plot()
```

### 1.46 Red Neuronal Probabilistica: Analisis Completo

Las **redes neuronales probabilisticas** combinan deep learning con teoria de probabilidad.

### 1.47 Arquitectura:
- 3 capas ocultas (64, 32, 16) con ReLU y Dropout
- Capa de salida: `DistributionLambda` (genera distribucion Normal)
- Loss: Negative Log-Likelihood

### 1.48 Evaluacion:
- **Train/Test split**: 80/20
- **Metricas**: MAE, RMSE, R2 para ambos conjuntos
- **Visualizaciones**: 9 graficas incluyendo curvas de aprendizaje, predicciones, residuos

### 1.49 Interpretacion:
- **Delta (train-test) pequeno**: Modelo generaliza bien
- **Delta grande**: Posible sobreajuste
- **R2 cercano a 1**: Excelente ajuste

### 1.50 Comparacion con Metodos Clasicos:

| Aspecto | MLE Clasico | Red Neuronal |
|---------|-------------|---------------|
| Velocidad | Rapido | Lento |
| Interpretabilidad | Alta | Baja |
| Flexibilidad | Baja | Alta |
| Datos requeridos | Pocos | Muchos |

```python
## RED NEURONAL PROBABILISTICA: Analisis Train/Test Completo
import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
from scipy import stats

tfd = tfp.distributions
tfpl = tfp.layers

np.random.seed(42)
tf.random.set_seed(42)

print('='*80)
print(' '*20 + 'RED NEURONAL PROBABILISTICA')
print('='*80)

## 1. DATOS
print('\n[1/6] Generando datos...')
n_samples = 2000
X_data = np.random.randn(n_samples, 1).astype(np.float32)
y_data = X_data.copy()

X_train, X_test, y_train, y_test = train_test_split(
    X_data, y_data, test_size=0.2, random_state=42)

print(f'   Total: {n_samples} muestras')
print(f'   Train: {X_train.shape[0]} ({X_train.shape[0]/n_samples*100:.0f}%)')
print(f'   Test: {X_test.shape[0]} ({X_test.shape[0]/n_samples*100:.0f}%)')

## 2. MODELO
print('\n[2/6] Construyendo modelo...')
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(2),  # Output layer now directly outputs loc and scale
])

## Modified loss function to create distribution from model output
def neg_log_likelihood(y_true, y_pred_params):
## y_pred_params will be the output of the last Dense layer (loc and scale)
    loc, scale = tf.split(y_pred_params, num_or_size_splits=2, axis=-1)
## Ensure scale is positive using softplus
    scale = tf.math.softplus(scale)
## Create the distribution
    y_pred_dist = tfd.Normal(loc=loc, scale=scale)
## Compute the negative log probability
    return -y_pred_dist.log_prob(y_true)

model.compile(
    optimizer=tf.keras.optimizers.Adam(0.001),
    loss=neg_log_likelihood,
## Can add metrics that work with tensor output, e.g., 'mae' if desired,
## but be mindful that this is comparing the mean of the predicted distribution
## to the true value, not evaluating the full distribution fit.
## For now, keeping metrics simple or removed to avoid potential issues.
## metrics=['mae'] # Re-add MAE if needed and compatible
)

print(f'   Parametros: {model.count_params():,}')

## 3. ENTRENAR
print('\n[3/6] Entrenando...')
early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=15, restore_best_weights=True)
history = model.fit(X_train, y_train, validation_split=0.2, epochs=200, batch_size=32, callbacks=[early_stop], verbose=0)

print(f'   Epocas: {len(history.history["loss"])}')

## 4. PREDICCIONES
print('\n[4/6] Predicciones...')
## When predicting after training, get the parameters and create the distribution
y_pred_params_train = model(X_train)
y_pred_dist_train = tfd.Normal(loc=y_pred_params_train[..., :1], scale=tf.math.softplus(y_pred_params_train[..., 1:]))
y_pred_train = y_pred_dist_train.mean().numpy()

y_pred_params_test = model(X_test)
y_pred_dist_test = tfd.Normal(loc=y_pred_params_test[..., :1], scale=tf.math.softplus(y_pred_params_test[..., 1:]))
y_pred_test = y_pred_dist_test.mean().numpy()

## 5. METRICAS
print('\n[5/6] Calculando metricas...')
mae_train = mean_absolute_error(y_train, y_pred_train)
rmse_train = np.sqrt(mean_squared_error(y_train, y_pred_train))
r2_train = r2_score(y_train, y_pred_train)

mae_test = mean_absolute_error(y_test, y_pred_test)
rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))
r2_test = r2_score(y_test, y_pred_test)

print('\n' + '='*80)
print(' '*25 + 'METRICAS DE RENDIMIENTO')
print('='*80)
print(f'\nTRAIN:')
print(f'  MAE:  {mae_train:.6f}')
print(f'  RMSE: {rmse_train:.6f}')
print(f'  R2:   {r2_train:.6f}')

print(f'\nTEST:')
print(f'  MAE:  {mae_test:.6f}')
print(f'  RMSE: {rmse_test:.6f}')
print(f'  R2:   {r2_test:.6f}')

print(f'\nDIFERENCIA (sobreajuste):')
print(f'  Delta MAE:  {abs(mae_train-mae_test):.6f}')
print(f'  Delta RMSE: {abs(rmse_train-rmse_test):.6f}')
print(f'  Delta R2:   {abs(r2_train-r2_test):.6f}')
print('='*80)

## 6. VISUALIZACIONES
print('\n[6/6] Generando visualizaciones...')

fig = plt.figure(figsize=(20, 14))
gs = fig.add_gridspec(3, 3, hspace=0.35, wspace=0.3)

## Loss
ax1 = fig.add_subplot(gs[0, 0])
epochs = range(1, len(history.history['loss'])+1)
ax1.plot(epochs, history.history['loss'], 'b-', lw=2, label='Train', alpha=0.8)
ax1.plot(epochs, history.history['val_loss'], 'r-', lw=2, label='Val', alpha=0.8)
ax1.set_xlabel('Epoca', fontsize=11, fontweight='bold')
ax1.set_ylabel('Loss', fontsize=11, fontweight='bold')
ax1.set_title('Curva de Aprendizaje: Loss', fontsize=13, fontweight='bold')
ax1.legend()
ax1.grid(True, alpha=0.3)

## MAE
## MAE is calculated manually after training, not available in history
## ax2 = fig.add_subplot(gs[0, 1])
## ax2.set_xlabel('Epoca', fontsize=11, fontweight='bold')
## ax2.set_ylabel('MAE', fontsize=11, fontweight='bold')
## ax2.set_title('Curva de Aprendizaje: MAE (Calculated Post-Training)', fontsize=13, fontweight='bold')
## ax2.grid(True, alpha=0.3)
## Placeholder for MAE plot if history was available or calculated per epoch

## Barras metricas
ax3 = fig.add_subplot(gs[0, 2])
metricas = ['MAE', 'RMSE', 'R2']
train_vals = [mae_train, rmse_train, r2_train]
test_vals = [mae_test, rmse_test, r2_test]
x = np.arange(len(metricas))
w = 0.35
bars1 = ax3.bar(x-w/2, train_vals, w, label='Train', alpha=0.8, color='steelblue')
bars2 = ax3.bar(x+w/2, test_vals, w, label='Test', alpha=0.8, color='coral')
ax3.set_xticks(x)
ax3.set_xticklabels(metricas)
ax3.set_ylabel('Valor', fontsize=11, fontweight='bold')
ax3.set_title('Metricas: Train vs Test', fontsize=13, fontweight='bold')
ax3.legend()
ax3.grid(True, alpha=0.3, axis='y')
for bars in [bars1, bars2]:
    for bar in bars:
        h = bar.get_height()
        ax3.text(bar.get_x()+bar.get_width()/2, h, f'{h:.3f}', ha='center', va='bottom', fontsize=8)

## Scatter Train
ax4 = fig.add_subplot(gs[1, 0])
ax4.scatter(y_train, y_pred_train, alpha=0.4, s=25, c='steelblue')
lims = [min(y_train.min(), y_pred_train.min()), max(y_train.max(), y_pred_train.max())]
ax4.plot(lims, lims, 'r--', lw=2.5, label='Ideal', zorder=5)
ax4.set_xlabel('Real', fontsize=11, fontweight='bold')
ax4.set_ylabel('Predicho', fontsize=11, fontweight='bold')
ax4.set_title(f'Train: Real vs Pred (R2={r2_train:.4f})', fontsize=13, fontweight='bold')
ax4.legend()
ax4.grid(True, alpha=0.3)
ax4.set_aspect('equal', adjustable='box')

## Scatter Test
ax5 = fig.add_subplot(gs[1, 1])
ax5.scatter(y_test, y_pred_test, alpha=0.4, s=25, c='coral')
lims = [min(y_test.min(), y_pred_test.min()), max(y_test.max(), y_pred_test.max())]
ax5.plot(lims, lims, 'r--', lw=2.5, label='Ideal', zorder=5)
ax5.set_xlabel('Real', fontsize=11, fontweight='bold')
ax5.set_ylabel('Predicho', fontsize=11, fontweight='bold')
ax5.set_title(f'Test: Real vs Pred (R2={r2_test:.4f})', fontsize=13, fontweight='bold')
ax5.legend()
ax5.grid(True, alpha=0.3)
ax5.set_aspect('equal', adjustable='box')

## Combinado
ax6 = fig.add_subplot(gs[1, 2])
ax6.scatter(y_train, y_pred_train, alpha=0.3, s=20, c='steelblue', label='Train')
ax6.scatter(y_test, y_pred_test, alpha=0.3, s=20, c='coral', label='Test')
lims = [
    min(y_train.min(), y_test.min(), y_pred_train.min(), y_pred_test.min()),
    max(y_train.max(), y_test.max(), y_pred_train.max(), y_pred_test.max())
]
ax6.plot(lims, lims, 'r--', lw=2.5, label='Ideal', zorder=5)
ax6.set_xlabel('Real', fontsize=11, fontweight='bold')
ax6.set_ylabel('Predicho', fontsize=11, fontweight='bold')
ax6.set_title('Comparacion Train/Test', fontsize=13, fontweight='bold')
ax6.legend()
ax6.grid(True, alpha=0.3)
ax6.set_aspect('equal', adjustable='box')

## Residuos Train
ax7 = fig.add_subplot(gs[2, 0])
res_train = (y_train - y_pred_train).flatten()
ax7.scatter(y_pred_train, res_train, alpha=0.4, s=25, c='steelblue')
ax7.axhline(y=0, color='red', linestyle='--', lw=2.5, label='Res=0')
ax7.set_xlabel('Predicho', fontsize=11, fontweight='bold')
ax7.set_ylabel('Residuo', fontsize=11, fontweight='bold')
ax7.set_title('Residuos: Train', fontsize=13, fontweight='bold')
ax7.legend()
ax7.grid(True, alpha=0.3)

## Residuos Test
ax8 = fig.add_subplot(gs[2, 1])
res_test = (y_test - y_pred_test).flatten()
ax8.scatter(y_pred_test, res_test, alpha=0.4, s=25, c='coral')
ax8.axhline(y=0, color='red', linestyle='--', lw=2.5, label='Res=0')
ax8.set_xlabel('Predicho', fontsize=11, fontweight='bold')
ax8.set_ylabel('Residuo', fontsize=11, fontweight='bold')
ax8.set_title('Residuos: Test', fontsize=13, fontweight='bold')
ax8.legend()
ax8.grid(True, alpha=0.3)

## Distribucion errores
ax9 = fig.add_subplot(gs[2, 2])
ax9.hist(res_train, bins=50, alpha=0.6, label='Train', color='steelblue', density=True, edgecolor='black')
ax9.hist(res_test, bins=50, alpha=0.6, label='Test', color='coral', density=True, edgecolor='black')
x_norm = np.linspace(res_train.min(), res_train.max(), 100)
ax9.plot(x_norm, stats.norm.pdf(x_norm, 0, res_train.std()), 'g--', lw=2, label='Normal')
ax9.set_xlabel('Error', fontsize=11, fontweight='bold')
ax9.set_ylabel('Densidad', fontsize=11, fontweight='bold')
ax9.set_title('Distribucion de Errores', fontsize=13, fontweight='bold')
ax9.legend()
ax9.grid(True, alpha=0.3)

plt.suptitle('RED NEURONAL: Analisis Completo Train/Test', fontsize=16, fontweight='bold', y=0.997)
plt.show()

print('\n' + '='*80)
print('Analisis completo finalizado')
print('='*80)
```

### 1.51 Guardar el Modelo Entrenado

Puedes guardar tu modelo usando el método `model.save()`. Especifica la ruta donde quieres guardar el modelo.

```python
## Define la ruta donde quieres guardar el modelo
model_save_path = 'probabilistic_model.keras' # Added .keras extension

## Guarda el modelo en formato SavedModel
model.save(model_save_path)

print(f"Modelo guardado en: {model_save_path}")
```

### 1.52 Cargar el Modelo Guardado

Para usar el modelo más tarde, puedes cargarlo usando `tf.keras.models.load_model()`. Es importante que la función de pérdida personalizada (`neg_log_likelihood`) esté disponible en el entorno donde cargas el modelo, ya que es necesaria para la configuración del modelo.

```python
## Carga el modelo guardado
## Asegúrate de que la funcion neg_log_likelihood este definida en este entorno
loaded_model = tf.keras.models.load_model(model_save_path, custom_objects={'neg_log_likelihood': neg_log_likelihood})

print("Modelo cargado exitosamente.")
```

### 1.53 Usar el Modelo Cargado para Cálculos Probabilísticos

Una vez que el modelo está cargado, puedes usarlo para hacer predicciones en nuevos datos. La salida del modelo cargado seguirá siendo un objeto de distribución de TensorFlow Probability, lo que te permite realizar cálculos probabilísticos como obtener la media, la desviación estándar, o calcular la probabilidad de observar ciertos valores.

### 1.54 Problema contextualizado en Nanotecnología: Control de Calidad en Nanopartículas

Imagina que estás trabajando en un laboratorio de nanotecnología sintetizando nanopartículas de oro para aplicaciones biomédicas. El tamaño de las nanopartículas es crucial para su eficacia y seguridad. Durante el proceso de síntesis, controlas un parámetro clave, como la concentración de un agente reductor. Sabes que este parámetro influye en el tamaño final de las nanopartículas, pero el proceso tiene una variabilidad inherente.

Has recopilado datos experimentales donde registraste la concentración del agente reductor (`X`) y el tamaño promedio de las nanopartículas obtenidas (`y`). Entrenaste el modelo de red neuronal probabilística que acabamos de desarrollar para predecir el tamaño de la nanopartícula (`y`) basándose en la concentración del agente reductor (`X`).

Ahora, quieres utilizar tu modelo para:

1.  **Predecir el tamaño esperado** de las nanopartículas para nuevas concentraciones del agente reductor.
2.  **Cuantificar la incertidumbre** en esas predicciones (es decir, saber cuán variable podría ser el tamaño real alrededor de la predicción promedio).
3.  **Calcular la probabilidad** de que el tamaño de las nanopartículas caiga dentro de un rango específico o exceda un cierto umbral para una concentración dada. Esto es vital para el control de calidad, ya que solo se aceptan lotes de nanopartículas dentro de un rango de tamaño muy estrecho.

**Ejemplo de uso:**

Supongamos que quieres predecir el tamaño de las nanopartículas para concentraciones del agente reductor de 1.5, -0.8, 0.0 y 2.1 (estos valores, aunque simplificados para el ejemplo, representarían tus niveles controlados del parámetro X).

Utilizarías el código que ya tenemos para:

*   Obtener la media predicha del tamaño para cada concentración.
*   Obtener la desviación estándar predicha del tamaño para cada concentración (esta es tu medida de incertidumbre).
*   Calcular, por ejemplo, la probabilidad de que el tamaño de las nanopartículas sea mayor a 1.8 nm (un umbral de control de calidad) cuando la concentración del agente reductor es 1.5.

Este problema ilustra cómo el modelo probabilístico va más allá de una simple predicción puntual, proporcionando información valiosa sobre la variabilidad y permitiendo cálculos de probabilidad esenciales para el control de calidad en un contexto de nanotecnología.

```python
## Genera algunos datos nuevos para prediccion
new_data = np.array([[1.5], [-0.8], [0.0], [2.1]], dtype=np.float32)

## Realiza predicciones con el modelo cargado
## The loaded model outputs the raw parameters (loc and scale)
predicted_params = loaded_model(new_data)

## Explicitly create the distribution object from the predicted parameters
loc, scale = tf.split(predicted_params, num_or_size_splits=2, axis=-1)
## Ensure scale is positive using softplus, consistent with training
scale = tf.math.softplus(scale)
predicted_distribution = tfd.Normal(loc=loc, scale=scale)

## Ahora puedes usar los metodos de la distribucion para calculos probabilisticos
mean_predictions = predicted_distribution.mean().numpy()
stddev_predictions = predicted_distribution.stddev().numpy()
## You can also sample from the distribution
## samples = predicted_distribution.sample(100)

print("Predicciones (Media):")
print(mean_predictions)

print("\nPredicciones (Desviacion Estandar):")
print(stddev_predictions)

## Ejemplo: Calcular la probabilidad de que el primer nuevo dato sea mayor que 1.0
## This is equivalent to 1 - CDF(1.0)
probability_greater_than_1 = 1.0 - predicted_distribution.cdf(1.0).numpy()
print(f"\nProbabilidad de que el primer dato sea > 1.0: {probability_greater_than_1[0][0]:.4f}")
```

### 1.55 Interpretación de los Resultados en el Contexto del Problema de Nanotecnología

Recordemos que estás prediciendo el **tamaño promedio de las nanopartículas** (`y`) basado en la **concentración del agente reductor** (`X`). Las `Predicciones (Media)` te dan el tamaño promedio esperado, y las `Predicciones (Desviacion Estandar)` te dan la incertidumbre o variabilidad esperada alrededor de ese tamaño promedio para cada concentración de agente reductor que probaste (`new_data`).

Interpretación de los resultados:

1.  **Predicciones (Media):**
    *   Para la concentración de agente reductor de **1.5**, el modelo predice un tamaño promedio de nanopartícula de aproximadamente **1.397 nm**.
    *   Para la concentración de **-0.8**, el tamaño promedio predicho es de aproximadamente **-0.752 nm**. (Nota: Un tamaño negativo no tiene sentido físico. Esto podría indicar que la concentración de -0.8 está fuera del rango de los datos de entrenamiento donde el modelo se comporta bien, o que se necesita una transformación en los datos de salida para asegurar predicciones positivas).
    *   Para la concentración de **0.0**, el tamaño promedio predicho es de aproximadamente **-0.012 nm**. (Similar al punto anterior, sugiere revisar el rango de datos o aplicar transformaciones).
    *   Para la concentración de **2.1**, el tamaño promedio predicho es de aproximadamente **1.900 nm**.

2.  **Predicciones (Desviación Estándar):**
    *   Para la concentración de **1.5**, la desviación estándar predicha es de aproximadamente **0.193 nm**. Esto significa que, aunque el tamaño promedio esperado es 1.397 nm, el tamaño real de las nanopartículas en un lote sintetizado con esta concentración probablemente variará alrededor de este valor con una dispersión típica de 0.193 nm.
    *   Para la concentración de **-0.8**, la desviación estándar es de aproximadamente **0.088 nm**. La variabilidad predicha es menor aquí.
    *   Para la concentración de **0.0**, la desviación estándar es de aproximadamente **0.036 nm**. La variabilidad predicha es aún menor.
    *   Para la concentración de **2.1**, la desviación estándar es de aproximadamente **0.208 nm**. La variabilidad predicha es la más alta entre estos ejemplos.

    La desviación estándar es tu medida de **incertidumbre** o la **variabilidad esperada en el tamaño de las nanopartículas**. Un valor más alto indica que es probable que los tamaños de las nanopartículas dentro de un lote estén más dispersos alrededor del tamaño promedio predicho. Esto es crucial para el control de calidad, ya que te dice cuán consistente es probable que sea el proceso de síntesis para una concentración dada del agente reductor.

3.  **Probabilidad de que el primer dato sea > 1.0: 0.9805**
    *   Esta línea se refiere a la primera entrada en `new_data`, que corresponde a una concentración de agente reductor de **1.5**.
    *   El resultado de **0.9805** significa que, basado en tu modelo probabilístico, hay una probabilidad del **98.05%** de que el tamaño de las nanopartículas sintetizadas con una concentración de agente reductor de 1.5 nm sea **mayor que 1.0 nm**.

**Implicaciones para el Control de Calidad:**

*   Si tu criterio de control de calidad requiere que el tamaño de las nanopartículas esté en un rango específico (por ejemplo, entre 1.2 nm y 1.6 nm), no solo mirarías la media predicha (1.397 nm para X=1.5), sino también la desviación estándar (0.193 nm). Una desviación estándar alta podría significar que, aunque la media esté en el rango, una porción significativa de las nanopartículas podría estar fuera del rango aceptable debido a la variabilidad del proceso.
*   La probabilidad calculada (98.05% de que el tamaño sea > 1.0 nm para X=1.5) es un ejemplo directo de cómo puedes usar el modelo para tomar decisiones de control de calidad. Si, por ejemplo, la especificación mínima de tamaño es 1.0 nm, una probabilidad del 98.05% de estar por encima de ese umbral es una información valiosa para decidir si un lote producido bajo estas condiciones es aceptable. Podrías calcular la probabilidad de estar *dentro* de tu rango de tamaño objetivo de manera similar.
*   Los resultados para concentraciones de -0.8 y 0.0 sugieren que estas concentraciones, si bien predicen desviaciones estándar bajas, dan como resultado tamaños promedio que no son físicamente posibles. Esto subraya la importancia de entender el dominio de tus datos y el comportamiento del modelo fuera del rango de entrenamiento.

Este análisis te permite ir más allá de simplemente predecir un valor puntual y te da una comprensión de la incertidumbre asociada, lo cual es fundamental para optimizar tus procesos de síntesis y establecer criterios de control de calidad basados en probabilidades.

#Investigación

## 10. Módulo de Simulación: Estimación No Paramétrica de Densidad (KDE) y Muestras Multivariadas

En el análisis de datos de caracterización nanotecnológica, cuando no se presupone un modelo paramétrico estricto, se emplea la **Estimación No Paramétrica de Densidad por Kernel (KDE)**.

### 10.1 Definición Matemática de KDE
Dada una muestra independiente de tamaño $n$, el estimador de densidad por kernel $f_h(x)$ viene dado por:
$$f_h(x) = \frac{1}{n h} \sum_{i=1}^n K\left(\frac{x - x_i}{h}
\right)$$
donde $K(u)$ es el kernel gaussiano $K(u) = \frac{1}{\sqrt{2\pi}} e^{-u^2/2}$ y $h > 0$ es el ancho de banda (bandwidth).

### 10.2 Implementación Computacional en Python
```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, Math

## Generación de muestra sintética bimodal (nanopartículas coloidales)
np.random.seed(101)
muestras_nano = np.concatenate([
    stats.norm.rvs(loc=15, scale=2, size=300),
    stats.norm.rvs(loc=35, scale=5, size=700)
])

## Estimación KDE
kde = stats.gaussian_kde(muestras_nano, bw_method='silverman')
x_grid = np.linspace(5, 55, 500)
pdf_kde = kde.evaluate(x_grid)

## Visualización
plt.figure(figsize=(10, 5))
sns.histplot(muestras_nano, bins=30, stat="density", color="skyblue", label="Histrograma Muestral")
plt.plot(x_grid, pdf_kde, color="darkblue", linewidth=2.5, label="Estimación KDE (Kernel Gaussiano)")
plt.title("Estimación No Paramétrica de Densidad de Diámetro de Nanopartículas (KDE)", fontsize=12, fontweight="bold")
plt.xlabel("Diámetro (nm)")
plt.ylabel("Densidad de Probabilidad")
plt.legend()
plt.tight_layout()
plt.show()

display(Math(fr"\text{{Estimación KDE completada sobre }} n = {len(muestras_nano)} \text{{ observaciones.}}"))
```

---

## 11. Módulo de Integración de Datos Reales: Materials Project API (mp-api) y OQMD API

En la investigación moderna en IA y Nanotecnología, el análisis estadístico descriptivo se aplica directamente sobre repositorios masivos de materiales como **Materials Project** y **OQMD (Open Quantum Materials Database)**.

### 11.1 Consulta y Conexión a Materials Project API (`MPRester`)
Mediante la librería oficial `mp-api` y `pymatgen`, es posible extraer propiedades fisicoquímicas reales (como el *Band Gap* $E_g$, *Energía de Formación por Átomos* $\Delta E_f$, *Volumen de Celda* $V$ y *Grupo Espacial*):

```python
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, Math

## 1. Simulación / Carga de Estructura de Datos de Materials Project (mp-api)
## Campos extraídos: material_id, formula, band_gap (eV), formation_energy_per_atom (eV/atom), volume (A^3)
np.random.seed(2026)
n_materiales = 150

datos_materials_project = {
    "material_id": [f"mp-{1000 + i}" for i in range(n_materiales)],
    "formula": ["TiO2"]*50 + ["ZnO"]*50 + ["Fe2O3"]*50,
    "band_gap": np.concatenate([
        stats.norm.rvs(loc=3.2, scale=0.15, size=50), # TiO2 (Anatasa)
        stats.norm.rvs(loc=3.37, scale=0.20, size=50), # ZnO
        stats.norm.rvs(loc=2.1, scale=0.18, size=50)   # Fe2O3 (Hematita)
    ]),
    "formation_energy_per_atom": stats.expon.rvs(scale=0.8, size=n_materiales) - 3.5,
    "volume_a3": stats.lognorm.rvs(s=0.3, scale=120, size=n_materiales)
}

df_mp = pd.DataFrame(datos_materials_project)

## 2. Análisis Estadístico Descriptivo de Band Gap (eV)
band_gap_data = df_mp["band_gap"]

media_bg = band_gap_data.mean()
mediana_bg = band_gap_data.median()
std_bg = band_gap_data.std()
skewness_bg = band_gap_data.skew()

display(Math(fr"\text{{Resumen Estadístico del Band Gap }} (E_g):"))
display(Math(fr"\text{{Media: }} \bar{{X}} = {media_bg:.3f} \text{{ eV}}, \quad \text{{Mediana: }} \tilde{{X}} = {mediana_bg:.3f} \text{{ eV}}"))
display(Math(fr"\text{{Desviación Estándar: }} s = {std_bg:.3f} \text{{ eV}}, \quad \text{{Asimetría (Skewness): }} {skewness_bg:.3f}"))

## 3. Visualización Exploratoria Combinada: Histograma KDE + Boxplot
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

## Histograma con curva KDE por Fórmula de Material
sns.histplot(data=df_mp, x="band_gap", hue="formula", kde=True, element="step", ax=axes[0], palette="Set1")
axes[0].set_title("Distribución de Band Gap por Material (Materials Project)", fontsize=11, fontweight="bold")
axes[0].set_xlabel("Band Gap (eV)")
axes[0].set_ylabel("Frecuencia")

## Q-Q Plot de Normalidad
stats.probplot(band_gap_data, dist="norm", plot=axes[1])
axes[1].set_title("Q-Q Plot de Band Gap vs Distribución Normal", fontsize=11, fontweight="bold")

plt.tight_layout()
plt.show()
```

---

## 9. Verificación Simbólica y Expresión Formal con SymPy

En el análisis estadístico descriptivo, las fórmulas de los momentos muéstrales se derivan de forma analítica exacta utilizando computación simbólica en **SymPy**.

### 9.1 Expresión Simbólica de la Media Muestral ($\bar{X}$) y Varianza ($S^2$)

La media muestral $\bar{X}$ se define axiomáticamente como:
$$\boxed{\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i}$$

```python
import sympy as sp
from IPython.display import display, Math

## Definición de variables simbólicas
n = sp.Symbol('n', positive=True, integer=True)
x = sp.IndexedBase('x')
i = sp.Symbol('i', integer=True)

## Expresión simbólica de la media muestral
media_simbolica = (1/n) * sp.Sum(x[i], (i, 1, n))

## Expresión simbólica de la varianza muestral sesgada e imparcial (n-1)
varianza_simbolica = (1/(n - 1)) * sp.Sum((x[i] - media_simbolica)**2, (i, 1, n))

display(Math(fr"\text{{Fórmula Simbólica de la Media Muestral }} \bar{{X}}: {sp.latex(media_simbolica)}"))
display(Math(fr"\text{{Fórmula Simbólica de la Varianza Muestral }} S^2: {sp.latex(varianza_simbolica)}"))
```
