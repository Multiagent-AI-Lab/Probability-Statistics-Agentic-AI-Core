# UNIDAD 3: Variables Aleatorias Discretas y Distribuciones de Probabilidad

**Duración:** 2 semanas (12 horas)

**Curso:** Probabilidad y Estadística Inferencial

**Institución:** Universidad de la Ciénega del Estado de Michoacán de Ocampo (UCEMICH)

**Profesor:** Luis José Yudico Anaya

**Carrera:** Ingeniería en Nanotecnología

**Nivel:** Tercer Semestre

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Multiagent-AI-Lab/Probability-Statistics-Agentic-AI-Core/blob/master/notebooks/UNIDAD_3_VARIABLES_ALEATORIAS_DISCRETAS.ipynb)

```python
import os
import sys

if 'google.colab' in sys.modules:
    repo_dir = "Probability-Statistics-Agentic-AI-Core"
    if not os.path.exists(repo_dir):
        !git clone -q https://github.com/Multiagent-AI-Lab/{repo_dir}.git
    os.chdir(repo_dir)
    %pip install -q -r requirements.txt
```

---

## Prerequisitos de esta unidad

- **Teorema de Bayes y Probabilidad Condicional** (Unidad 2) — se reutiliza al interpretar la PMF de una variable aleatoria condicionada a un evento observado.

---

## 1. Fundamentación Teórica y Conceptos Clave

En la teoría de la probabilidad y la ingeniería, una **Variable Aleatoria Discreta (VAD)** es una función determinista $X: \Omega \rightarrow \mathbb{R}$ que asigna un valor real a cada resultado de un espacio muestral $\Omega$, de modo que el rango de valores $R_X = \{x_1, x_2, x_3, \dots\}$ es un conjunto finito o infinito contable.

### 1.1 Función de Masa de Probabilidad (PMF) y Propiedades
La **Función de Masa de Probabilidad (PMF)** $p_X(x) = P(X = x)$ especifica la probabilidad exacta de que la variable aleatoria tome el valor $x$. Toda PMF válida satisface dos propiedades axiomáticas:

1. **No Negatividad**: $p_X(x) \ge 0$ para todo $x \in R_X$.
2. **Normalización Total**:
   $$\sum_{x \in R_X} p_X(x) = 1$$

### 1.2 Función de Distribución Acumulada (CDF)
La **Función de Distribución Acumulada (CDF)** $F_X(x)$ se define como la probabilidad de que $X$ tome un valor menor o igual a $x$:

$$F_X(x) = P(X \le x) = \sum_{x_k \le x} p_X(x_k)$$

Propiedades clave de la CDF discreta:
* Es una función escalonada (discontinua a la derecha), con saltos de altura $p_X(x_k)$ en cada valor soporte $x_k$.
* $\lim_{x \to -\infty} F_X(x) = 0$ y $\lim_{x \to +\infty} F_X(x) = 1$.
* Cálculo de probabilidad de intervalos: $P(a < X \le b) = F_X(b) - F_X(a)$.

### 1.3 Valor Esperado ($\mathbb{E}[X]$), Varianza ($\text{Var}(X)$) y Momentos
* **Valor Esperado (Media)**:
  $$\mathbb{E}[X] = \mu = \sum_{x \in R_X} x \cdot p_X(x)$$
* **Varianza**:
  $$\text{Var}(X) = \sigma^2 = \mathbb{E}[(X - \mu)^2] = \sum_{x \in R_X} (x - \mu)^2 p_X(x) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$$
* **Desviación Estándar**: $\sigma = \sqrt{\text{Var}(X)}$.

---

## 2. Familias Principales de Distribuciones Discretas

### 2.1 Distribución Bernoulli ($X \sim \text{Bernoulli}(p)$)
Modela un único ensayo aleatorio binario con probabilidad de éxito $p$ ($X=1$) y fracaso $q = 1-p$ ($X=0$).
* PMF: $P(X = x) = p^x (1-p)^{1-x}, \quad x \in \{0, 1\}$.
* Esperanza: $\mathbb{E}[X] = p$, Varianza: $\text{Var}(X) = p(1-p)$.

### 2.2 Distribución Binomial ($X \sim \text{Binomial}(n, p)$)
Número de éxitos en $n$ ensayos independientes e idénticamente distribuidos de Bernoulli.
* PMF:
  $$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k \in \{0, 1, 2, \dots, n\}$$
* Esperanza: $\mathbb{E}[X] = n p$, Varianza: $\text{Var}(X) = n p (1-p)$.

### 2.3 Distribución de Poisson ($X \sim \text{Poisson}(\lambda)$)
Modela la ocurrencia de eventos raros en un intervalo continuo de tiempo o espacio, con tasa media $\lambda > 0$.
* PMF:
  $$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k \in \{0, 1, 2, \dots\}$$
