# UNIDAD 8: Proyecto Integrador: Inferencia Estadística y Modelado en Nanotecnología e IA

**Duración:** 1.5 semanas (9 horas)

**Curso:** Probabilidad y Estadística Inferencial

**Institución:** Universidad de la Ciénega del Estado de Michoacán de Ocampo (UCEMICH)

**Profesor:** Luis José Yudico Anaya

**Carrera:** Ingeniería en Nanotecnología

**Nivel:** Tercer Semestre

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Multiagent-AI-Lab/Probability-Statistics-Agentic-AI-Core/blob/master/notebooks/UNIDAD_8_PROYECTO_INTEGRADOR.ipynb)

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

## 1. Fundamentación Teórica: Metodología de Pruebas de Hipótesis y Evaluación de Proyectos

El **Proyecto Integrador** consolida las herramientas de Estadística Descriptiva, Teoría de la Probabilidad, Variables Aleatorias, Inferencia Estadística y Simulación Estocástica desarrolladas a lo largo del curso. En este marco, los estudiantes aplican la metodología completa de Pruebas de Hipótesis para la toma de decisiones basada en datos empíricos en sistemas nanotecnológicos y modelos de Inteligencia Artificial.

### 1.1 Estructura Axiomática de una Prueba de Hipótesis
Una prueba de hipótesis es un procedimiento probabilístico para evaluar si la evidencia empírica proporcionada por una muestra $x_1, x_2, \dots, x_n$ contradice una afirmación sobre el parámetro poblacional $\theta$.

1. **Hipótesis Nula ($H_0$)**: Afirmación de no efecto o estado por defecto (p. ej., $H_0: \mu_1 = \mu_2$).
2. **Hipótesis Alternativa ($H_1$ o $H_a$)**: Afirmación investigativa que se busca respaldar con evidencia empírica.
3. **Estadístico de Prueba ($T(X)$)**: Función de la muestra cuyo comportamiento bajo $H_0$ es conocido.
4. **Región de Rechazo / Región Crítica ($\mathcal{R}$)**: Conjunto de valores del estadístico donde se rechaza $H_0$ a un nivel de significancia $\alpha$.

### 1.2 Errores Tipo I, Tipo II y Potencia de la Prueba
* **Error Tipo I ($\alpha$)**: Rechazar $H_0$ siendo verdadera. $\alpha = P(\text{Rechazar } H_0 | H_0 \text{ es cierta})$.
* **Error Tipo II ($\beta$)**: No rechazar $H_0$ siendo falsa. $\beta = P(\text{No Rechazar } H_0 | H_1 \text{ es cierta})$.
* **Potencia de la Prueba ($1 - \beta$)**: Probabilidad de rechazar correctamente $H_0$ cuando $H_1$ es verdadera.

$$\text{Potencia} = 1 - \beta = P(\text{Rechazar } H_0 | H_1 \text{ es cierta})$$

---

## 2. Guía Estructurada del Proyecto Integrador (Paso a Paso)

El proyecto requiere desarrollar cinco fases metodológicas:
1. **Fase 1: Planteamiento del Problema Nanotecnológico**: Definir las variables físicas (diámetro de partícula, potencial zeta, conductividad térmica) y formular $H_0$ y $H_1$.
2. **Fase 2: Análisis Exploratorio de Datos (EDA)**: Calcular estadísticos descriptivos ($\bar{X}, S^2$, IQR) y verificar supuestos de normalidad (Shapiro-Wilk) y homocedasticidad (Levene).
3. **Fase 3: Verificación Simbólica en SymPy**: Derivar las expresiones exactas del estadístico de prueba y $p$-valor.
4. **Fase 4: Solución Computacional en Python**: Ejecutar pruebas de hipótesis t de Student o ANOVA y simular la curva de potencia por Monte Carlo.
5. **Fase 5: Conclusiones e Interpretación**: Traducir el resultado estadístico ($p < \alpha$) en una decisión técnica industrial.

### 2.1 Rúbrica de Evaluación del Proyecto Integrador

