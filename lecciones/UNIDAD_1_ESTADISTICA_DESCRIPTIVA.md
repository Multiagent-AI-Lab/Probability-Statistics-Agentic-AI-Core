# UNIDAD 1: Estadística Descriptiva y Análisis Exploratorio de Datos

**Duración:** 1.5 semanas (9 horas)

**Curso:** Probabilidad y Estadística Inferencial

**Institución:** Universidad de la Ciénega del Estado de Michoacán de Ocampo (UCEMICH)

**Profesor:** Luis José Yudico Anaya

**Carrera:** Ingeniería en Nanotecnología

**Nivel:** Tercer Semestre

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Multiagent-AI-Lab/Probability-Statistics-Agentic-AI-Core/blob/master/notebooks/UNIDAD_1_ESTADISTICA_DESCRIPTIVA.ipynb)

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

## 1. Fundamentación Teórica y Conceptos Clave

La **Estadística Descriptiva** y el **Análisis Exploratorio de Datos (EDA)** constituyen los cimientos fundamentales para caracterizar e interpretar conjuntos de datos experimentales en ciencias e ingeniería, particularmente en el estudio de sistemas nanotecnológicos y modelos de Inteligencia Artificial. El análisis descriptivo permite resumir la tendencia central, dispersión, simetría y forma de una distribución muestral mediante medidas numéricas y representaciones gráficas cuantitativas, antes de intentar cualquier modelo probabilístico o inferencia sobre la población de origen.

En esta unidad abordamos:
* Cálculo de estadísticas descriptivas cuantitativas (media, mediana, moda, varianza, desviación estándar, rango, cuantiles).
* Medidas de forma de una distribución (asimetría y curtosis).
* Análisis exploratorio visual mediante diagramas de caja (boxplots), histogramas de frecuencias y estimación de densidad de kernel (KDE).
* Aplicaciones computacionales en Python utilizando las bibliotecas `scipy.stats`, `numpy`, `pandas`, `matplotlib` y `seaborn`.

### 1.1 Medidas de Tendencia Central
Dada una muestra $x_1, x_2, \dots, x_n$, las medidas de tendencia central ubican el "centro" de los datos:

* **Media Aritmética Muestral**:
  $$\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i$$
  Es sensible a valores atípicos (outliers), ya que cada observación contribuye proporcionalmente a la suma total.
* **Mediana**: el valor que divide a los datos ordenados en dos mitades iguales. Si $n$ es impar, es el valor central; si $n$ es par, es el promedio de los dos valores centrales. Es robusta ante outliers.
* **Moda**: el valor (o valores) que ocurre con mayor frecuencia. Es la única medida de tendencia central aplicable a datos categóricos.

### 1.2 Medidas de Dispersión
Las medidas de dispersión cuantifican qué tan esparcidos están los datos respecto al centro:

* **Rango**: $R = x_{\max} - x_{\min}$. Es fácil de calcular pero extremadamente sensible a valores extremos.
* **Varianza Muestral** (con corrección de Bessel, $n-1$ grados de libertad, para estimador insesgado de la varianza poblacional):
  $$s^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2$$
  La resta de un grado de libertad se debe a que $\bar{x}$ ya fue estimada de la misma muestra, dejando solo $n-1$ desviaciones independientes.
* **Desviación Estándar Muestral**: $s = \sqrt{s^2}$, en las mismas unidades que los datos originales (a diferencia de la varianza, que está en unidades al cuadrado).
* **Cuantiles y Percentiles**: el cuantil $q$ (o percentil $100q$) es el valor $x_q$ tal que una proporción $q$ de los datos es menor o igual a él. Los **cuartiles** $Q_1$ (percentil 25), $Q_2$ (percentil 50, la mediana) y $Q_3$ (percentil 75) dividen los datos en cuatro partes iguales.
* **Rango Intercuartílico (IQR)**:
  $$IQR = Q_3 - Q_1$$
  Mide la dispersión del 50% central de los datos y es robusto ante outliers; se usa además como criterio estándar de detección de valores atípicos: un dato se considera atípico si cae fuera de $[Q_1 - 1.5 \cdot IQR,\ Q_3 + 1.5 \cdot IQR]$.

### 1.3 Medidas de Forma
* **Asimetría (Skewness)**: mide la falta de simetría de la distribución respecto a su media.
  $$g_1 = \frac{\frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^3}{s^3}$$
  $g_1 > 0$ indica cola derecha más larga (asimetría positiva); $g_1 < 0$ indica cola izquierda más larga (asimetría negativa); $g_1 \approx 0$ sugiere simetría aproximada.
* **Curtosis (Kurtosis)**: mide qué tan "apuntada" o "achatada" es la distribución respecto a una normal, es decir, el peso relativo de sus colas.
  $$g_2 = \frac{\frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^4}{s^4} - 3$$
  La resta de 3 define el **exceso de curtosis**, de modo que una distribución normal tiene $g_2 = 0$. $g_2 > 0$ (leptocúrtica) indica colas más pesadas que la normal; $g_2 < 0$ (platicúrtica) indica colas más ligeras.

### 1.4 Visualización Exploratoria
* **Histograma**: agrupa los datos en intervalos (bins) y grafica la frecuencia (o densidad) de cada uno; es la herramienta más directa para intuir la forma de la distribución subyacente.
* **Diagrama de Caja (Boxplot)**: representa gráficamente $Q_1$, la mediana, $Q_3$, los bigotes (hasta $1.5 \cdot IQR$) y los outliers como puntos individuales; es ideal para comparar la dispersión entre varios grupos.
* **Estimación de Densidad de Kernel (KDE)**: una versión suavizada del histograma que estima la función de densidad de probabilidad subyacente sin asumir una forma paramétrica, sumando "kernels" (típicamente gaussianos) centrados en cada observación.

### 1.5 Los Cinco Grandes Problemas de la Estadística

La Estadística, como disciplina, no se agota en resumir un conjunto de datos: el análisis descriptivo de esta Unidad 1 es solo la primera de cinco direcciones que estructuran todo el curso. Antes de continuar, conviene ubicar dónde encaja cada herramienta futura dentro de un mapa conceptual completo — sin resolver todavía ninguno de los problemas 2 a 5, para los cuales aún no se cuenta con las herramientas necesarias:

1. **Problema de Representación de Datos**: ¿cómo resumir y visualizar un conjunto de observaciones de forma que revele su estructura (centro, dispersión, forma, valores atípicos)? Es exactamente el problema que resuelve **esta misma Unidad 1**, mediante las medidas descriptivas y la visualización exploratoria de las secciones 1.1-1.4 y 6.

2. **Problema de Ajuste de la Distribución a los Datos**: dado que los datos son una muestra de un proceso aleatorio subyacente, ¿qué modelo probabilístico (Binomial, Poisson, Normal, Exponencial, Gamma, ...) describe mejor ese proceso? Se aborda en las **Unidades 2 a 5**, que desarrollan las familias de distribuciones discretas y continuas y sus criterios de ajuste.

