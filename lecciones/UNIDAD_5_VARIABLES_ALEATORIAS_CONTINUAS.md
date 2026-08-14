# UNIDAD 5: Variables Aleatorias Continuas y Distribuciones de Probabilidad
> **Asignatura: Probabilidad y Estadística Inferencial**
> **UCEMICH — Ingeniería en IA y Nanotecnología**
> **Autor y Profesor: Mtro. Luis José Yudico Anaya**

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