* Esperanza: $\mathbb{E}[X] = \lambda$, Varianza: $\text{Var}(X) = \lambda$.

### 2.4 Distribución Geométrica ($X \sim \text{Geométrica}(p)$)
Número de ensayos independientes de Bernoulli hasta obtener el **primer éxito**.
* PMF: $P(X = k) = (1-p)^{k-1} p, \quad k \in \{1, 2, 3, \dots\}$.
* Esperanza: $\mathbb{E}[X] = \frac{1}{p}$, Varianza: $\text{Var}(X) = \frac{1-p}{p^2}$.

### 2.5 Distribución Binomial Negativa ($X \sim \text{BinomialNegativa}(r, p)$)
Número de fracasos $k$ antes de observar el $r$-ésimo éxito.
* PMF:
  $$P(K = k) = \binom{k + r - 1}{k} p^r (1-p)^k, \quad k \in \{0, 1, 2, \dots\}$$
* Esperanza: $\mathbb{E}[K] = \frac{r(1-p)}{p}$, Varianza: $\text{Var}(K) = \frac{r(1-p)}{p^2}$.

### 2.6 Distribución Hipergeométrica ($X \sim \text{Hipergeométrica}(N, K, n)$)
Muestreo **sin reemplazo** de una población finita $N$ que contiene $K$ elementos con la característica deseada.
* PMF:
  $$P(X = k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}}$$

### 2.7 Distribución Uniforme Discreta ($X \sim \text{Uniforme}\{1,\dots,k\}$)
Modela un experimento donde cada uno de $k$ resultados posibles tiene exactamente la misma probabilidad de ocurrir.
* PMF: $P(X = x_i) = \dfrac{1}{k}, \quad x_i \in \{1, 2, \dots, k\}$.
* Esperanza: $\mathbb{E}[X] = \dfrac{k+1}{2}$, Varianza: $\text{Var}(X) = \dfrac{k^2-1}{12}$.

### 2.8 Distribución Multinomial ($X_1,\dots,X_k \sim \text{Multinomial}(n, p_1,\dots,p_k)$)
Generaliza la distribución Binomial a experimentos con más de dos resultados posibles por ensayo.
* PMF: $P(X_1=k_1,\dots,X_k=k_k) = \dfrac{n!}{k_1!\,k_2!\cdots k_k!}\, p_1^{k_1} p_2^{k_2} \cdots p_k^{k_k}$, con $\sum_i k_i = n$.
* Esperanza por componente: $\mathbb{E}[X_i] = np_i$, Desviación estándar: $\sigma_i = \sqrt{np_i(1-p_i)}$.

### 2.9 Profundización: PMF Completa, CDF y Aplicaciones por Dominio

Las subsecciones 2.1 a 2.8 dan la definición mínima de cada familia. Esta subsección profundiza las 8 distribuciones discretas del curso con su CDF explícita, código de comparación gráfica en `scipy.stats`, y ejemplos de uso concretos en **Nanotecnología**, **Inteligencia Artificial** y **Diseño de Experimentos (DOE)**.

#### 2.9.1 Distribución Bernoulli — Profundización

* **CDF**: $F(x) = 0$ si $x<0$; $F(x) = 1-p$ si $0\le x<1$; $F(x)=1$ si $x\ge 1$.
* Caso especial de la Binomial con $n=1$: `scipy.stats.bernoulli` es un atajo de `binom(n=1, p)`.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

## PMF de Bernoulli: probabilidad de que un nanosensor individual
## detecte correctamente un analito en una sola prueba (p=0.7)
p = 0.7
dist = bernoulli(p)
valores = [0, 1]
probabilidades = dist.pmf(valores)

plt.figure(figsize=(6, 4))
plt.bar(valores, probabilidades, color=["lightcoral", "skyblue"], edgecolor="black")
plt.xticks(valores, ["0 (fallo)", "1 (éxito)"])
plt.title(f"PMF Bernoulli(p={p})")
plt.ylabel("Probabilidad")
plt.ylim(0, 1)
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: resultado binario de una sola prueba de control de calidad sobre un nanodispositivo (pasa/no pasa la especificación de espesor). (2) *IA*: unidad básica de clasificación binaria — la salida de una neurona con activación sigmoide seguida de umbral se modela como Bernoulli con $p$ igual a la probabilidad predicha. (3) *DOE*: resultado de un único ensayo experimental con dos desenlaces posibles (p. ej., una réplica de síntesis produce o no el polimorfo deseado).

#### 2.9.2 Distribución Binomial — Profundización

* **CDF**: $F(x) = P(X\le x) = \sum_{i=0}^{\lfloor x\rfloor} \binom{n}{i}p^i(1-p)^{n-i}$.
* Suma de $n$ Bernoulli($p$) independientes: modela el conteo total de éxitos en un número fijo de ensayos idénticos.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