3. **Problema de Estimación de Parámetros**: una vez elegida una familia de distribuciones, ¿cuál es el mejor valor puntual (o el mejor intervalo) para sus parámetros desconocidos a partir de la muestra? Se aborda en la **Unidad 7** (Inferencia y Estimación), con el Método de los Momentos (§1.9) y la Estimación de Máxima Verosimilitud — MLE (§6.2-6.3).

4. **Problema de Contraste de Afirmaciones sobre la Población**: ¿los datos observados son consistentes con una afirmación específica sobre la población (una media, una proporción, la igualdad entre dos grupos), o la evidencia es suficiente para rechazarla? Se aborda también en la **Unidad 7**, con el marco completo de contrastes paramétricos (Z-test, t-test, §1.1-1.8) y no paramétricos (Kolmogorov-Smirnov, Mann-Whitney-Wilcoxon, Kruskal-Wallis, Signos y Mediana, §1.10-1.11).

5. **Problema de Correlación y Regresión**: ¿existe una relación estadística entre dos o más variables, y puede esa relación usarse para predecir una a partir de la otra? Se aborda en la **Unidad 8** (Proyecto Integrador), sección "Regresión Lineal y Correlación" (§7), que cubre desde el coeficiente de correlación de Pearson y la regresión por mínimos cuadrados (§7.1-7.2) hasta la correlación de rango, la correlación múltiple/parcial y los diagnósticos de regresión (§7.3-7.7).

Este mapa no es una curiosidad académica: cada vez que se enfrente un conjunto de datos nuevo, identificar primero *cuál* de estos cinco problemas se está resolviendo evita aplicar la herramienta equivocada (por ejemplo, calcular solo estadística descriptiva cuando la pregunta real exige contrastar una afirmación sobre la población).

---

## 2. Ejemplo Analítico Paso a Paso: Caracterización de Nanopartículas de Oro Sintetizadas

### 2.1 Contexto Aplicado en Nanotecnología
En un laboratorio de síntesis coloidal, se produjo un lote de nanopartículas de oro (AuNPs) mediante el método de reducción con citrato de sodio (método de Turkevich). Un ingeniero en nanotecnología midió, mediante microscopía electrónica de transmisión (TEM), el diámetro (en nanómetros) de una muestra aleatoria de $n = 10$ nanopartículas del lote:

$$x = \{12.1,\ 13.4,\ 11.8,\ 14.2,\ 12.9,\ 13.0,\ 40.5,\ 12.5,\ 13.8,\ 12.3\}$$

La observación de $40.5\ \text{nm}$ es sospechosa de ser un artefacto de agregación (dos nanopartículas fusionadas percibidas como una sola durante el conteo automatizado de la imagen TEM). El objetivo es calcular las estadísticas descriptivas de la muestra y evaluar, usando el criterio del IQR, si esa observación debe tratarse como un valor atípico antes de reportar el diámetro característico del lote.

### 2.2 Paso 1: Media y Mediana
$$\bar{x} = \frac{12.1+13.4+11.8+14.2+12.9+13.0+40.5+12.5+13.8+12.3}{10} = \frac{156.5}{10} = \boxed{15.65\ \text{nm}}$$

Ordenando la muestra: $\{11.8,\ 12.1,\ 12.3,\ 12.5,\ 12.9,\ 13.0,\ 13.4,\ 13.8,\ 14.2,\ 40.5\}$. Con $n=10$ (par), la mediana es el promedio de las posiciones 5 y 6:
$$\tilde{x} = \frac{12.9 + 13.0}{2} = \boxed{12.95\ \text{nm}}$$

La gran diferencia entre $\bar{x}=15.65$ y $\tilde{x}=12.95$ es la primera señal cuantitativa de que la media está siendo distorsionada por un valor extremo.

### 2.3 Paso 2: Varianza y Desviación Estándar Muestral
Con $\bar{x} = 15.65$:
$$\sum_{i=1}^{10} (x_i - \bar{x})^2 = (12.1-15.65)^2 + \dots + (12.3-15.65)^2 \approx 691.27$$
$$s^2 = \frac{691.27}{10-1} \approx \boxed{76.81\ \text{nm}^2}$$
$$s = \sqrt{76.81} \approx \boxed{8.76\ \text{nm}}$$

Una desviación estándar de $8.76\ \text{nm}$ es enorme frente a diámetros que en su mayoría rondan los $12$–$14\ \text{nm}$, lo que confirma la sospecha inicial.

### 2.4 Paso 3: Cuartiles, IQR y Detección de Outlier
Con los datos ordenados, $Q_1$ (percentil 25, interpolación lineal) cae entre $12.3$ y $12.5$, y $Q_3$ (percentil 75) entre $13.4$ y $13.8$:
$$Q_1 \approx 12.35\ \text{nm}, \qquad Q_3 \approx 13.70\ \text{nm}$$
$$IQR = Q_3 - Q_1 = 13.70 - 12.35 = \boxed{1.35\ \text{nm}}$$

El límite superior para outliers es:
$$Q_3 + 1.5 \cdot IQR = 13.70 + 1.5(1.35) = 13.70 + 2.025 = \boxed{15.725\ \text{nm}}$$

Como $40.5\ \text{nm} > 15.725\ \text{nm}$, la observación se clasifica formalmente como **valor atípico** y debe excluirse antes de reportar el diámetro característico del lote de síntesis, o investigarse por separado como evidencia de agregación de nanopartículas.

### 2.5 Paso 4: Estadísticas Recalculadas sin el Outlier
Excluyendo $40.5\ \text{nm}$, con $n=9$:
$$\bar{x}_{\text{limpia}} = \frac{116.0}{9} \approx \boxed{12.89\ \text{nm}}$$

Este valor coincide mucho más con la mediana original ($12.95\ \text{nm}$), confirmando que el diámetro característico real del lote de AuNPs sintetizadas es de aproximadamente $12.9\ \text{nm}$, no $15.65\ \text{nm}$.

### 2.6 Paso 5: Prueba Unitaria con pytest

Todo cálculo estadístico manual debe verificarse computacionalmente antes de reportarse — la misma disciplina de `pytest` que ya conoces de Lógica de Programación aplica aquí: en vez de solo confiar en la derivación a mano, se escribe una prueba que falla si el resultado numérico se aparta del valor esperado.

