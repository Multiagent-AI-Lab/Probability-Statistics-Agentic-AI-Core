# UNIDAD 5: Variables Aleatorias Continuas y Distribuciones de Probabilidad

**Duración:** 2 semanas (12 horas)

**Curso:** Probabilidad y Estadística Inferencial

**Institución:** Universidad de la Ciénega del Estado de Michoacán de Ocampo (UCEMICH)

**Profesor:** Luis José Yudico Anaya

**Carrera:** Ingeniería en Nanotecnología

**Nivel:** Tercer Semestre

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Multiagent-AI-Lab/Probability-Statistics-Agentic-AI-Core/blob/master/notebooks/UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.ipynb)

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

Una **Variable Aleatoria Continua (VAC)** es una función $X: \Omega \rightarrow \mathbb{R}$ cuyo rango de valores posibles $R_X$ es un intervalo continuo no numerable de números reales (por ejemplo, el tiempo de vida de un nanotransistor, la conductividad eléctrica de un nanotubo de carbono o el diámetro de una partícula coloidal).

### 1.1 Función de Densidad de Probabilidad (PDF) y Propiedades
A diferencia de las variables discretas, para una VAC la probabilidad puntual en cualquier valor exacto es cero ($P(X = x) = 0$). La probabilidad se define sobre intervalos a través de la **Función de Densidad de Probabilidad (PDF)** $f_X(x)$, la cual satisface los dos axiomas universales:

1. **No Negatividad**: $f_X(x) \ge 0$ para todo $x \in \mathbb{R}$.
2. **Normalización del Área**:
   $$\int_{-\infty}^{+\infty} f_X(x) dx = 1$$

La probabilidad de que $X$ caiga dentro del intervalo $[a, b]$ es el área bajo la curva de la PDF:
$$P(a \le X \le b) = \int_a^b f_X(x) dx$$

### 1.2 Función de Distribución Acumulada (CDF)
La **Función de Distribución Acumulada (CDF)** $F_X(x)$ acumula la densidad desde $-\infty$ hasta $x$:

$$F_X(x) = P(X \le x) = \int_{-\infty}^x f_X(t) dt$$

Por el Teorema Fundamental del Cálculo, si $f_X(x)$ es continua:
$$f_X(x) = \frac{d}{dx} F_X(x)$$

### 1.3 Valor Esperado, Varianza y Momentos Continuos
* **Valor Esperado (Media)**:
  $$\mathbb{E}[X] = \mu = \int_{-\infty}^{+\infty} x \cdot f_X(x) dx$$
* **Varianza**:
  $$\text{Var}(X) = \sigma^2 = \int_{-\infty}^{+\infty} (x - \mu)^2 f_X(x) dx = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$$

---

## 2. Familias Principales de Distribuciones Continuas

### 2.1 Distribución Uniforme Continua ($X \sim \text{Uniforme}(a, b)$)
Densidad constante en el intervalo $[a, b]$.
* PDF: $f(x) = \frac{1}{b-a}$ para $x \in [a, b]$.
* Esperanza: $\mathbb{E}[X] = \frac{a+b}{2}$, Varianza: $\text{Var}(X) = \frac{(b-a)^2}{12}$.

### 2.2 Distribución Normal o Gaussiana ($X \sim \mathcal{N}(\mu, \sigma^2)$)
La distribución más importante en ciencias e ingeniería por el Teorema del Límite Central.
* PDF:
  $$f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{1}{2} \left(\frac{x - \mu}{\sigma}\right)^2 \right), \quad x \in \mathbb{R}$$
* Estándar $\mathcal{N}(0, 1)$ mediante la transformación $Z = \frac{X - \mu}{\sigma}$.

### 2.3 Distribución Exponencial ($X \sim \text{Exponencial}(\lambda)$)
Modela el tiempo continuo entre eventos estocásticos Poisson independientes.
* PDF: $f(x) = \lambda e^{-\lambda x}$ para $x \ge 0$.
* CDF: $F(x) = 1 - e^{-\lambda x}$.
* Esperanza: $\mathbb{E}[X] = \frac{1}{\lambda}$, Varianza: $\text{Var}(X) = \frac{1}{\lambda^2}$.
* Propiedad de **Falta de Memoria**: $P(X > s + t | X > s) = P(X > t)$.

### 2.4 Distribución Gamma ($X \sim \text{Gamma}(k, \theta)$)
Generalización de la distribución exponencial para el tiempo hasta observar $k$ eventos.
* PDF: $f(x) = \frac{x^{k-1} e^{-x/\theta}}{\theta^k \Gamma(k)}$ para $x > 0$.

### 2.5 Distribución de Weibull ($X \sim \text{Weibull}(k, \lambda)$)
Ampliamente utilizada en ingeniería de materiales y confiabilidad para describir el tiempo de falla y resistencia a la rotura.
* PDF: $f(x) = \frac{k}{\lambda} \left(\frac{x}{\lambda}\right)^{k-1} \exp\left(-\left(\frac{x}{\lambda}\right)^k\right)$ para $x \ge 0$.

### 2.6 Distribución Chi-cuadrada ($X \sim \chi^2_k$)
Distribución de la suma de $k$ variables normales estándar independientes al cuadrado; fundamental en pruebas de hipótesis sobre varianzas.
* PDF: $f(x) = \dfrac{1}{2^{k/2}\Gamma(k/2)} x^{(k/2)-1} e^{-x/2}$ para $x \ge 0$.
* Esperanza: $\mathbb{E}[X] = k$, Desviación estándar: $\sigma = \sqrt{2k}$.
* **Aplicación en nanotecnología**: al caracterizar el diámetro de nanopartículas producidas por síntesis coloidal (por ejemplo, nanopartículas de oro o puntos cuánticos de CdSe), la variabilidad del proceso de fabricación se evalúa comparando la varianza muestral del diámetro medido por microscopía electrónica contra una varianza de referencia del protocolo de síntesis; el estadístico resultante sigue una distribución Chi-cuadrada bajo el supuesto de normalidad del diámetro de las nanopartículas.

### 2.7 Distribución t-Student ($X \sim t_\nu$)
Modela la media de una muestra pequeña cuando la varianza poblacional es desconocida; base del t-test.
* PDF: $f(x) = \dfrac{\Gamma\left(\frac{\nu+1}{2}\right)}{\sqrt{\nu\pi}\,\Gamma\left(\frac{\nu}{2}\right)} \left(1+\dfrac{x^2}{\nu}\right)^{-\frac{\nu+1}{2}}$.
* Esperanza: $\mathbb{E}[X] = 0$ (para $\nu>1$), Desviación estándar: $\sigma = \sqrt{\nu/(\nu-2)}$ (para $\nu>2$).
* **Aplicación en nanotecnología**: al estimar la conductividad térmica media de un lote pequeño (n < 30) de muestras de nanotubos de carbono sintetizados por deposición química de vapor, la varianza poblacional real es desconocida, por lo que la distribución t-Student modela la incertidumbre de la media muestral en lugar de la Normal estándar.

