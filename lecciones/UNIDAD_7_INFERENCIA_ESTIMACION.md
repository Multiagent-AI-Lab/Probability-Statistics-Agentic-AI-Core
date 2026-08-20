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

## Prerequisitos de esta unidad

- **Distribuciones Muestrales: Chi-cuadrada, t-Student y F** (Unidad 5) — señaladas explícitamente en la Parte C de esa unidad como "prerequisito de Inferencia"; son la base de todas las pruebas paramétricas de esta unidad.
- **Estadística Descriptiva y Medidas de Tendencia Central** (Unidad 1) — insumo directo para los estimadores puntuales (Método de Momentos, MLE) desarrollados aquí.

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

---

### 1.10 Pruebas No Paramétricas: Kolmogorov-Smirnov, Mann-Whitney-Wilcoxon y Kruskal-Wallis

Las pruebas vistas hasta §1.8 (Z, t, $\chi^2$) son **paramétricas**: asumen una forma funcional conocida (típicamente Normal) para la distribución subyacente. Cuando esta suposición no se cumple —distribuciones asimétricas, muestras pequeñas, o presencia de outliers—, las pruebas **no paramétricas** (basadas en rangos u órdenes, no en los valores originales) ofrecen alternativas más robustas.

**Kolmogorov-Smirnov (KS) de dos muestras**: a diferencia del KS de una muestra ya usado en §6.3 (bondad de ajuste contra una distribución teórica), el KS de dos muestras evalúa si dos conjuntos de datos independientes provienen de la **misma distribución**, sin asumir ninguna forma específica. El estadístico compara las funciones de distribución empíricas (CDF) de ambas muestras:
$$D_{n,m} = \sup_x |F_n(x) - F_m(x)|$$
donde $F_n$ y $F_m$ son las CDF empíricas de cada muestra. Valores grandes de $D$ indican que las distribuciones difieren.

**Mann-Whitney-Wilcoxon U**: compara dos muestras independientes sin asumir normalidad, usando la suma de rangos combinados en vez de las medias — por eso es robusta ante outliers que distorsionarían un t-test:
$$U_1 = n_1 n_2 + \frac{n_1(n_1+1)}{2} - R_1$$
donde $R_1$ es la suma de rangos del grupo 1 tras combinar y ordenar ambas muestras.

**Kruskal-Wallis H**: generaliza Mann-Whitney a $k>2$ grupos independientes (es el análogo no paramétrico de ANOVA de una vía), usando también rangos combinados:
$$H = \frac{12}{N(N+1)}\sum_{i=1}^k \frac{R_i^2}{n_i} - 3(N+1)$$
Bajo $H_0$ (todas las poblaciones tienen la misma distribución), $H \sim \chi^2_{k-1}$ aproximadamente.

**Contexto de nanotecnología (KS)**: se comparan los diámetros de AgNPs sintetizadas por dos métodos distintos (reducción con citrato vs. con borohidruro de sodio) para verificar si producen la misma distribución de tamaños.

**Contexto de nanotecnología (Mann-Whitney)**: se mide la dureza Vickers (HV) de nanocompuestos cerámica-nanotubos de carbono con dos concentraciones de refuerzo; el grupo A tiene una lectura anómala (aglomerado local de CNT) que distorsiona su media.

**Contexto de nanotecnología (Kruskal-Wallis)**: se comparan ángulos de contacto de recubrimientos hidrofóbicos con tres tipos de nanopartículas (SiO$_2$, TiO$_2$, ZnO), donde ZnO presenta mayor varianza por inestabilidad del proceso de síntesis — la condición de homogeneidad de varianzas requerida por ANOVA (ver §1.12, Levene) se viola, justificando el uso de Kruskal-Wallis.

**Solución computacional**:
```python
import numpy as np
import scipy.stats as stats

## --- KS de dos muestras: diametro de AgNPs, dos metodos de sintesis ---
np.random.seed(201)
metodo_citrato = stats.norm.rvs(loc=50, scale=4, size=40)
metodo_borohidruro = stats.lognorm.rvs(s=0.25, scale=48, size=40)

ks_stat, ks_p = stats.ks_2samp(metodo_citrato, metodo_borohidruro)
print(f"KS 2-muestras (Citrato vs Borohidruro): D={ks_stat:.4f}, p-valor={ks_p:.4f}")
print("Conclusion:", "Distribuciones distintas (rechaza H0)" if ks_p < 0.05 else "No hay evidencia de diferencia")

## --- Mann-Whitney U: dureza Vickers, nanocompuestos con outlier ---
dureza_A = np.array([410, 430, 390, 400, 420, 980])   # 980 HV = aglomerado anomalo de CNT
dureza_B = np.array([550, 600, 580, 620, 590, 570])

t_stat, t_p = stats.ttest_ind(dureza_A, dureza_B, equal_var=False)
print(f"\nWelch t-test (enganado por outlier): t={t_stat:.4f}, p-valor={t_p:.4f}")

u_stat, u_p = stats.mannwhitneyu(dureza_A, dureza_B, alternative='less')
print(f"Mann-Whitney U (H1: A < B, una cola): U={u_stat:.4f}, p-valor={u_p:.4f}")

## --- Kruskal-Wallis: angulo de contacto, 3 recubrimientos con varianzas distintas ---
np.random.seed(202)
rec_SiO2 = np.random.normal(105, 5, 15)
rec_TiO2 = np.random.normal(118, 5, 15)
rec_ZnO = np.random.normal(112, 14, 15)   # mayor varianza (sintesis inestable)

h_stat, h_p = stats.kruskal(rec_SiO2, rec_TiO2, rec_ZnO)
print(f"\nKruskal-Wallis H: H={h_stat:.4f}, p-valor={h_p:.6f}")
print("Conclusion:", "Al menos un recubrimiento difiere (rechaza H0)" if h_p < 0.05 else "No se detecta diferencia")
```