## PMF Binomial: numero de nanoparticulas defectuosas en un lote de
## n=20 con probabilidad de defecto p=0.05 por particula
n, p = 20, 0.05
dist = binom(n, p)
k = np.arange(0, n + 1)

plt.figure(figsize=(8, 5))
plt.bar(k, dist.pmf(k), color="steelblue", edgecolor="black")
plt.title(f"PMF Binomial(n={n}, p={p})")
plt.xlabel("Número de defectos (k)")
plt.ylabel("Probabilidad")
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: número de nanopartículas defectuosas en un lote de tamaño fijo bajo una tasa de defecto constante por partícula — control de calidad de síntesis. (2) *IA*: número de predicciones correctas de un clasificador binario sobre un conjunto de prueba de tamaño fijo, bajo el supuesto de accuracy constante; fundamento del intervalo de confianza binomial para accuracy reportada. (3) *DOE*: número de réplicas exitosas de un experimento (p. ej., síntesis que alcanza la pureza objetivo) de un total de $n$ réplicas planeadas, para dimensionar el tamaño de muestra necesario.

#### 2.9.3 Distribución de Poisson — Profundización

* **CDF**: $F(x) = P(X\le x) = \sum_{i=0}^{\lfloor x\rfloor} \dfrac{\lambda^i e^{-\lambda}}{i!}$.
* Límite de la Binomial cuando $n\to\infty$, $p\to 0$ con $np=\lambda$ constante — modela conteos raros en un intervalo continuo de tiempo o espacio.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

## PMF Poisson: numero de fallas de un nano-dispositivo por cada
## 1000 horas de operacion, con tasa promedio lambda=4
lam = 4
dist = poisson(lam)
k = np.arange(0, 16)

plt.figure(figsize=(8, 5))
plt.bar(k, dist.pmf(k), color="darkorange", edgecolor="black")
plt.title(f"PMF Poisson($\\lambda$={lam})")
plt.xlabel("Número de eventos (k)")
plt.ylabel("Probabilidad")
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: número de fallas de un nano-dispositivo por unidad de tiempo de operación, o número de defectos puntuales por unidad de área en una película delgada. (2) *IA*: número de solicitudes que llega a un servidor de inferencia por unidad de tiempo, modelo base para dimensionar la capacidad de un sistema de predicción en producción. (3) *DOE*: número de eventos raros observados en un experimento de conteo (p. ej., número de núcleos de cristalización espontánea por unidad de volumen), fundamento de las pruebas de bondad de ajuste para procesos de conteo.

#### 2.9.4 Distribución Geométrica — Profundización

* **CDF**: $F(x) = P(X\le x) = 1-(1-p)^{\lfloor x\rfloor}$.
* Modela el número de ensayos Bernoulli($p$) independientes hasta (e incluyendo) el primer éxito; análogo discreto de la propiedad de falta de memoria de la Exponencial.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom

## PMF Geometrica: numero de intentos de sintesis hasta obtener el
## primer lote de nanoparticulas dentro de especificacion (p=0.3)
p = 0.3
dist = geom(p)
k = np.arange(1, 15)

plt.figure(figsize=(8, 5))
plt.bar(k, dist.pmf(k), color="seagreen", edgecolor="black")
plt.title(f"PMF Geométrica(p={p})")
plt.xlabel("Número de ensayos hasta el primer éxito (k)")
plt.ylabel("Probabilidad")
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: número de intentos de síntesis necesarios hasta obtener el primer lote de nanopartículas dentro de especificación, útil para estimar el costo esperado de un protocolo de bajo rendimiento. (2) *IA*: número de consultas a un modelo generativo hasta obtener la primera salida que pasa un filtro de calidad, relevante en técnicas de *rejection sampling*. (3) *DOE*: número de réplicas experimentales necesarias hasta observar el primer resultado exitoso, para planear el presupuesto de un experimento secuencial.

#### 2.9.5 Distribución Binomial Negativa — Profundización

* **CDF**: sin forma cerrada simple; se evalúa numéricamente (`scipy.stats.nbinom.cdf`).
* Generaliza la Geométrica: modela el número de ensayos hasta obtener $r$ éxitos (no solo el primero). Para $r=1$ recupera la Geométrica.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nbinom

## PMF Binomial Negativa: numero de lotes de sintesis necesarios
## hasta obtener r=5 lotes dentro de especificacion (p=0.4)
r, p = 5, 0.4
dist = nbinom(r, p)
k = np.arange(0, 31)