| Componente | Descripción | Ponderación |
|---|---|---|
| **1. Planteamiento e Hipótesis** | Formulación clara de $H_0$ y $H_1$ con marco nanotecnológico | 20% |
| **2. Verificación de Supuestos** | Pruebas de Shapiro-Wilk y Levene explicadas y aplicadas | 20% |
| **3. Rigor Estadístico y SymPy** | Cálculo del estadístico, $p$-valor y validación simbólica | 20% |
| **4. Código Python (`scipy.stats`)** | Script ejecutable, limpio y con visualización de resultados | 20% |
| **5. Visualización y Conclusión** | Gráfico de región crítica/comparación + interpretación final | 20% |

---

## 3. Ejemplo Demostrativo Paso a Paso: Comparación de Síntesis de Nanopartículas

### 3.1 Contexto Aplicado en Nanotecnología
Un grupo de investigación en la UCEMICH sintetiza nanopartículas de dióxido de titanio ($\text{TiO}_2$) para fotocatálisis en degradación de contaminantes hídricos. Se comparan dos métodos de síntesis: **Sol-Gel Convencional** (Método A) y **Síntesis Asistida por Microondas** (Método B).

Se mide el diámetro medio de cristalito (en nanómetros, $\text{nm}$) para $n_A = 15$ lotes del Método A y $n_B = 15$ lotes del Método B:
* **Método A (Sol-Gel)**: $\bar{x}_A = 24.5\text{ nm}, \quad s_A = 2.1\text{ nm}$
* **Método B (Microondas)**: $\bar{x}_B = 21.2\text{ nm}, \quad s_B = 1.8\text{ nm}$

A un nivel de significancia $\alpha = 0.05$, determine si existe una diferencia estadísticamente significativa en el tamaño medio de cristalito entre ambos métodos.

### 3.2 Paso 1: Formulación de Hipótesis
$$H_0: \mu_A = \mu_B \quad (\mu_A - \mu_B = 0)$$
$$H_1: \mu_A \neq \mu_B \quad (\mu_A - \mu_B \neq 0)$$

### 3.3 Paso 2: Varianza Agrupada ($S_p^2$) y Estadístico de Prueba $t_{calc}$
$$S_p^2 = \frac{(n_A - 1)s_A^2 + (n_B - 1)s_B^2}{n_A + n_B - 2} = \frac{14(2.1)^2 + 14(1.8)^2}{28} = \frac{14(4.41) + 14(3.24)}{28} = \frac{61.74 + 45.36}{28} = 3.825$$
$$S_p = \sqrt{3.825} \approx 1.95576\text{ nm}$$

Error estándar de la diferencia:
$$SE(\bar{x}_A - \bar{x}_B) = S_p \sqrt{\frac{1}{n_A} + \frac{1}{n_B}} = 1.95576 \sqrt{\frac{2}{15}} = 1.95576 \times 0.365148 \approx 0.7141\text{ nm}$$

Estadístico $t$ calculado:
$$\boxed{t_{calc} = \frac{\bar{x}_A - \bar{x}_B}{SE} = \frac{24.5 - 21.2}{0.7141} = \frac{3.3}{0.7141} \approx 4.6212}$$

### 3.4 Paso 3: Región de Rechazo y Decisión
Grados de libertad $\nu = 15 + 15 - 2 = 28$. Para $\alpha = 0.05$ (dos colas), el valor crítico de la distribución $t$ de Student es $t_{0.025, 28} \approx 2.0484$.

Puesto que $|t_{calc}| = 4.6212 > 2.0484$, **se rechaza la hipótesis nula $H_0$** con un $p$-valor de $p < 0.0001$.

---

## 4. Código de Verificación Simbólica (SymPy)

```python
import sympy as sp
from IPython.display import display, Math

## 1. Definición de símbolos
mean_a, mean_b = sp.symbols('\\bar{X}_A \\bar{X}_B', real=True)
s_a, s_b = sp.symbols('S_A S_B', positive=True)
n_a, n_b = sp.symbols('n_A n_B', positive=True, integer=True)

## 2. Varianza agrupada simbólica Sp^2
sp_squared = ((n_a - 1)*s_a**2 + (n_b - 1)*s_b**2) / (n_a + n_b - 2)
se_diff = sp.sqrt(sp_squared * (1/n_a + 1/n_b))
t_stat = (mean_a - mean_b) / se_diff

display(Math(fr"\text{{Estadístico t Simbólico Agrupado: }} t = {sp.latex(t_stat)}"))

## 3. Sustitución de valores numéricos
valores = {
    mean_a: 24.5,
    mean_b: 21.2,
    s_a: 2.1,
    s_b: 1.8,
    n_a: 15,
    n_b: 15
}

t_val = float(t_stat.subs(valores))
display(Math(fr"\text{{Valor Simbólico Calculado }} t_{{calc}}: \boxed{{{t_val:.4f}}}"))
```

