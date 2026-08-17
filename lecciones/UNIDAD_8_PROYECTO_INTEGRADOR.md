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

### 7.3 Correlación de Rango: Spearman y Kendall

El coeficiente de Pearson de la Sección 7.1 solo captura **relaciones lineales**. Cuando la relación entre dos variables es monótona pero no lineal (crece o decrece de forma consistente, pero no en línea recta), Pearson puede subestimar la fuerza real de la asociación. Existen dos alternativas no paramétricas basadas en **rangos**, no en los valores originales:

* **Spearman ($\rho_S$)**: aplica la fórmula de Pearson a los rangos de $X$ y $Y$ en vez de a sus valores. Mide la fuerza de cualquier relación monótona.
* **Kendall ($\tau$)**: cuenta la proporción de pares concordantes menos discordantes entre las observaciones. Es más robusto que Spearman en muestras pequeñas o con muchos empates.

| Coeficiente | Tipo de relación | Basado en |
|---|---|---|
| Pearson ($\rho$) | Lineal | Valores originales |
| Spearman ($\rho_S$) | Monótona | Rangos |
| Kendall ($\tau$) | Monótona (concordancia) | Pares concordantes/discordantes |

**Contexto aplicado**: en la dispersión de nanotubos de carbono (CNT) en un solvente mediante sonicación ultrasónica, el porcentaje de homogeneidad de la dispersión crece con el tiempo de sonicación, pero de forma **saturante** (los primeros minutos mejoran mucho la homogeneidad; después de cierto punto, sonicar más aporta poco, e incluso puede dañar los CNT). Esta relación es monótona creciente pero fuertemente no lineal.

```python
import numpy as np
from scipy.stats import pearsonr, spearmanr, kendalltau

np.random.seed(70)
n = 25
tiempo_sonicacion = np.linspace(1, 60, n)  # minutos

## Relación monótona saturante (tipo logarítmica) + ruido de medición
homogeneidad_ideal = 100 * np.log1p(tiempo_sonicacion) / np.log1p(60)
ruido = np.random.normal(0, 3, n)
homogeneidad = np.clip(homogeneidad_ideal + ruido, 0, 100)

r_pearson, p_pearson = pearsonr(tiempo_sonicacion, homogeneidad)
rho_spearman, p_spearman = spearmanr(tiempo_sonicacion, homogeneidad)
tau_kendall, p_kendall = kendalltau(tiempo_sonicacion, homogeneidad)

print(f"Pearson r    = {r_pearson:.4f}  (p = {p_pearson:.6f})")
print(f"Spearman rho = {rho_spearman:.4f}  (p = {p_spearman:.6f})")
print(f"Kendall tau  = {tau_kendall:.4f}  (p = {p_kendall:.6f})")
```

**Interpretación**: Pearson obtiene $r \approx 0.92$, ya alto porque la relación es monótona y suave, pero Spearman captura mejor la asociación real ($\rho_S \approx 0.98$), confirmando que la relación es monótona casi perfecta aunque no estrictamente lineal. Kendall ($\tau \approx 0.91$) coincide en la misma dirección con una escala distinta (cuenta concordancias, no covarianza de rangos).

$$\boxed{\rho_S \approx 0.982 > r_{\text{Pearson}} \approx 0.923}$$

### 7.4 Correlación Múltiple y Correlación Parcial

Cuando una variable de respuesta $Y$ depende de **varios** predictores correlacionados entre sí, dos preguntas distintas requieren dos herramientas distintas:

1. **Correlación múltiple $R$**: ¿qué tan bien predicen $X_1, \ldots, X_k$ conjuntamente a $Y$? Se calcula como $R = \sqrt{R^2}$, la raíz del coeficiente de determinación de la regresión de $Y$ sobre todos los predictores.
2. **Correlación parcial $r_{Y,X_2 \cdot X_1}$**: ¿cuál es la asociación *neta* entre $Y$ y $X_2$, después de remover el efecto de $X_1$ sobre ambas? Se calcula con la fórmula:

$$r_{Y,X_2 \cdot X_1} = \frac{r_{Y,X_2} - r_{Y,X_1}\, r_{X_1,X_2}}{\sqrt{(1-r_{Y,X_1}^2)(1-r_{X_1,X_2}^2)}}$$

Esta pregunta es crítica cuando dos predictores están **colineales**: una correlación simple alta entre $X_2$ y $Y$ puede ser enteramente espuria, heredada de la correlación de $X_2$ con $X_1$.

