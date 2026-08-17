# UNIDAD 7: Inferencia Estadística y Prueba de Hipótesis

**Duración:** 2.5 semanas (15 horas)

**Curso:** Probabilidad y Estadística Inferencial

**Institución:** Universidad de la Ciénega del Estado de Michoacán de Ocampo (UCEMICH)

**Profesor:** Luis José Yudico Anaya

**Carrera:** Ingeniería en Nanotecnología

**Nivel:** Tercer Semestre

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Multiagent-AI-Lab/Probability-Statistics-Agentic-AI-Core/blob/master/notebooks/UNIDAD_7_INFERENCIA_ESTIMACION.ipynb)

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

## 1. Fundamentación Teórica de la Inferencia Estadística

La **Prueba de Hipótesis Estadística** es el proceso formal de utilizar información muestral para confirmar o refutar una aseveración (hipótesis) sobre un parámetro desconocido $\theta$ asociado a una distribución de probabilidad $f(x; \theta)$ de una población. Es una de las dos ramas centrales de la inferencia estadística (junto con la estimación de parámetros) y es la herramienta cuantitativa estándar para validar afirmaciones sobre procesos experimentales en ingeniería.

### 1.1 Hipótesis Nula y Alternativa
Una hipótesis estadística paramétrica es la verificación de una aseveración sobre el parámetro desconocido $\theta$:

* **Hipótesis Nula ($H_0$)**: la aseveración por defecto sobre el parámetro, denotada $H_0: \theta \in \Theta_0$. Por convención, el signo de igualdad ($=$, $\ge$ o $\le$) siempre se incluye en $H_0$.
* **Hipótesis Alternativa ($H_1$)**: la afirmación complementaria, $H_1: \theta \in \Theta_1 = \Theta \setminus \Theta_0$, que se sostiene solo si la evidencia muestral es suficientemente fuerte en su contra.

### 1.2 Estadístico de Prueba y Región Crítica
* **Estadístico de Prueba**: una estadística cuyo valor se calcula a partir de la muestra observada y cuya distribución bajo $H_0$ se conoce.
* **Región Crítica (o de Rechazo)**: el conjunto de valores del estadístico de prueba para los cuales $H_0$ se rechaza en favor de $H_1$.

### 1.3 Errores Tipo I y Tipo II
Al decidir entre $H_0$ y $H_1$ con información parcial (una muestra), se pueden cometer dos tipos de errores:

| | $H_0$ es verdadera | $H_0$ es falsa |
|:---:|:---:|:---:|
| **No rechazar $H_0$** | Decisión correcta | Error Tipo II ($\beta$) |
| **Rechazar $H_0$** | Error Tipo I ($\alpha$) | Decisión correcta |

* **Error Tipo I**: rechazar $H_0$ cuando en realidad es verdadera. Su probabilidad es el **nivel de significancia** $\alpha = P(\text{rechazar } H_0 \mid H_0 \text{ verdadera})$.
* **Error Tipo II**: no rechazar $H_0$ cuando en realidad es falsa, con probabilidad $\beta = P(\text{no rechazar } H_0 \mid H_0 \text{ falsa})$.
* **Poder de la Prueba**: $1-\beta$, la probabilidad de rechazar correctamente $H_0$ cuando es falsa.

**Ejemplo (cálculo de $\alpha$ y $\beta$)**: sea $X \sim \text{Exp}(\lambda)$, con $H_0: \mu = 20$ contra $H_1: \mu = 30$ ($\mu = 1/\lambda$), y regla de decisión "rechazar $H_0$ si $x > 28$" con una única observación:
$$\alpha = P(X > 28 \mid \mu=20) = e^{-28/20} \approx \boxed{0.2466}$$
$$\beta = P(X \le 28 \mid \mu=30) = 1 - e^{-28/30} \approx \boxed{0.6068}$$

### 1.4 El Valor p (p-value)
El **p-valor** es la probabilidad de obtener un resultado igual o más extremo que el observado, asumiendo que $H_0$ es verdadera. Es la métrica más usada en la práctica porque resume toda la evidencia contra $H_0$ en un solo número, sin necesidad de tabular valores críticos: se rechaza $H_0$ si $\text{p-valor} < \alpha$.

