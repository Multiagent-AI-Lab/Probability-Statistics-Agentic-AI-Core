
### 2.3 Ejemplo (Comprobación de Independencia, Discreto)
Con las marginales y conjunta de la tabla anterior: $P_X(1)=9/15$, $P_Y(1)=10/15$, $P_{X,Y}(1,1)=6/15$.

Si fueran independientes se debería cumplir $P_X(1)\cdot P_Y(1) = \frac{9}{15}\cdot\frac{10}{15} = \frac{90}{225} = 0.4$. Como $P_{X,Y}(1,1)=6/15=0.4$ también, la igualdad se sostiene para este par; verificándola en todos los pares $(x,y)$ se confirma si $X$ y $Y$ son independientes.

### 2.4 Ejemplo (Continuo)
Sea $f_{X,Y}(x,y)=2$ en el triángulo $0\le y\le x\le1$ y $0$ en otro caso.
* Marginal de $X$: $f_X(x)=\int_0^{x}2\,dy=2x$
* Marginal de $Y$: $f_Y(y)=\int_y^{1}2\,dx=2(1-y)$
* Producto: $f_X(x)f_Y(y)=4x(1-y)$, que **no coincide** con $f_{X,Y}(x,y)=2$; luego $X$ y $Y$ **no son independientes**.

### 2.5 Segundo Ejemplo (Continuo): Verificación de Independencia por Dos Métodos

El ejemplo anterior confirma dependencia porque el producto de marginales **no coincide** con la conjunta. El siguiente ejemplo muestra el caso contrario —confirmar independencia— y añade un segundo método de verificación: la PDF conjunta $f_{X,Y}(x,y)=2xe^{-(x+2y)}$ para $x,y\ge0$ modela el tiempo hasta el primer defecto detectable ($X$) y la profundidad de penetración de un recubrimiento protector ($Y$) en un proceso de pasivación de superficies.

**Paso 1 — Marginales**: separando la exponencial doble en factores integrables por separado:
$$f_X(x) = \int_0^\infty 2xe^{-(x+2y)}\,dy = 2xe^{-x}\int_0^\infty e^{-2y}\,dy = 2xe^{-x}\cdot\frac{1}{2} = xe^{-x}$$
$$f_Y(y) = \int_0^\infty 2xe^{-(x+2y)}\,dx = 2e^{-2y}\int_0^\infty xe^{-x}\,dx = 2e^{-2y}\cdot 1 = 2e^{-2y}$$
(la integral $\int_0^\infty xe^{-x}\,dx=1$ es la función Gamma $\Gamma(2)=1!=1$, así que $f_X(x)=xe^{-x}$ es una $\text{Gamma}(k=2,\theta=1)$, y $f_Y(y)=2e^{-2y}$ es una $\text{Exponencial}(\lambda=2)$).

**Paso 2 — Método 1: factorización directa**: $f_X(x)\cdot f_Y(y) = (xe^{-x})(2e^{-2y}) = 2xe^{-(x+2y)} = f_{X,Y}(x,y)$ ✓ — coincide exactamente, luego $X$ y $Y$ **son independientes**.

**Paso 3 — Método 2: la condicional no depende de la condicionante**: como verificación alternativa (útil cuando no es evidente cómo factorizar la conjunta a simple vista):
$$f_{X|Y}(x|y) = \frac{f_{X,Y}(x,y)}{f_Y(y)} = \frac{2xe^{-(x+2y)}}{2e^{-2y}} = xe^{-x}$$
El resultado **no contiene $y$** — la distribución condicional de $X$ es idéntica para cualquier valor fijo de $Y$, que es exactamente la definición de independencia ($f_{X|Y}(x|y)=f_X(x)$ para todo $y$).

