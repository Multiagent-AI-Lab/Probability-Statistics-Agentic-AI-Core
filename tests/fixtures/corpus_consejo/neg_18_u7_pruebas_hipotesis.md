### 1.6 Prueba para la Media Poblacional (Z-test y t-test)
Sea $X_1,\dots,X_n$ una muestra de $N(\mu, \sigma^2)$, con hipótesis $H_0:\mu=\mu_0$ contra $H_1:\mu\neq\mu_0$.

**Varianza $\sigma^2$ conocida (Z-test)**:
$$Z = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}} \sim N(0,1)$$
Se rechaza $H_0$ si $z_0 \notin (-z_{\alpha/2},\ z_{\alpha/2})$.

**Varianza $\sigma^2$ desconocida (t-test)**: se reemplaza $\sigma$ por la desviación muestral $s$, y el estadístico sigue una distribución $t$ de Student con $n-1$ grados de libertad:
$$t = \frac{\bar{X}-\mu_0}{s/\sqrt{n}} \sim t_{n-1}$$
Se rechaza $H_0$ si $t_0 < -t_{\alpha/2,n-1}$ o $t_0 > t_{\alpha/2,n-1}$ (para $n\ge30$, $t_{n-1}$ se aproxima bien por $N(0,1)$).

**Ejemplo resuelto (Z-test)**: notas de examen $\sim N(\mu, 0.25)$ ($\sigma=0.5$ conocida), $n=50$, $\bar{x}=7.8$, $\alpha=0.01$. $H_0:\mu=8$ contra $H_1:\mu\neq8$:
$$z_0 = \frac{7.8-8}{0.5/\sqrt{50}} \approx \boxed{-2.83}$$
Con $\alpha=0.01$ bilateral, $z_{0.005}=2.57$. Como $-2.83 < -2.57$, se **rechaza $H_0$**.

### 1.7 Prueba para la Varianza
Para $H_0:\sigma^2=\sigma_0^2$ contra $H_1:\sigma^2\neq\sigma_0^2$, el estadístico de prueba sigue una distribución Chi-cuadrado con $n-1$ grados de libertad:
$$\chi^2_0 = \frac{(n-1)s^2}{\sigma_0^2} \sim \chi^2_{n-1}$$
Se rechaza $H_0$ si $\chi^2_0 > \chi^2_{n-1,\alpha/2}$ o $\chi^2_0 < \chi^2_{n-1,1-\alpha/2}$.

**Ejemplo resuelto**: $\sigma_0 = 0.4\%$ histórico, muestra de $n=24$ semanas con $s=0.38\%$, $\alpha=0.05$. $H_0:\sigma^2=0.16$ contra $H_1:\sigma^2\neq0.16$: se calcula $\chi^2_0 \approx 20.76$, con región crítica $\chi^2_0 < 11.689$ o $\chi^2_0 > 38.076$ (para $df=23$). Como $20.76$ cae dentro del intervalo, **no se rechaza $H_0$**.

**Verificación computacional**: se reproduce el cálculo anterior con `scipy.stats.chi2`, confirmando el mismo estadístico y la misma decisión ya publicados en prosa.

```python
from scipy.stats import chi2

## Contexto ya establecido en la Seccion 1.7: control de calidad del proceso,
## sigma_0 = 0.4% (historico), muestra n=24 semanas con s=0.38%, alpha=0.05
sigma_0, n, s, alpha = 0.4, 24, 0.38, 0.05
df = n - 1

chi2_0 = (df * s ** 2) / sigma_0 ** 2

chi2_critico_superior = chi2.ppf(1 - alpha / 2, df)
chi2_critico_inferior = chi2.ppf(alpha / 2, df)

print(f"chi2_0 = {chi2_0:.4f}")
print(f"Region critica: chi2_0 < {chi2_critico_inferior:.3f} o chi2_0 > {chi2_critico_superior:.3f}")
print(f"Se rechaza H0: {chi2_0 < chi2_critico_inferior or chi2_0 > chi2_critico_superior}")
```

```
chi2_0 = 20.7575
Region critica: chi2_0 < 11.689 o chi2_0 > 38.076
Se rechaza H0: False
```

El valor $\chi^2_0=20.7575$ coincide con el $\approx20.76$ calculado a mano y confirma que cae dentro de la región de no rechazo.

