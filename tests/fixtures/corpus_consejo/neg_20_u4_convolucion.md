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

> ⚠️ **Nota sobre esta Poisson en particular**: en el cálculo anterior, $E[X]=\text{Var}(X)=\lambda=2$ coinciden porque $X$ es Poisson — es una propiedad exclusiva de esa familia, no una coincidencia general. Si $X$ siguiera otra distribución (p. ej. Binomial), $E[X]$ y $\text{Var}(X)$ tomarían valores distintos y ambos términos de la Ley de la Varianza Total deberían calcularse por separado sin ese atajo.

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