```python
import numpy as np
import pytest

diametros_nm = np.array([12.1, 13.4, 11.8, 14.2, 12.9, 13.0, 40.5, 12.5, 13.8, 12.3])


def test_media_muestral_coincide_con_calculo_manual():
    assert np.mean(diametros_nm) == pytest.approx(15.65, rel=1e-4)


def test_desviacion_estandar_muestral_usa_correccion_de_bessel():
    ## ddof=1 (denominador n-1) -- sin esto, pytest fallaria con s ~ 8.31 en vez de 8.76
    assert np.std(diametros_nm, ddof=1) == pytest.approx(8.76, rel=1e-3)


def test_valor_atipico_de_agregacion_se_detecta_por_criterio_iqr():
    q1, q3 = np.percentile(diametros_nm, [25, 75])
    limite_superior = q3 + 1.5 * (q3 - q1)
    assert 40.5 > limite_superior


def test_media_sin_el_atipico_se_acerca_a_la_mediana_original():
    diametros_limpios = diametros_nm[diametros_nm != 40.5]
    mediana_original = np.median(diametros_nm)
    assert np.mean(diametros_limpios) == pytest.approx(mediana_original, abs=0.1)
```

`test_desviacion_estandar_muestral_usa_correccion_de_bessel` es la prueba más importante del bloque: si alguien olvida `ddof=1` (equivalente al denominador $n-1$ visto en el §1.2), NumPy calcula la desviación estándar **poblacional** por defecto ($\sigma$, denominador $n$) y la prueba falla — exactamente el error conceptual descrito en "Errores Comunes" al final de esta unidad.

---

## 3. Código de Verificación Simbólica (SymPy)

```python
import sympy as sp
from IPython.display import display, Math

## 1. Definición simbólica de la muestra y su tamaño
datos = [12.1, 13.4, 11.8, 14.2, 12.9, 13.0, 40.5, 12.5, 13.8, 12.3]
x_vals = [sp.Rational(str(v)) for v in datos]
n = len(x_vals)

## 2. Media muestral simbólica (fracción exacta)
media_expr = sp.Add(*x_vals) / n
media_exacta = sp.nsimplify(media_expr)

display(Math(fr"\bar{{x}} = \frac{{1}}{{{n}}} \sum_{{i=1}}^{{{n}}} x_i = {sp.latex(media_expr)} = {float(media_expr):.4f}"))

## 3. Varianza muestral simbólica (n-1 grados de libertad)
suma_cuadrados = sp.Add(*[(xi - media_expr)**2 for xi in x_vals])
varianza_expr = suma_cuadrados / (n - 1)

display(Math(fr"s^2 = \frac{{1}}{{n-1}} \sum (x_i - \bar{{x}})^2 = \boxed{{{float(varianza_expr):.4f}}}"))
display(Math(fr"s = \sqrt{{s^2}} = \boxed{{{float(sp.sqrt(varianza_expr)):.4f}}}"))
```

---

## 4. Solución Computacional en Python (SciPy & Statsmodels)

```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

## Configuración visual profesional
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 5)

## --- PARTE A: Estadísticas Descriptivas con scipy.stats.describe ---
diametros_aunp = np.array([12.1, 13.4, 11.8, 14.2, 12.9, 13.0, 40.5, 12.5, 13.8, 12.3])

resumen = stats.describe(diametros_aunp)
q1, mediana, q3 = np.percentile(diametros_aunp, [25, 50, 75])
iqr = q3 - q1
limite_superior = q3 + 1.5 * iqr

print("--- RESUMEN ESTADÍSTICO: DIÁMETRO DE NANOPARTÍCULAS DE ORO (TEM) ---")
print(f"n:                        {resumen.nobs}")
print(f"Media:                    {resumen.mean:.4f} nm")
print(f"Mediana:                  {mediana:.4f} nm")
print(f"Varianza muestral:        {resumen.variance:.4f} nm^2")
print(f"Desviación estándar:      {np.sqrt(resumen.variance):.4f} nm")
print(f"Asimetría (skewness):     {resumen.skewness:.4f}")
print(f"Curtosis (exceso):        {resumen.kurtosis:.4f}")
print(f"Q1, Q3, IQR:              {q1:.2f}, {q3:.2f}, {iqr:.2f}")
print(f"Límite superior outliers: {limite_superior:.4f} nm")

## Filtrado del outlier detectado por criterio IQR
diametros_limpios = diametros_aunp[diametros_aunp <= limite_superior]
print(f"\nMedia sin outlier:        {diametros_limpios.mean():.4f} nm")

## --- PARTE A-bis: Max, Min, Coeficiente de Variación y Media Geométrica ---
## scipy.stats.describe (arriba) ya reporta media/varianza/skewness/kurtosis,
## pero no expone max/min explícitos ni CV/media geométrica -- se calculan aquí.
from scipy.stats import gmean

max_val = diametros_limpios.max()
min_val = diametros_limpios.min()
rango_limpio = max_val - min_val
media_limpia = diametros_limpios.mean()
std_limpia = diametros_limpios.std(ddof=1)
cv_limpia = std_limpia / media_limpia
gm_limpia = gmean(diametros_limpios)

print("\n--- ESTADÍSTICAS ADICIONALES (muestra sin outlier, n=9) ---")
print(f"Máximo:                       {max_val:.4f} nm")
print(f"Mínimo:                       {min_val:.4f} nm")
print(f"Rango:                        {rango_limpio:.4f} nm")
print(f"Coeficiente de Variación:     {cv_limpia:.4f}  ({cv_limpia*100:.2f}%)")
print(f"Media Geométrica:             {gm_limpia:.4f} nm")
```

**Verificación numérica** (ejecutado sobre `diametros_limpios`, la muestra de $n=9$ tras excluir el outlier de agregación de la Sección 2.4):

$$\boxed{\text{Max} = 14.20\ \text{nm}, \quad \text{Min} = 11.80\ \text{nm}, \quad \text{CV} = 6.21\%, \quad \text{Media Geométrica} = 12.8670\ \text{nm}}$$

**Interpretación**: el Coeficiente de Variación ($CV = s/\bar{x}$) expresa la dispersión relativa a la escala de la media — a diferencia de $s$ (en nm), el CV es adimensional, lo que permite comparar la variabilidad de lotes de nanopartículas con diámetros promedio muy distintos (ver gráfico dedicado en la Sección 6.7). La Media Geométrica ($12.8670$ nm) es ligeramente menor que la Media Aritmética ($12.8889$ nm) — una relación que se cumple siempre para datos positivos no idénticos (desigualdad AM-GM), y que se vuelve más pronunciada cuanto mayor es la dispersión relativa de los datos (ver comparación explícita en la Sección 6.10 con un dataset de tasas de rendimiento).

```python
## --- PARTE B: Visualización Exploratoria (Boxplot + Histograma con KDE) ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

## Gráfico 1: Boxplot mostrando el outlier de agregación
sns.boxplot(x=diametros_aunp, color="goldenrod", ax=axes[0])
axes[0].set_title("Boxplot: Diámetro de AuNPs (con outlier de agregación)", fontsize=12, fontweight="bold")
axes[0].set_xlabel("Diámetro (nm)")

## Gráfico 2: Histograma + KDE de la muestra limpia
sns.histplot(diametros_limpios, kde=True, color="darkorange", bins=6, ax=axes[1])
axes[1].axvline(diametros_limpios.mean(), color='red', linestyle='--', label=f'Media = {diametros_limpios.mean():.2f} nm')
axes[1].set_title("Histograma + KDE: Diámetro de AuNPs (sin outlier)", fontsize=12, fontweight="bold")
axes[1].set_xlabel("Diámetro (nm)")
axes[1].set_ylabel("Frecuencia / Densidad")
axes[1].legend()

plt.tight_layout()
plt.show()
```

