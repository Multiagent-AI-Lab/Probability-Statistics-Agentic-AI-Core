# UNIDAD 4: Distribuciones de Probabilidad Conjuntas y Bivariadas

**Duración:** 2.5 semanas (15 horas)

**Curso:** Probabilidad y Estadística Inferencial

**Institución:** Universidad de la Ciénega del Estado de Michoacán de Ocampo (UCEMICH)

**Profesor:** Luis José Yudico Anaya

**Carrera:** Ingeniería en Nanotecnología

**Nivel:** Tercer Semestre

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Multiagent-AI-Lab/Probability-Statistics-Agentic-AI-Core/blob/master/notebooks/UNIDAD_4_DISTRIBUCIONES_CONJUNTAS.ipynb)

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

## 1. Fundamentación Teórica: Distribuciones Conjuntas y Marginales

### 1.1 Concepto General
Cuando dos o más variables aleatorias se analizan simultáneamente, su comportamiento combinado se describe mediante una **distribución conjunta**: indica la probabilidad de que $X$ y $Y$ tomen determinados valores de forma simultánea.

Para variables **discretas**, la función de masa de probabilidad conjunta (PMF) se denota:
$$P_{X,Y}(x,y) = P(X = x,\ Y = y)$$

Para variables **continuas**, se utiliza la función de densidad de probabilidad conjunta (PDF) $f_{X,Y}(x,y)$.

### 1.2 Propiedades Básicas
1. **No-negatividad**: $P_{X,Y}(x,y)\ge0$, $f_{X,Y}(x,y)\ge0$.
2. **Normalización**:
   * Discretas: $\displaystyle\sum_x\sum_y P_{X,Y}(x,y)=1$
   * Continuas: $\displaystyle\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dx\,dy = 1$

**Ejemplo intuitivo**: sea $X$ = número de bolas rojas extraídas y $Y$ = número de bolas azules extraídas de una urna. Cada par $(x,y)$ tiene una probabilidad $P_{X,Y}(x,y)$ que indica cuántas combinaciones producen ese resultado.

### 1.3 Distribuciones Marginales
La **distribución marginal** de una variable se obtiene a partir de la conjunta **eliminando** (sumando o integrando) la otra variable:
$$P_X(x)=\sum_y P_{X,Y}(x,y), \qquad P_Y(y)=\sum_x P_{X,Y}(x,y)$$
$$f_X(x)=\int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dy,\qquad f_Y(y)=\int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dx$$

**Ejemplo (discreto)**. Suponga la siguiente tabla de probabilidades conjuntas:

| X \ Y |   0  |   1  |  2  |
| :---: | :--: | :--: | :-: |
|   0   | 1/15 | 2/15 |  0  |
|   1   | 3/15 | 6/15 |  0  |
|   2   | 1/15 | 2/15 |  0  |

Marginal de $X$: $P_X(0)=3/15$, $P_X(1)=9/15$, $P_X(2)=3/15$.
Marginal de $Y$: $P_Y(0)=5/15$, $P_Y(1)=10/15$, $P_Y(2)=0$.

Las marginales resumen la información individual de cada variable sin considerar su relación conjunta y permiten calcular expectativas o probabilidades univariadas.

---

## 2. Independencia de Variables Aleatorias

### 2.1 Concepto y Criterio
Dos variables aleatorias $X$ y $Y$ son **independientes** si el conocimiento de una **no afecta** la distribución de la otra:
$$P_{X,Y}(x,y)=P_X(x)\,P_Y(y) \qquad \text{o, en el caso continuo,} \qquad f_{X,Y}(x,y)=f_X(x)\,f_Y(y)$$

### 2.2 Propiedades Clave
Si $X$ e $Y$ son independientes:
1. $E[XY]=E[X]\,E[Y]$
2. La covarianza es cero: $\mathrm{Cov}(X,Y)=E[(X-E[X])(Y-E[Y])]=0$

### 2.3 Ejemplo (Comprobación de Independencia, Discreto)
Con las marginales y conjunta de la tabla anterior: $P_X(1)=9/15$, $P_Y(1)=10/15$, $P_{X,Y}(1,1)=6/15$.

Si fueran independientes se debería cumplir $P_X(1)\cdot P_Y(1) = \frac{9}{15}\cdot\frac{10}{15} = \frac{90}{225} = 0.4$. Como $P_{X,Y}(1,1)=6/15=0.4$ también, la igualdad se sostiene para este par; verificándola en todos los pares $(x,y)$ se confirma si $X$ y $Y$ son independientes.

### 2.4 Ejemplo (Continuo)
Sea $f_{X,Y}(x,y)=2$ en el triángulo $0\le y\le x\le1$ y $0$ en otro caso.
* Marginal de $X$: $f_X(x)=\int_0^{x}2\,dy=2x$
* Marginal de $Y$: $f_Y(y)=\int_y^{1}2\,dx=2(1-y)$
* Producto: $f_X(x)f_Y(y)=4x(1-y)$, que **no coincide** con $f_{X,Y}(x,y)=2$; luego $X$ y $Y$ **no son independientes**.

---

## 3. Distribuciones Condicionales (PMF/PDF) y Esperanza Condicional