plt.figure(figsize=(8, 5))
plt.bar(k, dist.pmf(k), color="mediumpurple", edgecolor="black")
plt.title(f"PMF Binomial Negativa(r={r}, p={p})")
plt.xlabel("Número de fallos antes del r-ésimo éxito (k)")
plt.ylabel("Probabilidad")
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: número de lotes de síntesis necesarios hasta acumular $r$ lotes dentro de especificación, para planificar la producción de un número fijo de muestras válidas. (2) *IA*: modelado de conteos con sobre-dispersión (varianza mayor que la media) en datos de conteo del mundo real, donde la Poisson resulta demasiado restrictiva — común en modelos de recuento de eventos raros con heterogeneidad. (3) *DOE*: número de réplicas experimentales necesarias hasta acumular un número objetivo de resultados exitosos, extendiendo el caso geométrico a metas de más de un éxito.

#### 2.9.6 Distribución Hipergeométrica — Profundización

* **CDF**: $F(x) = \sum_{j=0}^{\lfloor x\rfloor} \dfrac{\binom{K}{j}\binom{N-K}{n-j}}{\binom{N}{n}}$.
* A diferencia de la Binomial, modela muestreo **sin reemplazo** de una población finita — las probabilidades cambian con cada extracción.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom

## PMF Hipergeometrica: numero de nanoparticulas defectuosas al
## extraer una muestra de n=15 de un lote finito N=50 con K=10 defectuosas
N, K, n = 50, 10, 15
dist = hypergeom(N, K, n)
k = np.arange(0, min(K, n) + 1)

plt.figure(figsize=(8, 5))
plt.bar(k, dist.pmf(k), color="indianred", edgecolor="black")
plt.title(f"PMF Hipergeométrica(N={N}, K={K}, n={n})")
plt.xlabel("Número de defectuosas en la muestra (k)")
plt.ylabel("Probabilidad")
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: número de nanopartículas defectuosas al extraer una muestra de inspección de un lote finito de producción, sin reponer las unidades muestreadas — el caso realista de control de calidad destructivo. (2) *IA*: muestreo de un conjunto de datos finito (p. ej., seleccionar un subconjunto de validación sin reemplazo de un dataset fijo), relevante para el diseño de validación cruzada. (3) *DOE*: número de muestras con una característica de interés (p. ej., un lote de materia prima defectuoso) al extraer una muestra de auditoría de un envío finito, sin reposición.

#### 2.9.7 Distribución Uniforme Discreta — Profundización

* **CDF**: $F(x) = \dfrac{\lfloor x\rfloor - a + 1}{k}$ para $a\le x\le b$, con $k=b-a+1$.
* Todos los $k$ valores del rango $\{a,\dots,b\}$ son igualmente probables — es el generador discreto base para simulación por muestreo aleatorio simple.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import randint

## PMF Uniforme Discreta: seleccion aleatoria de una posicion de
## un chip de 6 sitios de reaccion en un ensayo de sintesis paralela
a, b = 1, 6
dist = randint(a, b + 1)
valores = np.arange(a, b + 1)

plt.figure(figsize=(7, 4))
plt.bar(valores, dist.pmf(valores), color="gold", edgecolor="black")
plt.title(f"PMF Uniforme Discreta en [{a}, {b}]")
plt.xlabel("Valor (x)")
plt.ylabel("Probabilidad")
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: selección aleatoria de un sitio de reacción entre $k$ posiciones equivalentes en un chip de síntesis paralela, cuando no hay razón física para preferir una posición sobre otra. (2) *IA*: asignación aleatoria uniforme de ejemplos a particiones de entrenamiento/validación cuando se desea que cada partición tenga igual probabilidad de recibir cualquier ejemplo. (3) *DOE*: aleatorización del orden de corrida de los tratamientos de un experimento (randomización), un requisito metodológico estándar para evitar sesgos por efectos temporales.

#### 2.9.8 Distribución Multinomial — Profundización

* Generaliza la Binomial a $k>2$ categorías; no tiene una CDF cerrada de uso práctico — se trabaja directamente con la PMF conjunta o vía simulación.
* Cada componente marginal $X_i$ es por sí sola Binomial($n$, $p_i$), pero las componentes no son independientes entre sí (están ligadas por $\sum_i X_i = n$).

```python
import numpy as np
from scipy.stats import multinomial

## PMF Multinomial: clasificacion de n=20 nanoparticulas en 3
## categorias de tamano (pequena, mediana, grande) segun el proceso
n = 20
probabilidades = [0.2, 0.5, 0.3]
dist = multinomial(n, probabilidades)

## Probabilidad de obtener exactamente 4 pequenas, 10 medianas, 6 grandes
conteo_observado = [4, 10, 6]
prob = dist.pmf(conteo_observado)
print(f"P(4 pequeñas, 10 medianas, 6 grandes) = {prob:.4f}")

## Esperanza por categoria: E[X_i] = n * p_i
esperanza = n * np.array(probabilidades)
print(f"Esperanza por categoría: {esperanza}")
```

