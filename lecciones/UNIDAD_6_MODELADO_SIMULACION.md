# UNIDAD 6: Modelado y Simulación Estocástica

**Duración:** 2 semanas (12 horas)

**Curso:** Probabilidad y Estadística Inferencial

**Institución:** Universidad de la Ciénega del Estado de Michoacán de Ocampo (UCEMICH)

**Profesor:** Luis José Yudico Anaya

**Carrera:** Ingeniería en Nanotecnología

**Nivel:** Tercer Semestre

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Multiagent-AI-Lab/Probability-Statistics-Agentic-AI-Core/blob/master/notebooks/UNIDAD_6_MODELADO_SIMULACION.ipynb)

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

- **Distribuciones Continuas y su CDF** (Unidad 5) — el Método de la Transformada Inversa parte directamente de invertir la CDF de la distribución continua a simular.
- **Simulación Monte Carlo** (Unidad 2) — introducida ahí como filtrado bayesiano; aquí se generaliza al modelado estocástico completo.

---

## 1. Fundamentación Teórica y Conceptos Clave de Simulación

El **Modelado y Simulación Estocástica** comprende la caracterización computacional de sistemas físicos, químicos y probabilísticos cuya complejidad analítica impide resolverlos mediante integrales explícitas o fórmulas cerradas. En el ámbito de la Nanotecnología y la Inteligencia Artificial, la simulación estocástica permite modelar el movimiento browniano de nanopartículas, la difusividad térmica en películas delgadas, los procesos de transporte cuántico en puntos cuánticos (quantum dots) y la inferencia variacional en modelos generativos.

### 1.1 Números Seudoaleatorios y Generación Uniforme
La piedra angular de toda simulación Monte Carlo es el generador de números seudoaleatorios distribuido uniformemente $U \sim \text{Uniforme}(0, 1)$. Aunque las computadoras deterministas no pueden generar aleatoriedad pura sin hardware cuántico, los **Generadores Congruenciales Lineales (LCG)** y el algoritmo **Mersenne Twister (MT19937)** producen secuencias de enteros $X_n$ mediante recurrencias del tipo:

$$X_{n+1} = (a X_n + c) \pmod m$$

Donde $a$ es el multiplicador, $c$ el incremento, $m$ el módulo y $X_0$ la semilla (seed). Al dividir $U_n = \frac{X_n}{m}$, se obtiene una aproximación computacionalmente rápida a variables continuas independientes e idénticamente distribuidas en el intervalo $(0, 1)$.

### 1.2 Métodos de Generación de Variables Aleatorias Continuas y Discretas
Para transformar variables aleatorias uniformes $U \sim \text{Uniforme}(0, 1)$ en variables con distribuciones de probabilidad arbitrarias $F(x)$, se emplean tres métodos principales:

1. **Método de la Transformada Inversa**:
   Basado en el principio de que si $X$ tiene una función de distribución acumulada (CDF) continua y estrictamente creciente $F(x)$, entonces la variable $U = F(X)$ sigue una distribución $\text{Uniforme}(0, 1)$. Por lo tanto, si $U \sim \text{Uniforme}(0, 1)$, la variable transformada:
   $$\boxed{X = F^{-1}(U)}$$
   posee exactamente la CDF $F(x)$. Este método es ideal para distribuciones con función cuantil cerrada como la Exponencial, Weibull, Uniforme y Cauchy.

2. **Método de Aceptación-Rechazo (von Neumann)**:
   Utilizado cuando la CDF inversa $F^{-1}(u)$ no posee forma analítica cerrada (p. ej., distribuciones Gamma, Beta o Normal). Sea $f(x)$ la densidad objetivo deseada y $g(x)$ una densidad propuesta accesible de la cual sabemos simular muestras, tal que existe una constante $c \ge 1$ con $f(x) \le c \cdot g(x)$ para todo $x$. El algoritmo procede así:
   - Generar $Y \sim g(y)$ y $U \sim \text{Uniforme}(0, 1)$ de forma independiente.
   - Si $U \le \frac{f(Y)}{c \cdot g(Y)}$, **aceptar** $X = Y$.
   - De lo contrario, **rechazar** $Y$ y repetir la iteración.
   La eficiencia del algoritmo es $\frac{1}{c}$, por lo que se busca minimizar la envolvente $c$.