### 2.8 Distribución F (Fisher-Snedecor) ($X \sim F_{d_1,d_2}$)
Modela el cociente de dos varianzas muestrales independientes; base de la comparación de varianzas entre grupos y de la prueba de igualdad de varianzas, tema que se retoma formalmente en unidades posteriores de inferencia.
* PDF: $f(x) = \dfrac{\left(d_1/d_2\right)^{d_1/2}\, x^{d_1/2-1}}{\left(1+\frac{d_1}{d_2}x\right)^{(d_1+d_2)/2}\, B(d_1/2,\,d_2/2)}$ para $x \ge 0$.
* Esperanza: $\mathbb{E}[X] = \dfrac{d_1}{d_1-2}$ (para $d_1>2$).
* **Aplicación en nanotecnología**: al comparar la dispersión del diámetro de nanopartículas obtenidas por dos rutas de síntesis distintas (por ejemplo, síntesis sol-gel frente a síntesis hidrotermal para nanomateriales cerámicos), el cociente de las varianzas muestrales del diámetro sigue una distribución F, lo que permite evaluar si un método de síntesis produce partículas más homogéneas que el otro.

### 2.9 Distribución Log-Normal ($X \sim \text{LogNormal}(\mu, \sigma^2)$)
Modela variables positivas cuyo logaritmo sigue una distribución normal; útil para tamaños de partícula y variables con sesgo a la derecha.
* PDF: $f(x) = \dfrac{1}{x\sigma\sqrt{2\pi}} \exp\left(-\dfrac{(\ln x - \mu)^2}{2\sigma^2}\right)$ para $x > 0$.
* Esperanza: $\mathbb{E}[X] = e^{\mu + \sigma^2/2}$.
* **Aplicación en nanotecnología**: la distribución de tamaño de nanopartículas obtenidas por síntesis en fase líquida (nucleación y crecimiento) suele presentar un sesgo marcado a la derecha, con muchas partículas pequeñas y una cola de partículas de mayor diámetro; el diámetro de estas nanopartículas se modela con frecuencia como una variable Log-Normal en lugar de Normal.

### 2.10 Distribución Beta ($X \sim \text{Beta}(\alpha, \beta)$)
Modela variables continuas acotadas en $[0,1]$, como proporciones o probabilidades.
* PDF: $f(x) = \dfrac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}$ para $0<x<1$.
* Esperanza: $\mathbb{E}[X] = \dfrac{\alpha}{\alpha+\beta}$.
* **Aplicación en nanotecnología**: la fracción de recubrimiento superficial de un nanomaterial funcionalizado (por ejemplo, el porcentaje de sitios activos de un nanotubo cubiertos por un ligando durante la síntesis) es una proporción acotada entre 0 y 1, y se modela naturalmente con una distribución Beta cuyos parámetros $\alpha$ y $\beta$ se ajustan a partir de mediciones experimentales del proceso de síntesis.

### 2.11 Distribución de Dirichlet ($\mathbf{X} \sim \text{Dirichlet}(\boldsymbol{\alpha})$)
Generalización multivariada de la distribución Beta: modela vectores de proporciones que suman 1 (un símplex), como las fracciones de composición de una aleación o mezcla de nanomateriales.
* PDF: $f(x_1,\dots,x_k) = \dfrac{1}{B(\boldsymbol{\alpha})} \prod_{i=1}^k x_i^{\alpha_i - 1}$, con $\sum_i x_i = 1$.
* Esperanza por componente: $\mathbb{E}[X_i] = \alpha_i / \sum_j \alpha_j$.
* **Aplicación en nanotecnología**: en la síntesis de nanomateriales compuestos (por ejemplo, una aleación nanoparticulada de Au-Ag-Pt), las fracciones molares de cada elemento constituyente suman siempre 1; la distribución Dirichlet modela la incertidumbre conjunta de estas proporciones de composición generadas por variabilidad del proceso de síntesis, generalizando el caso univariado de la distribución Beta a $k$ componentes de la aleación de nanomateriales.

### 2.12 Profundización: PDF Completa, CDF y Aplicaciones por Dominio

Las subsecciones 2.1 a 2.11 dan la definición mínima de cada familia. Esta subsección profundiza tres de las distribuciones más usadas en el curso — Normal, Weibull y Chi-cuadrada — con su CDF explícita, código de comparación gráfica en `scipy.stats`, y ejemplos de uso concretos en **Nanotecnología**, **Inteligencia Artificial** y **Diseño de Experimentos (DOE)**, más allá del PDF y una sola aplicación ya vistos arriba.

#### 2.12.1 Distribución Normal — Profundización

* **CDF**: $F(x) = \Phi\left(\dfrac{x-\mu}{\sigma}\right)$, donde $\Phi$ es la CDF de la Normal estándar $\mathcal{N}(0,1)$ — no tiene forma cerrada y se evalúa numéricamente (`scipy.stats.norm.cdf`).
* **Regla empírica 68-95-99.7%**: $P(\mu-\sigma < X < \mu+\sigma) \approx 0.6826$, $P(\mu-2\sigma < X < \mu+2\sigma) \approx 0.9544$, $P(\mu-3\sigma < X < \mu+3\sigma) \approx 0.9974$ — se usa para fijar límites de control estadístico de procesos (SPC) sin necesitar la CDF exacta.
* **Estandarización**: si $X \sim \mathcal{N}(\mu, \sigma^2)$, entonces $a + bX \sim \mathcal{N}(a+b\mu,\, b^2\sigma^2)$; en particular $Z = (X-\mu)/\sigma \sim \mathcal{N}(0,1)$, lo que permite calcular cualquier probabilidad de $X$ a partir de la tabla o CDF de $Z$.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

## Comparación de PDFs Normales: variabilidad del diámetro de puntos cuánticos
## de CdSe sintetizados con 3 protocolos distintos (misma media, distinta sigma)
x = np.linspace(-6, 6, 400)
parametros = [(-2, 1.0), (0, 1.0), (2, 1.5)]

plt.figure(figsize=(9, 5))
for mu, sigma in parametros:
    plt.plot(x, norm.pdf(x, loc=mu, scale=sigma), label=f"$\\mu={mu}$, $\\sigma={sigma}$")
