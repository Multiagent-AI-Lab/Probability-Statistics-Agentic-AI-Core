"""
Script para reconstruir con pureza 100% Python/SciPy las lecciones U3 y U5,
eliminando todas las funciones de R (dbinom, dgeom, dpois, dnorm, etc.) y estructurando
impecablemente los encabezados H2 (1..10) y H3 (X.Y).
"""

import os

# --- CONSTRUCCIÓN DE UNIDAD 3: VARIABLES ALEATORIAS DISCRETAS ---
u3_content = r"""# UNIDAD 3: Variables Aleatorias Discretas y Distribuciones de Probabilidad
## Asignatura: Probabilidad y Estadística Inferencial
### UCEMICH — Ingeniería en IA y Nanotecnología
### Autor y Profesor: Mtro. Luis José Yudico Anaya

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

### Contexto Aplicado en Nanotecnología
En una sala limpia de fabricación de nano-sensores piezoresistivos para dispositivos médicos implantables, la probabilidad de que una unidad presente una micro-grieta estructural en el diafragma de silicio durante la etapa de grabado químico es $p = 0.05$. Un ingeniero en control de calidad selecciona una muestra aleatoria de $n = 20$ nano-sensores del lote de producción diaria.

Determine:
1. La probabilidad exacta de encontrar exactamente 2 nano-sensores defectuosos en la muestra.
2. La probabilidad de encontrar al menos 1 nano-sensor defectuoso.
3. El número esperado y la desviación estándar de nano-sensores defectuosos.

### Paso 1: Identificación del Modelo y Parámetros
El conteo de nano-sensores defectuosos en $n=20$ ensayos independientes con $p=0.05$ sigue una distribución Binomial:
$$X \sim \text{Binomial}(n = 20, p = 0.05)$$

### Paso 2: Cálculo de $P(X = 2)$
$$P(X = 2) = \binom{20}{2} (0.05)^2 (0.95)^{18}$$
$$\binom{20}{2} = \frac{20 \times 19}{2} = 190$$
$$(0.05)^2 = 0.0025, \quad (0.95)^{18} \approx 0.397214$$
$$\boxed{P(X = 2) = 190 \times 0.0025 \times 0.397214 \approx 0.18868 \quad (18.87\%)}$$

### Paso 3: Cálculo de $P(X \ge 1)$ por Complemento
$$P(X \ge 1) = 1 - P(X = 0) = 1 - \binom{20}{0} (0.05)^0 (0.95)^{20}$$
$$(0.95)^{20} \approx 0.358486$$
$$\boxed{P(X \ge 1) = 1 - 0.358486 = 0.64151 \quad (64.15\%)}$$

### Paso 4: Esperanza y Desviación Estándar
$$\mathbb{E}[X] = n p = 20 \times 0.05 = \boxed{1.0 \text{ nano-sensor}}$$
$$\text{Var}(X) = n p (1-p) = 20 \times 0.05 \times 0.95 = 0.95 \implies \sigma = \sqrt{0.95} \approx \boxed{0.9747\text{ nano-sensores}}$$

---

## 4. Código de Verificación Simbólica (SymPy)

```python
import sympy as sp
from IPython.display import display, Math

# 1. Definición de símbolos
n = sp.Symbol('n', positive=True, integer=True)
k = sp.Symbol('k', integer=True)
p = sp.Symbol('p', positive=True)

# 2. Expresión simbólica de la PMF Binomial y Esperanza
pmf_binomial = sp.binomial(n, k) * (p**k) * ((1 - p)**(n - k))
esperanza_expr = sp.Sum(k * pmf_binomial, (k, 0, n))

display(Math(fr"\text{{PMF Binomial Simbólica: }} P(X = k) = {sp.latex(pmf_binomial)}"))

# 3. Sustitución de los parámetros de la inspección nanotecnológica (n=20, p=0.05, k=2)
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

# Configuración visual profesional
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 5)

# --- PARTE A: Cálculo Exacto con scipy.stats.binom ---
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

# --- PARTE B: Comparación de Familias Discretas (Binomial vs Poisson vs Geométrica) ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Gráfico 1: PMF de Binomial n=20, p=0.05
k_range = np.arange(0, 8)
pmf_vals = stats.binom.pmf(k_range, n=n_val, p=p_val)

axes[0].bar(k_range, pmf_vals, color='royalblue', alpha=0.85, edgecolor='black', width=0.5)
axes[0].axvline(x=1.0, color='red', linestyle='--', label='Esperanza E[X] = 1.0')
axes[0].set_title("PMF Binomial (n=20, p=0.05): Defectos en Nano-sensores", fontsize=12, fontweight="bold")
axes[0].set_xlabel("Número de Nano-sensores Defectuosos (k)")
axes[0].set_ylabel("Probabilidad P(X = k)")
axes[0].legend()

# Gráfico 2: Simulación de Distribución Geométrica (Ensayos hasta primer defecto)
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
"""

