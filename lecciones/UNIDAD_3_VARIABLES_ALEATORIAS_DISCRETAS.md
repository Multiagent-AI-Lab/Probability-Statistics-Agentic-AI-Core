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
```

---

### 5.3 PARTE C: Distribución Multinomial — Clasificación de Nanopartículas Sintetizadas por Tamaño

En aplicaciones de nanotecnología de síntesis de nanomateriales, es común clasificar nanopartículas en categorías de tamaño tras su síntesis química. En un proceso de síntesis sol-gel de nanopartículas de óxido metálico, se obtiene un lote de nanopartículas que se clasifican automáticamente en tres categorías de diámetro: pequeñas (<10 nm), medianas (10-30 nm) y grandes (>30 nm). Este tipo de clasificación multinomial es crítico para el control de calidad en nanotecnología y permite optimizar los parámetros de síntesis para obtener la distribución deseada de tamaños.

```python
## --- PARTE C: Distribución Multinomial — Clasificación de Nanopartículas por Tamaño ---
from scipy.stats import multinomial

## Un lote de n=20 nanopartículas se clasifica en 3 categorías de tamaño tras la síntesis:
## pequeña (<10nm), mediana (10-30nm), grande (>30nm), con probabilidades conocidas del proceso
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


## 6. Interpretación Post-Gráfico & Diccionario de Variables

### 6.1 Interpretación de Resultados Computacionales
1. **Asimetría Positiva en Eventos Raros**: La PMF de la distribución binomial para $n=20, p=0.05$ exhibe una fuerte asimetría a la derecha concentrada en $k=0$ ($35.8\%$) y $k=1$ ($37.7\%$). La probabilidad de obtener más de 3 nano-sensores defectuosos es prácticamente nula ($< 1.6\%$).
2. **Comportamiento Memoria Geométrica**: La simulación de $50,000$ réplicas geométricas muestra que el número esperado de inspecciones necesarias para detectar el primer defecto es $\mathbb{E}[K] = 1/0.05 = 20$ ensayos.

### 6.2 Diccionario de Variables Nanotecnológicas
* $X$: Variable aleatoria discreta que representa el número de nano-sensores defectuosos.
* $n$: Tamaños del lote inspeccionado ($n=20$).
* $p$: Probabilidad individual de falla microscópica por grabado de silicio ($p=0.05$).
* $\lambda$: Tasa media de ocurrencia de defectos en procesos continuos de litografía (Poisson).
* $K$: Número de ensayos independientes hasta observar la primera falla (Geométrica).

---

## 10. Módulo de Simulación: Algoritmo de Generación Estocástica de Variables Discretas

### 10.1 Algoritmo General de Inversión por Suma Acumulada
Dada una variable aleatoria discreta $X$ con PMF $P(X = x_k) = p_k$:
1. Generar $U \sim \text{Uniforme}(0, 1)$.
2. Seleccionar el menor índice $k$ tal que $\sum_{j=1}^k p_j \ge U$.

### 10.2 Simulación Estocástica en Python de Fallas Poisson
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

## 11. Referencia Avanzada (Opcional)

Este curso (tercer semestre) trata a las variables aleatorias discretas con herramientas de cálculo elemental. Para quien desee profundizar hacia un tratamiento formal medida-teórico (variables aleatorias como funciones medibles, espacios de probabilidad abstractos), el curso de posgrado **MIT 6.436J — Fundamentals of Probability** (Prof. Yury Polyanskiy) cubre este mismo tema en sus *Lecture Notes* 4–6, con los prerrequisitos de análisis real y teoría de la medida que ese enfoque exige: [ocw.mit.edu/courses/6-436j-fundamentals-of-probability-fall-2018/pages/lecture-notes](https://ocw.mit.edu/courses/6-436j-fundamentals-of-probability-fall-2018/pages/lecture-notes/).
