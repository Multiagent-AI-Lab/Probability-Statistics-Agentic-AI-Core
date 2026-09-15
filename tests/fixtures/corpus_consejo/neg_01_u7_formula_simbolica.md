### 5.3 Diccionario de Variables Nanotecnológicas del Ejemplo Aplicado
* $\mu_0$: diámetro medio histórico especificado del proceso de síntesis de AgNPs ($50\ \text{nm}$).
* $\sigma$: desviación estándar poblacional históricamente conocida del proceso ($4\ \text{nm}$).
* $\bar{x}$: diámetro medio muestral medido por DLS en el nuevo lote bajo control de calidad.
* $n$: tamaño de la muestra de nanopartículas analizadas.
* $z_0, t_0, \chi^2_0$: estadísticos de prueba observados para la media (varianza conocida/desconocida) y para la forma de la distribución de tamaños, respectivamente.
* $\alpha$: nivel de significancia, la probabilidad máxima tolerada de rechazar incorrectamente un lote que en realidad cumple la especificación (Error Tipo I).

---

## 6. Módulo Complementario: Estimación MLE y Bootstrap No Paramétrico

La inferencia moderna combina la **Estimación por Máxima Verosimilitud (MLE)** con el **remuestreo Bootstrap** para obtener intervalos de confianza empíricos sin asumir normalidad. El algoritmo de Bootstrap no paramétrico, dada una muestra $x_1,\dots,x_n$, consiste en:

1. Generar $B$ muestras con reemplazo de tamaño $n$: $x_b^*$.
2. Calcular el estimador $\hat{\theta}_b^*$ para cada réplica.
3. Construir el intervalo de confianza del $(1-\alpha)\times 100\%$ mediante los percentiles $[\alpha/2,\ 1-\alpha/2]$ de las $B$ estimaciones.

### 6.1 Inferencia Bootstrap en Python

El **Bootstrap no paramétrico** responde una pregunta que el enfoque analítico clásico (§1.6, IC basado en $t$/$Z$) solo resuelve bajo el supuesto de normalidad: ¿cuál es la incertidumbre de un estimador cuando **no** se conoce (o no se puede tabular fácilmente) su distribución muestral exacta? En vez de derivar una fórmula, el Bootstrap la **simula**: remuestrea la propia muestra observada, repitiendo el proceso miles de veces, para construir empíricamente la distribución del estimador.

**Contexto de nanotecnología**: se mide el tiempo hasta falla (en horas) de $n=40$ nano-sensores piezoresistivos bajo estrés acelerado, modelado como $\text{Exponencial}(\lambda)$. Se desea un intervalo de confianza del $95\%$ para el tiempo medio de falla $\mathbb{E}[X]=1/\lambda$, sin depender de la aproximación normal de la media muestral (válida asintóticamente, pero cuestionable con $n=40$ y una distribución tan asimétrica como la Exponencial).

```python
import numpy as np
import scipy.stats as stats
from IPython.display import display, Math

np.random.seed(42)
n = 40
muestra_exp = stats.expon.rvs(scale=12.5, size=n)  # tiempo hasta falla, muestra original

## --- Bootstrap no parametrico (B = 10,000 replicas) ---
B = 10_000
rng = np.random.default_rng(42)
medias_boot = np.array([
    np.mean(rng.choice(muestra_exp, size=n, replace=True)) for _ in range(B)
])

ic_boot_inf = np.percentile(medias_boot, 2.5)
ic_boot_sup = np.percentile(medias_boot, 97.5)

## --- Comparacion: IC analitico aproximado por el Teorema del Limite Central ---
## (asume que la media muestral es aproximadamente Normal, valido para n grande)
error_estandar = np.std(muestra_exp, ddof=1) / np.sqrt(n)
z_critico = stats.norm.ppf(0.975)
ic_normal_inf = np.mean(muestra_exp) - z_critico * error_estandar
ic_normal_sup = np.mean(muestra_exp) + z_critico * error_estandar

display(Math(fr"\text{{Media Muestral Original: }} \bar{{X}} = {np.mean(muestra_exp):.3f}\text{{ h}}"))
display(Math(fr"\text{{IC Bootstrap 95\% (percentil): }} [{ic_boot_inf:.3f},\ {ic_boot_sup:.3f}]\text{{ h}}"))
display(Math(fr"\text{{IC Normal aproximado 95\% (TLC): }} [{ic_normal_inf:.3f},\ {ic_normal_sup:.3f}]\text{{ h}}"))

print(f"\nDesviacion estandar de las {B} medias bootstrap (error estandar bootstrap): {np.std(medias_boot):.4f}")
print(f"Error estandar analitico (TLC): {error_estandar:.4f}")
```