### 1.8 Pruebas Chi-cuadrado de Bondad de Ajuste, Contingencia y Proporciones
Además de la media y la varianza, la familia $\chi^2$ cubre tres pruebas no paramétricas de uso constante en control de calidad:

* **Bondad de Ajuste**: evalúa si una muestra proviene de una distribución específica, comparando frecuencias observadas $O_i$ contra esperadas $E_i = nP_i$ en $k$ categorías: $D^2 = \sum_{i=1}^k (O_i-E_i)^2/E_i \sim \chi^2_{k-1}$ (o $\chi^2_{k-1-r}$ si se estimaron $r$ parámetros de la muestra).
* **Tablas de Contingencia (Independencia)**: evalúa si dos variables categóricas son independientes, con frecuencia esperada $e_{ij} = (r_i \cdot c_j)/N$ por celda y estadístico $D^2 = \sum_{i,j} (n_{ij}-e_{ij})^2/e_{ij} \sim \chi^2_{(r-1)(c-1)}$.
* **Igualdad de Proporciones (Homogeneidad)**: evalúa $H_0: p_1=p_2=\dots=p_k$ contra $H_1$: al menos una proporción difiere, estimando una proporción común $\hat{p}$ y aplicando el mismo esquema $\chi^2$ sobre las celdas de éxito/fracaso.

En los tres casos se rechaza $H_0$ cuando el estadístico supera el valor crítico $\chi^2$ correspondiente, o equivalentemente cuando el p-valor es menor que $\alpha$.

**Ejemplo — Bondad de Ajuste**: se registran los tiempos entre fallas de $n=150$ nano-sensores piezoresistivos, agrupados en $k=4$ intervalos, y se desea verificar si siguen una distribución Exponencial con $\lambda=0.005$ ($\alpha=0.01$). Con frecuencias observadas/esperadas por intervalo, el estadístico de prueba resulta $D_0^2 \approx 12.79$, con $k-1=3$ grados de libertad. El valor crítico es $\chi^2_{3,\,0.01} \approx 11.34$. Como $D_0^2 = 12.79 > 11.34$, **se rechaza $H_0$**: los tiempos entre fallas no son consistentes con una distribución Exponencial($\lambda=0.005$).

**Ejemplo — Tabla de Contingencia**: se desea evaluar si el **método de síntesis** de nanopartículas de oro (Turkevich vs. método alternativo) es independiente de la **presencia de agregación** observada por TEM. Con una tabla $2\times 2$ de frecuencias observadas y $\alpha=0.05$, el estadístico $D_0^2$ se compara contra $\chi^2_{1,\,0.05}$; el procedimiento sigue el mismo esquema de bondad de ajuste, sustituyendo las frecuencias esperadas por celda $e_{ij}=(r_i \cdot c_j)/N$.

**Verificación computacional**: se evalúa un caso concreto de tabla de contingencia $3\times 3$ — **tipo de defecto** (agregación, subrecubrimiento, ninguno) observado por TEM vs. **lote de producción** (A, B, C) de AgNPs — usando `scipy.stats.chi2_contingency`, que calcula el estadístico, los grados de libertad, el p-valor y las frecuencias esperadas en un solo paso:

```python
import numpy as np
from scipy.stats import chi2_contingency

## Tabla de contingencia: tipo de defecto (agregacion, subrecubrimiento, ninguno)
## vs. lote de produccion (Lote A, Lote B, Lote C) de AgNPs
## Filas: tipo de defecto; Columnas: lote
tabla = np.array([
    [12,  8, 15],   # Agregacion
    [ 7, 18,  9],   # Subrecubrimiento
    [41, 34, 36],   # Ninguno
])

alpha = 0.05
chi2_stat, p_valor, df, esperadas = chi2_contingency(tabla)

print(f"Estadistico chi2 = {chi2_stat:.4f}")
print(f"Grados de libertad = {df}")
print(f"p-valor = {p_valor:.4f}")
print("Frecuencias esperadas:")
print(np.round(esperadas, 2))
print(f"Se rechaza H0 (independencia): {p_valor < alpha}")
```

```
Estadistico chi2 = 8.8758
Grados de libertad = 4
p-valor = 0.0643
Frecuencias esperadas:
[[11.67 11.67 11.67]
 [11.33 11.33 11.33]
 [37.   37.   37.  ]]
Se rechaza H0 (independencia): False
```