plt.title("PDF Normal: efecto de $\\mu$ (desplazamiento) y $\\sigma$ (dispersión)")
plt.xlabel("x")
plt.ylabel("Densidad")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

**Aplicaciones — Nanotecnología**: (1) *Distribución de tamaño de nanopartículas*: el diámetro medio ($\mu$) y su dispersión ($\sigma$) de un lote de puntos cuánticos o nanopartículas de oro se modelan como Normal; una $\sigma$ pequeña (lote monodisperso) es crítica en nanomedicina y en *displays* QLED. (2) *Variabilidad en nanodispositivos*: variaciones en el grosor de la capa aislante de un nanotransistor por imprecisiones de litografía, usadas para fijar tolerancias de fabricación. (3) *Ruido instrumental*: mediciones repetidas de espesor de película delgada por AFM, donde se asume error de medición Normal para construir intervalos de confianza.

**Aplicaciones — Inteligencia Artificial**: (1) *Inicialización de pesos*: las redes neuronales inicializan pesos muestreando de $\mathcal{N}(0, \sigma^2)$ pequeña (inicialización de Xavier/He) para evitar gradientes que exploten o se desvanezcan. (2) *Naive Bayes Gaussiano*: asume que cada característica numérica, condicionada a la clase, sigue una Normal. (3) *Modelos de Mezclas Gaussianas (GMM)* y el espacio latente de autoencoders variacionales (VAE), modelado como Normal multivariada.

**Aplicaciones — DOE**: (1) *Análisis de varianza entre tratamientos* (tema formal de unidades posteriores de inferencia): la validez de las pruebas $t$ y $F$ subyacentes depende de que los residuos del modelo sean aproximadamente Normales (verificado con Shapiro-Wilk). (2) *Intervalos de confianza y pruebas $t$/$Z$*: el Teorema del Límite Central permite usar la Normal para la media muestral aunque la población no sea perfectamente Normal, si $n$ es grande. (3) *Control estadístico de procesos (SPC)*: gráficos de control $\bar{X}$ y $R$ con límites $\mu \pm 3\sigma$ para detectar procesos fuera de control.

#### 2.12.2 Distribución de Weibull — Profundización

* **CDF**: $F(x) = 1 - e^{-(x/\lambda)^k}$ para $x \ge 0$.
* **Interpretación del parámetro de forma $k$**: $k<1$ indica tasa de falla decreciente ("mortalidad infantil", defectos de fabricación); $k=1$ recupera la distribución Exponencial (tasa de falla constante); $k>1$ indica tasa de falla creciente (desgaste, fatiga, envejecimiento) — las tres fases de la curva de la bañera de confiabilidad.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

## Comparación de PDFs Weibull: tres regímenes de falla de un recubrimiento
## protector de nanopartículas de sílice (mismo lambda, distinto k)
x = np.linspace(0, 3, 300)
k_valores = [0.5, 1, 2]

plt.figure(figsize=(9, 5))
for k in k_valores:
    plt.plot(x, weibull_min.pdf(x, c=k, scale=1), label=f"k={k}")
plt.title("PDF Weibull: régimen de falla según el parámetro de forma k")
plt.xlabel("Tiempo hasta falla (unidades normalizadas)")
plt.ylabel("Densidad")
plt.legend(title="Forma (k)")
plt.grid(alpha=0.3)
plt.show()
```

**Aplicaciones — Nanotecnología / Ciencia de Materiales**: (1) *Resistencia a la fractura de materiales frágiles*: la falla de cerámicas ($\text{SiC}$, $\text{Al}_2\text{O}_3$) o fibras de carbono está gobernada por el defecto crítico más débil en el volumen sometido a tensión ("teoría del eslabón más débil"); un módulo de Weibull $k$ alto ($k>10$) indica defectos uniformes y alta calidad. (2) *Efecto de escala (size effect)*: predice que un componente de mayor volumen es estadísticamente más débil, al tener mayor probabilidad de contener un defecto crítico. (3) *Fallos en nano-dispositivos* ($k<1$, defectos de fabricación en un chip o capa delgada) vs. *fatiga en recubrimientos* ($k>1$, degradación acumulada).

**Aplicaciones — Confiabilidad / Vida Útil**: (1) *Predicción de vida a fatiga*: relación entre número de ciclos de tensión y probabilidad de falla, esencial en diseño aeronáutico y automotriz. (2) *Cualificación de materiales compuestos*: comparar la vida característica ($\eta$) de distintas aleaciones bajo condiciones extremas. (3) *Modelado de corrosión*: tiempo hasta que el espesor residual no corroído es insuficiente.

**Aplicaciones — DOE**: al diseñar un experimento de vida acelerada (temperatura, humedad, voltaje) para caracterizar la confiabilidad de un nanomaterial, se ajusta un modelo Weibull a los tiempos de falla observados en cada condición para extrapolar la vida útil en condiciones normales de operación.

#### 2.12.3 Distribución Chi-cuadrada — Profundización

* **CDF**: no tiene forma cerrada; se evalúa numéricamente (`scipy.stats.chi2.cdf`).
* **Forma según $k$**: para $k=1$ la distribución está fuertemente sesgada a la derecha; a medida que $k$ aumenta, se vuelve más simétrica y se aproxima a una Normal (consecuencia del Teorema del Límite Central sobre la suma de $k$ cuadrados).

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

## Comparación de PDFs Chi-cuadrada: bondad de ajuste de un modelo de
## vida util (Weibull/Log-Normal) a datos de fallo de nanomateriales
x = np.linspace(0, 30, 500)
k_valores = [1, 2, 5, 10]

plt.figure(figsize=(9, 5))
for k in k_valores:
    plt.plot(x, chi2.pdf(x, df=k), label=f"k={k}")
plt.title("PDF Chi-cuadrada: convergencia a la Normal al aumentar los grados de libertad")
plt.xlabel("x")
plt.ylabel("Densidad")
plt.legend(title="Grados de libertad (k)")
plt.grid(alpha=0.3)
plt.show()
```

**Aplicaciones — Ciencia de Materiales**: (1) *Bondad de ajuste de distribuciones de vida útil*: la prueba de Chi-cuadrada compara frecuencias de fallo observadas contra las esperadas bajo un modelo teórico (Weibull, Log-Normal); un $\chi^2$ bajo indica buen ajuste. (2) *Análisis de dispersión en mediciones*: construir intervalos de confianza para la varianza poblacional de una propiedad del material (resistencia, dureza, espesor), donde una varianza excesiva señala falta de homogeneidad en el proceso de fabricación. (3) *Ajuste por mínimos cuadrados ponderados*: técnicas como reflectividad de rayos X (XRR) o elipsometría reportan un $\chi^2$ reducido como métrica de bondad de ajuste — cercano a 1 indica ajuste excelente.

