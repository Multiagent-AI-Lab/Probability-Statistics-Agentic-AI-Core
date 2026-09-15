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

---

* Sharafi, S. M., Flores, M., Appuhami, H. & Selim, F. A. (2026). Control of Microstructure, Trap Levels, and Trap Distribution in HfO2 Films Grown by Atomic Layer Deposition. *Nanomaterials*, 16(8), 451. DOI: [10.3390/nano16080451](https://doi.org/10.3390/nano16080451) — control de espesor y microestructura de películas de HfO₂ depositadas por ALD, el material y proceso exactos del ejemplo aplicado de esta unidad (Distribución Normal del espesor dieléctrico).