### 3.1 PMF Condicional (Discreta)
Cuando se conoce el valor de una variable $X=x$, la incertidumbre sobre otra variable $Y$ cambia; la distribución resultante se denomina **distribución condicional**. Dadas dos variables aleatorias discretas $X$ e $Y$ con PMF conjunta $P_{X,Y}(x,y)$:
$$P_{Y|X}(y|x) = P(Y=y \mid X=x) = \frac{P_{X,Y}(x,y)}{P_X(x)}, \qquad P_X(x) > 0$$

**Propiedades**: (1) $\sum_y P_{Y|X}(y|x) = 1$ para $x$ fijo; (2) Regla de multiplicación: $P_{X,Y}(x,y) = P_X(x)\,P_{Y|X}(y|x)$.

**Ejemplo (urna con bolas rojas y azules)**: retomando $P_{X,Y}(1,0)=3/15$, $P_{X,Y}(1,1)=6/15$, $P_X(1)=9/15$:
$$P_{Y|X}(0|1) = \frac{3/15}{9/15} = \frac{1}{3}, \qquad P_{Y|X}(1|1) = \frac{6/15}{9/15} = \frac{2}{3}$$
Verificación: $\frac{1}{3}+\frac{2}{3}=1$. ✓

```python
## Cálculo de PMF condicional discreta
import numpy as np
from fractions import Fraction

## PMF Conjunta P(x, y)
P_XY = {(0, 0): 0, (0, 1): Fraction(2, 15), (0, 2): Fraction(1, 15),
        (1, 0): Fraction(3, 15), (1, 1): Fraction(6, 15), (1, 2): 0,
        (2, 0): Fraction(3, 15), (2, 1): 0, (2, 2): 0}

## PMF Marginal de X
P_X_1 = Fraction(9, 15)
print(f"PMF Marginal P_X(1) = {P_X_1}")

## Calcular PMF Condicional P(Y | X=1)
print("\nPMF Condicional P(Y | X=1):")
for y in range(3):
    P_Y_cond_X = P_XY[(1, y)] / P_X_1
    print(f"P(Y={y} | X=1) = {P_Y_cond_X}")
```

### 3.2 PDF Condicional (Continua)
Dadas dos variables aleatorias continuas $X$ e $Y$ con PDF conjunta $f_{X,Y}(x,y)$:
$$f_{Y|X}(y|x) = \frac{f_{X,Y}(x,y)}{f_X(x)}, \qquad f_X(x) > 0$$

**Propiedades**: (1) $\int_{-\infty}^{\infty} f_{Y|X}(y|x)\,dy = 1$; (2) $f_{X,Y}(x,y) = f_{Y|X}(y|x)\,f_X(x)$; (3) si $X$ e $Y$ son independientes, $f_{Y|X}(y|x)=f_Y(y)$.

**Ejemplo**: sea $f_{X,Y}(x,y) = x+y$ para $0 \le x,y \le 1$. La marginal es $f_X(x) = \int_0^1(x+y)\,dy = x+\frac{1}{2}$, por lo que:
$$f_{Y|X}(y|x) = \frac{x+y}{x+\frac{1}{2}}$$
Con $x=0.5$: $f_{Y|X}(y|0.5) = 0.5+y$, y entonces:
$$P(Y<0.5 \mid X=0.5) = \int_0^{0.5} (0.5+y)\,dy = \boxed{0.375}$$

### 3.3 Esperanza Condicional
La **esperanza condicional** de $Y$ dado $X=x$ es el valor esperado de $Y$ respecto a su distribución condicional:
$$E[Y|X=x] = \sum_y y\,P_{Y|X}(y|x) \quad \text{(discreta)}, \qquad E[Y|X=x] = \int_{-\infty}^{\infty} y\,f_{Y|X}(y|x)\,dy \quad \text{(continua)}$$

**Propiedades**: (1) Linealidad: $E[aY+b|X]=aE[Y|X]+b$; (2) Ley de la Esperanza Total (iteración): $E[Y]=E[E[Y|X]]$; (3) si $X,Y$ independientes, $E[Y|X]=E[Y]$.

**Ejemplo discreto**: con $P_{Y|X}(0|1)=1/3$ y $P_{Y|X}(1|1)=2/3$:
$$E[Y|X=1]=0\cdot\frac{1}{3}+1\cdot\frac{2}{3}=\boxed{\frac{2}{3}}$$

**Ejemplo de aplicación de la Ley de la Esperanza Total**: si $E[Y|X=x]=2x+1$ y $E[X]=3$, entonces $E[Y]=E[2X+1]=2E[X]+1=\boxed{7}$.

```python
## Esperanza condicional discreta
import numpy as np

y_vals = np.array([0, 1])
p_cond = np.array([1/3, 2/3])
E_Y_given_X1 = np.sum(y_vals * p_cond)
print(f"E[Y|X=1] = {E_Y_given_X1:.4f}")
```

---

## 4. Suma de Variables Aleatorias y Convolución

### 4.1 Definición (Discreta y Continua)
Sea $Z=X+Y$ con $X,Y$ independientes. La distribución de $Z$ se obtiene mediante **convolución**:

**Discreta**: $\displaystyle P_Z(z)=P(X+Y=z)=\sum_{x} P_X(x)\,P_Y(z-x)$

**Continua**: $\displaystyle f_Z(z)=\int_{-\infty}^{\infty} f_X(x)\,f_Y(z-x)\,dx$

En ambos casos la convolución suma la contribución de todas las parejas $(x,y)$ tales que $x+y=z$.