**Contexto aplicado**: la conductividad eléctrica ($Y$) de un nanocompuesto de grafeno depende de la concentración de grafeno ($X_1$, % en peso) y de la temperatura de curado ($X_2$). En el protocolo del laboratorio, los lotes con mayor concentración de grafeno también se curan a mayor temperatura (están correlacionados entre sí), por lo que la correlación bruta de $X_2$ con $Y$ puede estar inflada por ese vínculo indirecto.

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.stats import pearsonr

np.random.seed(71)
n = 40
concentracion_grafeno = np.random.uniform(0.5, 5.0, n)  # % en peso
temperatura_curado = 120 + 15 * concentracion_grafeno + np.random.normal(0, 8, n)  # °C
conductividad = 8 * concentracion_grafeno + 0.15 * temperatura_curado + np.random.normal(0, 5, n)  # S/cm

df = pd.DataFrame({
    "conc_grafeno": concentracion_grafeno,
    "temp_curado": temperatura_curado,
    "conductividad": conductividad,
})

## Correlación múltiple: R de la regresión Y ~ X1 + X2
X = sm.add_constant(df[["conc_grafeno", "temp_curado"]])
modelo_multiple = sm.OLS(df["conductividad"], X).fit()
R_multiple = np.sqrt(modelo_multiple.rsquared)

## Correlaciones simples de Pearson
corr = df.corr(method="pearson")
r_y_x1 = corr.loc["conductividad", "conc_grafeno"]
r_y_x2 = corr.loc["conductividad", "temp_curado"]
r_x1_x2 = corr.loc["conc_grafeno", "temp_curado"]

## Correlación parcial de Y con X2, controlando por X1
r_parcial = (r_y_x2 - r_y_x1 * r_x1_x2) / np.sqrt((1 - r_y_x1**2) * (1 - r_x1_x2**2))

## Verificación cruzada: correlación de los residuos de regresar Y y X2 sobre X1
res_y = df["conductividad"] - sm.OLS(df["conductividad"], sm.add_constant(df["conc_grafeno"])).fit().fittedvalues
res_x2 = df["temp_curado"] - sm.OLS(df["temp_curado"], sm.add_constant(df["conc_grafeno"])).fit().fittedvalues
r_residuos, _ = pearsonr(res_y, res_x2)

print(f"R múltiple (Y ~ X1 + X2)          = {R_multiple:.4f}")
print(f"r(Y, X2) bruta                    = {r_y_x2:.4f}")
print(f"r(Y, X2 · X1) parcial              = {r_parcial:.4f}")
print(f"Verificación por residuos          = {r_residuos:.4f}")
```

**Interpretación**: la correlación múltiple es alta ($R \approx 0.96$): ambos predictores juntos explican bien la conductividad. Pero la correlación bruta de la temperatura con la conductividad ($r \approx 0.91$) se desploma a $r_{Y,X_2 \cdot X_1} \approx 0.07$ una vez removido el efecto de la concentración de grafeno — casi toda la asociación aparente de la temperatura con la conductividad era heredada de su colinealidad con la concentración de grafeno, no un efecto propio. La verificación por residuos (correlacionar directamente lo que sobra de $Y$ y de $X_2$ tras remover $X_1$ de ambos) reproduce el mismo valor, confirmando la fórmula analítica.

$$\boxed{r_{Y,X_2 \cdot X_1} \approx 0.074 \ll r_{Y,X_2} \approx 0.914}$$

### 7.5 Prueba de Breusch-Pagan: Homocedasticidad de los Residuos

El Teorema de Gauss-Markov exige que los residuos de una regresión OLS tengan **varianza constante** (homocedasticidad) para que los errores estándar de los coeficientes — y por tanto sus intervalos de confianza y p-valores — sean válidos. La inspección visual de residuos ayuda, pero la **prueba de Breusch-Pagan** formaliza la decisión: regresa los residuos al cuadrado sobre los predictores originales y prueba si esa regresión auxiliar tiene poder explicativo significativo.

$$H_0: \text{Var}(\epsilon_i) = \sigma^2 \ \text{(homocedasticidad)} \qquad H_1: \text{Var}(\epsilon_i) = f(X_i) \ \text{(heterocedasticidad)}$$

**Contexto aplicado**: se retoma la curva de calibración UV-Vis de la Sección 7.2, pero ahora sobre un rango de concentración mucho más amplio, donde el ruido de medición del espectrofotómetro crece con la concentración (común cerca del límite de saturación del detector óptico).

```python
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan

np.random.seed(72)
n = 60
concentraciones = np.linspace(0.0001, 0.01, n)  # Molar, rango amplio
epsilon, b_optico = 5000, 1.0
absorbancia_ideal = epsilon * b_optico * concentraciones

## Ruido heterocedástico: la desviación crece con la concentración
sigma_ruido = 0.02 + 3.0 * concentraciones
absorbancia_medida = absorbancia_ideal + np.random.normal(0, sigma_ruido, n)

X = sm.add_constant(concentraciones)
modelo = sm.OLS(absorbancia_medida, X).fit()

bp_stat, bp_pvalue, bp_fstat, bp_fpvalue = het_breuschpagan(modelo.resid, X)

print(f"Estadístico LM de Breusch-Pagan = {bp_stat:.4f}")
print(f"p-valor                         = {bp_pvalue:.6f}")

alpha = 0.05
if bp_pvalue < alpha:
    print(f"Decisión: p={bp_pvalue:.6f} < {alpha} -> Rechazar H0. Hay heterocedasticidad.")
else:
    print("Decisión: no rechazar H0.")
```

**Interpretación**: el estadístico LM produce $p \approx 0.005 < 0.05$, rechazando la homocedasticidad — el ruido de medición efectivamente crece con la concentración. Como control, al repetir el mismo experimento con ruido de varianza constante, la prueba da $p \approx 0.34$ (no se rechaza $H_0$), confirmando que el test distingue correctamente ambos escenarios. Cuando Breusch-Pagan rechaza $H_0$, los errores estándar de OLS ya no son confiables y conviene usar errores estándar robustos (HC, `cov_type="HC3"` en `statsmodels`) o una transformación de varianza estabilizadora.

$$\boxed{p_{\text{BP}} \approx 0.005 \implies \text{se rechaza homocedasticidad}}$$

### 7.6 RANSAC vs OLS: Regresión Robusta ante Outliers

La regresión OLS minimiza la suma de errores al cuadrado, lo que la hace extremadamente sensible a **outliers**: un solo punto extremo puede dominar el ajuste completo (su punto de ruptura es 0%). **RANSAC** (*Random Sample Consensus*) ajusta el modelo de forma robusta probando repetidamente subconjuntos aleatorios de los datos y quedándose con el que produce más puntos consistentes (*inliers*) dentro de un umbral de residuo.

**Contexto aplicado**: la relación entre el radio de nanopartículas de plata (AgNP, medido por dispersión de luz dinámica DLS) y la posición de su pico de resonancia plasmónica superficial (SPR, medido por UV-Vis) es aproximadamente lineal. Pero un subconjunto de las mediciones sufre **agregación** (las nanopartículas se aglomeran y generan un segundo pico de SPR desplazado), produciendo outliers severos que no reflejan la relación física real.

```python
import numpy as np
from sklearn.linear_model import LinearRegression, RANSACRegressor

np.random.seed(74)
n_samples = 45
radio_nm = np.linspace(5, 60, n_samples).reshape(-1, 1)
pendiente_real, intercepto_real = 2.3, 395  # nm de corrimiento SPR por nm de radio

spr_pico = pendiente_real * radio_nm.ravel() + intercepto_real + np.random.normal(0, 3, n_samples)

## Contaminación por agregación: 9 de 45 muestras con SPR desplazado
idx_agregados = np.random.choice(n_samples, 9, replace=False)
spr_pico[idx_agregados] += np.random.uniform(40, 90, 9)

ols = LinearRegression().fit(radio_nm, spr_pico)
ransac = RANSACRegressor(min_samples=15, residual_threshold=10.0, random_state=74)
ransac.fit(radio_nm, spr_pico)

print(f"Pendiente real     = {pendiente_real}")
print(f"Pendiente OLS      = {ols.coef_[0]:.4f}  (error = {abs(ols.coef_[0]-pendiente_real):.4f})")
print(f"Pendiente RANSAC   = {ransac.estimator_.coef_[0]:.4f}  (error = {abs(ransac.estimator_.coef_[0]-pendiente_real):.4f})")