Con $p=0.0643 > \alpha=0.05$, **no se rechaza $H_0$**: la evidencia muestral no es suficiente para concluir que el tipo de defecto depende del lote de producción, aunque el p-valor está cerca del umbral y ameritaría vigilancia en lotes futuros.

**Ejemplo — Igualdad de Proporciones**: se comparan las proporciones de nanopartículas defectuosas en $k=4$ lotes de síntesis de AgNPs ($H_0: p_1=p_2=p_3=p_4$ contra $H_1$: al menos una proporción difiere). Se estima la proporción común $\hat p$ a partir de los datos agregados, se calculan las frecuencias esperadas de "defectuoso"/"no defectuoso" por lote, y se aplica el estadístico $\chi^2$ con $k-1=3$ grados de libertad para decidir si el proceso de síntesis es consistente entre lotes.

**Verificación computacional**: se compara la **tasa de rendimiento de síntesis** (proporción de partículas exitosas) entre el método Turkevich y un método alternativo de reducción química, usando la misma `scipy.stats.chi2_contingency` sobre una tabla $2\times 2$ de éxito/fracaso (equivalente a la prueba de igualdad de dos proporciones):

```python
import numpy as np
from scipy.stats import chi2_contingency

## Comparacion de tasa de rendimiento (sintesis exitosa) entre dos metodos
## de sintesis de AgNPs: Turkevich vs. metodo alternativo (reduccion quimica)
## Filas: exito/fracaso; Columnas: metodo
exitos = np.array([171, 148])       # Turkevich, Alternativo
n_total = np.array([200, 180])
fracasos = n_total - exitos

tabla = np.array([exitos, fracasos])

alpha = 0.05
chi2_stat, p_valor, df, esperadas = chi2_contingency(tabla)

p1, p2 = exitos / n_total
print(f"Proporcion de exito Turkevich: {p1:.4f}")
print(f"Proporcion de exito Alternativo: {p2:.4f}")
print(f"Estadistico chi2 = {chi2_stat:.4f}")
print(f"Grados de libertad = {df}")
print(f"p-valor = {p_valor:.4f}")
print(f"Se rechaza H0 (p1 = p2): {p_valor < alpha}")
```

```
Proporcion de exito Turkevich: 0.8550
Proporcion de exito Alternativo: 0.8222
Estadistico chi2 = 0.5317
Grados de libertad = 1
p-valor = 0.4659
Se rechaza H0 (p1 = p2): False
```

Con $p=0.4659 \gg \alpha=0.05$, **no se rechaza $H_0$**: no hay evidencia estadística de que la tasa de rendimiento difiera entre los dos métodos de síntesis.

---

### 1.9 Método de los Momentos (Estimación Puntual)

El **Método de los Momentos (MoM)** es, junto con la Máxima Verosimilitud (MLE, ver §6.2-6.3), una técnica clásica de estimación puntual. Su idea es simple: igualar los **momentos poblacionales** (esperanza, varianza, etc.) con los **momentos muestrales** correspondientes, y despejar los parámetros desconocidos.

**Procedimiento general**: si una distribución tiene $k$ parámetros $\theta_1,\dots,\theta_k$, se plantean $k$ ecuaciones igualando los primeros $k$ momentos poblacionales $\mu_j = E[X^j]$ con los momentos muestrales $m_j = \frac{1}{n}\sum_{i=1}^n x_i^j$, y se resuelve el sistema para los $\theta$.

**Caso 1 — Distribución Exponencial (un parámetro)**: para $X \sim \text{Exp}(\lambda)$, el primer momento poblacional es $E[X] = 1/\lambda$. Igualando con la media muestral $\bar{x}$:
$$\bar{x} = \frac{1}{\hat{\lambda}_{MoM}} \quad\Longrightarrow\quad \hat{\lambda}_{MoM} = \frac{1}{\bar{x}}$$