### 4.2 Intuición Geométrica y Mecánica
* **Geometría (continua)**: piensa en $f_X(x)$ como una "forma" sobre el eje $x$. Para obtener $f_Z(z)$ se invierte y desplaza $f_Y$, se multiplica punto a punto con $f_X$ y se integra, obteniendo el área de superposición.
* **Intuición (discreta)**: para cada posible $x$ que $X$ puede tomar, la probabilidad de que $Z=z$ y $X=x$ es $P_X(x)P_Y(z-x)$; se suma sobre todos esos $x$.

### 4.3 Propiedades Fundamentales
1. **Conmutatividad**: $f_X * f_Y = f_Y * f_X$
2. **Asociatividad**: $(f_X * f_Y) * f_W = f_X * (f_Y * f_W)$
3. **Normalización**: si $f_X,f_Y$ son densidades válidas, $f_X * f_Y$ también lo es.
4. **Transformadas**: $\mathcal{F}\{f*g\} = \mathcal{F}\{f\}\cdot \mathcal{F}\{g\}$ (transformadas de Fourier o funciones generadoras de momentos convierten convoluciones en productos).
5. **Momentos**: $E[X+Y]=E[X]+E[Y]$, y $\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)+2\mathrm{Cov}(X,Y)$ (si independientes, $\mathrm{Cov}=0$).

### 4.4 Ejemplos Analíticos Completos

**Ejemplo A — Discreto: Suma de dos dados justos.** Con $P_X(k)=1/6$ para $k=1,\dots,6$, el número de pares $(x,y)$ con $x+y=z$ crece de 1 (en $z=2$) a 6 (en $z=7$) y decrece simétricamente hasta 1 (en $z=12$), produciendo la distribución triangular clásica $P_Z(7) = 6/36 = 1/6$.

```python
import numpy as np
import matplotlib.pyplot as plt

p = np.ones(6) / 6  # pmf de un dado
## convolución discreta (modo 'full')
pz = np.convolve(p, p)
z_vals = np.arange(2, 13)
print("P(Z=z) para z=2..12:", np.round(pz, 4))

plt.stem(z_vals, pz, basefmt=" ")
plt.xlabel("z")
plt.ylabel("P(Z=z)")
plt.title("PMF de la suma de dos dados justos")
plt.grid(True)
plt.show()
```

**Ejemplo B — Suma de Binomiales.** Si $X\sim \mathrm{Binomial}(n_1,p)$ y $Y\sim \mathrm{Binomial}(n_2,p)$ independientes, entonces $Z=X+Y\sim\mathrm{Binomial}(n_1+n_2,p)$. Interpretando $X$ como éxitos en $n_1$ ensayos y $Y$ en $n_2$ ensayos disjuntos con la misma $p$, la unión es $n_1+n_2$ ensayos independientes. Formalmente, por convolución de PMFs y la identidad de Vandermonde $\sum_{i=0}^k \binom{n_1}{i}\binom{n_2}{k-i} = \binom{n_1+n_2}{k}$:
$$P(Z=k) = \binom{n_1+n_2}{k} p^k(1-p)^{n_1+n_2-k}$$

```python
import numpy as np
from scipy.stats import binom

n1, n2, p = 5, 3, 0.4
x = np.arange(0, n1 + 1)
y = np.arange(0, n2 + 1)
pmf_x = binom.pmf(x, n1, p)
pmf_y = binom.pmf(y, n2, p)

pmf_z = np.convolve(pmf_x, pmf_y)
k = np.arange(0, n1 + n2 + 1)
pmf_z_binom = binom.pmf(k, n1 + n2, p)

np.testing.assert_allclose(pmf_z, pmf_z_binom, atol=1e-12)
print("Convolución coincide con Binomial(n1+n2,p).")
```

**Ejemplo C — Suma de Poissons.** Si $X\sim \mathrm{Poisson}(\lambda_1)$ y $Y\sim \mathrm{Poisson}(\lambda_2)$ independientes, entonces $Z=X+Y\sim\mathrm{Poisson}(\lambda_1+\lambda_2)$. Usando la función generadora de probabilidad $G_X(s)=\exp(\lambda_1(s-1))$: $G_Z(s)=G_X(s)G_Y(s)=\exp((\lambda_1+\lambda_2)(s-1))$, que es la PGF de $\mathrm{Poisson}(\lambda_1+\lambda_2)$.

**Ejemplo D — Convolución de dos Uniformes $U[0,1]$.** Con $X,Y\sim U[0,1]$ independientes, el intervalo de integración efectivo es $x\in[\max(0,z-1),\min(1,z)]$, dando la densidad triangular clásica en $[0,2]$:
$$f_Z(z) = \begin{cases} z, & 0 \le z \le 1 \\ 2-z, & 1 < z \le 2 \\ 0, & \text{en otro caso} \end{cases}$$

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve

N = 1000
x = np.linspace(0, 1, N)
dx = x[1] - x[0]
fX = np.ones_like(x)
fY = np.ones_like(x)
fZ_num = fftconvolve(fX, fY) * dx
z = np.linspace(0, 2, len(fZ_num))
fZ_theo = np.where(z <= 1, z, 2 - z)
fZ_theo = np.where((z < 0) | (z > 2), 0, fZ_theo)