---

## 5. Solución Computacional en Python (SciPy & Statsmodels)

```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

## Configuración visual
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 5)

## --- PARTE A: Generación de Datos Experimentales ---
np.random.seed(101)
lote_A = stats.norm.rvs(loc=24.5, scale=2.1, size=15)
lote_B = stats.norm.rvs(loc=21.2, scale=1.8, size=15)

## --- PARTE B: Verificación de Supuestos Estadísticos ---
p_norm_a = stats.shapiro(lote_A).pvalue
p_norm_b = stats.shapiro(lote_B).pvalue
p_homo = stats.levene(lote_A, lote_B).pvalue

print("--- VERIFICACIÓN DE SUPUESTOS ESTADÍSTICOS ---")
print(f"Normalidad Shapiro-Wilk Lote A: p-valor = {p_norm_a:.4f} (OK si > 0.05)")
print(f"Normalidad Shapiro-Wilk Lote B: p-valor = {p_norm_b:.4f} (OK si > 0.05)")
print(f"Homocedasticidad Levene:        p-valor = {p_homo:.4f} (OK si > 0.05)")

## --- PARTE C: Prueba t de Student de Dos Muestras ---
t_res = stats.ttest_ind(lote_A, lote_B, equal_var=True)
print("\n--- RESULTADO DE LA PRUEBA T DE STUDENT ---")
print(f"Estadístico t_calc: {t_res.statistic:.4f}")
print(f"p-valor de dos colas: {t_res.pvalue:.6f}")

## --- PARTE D: Visualización Profesional ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

## Gráfico 1: Boxplot comparativo de diámetros
df_exp = pd.DataFrame({
    'Diámetro (nm)': np.concatenate([lote_A, lote_B]),
    'Método Síntesis': ['Sol-Gel (A)']*15 + ['Microondas (B)']*15
})

sns.boxplot(data=df_exp, x='Método Síntesis', y='Diámetro (nm)', palette='Set2', ax=axes[0])
sns.stripplot(data=df_exp, x='Método Síntesis', y='Diámetro (nm)', color='black', alpha=0.6, jitter=0.2, ax=axes[0])
axes[0].set_title("Comparación Muestral de Diámetros TiO2 por Método", fontsize=12, fontweight="bold")

## Gráfico 2: Simulación de Potencia de la Prueba mediante Monte Carlo
efectos = np.linspace(0, 5, 50)
potencias = []
N_sim = 2000

for eff in efectos:
    rechazos = 0
    for _ in range(N_sim):
        s_a_sim = np.random.normal(loc=24.5 + eff, scale=2.1, size=15)
        s_b_sim = np.random.normal(loc=24.5, scale=1.8, size=15)
        if stats.ttest_ind(s_a_sim, s_b_sim).pvalue < 0.05:
            rechazos += 1
    potencias.append(rechazos / N_sim)

axes[1].plot(efectos, potencias, color='purple', lw=2.5, label='Curva de Potencia Simulada (1-β)')
axes[1].axhline(y=0.80, color='red', linestyle='--', label='Potencia Objetivo (80%)')
axes[1].set_title("Curva de Potencia Operativa de la Prueba (Monte Carlo)", fontsize=12, fontweight="bold")
axes[1].set_xlabel("Diferencia de Medias Real (nm)")
axes[1].set_ylabel("Potencia (1 - β)")
axes[1].legend()

plt.tight_layout()
plt.show()
```

---

## 6. Interpretación Post-Gráfico & Diccionario de Variables

### 6.1 Interpretación de Resultados Computacionales
1. **Validación de Supuestos**: Las pruebas de Shapiro-Wilk en ambos lotes confirmaron la normalidad ($p > 0.05$) y la prueba de Levene confirmó la homogeneidad de varianzas ($p > 0.05$), justificando el uso de la prueba $t$ de Student agrupada.
2. **Conclusión Técnica Nanotecnológica**: Dado que $p < 0.0001 < 0.05$, rechazamos $H_0$. El método de síntesis por microondas produce nanopartículas significativamente más pequeñas y de mayor superficie específica que el método sol-gel convencional.

