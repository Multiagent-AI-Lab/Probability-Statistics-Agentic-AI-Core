## 4. Código de Verificación Simbólica (SymPy)

Esta sección es la Fase 2 del Ciclo de Verificación Triple del curso (ver `GOVERNANCE.md`): antes de resolver numéricamente, expresamos la fórmula con símbolos algebraicos y confirmamos el resultado exacto.

```python
import sympy as sp
from IPython.display import display, Math

## 1. Definición de símbolos
n = sp.Symbol('n', positive=True, integer=True)
k = sp.Symbol('k', integer=True)
p = sp.Symbol('p', positive=True)

## 2. Expresión simbólica de la PMF Binomial y Esperanza
pmf_binomial = sp.binomial(n, k) * (p**k) * ((1 - p)**(n - k))
esperanza_expr = sp.Sum(k * pmf_binomial, (k, 0, n))

display(Math(fr"\text{{PMF Binomial Simbólica: }} P(X = k) = {sp.latex(pmf_binomial)}"))

## 3. Sustitución de los parámetros de la inspección nanotecnológica (n=20, p=0.05, k=2)
valores = {n: 20, p: sp.Rational(5, 100), k: 2}
prob_exacta = pmf_binomial.subs(valores)
prob_decimal = float(prob_exacta)

display(Math(fr"\text{{Resultado Exacto }} P(X=2): {sp.latex(prob_exacta)} = \boxed{{{prob_decimal:.5f}}}"))
```

---

## 5. Solución Computacional en Python (SciPy & Statsmodels)

```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

## Configuración visual profesional
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 5)

## --- PARTE A: Cálculo Exacto con scipy.stats.binom ---
n_val = 20
p_val = 0.05

pmf_k2 = stats.binom.pmf(k=2, n=n_val, p=p_val)
cdf_k0 = stats.binom.cdf(k=0, n=n_val, p=p_val)
prob_al_menos_1 = 1 - cdf_k0

print("--- RESULTADOS SCI PY STATS (BINOMIAL) ---")
print(f"P(X = 2) exacta:          {pmf_k2:.5f}")
print(f"P(X >= 1) acumulada:      {prob_al_menos_1:.5f}")
print(f"Esperanza teórica E[X]:   {stats.binom.mean(n=n_val, p=p_val):.2f}")
print(f"Desviación Estándar SD:   {stats.binom.std(n=n_val, p=p_val):.4f}")

## --- PARTE B: Comparación de Familias Discretas (Binomial vs Poisson vs Geométrica) ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

## Gráfico 1: PMF de Binomial n=20, p=0.05
k_range = np.arange(0, 8)
pmf_vals = stats.binom.pmf(k_range, n=n_val, p=p_val)

axes[0].bar(k_range, pmf_vals, color='royalblue', alpha=0.85, edgecolor='black', width=0.5)
axes[0].axvline(x=1.0, color='red', linestyle='--', label='Esperanza E[X] = 1.0')
axes[0].set_title("PMF Binomial (n=20, p=0.05): Defectos en Nano-sensores", fontsize=12, fontweight="bold")
axes[0].set_xlabel("Número de Nano-sensores Defectuosos (k)")
axes[0].set_ylabel("Probabilidad P(X = k)")
axes[0].legend()

## Gráfico 2: Simulación de Distribución Geométrica (Ensayos hasta primer defecto)
p_geom = 0.05
muestras_geom = stats.geom.rvs(p=p_geom, size=50_000, random_state=42)

sns.histplot(muestras_geom, discrete=True, stat="density", color="forestgreen", alpha=0.7, ax=axes[1])
x_geom = np.arange(1, 40)
pmf_geom_teorica = stats.geom.pmf(x_geom, p=p_geom)
axes[1].plot(x_geom, pmf_geom_teorica, 'ro-', lw=1.5, label='PMF Teórica Geométrica(p=0.05)')
axes[1].set_title("Distribución Geométrica: Inspecciones hasta el Primer Defecto", fontsize=12, fontweight="bold")
axes[1].set_xlabel("Número de Ensayo del Primer Defecto (k)")
axes[1].set_ylabel("Densidad de Frecuencia Muestral")
axes[1].legend()

plt.tight_layout()
plt.show()

## --- PARTE C: Distribución Multinomial — Clasificación de Nanopartículas por Tamaño ---
## En síntesis sol-gel de nanopartículas de óxido metálico, se clasifican en 3 categorías
## de diámetro: pequeña (<10nm), mediana (10-30nm), grande (>30nm), con probabilidades
## conocidas del proceso. Crítico para el control de calidad en nanotecnología.
from scipy.stats import multinomial

n_lote = 20
p_categorias = [0.2, 0.5, 0.3]  # P(pequeña), P(mediana), P(grande)

## Probabilidad de obtener exactamente 4 pequeñas, 10 medianas, 6 grandes
conteo_observado = [4, 10, 6]
prob_conteo = multinomial.pmf(conteo_observado, n=n_lote, p=p_categorias)
print(f"P(4 pequeñas, 10 medianas, 6 grandes) = {prob_conteo:.6f}")

## Esperanza por categoría
esperanza = [n_lote * p for p in p_categorias]
print(f"Número esperado por categoría: {esperanza}")
```