plt.plot(z, fZ_num, label='numérica (fft conv)')
plt.plot(z, fZ_theo, '--', label='teórica')
plt.legend()
plt.xlabel('z'); plt.ylabel('f_Z(z)')
plt.title('Convolución de dos Uniformes[0,1]')
plt.show()
```

**Ejemplo E — Suma de Normales.** Si $X\sim N(\mu_1,\sigma_1^2)$ y $Y\sim N(\mu_2,\sigma_2^2)$ independientes, usando la función característica $\phi_X(t)=\exp(i\mu_1 t - \tfrac12\sigma_1^2t^2)$ se obtiene $\phi_Z(t)=\phi_X(t)\phi_Y(t)=\exp(i(\mu_1+\mu_2)t - \tfrac12(\sigma_1^2+\sigma_2^2)t^2)$, que corresponde a $Z\sim N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$.

### 4.5 Tabla Resumen: Suma de Distribuciones Comunes

| Distribución de $X$ | Distribución de $Y$ | Distribución de $Z=X+Y$ | Nota |
|:---:|:---:|:---:|:---|
| $\mathrm{Binomial}(n_1,p)$ | $\mathrm{Binomial}(n_2,p)$ | $\mathrm{Binomial}(n_1+n_2,p)$ | Identidad de Vandermonde |
| $\mathrm{Poisson}(\lambda_1)$ | $\mathrm{Poisson}(\lambda_2)$ | $\mathrm{Poisson}(\lambda_1+\lambda_2)$ | Producto de PGFs |
| $\mathrm{Normal}(\mu_1,\sigma_1^2)$ | $\mathrm{Normal}(\mu_2,\sigma_2^2)$ | $\mathrm{Normal}(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$ | Función característica |
| $\mathrm{Gamma}(\alpha_1,\theta)$ | $\mathrm{Gamma}(\alpha_2,\theta)$ | $\mathrm{Gamma}(\alpha_1+\alpha_2,\theta)$ | Mismo parámetro de escala |

---

## 5. Ejemplo Analítico Paso a Paso: Diámetro y Potencial Zeta de Nanopartículas Coloidales

### 5.1 Contexto Aplicado en Nanotecnología
En el análisis bivariado de propiedades fisicoquímicas de nanopartículas coloidales, la distribución de probabilidad conjunta permite evaluar el impacto simultáneo de dos variables críticas para la estabilidad de una suspensión: el **diámetro de partícula** $X$ (en nm) y el **potencial zeta** $Y$ (en mV, una medida de la carga superficial efectiva que gobierna la repulsión electrostática entre partículas). Estas dos variables no son independientes en un proceso real de síntesis: partículas más grandes tienden a exhibir un potencial zeta más negativo debido a la mayor área superficial disponible para la adsorción de iones estabilizantes (p. ej. citrato).

Se modela el par $(X,Y)$ como un vector aleatorio bivariado con:
$$\mu = \begin{pmatrix} 25.0 \\ -40.0 \end{pmatrix} \text{nm, mV}, \qquad \Sigma = \begin{pmatrix} 16.0 & -18.0 \\ -18.0 & 36.0 \end{pmatrix}$$

### 5.2 Paso 1: Interpretación de la Matriz de Covarianza
La varianza de $X$ es $\mathrm{Var}(X)=16\ \text{nm}^2$ ($\sigma_X=4\ \text{nm}$) y la de $Y$ es $\mathrm{Var}(Y)=36\ \text{mV}^2$ ($\sigma_Y=6\ \text{mV}$). La covarianza $\mathrm{Cov}(X,Y)=-18$ es negativa, confirmando la relación inversa esperada entre tamaño de partícula y potencial zeta.

### 5.3 Paso 2: Coeficiente de Correlación
$$\rho_{X,Y} = \frac{\mathrm{Cov}(X,Y)}{\sigma_X \sigma_Y} = \frac{-18}{4 \times 6} = \boxed{-0.75}$$

Una correlación de $-0.75$ indica una relación lineal inversa fuerte: lotes con nanopartículas de mayor diámetro promedio tienden sistemáticamente a un potencial zeta menos negativo (en valor absoluto), lo cual es relevante para el control de calidad, ya que un $|\zeta| < 30\ \text{mV}$ suele considerarse zona de riesgo de agregación coloidal.

### 5.4 Paso 3: Simulación por Descomposición de Cholesky
Para generar muestras correlacionadas de este vector bivariado, se factoriza $\Sigma = LL^T$ (descomposición de Cholesky) y se transforma ruido gaussiano independiente $Z\sim N(0,I_2)$:
$$X = \mu + LZ \implies X \sim N(\mu, \Sigma)$$

### 5.5 Paso 4: Probabilidad de Zona de Riesgo de Agregación
Usando la marginal de $Y\sim N(-40, 36)$, la probabilidad de que un lote tenga $|\zeta|<30\ \text{mV}$ (es decir $-30 < Y$) es:
$$P(Y > -30) = P\left(Z > \frac{-30-(-40)}{6}\right) = P(Z > 1.667) \approx \boxed{0.0478}$$

Aproximadamente el $4.78\%$ de las nanopartículas individuales caen en zona de riesgo de agregación por baja repulsión electrostática, información crítica para decidir si el lote requiere reformulación del agente estabilizante.

---

## 6. Vectores Aleatorios, Matriz de Covarianza y Normal Multivariada

### 6.1 Definición e Intuición Geométrica
Un **vector aleatorio** $\mathbf{X}$ en $\mathbb{R}^p$ es una colección de $p$ variables aleatorias:
$$\mathbf{X} = \begin{pmatrix} X_1 \\ X_2 \\ \vdots \\ X_p \end{pmatrix}$$

Cada realización de $\mathbf{X}$ representa un punto en el espacio $p$-dimensional; la nube de puntos resultante revela la estructura de dependencia entre variables. En el caso bidimensional: si $X$ e $Y$ son independientes, la nube es isotrópica (circular); si están correlacionadas, es elipsoidal; con correlación perfecta, los puntos se alinean.

### 6.2 Función de Densidad Conjunta y Vector de Esperanza
Para variables continuas, la PDF conjunta satisface $P(\mathbf{X}\in R) = \int_R f_{\mathbf{X}}(\mathbf{x})\,d\mathbf{x}$, y bajo independencia se factoriza como $f_{\mathbf{X}}(\mathbf{x}) = \prod_{i=1}^p f_{X_i}(x_i)$. El vector de esperanza es:
$$\mathbb{E}[\mathbf{X}] = \begin{pmatrix} \mathbb{E}[X_1] \\ \vdots \\ \mathbb{E}[X_p] \end{pmatrix}$$

**Ejemplo**: para $f_{X,Y}(x,y)=2$ en el triángulo $0\le y\le x\le1$: $E[X] = 2/3$, $E[Y] = 1/3$.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import sympy as sp

## Verificación de normalización
result, error = integrate.dblquad(lambda y, x: 2, 0, 1, lambda x: 0, lambda x: x)
print(f"Integral de la PDF: {result}, Error: {error}")

## Cálculo de esperanzas marginales (numérico y simbólico)
E_X = integrate.dblquad(lambda y, x: x * 2, 0, 1, lambda x: 0, lambda x: x)[0]
E_Y = integrate.dblquad(lambda y, x: y * 2, 0, 1, lambda x: 0, lambda x: x)[0]
print(f"E[X] = {E_X:.3f}, E[Y] = {E_Y:.3f}")

x_sym, y_sym = sp.symbols('x y', real=True, positive=True)
f_xy = 2
E_X_sym = sp.integrate(x_sym * f_xy, (y_sym, 0, x_sym), (x_sym, 0, 1))
E_Y_sym = sp.integrate(y_sym * f_xy, (y_sym, 0, x_sym), (x_sym, 0, 1))
print(f"E[X] (analítico) = {E_X_sym} = {float(E_X_sym):.3f}")
print(f"E[Y] (analítico) = {E_Y_sym} = {float(E_Y_sym):.3f}")
```