### 6.2 Diccionario de Variables Nanotecnológicas
* $\mu_A, \mu_B$: Medias poblacionales de diámetro de cristalito de $\text{TiO}_2$ ($\text{nm}$).
* $S_p$: Desviación estándar agrupada (pooled standard deviation).
* $t_{calc}$: Estadístico $t$ de Student empírico.
* $p$-valor: Probabilidad de obtener una diferencia igual o más extrema si $H_0$ fuera cierta.
* $1-\beta$: Potencia probabilística para detectar diferencias efectivas en tamaño de partícula.

---

## 7. Regresión Lineal y Correlación

### 7.1 Fundamentos: Coeficiente de Correlación y Mínimos Cuadrados
El **coeficiente de correlación de Pearson** $\rho_{X,Y} = \text{Cov}(X,Y)/(\sigma_X\sigma_Y)$ mide la fuerza de la relación lineal entre dos variables. El **método de mínimos cuadrados** ajusta una recta $\hat y = mx + b$ minimizando la suma de residuos al cuadrado $\sum_i (y_i - \hat y_i)^2$; la calidad del ajuste se resume en el **coeficiente de determinación** $R^2$.

### 7.2 Ejemplo Aplicado: Curva de Calibración UV-Vis de Nanopartículas de Oro
La Ley de Beer-Lambert ($A = \epsilon \cdot b \cdot c$) relaciona la absorbancia $A$ medida por espectroscopía UV-Vis con la concentración $c$ de nanopartículas de oro coloidales en suspensión, a través de la absortividad molar $\epsilon$ y la longitud de paso óptico $b$.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

## Simulación de datos de calibración (Ley de Beer-Lambert)
np.random.seed(42)
epsilon = 5000  # Absortividad molar (M^-1 cm^-1)
b_optico = 1.0  # Longitud de paso óptico (cm)
concentraciones = np.linspace(0.0001, 0.001, 10)  # Molar
absorbancia_ideal = epsilon * b_optico * concentraciones
ruido = np.random.normal(0, 0.02, size=len(concentraciones))
absorbancia_medida = absorbancia_ideal + ruido

## Regresión lineal
resultado = linregress(concentraciones, absorbancia_medida)
print(f"Pendiente (m = epsilon*b): {resultado.slope:.2f}")
print(f"Intercepto: {resultado.intercept:.4f}")
print(f"Coeficiente de correlación r: {resultado.rvalue:.4f}")
print(f"R^2: {resultado.rvalue**2:.4f}")
print(f"p-valor: {resultado.pvalue:.6f}")

## Visualización
plt.figure(figsize=(8, 5))
plt.scatter(concentraciones, absorbancia_medida, label="Datos medidos")
plt.plot(concentraciones, resultado.slope*concentraciones + resultado.intercept, color="red", label=f"Ajuste ($R^2$={resultado.rvalue**2:.3f})")
plt.xlabel("Concentración (M)")
plt.ylabel("Absorbancia")
plt.title("Curva de Calibración UV-Vis: Nanopartículas de Oro")
plt.legend()
plt.tight_layout()
plt.show()
```

---

## 8. Módulo Integrador: Inferencia con Datos de Materials Project API

En el Proyecto Integrador, el estudiante puede consultar la API de Materials Project para formular y contrastar hipótesis sobre propiedades semiconductoras reales.

### 8.1 Comparación de Band Gap entre Óxidos Semiconductores (Prueba t de Dos Muestras)

```python
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, Math

## 1. Extracción de sub-muestras por material desde Materials Project (simulado)
np.random.seed(55)
bg_tio2 = stats.norm.rvs(loc=3.20, scale=0.12, size=35)
bg_zno = stats.norm.rvs(loc=3.37, scale=0.18, size=35)

## 2. Verificación de Supuestos de Inferencia
shapiro_tio2 = stats.shapiro(bg_tio2)
shapiro_zno = stats.shapiro(bg_zno)
levene_test = stats.levene(bg_tio2, bg_zno)