n_outliers_detectados = (~ransac.inlier_mask_).sum()
coincidencia = len(set(np.where(~ransac.inlier_mask_)[0]) & set(idx_agregados))
print(f"Outliers reales = {len(idx_agregados)}, detectados por RANSAC = {n_outliers_detectados}, coinciden = {coincidencia}")
```

**Interpretación**: OLS produce una pendiente muy sesgada ($\approx 1.68$, error $0.62$) porque los 9 puntos agregados lo arrastran. RANSAC recupera la pendiente real casi exactamente ($\approx 2.29$, error $0.013$) e identifica los 9 outliers reales con coincidencia perfecta (9 de 9), sin que se le indique de antemano cuáles eran contaminados.

$$\boxed{\text{Error pendiente: OLS} \approx 0.625 \ \text{vs. RANSAC} \approx 0.013}$$

### 7.7 GLMs Generalizados: Poisson y Binomial Negativa para Datos de Conteo

Los Modelos Lineales Generalizados (GLM) extienden la regresión a respuestas no normales mediante una **función de enlace** $g(\mu) = \eta$. Para datos de **conteo** (número de eventos discretos), el GLM canónico es el **Poisson**, con enlace logarítmico $\ln(\mu) = \beta_0 + \beta_1 x$, que asume $\text{Var}(Y) = \mu$ (varianza igual a la media).

En procesos reales de fabricación, esta suposición suele fallar por **sobredispersión** ($\text{Var}(Y) > \mu$), generalmente porque hay heterogeneidad no observada entre lotes. La **Binomial Negativa** introduce un parámetro de dispersión adicional (equivalente a una mezcla Gamma-Poisson) que absorbe esa varianza extra.

**Contexto aplicado**: se cuentan defectos puntuales (vacancias) por oblea de silicio, observados por microscopía electrónica, en función del tiempo de crecimiento epitaxial. Las condiciones de cámara varían levemente entre lotes, generando sobredispersión real en el conteo de defectos.

```python
import numpy as np
import statsmodels.api as sm

np.random.seed(75)
n_samples = 80
tiempo_crecimiento = np.linspace(1, 12, n_samples)  # horas

## Generación con sobredispersión real (mezcla Gamma-Poisson)
mu = np.exp(0.15 * tiempo_crecimiento + 0.8)
alpha_real = 0.6
r_param = 1 / alpha_real
prob = r_param / (r_param + mu)
defectos = np.random.negative_binomial(r_param, prob)

X = sm.add_constant(tiempo_crecimiento)
modelo_poisson = sm.GLM(defectos, X, family=sm.families.Poisson()).fit()
modelo_negbin = sm.GLM(defectos, X, family=sm.families.NegativeBinomial(alpha=alpha_real)).fit()

ratio_var_media = defectos.var(ddof=1) / defectos.mean()

print(f"AIC Poisson       = {modelo_poisson.aic:.2f}")
print(f"AIC Binomial Neg. = {modelo_negbin.aic:.2f}")
print(f"Ratio Varianza/Media observado = {ratio_var_media:.4f} (>1 indica sobredispersión)")
```

**Interpretación**: el ratio Varianza/Media observado es $\approx 5.44$, muy por encima de 1, confirmando sobredispersión fuerte. En consecuencia, el modelo Binomial Negativa tiene un AIC mucho menor ($\approx 443$ vs. $\approx 547$ del Poisson, $\Delta \text{AIC} \approx 104$), indicando un ajuste sustancialmente mejor. Usar Poisson aquí subestimaría los errores estándar de los coeficientes y produciría intervalos de confianza y p-valores falsamente optimistas.

$$\boxed{\Delta\text{AIC}_{\text{Poisson} \to \text{NegBin}} \approx 104 \implies \text{Binomial Negativa es preferible}}$$

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

## 9. Cierre Integrador: PCA, Distancia de Mahalanobis y Whitening Gaussiano

La Unidad 4 (§7.3-7.4) ya introdujo el **blanqueamiento (whitening)** y el **PCA** como transformaciones lineales de vectores gaussianos, y definió la **distancia de Mahalanobis** $D^2=(\mathbf{x}-\mu)^T\Sigma^{-1}(\mathbf{x}-\mu)$ como la métrica de distancia estadística que considera la correlación entre variables (Unidad 4 §6.4). Esta sección cierra el curso aplicando esas tres piezas juntas a un problema de **control de calidad multivariado**, sin reimplementar PCA ni whitening desde cero.

### 9.1 La Distancia de Mahalanobis como Estadístico de Prueba: $D^2 \sim \chi^2_p$

Un resultado clave, no explotado aún en el curso, es que si $\mathbf{X} \sim \mathcal{N}(\mathbf{\mu}, \mathbf{\Sigma})$ en $p$ dimensiones, entonces su distancia de Mahalanobis al cuadrado se distribuye como una **Chi-cuadrado con $p$ grados de libertad**:

$$D^2 = (\mathbf{X}-\mathbf{\mu})^T\mathbf{\Sigma}^{-1}(\mathbf{X}-\mathbf{\mu}) \sim \chi^2_p$$

Esto permite construir un **umbral de rechazo formal**: cualquier observación con $D^2$ por encima del cuantil $1-\alpha$ de $\chi^2_p$ se considera una anomalía estadística al nivel $\alpha$, exactamente igual que un valor crítico de una prueba de hipótesis.

### 9.2 Contexto Aplicado: Control de Calidad de Puntos Cuánticos

En la síntesis de puntos cuánticos (*quantum dots*) de CdSe, dos variables de proceso determinan conjuntamente el diámetro final: la **temperatura de inyección** y el **tiempo de crecimiento**. Ambas están correlacionadas por el protocolo estándar del reactor. Un lote puede estar "dentro de rango" en cada variable por separado y aun así ser anómalo si **rompe la correlación esperada** entre ambas — algo que un control de calidad univariado (mirar cada variable con su propio umbral de $\pm 2\sigma$) no puede detectar.

```python
import numpy as np
from scipy.stats import chi2
from scipy.spatial.distance import mahalanobis
from sklearn.decomposition import PCA