**Aplicaciones**: (1) *Nanotecnología*: clasificación de un lote de $n$ nanopartículas en $k$ categorías de tamaño (pequeña/mediana/grande) según las probabilidades conocidas de un proceso de síntesis sol-gel. (2) *IA*: distribución de probabilidad de salida de un clasificador multiclase (capa *softmax*) sobre $k$ categorías — la Multinomial es la distribución muestral subyacente a los conteos de predicciones correctas por clase. (3) *DOE*: resultado de un experimento con más de dos desenlaces categóricos posibles por unidad experimental (p. ej., clasificar cada muestra en "aprobada", "reprocesable" o "rechazada"), base de las pruebas de bondad de ajuste $\chi^2$ sobre datos categóricos.

---

## 3. Ejemplo Analítico Paso a Paso: Inspección Nanotecnológica de Micro-sensores

### 3.1 Contexto Aplicado en Nanotecnología
En una sala limpia de fabricación de nano-sensores piezoresistivos para dispositivos médicos implantables, la probabilidad de que una unidad presente una micro-grieta estructural en el diafragma de silicio durante la etapa de grabado químico es $p = 0.05$. Un ingeniero en control de calidad selecciona una muestra aleatoria de $n = 20$ nano-sensores del lote de producción diaria.

Determine:
1. La probabilidad exacta de encontrar exactamente 2 nano-sensores defectuosos en la muestra.
2. La probabilidad de encontrar al menos 1 nano-sensor defectuoso.
3. El número esperado y la desviación estándar de nano-sensores defectuosos.

### 3.2 Paso 1: Identificación del Modelo y Parámetros
El conteo de nano-sensores defectuosos en $n=20$ ensayos independientes con $p=0.05$ sigue una distribución Binomial:
$$X \sim \text{Binomial}(n = 20, p = 0.05)$$

### 3.3 Paso 2: Cálculo de $P(X = 2)$
$$P(X = 2) = \binom{20}{2} (0.05)^2 (0.95)^{18}$$
$$\binom{20}{2} = \frac{20 \times 19}{2} = 190$$
$$(0.05)^2 = 0.0025, \quad (0.95)^{18} \approx 0.397214$$
$$\boxed{P(X = 2) = 190 \times 0.0025 \times 0.397214 \approx 0.18868 \quad (18.87\%)}$$

### 3.4 Paso 3: Cálculo de $P(X \ge 1)$ por Complemento
$$P(X \ge 1) = 1 - P(X = 0) = 1 - \binom{20}{0} (0.05)^0 (0.95)^{20}$$
$$(0.95)^{20} \approx 0.358486$$
$$\boxed{P(X \ge 1) = 1 - 0.358486 = 0.64151 \quad (64.15\%)}$$

### 3.5 Paso 4: Esperanza y Desviación Estándar
$$\mathbb{E}[X] = n p = 20 \times 0.05 = \boxed{1.0 \text{ nano-sensor}}$$
$$\text{Var}(X) = n p (1-p) = 20 \times 0.05 \times 0.95 = 0.95 \implies \sigma = \sqrt{0.95} \approx \boxed{0.9747\text{ nano-sensores}}$$

### 3.6 Prueba Unitaria con pytest

Se contrasta cada resultado derivado a mano (combinatoria + PMF Binomial) contra `scipy.stats.binom`, que calcula la misma fórmula sin riesgo de error aritmético humano:

```python
import ipytest
import pytest
from scipy.stats import binom

ipytest.autoconfig()

n, p = 20, 0.05


def test_probabilidad_de_exactamente_2_defectuosos():
    assert binom.pmf(2, n, p) == pytest.approx(0.18868, rel=1e-3)


def test_probabilidad_de_al_menos_1_defectuoso_por_complemento():
    prob_al_menos_uno = 1 - binom.pmf(0, n, p)
    assert prob_al_menos_uno == pytest.approx(0.64151, rel=1e-3)


def test_esperanza_y_varianza_binomial():
    assert n * p == pytest.approx(1.0)
    assert n * p * (1 - p) == pytest.approx(0.95)


ipytest.run("-vv")
```

---

## 4. Código de Verificación Simbólica (SymPy)

```python
import sympy as sp
from IPython.display import display, Math

## 1. Definición de símbolos
n = sp.Symbol('n', positive=True, integer=True)
k = sp.Symbol('k', integer=True)
p = sp.Symbol('p', positive=True)

## 2. Expresión simbólica de la PMF Binomial y Esperanza
pmf_binomial = sp.binomial(n, k) * (p**k) * ((1 - p)**(n - k))
esperanza_expr = sp.Sum(k * pmf_binomial, (k, 0, n))

display(Math(fr"\text{{PMF Binomial Simbólica: }} P(X = k) = {sp.latex(pmf_binomial)}"))

## 3. Sustitución de los parámetros de la inspección nanotecnológica (n=20, p=0.05, k=2)
valores = {n: 20, p: sp.Rational(5, 100), k: 2}
prob_exacta = pmf_binomial.subs(valores)
prob_decimal = float(prob_exacta)

display(Math(fr"\text{{Resultado Exacto }} P(X=2): {sp.latex(prob_exacta)} = \boxed{{{prob_decimal:.5f}}}"))
```