---

## 5. Interpretación Post-Gráfico & Diccionario de Variables

### 5.1 Interpretación de Resultados Computacionales
1. **Discrepancia Media–Mediana como Señal de Asimetría**: la diferencia inicial de casi $3\ \text{nm}$ entre $\bar{x}$ y la mediana, junto con una asimetría (skewness) fuertemente positiva, es la firma estadística característica de una distribución con cola derecha causada por un valor extremo — coherente con un evento de agregación de nanopartículas durante la síntesis o el conteo en TEM.
2. **Boxplot como Herramienta de Control de Calidad**: el diagrama de caja hace visualmente evidente el punto atípico fuera del bigote superior, validando el criterio analítico de $Q_3 + 1.5 \cdot IQR$ calculado a mano. En control de calidad de síntesis coloidal, este tipo de detección automática es rutinaria antes de reportar el diámetro característico de un lote.
3. **Distribución Limpia Aproximadamente Simétrica**: una vez excluido el outlier, el histograma con KDE muestra una distribución unimodal y razonablemente simétrica alrededor de $12.9\ \text{nm}$, consistente con la dispersión de tamaño esperada (polidispersidad) de un proceso de nucleación y crecimiento bien controlado.

### 5.2 Diccionario de Variables Nanotecnológicas
* $x_i$: diámetro medido de la $i$-ésima nanopartícula de oro en la muestra TEM, en nanómetros (nm).
* $n$: tamaño de la muestra de nanopartículas medidas ($n=10$).
* $\bar{x}$: diámetro promedio muestral de las nanopartículas de oro.
* $s^2, s$: varianza y desviación estándar muestral del diámetro, indicadoras de la polidispersidad del lote sintetizado.
* $Q_1, Q_3, IQR$: cuartiles y rango intercuartílico del diámetro, usados como criterio robusto de control de calidad para descartar artefactos de agregación en la síntesis de nanopartículas.

---

## 6. Visualización Individual de Conceptos Descriptivos

Las secciones anteriores presentaron los 12 conceptos descriptivos de esta unidad (Máximo, Mínimo, Rango, Media, Varianza, Desviación Estándar, Coeficiente de Variación, Moda, Mediana, Media Geométrica, Asimetría y Curtosis) agrupados en tablas numéricas y gráficos combinados. Esta sección dedica **un gráfico individual a cada concepto**, aislando visualmente qué mide cada uno y sobre qué parte de la distribución actúa — un refuerzo pedagógico distinto de (y complementario a) los gráficos combinados de las Secciones 4 y 5.

Salvo donde se indique lo contrario, todos los gráficos reutilizan `diametros_aunp` (con outlier, $n=10$) o `diametros_limpios` (sin outlier, $n=9$), ya definidos en la Sección 4, para mantener continuidad narrativa con el resto de la unidad. Los tres conceptos que requieren comparar contra un segundo dataset (CV, Media Geométrica, Skewness, Kurtosis) generan esos datasets sintéticos con `np.random.seed()` fijo.

```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
```

### 6.1 Máximo

```python
plt.figure(figsize=(9, 3))
sns.stripplot(x=diametros_limpios, color="steelblue", size=10, alpha=0.7)
idx_max = np.argmax(diametros_limpios)
plt.scatter(diametros_limpios[idx_max], 0, color="crimson", s=200, zorder=5, label=f"Máximo = {diametros_limpios[idx_max]:.2f} nm")
plt.axvline(diametros_limpios[idx_max], color="crimson", linestyle="--", alpha=0.6)
plt.title(f"Máximo del Diámetro de AuNPs (sin outlier): {diametros_limpios.max():.2f} nm", fontweight="bold")
plt.xlabel("Diámetro (nm)")
plt.legend()
plt.tight_layout()
plt.show()
```

$$\boxed{\text{Max} = 14.20\ \text{nm}}$$

### 6.2 Mínimo

```python
plt.figure(figsize=(9, 3))
sns.stripplot(x=diametros_limpios, color="steelblue", size=10, alpha=0.7)
idx_min = np.argmin(diametros_limpios)
plt.scatter(diametros_limpios[idx_min], 0, color="darkgreen", s=200, zorder=5, label=f"Mínimo = {diametros_limpios[idx_min]:.2f} nm")
plt.axvline(diametros_limpios[idx_min], color="darkgreen", linestyle="--", alpha=0.6)
plt.title(f"Mínimo del Diámetro de AuNPs (sin outlier): {diametros_limpios.min():.2f} nm", fontweight="bold")
plt.xlabel("Diámetro (nm)")
plt.legend()
plt.tight_layout()
plt.show()
```

$$\boxed{\text{Min} = 11.80\ \text{nm}}$$

### 6.3 Rango

```python
plt.figure(figsize=(9, 3))
sns.stripplot(x=diametros_limpios, color="steelblue", size=10, alpha=0.7)
r_min, r_max = diametros_limpios.min(), diametros_limpios.max()
plt.annotate("", xy=(r_max, 0.15), xytext=(r_min, 0.15),
             arrowprops=dict(arrowstyle="<->", color="darkorange", lw=2))
plt.text((r_min + r_max) / 2, 0.22, f"R = {r_max - r_min:.2f} nm", ha="center", color="darkorange", fontweight="bold")
plt.title(f"Rango del Diámetro de AuNPs (sin outlier): {r_max - r_min:.2f} nm", fontweight="bold")
plt.xlabel("Diámetro (nm)")
plt.ylim(-0.3, 0.4)
plt.tight_layout()
plt.show()
```

$$\boxed{R = 2.40\ \text{nm}}$$

### 6.4 Media

```python
plt.figure(figsize=(9, 4))
sns.histplot(diametros_limpios, bins=5, color="skyblue", edgecolor="black")
plt.axvline(diametros_limpios.mean(), color="red", linestyle="--", linewidth=2.5, label=f"Media = {diametros_limpios.mean():.2f} nm")
plt.title(f"Media del Diámetro de AuNPs (sin outlier): {diametros_limpios.mean():.2f} nm", fontweight="bold")
plt.xlabel("Diámetro (nm)")
plt.ylabel("Frecuencia")
plt.legend()
plt.tight_layout()
plt.show()
```

$$\boxed{\bar{x} = 12.8889\ \text{nm}}$$

### 6.5 Varianza