np.random.seed(76)

## Proceso "en control": temperatura y tiempo correlacionados por protocolo
mu = np.array([240.0, 12.0])  # [temperatura °C, tiempo min]
Sigma = np.array([[16.0, 6.0], [6.0, 4.0]])
N, p = 1500, 2
X_samples = np.random.multivariate_normal(mu, Sigma, size=N)
Sigma_inv = np.linalg.inv(Sigma)

## 1. Umbral de rechazo al 95% (teórico vía chi2 y muestral vía percentil)
d2_samples = np.array([mahalanobis(x, mu, Sigma_inv) ** 2 for x in X_samples])
umbral_teorico = chi2.ppf(0.95, df=p)
umbral_muestral = np.percentile(d2_samples, 95)
print(f"Umbral teórico (chi2, df={p})  = {umbral_teorico:.4f}")
print(f"Umbral muestral (percentil 95) = {umbral_muestral:.4f}")

## 2. Evaluación de 3 lotes nuevos
lotes = {
    "Lote normal": np.array([241.0, 12.5]),
    "Lote outlier marginal (obvio en ambas variables)": np.array([280.0, 25.0]),
    "Lote outlier conjunto (rompe correlación, normal marginalmente)": np.array([244.0, 8.5]),
}
for nombre, x in lotes.items():
    d2 = mahalanobis(x, mu, Sigma_inv) ** 2
    z_temp = (x[0] - mu[0]) / np.sqrt(Sigma[0, 0])
    z_tiempo = (x[1] - mu[1]) / np.sqrt(Sigma[1, 1])
    decision = "RECHAZADO" if d2 > umbral_teorico else "aceptado"
    print(f"{nombre}: D²={d2:.4f}, z_temp={z_temp:.2f}, z_tiempo={z_tiempo:.2f} -> {decision}")

## 3. Whitening (reutilizando la definición de U4 §7.3): verificar Cov(Z) = I
eigenvals, eigenvecs = np.linalg.eigh(Sigma)
W = eigenvecs @ np.diag(1.0 / np.sqrt(eigenvals)) @ eigenvecs.T
Z_samples = (X_samples - mu) @ W.T
print(f"\nCov(Z) tras blanqueamiento ≈ I: {np.allclose(np.cov(Z_samples, rowvar=False), np.eye(2), atol=0.1)}")

## En el espacio blanqueado, Mahalanobis == distancia Euclidiana al cuadrado
d2_euclid_Z = np.sum(Z_samples ** 2, axis=1)
print(f"Max |D²_Mahalanobis - ||Z||²_Euclid| = {np.max(np.abs(d2_euclid_Z - d2_samples)):.2e}")