**Interpretación**: el KS de dos muestras rechaza $H_0$ ($D=0.4250$, $p=0.0013$): los dos métodos de síntesis de AgNPs producen distribuciones de tamaño distinguibles, pese a tener medias similares (el KS es sensible a diferencias en la *forma* completa de la distribución, no solo en la media). En el caso de dureza, el t-test bilateral **no detecta diferencia** ($p=0.4405$) porque el outlier de 980 HV infla artificialmente la varianza y la media del grupo A; el Mann-Whitney dirigido ($H_1: A<B$), al basarse en rangos, sí detecta que B es consistentemente más duro ($p=0.0325 < 0.05$) — el mismo patrón de robustez que ilustra por qué estas pruebas son preferibles ante outliers. Finalmente, Kruskal-Wallis rechaza $H_0$ con fuerte evidencia ($p=0.000263$): al menos un recubrimiento produce un ángulo de contacto distinto — este resultado es el prerrequisito para el post-hoc de Dunn de §1.14.

$$\boxed{D_{KS}=0.4250\ (p=0.0013) \qquad U_{MW}=6.0\ (p=0.0325,\ \text{una cola}) \qquad H_{KW}=16.4854\ (p=0.000263)}$$

---

### 1.11 Prueba de Signos y Prueba de la Mediana

Cuando ni siquiera se puede asumir que los datos son simétricos o que la escala de medición es de intervalo (solo orden), las pruebas basadas en **signos** son las más robustas de toda la familia no paramétrica: ignoran la magnitud de las diferencias y usan solamente su dirección.

**Prueba de Signos**: contrasta si la mediana de una población es igual a un valor de referencia $\theta_0$: $H_0: \tilde\mu = \theta_0$ contra $H_1: \tilde\mu \neq \theta_0$. Se cuenta cuántas observaciones caen por encima ($n_+$) y por debajo ($n_-$) de $\theta_0$ (los empates exactos se descartan), y bajo $H_0$ cada observación tiene probabilidad $0.5$ de caer en cualquiera de los dos lados — por lo tanto $n_+ \sim \text{Binomial}(n_+ + n_-,\ 0.5)$ bajo $H_0$. Esto convierte la prueba de signos en un caso directo de prueba binomial exacta.

**Prueba de la Mediana**: generaliza la idea anterior a $k$ grupos independientes. Se calcula la mediana combinada de todas las observaciones (agrupando los $k$ grupos), se clasifica cada observación de cada grupo como "por encima" o "por debajo" de esa mediana combinada, y se construye una tabla de contingencia $2\times k$ que se evalúa con un test $\chi^2$ de independencia (ver §1.8) — la hipótesis nula es que los $k$ grupos comparten la misma mediana poblacional.

**Contexto de nanotecnología (Signos)**: se mide la rugosidad superficial (nm, vía AFM) de $n=20$ obleas recubiertas con un nuevo proceso de deposición, y se contrasta si la mediana del proceso iguala la especificación histórica de $\theta_0=2.5\ \text{nm}$.

**Contexto de nanotecnología (Mediana)**: se comparan tres lotes independientes de síntesis de AgNPs (diámetro en nm) para verificar si comparten la misma mediana de tamaño, sin asumir normalidad.

**Solución computacional**:
```python
import numpy as np
import scipy.stats as stats

## --- Prueba de Signos: rugosidad superficial vs especificacion (2.5 nm) ---
np.random.seed(301)
rugosidad = np.round(stats.norm.rvs(loc=2.8, scale=0.6, size=20), 2)
theta_0 = 2.5

n_mayor = np.sum(rugosidad > theta_0)
n_menor = np.sum(rugosidad < theta_0)
n_efectivo = n_mayor + n_menor  # excluye empates exactos con theta_0, si los hubiera

resultado_signos = stats.binomtest(n_mayor, n_efectivo, 0.5, alternative='two-sided')
print(f"Rugosidad: n_mayor={n_mayor}, n_menor={n_menor} (n_efectivo={n_efectivo})")
print(f"Prueba de Signos: p-valor = {resultado_signos.pvalue:.4f}")
print("Conclusion:", "Rechaza H0: mediana != 2.5 nm" if resultado_signos.pvalue < 0.05 else "No rechaza H0")

## --- Prueba de la Mediana: 3 lotes de sintesis de AgNPs ---
np.random.seed(302)
lote_1 = stats.norm.rvs(loc=50, scale=3, size=12)
lote_2 = stats.norm.rvs(loc=53, scale=3, size=12)
lote_3 = stats.norm.rvs(loc=49, scale=3, size=12)

stat_mediana, p_mediana, mediana_combinada, tabla = stats.median_test(lote_1, lote_2, lote_3)
print(f"\nMediana combinada: {mediana_combinada:.4f} nm")
print(f"Estadistico chi2: {stat_mediana:.4f}, p-valor: {p_mediana:.4f}")
print("Tabla de contingencia (fila 0 = por encima, fila 1 = por debajo):")
print(tabla)
```

**Interpretación**: la prueba de signos rechaza $H_0$ ($p=0.0414 < 0.05$): 15 de 20 obleas tienen rugosidad por encima de 2.5 nm, evidencia de que la mediana real del nuevo proceso se desvió de la especificación histórica — sin necesitar ningún supuesto sobre la forma de la distribución de rugosidades. La prueba de la mediana, en cambio, **no rechaza** $H_0$ ($p=0.2636$): con estas muestras no hay evidencia suficiente de que los tres lotes difieran en su mediana de diámetro, aunque sus medias muestrales numéricas difieran ligeramente (50, 53, 49 nm) — la prueba de la mediana es intencionalmente conservadora porque descarta toda la información salvo la posición relativa a la mediana global.