---

## 6. Interpretación Post-Gráfico & Diccionario de Variables

### 6.1 Interpretación de Resultados Computacionales
1. **Asimetría Positiva en Eventos Raros**: La PMF de la distribución binomial para $n=20, p=0.05$ exhibe una fuerte asimetría a la derecha concentrada en $k=0$ ($35.8\%$) y $k=1$ ($37.7\%$). La probabilidad de obtener más de 3 nano-sensores defectuosos es prácticamente nula ($< 1.6\%$).
2. **Comportamiento Memoria Geométrica**: La simulación de $50,000$ réplicas geométricas muestra que el número esperado de inspecciones necesarias para detectar el primer defecto es $\mathbb{E}[K] = 1/0.05 = 20$ ensayos.
3. **Clasificación Multinomial de Nanopartículas por Tamaño**: El resultado computacional de PARTE C confirma que, para un lote de $n=20$ nanopartículas sintetizadas por vía sol-gel con probabilidades de categoría $p = (0.2, 0.5, 0.3)$, el conteo esperado por categoría de diámetro es de $4$ nanopartículas pequeñas ($<10$ nm), $10$ medianas ($10$–$30$ nm) y $6$ grandes ($>30$ nm) — exactamente el escenario evaluado, lo que explica por qué su probabilidad puntual es la moda de la distribución multinomial. En control de calidad de nanomateriales, esta distribución conjunta permite estimar la probabilidad de que un lote de síntesis cumpla simultáneamente los tres rangos de tamaño objetivo, en lugar de evaluar cada categoría de forma aislada como haría una binomial marginal; esto es clave para ajustar los parámetros del proceso sol-gel (pH, temperatura, tiempo de reacción) cuando la distribución de tamaños observada se desvía de la especificación de diseño del nanomaterial.

### 6.2 Diccionario de Variables de la Unidad

Notación general introducida en las Secciones 1-2, independiente del ejemplo aplicado específico:

* $X$: variable aleatoria discreta genérica; $\Omega$: espacio muestral; $R_X$: rango (soporte) de $X$.
* $p_X(x)$: función de masa de probabilidad (PMF), $p_X(x) = P(X=x)$.
* $F_X(x)$: función de distribución acumulada (CDF), $F_X(x) = P(X \le x)$.
* $\mathbb{E}[X]$, $\mu$: valor esperado (media) de $X$.
* $\text{Var}(X)$, $\sigma^2$: varianza de $X$; $\sigma$: desviación estándar ($\sigma=\sqrt{\text{Var}(X)}$).
* $p$: probabilidad de éxito de un ensayo (Bernoulli, Binomial, Geométrica, Binomial Negativa); $q=1-p$: probabilidad de fracaso (Bernoulli).
* $n$: número de ensayos independientes (Binomial), o tamaño de la muestra extraída (Hipergeométrica), o número total de ensayos por experimento (Multinomial).
* $k$, $x$: valor puntual sobre el que se evalúa la PMF/CDF de una distribución discreta (número de éxitos, de fallos o de ensayos, según la familia).
* $\lambda$: tasa media de ocurrencia de eventos por intervalo (Poisson), $\lambda>0$.
* $r$: número objetivo de éxitos a acumular (Binomial Negativa).
* $N$: tamaño de la población finita; $K$: número de elementos con la característica de interés en la población (Hipergeométrica; distinta de la $K$ usada como variable aleatoria de conteo de fallos en la Sección 6.3).
* $a, b$: extremos del rango de valores igualmente probables; $k=b-a+1$: número de valores posibles (Uniforme Discreta).
* $X_1,\dots,X_k$: componentes del vector aleatorio conjunto; $p_1,\dots,p_k$ (con $\sum_i p_i=1$): probabilidades por categoría; $k_1,\dots,k_k$ (con $\sum_i k_i=n$): conteos observados por categoría (Multinomial).

### 6.3 Diccionario de Variables Nanotecnológicas del Ejemplo Aplicado
* $X$: Variable aleatoria discreta que representa el número de nano-sensores defectuosos.
* $n$: Tamaños del lote inspeccionado ($n=20$).
* $p$: Probabilidad individual de falla microscópica por grabado de silicio ($p=0.05$).
* $\lambda$: Tasa media de ocurrencia de defectos en procesos continuos de litografía (Poisson).
* $K$: Número de ensayos independientes hasta observar la primera falla (Geométrica).

---

## 7. Módulo de Simulación: Algoritmo de Generación Estocástica de Variables Discretas

### 7.1 Algoritmo General de Inversión por Suma Acumulada
Dada una variable aleatoria discreta $X$ con PMF $P(X = x_k) = p_k$:
1. Generar $U \sim \text{Uniforme}(0, 1)$.
2. Seleccionar el menor índice $k$ tal que $\sum_{j=1}^k p_j \ge U$.

### 7.2 Simulación Estocástica en Python de Fallas Poisson
```python
import numpy as np
import scipy.stats as stats

np.random.seed(123)
N_sim = 50_000
lam = 4.5  # Promedio de micro-defectos por oblea de silicio
muestras_poisson = stats.poisson.rvs(mu=lam, size=N_sim)

print(f"Promedio Muestral de Defectos Simulado: {np.mean(muestras_poisson):.4f} | Teórico: {lam}")
print(f"Varianza Muestral Simulada:             {np.var(muestras_poisson):.4f} | Teórica: {lam}")
```

---

## 8. Referencia Avanzada (Opcional)

Este curso (tercer semestre) trata a las variables aleatorias discretas con herramientas de cálculo elemental. Para quien desee profundizar hacia un tratamiento formal medida-teórico (variables aleatorias como funciones medibles, espacios de probabilidad abstractos), el curso de posgrado **MIT 6.436J — Fundamentals of Probability** (Prof. Yury Polyanskiy) cubre este mismo tema en sus *Lecture Notes* 4–6, con los prerrequisitos de análisis real y teoría de la medida que ese enfoque exige: [ocw.mit.edu/courses/6-436j-fundamentals-of-probability-fall-2018/pages/lecture-notes](https://ocw.mit.edu/courses/6-436j-fundamentals-of-probability-fall-2018/pages/lecture-notes/).

## Errores Comunes / Misconceptions

---

* Li, Y. & Jiang, Z. (2008). An Overview of Reliability and Failure Mode Analysis of Microelectromechanical Systems (MEMS). En *Handbook of Performability Engineering*. Springer, London. DOI: [10.1007/978-1-84800-131-2_58](https://doi.org/10.1007/978-1-84800-131-2_58) — modos de falla y análisis de confiabilidad de micro-sensores, el contexto aplicado del ejemplo analítico de esta unidad (conteo Binomial de defectos en un lote de nano-sensores).