```python
media_l, std_l = diametros_limpios.mean(), diametros_limpios.std(ddof=1)
plt.figure(figsize=(9, 4))
sns.histplot(diametros_limpios, bins=5, color="skyblue", edgecolor="black")
plt.axvspan(media_l - std_l, media_l + std_l, color="orange", alpha=0.25, label=f"$[\\bar{{x}}-s,\\ \\bar{{x}}+s]$, $s^2$ = {std_l**2:.4f} nm²")
plt.axvline(media_l, color="red", linestyle="--", linewidth=2)
plt.title(f"Varianza del Diámetro de AuNPs: s² = {std_l**2:.4f} nm²", fontweight="bold")
plt.xlabel("Diámetro (nm)")
plt.ylabel("Frecuencia")
plt.legend()
plt.tight_layout()
plt.show()
```

$$\boxed{s^2 = 0.6411\ \text{nm}^2}$$

**Nota**: la varianza se ilustra vía la banda de una desviación estándar porque $s^2$ está en unidades al cuadrado ($\text{nm}^2$) y no puede representarse directamente sobre el eje de diámetro; ver Sección 6.6 para la distinción con $s$.

### 6.6 Desviación Estándar

```python
plt.figure(figsize=(9, 4))
sns.histplot(diametros_limpios, bins=5, color="skyblue", edgecolor="black")
plt.axvspan(media_l - std_l, media_l + std_l, color="teal", alpha=0.25, label=f"$[\\bar{{x}}-s,\\ \\bar{{x}}+s]$, $s$ = {std_l:.4f} nm")
plt.axvline(media_l, color="red", linestyle="--", linewidth=2, label=f"Media = {media_l:.2f} nm")
plt.title(f"Desviación Estándar del Diámetro de AuNPs: s = {std_l:.4f} nm", fontweight="bold")
plt.xlabel("Diámetro (nm)")
plt.ylabel("Frecuencia")
plt.legend()
plt.tight_layout()
plt.show()
```

$$\boxed{s = 0.8007\ \text{nm}}$$

**Distinción Varianza vs. Desviación Estándar** (refuerza el misconception documentado en Errores Comunes): la banda sombreada es geométricamente idéntica en 6.5 y 6.6 — lo que cambia es la magnitud que se reporta junto a ella. $s = 0.8007\ \text{nm}$ está en las mismas unidades que el diámetro y es directamente interpretable sobre el eje; $s^2 = 0.6411\ \text{nm}^2$ no lo está.

### 6.7 Coeficiente de Variación

```python
np.random.seed(42)
lote_A = stats.norm.rvs(loc=13.0, scale=0.5, size=200)   # baja dispersión relativa
lote_B = stats.norm.rvs(loc=13.0, scale=1.5, size=200)   # dispersión media
lote_C = stats.norm.rvs(loc=13.0, scale=3.0, size=200)   # alta dispersión relativa

lotes = {"Lote A (σ=0.5)": lote_A, "Lote B (σ=1.5)": lote_B, "Lote C (σ=3.0)": lote_C}
cvs = {nombre: (lote.std(ddof=1) / lote.mean()) * 100 for nombre, lote in lotes.items()}

plt.figure(figsize=(8, 4.5))
barras = plt.bar(cvs.keys(), cvs.values(), color=["#4C72B0", "#DD8452", "#C44E52"])
for barra, v in zip(barras, cvs.values()):
    plt.text(barra.get_x() + barra.get_width() / 2, v, f"{v:.2f}%", ha="center", va="bottom", fontweight="bold")
plt.title("Coeficiente de Variación: 3 Lotes de AuNPs con Media ≈ 13 nm, Distinta Dispersión", fontweight="bold")
plt.ylabel("CV (%)")
plt.tight_layout()
plt.show()
```

$$\boxed{CV_A = 3.59\%, \quad CV_B = 11.28\%, \quad CV_C = 23.40\%}$$

**Interpretación**: los tres lotes comparten prácticamente la misma media ($\approx 13\ \text{nm}$), por lo que $s$ por sí sola bastaría para compararlos. El CV se vuelve indispensable cuando se comparan datasets de **distinta escala** (por ejemplo, diámetro en nm vs. band gap en eV): al ser adimensional, permite decir "el Lote C es relativamente 6.5 veces más disperso que el Lote A" sin que las unidades interfieran.

### 6.8 Moda

```python
plt.figure(figsize=(9, 4))
counts, bin_edges, patches = plt.hist(diametros_limpios, bins=4, color="lightgray", edgecolor="black")
idx_modal = np.argmax(counts)
patches[idx_modal].set_facecolor("purple")
plt.title(f"Clase Modal del Diámetro de AuNPs: [{bin_edges[idx_modal]:.2f}, {bin_edges[idx_modal+1]:.2f}) nm, frecuencia={int(counts[idx_modal])}", fontweight="bold")
plt.xlabel("Diámetro (nm)")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.show()
```

$$\boxed{\text{Clase modal} = [11.80,\ 12.40)\ \text{nm}, \quad \text{frecuencia} = 3}$$

### 6.9 Mediana

```python
plt.figure(figsize=(9, 3.5))
sns.boxplot(x=diametros_aunp, color="goldenrod")
mediana_out = np.median(diametros_aunp)
media_out = diametros_aunp.mean()
plt.axvline(mediana_out, color="green", linewidth=2.5, label=f"Mediana = {mediana_out:.2f} nm")
plt.axvline(media_out, color="red", linestyle="--", linewidth=2.5, label=f"Media = {media_out:.2f} nm")
plt.title("Mediana vs. Media del Diámetro de AuNPs (con outlier de agregación)", fontweight="bold")
plt.xlabel("Diámetro (nm)")
plt.legend()
plt.tight_layout()
plt.show()
```

$$\boxed{\tilde{x} = 12.95\ \text{nm} \ll \bar{x} = 15.65\ \text{nm}}$$

**Interpretación**: con el outlier de agregación incluido, la mediana ($12.95\ \text{nm}$) permanece casi idéntica a la media sin outlier de la Sección 2.5 ($12.89\ \text{nm}$), mientras que la media con outlier se dispara a $15.65\ \text{nm}$ — evidencia visual directa de la robustez de la mediana frente a valores extremos.

### 6.10 Media Geométrica

```python
np.random.seed(7)
## Tasas de rendimiento de síntesis por lote (factores multiplicativos, siempre positivos)
tasas_rendimiento = np.random.uniform(0.85, 1.35, size=12)

media_aritmetica_t = tasas_rendimiento.mean()
media_geometrica_t = stats.gmean(tasas_rendimiento)

plt.figure(figsize=(7, 4.5))
barras = plt.bar(["Media Aritmética", "Media Geométrica"], [media_aritmetica_t, media_geometrica_t],
                  color=["#4C72B0", "#55A868"])
for barra, v in zip(barras, [media_aritmetica_t, media_geometrica_t]):
    plt.text(barra.get_x() + barra.get_width() / 2, v, f"{v:.4f}", ha="center", va="bottom", fontweight="bold")
plt.title("Media Aritmética vs. Media Geométrica: Tasas de Rendimiento de Síntesis (12 lotes)", fontweight="bold")
plt.ylabel("Factor de rendimiento")
plt.ylim(0, max(media_aritmetica_t, media_geometrica_t) * 1.25)
plt.tight_layout()
plt.show()
```