$$\boxed{\text{Signos: } p=0.0414\ (\text{rechaza}) \qquad \text{Mediana: } \chi^2=2.6667,\ p=0.2636\ (\text{no rechaza})}$$

---

### 1.12 Prueba de Levene (Homogeneidad de Varianzas)

La prueba de Levene contrasta $H_0: \sigma_1^2 = \sigma_2^2 = \dots = \sigma_k^2$ contra $H_1$: al menos una varianza difiere. Es el **prerrequisito estándar** antes de aplicar ANOVA clásico (que asume varianzas homogéneas entre grupos) — si Levene rechaza $H_0$, se debe usar una alternativa robusta (Welch's ANOVA o el Kruskal-Wallis de §1.10).

A diferencia de la prueba $\chi^2$ para una sola varianza (§1.7), que exige normalidad estricta, Levene es robusta ante desviaciones de la normalidad porque no trabaja directamente con los datos $x_{ij}$, sino con sus **desviaciones absolutas respecto a la mediana de cada grupo** $z_{ij} = |x_{ij} - \tilde{x}_i|$, y luego aplica un ANOVA de una vía sobre esos $z_{ij}$:
$$W = \frac{(N-k)}{(k-1)} \cdot \frac{\sum_{i=1}^k n_i (\bar{z}_i - \bar{z})^2}{\sum_{i=1}^k \sum_{j=1}^{n_i} (z_{ij}-\bar{z}_i)^2} \sim F_{k-1,\ N-k} \ \text{(aprox., bajo } H_0\text{)}$$

**Contexto de nanotecnología**: se reutilizan los mismos tres grupos de ángulo de contacto de §1.10 (SiO$_2$, TiO$_2$, ZnO) — el gap de Levene es precisamente el que justifica formalmente por qué esos datos requirieron Kruskal-Wallis en vez de ANOVA.

**Solución computacional**:
```python
import numpy as np
import scipy.stats as stats

np.random.seed(202)
rec_SiO2 = np.random.normal(105, 5, 15)
rec_TiO2 = np.random.normal(118, 5, 15)
rec_ZnO = np.random.normal(112, 14, 15)

lev_stat, lev_p = stats.levene(rec_SiO2, rec_TiO2, rec_ZnO)
print(f"Levene: W = {lev_stat:.4f}, p-valor = {lev_p:.6f}")

if lev_p < 0.05:
    print("Conclusion: Rechaza H0. Varianzas NO homogeneas -> usar Kruskal-Wallis, no ANOVA clasico.")
else:
    print("Conclusion: No rechaza H0. Varianzas homogeneas -> ANOVA clasico es valido.")
```

**Interpretación**: Levene rechaza $H_0$ ($W=9.0366$, $p=0.000544$), confirmando numéricamente que ZnO (con $\sigma=14$ frente a $\sigma=5$ de los otros dos recubrimientos) rompe el supuesto de homocedasticidad — exactamente la razón por la que en §1.10 se usó Kruskal-Wallis en lugar de ANOVA para comparar los tres recubrimientos.

$$\boxed{W_{\text{Levene}} = 9.0366,\quad p = 0.000544\ (\text{varianzas heterogéneas})}$$

---

### 1.13 Tamaño del Efecto: $d$ de Cohen

El p-valor indica *si* existe evidencia de una diferencia, pero no dice nada sobre *cuán grande* es esa diferencia en términos prácticos — con una muestra suficientemente grande, hasta una diferencia trivial resulta estadísticamente significativa (ver el misconception ya documentado al final de esta unidad). El **tamaño del efecto** cuantifica la magnitud de la diferencia entre dos grupos en unidades de desviación estándar, independientemente del tamaño de muestra.

Para dos grupos independientes con medias $\bar{x}_1,\bar{x}_2$ y desviaciones estándar muestrales $s_1,s_2$ (tamaños $n_1,n_2$), la $d$ de Cohen usa la **desviación estándar combinada (pooled)**:
$$s_{pooled} = \sqrt{\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}} \qquad d = \frac{\bar{x}_1-\bar{x}_2}{s_{pooled}}$$

**Regla práctica de interpretación** (Cohen, 1988): $|d|\approx 0.2$ efecto pequeño, $|d|\approx 0.5$ mediano, $|d|\approx 0.8$ grande.

**Contexto de nanotecnología**: se compara la conductividad eléctrica ($\text{S/m}$, escala arbitraria de medición) de nanocables de óxido de zinc antes y después de un proceso de dopaje con aluminio, para cuantificar no solo si el dopaje tiene efecto, sino qué tan grande es ese efecto.

**Solución computacional**:
```python
import numpy as np
import scipy.stats as stats

np.random.seed(501)
sin_dopaje = stats.norm.rvs(loc=120, scale=18, size=25)
con_dopaje = stats.norm.rvs(loc=145, scale=20, size=25)

n1, n2 = len(sin_dopaje), len(con_dopaje)
s1, s2 = np.std(sin_dopaje, ddof=1), np.std(con_dopaje, ddof=1)
s_pooled = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))
cohens_d = (np.mean(con_dopaje) - np.mean(sin_dopaje)) / s_pooled

t_stat, p_val = stats.ttest_ind(con_dopaje, sin_dopaje, equal_var=True)

print(f"Media sin dopaje: {np.mean(sin_dopaje):.4f} S/m")
print(f"Media con dopaje:  {np.mean(con_dopaje):.4f} S/m")
print(f"s_pooled: {s_pooled:.4f}")
print(f"\nt-test: t={t_stat:.4f}, p-valor={p_val:.6f}")
print(f"Cohen's d = {cohens_d:.4f}")
```

