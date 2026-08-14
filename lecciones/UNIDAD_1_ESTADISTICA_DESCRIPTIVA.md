# UNIDAD 1: Estadística Descriptiva y Análisis Exploratorio de Datos
> **Asignatura: Probabilidad y Estadística Inferencial**
> **UCEMICH — Ingeniería en IA y Nanotecnología**
> **Autor y Profesor: Mtro. Luis José Yudico Anaya**

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