```python
import numpy as np
from scipy.integrate import dblquad

def f_xy(x, y):
    return 2 * x * np.exp(-(x + 2 * y))

## Verificacion 1: covarianza teoricamente nula si son independientes
E_X, _ = dblquad(lambda y, x: x * f_xy(x, y), 0, np.inf, 0, np.inf)
E_Y, _ = dblquad(lambda y, x: y * f_xy(x, y), 0, np.inf, 0, np.inf)
E_XY, _ = dblquad(lambda y, x: x * y * f_xy(x, y), 0, np.inf, 0, np.inf)
cov_xy = E_XY - E_X * E_Y

## Verificacion 2: simulacion Monte Carlo de la covarianza muestral
rng = np.random.default_rng(42)
X_sim = rng.gamma(shape=2, scale=1, size=200_000)   # marginal de X: Gamma(k=2, theta=1)
Y_sim = rng.exponential(scale=1 / 2, size=200_000)  # marginal de Y: Exponencial(lambda=2)
cov_sim = np.cov(X_sim, Y_sim)[0, 1]

print(f"E[X]={E_X:.4f}  E[Y]={E_Y:.4f}  E[XY]={E_XY:.4f}")
print(f"Cov(X,Y) analitica (deberia ser ~0):  {cov_xy:.6f}")
print(f"Cov(X,Y) simulada (variables independientes generadas por separado): {cov_sim:.6f}")
```

**Verificación simbólica (SymPy) de la factorización**: en vez de solo verificar numéricamente que la covarianza es aproximadamente cero, se puede confirmar de forma exacta —vía integración simbólica— que las marginales obtenidas en el Paso 1 son las que efectivamente factorizan la conjunta:

```python
import sympy as sp

x, y = sp.symbols('x y', positive=True)
f_xy_sym = 2 * x * sp.exp(-(x + 2 * y))

## Integracion simbolica de la conjunta para obtener cada marginal
f_x_sym = sp.simplify(sp.integrate(f_xy_sym, (y, 0, sp.oo)))
f_y_sym = sp.simplify(sp.integrate(f_xy_sym, (x, 0, sp.oo)))
print(f"f_X(x) = {f_x_sym}")  # debe dar x*exp(-x)
print(f"f_Y(y) = {f_y_sym}")  # debe dar 2*exp(-2*y)

## Confirmacion simbolica de independencia: f_X(x)*f_Y(y) == f_XY(x,y)
producto_marginales = sp.simplify(f_x_sym * f_y_sym)
diferencia = sp.simplify(producto_marginales - f_xy_sym)
print(f"f_X(x)*f_Y(y) = {producto_marginales}")
print(f"Coincide exactamente con f_X,Y(x,y): {diferencia == 0}")
```

Nótese que la simulación genera $X$ y $Y$ **por separado** (cada una de su propia marginal, sin acoplarlas) precisamente porque ya se demostró que son independientes — esa es la ventaja práctica de probar independencia analíticamente antes de simular: permite generar cada variable con su propio generador estándar (`rng.gamma`, `rng.exponential`) en vez de necesitar un método de simulación conjunta más complejo (como la Cholesky de la Sección 5.4, necesaria quando SÍ hay dependencia).

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

### 3.4 Ley de la Esperanza Total: Ejemplo Continuo Completo

El ejemplo anterior ($E[Y|X=x]=2x+1$) muestra la mecánica algebraica de la Ley de la Esperanza Total, pero con una relación condicional ya lineal en $x$ dada de antemano. El siguiente ejemplo desarrolla el caso continuo desde una PDF real, con $X$ representando un parámetro de proceso: la temperatura de recocido de puntos cuánticos de grafeno (GQD) para celdas solares, $X\sim U(200,300)\ ^\circ\text{C}$, con eficiencia condicional $E[Y|X=x]=20+0.1x$ ($\%$).

Por la Ley de la Esperanza Total continua:
$$E[Y] = \int_{-\infty}^{\infty} E[Y|X=x]\,f_X(x)\,dx = \int_{200}^{300} (20+0.1x)\cdot\frac{1}{100}\,dx$$

$$E[Y] = \frac{1}{100}\left[20x + 0.05x^2\right]_{200}^{300} = \frac{1}{100}\big[(6000+4500)-(4000+2000)\big] = \frac{4500}{100} = \boxed{45.0\%}$$

```python
from scipy import integrate

a, b = 200, 300  # soporte de X ~ U(200, 300)
alpha, beta = 20, 0.1  # E[Y|X=x] = alpha + beta*x


def esperanza_condicional(x):
    return alpha + beta * x


def pdf_uniforme(x):
    return 1 / (b - a) if a <= x <= b else 0


def integrando_let(x):
    return esperanza_condicional(x) * pdf_uniforme(x)


E_Y_quad, error = integrate.quad(integrando_let, a, b)
print(f"E[Y] via LET (quad): {E_Y_quad:.4f}%  (error estimado: {error:.2e})")
```