$$\boxed{\bar{x}_{\text{aritmética}} = 1.1150, \quad \bar{x}_{\text{geométrica}} = 1.1063}$$

**Interpretación**: a diferencia del diámetro de AuNPs (Sección 6.4), las tasas de rendimiento son factores multiplicativos, no medidas aditivas — la Media Geométrica es la medida correcta para "tasa de crecimiento promedio compuesto" (idéntica lógica que una tasa de interés compuesto), y siempre es $\le$ la Media Aritmética para datos positivos no idénticos (desigualdad AM-GM), como se observa aquí.

### 6.11 Asimetría (Skewness)

```python
np.random.seed(11)
muestra_simetrica = stats.norm.rvs(loc=13, scale=1, size=10)

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
sns.histplot(diametros_aunp, bins=6, color="darkorange", ax=axes[0])
axes[0].set_title(f"AuNPs reales (con outlier)\nSkewness = {stats.skew(diametros_aunp):.4f}", fontweight="bold")
axes[0].set_xlabel("Diámetro (nm)")

sns.histplot(muestra_simetrica, bins=6, color="mediumseagreen", ax=axes[1])
axes[1].set_title(f"Muestra sintética simétrica\nSkewness = {stats.skew(muestra_simetrica):.4f}", fontweight="bold")
axes[1].set_xlabel("Valor")

plt.tight_layout()
plt.show()
```

$$\boxed{g_{1,\text{AuNPs}} = 2.6298 \ (\text{asimetría positiva fuerte}), \quad g_{1,\text{sintética}} = -0.3872 \ (\text{aprox. simétrica})}$$

### 6.12 Curtosis (Kurtosis)

```python
np.random.seed(12)
leptocurtica = stats.t.rvs(df=3, size=2000)      # colas pesadas
platicurtica = stats.uniform.rvs(loc=-3, scale=6, size=2000)  # colas ligeras

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
sns.histplot(leptocurtica, bins=50, stat="density", color="indianred", kde=True, ax=axes[0])
axes[0].set_title(f"t-Student (df=3): Leptocúrtica\nKurtosis (exceso) = {stats.kurtosis(leptocurtica):.4f}", fontweight="bold")
axes[0].set_xlim(-10, 10)

sns.histplot(platicurtica, bins=50, stat="density", color="cornflowerblue", kde=True, ax=axes[1])
axes[1].set_title(f"Uniforme: Platicúrtica\nKurtosis (exceso) = {stats.kurtosis(platicurtica):.4f}", fontweight="bold")

plt.tight_layout()
plt.show()
```

$$\boxed{g_{2,\text{t(3)}} = 36.6526 \ (\text{leptocúrtica}), \quad g_{2,\text{uniforme}} = -1.2285 \ (\text{platicúrtica})}$$

**Interpretación**: la t-Student con 3 grados de libertad tiene colas extremadamente pesadas (exceso de curtosis muy alto, valores atípicos mucho más probables que en una Normal), mientras que la Uniforme tiene colas inexistentes por definición (soporte acotado, exceso de curtosis negativo cercano al mínimo teórico de $-1.2$) — los dos extremos del espectro de curtosis, frente al valor de referencia $g_2=0$ de la distribución Normal.

---

## 7. Módulo de Simulación: Estimación No Paramétrica de Densidad (KDE)

En el análisis de datos de caracterización nanotecnológica, cuando no se presupone un modelo paramétrico estricto para el diámetro de las nanopartículas, se emplea la **Estimación No Paramétrica de Densidad por Kernel (KDE)**.

### 7.1 Definición Matemática de KDE
Dada una muestra independiente de tamaño $n$, el estimador de densidad por kernel $f_h(x)$ viene dado por:
$$f_h(x) = \frac{1}{nh} \sum_{i=1}^n K\left(\frac{x - x_i}{h}\right)$$
donde $K(u)$ es el kernel gaussiano $K(u) = \frac{1}{\sqrt{2\pi}} e^{-u^2/2}$ y $h > 0$ es el ancho de banda (bandwidth).

### 7.2 Implementación Computacional en Python

```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

## Generación de muestra sintética bimodal (diámetro de nanopartículas coloidales, dos poblaciones)
np.random.seed(101)
muestras_nano = np.concatenate([
    stats.norm.rvs(loc=15, scale=2, size=300),
    stats.norm.rvs(loc=35, scale=5, size=700)
])

## Estimación KDE con ancho de banda de Silverman
kde = stats.gaussian_kde(muestras_nano, bw_method='silverman')
x_grid = np.linspace(5, 55, 500)
pdf_kde = kde.evaluate(x_grid)

## Visualización
plt.figure(figsize=(10, 5))
sns.histplot(muestras_nano, bins=30, stat="density", color="skyblue", label="Histograma Muestral")
plt.plot(x_grid, pdf_kde, color="darkblue", linewidth=2.5, label="Estimación KDE (Kernel Gaussiano)")
plt.title("Estimación No Paramétrica de Densidad de Diámetro de Nanopartículas (KDE)", fontsize=12, fontweight="bold")
plt.xlabel("Diámetro (nm)")
plt.ylabel("Densidad de Probabilidad")
plt.legend()
plt.tight_layout()
plt.show()

print(f"Estimación KDE completada sobre n = {len(muestras_nano)} observaciones.")
print(f"Ancho de banda (bandwidth) de Silverman: {kde.factor:.4f}")
```

### 7.3 Selección de Kernel y Optimización del Ancho de Banda con `GridSearchCV`

El KDE de la Sección 7.2 usa la regla de Silverman para fijar el ancho de banda $h$ — una heurística rápida, pero no necesariamente óptima para una muestra específica. La elección de $h$ es el parámetro más determinante del KDE: un $h$ demasiado pequeño produce sobreajuste (una curva con un pico por cada observación, alta varianza); un $h$ demasiado grande produce subajuste (pierde la multimodalidad real, alto sesgo). `scikit-learn` permite optimizar $h$ formalmente mediante **validación cruzada** (`GridSearchCV`), maximizando la log-verosimilitud promedio de los datos dejados fuera en cada partición — un criterio objetivo en vez de una regla heurística fija.

La elección del **kernel** en sí (Gaussiano, Epanechnikov, Tophat, ...) es secundaria frente al ancho de banda: el kernel Gaussiano es una elección por defecto adecuada en la mayoría de los casos, mientras que kernels de soporte finito (Epanechnikov, Tophat) solo aportan una ventaja clara cuando se sabe *a priori* que la densidad real es exactamente cero fuera de un rango (por ejemplo, un diámetro de nanopartícula, que nunca es negativo).