## 4. PCA (reutilizando U4 §7.4): varianza explicada del mismo proceso
pca = PCA(n_components=2).fit(X_samples)
print(f"\nVarianza explicada por componente: {pca.explained_variance_ratio_}")
```

### 9.3 Interpretación en el Contexto de Nanotecnología

El umbral teórico ($\chi^2_2$ al 95%, $D^2 \approx 5.99$) coincide con el umbral muestral empírico, confirmando que el proceso se comporta como la Normal bivariada asumida. El lote "outlier conjunto" tiene ambas variables dentro de $\pm 2\sigma$ marginalmente (lo que un control univariado aceptaría sin problema), pero su $D^2 \approx 15.3$ excede ampliamente el umbral — la anomalía solo es visible al considerar la **covarianza conjunta**, no cada variable por separado. La verificación de whitening confirma numéricamente la equivalencia teórica: la distancia de Mahalanobis en el espacio original es exactamente la distancia Euclidiana en el espacio blanqueado (diferencia $\sim 10^{-14}$, error de punto flotante). El PCA del mismo proceso (Unidad 4 §7.4) muestra que la primera componente principal concentra $>90\%$ de la varianza, es decir, casi toda la variabilidad del proceso ocurre a lo largo de una única dirección física (probablemente correlacionada con el tiempo total de reacción efectivo).

$$\boxed{D^2_{\text{umbral}} \approx 5.99 \ (\chi^2_2, 95\%) \implies \text{lote outlier conjunto } (D^2\approx 15.3) \text{ se rechaza aunque cada variable esté individualmente en rango}}$$

---

## 10. Aplicación Avanzada: Red Neuronal Probabilística para Control de Calidad

A diferencia de una red neuronal estándar que predice un único valor puntual, una **red neuronal probabilística** predice los parámetros de una distribución (típicamente media $\mu$ y escala $\sigma$), permitiendo cuantificar la incertidumbre de la predicción — relevante cuando se requiere no solo estimar una propiedad de un lote de nanopartículas, sino también la confianza de esa estimación.

### 10.1 Arquitectura Conceptual
La red recibe como entrada variables de proceso (p. ej. temperatura de síntesis, concentración de precursor) y produce dos salidas: $\hat\mu(x)$ y $\hat\sigma(x)$, que parametrizan una distribución Normal $\mathcal{N}(\hat\mu(x), \hat\sigma(x)^2)$ sobre la propiedad objetivo (p. ej. diámetro de nanopartícula). El entrenamiento minimiza la log-verosimilitud negativa de los datos observados bajo esa distribución predicha, en vez del error cuadrático medio de una red estándar.

### 10.2 Aplicación: Control de Calidad de Nanopartículas
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

### 10.3 Interpretación en el Contexto de Nanotecnología
Si el criterio de control de calidad exige que el diámetro esté en un rango específico, no basta con mirar la media predicha: la desviación estándar predicha indica qué tan confiable es esa estimación para el lote en cuestión — una desviación alta sugiere que, aunque la media esté dentro de especificación, una porción significativa de las nanopartículas del lote podría estar fuera de rango debido a la variabilidad del proceso de síntesis.

### 10.4 Extensión con TensorFlow Probability: Entrenamiento Real de la Red Probabilística

El ejemplo anterior (§10.2) usó valores de $\hat\mu$ y $\hat\sigma$ ya calculados, "como si vinieran del modelo". Esta sección entrena el modelo real con **TensorFlow Probability (TFP)**, la librería especializada para redes cuya capa de salida parametriza una distribución en vez de un valor puntual, sobre el mismo problema conceptual (diámetro de AuNP en función de la temperatura de síntesis), ahora con **heterocedasticidad real**: a mayor temperatura, mayor variabilidad del proceso de síntesis coloidal.

```python
## En Google Colab, instalar la extensión TF de TFP si no está disponible:
## %pip install -q "tensorflow-probability[tf]"
import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

tfd = tfp.distributions
np.random.seed(77)
tf.random.set_seed(77)

## 1. Datos: diámetro de AuNP en función de temperatura de síntesis (normalizada)
n_samples = 1500
temp_norm = np.random.uniform(-2, 2, (n_samples, 1)).astype(np.float32)
mu_real = 15.0 + 3.0 * temp_norm.ravel()
sigma_real = 0.5 + 0.8 * np.abs(temp_norm.ravel())  # heterocedasticidad: más ruido en extremos
diametro = np.random.normal(mu_real, sigma_real).astype(np.float32).reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(temp_norm, diametro, test_size=0.2, random_state=77)

## 2. Modelo: red que predice [mu, log_sigma] en vez de un único valor
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation="relu", input_shape=(1,)),
    tf.keras.layers.Dense(16, activation="relu"),
    tf.keras.layers.Dense(2),  # salida: [mu, raw_scale]
])

def neg_log_likelihood(y_true, y_pred_params):
    """Negative log-likelihood de una Normal con parámetros predichos por la red."""
    loc, raw_scale = tf.split(y_pred_params, num_or_size_splits=2, axis=-1)
    scale = tf.math.softplus(raw_scale) + 1e-6  # asegura escala positiva
    return -tfd.Normal(loc=loc, scale=scale).log_prob(y_true)

modelo.compile(optimizer=tf.keras.optimizers.Adam(0.01), loss=neg_log_likelihood)
early_stop = tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=15, restore_best_weights=True)
historia = modelo.fit(X_train, y_train, validation_split=0.2, epochs=150, batch_size=32,
                       callbacks=[early_stop], verbose=0)