---

## 5. Solución Computacional en Python (SciPy & Statsmodels)

```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

## Configuración visual profesional
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 5)

## --- PARTE A: Cálculo Exacto con scipy.stats.binom ---
n_val = 20
p_val = 0.05

pmf_k2 = stats.binom.pmf(k=2, n=n_val, p=p_val)
cdf_k0 = stats.binom.cdf(k=0, n=n_val, p=p_val)
prob_al_menos_1 = 1 - cdf_k0

print("--- RESULTADOS SCI PY STATS (BINOMIAL) ---")
print(f"P(X = 2) exacta:          {pmf_k2:.5f}")
print(f"P(X >= 1) acumulada:      {prob_al_menos_1:.5f}")
print(f"Esperanza teórica E[X]:   {stats.binom.mean(n=n_val, p=p_val):.2f}")
print(f"Desviación Estándar SD:   {stats.binom.std(n=n_val, p=p_val):.4f}")

## --- PARTE B: Comparación de Familias Discretas (Binomial vs Poisson vs Geométrica) ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

## Gráfico 1: PMF de Binomial n=20, p=0.05
k_range = np.arange(0, 8)
pmf_vals = stats.binom.pmf(k_range, n=n_val, p=p_val)

axes[0].bar(k_range, pmf_vals, color='royalblue', alpha=0.85, edgecolor='black', width=0.5)
axes[0].axvline(x=1.0, color='red', linestyle='--', label='Esperanza E[X] = 1.0')
axes[0].set_title("PMF Binomial (n=20, p=0.05): Defectos en Nano-sensores", fontsize=12, fontweight="bold")
axes[0].set_xlabel("Número de Nano-sensores Defectuosos (k)")
axes[0].set_ylabel("Probabilidad P(X = k)")
axes[0].legend()

## Gráfico 2: Simulación de Distribución Geométrica (Ensayos hasta primer defecto)
p_geom = 0.05
muestras_geom = stats.geom.rvs(p=p_geom, size=50_000, random_state=42)

sns.histplot(muestras_geom, discrete=True, stat="density", color="forestgreen", alpha=0.7, ax=axes[1])
x_geom = np.arange(1, 40)
pmf_geom_teorica = stats.geom.pmf(x_geom, p=p_geom)
axes[1].plot(x_geom, pmf_geom_teorica, 'ro-', lw=1.5, label='PMF Teórica Geométrica(p=0.05)')
axes[1].set_title("Distribución Geométrica: Inspecciones hasta el Primer Defecto", fontsize=12, fontweight="bold")
axes[1].set_xlabel("Número de Ensayo del Primer Defecto (k)")
axes[1].set_ylabel("Densidad de Frecuencia Muestral")
axes[1].legend()

plt.tight_layout()
plt.show()

## --- PARTE C: Distribución Multinomial — Clasificación de Nanopartículas por Tamaño ---
## En síntesis sol-gel de nanopartículas de óxido metálico, se clasifican en 3 categorías
## de diámetro: pequeña (<10nm), mediana (10-30nm), grande (>30nm), con probabilidades
## conocidas del proceso. Crítico para el control de calidad en nanotecnología.
from scipy.stats import multinomial

n_lote = 20
p_categorias = [0.2, 0.5, 0.3]  # P(pequeña), P(mediana), P(grande)

## Probabilidad de obtener exactamente 4 pequeñas, 10 medianas, 6 grandes
conteo_observado = [4, 10, 6]
prob_conteo = multinomial.pmf(conteo_observado, n=n_lote, p=p_categorias)
print(f"P(4 pequeñas, 10 medianas, 6 grandes) = {prob_conteo:.6f}")

## Esperanza por categoría
esperanza = [n_lote * p for p in p_categorias]
print(f"Número esperado por categoría: {esperanza}")
```

---

## 6. Interpretación Post-Gráfico & Diccionario de Variables