**Interpretación**: el t-test confirma significancia estadística ($p=0.0105<0.05$), pero es la $d$ de Cohen la que cuantifica la magnitud práctica: $d=0.75$ es un efecto **grande** según la regla de Cohen — el dopaje con aluminio no solo produce una diferencia detectable, sino una mejora sustancial de la conductividad respecto a la variabilidad natural del proceso, relevante para decisiones de ingeniería más allá de la mera significancia estadística.

$$\boxed{d_{\text{Cohen}} = \frac{145.19-125.37}{22.32} \approx 0.75\ (\text{efecto grande})}$$

---

### 1.14 Comparaciones Múltiples Post-Hoc: Dunn con Corrección de Bonferroni

Cuando Kruskal-Wallis (§1.10) rechaza $H_0$, sabemos que *al menos uno* de los $k$ grupos difiere, pero no *cuáles*. Responder esa pregunta exige comparar todos los pares posibles ($\binom{k}{2}$ comparaciones), pero hacerlo con Mann-Whitney repetido sin ajuste infla el Error Tipo I global: con $\alpha=0.05$ y varias comparaciones, la probabilidad de al menos un falso positivo crece muy por encima de $0.05$ — el mismo problema de pruebas múltiples que motiva la corrección de Bonferroni en otros contextos del curso.

**Prueba de Dunn**: es el post-hoc no paramétrico diseñado específicamente para seguir a Kruskal-Wallis. Reutiliza los mismos rangos combinados del test de Kruskal-Wallis y compara cada par de rangos promedio mediante un estadístico $z$:
$$z_{ij} = \frac{\bar{R}_i - \bar{R}_j}{\sqrt{\left(\frac{N(N+1)}{12} - \frac{C}{12(N-1)}\right)\left(\frac{1}{n_i}+\frac{1}{n_j}\right)}}$$
donde $\bar{R}_i$ es el rango promedio del grupo $i$, $N$ el tamaño total, y $C=\sum(t^3-t)$ una corrección por empates (rangos repetidos). El p-valor de cada comparación se obtiene de la Normal estándar, y luego se ajusta con la **corrección de Bonferroni** (ya introducida en §1.8 con la familia $\chi^2$, y aplicable aquí de forma idéntica):
$$p_{\text{ajustado}} = \min\left(1,\ p_{\text{raw}} \times \binom{k}{2}\right)$$

**Contexto de nanotecnología**: se retoman los tres recubrimientos hidrofóbicos de §1.10-1.12 (SiO$_2$, TiO$_2$, ZnO), donde Kruskal-Wallis ya rechazó $H_0$ — el post-hoc de Dunn identifica cuál(es) par(es) específico(s) de recubrimientos difieren realmente.

**Solución computacional** (implementación directa de la fórmula de Dunn, ya que no todo entorno tiene instalado el paquete opcional `scikit-posthocs`):
```python
import numpy as np
import scipy.stats as stats

def dunn_bonferroni(*grupos, etiquetas=None):
    """Prueba de Dunn post-hoc (Dunn, 1964) con correccion de Bonferroni,
    a partir de los rangos combinados usados por Kruskal-Wallis."""
    k = len(grupos)
    datos_combinados = np.concatenate(grupos)
    N = len(datos_combinados)
    rangos = stats.rankdata(datos_combinados)

    tamanos = [len(g) for g in grupos]
    limites = np.cumsum([0] + tamanos)
    rangos_por_grupo = [rangos[limites[i]:limites[i+1]] for i in range(k)]
    rango_promedio = [np.mean(r) for r in rangos_por_grupo]

    ## Correccion por empates (ties)
    _, conteos = np.unique(datos_combinados, return_counts=True)
    correccion_empates = np.sum(conteos**3 - conteos) / (12 * (N - 1))

    n_comparaciones = k * (k - 1) // 2
    resultados = []
    for i in range(k):
        for j in range(i + 1, k):
            se = np.sqrt((N*(N+1)/12 - correccion_empates) * (1/tamanos[i] + 1/tamanos[j]))
            z = (rango_promedio[i] - rango_promedio[j]) / se
            p_raw = 2 * (1 - stats.norm.cdf(abs(z)))
            p_bonferroni = min(1.0, p_raw * n_comparaciones)
            nombre_i = etiquetas[i] if etiquetas else f"G{i}"
            nombre_j = etiquetas[j] if etiquetas else f"G{j}"
            resultados.append((f"{nombre_i} vs {nombre_j}", z, p_raw, p_bonferroni))
    return resultados

np.random.seed(202)
rec_SiO2 = np.random.normal(105, 5, 15)
rec_TiO2 = np.random.normal(118, 5, 15)
rec_ZnO = np.random.normal(112, 14, 15)

print(f"{'Comparacion':<15}{'z':>10}{'p_raw':>12}{'p_bonferroni':>15}")
for comparacion, z, p_raw, p_bonf in dunn_bonferroni(rec_SiO2, rec_TiO2, rec_ZnO, etiquetas=["SiO2","TiO2","ZnO"]):
    marca = " *" if p_bonf < 0.05 else ""
    print(f"{comparacion:<15}{z:>10.4f}{p_raw:>12.6f}{p_bonf:>15.6f}{marca}")
```

**Interpretación**: tras la corrección de Bonferroni, solo la comparación **SiO$_2$ vs TiO$_2$** sigue siendo significativa ($p_{\text{bonf}}=0.000148$); las comparaciones que involucran ZnO (SiO$_2$ vs ZnO: $p_{\text{bonf}}=0.1038$; TiO$_2$ vs ZnO: $p_{\text{bonf}}=0.1549$) dejan de serlo tras el ajuste, pese a que sin corrección alguna hubiera parecido significativa la comparación SiO$_2$ vs ZnO ($p_{\text{raw}}=0.0346 < 0.05$). Esto ilustra directamente por qué la corrección es necesaria: la alta varianza de ZnO (ya detectada por Levene en §1.12) hace que sus rangos se solapen más con los de los otros grupos, reduciendo la potencia estadística para distinguirlo con confianza tras controlar el error acumulado.