**Verificación simbólica (SymPy)**: la integral anterior se resolvió numéricamente vía `quad`; a continuación se repite el mismo cálculo mediante integración simbólica exacta, sustituyendo $E[Y|X=x]=20+0.1x$ y la densidad uniforme $f_X(x)=1/100$ ya establecidas en el texto:

```python
import sympy as sp

x = sp.symbols('x', positive=True)
a_sym, b_sym = 200, 300
alpha_sym, beta_sym = 20, sp.Rational(1, 10)

e_y_dado_x = alpha_sym + beta_sym * x  # E[Y|X=x] = 20 + 0.1x, ya establecido arriba
f_x_uniforme = sp.Rational(1, b_sym - a_sym)  # densidad uniforme f_X(x) = 1/(300-200)

E_Y_sym = sp.integrate(e_y_dado_x * f_x_uniforme, (x, a_sym, b_sym))
E_Y_sym = sp.simplify(E_Y_sym)
print(f"E[Y] via integracion simbolica: {E_Y_sym} = {float(E_Y_sym)}%")  # debe dar 45.0
```

Este resultado es la base para el ejemplo mixto (discreto-continuo) de la Sección 3.5, que extiende la misma idea —promediar una esperanza condicional sobre la distribución de la variable condicionante— a un caso donde además se necesita descomponer la varianza total.

### 3.5 Ley de la Varianza Total: Ejemplo Mixto Discreto-Continuo

Cuando $E[Y|X=x]$ **depende de $x$** (como en 3.4), la varianza de $Y$ no es simplemente $E[\text{Var}(Y|X)]$: parte de la variabilidad de $Y$ proviene de que su propia media condicional cambia con $X$. La **Ley de la Varianza Total** descompone esto en dos términos:

$$\text{Var}(Y) = \underbrace{\mathbb{E}[\text{Var}(Y|X)]}_{\text{variabilidad "dentro" de cada valor de }X} + \underbrace{\text{Var}(\mathbb{E}[Y|X])}_{\text{variabilidad "entre" distintos valores de }X}$$

**Contexto aplicado**: la resistencia eléctrica de un *nanowire* ($Y$, en $\Omega$) depende del número de defectos puntuales en la red cristalina ($X$, discreto), con $X\sim\text{Poisson}(\lambda=2)$. La relación condicional es $E[Y|X=x]=100+10x$ y, crucialmente, la varianza condicional **no es constante**: $\text{Var}(Y|X=x)=5x$ (más defectos no solo aumentan la resistencia esperada, también la hacen menos predecible — **heterocedasticidad**).

**Solución analítica vía LET**: para Poisson($\lambda$), $E[X]=\lambda=2$, así:
$$E[Y] = E[E[Y|X]] = E[100+10X] = 100+10E[X] = 100+10(2) = \boxed{120.0\ \Omega}$$

**Solución analítica vía Ley de la Varianza Total**: usando $E[\text{Var}(Y|X)]=E[5X]=5E[X]=5(2)=10$, y $\text{Var}(E[Y|X])=\text{Var}(100+10X)=10^2\text{Var}(X)=100\cdot\lambda=100(2)=200$ (recordando que para Poisson, $\text{Var}(X)=\lambda$ también):

$$\text{Var}(Y) = \underbrace{E[5X]}_{10} + \underbrace{\text{Var}(100+10X)}_{200} = 10+200 = \boxed{210.0\ \Omega^2}$$

```python
import numpy as np
from scipy.stats import poisson

alpha, beta, gamma = 100, 10, 5  # E[Y|X]=alpha+beta*X, Var(Y|X)=gamma*X
lambda_poisson = 2
N = 10_000

## 1. Simular X ~ Poisson(lambda) -- numero de defectos por nanowire
X_samples = poisson.rvs(mu=lambda_poisson, size=N)

## 2. Para cada X_i, calcular los parametros de la Y condicional (heterocedastica)
mu_y_condicional = alpha + beta * X_samples
sigma_y_condicional = np.sqrt(gamma * X_samples)

## 3. Simular Y_i ~ N(mu_y_condicional[i], sigma_y_condicional[i]^2)
Y_samples = np.random.normal(loc=mu_y_condicional, scale=sigma_y_condicional)

## 4. Comparar promedio simulado contra el valor analitico de la LET
E_Y_simulado = np.mean(Y_samples)
print(f"E[Y] simulado (Monte Carlo, N={N}):  {E_Y_simulado:.4f}")
print(f"E[Y] analitico (Ley Esperanza Total): {100 + 10 * lambda_poisson:.4f}")

## 5. Ley de la Varianza Total: descomposicion en los dos terminos aditivos
E_de_Var_Y_dado_X = gamma * lambda_poisson       # E[Var(Y|X)] = E[5X] = 5*E[X]
Var_de_E_Y_dado_X = beta**2 * lambda_poisson      # Var(100+10X) = 100*Var(X) = 100*lambda
Var_Y_total_analitico = E_de_Var_Y_dado_X + Var_de_E_Y_dado_X

print(f"\nE[Var(Y|X)]          = {E_de_Var_Y_dado_X:.4f}")
print(f"Var(E[Y|X])           = {Var_de_E_Y_dado_X:.4f}")
print(f"Var(Y) total analitico = {Var_Y_total_analitico:.4f}")
print(f"Var(Y) simulado        = {np.var(Y_samples):.4f}")
```

