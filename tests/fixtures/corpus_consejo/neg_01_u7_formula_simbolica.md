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

### 6.3 Ajuste Computacional de MLE con `scipy.stats.fit`
Cuando no se busca solo la fórmula del estimador sino ajustar una distribución concreta a datos observados, `scipy.stats` provee ajuste numérico por máxima verosimilitud directamente:

```python
import numpy as np
from scipy import stats

np.random.seed(42)

## Datos simulados de diámetro de un lote de AgNPs (verdadero mu=50, sigma=4)
datos_diametro = stats.norm.rvs(loc=50, scale=4, size=200)

## Ajuste MLE de una distribución Normal a los datos
mu_mle, sigma_mle = stats.norm.fit(datos_diametro)
print(f"mu estimado (MLE): {mu_mle:.4f} nm")
print(f"sigma estimado (MLE): {sigma_mle:.4f} nm")

## Prueba de bondad de ajuste Kolmogorov-Smirnov
ks_stat, ks_pvalue = stats.kstest(datos_diametro, 'norm', args=(mu_mle, sigma_mle))
print(f"Kolmogorov-Smirnov: estadístico={ks_stat:.4f}, p-valor={ks_pvalue:.4f}")
print("Buen ajuste (p > 0.05)" if ks_pvalue > 0.05 else "Ajuste cuestionable (p <= 0.05)")
```

### 6.4 Estimación MAP (Máximo a Posteriori): Incorporando Conocimiento Previo

El **Método de Momentos** (§1.9) y el **MLE** (§6.2-6.3) comparten un supuesto: toda la información sobre el parámetro $\theta$ proviene únicamente de la muestra observada. La estimación **Bayesiana** relaja ese supuesto incorporando explícitamente conocimiento previo sobre $\theta$ —de literatura, procesos similares ya caracterizados, o restricciones físicas conocidas— mediante una **distribución a priori** $p(\theta)$. El Teorema de Bayes (Unidad 2, §4.2) combina ese prior con la verosimilitud de los datos $p(x|\theta)$ para obtener la **distribución a posteriori**:
$$p(\theta \mid x) \propto p(x \mid \theta)\cdot p(\theta)$$

El estimador **Máximo a Posteriori (MAP)** es el valor de $\theta$ que maximiza esa posterior — el análogo bayesiano del MLE, pero "penalizado" por el prior:
$$\hat\theta_{MAP} = \arg\max_\theta\ p(x\mid\theta)\,p(\theta)$$

**Caso: proporción de éxito con prior Beta (conjugado de la Bernoulli/Binomial)**. Un prior $\theta\sim\text{Beta}(\alpha,\beta)$ es **conjugado** de la verosimilitud Binomial: la posterior resultante es también una Beta, con actualización trivial de sus parámetros. Si se observan $x$ éxitos en $n$ ensayos:
$$p(\theta\mid x) = \text{Beta}(\alpha+x,\ \beta+n-x) \qquad\Longrightarrow\qquad \hat\theta_{MAP} = \frac{\alpha+x-1}{\alpha+\beta+n-2}\quad(\alpha,\beta>1)$$

**Contexto de nanotecnología**: un nuevo proceso de funcionalización de nanotubos de carbono se somete a $n=20$ ensayos, de los cuales $x=14$ resultan en funcionalización exitosa. Antes de este experimento, procesos similares documentados en la literatura sugieren una tasa de éxito moderada, sin fuerte evidencia hacia ningún extremo — se modela ese conocimiento previo con un prior débil $\text{Beta}(\alpha=2,\beta=2)$ (equivalente a "2 pseudo-éxitos y 2 pseudo-fracasos" de información previa, centrado en $0.5$).

```python
import numpy as np
from scipy.stats import beta

## Prior debil: Beta(2,2), centrado en 0.5, poca informacion previa
alpha_prior, beta_prior = 2, 2
n, x = 20, 14  # 14 exitos en 20 ensayos de funcionalizacion

## Posterior: Beta(alpha+x, beta+n-x) -- conjugacion Beta-Binomial
alpha_post = alpha_prior + x
beta_post = beta_prior + (n - x)

## Estimadores puntuales a comparar
theta_mle = x / n                                                    # MLE: solo los datos
theta_map = (alpha_post - 1) / (alpha_post + beta_post - 2)           # MAP: datos + prior
theta_media_posterior = alpha_post / (alpha_post + beta_post)         # media de la posterior (otro resumen bayesiano)

print(f"MLE (solo datos):              theta_hat = {theta_mle:.4f}")
print(f"MAP (datos + prior Beta(2,2)): theta_hat = {theta_map:.4f}")
print(f"Media de la posterior:         theta_hat = {theta_media_posterior:.4f}")
print(f"\nPosterior resultante: Beta(alpha={alpha_post}, beta={beta_post})")
```

**Interpretación**: el MLE ($\hat\theta=0.700$) usa únicamente los 20 ensayos observados; el MAP ($\hat\theta=0.6818$) lo "encoge" ligeramente hacia el $0.5$ del prior, precisamente porque el prior aporta la equivalente de información previa moderada. A medida que $n\to\infty$, el término de los datos ($x$, $n-x$) domina sobre el prior fijo ($\alpha$, $\beta$) y $\hat\theta_{MAP}\to\hat\theta_{MLE}$ — el prior deja de importar cuando hay suficiente evidencia muestral, un comportamiento deseable de cualquier estimador bayesiano razonable.