```python
import numpy as np
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt

## Reutiliza la muestra bimodal ya generada en 7.2 (seed=101, n=1000)
X = muestras_nano.reshape(-1, 1)

## Rango de anchos de banda candidatos (escala logarítmica)
bandwidths = 10 ** np.linspace(-1, 1, 30)

## GridSearchCV con validación cruzada de 5 particiones, kernel Gaussiano fijo
grid = GridSearchCV(
    KernelDensity(kernel="gaussian"),
    {"bandwidth": bandwidths},
    cv=5,
)
grid.fit(X)

bandwidth_optimo = grid.best_params_["bandwidth"]
print(f"Ancho de banda óptimo (GridSearchCV, cv=5): {bandwidth_optimo:.4f}")
print(f"Ancho de banda de Silverman (Sección 7.2, referencia): {kde.factor * muestras_nano.std(ddof=1):.4f}")

## KDE final con el ancho de banda optimizado
kde_optimo = KernelDensity(kernel="gaussian", bandwidth=bandwidth_optimo).fit(X)
x_grid_opt = np.linspace(5, 55, 500).reshape(-1, 1)
pdf_optima = np.exp(kde_optimo.score_samples(x_grid_opt))

plt.figure(figsize=(10, 5))
plt.plot(x_grid, pdf_kde, color="darkblue", linewidth=2, linestyle="--", label=f"KDE Silverman (h={kde.factor * muestras_nano.std(ddof=1):.2f})")
plt.plot(x_grid_opt.ravel(), pdf_optima, color="crimson", linewidth=2.5, label=f"KDE Óptimo GridSearchCV (h={bandwidth_optimo:.2f})")
plt.title("Comparación: KDE con Bandwidth de Silverman vs. Optimizado por Validación Cruzada", fontsize=11, fontweight="bold")
plt.xlabel("Diámetro (nm)")
plt.ylabel("Densidad de Probabilidad")
plt.legend()
plt.tight_layout()
plt.show()
```

**Resultado verificado** (seed=101, `bandwidths = 10**np.linspace(-1, 1, 30)`, `cv=5`):

$$\boxed{h_{\text{óptimo (GridSearchCV)}} \approx 0.9237}$$

**Interpretación**: el ancho de banda óptimo por validación cruzada difiere del de Silverman porque este último es una fórmula cerrada que asume implícitamente unimodalidad aproximada, mientras que la muestra de esta sección es explícitamente bimodal (dos poblaciones de nanopartículas coloidales superpuestas). `GridSearchCV` no hace ese supuesto: encuentra el $h$ que mejor predice datos no vistos dentro de la misma muestra, lo que en distribuciones multimodales típicamente favorece un ancho de banda más fino que el de Silverman, capaz de resolver ambos modos sin fragmentar la curva en picos espurios.

---

## 8. Módulo de Integración de Datos Reales: Materials Project API

En la investigación moderna en IA y Nanotecnología, el análisis estadístico descriptivo se aplica directamente sobre repositorios masivos de materiales como **Materials Project**. A diferencia del ejercicio de control de calidad de nanopartículas de oro (Sección 2), aquí se ilustra el mismo tipo de análisis descriptivo sobre un dataset con múltiples materiales.

### 8.1 Consulta y Análisis del Band Gap ($E_g$)
Mediante la librería oficial `mp-api` es posible extraer propiedades fisicoquímicas reales de materiales, como el *Band Gap* $E_g$ (eV), la *Energía de Formación por Átomo* $\Delta E_f$ y el *Volumen de Celda* $V$. El siguiente ejemplo simula la estructura de datos que retornaría dicha consulta para tres óxidos semiconductores:

```python
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, Math

## 1. Simulación de estructura de datos de Materials Project (mp-api)
## Campos: material_id, formula, band_gap (eV), formation_energy_per_atom (eV/atom), volume (A^3)
np.random.seed(2026)
n_materiales = 150

datos_materials_project = {
    "material_id": [f"mp-{1000 + i}" for i in range(n_materiales)],
    "formula": ["TiO2"]*50 + ["ZnO"]*50 + ["Fe2O3"]*50,
    "band_gap": np.concatenate([
        stats.norm.rvs(loc=3.2, scale=0.15, size=50),   # TiO2 (Anatasa)
        stats.norm.rvs(loc=3.37, scale=0.20, size=50),  # ZnO
        stats.norm.rvs(loc=2.1, scale=0.18, size=50)    # Fe2O3 (Hematita)
    ]),
}

df_mp = pd.DataFrame(datos_materials_project)

## 2. Análisis Estadístico Descriptivo de Band Gap (eV)
band_gap_data = df_mp["band_gap"]

media_bg = band_gap_data.mean()
mediana_bg = band_gap_data.median()
std_bg = band_gap_data.std()
skewness_bg = band_gap_data.skew()

display(Math(fr"\text{{Media: }} \bar{{X}} = {media_bg:.3f} \text{{ eV}}, \quad \text{{Mediana: }} \tilde{{X}} = {mediana_bg:.3f} \text{{ eV}}"))
display(Math(fr"\text{{Desviación Estándar: }} s = {std_bg:.3f} \text{{ eV}}, \quad \text{{Asimetría (Skewness): }} {skewness_bg:.3f}"))

## 3. Visualización Exploratoria: Histograma+KDE por material + Q-Q Plot
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

sns.histplot(data=df_mp, x="band_gap", hue="formula", kde=True, element="step", ax=axes[0], palette="Set1")
axes[0].set_title("Distribución de Band Gap por Material (Materials Project)", fontsize=11, fontweight="bold")
axes[0].set_xlabel("Band Gap (eV)")
axes[0].set_ylabel("Frecuencia")

stats.probplot(band_gap_data, dist="norm", plot=axes[1])
axes[1].set_title("Q-Q Plot de Band Gap vs Distribución Normal", fontsize=11, fontweight="bold")

plt.tight_layout()
plt.show()
```

### 8.2 Selección Automática de Distribución con `distfit`

El ajuste manual de distribuciones (comparar histograma, KDE y Q-Q plot "a ojo" contra candidatas teóricas, como en §8.1) no escala cuando se necesita evaluar sistemáticamente decenas de familias de distribuciones candidatas. La librería `distfit` automatiza ese proceso: ajusta un conjunto de distribuciones candidatas por máxima verosimilitud, calcula una métrica de bondad de ajuste (suma de residuos cuadrados, RSS, entre la densidad empírica y la teórica) para cada una, y devuelve la de mejor ajuste ordenadas por score.

```python
%pip install -q distfit
from distfit import distfit
import numpy as np
import scipy.stats as stats

## Reutiliza el Band Gap de TiO2 ya generado en la PARTE 1 de esta sección (n=50, seed=2026)
np.random.seed(2026)
banda_tio2 = stats.norm.rvs(loc=3.2, scale=0.15, size=50)

## Instanciar sobre el catálogo de distribuciones "populares" (evita explorar ~90 familias poco relevantes)
dfit = distfit(distr='popular')
dfit.fit_transform(banda_tio2, verbose=0)

mejor_dist = dfit.model['name']
mejores_parametros = dfit.model['params']
mejor_score = dfit.model['score']

print(f"Mejor distribución encontrada: {mejor_dist}")
print(f"Parámetros ajustados: {mejores_parametros}")
print(f"Score (RSS, menor es mejor ajuste): {mejor_score:.6f}")

## Visualización del ajuste (histograma empírico + PDF de la distribución ganadora)
dfit.plot()
```