### 6.3 Matriz de Covarianza
$$\mathbf{\Sigma} = \mathbb{E}[(\mathbf{X} - \mathbf{\mu})(\mathbf{X} - \mathbf{\mu})^T]$$

Elementos diagonales $\Sigma_{ii}=\mathrm{Var}(X_i)$; fuera de la diagonal $\Sigma_{ij}=\mathrm{Cov}(X_i,X_j)$. Propiedades: simétrica, semidefinida positiva, y su rango indica dependencias lineales entre componentes.

```python
def calcular_covarianza_analitica():
    """Cálculo analítico completo de la matriz de covarianza (triangular f(x,y)=2)"""
    E_X, E_Y = 2 / 3, 1 / 3
    E_X2 = sp.integrate(x_sym**2 * f_xy, (y_sym, 0, x_sym), (x_sym, 0, 1))
    E_Y2 = sp.integrate(y_sym**2 * f_xy, (y_sym, 0, x_sym), (x_sym, 0, 1))
    E_XY = sp.integrate(x_sym * y_sym * f_xy, (y_sym, 0, x_sym), (x_sym, 0, 1))

    Var_X = E_X2 - E_X**2
    Var_Y = E_Y2 - E_Y**2
    Cov_XY = E_XY - E_X * E_Y

    return np.array([[float(Var_X), float(Cov_XY)], [float(Cov_XY), float(Var_Y)]])

Sigma_analitica = calcular_covarianza_analitica()
print("Matriz de covarianza analítica:\n", Sigma_analitica)

## Verificación por simulación (max(U1,U2), min(U1,U2)) genera la densidad triangular
def generar_muestra_triangular(n=10000):
    u1 = np.random.uniform(0, 1, n)
    u2 = np.random.uniform(0, 1, n)
    return np.column_stack([np.maximum(u1, u2), np.minimum(u1, u2)])

muestra = generar_muestra_triangular(100_000)
print("\nMatriz de covarianza muestral:\n", np.cov(muestra, rowvar=False))
```

### 6.4 Distribución Normal Multivariada
La PDF de una normal $p$-dimensional $\mathbf{X}\sim \mathcal{N}(\mathbf{\mu},\mathbf{\Sigma})$ es:
$$f(\mathbf{x}) = \frac{1}{(2\pi)^{p/2}|\mathbf{\Sigma}|^{1/2}} \exp\left(-\frac{1}{2}(\mathbf{x}-\mathbf{\mu})^T\mathbf{\Sigma}^{-1}(\mathbf{x}-\mathbf{\mu})\right)$$