### 6.1 Interpretación de Resultados Computacionales
1. **Asimetría Positiva en Eventos Raros**: La PMF de la distribución binomial para $n=20, p=0.05$ exhibe una fuerte asimetría a la derecha concentrada en $k=0$ ($35.8\%$) y $k=1$ ($37.7\%$). La probabilidad de obtener más de 3 nano-sensores defectuosos es prácticamente nula ($< 1.6\%$).
2. **Comportamiento Memoria Geométrica**: La simulación de $50,000$ réplicas geométricas muestra que el número esperado de inspecciones necesarias para detectar el primer defecto es $\mathbb{E}[K] = 1/0.05 = 20$ ensayos.
3. **Clasificación Multinomial de Nanopartículas por Tamaño**: El resultado computacional de PARTE C confirma que, para un lote de $n=20$ nanopartículas sintetizadas por vía sol-gel con probabilidades de categoría $p = (0.2, 0.5, 0.3)$, el conteo esperado por categoría de diámetro es de $4$ nanopartículas pequeñas ($<10$ nm), $10$ medianas ($10$–$30$ nm) y $6$ grandes ($>30$ nm) — exactamente el escenario evaluado, lo que explica por qué su probabilidad puntual es la moda de la distribución multinomial. En control de calidad de nanomateriales, esta distribución conjunta permite estimar la probabilidad de que un lote de síntesis cumpla simultáneamente los tres rangos de tamaño objetivo, en lugar de evaluar cada categoría de forma aislada como haría una binomial marginal; esto es clave para ajustar los parámetros del proceso sol-gel (pH, temperatura, tiempo de reacción) cuando la distribución de tamaños observada se desvía de la especificación de diseño del nanomaterial.

### 6.2 Diccionario de Variables Nanotecnológicas
* $X$: Variable aleatoria discreta que representa el número de nano-sensores defectuosos.
* $n$: Tamaños del lote inspeccionado ($n=20$).
* $p$: Probabilidad individual de falla microscópica por grabado de silicio ($p=0.05$).
* $\lambda$: Tasa media de ocurrencia de defectos en procesos continuos de litografía (Poisson).
* $K$: Número de ensayos independientes hasta observar la primera falla (Geométrica).

---

## 7. Módulo de Simulación: Algoritmo de Generación Estocástica de Variables Discretas

### 7.1 Algoritmo General de Inversión por Suma Acumulada
Dada una variable aleatoria discreta $X$ con PMF $P(X = x_k) = p_k$:
1. Generar $U \sim \text{Uniforme}(0, 1)$.
2. Seleccionar el menor índice $k$ tal que $\sum_{j=1}^k p_j \ge U$.

### 7.2 Simulación Estocástica en Python de Fallas Poisson
```python
import numpy as np
import scipy.stats as stats

np.random.seed(123)
N_sim = 50_000
lam = 4.5  # Promedio de micro-defectos por oblea de silicio
muestras_poisson = stats.poisson.rvs(mu=lam, size=N_sim)

print(f"Promedio Muestral de Defectos Simulado: {np.mean(muestras_poisson):.4f} | Teórico: {lam}")
print(f"Varianza Muestral Simulada:             {np.var(muestras_poisson):.4f} | Teórica: {lam}")
```

---

## 8. Referencia Avanzada (Opcional)