3. **Método de Box-Muller para Variables Normales**:
   Genera pares de variables aleatorias normales estándar independientes $Z_1, Z_2 \sim \mathcal{N}(0, 1)$ a partir de dos variables uniformes $U_1, U_2 \sim \text{Uniforme}(0, 1)$ mediante transformación a coordenadas polares:
   $$Z_1 = \sqrt{-2 \ln U_1} \cos(2\pi U_2), \quad Z_2 = \sqrt{-2 \ln U_1} \sen(2\pi U_2)$$

### 1.3 Métodos de Monte Carlo e Integración Estocástica
La integración por Monte Carlo evalúa integrales definidas multidimensionales mediante la aproximación del valor esperado de un estimador estocástico. Sea la integral $\theta = \int_a^b g(x) dx$, la cual puede reescribirse como $\theta = (b-a) \mathbb{E}[g(X)]$ con $X \sim \text{Uniforme}(a, b)$. El estimador de Monte Carlo con $N$ réplicas es:

$$\hat{\theta}_N = \frac{b-a}{N} \sum_{i=1}^N g(X_i)$$

Por el Teorema del Límite Central, el error de estimación decrece con orden $\mathcal{O}(N^{-1/2})$, **independientemente de la dimensión del espacio de integración**, lo que convierte a Monte Carlo en el único método ejecutable para problemas de física estadística y aprendizaje profundo en alta dimensión.

---

## 2. Ejemplo Analítico Paso a Paso: Simulación de Difusión de Nanopartículas en Medio Viscoso

### 2.1 Contexto Aplicado en Nanotecnología
En el desarrollo de nanosistemas de liberación controlada de fármacos antitumorales (doxorrubicina encapsulada en liposomas nanométricos), se requiere evaluar el tiempo de tránsito $T$ (en segundos) que tarda una nanopartícula en atravesar la membrana endotelial microvascular. Debido a la heterogeneidad estructural del tejido tumoral, la tasa de permeación sigue una distribución de Weibull con parámetro de forma $k = 1.5$ y parámetro de escala $\lambda = 12.0\text{ segundos}$.

Para optimizar la dosis mediante simulaciones estocásticas de millones de trayectorias celulares:
1. Derivar la fórmula analítica explicita del método de la transformada inversa para la distribución de Weibull.
2. Calcular analíticamente el tiempo de tránsito $T$ correspondiente a un número aleatorio uniforme generado $U = 0.35$.
3. Estimar la media del tiempo de tránsito $\mathbb{E}[T]$ utilizando la función Gamma.

### 2.2 Paso 1: Derivación del Método de la Transformada Inversa para Weibull
La función de distribución acumulada (CDF) de la distribución de Weibull es:
$$F(t) = 1 - \exp\left(-\left(\frac{t}{\lambda}\right)^k\right), \quad t \ge 0$$

Igualando $F(t) = U$ con $U \sim \text{Uniforme}(0, 1)$:
$$1 - \exp\left(-\left(\frac{t}{\lambda}\right)^k\right) = U \implies 1 - U = \exp\left(-\left(\frac{t}{\lambda}\right)^k\right)$$

Tomando logaritmo natural en ambos lados:
$$\ln(1 - U) = -\left(\frac{t}{\lambda}\right)^k \implies -\ln(1 - U) = \left(\frac{t}{\lambda}\right)^k$$

Despejando el tiempo de tránsito $T$:
$$t = \lambda \left(-\ln(1 - U)\right)^{1/k}$$