### 1.5 Lema de Neyman–Pearson y Pruebas Más Potentes (UMP)
Para un nivel $\alpha$ fijo, la teoría de Neyman–Pearson busca minimizar $\beta$ (maximizar el poder). Un test que logra esto para toda alternativa se llama **uniformemente más potente (UMP)**.

**Teorema (Lema de Neyman–Pearson)**: para $H_0: \theta=\theta_0$ contra $H_1: \theta=\theta_1$, el test más potente de tamaño $\alpha$ rechaza $H_0$ cuando el cociente de verosimilitud (likelihood ratio) excede una constante $k$:
$$\varphi(x) = \begin{cases} 1 & \text{si } f_1(x)/f_0(x) > k \\ 0 & \text{si } f_1(x)/f_0(x) < k \end{cases}$$

**Ejemplo**: con $f_0(x) = 2x$ y $f_1(x) = 2(1-x)$ en $(0,1)$, el cociente $f_1/f_0 = (1-x)/x$ lleva a rechazar $H_0$ si $X < 1/(1+k)$. Resolviendo $\alpha = \int_0^{1/(1+k)} 2t\,dt$ se obtiene $k = (1-\sqrt{\alpha})/\sqrt{\alpha}$, de modo que la región de rechazo óptima es $X < \sqrt{\alpha}$, con función de potencia $1-(1-\sqrt{\alpha})^2$.

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

### 1.8 Pruebas Chi-cuadrado de Bondad de Ajuste, Contingencia y Proporciones
Además de la media y la varianza, la familia $\chi^2$ cubre tres pruebas no paramétricas de uso constante en control de calidad:

* **Bondad de Ajuste**: evalúa si una muestra proviene de una distribución específica, comparando frecuencias observadas $O_i$ contra esperadas $E_i = nP_i$ en $k$ categorías: $D^2 = \sum_{i=1}^k (O_i-E_i)^2/E_i \sim \chi^2_{k-1}$ (o $\chi^2_{k-1-r}$ si se estimaron $r$ parámetros de la muestra).
* **Tablas de Contingencia (Independencia)**: evalúa si dos variables categóricas son independientes, con frecuencia esperada $e_{ij} = (r_i \cdot c_j)/N$ por celda y estadístico $D^2 = \sum_{i,j} (n_{ij}-e_{ij})^2/e_{ij} \sim \chi^2_{(r-1)(c-1)}$.
* **Igualdad de Proporciones (Homogeneidad)**: evalúa $H_0: p_1=p_2=\dots=p_k$ contra $H_1$: al menos una proporción difiere, estimando una proporción común $\hat{p}$ y aplicando el mismo esquema $\chi^2$ sobre las celdas de éxito/fracaso.

En los tres casos se rechaza $H_0$ cuando el estadístico supera el valor crítico $\chi^2$ correspondiente, o equivalentemente cuando el p-valor es menor que $\alpha$.

**Ejemplo — Bondad de Ajuste**: se registran los tiempos entre fallas de $n=150$ nano-sensores piezoresistivos, agrupados en $k=4$ intervalos, y se desea verificar si siguen una distribución Exponencial con $\lambda=0.005$ ($\alpha=0.01$). Con frecuencias observadas/esperadas por intervalo, el estadístico de prueba resulta $D_0^2 \approx 12.79$, con $k-1=3$ grados de libertad. El valor crítico es $\chi^2_{3,\,0.01} \approx 11.34$. Como $D_0^2 = 12.79 > 11.34$, **se rechaza $H_0$**: los tiempos entre fallas no son consistentes con una distribución Exponencial($\lambda=0.005$).

**Ejemplo — Tabla de Contingencia**: se desea evaluar si el **método de síntesis** de nanopartículas de oro (Turkevich vs. método alternativo) es independiente de la **presencia de agregación** observada por TEM. Con una tabla $2\times 2$ de frecuencias observadas y $\alpha=0.05$, el estadístico $D_0^2$ se compara contra $\chi^2_{1,\,0.05}$; el procedimiento sigue el mismo esquema de bondad de ajuste, sustituyendo las frecuencias esperadas por celda $e_{ij}=(r_i \cdot c_j)/N$.