La **distancia de Mahalanobis** $D^2=(\mathbf{x}-\mu)^T\Sigma^{-1}(\mathbf{x}-\mu)$ mide distancia estadística considerando la correlación entre variables. Geométricamente, las curvas de nivel son elipses (2D) o elipsoides ($p$D), con ejes principales dados por los autovectores de $\Sigma$ y longitudes $\sqrt{\text{autovalores}}$.

```python
def visualizar_normal_multivariada():
    """Visualización de distribución normal bivariada con componentes principales"""
    mu = np.array([0, 0])
    Sigma = np.array([[2, 1], [1, 1]])

    theta = np.linspace(0, 2 * np.pi, 100)
    circle = np.column_stack([np.cos(theta), np.sin(theta)])

    ## Descomposición espectral (eigh: más estable para matrices simétricas)
    eigenvals, eigenvecs = np.linalg.eigh(Sigma)
    ellipse = circle @ np.diag(np.sqrt(eigenvals)) @ eigenvecs.T + mu

    plt.figure(figsize=(8, 6))
    plt.plot(ellipse[:, 0], ellipse[:, 1], 'r-', linewidth=2, label='Elipse 1-sigma')
    for i, color in zip(range(2), ['blue', 'green']):
        v = eigenvecs[:, i] * np.sqrt(eigenvals[i])
        plt.quiver(mu[0], mu[1], v[0], v[1], angles='xy', scale_units='xy',
                   scale=1, color=color, width=0.01, label=f'PC{i+1}')

    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.legend()
    plt.title('Distribución Normal Bivariada y Componentes Principales')
    plt.show()

visualizar_normal_multivariada()
```

---

## 7. Transformaciones Lineales, Whitening y PCA

### 7.1 Transformaciones Lineales de Vectores Gaussianos
Sea $\mathbf{Y} = \mathbf{A}\mathbf{X} + \mathbf{b}$ con $\mathbf{X} \sim \mathcal{N}(\mathbf{\mu}_X, \mathbf{\Sigma}_X)$. Entonces:
$$\mathbf{Y} \sim \mathcal{N}(\mathbf{A}\mathbf{\mu}_X + \mathbf{b},\ \mathbf{A}\mathbf{\Sigma}_X\mathbf{A}^T)$$

```python
def transformacion_lineal_multivariada():
    """Transformación lineal de un vector gaussiano 3D a 2D"""
    mu_X = np.array([1, 2, 3])
    Sigma_X = np.array([[4, 1, 0.5], [1, 3, 0.8], [0.5, 0.8, 2]])
    A = np.array([[1, 0.5, 0], [0, 1, 1]])
    b = np.array([-1, 2])

    mu_Y = A @ mu_X + b
    Sigma_Y = A @ Sigma_X @ A.T
    print(f"mu_Y = {mu_Y}\nSigma_Y =\n{Sigma_Y}")

    ## Verificación por simulación
    X = np.random.multivariate_normal(mu_X, Sigma_X, 10_000)
    Y_sim = (A @ X.T + b.reshape(-1, 1)).T
    print(f"\nmu_Y simulado = {np.mean(Y_sim, axis=0)}")
    print(f"Sigma_Y simulado =\n{np.cov(Y_sim, rowvar=False)}")

transformacion_lineal_multivariada()
```

### 7.2 Descomposición Espectral y Geometría
La descomposición $\mathbf{\Sigma} = \mathbf{V}\mathbf{\Lambda}\mathbf{V}^T$ revela los eigenvectores (direcciones principales de variación) y eigenvalores (magnitud de variación en cada dirección).

```python
def analisis_espectral_completo(Sigma):
    """Descomposición espectral, ortogonalidad y varianza explicada"""
    eigenvals, eigenvecs = np.linalg.eigh(Sigma)  # eigh: estable para matrices simétricas
    print(f"Eigenvalores: {eigenvals}\nEigenvectores:\n{eigenvecs}")
    print(f"\nOrtogonalidad (V·V^T):\n{eigenvecs @ eigenvecs.T}")

    prop_var = eigenvals / np.sum(eigenvals)
    print(f"\nProporción de varianza explicada: {prop_var}")
    return eigenvals, eigenvecs

Sigma_ejemplo = np.array([[5, 2, 1], [2, 3, 0.5], [1, 0.5, 2]])
analisis_espectral_completo(Sigma_ejemplo)
```

### 7.3 Blanqueamiento (Whitening)
El blanqueamiento transforma los datos para que tengan media cero y covarianza identidad: $Z = W(X-\mu)$, con $W\Sigma W^T = I$. Existen tres variantes: **ZCA** (mantiene la orientación original, basado en distancia de Mahalanobis), **PCA** (rota los ejes según los eigenvectores) y **Cholesky** (usa factorización triangular inferior).