Puesto que si $U \sim \text{Uniforme}(0, 1)$, entonces $(1 - U) \sim \text{Uniforme}(0, 1)$, la fórmula generadora simplificada es:
$$\boxed{T = \lambda \cdot (-\ln U)^{1/k}}$$

### 2.3 Paso 2: Evaluación Numérica Paso a Paso para $U = 0.35$
Sustituyendo los parámetros $\lambda = 12.0$, $k = 1.5$ y $U = 0.35$:
1. Logaritmo natural: $-\ln(0.35) \approx -(-1.049822) = 1.049822$
2. Exponente $1/k = 1/1.5 = \frac{2}{3} \approx 0.666667$
3. Potencia: $(1.049822)^{0.666667} \approx 1.03297$
4. Tiempo final $T$:
$$\boxed{T = 12.0 \times 1.03297 \approx 12.3957 \text{ segundos}}$$

### 2.4 Paso 3: Cálculo del Valor Esperado Teórico $\mathbb{E}[T]$
$$\mathbb{E}[T] = \lambda \cdot \Gamma\left(1 + \frac{1}{k}\right) = 12.0 \cdot \Gamma(1 + 0.6667) = 12.0 \cdot \Gamma(1.6667) \approx 12.0 \times 0.902746 \approx 10.833 \text{ s}$$

### 2.5 Prueba Unitaria con pytest

Antes de lanzar millones de trayectorias simuladas, se verifica la fórmula generadora de la transformada inversa contra un valor de $U$ conocido y contra la función de supervivencia de `scipy.stats.weibull_min` (deben ser funciones inversas entre sí):

```python
import ipytest
import pytest
import numpy as np
from scipy.stats import weibull_min
from scipy.special import gamma

ipytest.autoconfig()

lam, k = 12.0, 1.5


def test_transformada_inversa_para_u_conocida():
    U = 0.35
    T = lam * (-np.log(U)) ** (1 / k)
    assert T == pytest.approx(12.3953, rel=1e-4)


def test_transformada_inversa_es_consistente_con_la_funcion_de_supervivencia():
    ## La formula usa T = lambda*(-ln U)^(1/k), que invierte 1-F(t)=U (la
    ## funcion de supervivencia), no F(t)=U directamente -- por eso se
    ## contrasta contra .sf() y no contra .cdf().
    U = 0.35
    T = lam * (-np.log(U)) ** (1 / k)
    assert weibull_min.sf(T, c=k, scale=lam) == pytest.approx(U, rel=1e-6)


def test_esperanza_teorica_del_tiempo_de_transito():
    esperanza = lam * gamma(1 + 1 / k)
    assert esperanza == pytest.approx(10.833, rel=1e-3)


ipytest.run("-vv")
```

---

## 3. Código de Verificación Simbólica (SymPy)

```python
import sympy as sp
from IPython.display import display, Math

## 1. Definición de variables simbólicas
u = sp.Symbol('U', positive=True)
lam = sp.Symbol('lambda', positive=True)
k = sp.Symbol('k', positive=True)
t = sp.Symbol('t', positive=True)

## 2. Ecuación de CDF de Weibull F(t) = U
cdf_weibull = 1 - sp.exp(-(t/lam)**k)
ecuacion = sp.Eq(cdf_weibull, u)

## 3. Despeje simbólico de t (Transformada Inversa)
solucion_t = sp.solve(sp.Eq(1 - u, sp.exp(-(t/lam)**k)), t)[0]

display(Math(fr"\text{{Expresión Simbólica de la Transformada Inversa Weibull: }} T = {sp.latex(solucion_t)}"))

## 4. Sustitución de valores numéricos de la nano-difusión (lambda=12.0, k=1.5, U=0.35)
valores = {lam: 12.0, k: 1.5, u: 0.35}
t_numerico = float(solucion_t.subs(valores))

display(Math(fr"\text{{Tiempo de Tránsito Simulado para }} U=0.35: \boxed{{{t_numerico:.4f} \text{{ s}}}}"))
```