with open('lecciones/UNIDAD_3_VARIABLES_ALEATORIAS_DISCRETAS.md', 'w', encoding='utf-8') as f:
    f.write(u3_content)

print("UNIDAD_3_VARIABLES_ALEATORIAS_DISCRETAS.md reconstruida con pureza 100% Python!")


# --- CONSTRUCCIÓN DE UNIDAD 5: VARIABLES ALEATORIAS CONTINUAS ---
u5_content = r"""# UNIDAD 5: Variables Aleatorias Continuas y Distribuciones de Probabilidad
## Asignatura: Probabilidad y Estadística Inferencial
### UCEMICH — Ingeniería en IA y Nanotecnología
### Autor y Profesor: Mtro. Luis José Yudico Anaya

---

## 1. Fundamentación Teórica y Conceptos Clave

Una **Variable Aleatoria Continua (VAC)** es una función $X: \Omega \rightarrow \mathbb{R}$ cuyo rango de valores posibles $R_X$ es un intervalo continuo no numerable de números reales (por ejemplo, el tiempo de vida de un nanotransistor, la conductividad eléctrica de un nanotubo de carbono o el diámetro de una partícula coloidal).

### 1.1 Función de Densidad de Probabilidad (PDF) y Propiedades
A diferencia de las variables discretas, para una VAC la probabilidad puntual en cualquier valor exacto es cero ($P(X = x) = 0$). La probabilidad se define sobre intervalos a través de la **Función de Densidad de Probabilidad (PDF)** $f_X(x)$, la cual satisface los dos axiomas universales:

1. **No Negatividad**: $f_X(x) \ge 0$ para todo $x \in \mathbb{R}$.
2. **Normalización del Área**:
   $$\int_{-\infty}^{+\infty} f_X(x) dx = 1$$

La probabilidad de que $X$ caiga dentro del intervalo $[a, b]$ es el área bajo la curva de la PDF:
$$P(a \le X \le b) = \int_a^b f_X(x) dx$$

### 1.2 Función de Distribución Acumulada (CDF)
La **Función de Distribución Acumulada (CDF)** $F_X(x)$ acumula la densidad desde $-\infty$ hasta $x$:

$$F_X(x) = P(X \le x) = \int_{-\infty}^x f_X(t) dt$$

Por el Teorema Fundamental del Cálculo, si $f_X(x)$ es continua:
$$f_X(x) = \frac{d}{dx} F_X(x)$$

### 1.3 Valor Esperado, Varianza y Momentos Continuos
* **Valor Esperado (Media)**:
  $$\mathbb{E}[X] = \mu = \int_{-\infty}^{+\infty} x \cdot f_X(x) dx$$
* **Varianza**:
  $$\text{Var}(X) = \sigma^2 = \int_{-\infty}^{+\infty} (x - \mu)^2 f_X(x) dx = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$$

---

## 2. Familias Principales de Distribuciones Continuas

### 2.1 Distribución Uniforme Continua ($X \sim \text{Uniforme}(a, b)$)
Densidad constante en el intervalo $[a, b]$.
* PDF: $f(x) = \frac{1}{b-a}$ para $x \in [a, b]$.
* Esperanza: $\mathbb{E}[X] = \frac{a+b}{2}$, Varianza: $\text{Var}(X) = \frac{(b-a)^2}{12}$.

### 2.2 Distribución Normal o Gaussiana ($X \sim \mathcal{N}(\mu, \sigma^2)$)
La distribución más importante en ciencias e ingeniería por el Teorema del Límite Central.
* PDF:
  $$f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{1}{2} \left(\frac{x - \mu}{\sigma}\right)^2 \right), \quad x \in \mathbb{R}$$
* Estándar $\mathcal{N}(0, 1)$ mediante la transformación $Z = \frac{X - \mu}{\sigma}$.

### 2.3 Distribución Exponencial ($X \sim \text{Exponencial}(\lambda)$)
Modela el tiempo continuo entre eventos estocásticos Poisson independientes.
* PDF: $f(x) = \lambda e^{-\lambda x}$ para $x \ge 0$.
* CDF: $F(x) = 1 - e^{-\lambda x}$.
* Esperanza: $\mathbb{E}[X] = \frac{1}{\lambda}$, Varianza: $\text{Var}(X) = \frac{1}{\lambda^2}$.
* Propiedad de **Falta de Memoria**: $P(X > s + t | X > s) = P(X > t)$.

### 2.4 Distribución Gamma ($X \sim \text{Gamma}(k, \theta)$)
Generalización de la distribución exponencial para el tiempo hasta observar $k$ eventos.
* PDF: $f(x) = \frac{x^{k-1} e^{-x/\theta}}{\theta^k \Gamma(k)}$ para $x > 0$.

### 2.5 Distribución de Weibull ($X \sim \text{Weibull}(k, \lambda)$)
Ampliamente utilizada en ingeniería de materiales y confiabilidad para describir el tiempo de falla y resistencia a la rotura.
* PDF: $f(x) = \frac{k}{\lambda} \left(\frac{x}{\lambda}\right)^{k-1} \exp\left(-\left(\frac{x}{\lambda}\right)^k\right)$ para $x \ge 0$.

---

## 3. Ejemplo Analítico Paso a Paso: Espesor de Películas Delgadas en Litografía Nanométrica

### Contexto Aplicado en Nanotecnología
En la fabricación de transistores de efecto de campo de grafeno (GFETs), el espesor de la capa dieléctrica de dióxido de hafnio ($\text{HfO}_2$) depositada por capa atómica (ALD) sigue una distribución Normal con media $\mu = 8.5\text{ nm}$ y desviación estándar $\sigma = 0.4\text{ nm}$.

Para asegurar un rendimiento dieléctrico adecuado sin riesgo de tunelamiento cuántico indebido, el espesor debe estar comprendido entre $7.9\text{ nm}$ y $9.1\text{ nm}$.

Determine:
1. La probabilidad de que una oblea de silicio procesada tenga un espesor dentro del rango de tolerancia especificado.
2. El cota de espesor $x_{0.95}$ correspondiente al percentil $95\%$ de la producción.

### Paso 1: Estandarización a la Variable Normal Estándar $Z$
$$Z = \frac{X - \mu}{\sigma} = \frac{X - 8.5}{0.4}$$

Para el límite inferior $x_1 = 7.9\text{ nm}$:
$$z_1 = \frac{7.9 - 8.5}{0.4} = \frac{-0.6}{0.4} = -1.50$$

Para el límite superior $x_2 = 9.1\text{ nm}$:
$$z_2 = \frac{9.1 - 8.5}{0.4} = \frac{0.6}{0.4} = +1.50$$

### Paso 2: Cálculo de Probabilidad $P(7.9 \le X \le 9.1)$
$$P(7.9 \le X \le 9.1) = P(-1.50 \le Z \le +1.50) = \Phi(1.50) - \Phi(-1.50)$$

Consultando la CDF normal estándar $\Phi(1.50) \approx 0.93319$:
$$\Phi(-1.50) = 1 - \Phi(1.50) \approx 1 - 0.93319 = 0.06681$$
$$P(7.9 \le X \le 9.1) = 0.93319 - 0.06681 = \boxed{0.86638 \quad (86.64\%)}$$

### Paso 3: Cálculo del Percentil $95\%$ ($x_{0.95}$)
Buscamos $z_{0.95}$ tal que $\Phi(z_{0.95}) = 0.95 \implies z_{0.95} \approx 1.64485$.
Desestandarizando:
$$\boxed{x_{0.95} = \mu + z_{0.95} \cdot \sigma = 8.5 + (1.64485 \times 0.4) = 8.5 + 0.65794 = 9.1579\text{ nm}}$$

---

## 4. Código de Verificación Simbólica (SymPy)

```python
import sympy as sp
from IPython.display import display, Math

# 1. Definición de símbolos
x = sp.Symbol('x', real=True)
mu = sp.Symbol('mu', real=True)
sigma = sp.Symbol('sigma', positive=True)

# 2. Expresión simbólica de la PDF Normal
pdf_normal = (1 / (sigma * sp.sqrt(2 * sp.pi))) * sp.exp(-((x - mu)**2) / (2 * sigma**2))

display(Math(fr"\text{{PDF Normal Simbólica: }} f(x) = {sp.latex(pdf_normal)}"))

# 3. Integración simbólica para calcular la probabilidad del rango [7.9, 9.1]
prob_integrada = sp.integrate(pdf_normal.subs({mu: 8.5, sigma: 0.4}), (x, 7.9, 9.1))
prob_float = float(prob_integrada.evalf())

display(Math(fr"\text{{Probabilidad Integrada }} P(7.9 \le X \le 9.1): \boxed{{{prob_float:.5f}}}"))
```

---

## 5. Solución Computacional en Python (SciPy & Statsmodels)

```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración gráfica
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 5)

# --- PARTE A: Evaluación de la Distribución Normal ---
mu_val = 8.5
sigma_val = 0.4

prob_rango = stats.norm.cdf(9.1, loc=mu_val, scale=sigma_val) - stats.norm.cdf(7.9, loc=mu_val, scale=sigma_val)
percentil_95 = stats.norm.ppf(0.95, loc=mu_val, scale=sigma_val)

print("--- EVALUACIÓN EN SCI PY STATS (NORMAL) ---")
print(f"P(7.9 <= X <= 9.1):           {prob_rango:.5f}")
print(f"Percentil 95% (Espesor):      {percentil_95:.4f} nm")

# --- PARTE B: Visualización Profesional de la Densidad ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Gráfico 1: PDF de Espesor HfO2 con región sombreada de tolerancia
x_axis = np.linspace(7.0, 10.0, 500)
pdf_vals = stats.norm.pdf(x_axis, loc=mu_val, scale=sigma_val)

axes[0].plot(x_axis, pdf_vals, color='navy', lw=2.5, label='PDF Normal (μ=8.5, σ=0.4)')
x_fill = np.linspace(7.9, 9.1, 200)
axes[0].fill_between(x_fill, stats.norm.pdf(x_fill, loc=mu_val, scale=sigma_val), color='lightgreen', alpha=0.6, label='Tolerancia (86.64%)')
axes[0].axvline(x=mu_val, color='red', linestyle='--', label='Media μ = 8.5 nm')
axes[0].set_title("Distribución de Espesor en Litografía HfO2", fontsize=12, fontweight="bold")
axes[0].set_xlabel("Espesor de Capa (nm)")
axes[0].set_ylabel("Densidad de Probabilidad f(x)")
axes[0].legend()

# Gráfico 2: Comparación de Densidades Continuas (Normal vs Exponencial vs Weibull)
exp_samples = stats.expon.rvs(scale=8.5, size=50_000, random_state=42)
weib_samples = stats.weibull_min.rvs(c=2.5, scale=8.5, size=50_000, random_state=42)

sns.kdeplot(exp_samples, color='crimson', lw=2, label='Exponencial (λ=1/8.5)', ax=axes[1])
sns.kdeplot(weib_samples, color='darkorange', lw=2, label='Weibull (k=2.5, λ=8.5)', ax=axes[1])
axes[1].set_title("Comparación de Modelos Continuos en Confiabilidad", fontsize=12, fontweight="bold")
axes[1].set_xlabel("Valor de la Variable Continuada")
axes[1].set_ylabel("Densidad de Kernel (KDE)")
axes[1].set_xlim(0, 25)
axes[1].legend()

plt.tight_layout()
plt.show()
```

---

## 6. Interpretación Post-Gráfico & Diccionario de Variables

### 6.1 Interpretación de Resultados Computacionales
1. **Conformidad de Proceso Litográfico**: El $86.64\%$ del lote de obleas cumple con la especificación de tolerancia ($7.9 - 9.1\text{ nm}$). El percentil $95\%$ se ubica en $9.1579\text{ nm}$, indicando que menos del $5\%$ de la producción supera esa cota máxima de espesor.
2. **Modelado de Fallas**: El gráfico comparativo resalta las diferencias entre distribuciones continuas: la Exponencial posee una tasa de falla constante (falta de memoria), mientras que la Weibull con $k=2.5$ caracteriza el envejecimiento por fatiga de materiales nanotecnológicos.

### 6.2 Diccionario de Variables Nanotecnológicas
* $X$: Espesor continuo de la capa dieléctrica $\text{HfO}_2$ ($\text{nm}$).
* $\mu$: Espesor medio poblacional ($\mu = 8.5\text{ nm}$).
* $\sigma$: Desviación estándar de deposición por capa atómica ($\sigma = 0.4\text{ nm}$).
* $Z$: Variable aleatoria normal estándar estandarizada $Z \sim \mathcal{N}(0, 1)$.
* $\Phi(z)$: Función de distribución acumulada de la normal estándar.
"""

with open('lecciones/UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.md', 'w', encoding='utf-8') as f:
    f.write(u5_content)

print("UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.md reconstruida con pureza 100% Python!")