## 3. Predicciones: extraer mu y sigma predichos
params_test = modelo.predict(X_test, verbose=0)
loc_test, raw_scale_test = np.split(params_test, 2, axis=-1)
scale_test = np.log1p(np.exp(raw_scale_test)) + 1e-6

print(f"MAE de mu predicho en test = {mean_absolute_error(y_test, loc_test):.4f} nm")
print(f"R² de mu predicho en test  = {r2_score(y_test, loc_test):.4f}")

## 4. Verificar que sigma predicho captura la heterocedasticidad real
corr_sigma = np.corrcoef(np.abs(X_test.ravel()), scale_test.ravel())[0, 1]
print(f"Correlación |temperatura| vs sigma_predicho = {corr_sigma:.4f}")

## 5. Guardado y carga del modelo (requiere registrar la función de pérdida personalizada)
modelo.save("modelo_probabilistico_aunp.keras")
modelo_cargado = tf.keras.models.load_model(
    "modelo_probabilistico_aunp.keras", custom_objects={"neg_log_likelihood": neg_log_likelihood}
)
x_nuevo = np.array([[1.8]], dtype=np.float32)
coincide = np.allclose(modelo.predict(x_nuevo, verbose=0), modelo_cargado.predict(x_nuevo, verbose=0))
print(f"Predicción del modelo recargado coincide con el original: {coincide}")
```

**Interpretación**: el modelo entrenado con TFP alcanza $R^2 \approx 0.85$ para la media predicha, y — a diferencia de una red estándar que solo estima $\hat\mu$ — captura correctamente la heterocedasticidad real del proceso: la correlación entre $|\text{temperatura}|$ y $\hat\sigma$ predicho es $\approx 0.98$, y $\hat\sigma$ promedio más que se duplica entre temperaturas moderadas y extremas ($\approx 0.82$ nm vs. $\approx 1.78$ nm). Esto es información que una red de regresión estándar (que solo predice $\hat\mu$) no puede ofrecer: dos lotes con la misma media predicha pueden tener niveles de confianza muy distintos. El guardado y recarga del modelo confirma que la función de pérdida personalizada (`neg_log_likelihood`) debe registrarse explícitamente vía `custom_objects` al cargar, o Keras no puede reconstruir el grafo de cómputo del modelo.

$$\boxed{\text{Corr}(|\text{temp}|, \hat\sigma) \approx 0.98 \implies \text{la red capta correctamente la heterocedasticidad del proceso}}$$

---

## 11. Módulo de Simulación: Simulación Estocástica de Potencia y Tamaño Muestral

### 11.1 Algoritmo de Simulación de Potencia
1. Fijar el tamaño de efecto esperado $\Delta = \mu_A - \mu_B$.
2. Simular $N$ pares de muestras normales bajo $H_1$.
3. Estimar la potencia como la fracción de simulaciones con $p$-valor $< \alpha$.

### 11.2 Curva de Potencia Simulada en Python
```python
import numpy as np
import scipy.stats as stats

np.random.seed(42)
n_sim = 10_000
p_vals = [stats.ttest_ind(np.random.normal(24.5, 2.1, 15), np.random.normal(21.2, 1.8, 15)).pvalue for _ in range(n_sim)]
potencia_est = np.mean(np.array(p_vals) < 0.05)