```python
class WhiteningTransformer:
    """Implementación de blanqueamiento gaussiano (ZCA, PCA o Cholesky)"""

    def __init__(self, method='zca'):
        self.method = method  # 'zca', 'pca', 'cholesky'

    def fit(self, X):
        self.mu = np.mean(X, axis=0)
        X_centered = X - self.mu
        self.Sigma = np.cov(X_centered, rowvar=False)
        self.eigenvals, self.eigenvecs = np.linalg.eigh(self.Sigma)

        if self.method == 'pca':
            self.W = self.eigenvecs @ np.diag(1.0 / np.sqrt(self.eigenvals)) @ self.eigenvecs.T
        elif self.method == 'zca':
            self.W = np.linalg.inv(self.eigenvecs @ np.diag(np.sqrt(self.eigenvals)) @ self.eigenvecs.T)
        else:  # Cholesky
            self.W = np.linalg.cholesky(np.linalg.inv(self.Sigma))
        return self

    def transform(self, X):
        return (X - self.mu) @ self.W.T

    def inverse_transform(self, Z):
        return Z @ np.linalg.inv(self.W.T) + self.mu

## Ejemplo de uso
X_data = np.random.multivariate_normal([1, 2], [[4, 2], [2, 3]], 1000)
whitener = WhiteningTransformer(method='zca').fit(X_data)
Z_white = whitener.transform(X_data)
print("Covarianza original:\n", np.cov(X_data.T))
print("\nCovarianza después de blanqueamiento:\n", np.cov(Z_white.T))
```

### 7.4 Análisis de Componentes Principales (PCA)
Dado $\mathbf{X}\in\mathbb{R}^{n\times p}$, PCA: (1) centra los datos $\mathbf{X}_c=\mathbf{X}-\mathbf{1}\mathbf{\mu}^T$; (2) descompone $\mathbf{X}_c^T\mathbf{X}_c=\mathbf{V}\mathbf{\Lambda}\mathbf{V}^T$; (3) proyecta $\mathbf{Y}=\mathbf{X}_c\mathbf{V}_k$ sobre las $k$ direcciones de mayor varianza.

```python
class PCAFromScratch:
    """Implementación de PCA desde primeros principios"""

    def __init__(self, n_components=None):
        self.n_components = n_components

    def fit(self, X):
        self.mean_ = np.mean(X, axis=0)
        X_centered = X - self.mean_
        n_samples = X.shape[0]
        self.cov_matrix_ = (X_centered.T @ X_centered) / (n_samples - 1)

        eigenvals, eigenvecs = np.linalg.eigh(self.cov_matrix_)
        idx = np.argsort(eigenvals)[::-1]  # descendente
        self.eigenvalues_ = eigenvals[idx]
        self.components_ = eigenvecs[:, idx]

        if self.n_components is not None:
            self.components_ = self.components_[:, :self.n_components]
            self.eigenvalues_ = self.eigenvalues_[:self.n_components]

        self.explained_variance_ratio_ = self.eigenvalues_ / np.sum(self.eigenvalues_)
        return self

    def transform(self, X):
        return (X - self.mean_) @ self.components_

    def inverse_transform(self, Y):
        return Y @ self.components_.T + self.mean_

## Comparación con scikit-learn
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data

pca_scratch = PCAFromScratch(n_components=2).fit(X)
pca_sklearn = PCA(n_components=2).fit(X)

print("Varianza explicada (scratch):", pca_scratch.explained_variance_ratio_)
print("Varianza explicada (sklearn):", pca_sklearn.explained_variance_ratio_)
```

**Limitaciones de PCA**: (1) solo captura relaciones lineales; (2) maximiza varianza, no necesariamente información relevante para la tarea; (3) sensible a la escala (requiere estandarización previa); (4) sensible a outliers. Alternativas no lineales incluyen t-SNE, UMAP y autoencoders.

---

## 8. Código de Verificación Simbólica (SymPy)

```python
import sympy as sp
from IPython.display import display, Math

x, y = sp.symbols('x y', real=True)
c = sp.Symbol('c', positive=True)

## Densidad conjunta f(x,y) = c * x * y en [0,1]x[0,1]
f_xy_sym = c * x * y

## Cálculo de la constante de normalización 'c'
integral_doble = sp.integrate(f_xy_sym, (x, 0, 1), (y, 0, 1))
c_resuelto = sp.solve(integral_doble - 1, c)[0]

display(Math(r'\text{Constante de Normalización } c: ' + sp.latex(c_resuelto)))
display(Math(r'\text{Densidad Conjunta Validada } f(x,y): ' + sp.latex(c_resuelto * x * y)))
```

---

## 9. Solución Computacional en Python (SciPy & Statsmodels): Simulación Bivariada por Cholesky

Para simular vectores aleatorios continuos bivariados $(X,Y)$ con matriz de covarianza especificada $\Sigma$, se utiliza la **Descomposición de Cholesky** $\Sigma=LL^T$. Dado $Z=(Z_1,Z_2)^T\sim\mathcal{N}(0,I_2)$ independientes:
$$X = \mu + LZ \implies X \sim \mathcal{N}(\mu, \Sigma)$$

```python
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, Math

## Parámetros: [Diámetro (nm), Potencial Zeta (mV)] de nanopartículas coloidales
mu = np.array([25.0, -40.0])
cov = np.array([
    [16.0, -18.0],   # Varianza X=16, Cov(X,Y)=-18
    [-18.0, 36.0]    # Varianza Y=36
])

## Descomposición de Cholesky
L = np.linalg.cholesky(cov)

## Muestreo
np.random.seed(99)
Z = stats.norm.rvs(size=(2, 10_000))
muestras_bivariadas = (mu.reshape(2, 1) + L @ Z).T

## Visualización
df_bivariado = pd.DataFrame(muestras_bivariadas, columns=["Diametro_nm", "PotencialZeta_mV"])
g = sns.jointplot(data=df_bivariado, x="Diametro_nm", y="PotencialZeta_mV", kind="kde", cmap="Blues", fill=True)
g.fig.suptitle("Simulación Bivariada por Cholesky: Diámetro vs Potencial Zeta", y=1.02, fontweight="bold")
plt.show()

cov_sim = np.cov(muestras_bivariadas.T)
display(Math(fr"\text{{Covarianza Simulada: }} \text{{Cov}}(X, Y) = {cov_sim[0, 1]:.2f}"))
```