display(Math(fr"\text{{Shapiro-Wilk TiO2: }} p = {shapiro_tio2.pvalue:.4f}"))
display(Math(fr"\text{{Shapiro-Wilk ZnO: }} p = {shapiro_zno.pvalue:.4f}"))
display(Math(fr"\text{{Homocedasticidad (Levene): }} p = {levene_test.pvalue:.4f}"))

## 3. Prueba de Hipótesis de Dos Muestras: H0: mu_TiO2 = mu_ZnO vs H1: mu_TiO2 != mu_ZnO
t_stat, p_val = stats.ttest_ind(bg_tio2, bg_zno, equal_var=True)

display(Math(fr"\text{{Estadístico t calculado: }} t = {t_stat:.4f}"))
display(Math(fr"\text{{p-valor exacto: }} p = {p_val:.6f}"))

if p_val < 0.05:
    display(Math(r"\text{Decisión: Rechazar } H_0 \implies \text{Existe diferencia estadísticamente significativa en } E_g"))
else:
    display(Math(r"\text{Decisión: No rechazar } H_0"))
```

---

## 9. Aplicación Avanzada: Red Neuronal Probabilística para Control de Calidad

A diferencia de una red neuronal estándar que predice un único valor puntual, una **red neuronal probabilística** predice los parámetros de una distribución (típicamente media $\mu$ y escala $\sigma$), permitiendo cuantificar la incertidumbre de la predicción — relevante cuando se requiere no solo estimar una propiedad de un lote de nanopartículas, sino también la confianza de esa estimación.

### 9.1 Arquitectura Conceptual
La red recibe como entrada variables de proceso (p. ej. temperatura de síntesis, concentración de precursor) y produce dos salidas: $\hat\mu(x)$ y $\hat\sigma(x)$, que parametrizan una distribución Normal $\mathcal{N}(\hat\mu(x), \hat\sigma(x)^2)$ sobre la propiedad objetivo (p. ej. diámetro de nanopartícula). El entrenamiento minimiza la log-verosimilitud negativa de los datos observados bajo esa distribución predicha, en vez del error cuadrático medio de una red estándar.

### 9.2 Aplicación: Control de Calidad de Nanopartículas
Una vez entrenado el modelo con datos históricos de producción, se usa para calcular probabilidades sobre nuevos lotes:

```python
import numpy as np
from scipy.stats import norm

## Ejemplo conceptual: el modelo entrenado predice mu y sigma para un lote
## dado un vector de condiciones de proceso X_nuevo (simulado como si viniera del modelo)
mu_predicho = 1.397   # nm, predicho por la red para las condiciones dadas
sigma_predicho = 0.193  # nm, incertidumbre predicha para esas condiciones

## Probabilidad de que el diámetro esté por encima del umbral mínimo de especificación (1.0 nm)
prob_sobre_umbral = 1 - norm.cdf(1.0, loc=mu_predicho, scale=sigma_predicho)
print(f"P(diámetro > 1.0 nm) = {prob_sobre_umbral:.4f} ({prob_sobre_umbral*100:.2f}%)")
```

### 9.3 Interpretación en el Contexto de Nanotecnología
Si el criterio de control de calidad exige que el diámetro esté en un rango específico, no basta con mirar la media predicha: la desviación estándar predicha indica qué tan confiable es esa estimación para el lote en cuestión — una desviación alta sugiere que, aunque la media esté dentro de especificación, una porción significativa de las nanopartículas del lote podría estar fuera de rango debido a la variabilidad del proceso de síntesis.

---

## 10. Módulo de Simulación: Simulación Estocástica de Potencia y Tamaño Muestral

### 10.1 Algoritmo de Simulación de Potencia
1. Fijar el tamaño de efecto esperado $\Delta = \mu_A - \mu_B$.
2. Simular $N$ pares de muestras normales bajo $H_1$.
3. Estimar la potencia como la fracción de simulaciones con $p$-valor $< \alpha$.

### 10.2 Curva de Potencia Simulada en Python
```python
import numpy as np
import scipy.stats as stats

np.random.seed(42)
n_sim = 10_000
p_vals = [stats.ttest_ind(np.random.normal(24.5, 2.1, 15), np.random.normal(21.2, 1.8, 15)).pvalue for _ in range(n_sim)]
potencia_est = np.mean(np.array(p_vals) < 0.05)

print(f"Potencia Empírica Simulada de la Prueba: {potencia_est * 100:.2f}%")
```