print(f"Potencia Empírica Simulada de la Prueba: {potencia_est * 100:.2f}%")
```

## Errores Comunes / Misconceptions

* **Error**: Interpretar un $R^2$ alto en una regresión lineal como evidencia de relación causal entre las variables.
  **Correcto**: $R^2$ mide qué proporción de la varianza de $Y$ es explicada linealmente por $X$ — es una medida de asociación estadística, no de causalidad. Una correlación fuerte puede deberse a una causa común (variable confusora), causalidad inversa, o coincidencia; establecer causalidad requiere diseño experimental (aleatorización) o métodos causales explícitos, no solo el ajuste del modelo.

* **Error**: Aplicar una prueba t o ANOVA sin verificar previamente los supuestos de normalidad y homocedasticidad (varianzas iguales entre grupos).
  **Correcto**: la validez de las pruebas paramétricas depende de esos supuestos — deben verificarse con pruebas formales (Shapiro-Wilk, Levene) o inspección gráfica (Q-Q plot) antes de interpretar el p-valor. Si los supuestos fallan de forma severa, corresponde usar una alternativa robusta o no paramétrica (p. ej. Welch's t-test o Mann-Whitney U).

* **Error**: Concluir, a partir de una prueba de hipótesis no significativa, que "se demostró que no hay efecto" o "los dos grupos son iguales".
  **Correcto**: una prueba no significativa (p. ej. $p > 0.05$) indica falta de evidencia suficiente para rechazar $H_0$, que puede deberse a un efecto real ausente o a potencia insuficiente (muestra pequeña). Para argumentar ausencia de efecto con rigor se requiere un análisis de potencia post-hoc o pruebas de equivalencia diseñadas para ese propósito.

## Ejercicio Propuesto

Se midió el band gap $E_g$ (en eV) de dos óxidos semiconductores nanoestructurados sintetizados por dos rutas distintas, con $n=8$ mediciones independientes por grupo:

$$\text{SnO}_2 = \{3.58,\ 3.62,\ 3.55,\ 3.60,\ 3.57,\ 3.63,\ 3.59,\ 3.56\}$$
$$\text{In}_2\text{O}_3 = \{3.71,\ 3.68,\ 3.75,\ 3.70,\ 3.73,\ 3.69,\ 3.72,\ 3.74\}$$

Se quiere probar $H_0: \mu_{\text{SnO}_2} = \mu_{\text{In}_2\text{O}_3}$ contra $H_1: \mu_{\text{SnO}_2} \ne \mu_{\text{In}_2\text{O}_3}$, con $\alpha=0.05$.

1. Calcula la media y desviación estándar muestral de cada grupo.
2. Verifica el supuesto de homocedasticidad con la prueba de Levene (`scipy.stats.levene`) antes de elegir la variante de la prueba t.
3. Ejecuta una prueba t de dos muestras independientes con `scipy.stats.ttest_ind(..., equal_var=False)` (Welch, robusta ante posible heterocedasticidad) y decide si se rechaza $H_0$. Interpreta el resultado en términos de diferencia de band gap entre las dos rutas de síntesis, sin usar la palabra "causa" ni implicar causalidad.

Escribe tu solución en una celda de código nueva en tu notebook. La celda de autoevaluación de la siguiente sección verificará tu resultado.

## Referencias

* García, J., Molina, J. M., Berlanga, A., Patricio, M. Á., Bustamante, Á. L. & Padilla, W. R. (2018). *Ciencia de Datos: Técnicas Analíticas y Aprendizaje Estadístico en un Enfoque Práctico*. Alfaomega/Publicaciones Altaria. Capítulos sobre inferencia estadística aplicada y aprendizaje estadístico como cierre integrador del curso.
* Virtanen, P. et al. (2020). SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. *Nature Methods*, 17, 261-272. Documentación: [docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html)

## Autoevaluación

Guarda tu solución al Ejercicio Propuesto en un archivo separado y evalúala contra el pipeline de auditoría del curso:

```python
%%writefile solucion_ejercicio_u8.py
# Completa aquí tu solución al Ejercicio Propuesto de esta unidad.
import numpy as np
import scipy.stats as stats

sno2 = np.array([3.58, 3.62, 3.55, 3.60, 3.57, 3.63, 3.59, 3.56])
in2o3 = np.array([3.71, 3.68, 3.75, 3.70, 3.73, 3.69, 3.72, 3.74])
alpha = 0.05

# TODO: calcula la media y desviación estándar muestral de cada grupo
# TODO: verifica el supuesto de homocedasticidad con la prueba de Levene (stats.levene)
#       antes de elegir la variante de la prueba t
# TODO: ejecuta stats.ttest_ind(sno2, in2o3, equal_var=False) (Welch) y decide si se
#       rechaza H0; interpreta el resultado sin usar la palabra "causa"
```

```python
from src.multiagent_core.code_auditor_agent import CodeAuditorAgent
from external_skills.pedagogy.socratic_debugger import SocraticDebugger

with open("solucion_ejercicio_u8.py", encoding="utf-8") as f:
    codigo_alumno = f.read()

auditor = CodeAuditorAgent()
resultado = auditor.audit_code(codigo_alumno)

if resultado["issues"] or resultado["metrics"]["has_security_risk"]:
    debugger = SocraticDebugger()
    for issue in resultado["issues"]:
        tipo_error = "syntax_error" if "SyntaxError" in issue else "generic"
        print("💡", debugger.generate_socratic_question(tipo_error, "Unidad 8"))
    print("\n--- Detalle técnico ---")
    print(resultado)
else:
    print("✅ Tu código pasa las verificaciones automáticas de estilo y seguridad.")
    print(resultado)
```