**Aplicaciones — DOE**: (1) *Independencia de factores experimentales*: la prueba $\chi^2$ de independencia sobre una tabla de contingencia evalúa si un factor categórico (p. ej., tipo de catalizador) es independiente del resultado (éxito/fallo). (2) *Comparación de varianzas entre tratamientos*: pruebas de homocedasticidad (Bartlett, Levene) que fundamentan la validez de un análisis de varianza posterior entre tratamientos, tema formal de unidades de inferencia. (3) *Diseños factoriales con datos categóricos*: analizar si los efectos de interacción entre factores son significativos cuando la respuesta es binaria o nominal.

#### 2.12.4 Distribución Uniforme Continua — Profundización

* **CDF**: $F(x) = 0$ si $x<a$; $F(x) = \dfrac{x-a}{b-a}$ si $a\le x<b$; $F(x)=1$ si $x\ge b$.
* La densidad constante hace de la Uniforme la distribución "sin memoria estructural": ningún subintervalo de igual longitud es más probable que otro, lo que la vuelve el generador base de todo método de simulación Monte Carlo (transformada inversa, ver §10 de Modelado y Simulación).

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

## PDF de la Uniforme(0,1): base de la generacion de numeros pseudoaleatorios
## para simulacion Monte Carlo de procesos de sintesis de nanomateriales
x = np.linspace(-0.2, 1.2, 300)
plt.figure(figsize=(8, 5))
plt.plot(x, uniform.pdf(x, loc=0, scale=1), color="blue", linewidth=2)
plt.title("PDF de la Distribución Uniforme(0,1)")
plt.xlabel("x")
plt.ylabel("Densidad")
plt.grid(alpha=0.3)
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: modelar el error de cuantificación al redondear una medición digital de espesor de película delgada, o el tiempo de espera de un proceso de deposición programado en un intervalo fijo sin preferencia temporal. (2) *IA*: generación de números pseudoaleatorios base para simulación Monte Carlo — toda otra distribución (Normal, Exponencial, Weibull) se obtiene transformando muestras Uniformes vía el método de la transformada inversa. (3) *DOE*: modelar parámetros de calidad de un proceso de fabricación (p. ej., el grosor de una pieza) cuando solo se conocen los límites mínimo y máximo, sin evidencia de que los valores centrales sean más probables.

#### 2.12.5 Distribución Exponencial — Profundización

* **CDF**: $F(x) = 1-e^{-\lambda x}$ para $x\ge 0$.
* **Propiedad de falta de memoria**: es la única distribución continua con $P(X>s+t \mid X>s) = P(X>t)$ — la probabilidad de esperar $t$ unidades más no depende de cuánto se ha esperado ya.
* **Conexión Poisson-Exponencial**: si los eventos de un proceso ocurren según Poisson con tasa $\lambda$, el tiempo entre eventos consecutivos sigue Exponencial($\lambda$).

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

## PDF Exponencial: tiempo hasta el primer defecto detectado en una
## linea de fabricacion de nanocables, para 3 tasas de defectos distintas
x = np.linspace(0, 5, 300)
lambdas = [0.5, 1.0, 1.5]

plt.figure(figsize=(9, 5))
for lam in lambdas:
    plt.plot(x, expon.pdf(x, scale=1/lam), label=f"$\\lambda={lam}$")
plt.title("PDF Exponencial para distintas tasas $\\lambda$")
plt.xlabel("Tiempo hasta el evento")
plt.ylabel("Densidad")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: tiempo de vida útil del componente más simple en teoría de confiabilidad (caso límite $k=1$ de Weibull); tiempo entre fallos consecutivos de un nano-dispositivo bajo tasa de falla constante. (2) *IA*: tiempos entre llegadas en colas de procesamiento (p. ej., tiempo entre solicitudes a un servidor de inferencia), modelado clásico en teoría de colas. (3) *DOE*: modelar el tiempo hasta el primer defecto detectado en una línea de producción bajo tasa de defectos constante, para diseñar la frecuencia óptima de inspección.

#### 2.12.6 Distribución Gamma — Profundización

* **CDF**: $F(x) = \int_0^x f(t)\,dt$, sin forma cerrada; se evalúa numéricamente (`scipy.stats.gamma.cdf`).
* **Interpretación**: generaliza la Exponencial al tiempo hasta el $k$-ésimo evento de un proceso Poisson — si $k$ etapas exponenciales independientes de la misma tasa se sostienen en secuencia, su suma sigue Gamma($k$, $\theta$). Para $k=1$ recupera la Exponencial.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

## PDF Gamma: tiempo total de un proceso de crecimiento de nanocristales
## en multiples etapas de nucleacion y crecimiento (k etapas, misma escala)
x = np.linspace(0, 20, 300)
formas = [(2, 1), (5, 1)]

plt.figure(figsize=(9, 5))
for k, theta in formas:
    plt.plot(x, gamma.pdf(x, a=k, scale=theta), label=f"k={k}, $\\theta$={theta}")
plt.title("PDF Gamma: efecto del parámetro de forma k")
plt.xlabel("x")
plt.ylabel("Densidad")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: tiempo total de crecimiento de un nanocristal cuando el proceso involucra $k$ etapas secuenciales (nucleación, crecimiento capa por capa); acumulación de daño por radiación en un semiconductor hasta alcanzar un umbral de falla, donde $k$ representa el número de "golpes" necesarios. (2) *Ciencia de Materiales*: rugosidad superficial en deposición de películas delgadas, resultado de la acumulación de muchos depósitos aleatorios individuales. (3) *DOE*: modelar el tiempo de espera total de una muestra a través de $k$ estaciones de trabajo secuenciales con tiempos de procesamiento exponenciales, para optimizar el flujo de una línea de caracterización.

#### 2.12.7 Distribución t-Student — Profundización

* **CDF**: sin forma cerrada; se evalúa numéricamente (`scipy.stats.t.cdf`).
* **Interpretación de $\nu$**: para $\nu$ pequeño la distribución tiene colas más pesadas que la Normal (mayor probabilidad de valores extremos, reflejando la incertidumbre extra de estimar $\sigma$ con pocos datos); a medida que $\nu\to\infty$ converge a la Normal estándar.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, norm