---

## 4. Solución Computacional en Python (SciPy & Statsmodels)

```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

## Configuración de estilo gráfico profesional
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 5)

## --- PARTE A: Generador por Transformada Inversa vs SciPy ---
np.random.seed(42)
N_muestras = 100_000
lam_val = 12.0
k_val = 1.5

## Generación por Método de Transformada Inversa
u_samples = np.random.uniform(0, 1, N_muestras)
t_inversa = lam_val * (-np.log(u_samples)) ** (1.0 / k_val)

## Generación nativa con SciPy (scipy.stats.weibull_min)
t_scipy = stats.weibull_min.rvs(c=k_val, scale=lam_val, size=N_muestras)

print("--- EVALUACIÓN ESTADÍSTICA DE LA SIMULACIÓN MONTE CARLO ---")
print(f"Media Transformada Inversa: {np.mean(t_inversa):.4f} s | Teórica: {lam_val * math.gamma(1 + 1/k_val):.4f} s")
print(f"Media SciPy RVS:            {np.mean(t_scipy):.4f} s")
print(f"Desviación Estándar Inversa:{np.std(t_inversa):.4f} s")

## --- PARTE B: Visualización Profesional de la Simulación ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

## Gráfico 1: Histogramas comparativos de densidad empirical vs PDF teórica
sns.histplot(t_inversa, bins=60, stat="density", color="skyblue", label="Transformada Inversa (Monte Carlo)", ax=axes[0])
x_grid = np.linspace(0, 45, 500)
pdf_teorica = stats.weibull_min.pdf(x_grid, c=k_val, scale=lam_val)
axes[0].plot(x_grid, pdf_teorica, 'r-', lw=2.5, label="PDF Teórica Weibull(k=1.5, λ=12)")
axes[0].set_title("Distribución Muestral de Tiempos de Difusión Nanotecnológica", fontsize=12, fontweight="bold")
axes[0].set_xlabel("Tiempo de Tránsito T (segundos)")
axes[0].set_ylabel("Densidad de Probabilidad")
axes[0].legend()

## Gráfico 2: Q-Q Plot de validación de calidad de la simulación
stats.probplot(t_inversa, dist=stats.weibull_min, sparams=(k_val, 0, lam_val), plot=axes[1])
axes[1].set_title("Q-Q Plot de Validación Estocástica (Weibull)", fontsize=12, fontweight="bold")
axes[1].set_xlabel("Cuantiles Teóricos")
axes[1].set_ylabel("Cuantiles Muestrales Simulados")

plt.tight_layout()
plt.show()
```

---

## 5. Interpretación Post-Gráfico & Diccionario de Variables

### 5.1 Interpretación de Resultados Computacionales
1. **Fidelidad del Generador por Transformada Inversa**: El histograma de frecuencias simuladas con $100,000$ réplicas se superpone perfectamente sobre la curva teórica de la densidad de Weibull $\text{PDF}(t)$.
2. **Validación Mediante Q-Q Plot**: La alineación lineal estricta sobre la diagonal de $45^\circ$ en el gráfico Q-Q demuestra que el generador estocástico no introduce sesgos en las colas de la distribución, garantizando la validez para estimar tiempos extremos de penetración tumoral.

### 5.2 Diccionario de Variables Nanotecnológicas
* $U$: Variable aleatoria uniforme estándar $U \sim \text{Uniforme}(0, 1)$ que actúa como semilla probabilística.
* $T$: Tiempo de tránsito estocástico de la nanopartícula a través de la membrana microvascular (segundos).
* $\lambda$: Parámetro de escala de Weibull ($\lambda = 12.0\text{ s}$), relacionado con la viscosidad del estroma tumoral.
* $k$: Parámetro de forma de Weibull ($k = 1.5$), que caracteriza la heterogeneidad de los poros endoteliales.
* $\mathbb{E}[T]$: Valor esperado teórico del tiempo de permeación coloidal.