**Ejemplo — Igualdad de Proporciones**: se comparan las proporciones de nanopartículas defectuosas en $k=4$ lotes de síntesis de AgNPs ($H_0: p_1=p_2=p_3=p_4$ contra $H_1$: al menos una proporción difiere). Se estima la proporción común $\hat p$ a partir de los datos agregados, se calculan las frecuencias esperadas de "defectuoso"/"no defectuoso" por lote, y se aplica el estadístico $\chi^2$ con $k-1=3$ grados de libertad para decidir si el proceso de síntesis es consistente entre lotes.

---

## 2. Ejemplo Analítico Paso a Paso: Control de Calidad del Diámetro de Nanopartículas de Plata

### 2.1 Contexto Aplicado en Nanotecnología
Un fabricante de nanopartículas de plata (AgNPs) para recubrimientos antimicrobianos afirma que su proceso de síntesis produce partículas con un diámetro medio de $\mu_0 = 50\ \text{nm}$ y desviación estándar histórica conocida $\sigma = 4\ \text{nm}$ (parámetro bien caracterizado tras años de producción). Un laboratorio de control de calidad toma una muestra de $n=36$ nanopartículas de un nuevo lote y mide, vía dispersión dinámica de luz (DLS), un diámetro promedio muestral de $\bar{x} = 48.3\ \text{nm}$. Con $\alpha = 0.05$, se desea determinar si el nuevo lote es consistente con el proceso caracterizado o si el diámetro medio se ha desviado significativamente.

### 2.2 Paso 1: Planteamiento de Hipótesis
$$H_0: \mu = 50\ \text{nm} \qquad H_1: \mu \neq 50\ \text{nm}$$
Como $\sigma$ es conocida a partir del historial extenso del proceso, corresponde un **Z-test** bilateral para la media.

### 2.3 Paso 2: Cálculo del Estadístico de Prueba
$$z_0 = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}} = \frac{48.3 - 50}{4/\sqrt{36}} = \frac{-1.7}{0.6\overline{6}} \approx \boxed{-2.55}$$

### 2.4 Paso 3: Región Crítica y Decisión
Para $\alpha=0.05$ bilateral, $z_{\alpha/2} = z_{0.025} = 1.96$. La regla de rechazo es $z_0 \notin (-1.96,\ 1.96)$.

Como $z_0 = -2.55 < -1.96$, **se rechaza $H_0$**: existe evidencia estadística significativa de que el diámetro medio de las nanopartículas de plata del nuevo lote difiere de los $50\ \text{nm}$ especificados.

### 2.5 Paso 4: Cálculo del p-valor
$$\text{p-valor} = 2 \cdot P(Z < -2.55) = 2 \cdot 0.00539 \approx \boxed{0.0108}$$

Como $0.0108 < 0.05$, el p-valor confirma la decisión de rechazo tomada con el valor crítico, reforzando que el lote debe someterse a revisión del proceso de síntesis antes de su liberación para recubrimientos antimicrobianos.

---

## 3. Código de Verificación Simbólica (SymPy)

```python
import sympy as sp
from IPython.display import display, Math

## 1. Definición de símbolos del Z-test para la media
x_bar, mu_0, sigma, n = sp.symbols('bar_x mu_0 sigma n', positive=True)

## 2. Expresión simbólica del estadístico Z
z_expr = (x_bar - mu_0) / (sigma / sp.sqrt(n))
display(Math(fr"Z = \frac{{\bar{{X}} - \mu_0}}{{\sigma/\sqrt{{n}}}} = {sp.latex(z_expr)}"))

## 3. Sustitución de los valores del control de calidad de AgNPs (n=36, sigma=4, mu_0=50, x_bar=48.3)
valores = {x_bar: sp.Rational('48.3'), mu_0: 50, sigma: 4, n: 36}
z0_exacto = z_expr.subs(valores)
z0_decimal = float(z0_exacto)

display(Math(fr"z_0 = {sp.latex(z0_exacto)} = \boxed{{{z0_decimal:.4f}}}"))
```

---

## 4. Solución Computacional en Python (SciPy & Statsmodels)