## PDF t-Student: colas mas pesadas que la Normal cuando el tamano de
## muestra (grados de libertad) es pequeno
x = np.linspace(-5, 5, 400)
grados_libertad = [1, 2, 5, 10]

plt.figure(figsize=(9, 5))
for nu in grados_libertad:
    plt.plot(x, t.pdf(x, df=nu), label=f"$\\nu={nu}$")
plt.plot(x, norm.pdf(x), "k--", label="Normal(0,1)")
plt.title("PDF t-Student: convergencia a la Normal al aumentar los grados de libertad")
plt.xlabel("x")
plt.ylabel("Densidad")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: estimar la media de una propiedad medida en un lote pequeño ($n<30$) de nanomateriales (p. ej., conductividad térmica de nanotubos de carbono) cuando la varianza poblacional real es desconocida — situación habitual en caracterización experimental de bajo volumen. (2) *DOE*: construir intervalos de confianza para la media de una variable de proceso cuando solo se dispone de una muestra piloto pequeña, antes de escalar el experimento. (3) *Ciencia de Materiales*: comparar la media de dos lotes pequeños de un mismo material sintetizado por rutas distintas, fundamento de la prueba $t$ de dos muestras.

#### 2.12.8 Distribución F (Fisher-Snedecor) — Profundización

* **CDF**: sin forma cerrada; se evalúa numéricamente (`scipy.stats.f.cdf`).
* **Definición como cociente**: $F = \dfrac{\chi^2_{d_1}/d_1}{\chi^2_{d_2}/d_2}$ — el cociente de dos varianzas muestrales independientes normalizadas por sus grados de libertad. Si dos poblaciones tienen la misma varianza, $F$ debería estar cerca de 1.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f

## PDF F: comparacion de la dispersion del diametro de nanoparticulas
## obtenidas por 2 rutas de sintesis distintas (sol-gel vs hidrotermal)
x = np.linspace(0.01, 5, 400)
pares_gl = [(2, 5), (5, 2), (10, 5)]

plt.figure(figsize=(9, 5))
for d1, d2 in pares_gl:
    plt.plot(x, f.pdf(x, dfn=d1, dfd=d2), label=f"$d_1={d1}$, $d_2={d2}$")
plt.title("PDF F: sensibilidad a los grados de libertad del numerador y denominador")
plt.xlabel("x")
plt.ylabel("Densidad")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología / Ciencia de Materiales*: comparar la dispersión del diámetro de nanopartículas obtenidas por dos rutas de síntesis (sol-gel vs. hidrotermal) mediante el cociente de varianzas muestrales. (2) *DOE*: base estadística de las pruebas de igualdad de varianzas entre tratamientos y de la evaluación de bondad de ajuste en modelos de regresión, temas formales de unidades de inferencia. (3) *Confiabilidad*: verificar el supuesto de homocedasticidad entre lotes de producción antes de aplicar pruebas de comparación de medias.

#### 2.12.9 Distribución Log-Normal — Profundización

* **CDF**: $F(x) = \Phi\left(\dfrac{\ln x - \mu}{\sigma}\right)$ para $x>0$, donde $\Phi$ es la CDF Normal estándar.
* **Origen multiplicativo**: si $X = e^Y$ con $Y\sim\mathcal{N}(\mu,\sigma^2)$, entonces $X$ es Log-Normal — modela variables que resultan de la *multiplicación* de muchos factores aleatorios independientes (crecimiento multiplicativo), a diferencia de la Normal que modela una *suma* de factores.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

## PDF Log-Normal: distribucion del diametro de nanoparticulas obtenidas
## por nucleacion y crecimiento en fase liquida (proceso multiplicativo)
x = np.linspace(0.01, 10, 400)
parametros = [(0, 0.5), (1, 1.0)]

plt.figure(figsize=(9, 5))
for mu, sigma in parametros:
    plt.plot(x, lognorm.pdf(x, s=sigma, scale=np.exp(mu)), label=f"$\\mu={mu}$, $\\sigma={sigma}$")
plt.title("PDF Log-Normal: sesgo a la derecha por origen multiplicativo")
plt.xlabel("x")
plt.ylabel("Densidad")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: modelo estándar para el diámetro de nanopartículas obtenidas por nucleación y crecimiento (metálicas, óxidos, poliméricas), y para tamaño de grano en materiales policristalinos. (2) *Confiabilidad*: tiempo de vida de recubrimientos o películas delgadas sujetos a degradación multiplicativa (crecimiento de grietas por fatiga), donde la tasa de falla aumenta con el tiempo. (3) *IA*: variables de latencia o tiempo de respuesta en sistemas computacionales, positivas y sesgadas a la derecha — se recomienda transformación logarítmica antes de aplicar métodos que asumen normalidad.

#### 2.12.10 Distribución Beta — Profundización

* **CDF**: $F(x) = \int_0^x f(t)\,dt$, sin forma cerrada; se evalúa numéricamente (`scipy.stats.beta.cdf`).
* **Interpretación de $\alpha,\beta$**: si $\alpha>\beta$ la densidad se concentra cerca de 1 (sesgo a la derecha); si $\alpha<\beta$ se concentra cerca de 0 (sesgo a la izquierda); $\alpha=\beta=1$ recupera la Uniforme(0,1).

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

## PDF Beta: rendimiento (yield) de funcionalizacion exitosa de
## nanotubos de carbono en dos lotes de sintesis con calidad distinta
x = np.linspace(0, 1, 300)
parametros = [(2, 5), (5, 2)]

plt.figure(figsize=(9, 5))
for a, b in parametros:
    plt.plot(x, beta.pdf(x, a=a, b=b), label=f"$\\alpha={a}$, $\\beta={b}$")
plt.title("PDF Beta: sesgo segun la relación entre alpha y beta")
plt.xlabel("Proporción (0 a 1)")
plt.ylabel("Densidad")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: rendimiento (yield) de funcionalización exitosa de nanotubos o nanocables en un lote de síntesis; pureza de un material tras un proceso de purificación, ambos naturalmente acotados en $[0,1]$. (2) *IA*: distribución conjugada a priori de la Binomial en inferencia bayesiana — usada en A/B testing (comparar tasas de conversión de dos algoritmos) y en el algoritmo Thompson Sampling para problemas de bandido multi-brazo. (3) *DOE*: modelar la incertidumbre sobre la fracción de área efectiva de poro en un filtro nanoporoso, tratando la porosidad como una probabilidad en vez de un valor fijo.

#### 2.12.11 Distribución de Dirichlet — Profundización