---

## 6. Módulo de Simulación: Método de la Transformada Inversa y Aceptación-Rechazo

### 6.1 Algoritmo General de la Transformada Inversa
Dada una variable aleatoria continua $X$ con CDF $F(x)$:
1. Generar $U \sim \text{Uniforme}(0, 1)$.
2. Calcular $X = F^{-1}(U)$.

### 6.2 Simulación de la Distribución de Weibull para Resistencia de Fibras de Carbono

Encapsulamos el algoritmo general de §6.1 en una función reutilizable — cualquier distribución cuya CDF inversa $F^{-1}(u)$ tenga forma cerrada puede simularse llamándola con la función correspondiente:

```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


def simular_transformada_inversa(cdf_inversa, n_muestras, semilla):
    """Aplica el algoritmo general de la Transformada Inversa (§6.1):
    genera U ~ Uniforme(0,1) y devuelve X = cdf_inversa(U)."""
    np.random.seed(semilla)
    u_vals = np.random.uniform(0, 1, n_muestras)
    return cdf_inversa(u_vals)


## CDF inversa de Weibull(k=2.2, lambda=15.0): F^{-1}(u) = lambda * (-ln(u))^(1/k)
cdf_inversa_weibull = lambda u: 15.0 * (-np.log(u)) ** (1.0 / 2.2)

resistencia_fibras = simular_transformada_inversa(
    cdf_inversa_weibull, n_muestras=50_000, semilla=42
)

print(f"Resistencia Promedio Simulada de Fibras de Carbono: {np.mean(resistencia_fibras):.3f} MPa")
```

## Errores Comunes / Misconceptions

* **Error**: Asumir que aumentar el número de iteraciones Monte Carlo siempre mejora la precisión proporcionalmente, sin considerar el costo computacional.
  **Correcto**: el error estándar de una estimación Monte Carlo converge como $O(1/\sqrt{N})$, no linealmente — para reducir el error a la mitad se necesitan aproximadamente 4 veces más simulaciones. Duplicar $N$ solo reduce el error en un factor de $\approx 1.41$.

* **Error**: Confundir el muestreo con reemplazo (usado en bootstrap) con el muestreo sin reemplazo.
  **Correcto**: el bootstrap no paramétrico remuestrea *con reemplazo* de la muestra original (algunos datos pueden repetirse, otros quedar fuera de una réplica dada) precisamente para poder estimar la variabilidad del estadístico; muestrear sin reemplazo del mismo tamaño simplemente reproduce la muestra original sin aportar información nueva.

* **Error**: Tratar los números generados por `numpy.random` (o cualquier generador pseudoaleatorio) como verdaderamente aleatorios e impredecibles.
  **Correcto**: son deterministas — dado el mismo `seed`, la secuencia completa se reproduce exactamente. Esto es una ventaja para la reproducibilidad de experimentos computacionales, pero implica que no son adecuados para aplicaciones criptográficas que requieren aleatoriedad genuina.

## Ejercicio Propuesto

El tiempo hasta la primera falla de un nanosensor de gas basado en óxido de grafeno sigue una distribución Exponencial con tasa $\lambda = 0.05$ fallas/hora ($X \sim \text{Exponencial}(\lambda = 0.05)$).

1. Deriva simbólicamente (con SymPy) la función cuantil $F^{-1}(u)$ del método de la Transformada Inversa para la Exponencial, y evalúala en $u=0.65$ para obtener un tiempo de falla simulado (en horas). Verifica tu resultado contra `scipy.stats.expon.ppf(0.65, scale=1/0.05)`.
2. Fija la semilla `np.random.seed(6)` y genera 5 valores uniformes con `np.random.rand(5)`. Aplica la Transformada Inversa a cada uno para obtener 5 tiempos de falla simulados y calcula su media.
3. Explica por qué, si otro estudiante ejecuta tu mismo código con `np.random.seed(6)`, debe obtener exactamente los mismos 5 valores.