**Resultado verificado** (seed=2026, $n=50$): la distribución de mejor ajuste según `distfit` sobre esta muestra es **`dweibull`** (Weibull doble/simétrica), con score $RSS \approx 0.198$, no la Normal usada para generar los datos.

$$\boxed{\text{Mejor ajuste (distfit)} = \texttt{dweibull}, \quad RSS \approx 0.1980}$$

**Interpretación**: este resultado no es un error — con $n=50$ observaciones, varias familias de distribuciones (Normal, Weibull doble, t-Student con muchos grados de libertad) producen densidades casi indistinguibles, y el criterio puramente numérico de `distfit` puede preferir una familia con un parámetro de forma adicional que absorbe el ruido muestral, aunque el proceso generador real sea Normal. Esto ilustra una limitación importante de la selección automática: `distfit` optimiza bondad de ajuste sobre la muestra observada, no verifica el proceso físico subyacente — su salida debe contrastarse siempre con el conocimiento del dominio (aquí, la física de bandas prohibidas de óxidos semiconductores no tiene ninguna razón teórica para seguir una Weibull doble) y, cuando sea posible, con una muestra de mayor tamaño.

## Errores Comunes / Misconceptions

* **Error**: Confundir la desviación estándar muestral ($s$, denominador $n-1$) con la poblacional ($\sigma$, denominador $n$).
  **Correcto**: usar $n-1$ (corrección de Bessel) siempre que se estime $\sigma$ a partir de una muestra — produce un estimador insesgado de la varianza poblacional; usar $n$ solo cuando se dispone de la población completa.

* **Error**: Usar la media aritmética como medida de tendencia central sin verificar la presencia de outliers extremos.
  **Correcto**: la media no es robusta — un solo valor extremo puede desplazarla arbitrariamente lejos del centro real de los datos. Ante outliers confirmados, reportar también la mediana (o una media recortada) y justificar cuál es más representativa.

* **Error**: Asumir que "media > mediana implica asimetría positiva" (y viceversa) como regla universal.
  **Correcto**: esa relación es válida solo como heurística para distribuciones unimodales razonablemente regulares. En distribuciones multimodales o con outliers extremos la relación puede romperse; el diagnóstico correcto de asimetría es el coeficiente de asimetría (skewness) o la inspección visual del histograma.

## Ejercicio Propuesto

Un laboratorio de caracterización sintetizó un tercer lote de nanopartículas de plata (AgNPs) con un método de reducción química modificado y midió, vía DLS, el diámetro (en nm) de $n=14$ partículas:

$$x = \{21.4,\ 22.1,\ 20.8,\ 23.3,\ 21.9,\ 22.5,\ 52.7,\ 21.2,\ 22.8,\ 21.1,\ 22.2,\ 21.6,\ 53.9,\ 22.0\}$$

1. Calcula la media, mediana y desviación estándar muestral de este lote.
2. Aplica el criterio del IQR para identificar todos los valores atípicos (pueden ser más de uno).
3. Recalcula la media excluyendo los valores atípicos detectados y compárala con la mediana del conjunto completo. ¿Cuál de las dos, la media original o la media sin atípicos, se acerca más a la mediana? Justifica por qué ocurre esto en términos de robustez estadística.

Escribe tu solución en una celda de código nueva en tu notebook. La celda de autoevaluación de la siguiente sección verificará tu resultado.

## Referencias

* Bruce, P., Bruce, A. & Gedeck, P. (2020). *Practical Statistics for Data Scientists: 50+ Essential Concepts Using R and Python* (2nd ed.). O'Reilly Media. Capítulos sobre estadística descriptiva y exploración de datos.
* Virtanen, P. et al. (2020). SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. *Nature Methods*, 17, 261-272. Documentación: [docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html)

## Herramientas de esta Unidad

**StatsTutorAgent** — resuelve tus dudas conceptuales sobre estadística descriptiva citando el contenido exacto de esta unidad, y te hace una pregunta socrática si detecta un error conceptual común (p. ej. confundir varianza muestral con poblacional) en vez de darte la respuesta directa:

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
            "⚠️ [Unidad 1] No se encontró el secreto GEMINI_API_KEY ni GOOGLE_API_KEY en Colab. "
            "Créalo en el ícono de llave 🔑 de la barra lateral izquierda para usar StatsTutorAgent."
        )

from src.multiagent_core.stats_tutor_agent import StatsTutorAgent

tutor = StatsTutorAgent(course_dir=Path("lecciones"))
print(tutor.ask("¿por qué la desviación estándar muestral usa n-1 en vez de n?"))
```

No requiere configuración adicional más allá de tu `GEMINI_API_KEY` (créala en [aistudio.google.com/apikey](https://aistudio.google.com/apikey) y agrégala como secreto de Colab o variable de entorno local).

## Autoevaluación

Guarda tu solución al Ejercicio Propuesto en un archivo separado y evalúala contra el pipeline de auditoría del curso:

```python
%%writefile solucion_ejercicio_u1.py
# Completa aquí tu solución al Ejercicio Propuesto de esta unidad.
import numpy as np

datos = np.array([21.4, 22.1, 20.8, 23.3, 21.9, 22.5, 52.7, 21.2, 22.8, 21.1, 22.2, 21.6, 53.9, 22.0])

# TODO: calcula media, mediana y desviación estándar muestral del lote de AgNPs
# TODO: aplica el criterio del IQR para detectar todos los valores atípicos (pueden ser más de uno)
# TODO: recalcula la media excluyendo los atípicos detectados y compárala con la mediana del conjunto completo
```

```python
from src.multiagent_core.code_auditor_agent import CodeAuditorAgent
from external_skills.pedagogy.socratic_debugger import SocraticDebugger

with open("solucion_ejercicio_u1.py", encoding="utf-8") as f:
    codigo_alumno = f.read()

auditor = CodeAuditorAgent()
resultado = auditor.audit_code(codigo_alumno)

if resultado["issues"] or resultado["metrics"]["has_security_risk"]:
    debugger = SocraticDebugger()
    for issue in resultado["issues"]:
        tipo_error = "syntax_error" if "SyntaxError" in issue else "generic"
        print("💡", debugger.generate_socratic_question(tipo_error, "Unidad 1"))
    for issue in resultado["security_issues"]:
        print("🔒", debugger.generate_socratic_question("security_risk", "Unidad 1"))
        print("   ", issue)
    print("\n--- Detalle técnico ---")
    print(resultado)
else:
    print("✅ Tu código pasa las verificaciones automáticas de estilo y seguridad.")
    print(resultado)
```