Este curso (tercer semestre) trata a las variables aleatorias discretas con herramientas de cálculo elemental. Para quien desee profundizar hacia un tratamiento formal medida-teórico (variables aleatorias como funciones medibles, espacios de probabilidad abstractos), el curso de posgrado **MIT 6.436J — Fundamentals of Probability** (Prof. Yury Polyanskiy) cubre este mismo tema en sus *Lecture Notes* 4–6, con los prerrequisitos de análisis real y teoría de la medida que ese enfoque exige: [ocw.mit.edu/courses/6-436j-fundamentals-of-probability-fall-2018/pages/lecture-notes](https://ocw.mit.edu/courses/6-436j-fundamentals-of-probability-fall-2018/pages/lecture-notes/).

## Errores Comunes / Misconceptions

* **Error**: Confundir la PMF con la CDF — evaluar $P(X = k)$ cuando el problema pedía $P(X \le k)$ (o viceversa).
  **Correcto**: la PMF $p(k) = P(X=k)$ da la probabilidad de un valor puntual; la CDF $F(k) = P(X \le k) = \sum_{i \le k} p(i)$ acumula todas las probabilidades hasta $k$. Para "al menos" o "a lo más" siempre se necesita la CDF (o su complemento), no la PMF evaluada en un solo punto.

* **Error**: Asumir que la esperanza $\mathbb{E}[X]$ de una variable discreta debe coincidir con alguno de sus valores posibles.
  **Correcto**: $\mathbb{E}[X]$ es un promedio ponderado por probabilidades y puede caer entre valores posibles (p. ej. $\mathbb{E}[X] = 3.5$ para un dado justo, aunque 3.5 nunca es un resultado del lanzamiento).

* **Error**: Usar la aproximación Poisson de la Binomial ($\lambda = np$) en cualquier caso, sin verificar las condiciones de validez.
  **Correcto**: la aproximación solo es razonable cuando $n$ es grande, $p$ es pequeño y $np$ es moderado (regla práctica: $n \ge 20$ y $p \le 0.05$, o $np < 10$); fuera de ese régimen la Binomial y la Poisson difieren de forma apreciable, especialmente en las colas.

## Ejercicio Propuesto

Un lote de $n=25$ nanotubos de carbono de pared simple (SWCNT) se inspecciona por espectroscopía Raman; cada nanotubo tiene una probabilidad $p=0.08$ de presentar un defecto estructural (vacancia en la red), de forma independiente entre nanotubos: $X \sim \text{Binomial}(n=25,\ p=0.08)$.

1. Calcula, usando la fórmula exacta de la PMF binomial, $P(X = 3)$ (exactamente 3 nanotubos defectuosos).
2. Calcula $P(X \le 3)$ y $P(X \ge 1)$ (usando la CDF, no la PMF).
3. Calcula $\mathbb{E}[X]$ y $\text{Var}(X)$. Dado que $n \cdot p = 2.0$ pero $p = 0.08$ no cumple estrictamente $p \le 0.05$, calcula también la aproximación Poisson de $P(X=3)$ y compárala numéricamente con el valor exacto del punto 1 para verificar si la aproximación sigue siendo razonable en este caso límite.

Escribe tu solución en una celda de código nueva en tu notebook. La celda de autoevaluación de la siguiente sección verificará tu resultado.

## Referencias

* Unpingco, J. (2019). *Python for Probability, Statistics, and Machine Learning* (2nd ed.). Springer. Capítulos sobre variables aleatorias discretas y su implementación computacional.
* Li, Y. & Jiang, Z. (2008). An Overview of Reliability and Failure Mode Analysis of Microelectromechanical Systems (MEMS). En *Handbook of Performability Engineering*. Springer, London. https://doi.org/10.1007/978-1-84800-131-2_58 — modos de falla y análisis de confiabilidad de micro-sensores, el contexto aplicado del ejemplo analítico de esta unidad (conteo Binomial de defectos en un lote de nano-sensores).
* Virtanen, P. et al. (2020). SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. *Nature Methods*, 17, 261-272. Documentación: [docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html)

## Herramientas de esta Unidad

**StatsTutorAgent** — resuelve tus dudas conceptuales sobre variables aleatorias discretas citando el contenido exacto de esta unidad, y te hace una pregunta socrática si detecta un error conceptual común en vez de darte la respuesta directa:

```python
import os
import sys
from pathlib import Path

if 'google.colab' in sys.modules:
    from google.colab import userdata
    for nombre_secreto in ("GEMINI_API_KEY", "GOOGLE_API_KEY"):
        try:
            os.environ["GEMINI_API_KEY"] = userdata.get(nombre_secreto)
            break
        except Exception:
            continue
    else:
        print(
            "⚠️ [Unidad 3] No se encontró el secreto GEMINI_API_KEY ni GOOGLE_API_KEY en Colab. "
            "Créalo en el ícono de llave 🔑 de la barra lateral izquierda para usar StatsTutorAgent."
        )

from src.multiagent_core.stats_tutor_agent import StatsTutorAgent

tutor = StatsTutorAgent(course_dir=Path("lecciones"))
print(tutor.ask("¿cuándo debo usar la distribución binomial en vez de la de Poisson?"))
```

No requiere configuración adicional más allá de tu `GEMINI_API_KEY` (créala en [aistudio.google.com/apikey](https://aistudio.google.com/apikey) y agrégala como secreto de Colab o variable de entorno local).

## Autoevaluación

Guarda tu solución al Ejercicio Propuesto en un archivo separado y evalúala contra el pipeline de auditoría del curso:

```python
%%writefile solucion_ejercicio_u3.py
# Completa aquí tu solución al Ejercicio Propuesto de esta unidad.
import scipy.stats as stats

n = 25
p = 0.08

# TODO: calcula P(X = 3) usando la fórmula exacta de la PMF binomial (stats.binom.pmf)
# TODO: calcula P(X <= 3) y P(X >= 1) usando la CDF (stats.binom.cdf), no la PMF
# TODO: calcula E[X] y Var(X)
# TODO: calcula la aproximación Poisson de P(X=3) con lambda = n*p y compárala con el valor exacto
```

```python
from src.multiagent_core.code_auditor_agent import CodeAuditorAgent
from external_skills.pedagogy.socratic_debugger import SocraticDebugger

with open("solucion_ejercicio_u3.py", encoding="utf-8") as f:
    codigo_alumno = f.read()

auditor = CodeAuditorAgent()
resultado = auditor.audit_code(codigo_alumno)

if resultado["issues"] or resultado["metrics"]["has_security_risk"]:
    debugger = SocraticDebugger()
    for issue in resultado["issues"]:
        tipo_error = "syntax_error" if "SyntaxError" in issue else "generic"
        print("💡", debugger.generate_socratic_question(tipo_error, "Unidad 3"))
    for issue in resultado["security_issues"]:
        print("🔒", debugger.generate_socratic_question("security_risk", "Unidad 3"))
        print("   ", issue)
    print("\n--- Detalle técnico ---")
    print(resultado)
else:
    print("✅ Tu código pasa las verificaciones automáticas de estilo y seguridad.")
    print(resultado)
```