Escribe tu solución en una celda de código nueva en tu notebook. La celda de autoevaluación de la siguiente sección verificará tu resultado.

## Referencias

* Johansson, R. (2019). *Numerical Python: Scientific Computing and Data Science Applications with Numpy, SciPy and Matplotlib* (2nd ed.). Apress. Capítulos sobre simulación numérica y generación de números aleatorios con SciPy.
* Shabbir, F., Mujeeb, A. A., Jawed, S. F. et al. (2024). Simulation of transvascular transport of nanoparticles in tumor microenvironments for drug delivery applications. *Scientific Reports*, 14, 1764. https://doi.org/10.1038/s41598-024-52292-0 — simulación computacional del transporte de nanopartículas a través de la microvasculatura tumoral, el mismo escenario de difusión estocástica modelado en el ejemplo aplicado de esta unidad.
* Virtanen, P. et al. (2020). SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. *Nature Methods*, 17, 261-272. Documentación: [docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html)

## Herramientas de esta Unidad

**StatsTutorAgent** — resuelve tus dudas conceptuales sobre modelado y simulación estocástica citando el contenido exacto de esta unidad, y te hace una pregunta socrática si detecta un error conceptual común en vez de darte la respuesta directa:

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
            "⚠️ [Unidad 6] No se encontró el secreto GEMINI_API_KEY ni GOOGLE_API_KEY en Colab. "
            "Créalo en el ícono de llave 🔑 de la barra lateral izquierda para usar StatsTutorAgent."
        )

from src.multiagent_core.stats_tutor_agent import StatsTutorAgent

tutor = StatsTutorAgent(course_dir=Path("lecciones"))
print(tutor.ask("¿por qué el método de Monte Carlo necesita muchas iteraciones para converger?"))
```

No requiere configuración adicional más allá de tu `GEMINI_API_KEY` (créala en [aistudio.google.com/apikey](https://aistudio.google.com/apikey) y agrégala como secreto de Colab o variable de entorno local).

## Autoevaluación

Guarda tu solución al Ejercicio Propuesto en un archivo separado y evalúala contra el pipeline de auditoría del curso:

```python
%%writefile solucion_ejercicio_u6.py
# Completa aquí tu solución al Ejercicio Propuesto de esta unidad.
import numpy as np
import scipy.stats as stats

lam = 0.05

# TODO: deriva simbólicamente (o analíticamente) la función cuantil F^-1(u) de la
#       Transformada Inversa para la Exponencial y evalúala en u=0.65
# TODO: verifica tu resultado contra stats.expon.ppf(0.65, scale=1/lam)
# TODO: fija np.random.seed(6), genera 5 valores uniformes con np.random.rand(5),
#       aplica la Transformada Inversa a cada uno y calcula la media de los 5 tiempos de falla
```

```python
from src.multiagent_core.code_auditor_agent import CodeAuditorAgent
from external_skills.pedagogy.socratic_debugger import SocraticDebugger

with open("solucion_ejercicio_u6.py", encoding="utf-8") as f:
    codigo_alumno = f.read()

auditor = CodeAuditorAgent()
resultado = auditor.audit_code(codigo_alumno)

if resultado["issues"] or resultado["metrics"]["has_security_risk"]:
    debugger = SocraticDebugger()
    for issue in resultado["issues"]:
        tipo_error = "syntax_error" if "SyntaxError" in issue else "generic"
        print("💡", debugger.generate_socratic_question(tipo_error, "Unidad 6"))
    for issue in resultado["security_issues"]:
        print("🔒", debugger.generate_socratic_question("security_risk", "Unidad 6"))
        print("   ", issue)
    print("\n--- Detalle técnico ---")
    print(resultado)
else:
    print("✅ Tu código pasa las verificaciones automáticas de estilo y seguridad.")
    print(resultado)
```
