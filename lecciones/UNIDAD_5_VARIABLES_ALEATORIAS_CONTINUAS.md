# UNIDAD 5: Variables Aleatorias Continuas y Distribuciones de Probabilidad

**Duración:** 2 semanas (12 horas)

**Curso:** Probabilidad y Estadística Inferencial

**Institución:** Universidad de la Ciénega del Estado de Michoacán de Ocampo (UCEMICH)

**Profesor:** Luis José Yudico Anaya

**Carrera:** Ingeniería en Nanotecnología

**Nivel:** Tercer Semestre

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Multiagent-AI-Lab/Probability-Statistics-Agentic-AI-Core/blob/master/notebooks/UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.ipynb)

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

### 2.6 Distribución Chi-cuadrada ($X \sim \chi^2_k$)
Distribución de la suma de $k$ variables normales estándar independientes al cuadrado; fundamental en pruebas de hipótesis sobre varianzas.
* PDF: $f(x) = \dfrac{1}{2^{k/2}\Gamma(k/2)} x^{(k/2)-1} e^{-x/2}$ para $x \ge 0$.
* Esperanza: $\mathbb{E}[X] = k$, Desviación estándar: $\sigma = \sqrt{2k}$.
* **Aplicación en nanotecnología**: al caracterizar el diámetro de nanopartículas producidas por síntesis coloidal (por ejemplo, nanopartículas de oro o puntos cuánticos de CdSe), la variabilidad del proceso de fabricación se evalúa comparando la varianza muestral del diámetro medido por microscopía electrónica contra una varianza de referencia del protocolo de síntesis; el estadístico resultante sigue una distribución Chi-cuadrada bajo el supuesto de normalidad del diámetro de las nanopartículas.

### 2.7 Distribución t-Student ($X \sim t_\nu$)
Modela la media de una muestra pequeña cuando la varianza poblacional es desconocida; base del t-test.
* PDF: $f(x) = \dfrac{\Gamma\left(\frac{\nu+1}{2}\right)}{\sqrt{\nu\pi}\,\Gamma\left(\frac{\nu}{2}\right)} \left(1+\dfrac{x^2}{\nu}\right)^{-\frac{\nu+1}{2}}$.
* Esperanza: $\mathbb{E}[X] = 0$ (para $\nu>1$), Desviación estándar: $\sigma = \sqrt{\nu/(\nu-2)}$ (para $\nu>2$).
* **Aplicación en nanotecnología**: al estimar la conductividad térmica media de un lote pequeño (n < 30) de muestras de nanotubos de carbono sintetizados por deposición química de vapor, la varianza poblacional real es desconocida, por lo que la distribución t-Student modela la incertidumbre de la media muestral en lugar de la Normal estándar.

### 2.8 Distribución F (Fisher-Snedecor) ($X \sim F_{d_1,d_2}$)
Modela el cociente de dos varianzas muestrales independientes; base de la comparación de varianzas entre grupos y de la prueba de igualdad de varianzas, tema que se retoma formalmente en unidades posteriores de inferencia.
* PDF: $f(x) = \dfrac{\left(d_1/d_2\right)^{d_1/2}\, x^{d_1/2-1}}{\left(1+\frac{d_1}{d_2}x\right)^{(d_1+d_2)/2}\, B(d_1/2,\,d_2/2)}$ para $x \ge 0$.
* Esperanza: $\mathbb{E}[X] = \dfrac{d_1}{d_1-2}$ (para $d_1>2$).
* **Aplicación en nanotecnología**: al comparar la dispersión del diámetro de nanopartículas obtenidas por dos rutas de síntesis distintas (por ejemplo, síntesis sol-gel frente a síntesis hidrotermal para nanomateriales cerámicos), el cociente de las varianzas muestrales del diámetro sigue una distribución F, lo que permite evaluar si un método de síntesis produce partículas más homogéneas que el otro.

### 2.9 Distribución Log-Normal ($X \sim \text{LogNormal}(\mu, \sigma^2)$)
Modela variables positivas cuyo logaritmo sigue una distribución normal; útil para tamaños de partícula y variables con sesgo a la derecha.
* PDF: $f(x) = \dfrac{1}{x\sigma\sqrt{2\pi}} \exp\left(-\dfrac{(\ln x - \mu)^2}{2\sigma^2}\right)$ para $x > 0$.
* Esperanza: $\mathbb{E}[X] = e^{\mu + \sigma^2/2}$.
* **Aplicación en nanotecnología**: la distribución de tamaño de nanopartículas obtenidas por síntesis en fase líquida (nucleación y crecimiento) suele presentar un sesgo marcado a la derecha, con muchas partículas pequeñas y una cola de partículas de mayor diámetro; el diámetro de estas nanopartículas se modela con frecuencia como una variable Log-Normal en lugar de Normal.