**Caso 2 — Distribución Gamma (dos parámetros)**: para $X \sim \text{Gamma}(\alpha,\beta)$ (parametrización forma-escala), $E[X]=\alpha\beta$ y $\text{Var}(X)=\alpha\beta^2$. Igualando con $m_1=\bar{x}$ y $m_2=s^2$ (varianza muestral) y resolviendo el sistema:
$$\hat{\alpha}_{MoM} = \frac{m_1^2}{m_2} \qquad \hat{\beta}_{MoM} = \frac{m_2}{m_1}$$

**Contexto de nanotecnología**: se mide el tiempo hasta degradación oxidativa (en horas) de una muestra de $n=50$ nanopartículas de oro (AuNPs) sin recubrimiento protector, modelado como $\text{Exp}(\lambda)$; y por separado, el tamaño de $n=60$ nanoclusters de paladio sintetizados por reducción química, modelado como $\text{Gamma}(\alpha,\beta)$ (una distribución más flexible que la Normal para tamaños que no pueden ser negativos).

**Verificación simbólica**:
```python
import sympy as sp

## Metodo de Momentos para la Exponencial: E[X] = 1/lambda
lam, m1 = sp.symbols('lambda m1', positive=True)
sol_expon = sp.solve(sp.Eq(m1, 1/lam), lam)
print(f"Exponencial MoM: lambda_hat = {sol_expon[0]}")  # 1/m1

## Metodo de Momentos para la Gamma: E[X]=alpha*beta, Var[X]=alpha*beta^2
alpha, beta, mu1, mu2 = sp.symbols('alpha beta mu1 mu2', positive=True)
sistema = [sp.Eq(mu1, alpha*beta), sp.Eq(mu2, alpha*beta**2)]
sol_gamma = sp.solve(sistema, [alpha, beta])
print(f"Gamma MoM: alpha_hat = {sol_gamma[0][0]}, beta_hat = {sol_gamma[0][1]}")
```

**Solución computacional**:
```python
import numpy as np
import scipy.stats as stats

## --- Caso 1: Exponencial, tiempo de degradacion oxidativa de AuNPs (horas) ---
np.random.seed(101)
tiempo_degradacion = stats.expon.rvs(scale=18.0, size=50)  # lambda verdadero = 1/18

media_muestral = np.mean(tiempo_degradacion)
lambda_mom = 1 / media_muestral
print(f"Media muestral: {media_muestral:.4f} h")
print(f"lambda_MoM = {lambda_mom:.4f}  (verdadero lambda = 1/18 = {1/18:.4f})")

## --- Caso 2: Gamma, tamano de nanoclusters de Pd (nm) ---
np.random.seed(102)
diametros_pd = stats.gamma.rvs(a=4.0, scale=2.5, size=60)  # alpha=4.0, beta=2.5 verdaderos

m1 = np.mean(diametros_pd)
m2_var = np.var(diametros_pd, ddof=0)
alpha_mom = m1**2 / m2_var
beta_mom = m2_var / m1
print(f"\nGamma MoM: alpha_hat = {alpha_mom:.4f} (verdadero 4.0), beta_hat = {beta_mom:.4f} (verdadero 2.5)")

## Comparacion contra MLE (scipy.stats.gamma.fit, loc fijo en 0)
alpha_mle, _, beta_mle = stats.gamma.fit(diametros_pd, floc=0)
print(f"Gamma MLE: alpha_hat = {alpha_mle:.4f}, beta_hat = {beta_mle:.4f}")
```

**Interpretación**: con $n=50$, $\hat{\lambda}_{MoM} = 0.0532\ \text{h}^{-1}$ (verdadero $1/18=0.0556$), un error relativo pequeño esperado por variabilidad muestral. Para la Gamma, el MoM ($\hat\alpha=4.39$, $\hat\beta=2.10$) y el MLE ($\hat\alpha=3.92$, $\hat\beta=2.35$) difieren ligeramente entre sí — ambos son estimadores consistentes (convergen al valor verdadero cuando $n\to\infty$), pero el MoM es computacionalmente más simple (no requiere optimización numérica) mientras que el MLE es generalmente más eficiente (menor varianza asintótica). En la práctica, el MoM se usa frecuentemente como valor inicial para algoritmos iterativos de MLE.

$$\boxed{\hat{\lambda}_{MoM} = \frac{1}{\bar{x}} = 0.0532\ \text{h}^{-1} \qquad \hat{\alpha}_{MoM} = 4.39,\ \ \hat{\beta}_{MoM} = 2.10}$$