**Interpretación**: los dos métodos producen intervalos muy similares ($[7.62, 14.86]$ Bootstrap vs. $[7.47, 14.75]$ Normal-TLC) porque $n=40$ ya es razonablemente grande para que el Teorema del Límite Central se cumpla bien sobre la media — pero el Bootstrap llegó a ese resultado **sin asumir** normalidad de $\bar X$ en ningún punto del cálculo, solo remuestreando los datos observados. Esta es la ventaja práctica del método: funciona igual de bien (y a veces mejor) cuando $n$ es pequeño, cuando el estimador de interés no es la media (p. ej. una mediana o un percentil, para los que no existe una fórmula analítica simple de error estándar), o cuando la forma de la distribución subyacente es incierta.

**Verificación simbólica del IC analítico (TLC)**: a diferencia del Bootstrap (remuestreo, correctamente numérico y sin fórmula cerrada), el intervalo de confianza analítico $\bar{x} \pm z_{\alpha/2}\cdot s/\sqrt{n}$ sí tiene forma cerrada y puede verificarse simbólicamente con SymPy, sustituyendo los mismos valores muestrales ($\bar x$, $s$, $n$, $z_{0.025}$) obtenidos arriba:

```python
import sympy as sp
from IPython.display import display, Math

## 1. Definicion simbolica del IC analitico por TLC
x_bar, s, n_sim, z = sp.symbols('bar_x s n z', positive=True)
error_estandar_expr = s / sp.sqrt(n_sim)
ic_inf_expr = x_bar - z * error_estandar_expr
ic_sup_expr = x_bar + z * error_estandar_expr

display(Math(fr"\text{{IC}} = \bar{{x}} \pm z_{{\alpha/2}}\cdot\frac{{s}}{{\sqrt{{n}}}} = {sp.latex(x_bar)} \pm {sp.latex(z * error_estandar_expr)}"))

## 2. Sustitucion de los valores muestrales del ejemplo (tiempo hasta falla de nanosensores)
valores = {x_bar: sp.Float(float(np.mean(muestra_exp))), s: sp.Float(float(np.std(muestra_exp, ddof=1))), n_sim: n, z: sp.Float(float(z_critico))}
ic_inf_val = float(ic_inf_expr.subs(valores))
ic_sup_val = float(ic_sup_expr.subs(valores))

display(Math(fr"\text{{IC Normal (SymPy)}} = [{ic_inf_val:.4f},\ {ic_sup_val:.4f}]"))
```

```
IC Normal (SymPy) = [7.4715, 14.7529]
```

El resultado simbólico coincide con el IC Normal-TLC $[7.47, 14.75]$ ya calculado numéricamente arriba, confirmando la fórmula cerrada de comparación frente al Bootstrap.

---

### 6.2 Verificación Simbólica del Estimador MLE de la Media Normal

$$\boxed{\hat{\mu}_{MLE} = \bar{X} = \frac{1}{n}\sum_{i=1}^n X_i}$$

```python
import sympy as sp
from IPython.display import display, Math

mu, sigma, n = sp.symbols('mu sigma n', positive=True)
sum_x = sp.Symbol(r'(\sum X_i)', real=True)
sum_x2 = sp.Symbol(r'(\sum X_i^2)', real=True)

## Log-Verosimilitud de n observaciones normales
log_L = -(n / 2) * sp.log(2 * sp.pi * sigma**2) - (1 / (2 * sigma**2)) * (sum_x2 - 2 * mu * sum_x + n * mu**2)

## Derivada respecto a mu (ecuación de score) y solución del estimador MLE
d_logL_dmu = sp.diff(log_L, mu)
mu_mle = sp.solve(d_logL_dmu, mu)[0]

display(Math(r'\text{Ecuación de Score } \frac{d \ln L}{d\mu}: ' + sp.latex(d_logL_dmu)))
display(Math(r'\text{Estimador MLE Resuelto } \hat{\mu}: ' + sp.latex(mu_mle)))
```

