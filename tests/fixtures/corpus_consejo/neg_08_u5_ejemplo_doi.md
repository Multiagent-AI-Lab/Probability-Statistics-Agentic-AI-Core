### 2.13 Las Funciones Gamma y Beta: el Fundamento Matemático Detrás de las PDFs

Las secciones anteriores usan $\Gamma(k)$ (Gamma, Weibull, Chi-cuadrada, t-Student) y $B(\alpha,\beta)$ (Beta, F, Dirichlet) como constantes de normalización sin desarrollarlas — son **funciones matemáticas especiales**, no las distribuciones de probabilidad que llevan su nombre, y vale la pena distinguirlas explícitamente antes de seguir usándolas como caja negra.

**Función Gamma**: generaliza el factorial a números reales (y complejos) positivos:
$$\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}\,dt, \qquad \Gamma(n) = (n-1)!\ \text{para } n\in\mathbb{Z}^+$$
Por ejemplo, $\Gamma(2)=1!=1$ y $\Gamma(5)=4!=24$ — es precisamente esta función la que aparece en el denominador de la PDF Gamma (§2.4) para garantizar que el área bajo la curva sea 1.

**Función Beta**: relacionada con la Gamma mediante la identidad
$$B(x,y) = \int_0^1 t^{x-1}(1-t)^{y-1}\,dt = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}$$
Es **simétrica**: $B(x,y)=B(y,x)$. Por ejemplo, $B(2,3) = \dfrac{\Gamma(2)\Gamma(3)}{\Gamma(5)} = \dfrac{1\times2}{24} = \dfrac{1}{12}\approx0.0833$ — esta es la constante que normaliza la PDF Beta (§2.10) y aparece también en la PDF F (§2.8).

```python
import math

import sympy as sp
from scipy.special import gamma, beta
import numpy as np

## 1. Definicion simbolica: Gamma(n) para n entero positivo
n = sp.Symbol('n', positive=True, integer=True)
gamma_simbolico = sp.gamma(n)
print(f"Gamma(n) simbolico = {gamma_simbolico}")

## 2. Sustitucion de valores concretos y evaluacion simbolica exacta
for n_val in [2, 3, 5]:
    gamma_exacto = gamma_simbolico.subs(n, n_val)
    print(f"Gamma({n_val}) simbolico exacto = {gamma_exacto}  vs  (n-1)! = {math.factorial(n_val - 1)}")

## 3. Funcion Beta simbolica: B(x,y) = Gamma(x)Gamma(y)/Gamma(x+y)
x_sym, y_sym = sp.symbols('x y', positive=True)
beta_simbolico = sp.beta(x_sym, y_sym)
print(f"\nB(x,y) simbolico = {beta_simbolico}")

beta_exacto = sp.nsimplify(beta_simbolico.subs({x_sym: 2, y_sym: 3}))
print(f"B(2,3) simbolico exacto = {beta_exacto} = {float(beta_exacto):.6f}")

## 4. Verificacion numerica cruzada con scipy.special (funciones no simbolicas)
valores_z = np.array([2, 3, 5])
gamma_valores = gamma(valores_z)
factoriales_equivalentes = [math.factorial(z - 1) for z in valores_z]
print(f"\nGamma(2)={gamma_valores[0]:.1f}  Gamma(3)={gamma_valores[1]:.1f}  Gamma(5)={gamma_valores[2]:.1f}")
print(f"Factoriales equivalentes (n-1)!: {factoriales_equivalentes}")

## Funcion Beta: verifica la relacion B(x,y) = Gamma(x)Gamma(y)/Gamma(x+y)
x_val, y_val = 2, 3
beta_directa = beta(x_val, y_val)
beta_via_gamma = (gamma(x_val) * gamma(y_val)) / gamma(x_val + y_val)
beta_simetrica = beta(y_val, x_val)  # B(y,x) debe dar el mismo resultado que B(x,y)

print(f"\nB(2,3) directa:        {beta_directa:.6f}")
print(f"B(2,3) via Gamma:      {beta_via_gamma:.6f}")
print(f"B(3,2) (simetria):     {beta_simetrica:.6f}")
```

El paso simbólico confirma $\Gamma(2)=1$, $\Gamma(3)=2$, $\Gamma(5)=24$ y $B(2,3)=\frac{1}{12}\approx0.083333$ como expresiones exactas (no aproximaciones de punto flotante) antes de sustituir valores concretos — completando la cadena símbolo → sustitución → numérico y coincidiendo exactamente con la verificación numérica de `scipy.special` que sigue.

**Por qué importa distinguirlas**: `scipy.special.gamma` y `scipy.special.beta` calculan las *funciones matemáticas* $\Gamma(z)$ y $B(x,y)$ — no confundir con `scipy.stats.gamma` y `scipy.stats.beta`, que son las *distribuciones de probabilidad* Gamma y Beta ya usadas en las Secciones 2.4/2.6/2.7/2.10/2.12.6/2.12.10 de esta unidad (mismo nombre de módulo, API completamente distinta: una da un número, la otra da un objeto de distribución con `.pdf()`, `.cdf()`, `.rvs()`, etc.).

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

### 3.5 Prueba Unitaria con pytest

En vez de consultar tablas de la Normal estándar (con el redondeo que eso implica), se verifican los dos resultados directamente contra `scipy.stats.norm`, que evalúa $\Phi$ con precisión de punto flotante completa:

```python
import ipytest
import pytest
from scipy.stats import norm

ipytest.autoconfig()

mu, sigma = 8.5, 0.4


def test_probabilidad_de_espesor_dentro_de_tolerancia():
    prob = norm.cdf(9.1, mu, sigma) - norm.cdf(7.9, mu, sigma)
    assert prob == pytest.approx(0.86638, rel=1e-4)


def test_percentil_95_de_la_produccion():
    x_95 = norm.ppf(0.95, mu, sigma)
    assert x_95 == pytest.approx(9.1579, rel=1e-4)


ipytest.run("-vv")
```

---

## 4. Código de Verificación Simbólica (SymPy)

Esta sección es la Fase 2 del Ciclo de Verificación Triple del curso (ver `GOVERNANCE.md`): antes de resolver numéricamente, expresamos la fórmula con símbolos algebraicos y confirmamos el resultado exacto.

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

---

* Sharafi, S. M., Flores, M., Appuhami, H. & Selim, F. A. (2026). Control of Microstructure, Trap Levels, and Trap Distribution in HfO2 Films Grown by Atomic Layer Deposition. *Nanomaterials*, 16(8), 451. DOI: [10.3390/nano16080451](https://doi.org/10.3390/nano16080451) — control de espesor y microestructura de películas de HfO₂ depositadas por ALD, el material y proceso exactos del ejemplo aplicado de esta unidad (Distribución Normal del espesor dieléctrico).