$$\boxed{\text{Único par significativo tras Bonferroni: SiO}_2\text{ vs TiO}_2\ (p_{\text{bonf}}=0.000148)}$$

---

### 1.15 Regresión Logística: Wald, LRT, GLM Binomial y Odds Ratio

Cuando la variable respuesta es **binaria** (éxito/fracaso, colapso/supervivencia) en vez de continua, la regresión lineal (que asume $Y$ continua y normal) no es apropiada — sus predicciones no están acotadas en $[0,1]$. La **regresión logística** modela en su lugar la probabilidad de éxito $\pi(x)$ mediante la función logística (sigmoide), transformando el problema a un **Modelo Lineal Generalizado (GLM)** con función de enlace *logit* y componente aleatorio Binomial:
$$\ln\left(\frac{\pi(x)}{1-\pi(x)}\right) = \beta_0 + \beta_1 x \qquad\Longleftrightarrow\qquad \pi(x) = \frac{1}{1+e^{-(\beta_0+\beta_1 x)}}$$

**Interpretación de $\beta_1$ — Odds Ratio (razón de momios)**: si $x$ aumenta en una unidad, el *log-odds* de éxito aumenta en $\beta_1$; equivalentemente, la razón de momios $\text{ODDS}=\pi/(1-\pi)$ se multiplica por $e^{\beta_1}$ (el **odds ratio**).

**Los tres tests para $H_0:\beta_1=0$** (introducidos conceptualmente en el marco general de la unidad, aquí aplicados en la práctica):
* **Wald**: $z = \hat\beta_1 / SE(\hat\beta_1)$, comparado contra $N(0,1)$ — el más simple, reportado automáticamente por `statsmodels`.
* **Razón de Verosimilitud (LRT)**: compara la log-verosimilitud del modelo completo contra el modelo nulo (solo intercepto): $\Lambda = -2[\ell(H_0) - \ell(H_1)] \sim \chi^2_1$ bajo $H_0$ — más preciso que Wald en muestras pequeñas o cerca de separación completa.

**Contexto de nanotecnología**: se expone un cultivo celular a distintas dosis de nanopartículas de plata (AgNP, mg/L) y se registra si el cultivo colapsa (mortalidad $>50\%$) o sobrevive — un ejemplo clásico de curva dosis-respuesta en nanotoxicología, donde interesa además estimar la **LD$_{50}$** (dosis letal media, la dosis a la cual $\pi(x)=0.5$).

**Solución computacional**:
```python
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

## Dosis de AgNP (mg/L) replicada 4 veces por nivel, y resultado binario de colapso celular
dosis = np.array([5,5,5,5, 10,10,10,10, 15,15,15,15, 20,20,20,20, 25,25,25,25, 30,30,30,30], dtype=float)

np.random.seed(701)
logits_verdaderos = -6 + 0.35 * dosis
probs_verdaderas = 1 / (1 + np.exp(-logits_verdaderos))
np.random.seed(702)
colapso = np.random.binomial(1, probs_verdaderas)

X = sm.add_constant(dosis)
modelo_completo = sm.Logit(colapso, X).fit(disp=0)
modelo_nulo = sm.Logit(colapso, np.ones(len(colapso))).fit(disp=0)
print(modelo_completo.summary())

## Wald test (directo del summary)
wald_z, wald_p = modelo_completo.tvalues[1], modelo_completo.pvalues[1]

## Likelihood-Ratio Test (LRT)
lrt_stat = -2 * (modelo_nulo.llf - modelo_completo.llf)
lrt_p = stats.chi2.sf(lrt_stat, df=1)

## Odds ratio y LD50
odds_ratio = np.exp(modelo_completo.params[1])
beta0, beta1 = modelo_completo.params
ld50 = -beta0 / beta1

print(f"\nWald: z={wald_z:.4f}, p-valor={wald_p:.6f}")
print(f"LRT:  stat={lrt_stat:.4f}, p-valor={lrt_p:.6f}")
print(f"Odds ratio por mg/L adicional: {odds_ratio:.4f}")
print(f"LD50 (dosis letal 50%): {ld50:.4f} mg/L")

## GLM Binomial equivalente (misma estimacion, distinta interfaz)
modelo_glm = sm.GLM(colapso, X, family=sm.families.Binomial()).fit()
print(f"\nGLM Binomial: beta1={modelo_glm.params[1]:.6f} (coincide con Logit: {modelo_completo.params[1]:.6f})")

## Curva sigmoide de dosis-respuesta
x_plot = np.linspace(0, 35, 200)
y_pred = modelo_completo.predict(sm.add_constant(x_plot))
plt.figure(figsize=(8, 5))
plt.scatter(dosis, colapso, color="crimson", alpha=0.6, label="Datos observados")
plt.plot(x_plot, y_pred, color="navy", lw=2, label="Curva logística ajustada")
plt.axhline(0.5, color="gray", linestyle="--", label="LD50")
plt.axvline(ld50, color="gray", linestyle="--")
plt.xlabel("Dosis de AgNP (mg/L)")
plt.ylabel("Probabilidad de colapso celular")
plt.title("Curva Dosis-Respuesta: Nanotoxicidad de AgNP")
plt.legend()
plt.show()
```

**Interpretación**: tanto Wald ($z=2.3565$, $p=0.0184$) como LRT ($\Lambda=20.7687$, $p<0.0001$) rechazan $H_0:\beta_1=0$ — la dosis tiene un efecto significativo sobre la probabilidad de colapso celular. El GLM Binomial produce coeficientes idénticos al `Logit` directo (ambos son la misma estimación de máxima verosimilitud, solo con interfaces distintas de `statsmodels`). El odds ratio de $1.5550$ significa que cada mg/L adicional de AgNP multiplica los momios de colapso por $\approx 1.56$. La LD$_{50}$ estimada es $14.99\ \text{mg/L}$: la dosis a la cual el modelo predice exactamente $50\%$ de probabilidad de colapso celular, un valor de referencia estándar en estudios de toxicidad.