### 2.10 Distribución Beta ($X \sim \text{Beta}(\alpha, \beta)$)
Modela variables continuas acotadas en $[0,1]$, como proporciones o probabilidades.
* PDF: $f(x) = \dfrac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}$ para $0<x<1$.
* Esperanza: $\mathbb{E}[X] = \dfrac{\alpha}{\alpha+\beta}$.
* **Aplicación en nanotecnología**: la fracción de recubrimiento superficial de un nanomaterial funcionalizado (por ejemplo, el porcentaje de sitios activos de un nanotubo cubiertos por un ligando durante la síntesis) es una proporción acotada entre 0 y 1, y se modela naturalmente con una distribución Beta cuyos parámetros $\alpha$ y $\beta$ se ajustan a partir de mediciones experimentales del proceso de síntesis.

### 2.11 Distribución de Dirichlet ($\mathbf{X} \sim \text{Dirichlet}(\boldsymbol{\alpha})$)
Generalización multivariada de la distribución Beta: modela vectores de proporciones que suman 1 (un símplex), como las fracciones de composición de una aleación o mezcla de nanomateriales.
* PDF: $f(x_1,\dots,x_k) = \dfrac{1}{B(\boldsymbol{\alpha})} \prod_{i=1}^k x_i^{\alpha_i - 1}$, con $\sum_i x_i = 1$.
* Esperanza por componente: $\mathbb{E}[X_i] = \alpha_i / \sum_j \alpha_j$.
* **Aplicación en nanotecnología**: en la síntesis de nanomateriales compuestos (por ejemplo, una aleación nanoparticulada de Au-Ag-Pt), las fracciones molares de cada elemento constituyente suman siempre 1; la distribución Dirichlet modela la incertidumbre conjunta de estas proporciones de composición generadas por variabilidad del proceso de síntesis, generalizando el caso univariado de la distribución Beta a $k$ componentes de la aleación de nanomateriales.

---

## 3. Ejemplo Analítico Paso a Paso: Espesor de Películas Delgadas en Litografía Nanométrica

### 3.1 Contexto Aplicado en Nanotecnología
En la fabricación de transistores de efecto de campo de grafeno (GFETs), el espesor de la capa dieléctrica de dióxido de hafnio ($\text{HfO}_2$) depositada por capa atómica (ALD) sigue una distribución Normal con media $\mu = 8.5\text{ nm}$ y desviación estándar $\sigma = 0.4\text{ nm}$.

Para asegurar un rendimiento dieléctrico adecuado sin riesgo de tunelamiento cuántico indebido, el espesor debe estar comprendido entre $7.9\text{ nm}$ y $9.1\text{ nm}$.

Determine:
1. La probabilidad de que una oblea de silicio procesada tenga un espesor dentro del rango de tolerancia especificado.
2. El cota de espesor $x_{0.95}$ correspondiente al percentil $95\%$ de la producción.

### 3.2 Paso 1: Estandarización a la Variable Normal Estándar $Z$
$$Z = \frac{X - \mu}{\sigma} = \frac{X - 8.5}{0.4}$$

Para el límite inferior $x_1 = 7.9\text{ nm}$:
$$z_1 = \frac{7.9 - 8.5}{0.4} = \frac{-0.6}{0.4} = -1.50$$

Para el límite superior $x_2 = 9.1\text{ nm}$:
$$z_2 = \frac{9.1 - 8.5}{0.4} = \frac{0.6}{0.4} = +1.50$$

### 3.3 Paso 2: Cálculo de Probabilidad $P(7.9 \le X \le 9.1)$
$$P(7.9 \le X \le 9.1) = P(-1.50 \le Z \le +1.50) = \Phi(1.50) - \Phi(-1.50)$$

Consultando la CDF normal estándar $\Phi(1.50) \approx 0.93319$:
$$\Phi(-1.50) = 1 - \Phi(1.50) \approx 1 - 0.93319 = 0.06681$$
$$P(7.9 \le X \le 9.1) = 0.93319 - 0.06681 = \boxed{0.86638 \quad (86.64\%)}$$

### 3.4 Paso 3: Cálculo del Percentil $95\%$ ($x_{0.95}$)
Buscamos $z_{0.95}$ tal que $\Phi(z_{0.95}) = 0.95 \implies z_{0.95} \approx 1.64485$.
Desestandarizando:
$$\boxed{x_{0.95} = \mu + z_{0.95} \cdot \sigma = 8.5 + (1.64485 \times 0.4) = 8.5 + 0.65794 = 9.1579\text{ nm}}$$

---

## 4. Código de Verificación Simbólica (SymPy)