```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

## Configuración visual profesional
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 5)

## --- PARTE A: Z-test para la media (diámetro de AgNPs) ---
x_bar, mu_0, sigma, n_val = 48.3, 50.0, 4.0, 36
z0 = (x_bar - mu_0) / (sigma / np.sqrt(n_val))
p_valor_z = 2 * stats.norm.cdf(-abs(z0))
z_critico = stats.norm.ppf(1 - 0.05 / 2)

print("--- Z-TEST: DIÁMETRO DE NANOPARTÍCULAS DE PLATA (AgNPs) ---")
print(f"Estadístico z0:      {z0:.4f}")
print(f"Valor crítico z_a/2: {z_critico:.4f}")
print(f"P-valor (bilateral): {p_valor_z:.4f}")
print(f"Decisión:            {'Rechazar H0' if abs(z0) > z_critico else 'No rechazar H0'}")

## --- PARTE B: t-test cuando sigma es desconocida (muestra simulada de un segundo lote) ---
np.random.seed(7)
lote_2 = stats.norm.rvs(loc=48.8, scale=3.7, size=15)  # DLS en nm
t_stat, p_valor_t = stats.ttest_1samp(lote_2, popmean=50.0)

print("\n--- T-TEST: SEGUNDO LOTE (sigma desconocida, n=15) ---")
print(f"Media muestral:       {lote_2.mean():.4f} nm")
print(f"Estadístico t0:       {t_stat:.4f}")
print(f"P-valor (bilateral):  {p_valor_t:.4f}")
print(f"Decisión (alpha=.05): {'Rechazar H0' if p_valor_t < 0.05 else 'No rechazar H0'}")

## --- PARTE C: Visualización de la Región de Rechazo (Z-test) ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

z_range = np.linspace(-4, 4, 500)
pdf_z = stats.norm.pdf(z_range)
axes[0].plot(z_range, pdf_z, color="navy", lw=2, label="N(0,1) bajo H0")
axes[0].fill_between(z_range, pdf_z, where=(z_range <= -z_critico), color="red", alpha=0.4, label="Región de rechazo")
axes[0].fill_between(z_range, pdf_z, where=(z_range >= z_critico), color="red", alpha=0.4)
axes[0].axvline(z0, color="black", linestyle="--", lw=2, label=f"z0 = {z0:.2f}")
axes[0].set_title("Z-test: Región de Rechazo (Diámetro AgNPs)", fontsize=12, fontweight="bold")
axes[0].set_xlabel("z")
axes[0].legend()

## Gráfico D: prueba de bondad de ajuste chi-cuadrado (ejemplo de control de calidad)
frecuencias_obs = np.array([58, 39, 19, 34])   # bandas de tamaño observadas
frecuencias_esp = np.array([58.5, 36.0, 21.0, 33.0])  # esperadas bajo H0
chi2_stat = np.sum((frecuencias_obs - frecuencias_esp) ** 2 / frecuencias_esp)
p_valor_chi2 = 1 - stats.chi2.cdf(chi2_stat, df=len(frecuencias_obs) - 1)

categorias = ["0-25nm", "25-50nm", "50-75nm", ">75nm"]
x_pos = np.arange(len(categorias))
axes[1].bar(x_pos - 0.2, frecuencias_obs, width=0.4, label="Observada", color="steelblue")
axes[1].bar(x_pos + 0.2, frecuencias_esp, width=0.4, label="Esperada (H0)", color="salmon")
axes[1].set_xticks(x_pos)
axes[1].set_xticklabels(categorias)
axes[1].set_title(f"Bondad de Ajuste $\\chi^2$ (p-valor={p_valor_chi2:.3f})", fontsize=12, fontweight="bold")
axes[1].set_ylabel("Frecuencia")
axes[1].legend()

plt.tight_layout()
plt.show()
```

---

## 5. Interpretación Post-Gráfico & Diccionario de Variables

### 5.1 Interpretación de Resultados Computacionales
1. **Rechazo Consistente Z-test vs. p-valor**: tanto el criterio del valor crítico ($|z_0|=2.55 > 1.96$) como el p-valor ($0.0108 < 0.05$) coinciden en rechazar $H_0$, confirmando que el desplazamiento del diámetro medio observado en el lote de AgNPs no es atribuible al azar muestral bajo el proceso caracterizado.
2. **t-test como Generalización Práctica**: cuando $\sigma$ no se conoce de antemano (caso más común en un laboratorio que evalúa un lote nuevo sin historial), el t-test de una muestra (`scipy.stats.ttest_1samp`) sustituye naturalmente al Z-test, ampliando la incertidumbre de la región crítica para compensar el desconocimiento de la varianza poblacional.
3. **Bondad de Ajuste como Extensión Multi-categoría**: la prueba $\chi^2$ de bondad de ajuste generaliza la lógica de "comparar lo observado contra lo esperado bajo $H_0$" a distribuciones completas de tamaño de partícula agrupadas en bandas, útil cuando el control de calidad no se limita a un único estadístico resumen sino a la forma completa de la distribución de tamaños del lote.