* **Interpretación geométrica**: genera vectores en el símplex $k$-dimensional (todas las combinaciones de $k$ proporciones no negativas que suman 1); es la generalización multivariada exacta de la Beta ($k=2$ recupera la Beta).
* **Muestreo vía Gamma**: para simular $\mathbf{X}\sim\text{Dirichlet}(\boldsymbol{\alpha})$, se generan $k$ variables Gamma independientes $Y_i\sim\text{Gamma}(\alpha_i,1)$ y se normalizan: $X_i = Y_i/\sum_j Y_j$.

```python
import numpy as np
import matplotlib.pyplot as plt

## Simulacion Dirichlet (via Gamma) de la composicion molar de una
## aleacion nanoparticulada Au-Ag-Pt (k=3 componentes), dos regimenes
np.random.seed(7)
alphas = [(1, 1, 1), (5, 1, 1)]

fig, axes = plt.subplots(1, 2, figsize=(11, 5))
for ax, alpha in zip(axes, alphas):
    gamma_samples = np.column_stack([
        np.random.gamma(shape=a, scale=1, size=800) for a in alpha
    ])
    dirichlet_samples = gamma_samples / gamma_samples.sum(axis=1, keepdims=True)
    ax.scatter(dirichlet_samples[:, 0], dirichlet_samples[:, 1], alpha=0.4, s=10)
    ax.set_title(f"Dirichlet($\\alpha$={alpha})")
    ax.set_xlabel("$x_1$ (fracción Au)")
    ax.set_ylabel("$x_2$ (fracción Ag)")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
plt.tight_layout()
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: composición molar de una aleación nanoparticulada de $k$ elementos (p. ej., Au-Ag-Pt), donde las fracciones deben sumar 1 exactamente. (2) *IA*: distribución a priori conjugada de la Multinomial — corazón del modelo *Latent Dirichlet Allocation* (LDA) para modelado de temas en procesamiento de lenguaje natural, y de modelos de mezclas para *clustering* no paramétrico. (3) *DOE*: generación de datos sintéticos de proporciones (p. ej., composición de una mezcla de reactivos) que deben respetar la restricción de suma igual a 1.

---

## 3. Ejemplo Analítico Paso a Paso: Espesor de Películas Delgadas en Litografía Nanométrica

### 3.1 Contexto Aplicado en Nanotecnología
En la fabricación de transistores de efecto de campo de grafeno (GFETs), el espesor de la capa dieléctrica de dióxido de hafnio ($\text{HfO}_2$) depositada por capa atómica (ALD) sigue una distribución Normal con media $\mu = 8.5\text{ nm}$ y desviación estándar $\sigma = 0.4\text{ nm}$.

Para asegurar un rendimiento dieléctrico adecuado sin riesgo de tunelamiento cuántico indebido, el espesor debe estar comprendido entre $7.9\text{ nm}$ y $9.1\text{ nm}$.

Determine:
1. La probabilidad de que una oblea de silicio procesada tenga un espesor dentro del rango de tolerancia especificado.
2. El cota de espesor $x_{0.95}$ correspondiente al percentil $95\%$ de la producción.

### 3.2 Paso 1: Estandarización a la Variable Normal Estándar $Z$
$$Z = \frac{X - \mu}{\sigma} = \frac{X - 8.5}{0.4}$$

Para el límite inferior $x_1 = 7.9\text{ nm}$:
$$z_1 = \frac{7.9 - 8.5}{0.4} = \frac{-0.6}{0.4} = -1.50$$

Para el límite superior $x_2 = 9.1\text{ nm}$:
$$z_2 = \frac{9.1 - 8.5}{0.4} = \frac{0.6}{0.4} = +1.50$$

### 3.3 Paso 2: Cálculo de Probabilidad $P(7.9 \le X \le 9.1)$
$$P(7.9 \le X \le 9.1) = P(-1.50 \le Z \le +1.50) = \Phi(1.50) - \Phi(-1.50)$$

Consultando la CDF normal estándar $\Phi(1.50) \approx 0.93319$:
$$\Phi(-1.50) = 1 - \Phi(1.50) \approx 1 - 0.93319 = 0.06681$$
$$P(7.9 \le X \le 9.1) = 0.93319 - 0.06681 = \boxed{0.86638 \quad (86.64\%)}$$

### 3.4 Paso 3: Cálculo del Percentil $95\%$ ($x_{0.95}$)
Buscamos $z_{0.95}$ tal que $\Phi(z_{0.95}) = 0.95 \implies z_{0.95} \approx 1.64485$.
Desestandarizando:
$$\boxed{x_{0.95} = \mu + z_{0.95} \cdot \sigma = 8.5 + (1.64485 \times 0.4) = 8.5 + 0.65794 = 9.1579\text{ nm}}$$

### 3.5 Prueba Unitaria con pytest

En vez de consultar tablas de la Normal estándar (con el redondeo que eso implica), se verifican los dos resultados directamente contra `scipy.stats.norm`, que evalúa $\Phi$ con precisión de punto flotante completa:

```python
import ipytest
import pytest
from scipy.stats import norm

ipytest.autoconfig()

mu, sigma = 8.5, 0.4


def test_probabilidad_de_espesor_dentro_de_tolerancia():
    prob = norm.cdf(9.1, mu, sigma) - norm.cdf(7.9, mu, sigma)
    assert prob == pytest.approx(0.86638, rel=1e-4)


def test_percentil_95_de_la_produccion():
    x_95 = norm.ppf(0.95, mu, sigma)
    assert x_95 == pytest.approx(9.1579, rel=1e-4)


ipytest.run("-vv")
```

---

## 4. Código de Verificación Simbólica (SymPy)

```python
import sympy as sp
from IPython.display import display, Math

## 1. Definición de símbolos
x = sp.Symbol('x', real=True)
mu = sp.Symbol('mu', real=True)
sigma = sp.Symbol('sigma', positive=True)

## 2. Expresión simbólica de la PDF Normal
pdf_normal = (1 / (sigma * sp.sqrt(2 * sp.pi))) * sp.exp(-((x - mu)**2) / (2 * sigma**2))

display(Math(fr"\text{{PDF Normal Simbólica: }} f(x) = {sp.latex(pdf_normal)}"))

## 3. Integración simbólica para calcular la probabilidad del rango [7.9, 9.1]
prob_integrada = sp.integrate(pdf_normal.subs({mu: 8.5, sigma: 0.4}), (x, 7.9, 9.1))
prob_float = float(prob_integrada.evalf())

display(Math(fr"\text{{Probabilidad Integrada }} P(7.9 \le X \le 9.1): \boxed{{{prob_float:.5f}}}"))
```

---

## 5. Solución Computacional en Python (SciPy & Statsmodels)

```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