```python
import sympy as sp
from IPython.display import display, Math

## 1. Definición de símbolos
x = sp.Symbol('x', real=True)
mu = sp.Symbol('mu', real=True)
sigma = sp.Symbol('sigma', positive=True)

## 2. Expresión simbólica de la PDF Normal
pdf_normal = (1 / (sigma * sp.sqrt(2 * sp.pi))) * sp.exp(-((x - mu)**2) / (2 * sigma**2))

display(Math(fr"\text{{PDF Normal Simbólica: }} f(x) = {sp.latex(pdf_normal)}"))

## 3. Integración simbólica para calcular la probabilidad del rango [7.9, 9.1]
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

## Configuración gráfica
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 5)

## --- PARTE A: Evaluación de la Distribución Normal ---
mu_val = 8.5
sigma_val = 0.4

prob_rango = stats.norm.cdf(9.1, loc=mu_val, scale=sigma_val) - stats.norm.cdf(7.9, loc=mu_val, scale=sigma_val)
percentil_95 = stats.norm.ppf(0.95, loc=mu_val, scale=sigma_val)

print("--- EVALUACIÓN EN SCI PY STATS (NORMAL) ---")
print(f"P(7.9 <= X <= 9.1):           {prob_rango:.5f}")
print(f"Percentil 95% (Espesor):      {percentil_95:.4f} nm")

## --- PARTE B: Visualización Profesional de la Densidad ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

## Gráfico 1: PDF de Espesor HfO2 con región sombreada de tolerancia
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

## Gráfico 2: Comparación de Densidades Continuas (Normal vs Exponencial vs Weibull)
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

## --- PARTE C: Distribuciones Muestrales (prerequisito de Inferencia — Chi-cuadrada, t-Student, F) ---
from scipy.stats import chi2, t, f

## Chi-cuadrada: valor critico para intervalo de confianza de varianza (df=5, alpha=0.025 cola superior)
k_gl = 5
x_chi2 = chi2.ppf(0.975, df=k_gl)
print(f"Valor crítico Chi-cuadrada (df={k_gl}, 0.975): {x_chi2:.4f}")

## t-Student: valor critico para IC de la media (nu=10, alpha=0.05 dos colas)
nu = 10
x_t = t.ppf(0.975, df=nu)
print(f"Valor crítico t-Student (df={nu}, 0.975): {x_t:.4f}")

## F: valor critico para prueba de igualdad de varianzas (d1=5, d2=10, alpha=0.025)
d1, d2 = 5, 10
x_f = f.ppf(0.975, dfn=d1, dfd=d2)
print(f"Valor crítico F (d1={d1}, d2={d2}, 0.975): {x_f:.4f}")

## Visualización de las 3 distribuciones
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
x_range = np.linspace(0.01, 20, 300)
axes[0].plot(x_range, chi2.pdf(x_range, df=k_gl))
axes[0].set_title(f"Chi-cuadrada (df={k_gl})")
x_range_t = np.linspace(-4, 4, 300)
axes[1].plot(x_range_t, t.pdf(x_range_t, df=nu))
axes[1].set_title(f"t-Student (df={nu})")
axes[2].plot(x_range, f.pdf(x_range, dfn=d1, dfd=d2))
axes[2].set_title(f"F (d1={d1}, d2={d2})")
plt.tight_layout()
plt.show()

## --- PARTE D: Distribución de Dirichlet (composición de aleaciones de nanomateriales) ---
from scipy.stats import dirichlet

## Fracciones molares esperadas de una aleación nanoparticulada Au-Ag-Pt (k=3 componentes)
alpha_composicion = [2.0, 5.0, 3.0]

## PDF evaluada en un punto del simplex (las 3 fracciones deben sumar 1)
x_composicion = np.array([0.2, 0.5, 0.3])
pdf_dirichlet = dirichlet.pdf(x_composicion, alpha_composicion)
print(f"PDF Dirichlet en x={x_composicion.tolist()}: {pdf_dirichlet:.4f}")

## Media esperada por componente: alpha_i / suma(alpha)
media_dirichlet = dirichlet.mean(alpha_composicion)
print(f"Fracción molar media esperada (Au, Ag, Pt): {media_dirichlet}")

## Simulación de 5 lotes de síntesis con variabilidad en la composición
muestras_dirichlet = dirichlet.rvs(alpha_composicion, size=5, random_state=42)
print("Composiciones simuladas de 5 lotes de síntesis:")
print(muestras_dirichlet)
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

---

## 7. Referencia Avanzada (Opcional)

Este curso (tercer semestre) trata a las variables aleatorias continuas con herramientas de cálculo elemental. Para quien desee profundizar hacia un tratamiento formal medida-teórico (integración abstracta, funciones características, distribuciones normales multivariadas), el curso de posgrado **MIT 6.436J — Fundamentals of Probability** (Prof. Yury Polyanskiy) cubre este mismo tema en sus *Lecture Notes* 10–15, con los prerrequisitos de análisis real y teoría de la medida que ese enfoque exige: [ocw.mit.edu/courses/6-436j-fundamentals-of-probability-fall-2018/pages/lecture-notes](https://ocw.mit.edu/courses/6-436j-fundamentals-of-probability-fall-2018/pages/lecture-notes/).

## Errores Comunes / Misconceptions

* **Error**: Interpretar la densidad $f(x)$ como si fuera directamente una probabilidad, o calcular $P(X = x)$ para una variable continua como si fuera distinto de cero.
  **Correcto**: en variables continuas, $P(X = x) = 0$ para cualquier valor puntual $x$ — la probabilidad se obtiene integrando la densidad sobre un intervalo: $P(a \le X \le b) = \int_a^b f(x)\,dx$. $f(x)$ puede incluso superar 1 (no es una probabilidad, es una densidad).

* **Error**: Aplicar la propiedad de "falta de memoria" ($P(X > s+t \mid X > s) = P(X > t)$) a distribuciones continuas en general.
  **Correcto**: entre las distribuciones continuas, esa propiedad es exclusiva de la Exponencial (y, en el caso discreto, de la Geométrica). Aplicarla a una Normal, Gamma o Weibull con forma $k \ne 1$ produce resultados incorrectos.

* **Error**: Confundir el parámetro de tasa $\lambda$ de la distribución Exponencial con su media.
  **Correcto**: si $X \sim \text{Exponencial}(\lambda)$, entonces $\mathbb{E}[X] = 1/\lambda$, no $\lambda$. Un $\lambda$ grande (tasa alta de ocurrencia) corresponde a una media *pequeña* (tiempos de espera cortos), relación inversa que se olvida con frecuencia.

## Ejercicio Propuesto

Un proceso de recubrimiento por deposición de capas atómicas (ALD) produce películas de $\text{Al}_2\text{O}_3$ cuyo espesor $X$ (en nm) sigue $X \sim \mathcal{N}(\mu=15.0,\ \sigma=0.8)$.

1. Calcula $P(14.0 \le X \le 16.0)$, la probabilidad de que el espesor esté dentro de la ventana de tolerancia del proceso.
2. Calcula el percentil 90 del espesor (el valor $x$ tal que $P(X \le x) = 0.90$).
3. Calcula $P(X > 17.0)$, la probabilidad de un espesor excesivo. Explica por qué esta probabilidad puntual de la PDF evaluada en $x=17$ (es decir, $f(17)$) no sería la respuesta correcta a esta pregunta.

Escribe tu solución en una celda de código nueva en tu notebook. La celda de autoevaluación de la siguiente sección verificará tu resultado.

## Referencias

* Unpingco, J. (2019). *Python for Probability, Statistics, and Machine Learning* (2nd ed.). Springer. Capítulos sobre variables aleatorias continuas, distribuciones y su implementación con SciPy.
* Virtanen, P. et al. (2020). SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. *Nature Methods*, 17, 261-272. Documentación: [docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html)

## Autoevaluación

Guarda tu solución al Ejercicio Propuesto en un archivo separado y evalúala contra el pipeline de auditoría del curso:

```python
%%writefile solucion_ejercicio_u5.py
# Completa aquí tu solución al Ejercicio Propuesto de esta unidad.
import scipy.stats as stats