### 5.2 Diccionario de Variables Nanotecnológicas
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

```python
import numpy as np
import scipy.stats as stats
from IPython.display import display, Math

np.random.seed(42)
muestra_exp = stats.expon.rvs(scale=12.5, size=40)  # muestra original

## Bootstrap (B = 10,000 réplicas)
B = 10_000
medias_boot = [np.mean(np.random.choice(muestra_exp, size=len(muestra_exp), replace=True)) for _ in range(B)]

ic_inf = np.percentile(medias_boot, 2.5)
ic_sup = np.percentile(medias_boot, 97.5)

display(Math(fr"\text{{Media Muestral Original: }} \bar{{X}} = {np.mean(muestra_exp):.3f}"))
display(Math(fr"\text{{Intervalo de Confianza Bootstrap 95\%: }} [{ic_inf:.3f}, {ic_sup:.3f}]"))
```

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

## Errores Comunes / Misconceptions

* **Error**: Interpretar el p-valor como "la probabilidad de que $H_0$ sea verdadera".
  **Correcto**: el p-valor es $P(\text{observar un estadístico igual o más extremo que el obtenido} \mid H_0 \text{ es verdadera})$ — una probabilidad condicional sobre los datos, no sobre la hipótesis. No dice nada directo sobre $P(H_0 \mid \text{datos})$.

* **Error**: Interpretar "no rechazar $H_0$" como "aceptar $H_0$ como verdadera" o como evidencia de que $H_0$ es correcta.
  **Correcto**: no rechazar $H_0$ solo significa que la evidencia muestral no fue suficiente para descartarla al nivel de significancia elegido — puede deberse a que $H_0$ es cierta, o a que la prueba tuvo poca potencia (muestra pequeña, efecto real pequeño). La ausencia de evidencia no es evidencia de ausencia.

* **Error**: Igualar significancia estadística ($p < \alpha$) con relevancia práctica o magnitud del efecto.
  **Correcto**: con un tamaño de muestra $n$ suficientemente grande, incluso diferencias triviales (sin importancia práctica) resultan estadísticamente significativas. El p-valor no mide el tamaño del efecto — para eso se reporta el tamaño de efecto (p. ej. $d$ de Cohen) y el intervalo de confianza correspondiente.

## Ejercicio Propuesto

Un nuevo protocolo de síntesis de AgNPs afirma producir un diámetro medio de $\mu_0 = 25.0\text{ nm}$, con desviación estándar poblacional conocida $\sigma = 3.0\text{ nm}$ (a partir de control histórico del proceso). Se toma una muestra de $n=36$ nanopartículas y se mide un diámetro medio muestral $\bar{x} = 26.2\text{ nm}$. Se plantea $H_0: \mu = 25.0$ contra $H_1: \mu \ne 25.0$, con $\alpha = 0.05$.

1. Calcula el estadístico $Z$ de la prueba.
2. Calcula el p-valor (prueba de dos colas) y compáralo contra $\alpha$ para decidir si se rechaza $H_0$.
3. Enuncia la conclusión en términos correctos: ¿qué significa exactamente el p-valor obtenido en este contexto (no lo confundas con $P(H_0 \text{ verdadera})$)? Si la decisión hubiera sido "no rechazar $H_0$", ¿sería válido concluir que el nuevo protocolo produce exactamente $\mu=25.0\text{ nm}$?

Escribe tu solución en una celda de código nueva en tu notebook. La celda de autoevaluación de la siguiente sección verificará tu resultado.

## Referencias

* Agresti, A. & Kateri, M. (2022). *Foundations of Statistics for Data Scientists: With R and Python*. Chapman & Hall/CRC (Texts in Statistical Science). Capítulos sobre estimación puntual, máxima verosimilitud, intervalos de confianza y pruebas de hipótesis.
* Virtanen, P. et al. (2020). SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. *Nature Methods*, 17, 261-272. Documentación: [docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html)