**Verificación simbólica (SymPy)**: la descomposición anterior usa $E[X]=\text{Var}(X)=\lambda$ como hechos conocidos de la Poisson; a continuación se deriva esa propiedad simbólicamente a partir de la función generadora de momentos $M_X(t)=e^{\lambda(e^t-1)}$ ($E[X]=M_X'(0)$, $\text{Var}(X)=M_X''(0)-M_X'(0)^2$), y luego se sustituye en la descomposición aditiva de la Ley de la Varianza Total con $E[Y|X]=\alpha+\beta X$ y $\text{Var}(Y|X)=\gamma X$ dejados simbólicos hasta el final:

```python
import sympy as sp

alpha, beta, gamma, lam, t, X = sp.symbols('alpha beta gamma lambda t X', positive=True)

## E[X] y Var(X) para X ~ Poisson(lambda), derivados de la funcion generadora de momentos
mgf_poisson = sp.exp(lam * (sp.exp(t) - 1))
E_X_sym = sp.diff(mgf_poisson, t).subs(t, 0)
E_X2_sym = sp.diff(mgf_poisson, t, 2).subs(t, 0)
Var_X_sym = sp.simplify(E_X2_sym - E_X_sym**2)
print(f"E[X] (via MGF de Poisson)   = {E_X_sym}")   # debe dar lambda
print(f"Var[X] (via MGF de Poisson) = {Var_X_sym}")  # debe dar lambda

## Descomposicion simbolica: E[Var(Y|X)] = E[gamma*X] = gamma*E[X]
E_de_Var_Y_dado_X_sym = sp.simplify(gamma * E_X_sym)
## Var(E[Y|X]) = Var(alpha + beta*X) = beta^2 * Var(X)
Var_de_E_Y_dado_X_sym = sp.simplify(beta**2 * Var_X_sym)
Var_Y_total_sym = sp.simplify(E_de_Var_Y_dado_X_sym + Var_de_E_Y_dado_X_sym)
print(f"E[Var(Y|X)]  simbolico = {E_de_Var_Y_dado_X_sym}")
print(f"Var(E[Y|X])  simbolico = {Var_de_E_Y_dado_X_sym}")
print(f"Var(Y) total simbolico = {Var_Y_total_sym}")

## Sustitucion numerica: alpha=100, beta=10, gamma=5, lambda=2
valores = {alpha: 100, beta: 10, gamma: 5, lam: 2}
print(f"\nE[Var(Y|X)]  = {E_de_Var_Y_dado_X_sym.subs(valores)}")   # debe dar 10
print(f"Var(E[Y|X])  = {Var_de_E_Y_dado_X_sym.subs(valores)}")     # debe dar 200
print(f"Var(Y) total = {Var_Y_total_sym.subs(valores)}")           # debe dar 210
```

**Interpretación**: en planificación de manufactura, la LET y la Ley de la Varianza Total permiten a un ingeniero de procesos separar dos preguntas distintas: "¿cuál es la resistencia promedio esperada del producto final?" (respondida por $E[Y]=120\ \Omega$, integrando la tasa de defectos del proceso) y "¿qué tan dispersos serán los resultados, y por qué?" (respondida por la descomposición $210=10+200$, que revela que la mayor parte de la variabilidad total —$200$ de $210$— proviene de la variación *entre* lotes con distinto número de defectos, no de la variabilidad *dentro* de un mismo nivel de defectos). Esta distinción es la que determina si conviene invertir en reducir el número medio de defectos ($\lambda$) o en hacer más consistente la resistencia para un nivel de defectos fijo.