## Configuración gráfica
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 5)

## --- PARTE A: Evaluación de la Distribución Normal ---
mu_val = 8.5
sigma_val = 0.4

prob_rango = stats.norm.cdf(9.1, loc=mu_val, scale=sigma_val) - stats.norm.cdf(7.9, loc=mu_val, scale=sigma_val)
percentil_95 = stats.norm.ppf(0.95, loc=mu_val, scale=sigma_val)

print("--- EVALUACIÓN EN SCI PY STATS (NORMAL) ---")
print(f"P(7.9 <= X <= 9.1):           {prob_rango:.5f}")
print(f"Percentil 95% (Espesor):      {percentil_95:.4f} nm")

## --- PARTE B: Visualización Profesional de la Densidad ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

## Gráfico 1: PDF de Espesor HfO2 con región sombreada de tolerancia
x_axis = np.linspace(7.0, 10.0, 500)
pdf_vals = stats.norm.pdf(x_axis, loc=mu_val, scale=sigma_val)

axes[0].plot(x_axis, pdf_vals, color='navy', lw=2.5, label='PDF Normal (μ=8.5, σ=0.4)')
x_fill = np.linspace(7.9, 9.1, 200)
axes[0].fill_between(x_fill, stats.norm.pdf(x_fill, loc=mu_val, scale=sigma_val), color='lightgreen', alpha=0.6, label='Tolerancia (86.64%)')
axes[0].axvline(x=mu_val, color='red', linestyle='--', label='Media μ = 8.5 nm')
axes[0].set_title("Distribución de Espesor en Litografía HfO2", fontsize=12, fontweight="bold")
axes[0].set_xlabel("Espesor de Capa (nm)")
axes[0].set_ylabel("Densidad de Probabilidad f(x)")
axes[0].legend()

## Gráfico 2: Comparación de Densidades Continuas (Normal vs Exponencial vs Weibull)
exp_samples = stats.expon.rvs(scale=8.5, size=50_000, random_state=42)
weib_samples = stats.weibull_min.rvs(c=2.5, scale=8.5, size=50_000, random_state=42)

sns.kdeplot(exp_samples, color='crimson', lw=2, label='Exponencial (λ=1/8.5)', ax=axes[1])
sns.kdeplot(weib_samples, color='darkorange', lw=2, label='Weibull (k=2.5, λ=8.5)', ax=axes[1])
axes[1].set_title("Comparación de Modelos Continuos en Confiabilidad", fontsize=12, fontweight="bold")
axes[1].set_xlabel("Valor de la Variable Continuada")
axes[1].set_ylabel("Densidad de Kernel (KDE)")
axes[1].set_xlim(0, 25)
axes[1].legend()

plt.tight_layout()
plt.show()

## --- PARTE C: Distribuciones Muestrales (prerequisito de Inferencia — Chi-cuadrada, t-Student, F) ---
from scipy.stats import chi2, t, f

## Chi-cuadrada: valor critico para intervalo de confianza de varianza (df=5, alpha=0.025 cola superior)
k_gl = 5
x_chi2 = chi2.ppf(0.975, df=k_gl)
print(f"Valor crítico Chi-cuadrada (df={k_gl}, 0.975): {x_chi2:.4f}")

## t-Student: valor critico para IC de la media (nu=10, alpha=0.05 dos colas)
nu = 10
x_t = t.ppf(0.975, df=nu)
print(f"Valor crítico t-Student (df={nu}, 0.975): {x_t:.4f}")

## F: valor critico para prueba de igualdad de varianzas (d1=5, d2=10, alpha=0.025)
d1, d2 = 5, 10
x_f = f.ppf(0.975, dfn=d1, dfd=d2)
print(f"Valor crítico F (d1={d1}, d2={d2}, 0.975): {x_f:.4f}")

## Visualización de las 3 distribuciones
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
x_range = np.linspace(0.01, 20, 300)
axes[0].plot(x_range, chi2.pdf(x_range, df=k_gl))
axes[0].set_title(f"Chi-cuadrada (df={k_gl})")
x_range_t = np.linspace(-4, 4, 300)
axes[1].plot(x_range_t, t.pdf(x_range_t, df=nu))
axes[1].set_title(f"t-Student (df={nu})")
axes[2].plot(x_range, f.pdf(x_range, dfn=d1, dfd=d2))
axes[2].set_title(f"F (d1={d1}, d2={d2})")
plt.tight_layout()
plt.show()

## --- PARTE D: Distribución de Dirichlet (composición de aleaciones de nanomateriales) ---
from scipy.stats import dirichlet

## Fracciones molares esperadas de una aleación nanoparticulada Au-Ag-Pt (k=3 componentes)
alpha_composicion = [2.0, 5.0, 3.0]

## PDF evaluada en un punto del simplex (las 3 fracciones deben sumar 1)
x_composicion = np.array([0.2, 0.5, 0.3])
pdf_dirichlet = dirichlet.pdf(x_composicion, alpha_composicion)
print(f"PDF Dirichlet en x={x_composicion.tolist()}: {pdf_dirichlet:.4f}")

## Media esperada por componente: alpha_i / suma(alpha)
media_dirichlet = dirichlet.mean(alpha_composicion)
print(f"Fracción molar media esperada (Au, Ag, Pt): {media_dirichlet}")