---

## 10. Interpretación Post-Gráfico & Diccionario de Variables

### 10.1 Interpretación de Resultados Computacionales
1. **Correlación Negativa Diámetro–Potencial Zeta**: el `jointplot` de densidad KDE muestra una nube elipsoidal claramente inclinada, confirmando visualmente la correlación $\rho=-0.75$ calculada analíticamente entre el diámetro de la nanopartícula y su potencial zeta, y la covarianza simulada converge al valor teórico de $-18$ conforme $n\to\infty$.
2. **PCA como Herramienta de Reducción de Dimensionalidad**: al aplicar `PCAFromScratch` sobre datos correlacionados (2D o 3D), la primera componente principal (PC1) captura la dirección de máxima varianza conjunta — en un contexto de caracterización de nanopartículas, esto permitiría combinar múltiples mediciones fisicoquímicas correlacionadas (diámetro, potencial zeta, índice de polidispersidad) en un único índice de calidad del lote.
3. **Whitening como Preprocesamiento**: la transformación de blanqueamiento (ZCA/PCA/Cholesky) deja la covarianza en la identidad, eliminando la correlación estructural entre variables — un paso común antes de alimentar datos de caracterización de nanomateriales a modelos de aprendizaje automático que asumen features no correlacionados.

### 10.2 Diccionario de Variables Nanotecnológicas
* $X$: diámetro de la nanopartícula coloidal (nm).
* $Y$: potencial zeta de la nanopartícula ($\zeta$, mV), medida de la carga superficial efectiva y de la estabilidad electrostática de la suspensión.
* $\mu, \Sigma$: vector de medias y matriz de covarianza del vector aleatorio bivariado $(X,Y)$ del lote de síntesis.
* $\rho_{X,Y}$: coeficiente de correlación entre diámetro y potencial zeta ($-0.75$ en el ejemplo), indicador de la fuerza de la relación inversa tamaño–carga superficial.
* $L$: factor de Cholesky de $\Sigma$, usado para simular pares $(X,Y)$ correlacionados a partir de ruido gaussiano independiente.

## Errores Comunes / Misconceptions

* **Error**: Concluir que dos variables aleatorias son independientes porque su covarianza (o correlación) es cero.
  **Correcto**: $\text{Cov}(X,Y) = 0$ es condición necesaria pero no suficiente para independencia en el caso general — solo mide dependencia *lineal*. Existen variables con dependencia fuerte (p. ej. $Y = X^2$ con $X$ simétrica alrededor de 0) y covarianza cero. La equivalencia covarianza-cero-implica-independencia solo se sostiene en el caso particular de la Normal bivariada.

* **Error**: Confundir la distribución marginal $f_X(x)$ con la distribución condicional $f_{X|Y}(x|y)$.
  **Correcto**: la marginal describe el comportamiento de $X$ ignorando (integrando/sumando sobre) $Y$; la condicional describe el comportamiento de $X$ una vez fijado un valor específico de $Y$. Ambas coinciden solo si $X$ y $Y$ son independientes.

* **Error**: Calcular la varianza de la suma $X+Y$ como $\text{Var}(X) + \text{Var}(Y)$ sin verificar independencia (o covarianza nula).
  **Correcto**: en general $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2\,\text{Cov}(X,Y)$. Omitir el término de covarianza subestima la varianza real cuando las variables están correlacionadas positivamente (y la sobrestima si la correlación es negativa).

## Ejercicio Propuesto

Un nanocompuesto polimérico reforzado con nanopartículas cerámicas tiene dos propiedades correlacionadas: el diámetro de partícula $X$ (nm) y la conductividad térmica del compuesto $Y$ (W/m·K), con vector de medias $\mu = (30.0,\ 5.0)$ y matriz de covarianza:

$$\Sigma = \begin{pmatrix} 9.0 & 6.0 \\ 6.0 & 16.0 \end{pmatrix}$$

1. Calcula el coeficiente de correlación $\rho_{X,Y}$ a partir de $\Sigma$.
2. Calcula $\text{Var}(X+Y)$ usando la fórmula completa (incluyendo el término de covarianza) y compárala con el resultado que se obtendría omitiendo por error dicho término.
3. Verifica que $\Sigma$ es una matriz de covarianza válida obteniendo su descomposición de Cholesky $L$ (si `numpy.linalg.cholesky` no lanza error, $\Sigma$ es semidefinida positiva).

Escribe tu solución en una celda de código nueva en tu notebook. La celda de autoevaluación de la siguiente sección verificará tu resultado.

## Referencias

* Agresti, A. & Kateri, M. (2022). *Foundations of Statistics for Data Scientists: With R and Python*. Chapman & Hall/CRC (Texts in Statistical Science). Capítulos sobre distribuciones multivariadas y dependencia entre variables aleatorias.
* Virtanen, P. et al. (2020). SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. *Nature Methods*, 17, 261-272. Documentación: [docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html)