mu = 15.0
sigma = 0.8

# TODO: calcula P(14.0 <= X <= 16.0), la probabilidad de que el espesor esté dentro
#       de la ventana de tolerancia del proceso (usa stats.norm.cdf)
# TODO: calcula el percentil 90 del espesor (usa stats.norm.ppf)
# TODO: calcula P(X > 17.0), la probabilidad de un espesor excesivo, y explica en un
#       comentario por qué f(17) (la PDF evaluada en 17) no sería la respuesta correcta
```

```python
from src.multiagent_core.code_auditor_agent import CodeAuditorAgent
from external_skills.pedagogy.socratic_debugger import SocraticDebugger

with open("solucion_ejercicio_u5.py", encoding="utf-8") as f:
    codigo_alumno = f.read()

auditor = CodeAuditorAgent()
resultado = auditor.audit_code(codigo_alumno)

if resultado["issues"] or resultado["metrics"]["has_security_risk"]:
    debugger = SocraticDebugger()
    for issue in resultado["issues"]:
        tipo_error = "syntax_error" if "SyntaxError" in issue else "generic"
        print("💡", debugger.generate_socratic_question(tipo_error, "Unidad 5"))
    for issue in resultado["security_issues"]:
        print("🔒", debugger.generate_socratic_question("security_risk", "Unidad 5"))
        print("   ", issue)
    print("\n--- Detalle técnico ---")
    print(resultado)
else:
    print("✅ Tu código pasa las verificaciones automáticas de estilo y seguridad.")
    print(resultado)
```