$$\boxed{\hat\beta_1 = 0.4415\ (\text{OR}=1.5550,\ p_{\text{Wald}}=0.0184,\ p_{\text{LRT}}<0.0001) \qquad \text{LD}_{50} = 14.99\ \text{mg/L}}$$

---

### 1.16 Distancia de Cook: Diagnóstico de Puntos Influyentes en Regresión

En un modelo de regresión lineal, no todas las observaciones pesan igual sobre los coeficientes estimados $\hat\beta$: un punto extremo o mal medido puede "arrastrar" la recta de ajuste hacia sí, distorsionando las conclusiones del modelo entero. La **Distancia de Cook** ($D_i$) cuantifica cuánto cambiarían los coeficientes ajustados si se eliminara la observación $i$-ésima del conjunto de datos:
$$D_i = \frac{(\hat{\boldsymbol\beta} - \hat{\boldsymbol\beta}_{(i)})^\top (X^\top X)(\hat{\boldsymbol\beta} - \hat{\boldsymbol\beta}_{(i)})}{p\cdot MSE}$$
donde $\hat{\boldsymbol\beta}_{(i)}$ son los coeficientes recalculados sin la observación $i$, $p$ el número de parámetros, y $MSE$ el error cuadrático medio del modelo completo. En la práctica no se recalcula el modelo $n$ veces: `statsmodels` obtiene $D_i$ de forma cerrada a partir del *leverage* ($h_{ii}$, elemento diagonal de la Hat Matrix) y el residuo estandarizado. Un **umbral empírico común** es $D_i > 4/n$: observaciones por encima de ese umbral merecen inspección.

**Contexto de nanotecnología**: se modela la conductividad eléctrica de una película delgada de óxido de estaño (SnO$_2$) en función de la temperatura de recocido, sobre $n=30$ muestras — una de ellas corresponde a una medición defectuosa (falla del equipo de 4 puntas) que produce una lectura anómala.

**Solución computacional**:
```python
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

np.random.seed(801)
n = 30
temperatura = np.linspace(300, 700, n)          # K
conductividad = 2.0 + 0.05 * temperatura + np.random.normal(0, 3, n)  # S/cm
conductividad[5] = 150  # medicion defectuosa (falla del equipo de 4 puntas)

X = sm.add_constant(temperatura)
modelo = sm.OLS(conductividad, X).fit()

influencia = modelo.get_influence()
cooks_d, _ = influencia.cooks_distance
umbral = 4 / n

indices_influyentes = np.where(cooks_d > umbral)[0]
print(f"Umbral de influencia (4/n): {umbral:.4f}")
print(f"Indices con Distancia de Cook por encima del umbral: {indices_influyentes}")
print(f"Distancia de Cook en el punto 5 (medicion defectuosa): {cooks_d[5]:.4f}")

plt.figure(figsize=(9, 5))
plt.stem(np.arange(n), cooks_d, markerfmt=",")
plt.axhline(umbral, color="red", linestyle="--", label="Umbral 4/n")
plt.title("Distancia de Cook: Conductividad de SnO$_2$ vs Temperatura de Recocido")
plt.xlabel("Índice de muestra")
plt.ylabel("Distancia de Cook $D_i$")
plt.legend()
plt.show()
```

**Interpretación**: la observación en el índice 5 (la medición defectuosa insertada deliberadamente) tiene $D_5=1.0880$, muy por encima del umbral $4/30=0.1333$, y es la **única** observación influyente detectada. Esto confirma numéricamente que ese punto tiene un peso desproporcionado sobre los coeficientes del modelo — en la práctica, el siguiente paso sería investigar la causa de esa medición (recalibrar el equipo, repetir el experimento) antes de confiar en las conclusiones del ajuste, o reportar el modelo con y sin ese punto para mostrar su sensibilidad.

$$\boxed{D_5 = 1.0880 \gg \text{umbral } 4/n = 0.1333 \quad(\text{único punto influyente})}$$

---

### 1.17 Test de Permutación

El test de permutación es una alternativa completamente no paramétrica para comparar dos grupos, que no asume ninguna distribución teórica ni siquiera para el estadístico de prueba — construye la distribución nula directamente a partir de los datos observados, de la misma familia de ideas de remuestreo que el Bootstrap ya visto en §6.1, pero orientado a pruebas de hipótesis en vez de intervalos de confianza.

**Procedimiento**:
1. Calcular la diferencia observada $\Delta_{\text{obs}} = \bar{x}_A - \bar{x}_B$.
2. Combinar ambas muestras en un solo conjunto.
3. Reasignar aleatoriamente las etiquetas de grupo (permutación), preservando los tamaños $n_A,n_B$ originales.
4. Calcular la diferencia $\Delta^*$ bajo esa reasignación aleatoria.
5. Repetir $R$ veces (típicamente $R\ge1000$) para construir la distribución nula empírica $\{\Delta_1^*,\dots,\Delta_R^*\}$.
6. El p-valor empírico es la proporción de permutaciones con $|\Delta^*|\ge|\Delta_{\text{obs}}|$.

Bajo $H_0:\mu_A=\mu_B$, intercambiar las etiquetas de grupo no debería cambiar sistemáticamente la diferencia observada — por eso la distribución de las $\Delta^*$ aproxima la distribución muestral de la diferencia bajo la hipótesis nula, sin ningún supuesto paramétrico.