## Simulación de 5 lotes de síntesis con variabilidad en la composición
muestras_dirichlet = dirichlet.rvs(alpha_composicion, size=5, random_state=42)
print("Composiciones simuladas de 5 lotes de síntesis:")
print(muestras_dirichlet)
```

---

## 6. Interpretación Post-Gráfico & Diccionario de Variables

### 6.1 Interpretación de Resultados Computacionales
1. **Conformidad de Proceso Litográfico**: El $86.64\%$ del lote de obleas cumple con la especificación de tolerancia ($7.9 - 9.1\text{ nm}$). El percentil $95\%$ se ubica en $9.1579\text{ nm}$, indicando que menos del $5\%$ de la producción supera esa cota máxima de espesor.
2. **Modelado de Fallas**: El gráfico comparativo resalta las diferencias entre distribuciones continuas: la Exponencial posee una tasa de falla constante (falta de memoria), mientras que la Weibull con $k=2.5$ caracteriza el envejecimiento por fatiga de materiales nanotecnológicos.

### 6.2 Diccionario de Variables Nanotecnológicas
* $X$: Espesor continuo de la capa dieléctrica $\text{HfO}_2$ ($\text{nm}$).
* $\mu$: Espesor medio poblacional ($\mu = 8.5\text{ nm}$).
* $\sigma$: Desviación estándar de deposición por capa atómica ($\sigma = 0.4\text{ nm}$).
* $Z$: Variable aleatoria normal estándar estandarizada $Z \sim \mathcal{N}(0, 1)$.
* $\Phi(z)$: Función de distribución acumulada de la normal estándar.

---

## 7. Referencia Avanzada (Opcional)

Este curso (tercer semestre) trata a las variables aleatorias continuas con herramientas de cálculo elemental. Para quien desee profundizar hacia un tratamiento formal medida-teórico (integración abstracta, funciones características, distribuciones normales multivariadas), el curso de posgrado **MIT 6.436J — Fundamentals of Probability** (Prof. Yury Polyanskiy) cubre este mismo tema en sus *Lecture Notes* 10–15, con los prerrequisitos de análisis real y teoría de la medida que ese enfoque exige: [ocw.mit.edu/courses/6-436j-fundamentals-of-probability-fall-2018/pages/lecture-notes](https://ocw.mit.edu/courses/6-436j-fundamentals-of-probability-fall-2018/pages/lecture-notes/).

## Errores Comunes / Misconceptions

* **Error**: Interpretar la densidad $f(x)$ como si fuera directamente una probabilidad, o calcular $P(X = x)$ para una variable continua como si fuera distinto de cero.
  **Correcto**: en variables continuas, $P(X = x) = 0$ para cualquier valor puntual $x$ — la probabilidad se obtiene integrando la densidad sobre un intervalo: $P(a \le X \le b) = \int_a^b f(x)\,dx$. $f(x)$ puede incluso superar 1 (no es una probabilidad, es una densidad).

* **Error**: Aplicar la propiedad de "falta de memoria" ($P(X > s+t \mid X > s) = P(X > t)$) a distribuciones continuas en general.
  **Correcto**: entre las distribuciones continuas, esa propiedad es exclusiva de la Exponencial (y, en el caso discreto, de la Geométrica). Aplicarla a una Normal, Gamma o Weibull con forma $k \ne 1$ produce resultados incorrectos.

* **Error**: Confundir el parámetro de tasa $\lambda$ de la distribución Exponencial con su media.
  **Correcto**: si $X \sim \text{Exponencial}(\lambda)$, entonces $\mathbb{E}[X] = 1/\lambda$, no $\lambda$. Un $\lambda$ grande (tasa alta de ocurrencia) corresponde a una media *pequeña* (tiempos de espera cortos), relación inversa que se olvida con frecuencia.

## Ejercicio Propuesto

Un proceso de recubrimiento por deposición de capas atómicas (ALD) produce películas de $\text{Al}_2\text{O}_3$ cuyo espesor $X$ (en nm) sigue $X \sim \mathcal{N}(\mu=15.0,\ \sigma=0.8)$.

1. Calcula $P(14.0 \le X \le 16.0)$, la probabilidad de que el espesor esté dentro de la ventana de tolerancia del proceso.
2. Calcula el percentil 90 del espesor (el valor $x$ tal que $P(X \le x) = 0.90$).
3. Calcula $P(X > 17.0)$, la probabilidad de un espesor excesivo. Explica por qué esta probabilidad puntual de la PDF evaluada en $x=17$ (es decir, $f(17)$) no sería la respuesta correcta a esta pregunta.

Escribe tu solución en una celda de código nueva en tu notebook. La celda de autoevaluación de la siguiente sección verificará tu resultado.

## Referencias

* Unpingco, J. (2019). *Python for Probability, Statistics, and Machine Learning* (2nd ed.). Springer. Capítulos sobre variables aleatorias continuas, distribuciones y su implementación con SciPy.
* Virtanen, P. et al. (2020). SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. *Nature Methods*, 17, 261-272. Documentación: [docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html)

## Herramientas de esta Unidad

**StatsTutorAgent** — resuelve tus dudas conceptuales sobre variables aleatorias continuas citando el contenido exacto de esta unidad, y te hace una pregunta socrática si detecta un error conceptual común en vez de darte la respuesta directa:

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
            "⚠️ [Unidad 5] No se encontró el secreto GEMINI_API_KEY ni GOOGLE_API_KEY en Colab. "
            "Créalo en el ícono de llave 🔑 de la barra lateral izquierda para usar StatsTutorAgent."
        )

from src.multiagent_core.stats_tutor_agent import StatsTutorAgent

tutor = StatsTutorAgent(course_dir=Path("lecciones"))
print(tutor.ask("¿qué papel juega la función de densidad de probabilidad en una variable continua?"))
```

No requiere configuración adicional más allá de tu `GEMINI_API_KEY` (créala en [aistudio.google.com/apikey](https://aistudio.google.com/apikey) y agrégala como secreto de Colab o variable de entorno local).

## Autoevaluación

Guarda tu solución al Ejercicio Propuesto en un archivo separado y evalúala contra el pipeline de auditoría del curso:

```python
%%writefile solucion_ejercicio_u5.py
# Completa aquí tu solución al Ejercicio Propuesto de esta unidad.
import scipy.stats as stats

mu = 15.0
sigma = 0.8

# TODO: calcula P(14.0 <= X <= 16.0), la probabilidad de que el espesor esté dentro
#       de la ventana de tolerancia del proceso (usa stats.norm.cdf)
# TODO: calcula el percentil 90 del espesor (usa stats.norm.ppf)
# TODO: calcula P(X > 17.0), la probabilidad de un espesor excesivo, y explica en un
#       comentario por qué f(17) (la PDF evaluada en 17) no sería la respuesta correcta
```

```python
from src.multiagent_core.code_auditor_agent import CodeAuditorAgent
from external_skills.pedagogy.socratic_debugger import SocraticDebugger

with open("solucion_ejercicio_u5.py", encoding="utf-8") as f:
    codigo_alumno = f.read()

auditor = CodeAuditorAgent()
resultado = auditor.audit_code(codigo_alumno)

if resultado["issues"] or resultado["metrics"]["has_security_risk"]:
    debugger = SocraticDebugger()
    for issue in resultado["issues"]:
        tipo_error = "syntax_error" if "SyntaxError" in issue else "generic"
        print("💡", debugger.generate_socratic_question(tipo_error, "Unidad 5"))
    for issue in resultado["security_issues"]:
        print("🔒", debugger.generate_socratic_question("security_risk", "Unidad 5"))
        print("   ", issue)
    print("\n--- Detalle técnico ---")
    print(resultado)
else:
    print("✅ Tu código pasa las verificaciones automáticas de estilo y seguridad.")
    print(resultado)
```