**Contexto de nanotecnología**: se mide la fuerza de adhesión (N, ensayo de rayado/*scratch test*) de un recubrimiento nanoestructurado sobre sustrato de silicio, comparando el proceso estándar contra un nuevo tratamiento superficial con plasma, con muestras pequeñas ($n=8$ por grupo) típicas de un experimento costoso de caracterización.

**Solución computacional**:
```python
import numpy as np
import scipy.stats as stats

np.random.seed(901)
adhesion_control = stats.norm.rvs(loc=10.0, scale=0.6, size=8)   # proceso estandar
adhesion_tratado = stats.norm.rvs(loc=11.2, scale=0.6, size=8)   # tratamiento con plasma

def test_permutacion(x, y, n_perm=10000, seed=42):
    """Test de permutacion para la diferencia de medias, dos colas."""
    rng = np.random.default_rng(seed)
    obs = np.mean(x) - np.mean(y)
    combinado = np.concatenate([x, y])
    nx = len(x)
    diffs = np.empty(n_perm)
    for i in range(n_perm):
        perm = rng.permutation(combinado)
        diffs[i] = np.mean(perm[:nx]) - np.mean(perm[nx:])
    p_valor = np.mean(np.abs(diffs) >= np.abs(obs))
    return obs, p_valor, diffs

obs_diff, p_perm, distribucion_nula = test_permutacion(adhesion_tratado, adhesion_control)
print(f"Diferencia observada (tratado - control): {obs_diff:.4f} N")
print(f"P-valor (test de permutacion, R=10000): {p_perm:.4f}")

## Verificacion cruzada con la implementacion nativa de SciPy
def estadistico(x, y):
    return np.mean(x) - np.mean(y)

resultado_scipy = stats.permutation_test(
    (adhesion_tratado, adhesion_control), estadistico,
    n_resamples=10000, alternative='two-sided', random_state=42
)
print(f"scipy.stats.permutation_test: statistic={resultado_scipy.statistic:.4f}, p-valor={resultado_scipy.pvalue:.4f}")
```

**Interpretación**: el tratamiento con plasma produce una adhesión promedio $1.0119\ \text{N}$ mayor que el proceso estándar, y el test de permutación confirma que esta diferencia es significativa ($p=0.0341<0.05$ con la implementación manual, $p=0.0342$ con `scipy.stats.permutation_test` — la coincidencia entre ambas confirma la correcta implementación manual). Con $n=8$ por grupo, un t-test asumiría normalidad sin poder verificarla de forma confiable; el test de permutación evita ese supuesto por completo, siendo especialmente apropiado para experimentos de caracterización de materiales, donde las réplicas son costosas y las muestras pequeñas son la norma.

$$\boxed{\Delta_{\text{obs}} = 1.0119\ \text{N}, \quad p_{\text{permutación}} = 0.0341}$$

---

### 1.18 VIF (Factor de Inflación de Varianza): Diagnóstico de Multicolinealidad

En un modelo de regresión múltiple, la **multicolinealidad** ocurre cuando dos o más variables predictoras están altamente correlacionadas entre sí. Esto no sesga las predicciones del modelo, pero infla drásticamente la varianza (y por tanto el error estándar) de los coeficientes individuales — el modelo ya no puede distinguir con confianza cuál de las variables correlacionadas es la responsable del efecto sobre $Y$.

El **Factor de Inflación de Varianza (VIF)** de la variable $X_j$ se calcula ajustando una regresión auxiliar de $X_j$ contra todas las demás variables predictoras, y usando su $R_j^2$:
$$\text{VIF}_j = \frac{1}{1-R_j^2}$$
Si $X_j$ es completamente independiente del resto de predictores, $R_j^2=0$ y $\text{VIF}_j=1$ (sin inflación). Conforme $R_j^2\to 1$ (colinealidad casi perfecta), $\text{VIF}_j\to\infty$. Una **regla práctica común**: $\text{VIF}>5$–$10$ indica multicolinealidad severa que amerita revisar el modelo (eliminar una de las variables redundantes, o combinarlas).

**Contexto de nanotecnología**: se modela la conductividad de una película de óxido de estaño en función de tres predictores — temperatura de proceso, presión de la cámara (que en este reactor específico está mecánicamente acoplada a la temperatura, y por tanto correlacionada con ella) y concentración de dopante (controlada de forma independiente).

**Solución computacional**:
```python
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

np.random.seed(1001)
n = 50
temperatura = np.linspace(300, 800, n)
presion = 0.02 * temperatura + np.random.normal(0, 1, n)   # acoplada mecanicamente a la temperatura
dopante = np.random.uniform(0, 5, n)                       # controlado de forma independiente

X = sm.add_constant(np.column_stack([temperatura, presion, dopante]))
nombres = ["const", "Temperatura", "Presion", "Dopante"]

vif_valores = [variance_inflation_factor(X, i) for i in range(X.shape[1])]
for nombre, vif in zip(nombres, vif_valores):
    print(f"VIF({nombre}): {vif:.4f}")

print(f"\nCorrelacion Temperatura-Presion: {np.corrcoef(temperatura, presion)[0,1]:.4f}")
```

**Interpretación**: Temperatura y Presión muestran $\text{VIF}\approx10.2$ (ambas), muy por encima del umbral de $5$–$10$, consistente con su alta correlación ($r=0.9495$) impuesta por el diseño del reactor — el modelo no puede separar de forma confiable el efecto individual de cada una sobre la conductividad. En contraste, Dopante tiene $\text{VIF}=1.0161\approx1$, prácticamente sin inflación, porque fue controlada de forma independiente. La recomendación práctica en este caso sería eliminar Presión del modelo (dado que Temperatura ya la explica casi por completo) o combinarlas en un único índice de "condiciones del reactor".

$$\boxed{\text{VIF}_{\text{Temp}}=10.23,\ \ \text{VIF}_{\text{Presión}}=10.28\ \ (\text{multicolinealidad severa}),\quad \text{VIF}_{\text{Dopante}}=1.02\ (\text{sin inflación})}$$

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

### 2.6 Prueba Unitaria con pytest

Se verifica que el estadístico $z_0$, el valor crítico $z_{0.025}$ y el p-valor coincidan con los calculados a mano, y que la regla de decisión (rechazar $H_0$ porque $z_0$ cae fuera de la región de no rechazo) sea la correcta:

```python
import ipytest
import pytest
from scipy.stats import norm

ipytest.autoconfig()

x_bar, mu_0, sigma, n = 48.3, 50, 4, 36
alpha = 0.05


def test_estadistico_z_de_prueba():
    z0 = (x_bar - mu_0) / (sigma / n ** 0.5)
    assert z0 == pytest.approx(-2.55, rel=1e-3)


def test_valor_critico_bilateral_para_alpha_005():
    z_critico = norm.ppf(1 - alpha / 2)
    assert z_critico == pytest.approx(1.96, rel=1e-3)


def test_se_rechaza_h0_porque_z0_cae_fuera_de_la_region_de_no_rechazo():
    z0 = (x_bar - mu_0) / (sigma / n ** 0.5)
    z_critico = norm.ppf(1 - alpha / 2)
    assert abs(z0) > z_critico


def test_p_valor_coincide_con_la_decision_de_rechazo():
    z0 = (x_bar - mu_0) / (sigma / n ** 0.5)
    p_valor = 2 * norm.cdf(z0)
    assert p_valor == pytest.approx(0.0108, rel=1e-2)
    assert p_valor < alpha


ipytest.run("-vv")
```

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
* *Optimization of Silver Nanoparticle-Coating Methods on Acrylic, Silicone, and Zirconia Facial Prosthetic Materials: Surface Characterization and Antimicrobial Activity Against Pseudomonas aeruginosa* (2026). *Prosthesis*, 8(7), 66. https://doi.org/10.3390/prosthesis8070066 — usa pruebas $t$ pareadas para evaluar reproducibilidad y confiabilidad del recubrimiento de nanopartículas de plata (AgNPs), la misma prueba de hipótesis sobre diámetro de AgNPs desarrollada en el ejemplo aplicado de esta unidad.
* Virtanen, P. et al. (2020). SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. *Nature Methods*, 17, 261-272. Documentación: [docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html)

## Herramientas de esta Unidad

**StatsTutorAgent** — resuelve tus dudas conceptuales sobre inferencia estadística citando el contenido exacto de esta unidad, y te hace una pregunta socrática si detecta un error conceptual común (p. ej. malinterpretar un p-valor o confundir varianza muestral con poblacional) en vez de darte la respuesta directa:

```python
import os
import sys
from pathlib import Path

if 'google.colab' in sys.modules:
    from google.colab import userdata
    for nombre_secreto in ("GEMINI_API_KEY", "GOOGLE_API_KEY"):
        try:
            os.environ["GEMINI_API_KEY"] = userdata.get(nombre_secreto)
            break
        except Exception:
            continue
    else:
        print(
            "⚠️ [Unidad 7] No se encontró el secreto GEMINI_API_KEY ni GOOGLE_API_KEY en Colab. "
            "Créalo en el ícono de llave 🔑 de la barra lateral izquierda para usar StatsTutorAgent."
        )

from src.multiagent_core.stats_tutor_agent import StatsTutorAgent

tutor = StatsTutorAgent(course_dir=Path("lecciones"))
print(tutor.ask("¿qué significa el nivel de confianza de un intervalo de estimación?"))
```

No requiere configuración adicional más allá de tu `GEMINI_API_KEY` (créala en [aistudio.google.com/apikey](https://aistudio.google.com/apikey) y agrégala como secreto de Colab o variable de entorno local).

## Autoevaluación

Guarda tu solución al Ejercicio Propuesto en un archivo separado y evalúala contra el pipeline de auditoría del curso:

```python
%%writefile solucion_ejercicio_u7.py
# Completa aquí tu solución al Ejercicio Propuesto de esta unidad.
import numpy as np
import scipy.stats as stats

n = 36
sigma = 3.0
mu_0 = 25.0
x_bar = 26.2
alpha = 0.05

# TODO: calcula el estadístico Z de la prueba: Z = (x_bar - mu_0) / (sigma / sqrt(n))
# TODO: calcula el p-valor de dos colas y compáralo contra alpha para decidir si se rechaza H0
# TODO: en un comentario, enuncia la conclusión correcta: qué significa el p-valor obtenido
#       (no lo confundas con P(H0 verdadera)), y si "no rechazar H0" implicaría que mu=25.0 exactamente
```

```python
from src.multiagent_core.code_auditor_agent import CodeAuditorAgent
from external_skills.pedagogy.socratic_debugger import SocraticDebugger

with open("solucion_ejercicio_u7.py", encoding="utf-8") as f:
    codigo_alumno = f.read()

auditor = CodeAuditorAgent()
resultado = auditor.audit_code(codigo_alumno)

if resultado["issues"] or resultado["metrics"]["has_security_risk"]:
    debugger = SocraticDebugger()
    for issue in resultado["issues"]:
        tipo_error = "syntax_error" if "SyntaxError" in issue else "generic"
        print("💡", debugger.generate_socratic_question(tipo_error, "Unidad 7"))
    for issue in resultado["security_issues"]:
        print("🔒", debugger.generate_socratic_question("security_risk", "Unidad 7"))
        print("   ", issue)
    print("\n--- Detalle técnico ---")
    print(resultado)
else:
    print("✅ Tu código pasa las verificaciones automáticas de estilo y seguridad.")
    print(resultado)
```
