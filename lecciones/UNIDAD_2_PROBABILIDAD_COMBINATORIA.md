# UNIDAD 2: Probabilidad, Teoría de Conjuntos y Combinatoria
## Asignatura: Probabilidad y Estadística Inferencial
### UCEMICH — Ingeniería en IA y Nanotecnología
### Autor y Profesor: Mtro. Luis José Yudico Anaya

---

## Problemas de Nanotecnología: De la Condicionalidad al PCA (Enfoque Computacional)

Todos los problemas requieren el uso de librerías como `numpy` y `scipy.stats` para la simulación, cálculo de distribuciones o análisis matricial.

## I. Distribuciones Condicionales y Esperanza (5.3 - 5.4)

### 1. PMF Condicional: Filtrado de Nanopartículas 🧪
Se filtra una solución de nanopartículas, donde la probabilidad de tener $X$ partículas grandes y $Y$ partículas pequeñas (ambas discretas en $\{1, 2, 3\}$) se conoce.
| $P_{X,Y}(x, y)$ | $Y=1$ | $Y=2$ | $Y=3$ |
| :---: | :---: | :---: | :---: |
| $X=1$ | 0.05 | 0.15 | 0.10 |
| $X=2$ | 0.10 | 0.20 | 0.15 |
| $X=3$ | 0.05 | 0.10 | 0.10 |

**Tarea (Python):**
Calcule la **PMF condicional $P_{Y|X}(y|X=2)$** (probabilidad de partículas pequeñas dado $X=2$). Imprima la PMF y verifique que sume 1.

#### Solución Analítica

La PMF condicional se define como:
$$P_{Y|X}(y|x) = \frac{P_{X,Y}(x, y)}{P_X(x)}$$

Primero, necesitamos la **PMF marginal de $X$ en $X=2$**, $P_X(2)$, que es la suma de las probabilidades de la fila $X=2$:
$$P_X(2) = \sum_{y=1}^{3} P_{X,Y}(2, y) = 0.10 + 0.20 + 0.15 = \mathbf{0.45}$$

Ahora, calculamos las probabilidades condicionales para cada valor de $Y$:

1.  **Para $Y=1$:** $P_{Y|X}(1|2) = \frac{P_{X,Y}(2, 1)}{P_X(2)} = \frac{0.10}{0.45} \approx \mathbf{0.2222}$
2.  **Para $Y=2$:** $P_{Y|X}(2|2) = \frac{P_{X,Y}(2, 2)}{P_X(2)} = \frac{0.20}{0.45} \approx \mathbf{0.4444}$
3.  **Para $Y=3$:** $P_{Y|X}(3|2) = \frac{P_{X,Y}(2, 3)}{P_X(2)} = \frac{0.15}{0.45} \approx \mathbf{0.3333}$

La suma de las probabilidades condicionales es:
$$0.2222 + 0.4444 + 0.3333 = 1.0000$$

#### Solución Computacional (Python) mejorado por Claude

```python
import numpy as np

## Definición de la matriz de probabilidad conjunta (PMF)
## Las filas representan X (partículas grandes), las columnas representan Y (partículas pequeñas)
pmf_xy = np.array([
    [0.05, 0.15, 0.10],  # X=1
    [0.10, 0.20, 0.15],  # X=2
    [0.05, 0.10, 0.10]   # X=3
])

## El índice para X=2 es la fila 1 (Python usa índice 0)
x_index = 1

## 1. Calcular la PMF marginal P_X(2)
p_x_2 = np.sum(pmf_xy[x_index, :])

## 2. Calcular la PMF condicional P_Y|X(y|X=2)
pmf_y_given_x2 = pmf_xy[x_index, :] / p_x_2

print(f"Probabilidad Marginal P_X(2): {p_x_2:.4f}")
print("PMF Condicional P_Y|X(y|X=2):")
print(f"P(Y=1|X=2): {pmf_y_given_x2[0]:.4f}")
print(f"P(Y=2|X=2): {pmf_y_given_x2[1]:.4f}")
print(f"P(Y=3|X=2): {pmf_y_given_x2[2]:.4f}")

suma_total = np.sum(pmf_xy)
print(f"Suma total de P_X,Y: {suma_total}")
## PMF condicional para cada valor de X
for x_val in range(3):
    p_x = np.sum(pmf_xy[x_val, :])
    pmf_cond = pmf_xy[x_val, :] / p_x
    print(f"\nP_Y|X(y|X={x_val+1}):")
    print(pmf_cond)
## Verificar independencia: P(X,Y) = P(X)·P(Y)?
p_x = np.sum(pmf_xy, axis=1)
p_y = np.sum(pmf_xy, axis=0)
pmf_indep = np.outer(p_x, p_y)

print("Diferencia con modelo independiente:")
print(pmf_xy - pmf_indep)
assert np.isclose(np.sum(pmf_y_given_x2), 1.0, atol=1e-10), "La PMF no suma 1"
p_y = np.sum(pmf_xy, axis=0)
print(f"P(Y) marginal: {p_y}")
print(f"P(Y|X=2): {pmf_y_given_x2}")
E_Y_dado_X2 = np.sum([1, 2, 3] * pmf_y_given_x2)
print(f"E[Y|X=2] = {E_Y_dado_X2:.4f}")
import matplotlib.pyplot as plt

## Visualización de la PMF condicional
y_values = [1, 2, 3]
plt.figure(figsize=(8, 5))
plt.bar(y_values, pmf_y_given_x2, color='steelblue', alpha=0.7, edgecolor='black')
plt.xlabel('Y (Partículas Pequeñas)', fontsize=12)
plt.ylabel('P(Y|X=2)', fontsize=12)
plt.title('PMF Condicional: P(Y|X=2)', fontsize=14, fontweight='bold')
plt.xticks(y_values)
plt.ylim(0, 0.5)
plt.grid(axis='y', alpha=0.3)
for i, v in enumerate(pmf_y_given_x2):
    plt.text(y_values[i], v + 0.02, f'{v:.4f}', ha='center', fontweight='bold')
plt.tight_layout()
plt.show()
```

#### Interpretación en el Contexto del Problema

El resultado $P_{Y|X}(y|X=2)$ nos proporciona el **perfil de partículas pequeñas** sabiendo que el filtro retuvo un nivel moderado de **partículas grandes ($X=2$)**.

  * La probabilidad condicional más alta es **$P(Y=2|X=2) \approx 0.4444$**.
  * **Implicación en Nanotecnología:** Si la retención de partículas grandes fue de nivel 2, es casi 44.4% probable que las partículas pequeñas se encuentren en un nivel 2. Esto sugiere una **interdependencia** entre los dos tamaños de partículas. Un operario de filtrado puede usar esta PMF condicional para predecir el resultado de las partículas pequeñas sabiendo solo el resultado de las grandes, optimizando los tiempos de análisis.

### Conclusión

El estudio de la Función de Masa de Probabilidad (PMF) condicional aplicado específicamente al proceso de filtrado de nanopartículas es un ejercicio revelador. Esta metodología estadística nos brinda la capacidad de modelar y anticipar el comportamiento de sistemas complejos, ya sean configuraciones experimentales en el laboratorio o cadenas operativas a escala industrial.

### 2. Esperanza Condicional: Rendimiento de Células Solares ☀️
La eficiencia ($Y$) de una célula solar de puntos cuánticos (GQD) depende de la temperatura de recocido ($X$). La esperanza condicional es $E[Y|X=x] = 20 + 0.1x$. La temperatura $X$ se distribuye uniformemente en $[200, 300]^\circ \text{C}$.
**Tarea (Python):**
Use la **Ley de la Esperanza Total** integrando (o sumando sobre una discreción fina de $X$) para **estimar numéricamente el rendimiento marginal esperado $E[Y]$**.

#### Solución Analítica

La **Ley de la Esperanza Total (LET)** para una variable continua es:
$$E[Y] = E[E[Y|X]] = \int_{-\infty}^{\infty} E[Y|X=x] f_X(x) \,dx$$

1.  **PDF de la temperatura ($X$):** Dado que $X \sim U(200, 300)$, la PDF es:
  $$f_X(x) = \frac{1}{b-a} = \frac{1}{300-200} = \mathbf{0.01} \quad \text{ para } 200 \le x \le 300$$

2.  **Sustitución en la LET:**
  $$E[Y] = \int_{200}^{300} (20 + 0.1x) (0.01) \,dx = \int_{200}^{300} (0.2 + 0.001x) \,dx$$

3.  **Integración:**
  $$E[Y] = \left[ 0.2x + 0.001\frac{x^2}{2} \right]_{200}^{300} = \left[ 0.2x + 0.0005x^2 \right]_{200}^{300}$$
  $$E[Y] = (0.2(300) + 0.0005(300)^2) - (0.2(200) + 0.0005(200)^2)$$
  $$E[Y] = (60 + 45) - (40 + 20) = 105 - 60 = \mathbf{45.0}$$

#### Solución Computacional (Python) mejorado por Claude

Usaremos la integración numérica (regla del trapecio) para verificar el resultado.

```python
import numpy as np
import matplotlib.pyplot as plt

## Simulación Monte Carlo
np.random.seed(42)
n_samples = 100000

## Generar muestras de X ~ U(200, 300)
X_samples = np.random.uniform(200, 300, n_samples)

## Calcular Y para cada X usando E[Y|X=x]
Y_samples = 20 + 0.1 * X_samples

## Estimar E[Y] como la media de las muestras
expected_y_mc = np.mean(Y_samples)
std_error = np.std(Y_samples) / np.sqrt(n_samples)

print(f"E[Y] por Monte Carlo: {expected_y_mc:.4f} ± {std_error:.4f}")
print(f"E[Y] analítico: 45.0")
print(f"Diferencia: {abs(expected_y_mc - 45.0):.6f}")
## Método alternativo: Regla del trapecio
n_points = 1000
x_discrete = np.linspace(200, 300, n_points)
dx = x_discrete[1] - x_discrete[0]

## Calcular el integrando en cada punto
y_values = (20 + 0.1 * x_discrete) * 0.01

## Integración por trapecio
expected_y_trapezoid = np.trapz(y_values, x_discrete)

print(f"E[Y] por regla del trapecio: {expected_y_trapezoid:.4f}")
## ¿Cómo cambia E[Y] si variamos el rango de temperatura?
def calculate_expected_y(a, b):
    """Calcula E[Y] para X ~ U(a, b) con E[Y|X] = 20 + 0.1x"""
    return 20 + 0.1 * (a + b) / 2  # Usando E[X] = (a+b)/2 para uniforme

## Análisis de sensibilidad
ranges = [(180, 280), (190, 290), (200, 300), (210, 310), (220, 320)]
for a, b in ranges:
    e_y = calculate_expected_y(a, b)
    print(f"Rango [{a}, {b}]°C → E[Y] = {e_y:.2f}")
## Método directo: E[Y] = E[E[Y|X]] = E[20 + 0.1X]
## Como X ~ U(200, 300), E[X] = (200 + 300)/2 = 250
e_x = (200 + 300) / 2
e_y_direct = 20 + 0.1 * e_x

print(f"E[Y] método directo: E[20 + 0.1X] = 20 + 0.1·E[X] = 20 + 0.1·{e_x} = {e_y_direct}")

import matplotlib.pyplot as plt

## Crear visualización
x = np.linspace(200, 300, 1000)
e_y_given_x = 20 + 0.1 * x
pdf_x = np.ones_like(x) * 0.01

fig, axes = plt.subplots(2, 1, figsize=(10, 8))

## Panel 1: Esperanza condicional
axes[0].plot(x, e_y_given_x, 'b-', linewidth=2, label='E[Y|X=x] = 20 + 0.1x')
axes[0].axhline(y=45, color='r', linestyle='--', linewidth=2, label='E[Y] = 45.0')
axes[0].fill_between(x, e_y_given_x, alpha=0.3)
axes[0].set_xlabel('Temperatura X (°C)', fontsize=12)
axes[0].set_ylabel('Eficiencia E[Y|X]', fontsize=12)
axes[0].set_title('Esperanza Condicional vs Esperanza Marginal', fontsize=14, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

## Panel 2: PDF de X
axes[1].fill_between(x, pdf_x, alpha=0.5, color='green', label='f_X(x) = 0.01')
axes[1].set_xlabel('Temperatura X (°C)', fontsize=12)
axes[1].set_ylabel('Densidad de Probabilidad', fontsize=12)
axes[1].set_title('Distribución Uniforme de la Temperatura', fontsize=14, fontweight='bold')
axes[1].set_ylim([0, 0.015])
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

#### Interpretación en el Contexto del Problema

El rendimiento promedio esperado $E[Y]$ en la producción total es de **45.0 unidades de eficiencia**.

  * **Implicación en Nanotecnología:** La LET permite calcular el rendimiento promedio de una producción masiva *sin conocer la distribución completa de la eficiencia* (solo su esperanza condicional). Este resultado indica que, dada la variación de la temperatura de recocido (uniforme entre $200^\circ$ y $300^\circ$), el rendimiento promedio se fija en 45. Esto es crucial para la planificación de la producción y la estimación de costos/beneficios, garantizando que el diseño del proceso sea viable en promedio.

### Conclusión

Este ejercicio nos enseña algo clave: usando estadística y probabilidad (la "esperanza condicional"), podemos estimar qué tan bien funcionarán nuestras células solares, incluso cuando hay factores que cambian, como la temperatura de horneado (recocido).

### 3. PDF Condicional: Detección de Fibras de Carbono (Numérico)
La longitud de una fibra ($X$) y la tensión ($Y$) tienen una PDF conjunta $f_{X,Y}(x, y) = 6(1-x-y)$ para $x+y \le 1$ y $x, y \ge 0$. La marginal es $f_X(x) = 3(1-x)^2$.
**Tarea (Python):**
Dado $X=0.5$, calcule numéricamente la **probabilidad $P(Y>0.3 | X=0.5)$** integrando la PDF condicional $f_{Y|X}(y|0.5)$ en el rango $[0.3, 0.5]$.

#### Solución Analítica

1.  **Calcular la PDF Condicional $f_{Y|X}(y|x)$:**
    $$f_{Y|X}(y|x) = \frac{f_{X,Y}(x, y)}{f_X(x)} = \frac{6(1-x-y)}{3(1-x)^2} = \mathbf{\frac{2(1-x-y)}{(1-x)^2}}$$
    El rango de $Y$ es $0 \le y \le 1-x$.

2.  **Sustituir la condición $X=0.5$:**
    $$f_{Y|X}(y|0.5) = \frac{2(1-0.5-y)}{(1-0.5)^2} = \frac{2(0.5-y)}{(0.5)^2} = \frac{1-2y}{0.25} = \mathbf{4 - 8y}$$
    El rango condicional de $Y$ es $0 \le y \le 1-0.5 = 0.5$.

3.  **Calcular la Probabilidad $P(Y>0.3 | X=0.5)$ (Analítico):**
    El rango de integración es $[0.3, 0.5]$:
    $$P(Y>0.3 | X=0.5) = \int_{0.3}^{0.5} (4 - 8y) \,dy = \left[ 4y - 4y^2 \right]_{0.3}^{0.5}$$
    $$P = (4(0.5) - 4(0.5)^2) - (4(0.3) - 4(0.3)^2)$$
    $$P = (2 - 1) - (1.2 - 0.36) = 1 - 0.84 = \mathbf{0.16}$$

#### Solución Computacional (Python) mejorado por Claude

Usaremos la integración numérica para verificar el resultado analítico.

```python
import numpy as np
from scipy.integrate import quad

## Parámetros
x_cond = 0.5
y_start = 0.3
y_end = 0.5  # Límite superior: 1 - x_cond

## PDF condicional simplificada (sin condicionales innecesarios)
def conditional_pdf_y(y):
    return 4 - 8 * y

## Integración numérica
probability_numerical, error = quad(conditional_pdf_y, y_start, y_end)

## Cálculo analítico para comparación
def analytical_result():
## P = [4y - 4y²] evaluado de 0.3 a 0.5
    upper = 4 * y_end - 4 * y_end**2
    lower = 4 * y_start - 4 * y_start**2
    return upper - lower

prob_analytical = analytical_result()

print("DETECCIÓN DE FIBRAS DE CARBONO: PDF CONDICIONAL")
print(f"Condición: X = {x_cond}")
print(f"Evento: P(Y > {y_start} | X = {x_cond})")
print(f"\nPDF Condicional: f_Y|X(y|0.5) = 4 - 8y")
print(f"Rango de integración: [{y_start}, {y_end}]")
print("-"*60)
print(f"Probabilidad Analítica:      {prob_analytical:.4f}")
print(f"Probabilidad Numérica (quad): {probability_numerical:.4f}")
print(f"Error de integración:         {error:.2e}")
print(f"Diferencia absoluta:          {abs(prob_analytical - probability_numerical):.2e}")
print("="*60)
## Verificar que f_Y|X integra a 1 en [0, 0.5]
total_prob, _ = quad(conditional_pdf_y, 0, 0.5)
print(f"\n✓ Verificación: ∫₀^0.5 f_Y|X(y|0.5) dy = {total_prob:.6f}")
print(f"  (Debe ser 1.0 para ser una PDF válida)")
```

#### Interpretación en el Contexto del Problema

La probabilidad condicional $P(Y>0.3 | X=0.5) = 0.16$.

  * **Implicación en Nanotecnología:** Si la longitud de la fibra de carbono está controlada precisamente a $X=0.5$ (la mitad de su longitud máxima posible), la probabilidad de que la tensión máxima que soporte ($Y$) supere un umbral de $0.3$ es de **solo el $16\%$**. Esto sugiere que fibras más cortas (o un control en $X=0.5$) son más propensas a fallar bajo tensiones altas. Este análisis es fundamental para establecer especificaciones de calidad y evitar fallas estructurales.

### Conclusión

Este ejercicio sobre la **PDF condicional** aplicada a la detección de fibras de carbono resalta la relevancia de comprender cómo se relacionan las propiedades físicas de los materiales, como la longitud y la tensión. Este tipo de análisis será esencial para **evaluar la confiabilidad y resistencia de materiales avanzados**, optimizando parámetros de fabricación y asegurando su desempeño en aplicaciones críticas. Saber calcular y analizar probabilidades condicionales me permitirá **anticipar fallas, mejorar procesos de control de calidad** y garantizar que los productos cumplan con los estándares de seguridad y eficiencia.

### 4. Simulación de Esperanza Condicional (LET) 📈
La resistencia de un *nanowire* ($Y$) está modelada por $E[Y|X] = 100 + 10X$, donde $X \sim \text{Poisson}(2)$ (número de defectos). La varianza condicional es $\text{Var}(Y|X=x) = 5x$.
**Tarea (Python):**
Simule $N=10000$ realizaciones de $X$ y, para cada $X_i$, genere una $Y_i$ a partir de la distribución condicional. **Calcule el promedio muestral de $Y$** ($\bar{Y}$) y compárelo con el valor analítico de $E[Y]$ usando la LET.

#### Solución Analítica (LET)

La **Ley de la Esperanza Total (LET)** para una variable discreta es:
$$E[Y] = E[E[Y|X]]$$

1.  **Función de Esperanza Condicional:** $E[Y|X] = 100 + 10X$.
2.  **Propiedad de la Media:** $E[aX + b] = aE[X] + b$.
3.  **Media de $X$ (Poisson):** Si $X \sim \text{Poisson}(\lambda)$, entonces $E[X] = \lambda$. Aquí, $E[X] = \mathbf{2}$.
4.  **Cálculo de $E[Y]$:**
    $$E[Y] = E[100 + 10X] = 100 + 10 E[X] = 100 + 10(2) = \mathbf{120.0}$$

#### Solución Computacional (Python) mejorado por Claude

Usamos la simulación de Monte Carlo para verificar el resultado analítico de 120.

```python
import numpy as np
from scipy.stats import poisson

## Parámetros
N = 10000
lambda_poisson = 2

## 1. Simular X ~ Poisson(2)
X_samples = poisson.rvs(mu=lambda_poisson, size=N)

## 2. Calcular momentos condicionales
mu_y_conditional = 100 + 10 * X_samples
sigma_y_conditional = np.sqrt(5 * X_samples)  # Nota: σ=0 cuando X=0

## 3. SUPUESTO: Y|X ~ N(100+10X, 5X)
## (El problema solo especifica los momentos, no la distribución completa)
Y_samples = np.random.normal(loc=mu_y_conditional, scale=sigma_y_conditional)

## 4. Comparación
expected_y_analytical = 120.0
expected_y_simulated = np.mean(Y_samples)
std_error = np.std(Y_samples, ddof=1) / np.sqrt(N)

print(f"E[Y] Analítico (LET):     {expected_y_analytical:.4f}")
print(f"E[Y] Simulado (N={N}):    {expected_y_simulated:.4f}")
print(f"Error:                    {abs(expected_y_simulated - 120.0):.4f}")
print(f"Error estándar:           {std_error:.4f}")
print(f"IC 95%: [{expected_y_simulated - 1.96*std_error:.4f}, "
      f"{expected_y_simulated + 1.96*std_error:.4f}]")
```

#### Interpretación en el Contexto del Problema

El valor analítico y la estimación por simulación coinciden en que la resistencia promedio de los *nanowires* es de **120.0 $\Omega$**.

  * **Implicación en Nanotecnología:** La resistencia del *nanowire* está fuertemente influenciada por el número de defectos ($X$). Si bien la resistencia *cambia* según el lote (por la variación de $X$), la LET permite a los ingenieros de procesos garantizar que el producto promedio cumpla con la especificación de $120\ \Omega$. El resultado es una **herramienta de pronóstico** que integra la variabilidad del proceso (Poisson de defectos) con la calidad del producto final (resistencia $Y$).

### Conclusión

En la vida real, los nanocables nunca son perfectos; siempre hay defectos o impurezas que cambian su fuerza. Este tipo de análisis estadístico nos enseña a:

Anticipar el Promedio: En lugar de solo adivinar o esperar lo mejor, podemos predecir con bastante exactitud cuál será la resistencia promedio esperada de nuestro lote de materiales o dispositivos.

Identificar Influencias: Nos ayuda a entender exactamente cómo factores como la cantidad de impurezas afectan ese promedio. Saber esto es clave para fabricar mejores productos.

## II. Suma de Variables Aleatorias (5.5)

### 5. Suma de Tiempos de Ensamblaje (Convolución Discreta) ⏱️
El tiempo de preparación $X_1$ y el de montaje $X_2$ de un biosensor (en horas) tienen PMF: $P_{X_1}(1)=0.4, P_{X_1}(2)=0.6$ y $P_{X_2}(1)=0.3, P_{X_2}(2)=0.7$.
**Tarea (Python):**
**Calcule y grafique la PMF del tiempo total $Z = X_1 + X_2$** utilizando el método de convolución discreta (`numpy.convolve`).

#### Solución Analítica

La variable $Z = X_1 + X_2$ puede tomar valores en el conjunto $\{1+1, 1+2, 2+1, 2+2\} = \mathbf{\{2, 3, 4\}}$.

La PMF de $Z$ se calcula mediante la **convolución discreta** de $P_{X_1}$ y $P_{X_2}$:
$$P_Z(z) = \sum_{x_1} P_{X_1}(x_1) P_{X_2}(z - x_1)$$

1.  **$P_Z(2)$** (cuando $X_1=1, X_2=1$):
  $$P_Z(2) = P_{X_1}(1) P_{X_2}(1) = (0.4)(0.3) = \mathbf{0.12}$$

2.  **$P_Z(3)$** (cuando $X_1=1, X_2=2$ o $X_1=2, X_2=1$):
  $$P_Z(3) = P_{X_1}(1) P_{X_2}(2) + P_{X_1}(2) P_{X_2}(1) = (0.4)(0.7) + (0.6)(0.3) = 0.28 + 0.18 = \mathbf{0.46}$$

3.  **$P_Z(4)$** (cuando $X_1=2, X_2=2$):
  $$P_Z(4) = P_{X_1}(2) P_{X_2}(2) = (0.6)(0.7) = \mathbf{0.42}$$

**Verificación:** $0.12 + 0.46 + 0.42 = 1.00$.

#### Solución Computacional (Python) mejorado por Claude

```python
import numpy as np
import matplotlib.pyplot as plt

## SUPUESTO: X1 y X2 son INDEPENDIENTES (necesario para usar convolución)

## PMF de X1 y X2
## Representación: pmf_x1[i] = P(X1 = i+1), donde i es el índice del array
pmf_x1 = np.array([0.4, 0.6])  # P(X1=1)=0.4, P(X1=2)=0.6
pmf_x2 = np.array([0.3, 0.7])  # P(X2=1)=0.3, P(X2=2)=0.7

## Validaciones
assert np.isclose(np.sum(pmf_x1), 1.0), "PMF de X1 no suma 1"
assert np.isclose(np.sum(pmf_x2), 1.0), "PMF de X2 no suma 1"
assert np.all(pmf_x1 >= 0) and np.all(pmf_x2 >= 0), "Probabilidades negativas"

## Definir rangos explícitamente
x1_values = np.array([1, 2])
x2_values = np.array([1, 2])

## Calcular PMF de Z mediante convolución
pmf_z = np.convolve(pmf_x1, pmf_x2)

## Rango de Z: desde min(X1)+min(X2) hasta max(X1)+max(X2)
z_values = np.arange(x1_values.min() + x2_values.min(),
                      x1_values.max() + x2_values.max() + 1)

## Validar resultado
assert np.isclose(np.sum(pmf_z), 1.0), "PMF de Z no suma 1"

## Resultados
print("=" * 50)
print("PMF de Z = X1 + X2")
print("=" * 50)
for z, p in zip(z_values, pmf_z):
    print(f"P(Z={z}) = {p:.4f}")
print(f"\nVerificación: Σ P(Z) = {np.sum(pmf_z):.4f}")

## Estadísticos
E_X1 = np.sum(x1_values * pmf_x1)
E_X2 = np.sum(x2_values * pmf_x2)
E_Z_teorico = E_X1 + E_X2
E_Z_numerico = np.sum(z_values * pmf_z)

print("\n" + "=" * 50)
print("Estadísticos")
print("=" * 50)
print(f"E[X1] = {E_X1:.2f}")
print(f"E[X2] = {E_X2:.2f}")
print(f"E[Z] (teórico por linealidad) = {E_Z_teorico:.2f}")
print(f"E[Z] (numérico desde PMF) = {E_Z_numerico:.2f}")

## Gráfico
plt.figure(figsize=(8, 5))
bars = plt.bar(z_values, pmf_z, width=0.4, color='skyblue',
               edgecolor='black', linewidth=1.5)
plt.title('PMF del Tiempo Total de Ensamblaje Z = X₁ + X₂', fontsize=14, fontweight='bold')
plt.xlabel('Tiempo Total (horas)', fontsize=12)
plt.ylabel('Probabilidad P(Z=z)', fontsize=12)
plt.xticks(z_values)
plt.ylim(0, 0.5)

## Añadir valores sobre las barras
for bar, p in zip(bars, pmf_z):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{p:.2f}', ha='center', va='bottom', fontweight='bold')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
```

#### Interpretación en el Contexto del Problema

El tiempo total de ensamblaje del biosensor $Z$ tiene la siguiente distribución: $P(Z=2)=12\%$, $P(Z=3)=46\%$, y $P(Z=4)=42\%$.

  * **Implicación en Nanotecnología:** La probabilidad de que el ensamblaje tome **3 horas ($46\%$) es la más alta**. Sorprendentemente, la probabilidad de que tome **4 horas ($42\%$) es casi tan alta**. Esto sugiere que la variabilidad en los tiempos de ensamblaje ($X_1$ y $X_2$) provoca que el tiempo total se distribuya ampliamente alrededor de la media. El gerente de producción debe planificar el $88\%$ de los ensamblajes para que tomen $\mathbf{3}$ o $\mathbf{4}$ horas, siendo las 2 horas un evento atípico.

### Conclusión

Este ejercicio demuestra que dominar la convolución discreta no es solo un truco matemático, sino una habilidad vital para cualquier ingeniero o gerente de proyectos. Nos da el poder de calcular cómo se comporta la suma de varios tiempos o costos inciertos ($Z = X_1 + X_2$) para obtener una distribución total.

### 6. Suma de Fallas de Poisson (Python)
El número de fallas por litografía ($X_1$) sigue $\text{Poisson}(\lambda_1=3)$ y por deposición ($X_2$) sigue $\text{Poisson}(\lambda_2=5)$. $Z = X_1 + X_2$.
**Tarea (Python):**
Calcule la **probabilidad $P(Z \le 8)$** usando la propiedad de la suma de Poisson (con $\lambda=8$) y la función de distribución acumulada (CDF) de Poisson de `scipy.stats`.

#### Solución Analítica

La suma de variables de Poisson independientes es también una variable de Poisson.
Si $X_1 \sim \text{Poisson}(\lambda_1)$ y $X_2 \sim \text{Poisson}(\lambda_2)$, entonces $Z = X_1 + X_2 \sim \text{Poisson}(\lambda)$, donde $\lambda = \lambda_1 + \lambda_2$.

1.  **Parámetro de $Z$:** $\lambda = 3 + 5 = \mathbf{8}$.
2.  **Probabilidad Requerida:** $P(Z \le 8) = P(Z=0) + P(Z=1) + \dots + P(Z=8)$.

La fórmula de la PMF de Poisson es $P(Z=k) = \frac{e^{-\lambda} \lambda^k}{k!}$.
  $P(Z \le 8) = \sum_{k=0}^{8} \frac{e^{-8} 8^k}{k!}$

#### Solución Computacional (Python) mejorado por Claude

Usamos la **función de distribución acumulada (CDF)** de Poisson para evitar sumar cada término.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

## SUPUESTO CRÍTICO: X1 y X2 son INDEPENDIENTES
## Esto permite usar la propiedad: Z = X1 + X2 ~ Poisson(λ1 + λ2)

## Parámetros
lambda_1 = 3  # Fallas por litografía
lambda_2 = 5  # Fallas por deposición
lambda_z = lambda_1 + lambda_2  # λ total = 8
k_threshold = 8  # Umbral de interés

print("=" * 60)
print("SUMA DE VARIABLES POISSON")
print("=" * 60)
print(f"X1 ~ Poisson(λ1={lambda_1}) - Fallas litografía")
print(f"X2 ~ Poisson(λ2={lambda_2}) - Fallas deposición")
print(f"Z = X1 + X2 ~ Poisson(λ={lambda_z})")
print("=" * 60)

## 1. Calcular P(Z ≤ 8) usando CDF
prob_z_le_k = poisson.cdf(k_threshold, mu=lambda_z)

print(f"\nProbabilidad acumulada:")
print(f"P(Z ≤ {k_threshold}) = {prob_z_le_k:.4f} ({prob_z_le_k*100:.2f}%)")
print(f"P(Z > {k_threshold}) = {1-prob_z_le_k:.4f} ({(1-prob_z_le_k)*100:.2f}%)")

## 2. Validación: Sumar PMF manualmente
prob_manual = sum(poisson.pmf(k, mu=lambda_z) for k in range(k_threshold + 1))
print(f"\nValidación (suma manual de PMF): {prob_manual:.4f}")
print(f"Diferencia: {abs(prob_z_le_k - prob_manual):.2e}")

## 3. Estadísticos
media_z = lambda_z
std_z = np.sqrt(lambda_z)
mediana_z = poisson.ppf(0.5, mu=lambda_z)

print("\n" + "=" * 60)
print("ESTADÍSTICOS")
print("=" * 60)
print(f"E[Z] = {media_z:.2f}")
print(f"Var[Z] = {lambda_z:.2f}")
print(f"σ[Z] = {std_z:.2f}")
print(f"Mediana[Z] = {mediana_z:.0f}")

## 4. Cuantiles para planificación
percentiles = [0.50, 0.75, 0.90, 0.95, 0.99]
print("\n" + "=" * 60)
print("CUANTILES PARA PLANIFICACIÓN")
print("=" * 60)
for p in percentiles:
    q = poisson.ppf(p, mu=lambda_z)
    print(f"P(Z ≤ {q:.0f}) = {p*100:.0f}%")

## 5. Visualización
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

## Subplot 1: PMF con área acumulada
k_values = np.arange(0, 20)
pmf_values = poisson.pmf(k_values, mu=lambda_z)

axes[0].bar(k_values, pmf_values, color='lightgray', edgecolor='black',
            label='PMF de Z')
axes[0].bar(k_values[k_values <= k_threshold],
            pmf_values[k_values <= k_threshold],
            color='skyblue', edgecolor='black',
            label=f'P(Z ≤ {k_threshold}) = {prob_z_le_k:.4f}')
axes[0].axvline(lambda_z, color='red', linestyle='--', linewidth=2,
                label=f'E[Z] = {lambda_z}')
axes[0].set_xlabel('Número de Fallas (Z)', fontsize=11)
axes[0].set_ylabel('Probabilidad P(Z=k)', fontsize=11)
axes[0].set_title('PMF de Z = X₁ + X₂ ~ Poisson(8)', fontsize=12, fontweight='bold')
axes[0].legend()
axes[0].grid(axis='y', alpha=0.3)

## Subplot 2: CDF
k_values_cdf = np.arange(0, 25)
cdf_values = poisson.cdf(k_values_cdf, mu=lambda_z)

axes[1].step(k_values_cdf, cdf_values, where='post', color='navy', linewidth=2)
axes[1].scatter(k_threshold, prob_z_le_k, color='red', s=100, zorder=5,
                label=f'P(Z ≤ {k_threshold}) = {prob_z_le_k:.4f}')
axes[1].hlines(0.5, 0, k_threshold, color='gray', linestyle=':', alpha=0.7)
axes[1].vlines(k_threshold, 0, prob_z_le_k, color='red', linestyle='--', alpha=0.7)
axes[1].set_xlabel('Número de Fallas (k)', fontsize=11)
axes[1].set_ylabel('Probabilidad Acumulada P(Z ≤ k)', fontsize=11)
axes[1].set_title('CDF de Z ~ Poisson(8)', fontsize=12, fontweight='bold')
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()

## 6. Interpretación contextual mejorada
print("\n" + "=" * 60)
print("INTERPRETACIÓN PARA CONTROL DE CALIDAD")
print("=" * 60)
print(f"• El número ESPERADO de fallas totales es {lambda_z}")
print(f"• Hay {prob_z_le_k*100:.1f}% de probabilidad de tener ≤{k_threshold} fallas")
print(f"• Hay {(1-prob_z_le_k)*100:.1f}% de RIESGO de exceder {k_threshold} fallas")
print(f"• En el 95% de lotes, habrá como máximo {poisson.ppf(0.95, mu=lambda_z):.0f} fallas")
print("\nRECOMENDACIÓN:")
print(f"  Si el umbral de aceptación es {k_threshold} fallas, aproximadamente")
print(f"  {(1-prob_z_le_k)*100:.0f}% de los lotes requerirán reprocesamiento.")
```

#### Interpretación en el Contexto del Problema

La probabilidad de que las fallas totales $Z$ sean menores o iguales a 8 es de **$P(Z \le 8) \approx 0.5925$**.

  * **Implicación en Nanotecnología:** El número esperado de fallas es $\lambda=8$. Como la distribución de Poisson es asimétrica, la probabilidad de que el número de fallas sea menor o igual al valor esperado es del $\mathbf{59.25\%}$. Esto proporciona una métrica de riesgo para la producción: hay un $40.75\%$ de probabilidad de que el lote exceda las 8 fallas. Este análisis es esencial para el **cálculo de rendimiento** y la toma de decisiones sobre si un lote es aceptable o necesita reprocesamiento.

### Conclusión

Comprender la Distribución de Poisson y cómo se combinan estas variables nos equipa para enfrentar retos reales, especialmente en la fabricación de productos delicados como dispositivos nanotecnológicos o electrónicos. Esta habilidad es clave porque nos permite:

Anticipar Defectos: Nos ayuda a estimar cuántos defectos podemos esperar en una línea de producción en un tiempo o espacio determinado (por ejemplo, fallas por metro cuadrado de un chip).

Evaluar Riesgos: Podemos cuantificar la probabilidad de tener un lote con demasiados errores, permitiéndonos tomar medidas antes de que sea demasiado tarde.

Optimizar la Eficiencia: Al saber dónde y cuándo se concentran las fallas, podemos ajustar los procesos para reducir los errores y, por lo tanto, mejorar la eficiencia y reducir costos.

### 7. Varianza de la Suma Correlacionada (Python)
Dos propiedades de un polímero $X$ y $Y$ tienen $\text{Var}(X)=16$, $\text{Var}(Y)=9$, y $\rho_{X,Y} = -0.7$. Se estudia la variable de desempeño $D = 2X + 3Y$.
**Tarea (Python):**
Calcule la **covarianza $\text{Cov}(X, Y)$** y use las propiedades de la varianza para **calcular $\text{Var}(D)$**.

### Problema 7: Varianza de la Suma Correlacionada (Python)

Dos propiedades de un polímero $X$ y $Y$ tienen $\text{Var}(X)=16$, $\text{Var}(Y)=9$, y $\rho_{X,Y} = -0.7$. Se estudia la variable de desempeño $D = 2X + 3Y$.

**Tarea (Python):**
Calcule la **covarianza $\text{Cov}(X, Y)$** y use las propiedades de la varianza para **calcular $\text{Var}(D)$**.

#### Solución Analítica

La varianza de una combinación lineal de variables aleatorias correlacionadas es:
$$\text{Var}(D) = \text{Var}(aX + bY) = a^2\text{Var}(X) + b^2\text{Var}(Y) + 2ab\text{Cov}(X, Y)$$

1.  **Cálculo de la Covarianza $\text{Cov}(X, Y)$:**
    $$\text{Cov}(X, Y) = \rho_{X,Y} \sqrt{\text{Var}(X)} \sqrt{\text{Var}(Y)} = (-0.7) (\sqrt{16}) (\sqrt{9})$$
    $$\text{Cov}(X, Y) = (-0.7)(4)(3) = \mathbf{-8.4}$$

2.  **Cálculo de la Varianza de $D$ ($\text{Var}(D)$):**
    Aquí, $a=2$ y $b=3$.
    $$\text{Var}(D) = (2)^2(16) + (3)^2(9) + 2(2)(3)(-8.4)$$
    $$\text{Var}(D) = 4(16) + 9(9) + 12(-8.4)$$
    $$\text{Var}(D) = 64 + 81 - 100.8$$
    $$\text{Var}(D) = 145 - 100.8 = \mathbf{44.2}$$

#### Solución Computacional (Python) mejorado por Claude

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

print("="*70)
print("VARIANZA DE COMBINACIÓN LINEAL CON CORRELACIÓN")
print("="*70)

## Parámetros dados
var_x = 16
var_y = 9
rho_xy = -0.7
a = 2  # Coeficiente de X en D
b = 3  # Coeficiente de Y en D

## Desviaciones estándar
std_x = np.sqrt(var_x)
std_y = np.sqrt(var_y)

## 1. Calcular la Covarianza
cov_xy = rho_xy * std_x * std_y

print(f"\nCálculo de covarianza:")
print(f"  Cov(X,Y) = ρ·σ(X)·σ(Y) = {rho_xy}·{std_x}·{std_y} = {cov_xy:.2f}")

## 2. Verificar validez de la matriz de covarianza
cov_matrix = np.array([[var_x, cov_xy],
                       [cov_xy, var_y]])
eigenvalues = np.linalg.eigvals(cov_matrix)

print(f"\nValidación de la matriz de covarianza:")
print(f"  Autovalores: {eigenvalues}")
if np.all(eigenvalues >= -1e-10):  # Tolerancia numérica
    print("  ✓ Matriz es semidefinida positiva (válida)")
else:
    print("  ✗ ERROR: Matriz no es válida")

## 3. Calcular Var(D)
var_d = (a**2 * var_x) + (b**2 * var_y) + (2 * a * b * cov_xy)
std_d = np.sqrt(var_d)

print("\n" + "="*70)
print("RESULTADOS")
print("="*70)
print(f"Var(D) = {a}²·{var_x} + {b}²·{var_y} + 2·{a}·{b}·{cov_xy:.2f}")
print(f"Var(D) = {a**2 * var_x:.0f} + {b**2 * var_y:.0f} + {2*a*b*cov_xy:.1f}")
print(f"Var(D) = {var_d:.2f}")
print(f"σ(D)   = {std_d:.2f}")

## 4. Análisis del efecto de correlación
var_d_independent = a**2 * var_x + b**2 * var_y
var_d_perfect_neg = a**2 * var_x + b**2 * var_y - 2*a*b*std_x*std_y
var_d_perfect_pos = a**2 * var_x + b**2 * var_y + 2*a*b*std_x*std_y

print("\n" + "="*70)
print("EFECTO DE LA CORRELACIÓN")
print("="*70)
print(f"Var(D) si ρ = -1 (correlación perfecta negativa): {var_d_perfect_neg:.2f}")
print(f"Var(D) si ρ =  0 (independientes):                {var_d_independent:.2f}")
print(f"Var(D) si ρ = {rho_xy} (caso actual):                  {var_d:.2f}")
print(f"Var(D) si ρ = +1 (correlación perfecta positiva): {var_d_perfect_pos:.2f}")

reduction = (var_d_independent - var_d) / var_d_independent * 100
print(f"\n¡La correlación negativa reduce Var(D) en {reduction:.1f}%!")

## 5. Validación por simulación
n_samples = 100000
samples = multivariate_normal.rvs(mean=[0, 0], cov=cov_matrix, size=n_samples)
X_sim = samples[:, 0]
Y_sim = samples[:, 1]
D_sim = a * X_sim + b * Y_sim

var_d_simulated = np.var(D_sim, ddof=1)
cov_xy_simulated = np.cov(X_sim, Y_sim)[0, 1]

print("\n" + "="*70)
print(f"VALIDACIÓN POR SIMULACIÓN (N={n_samples:,})")
print("="*70)
print(f"Cov(X,Y): Analítico = {cov_xy:.4f}, Simulado = {cov_xy_simulated:.4f}")
print(f"Var(D):   Analítico = {var_d:.4f}, Simulado = {var_d_simulated:.4f}")
print(f"Error relativo: {abs(var_d - var_d_simulated)/var_d * 100:.3f}%")

## 6. Visualizaciones
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

## Subplot 1: Efecto de ρ en Var(D)
rho_range = np.linspace(-1, 1, 200)
var_d_range = []

for rho in rho_range:
    cov_temp = rho * std_x * std_y
    var_d_temp = (a**2 * var_x) + (b**2 * var_y) + (2 * a * b * cov_temp)
    var_d_range.append(var_d_temp)

axes[0].plot(rho_range, var_d_range, linewidth=2.5, color='navy',
             label='Var(D) en función de ρ')
axes[0].scatter(rho_xy, var_d, color='red', s=150, zorder=5,
                label=f'Caso actual: ρ={rho_xy}, Var(D)={var_d:.2f}')
axes[0].axhline(var_d_independent, color='gray', linestyle='--',
                label=f'ρ=0: Var(D)={var_d_independent:.0f}')
axes[0].axvline(0, color='lightgray', linestyle='-', alpha=0.5)
axes[0].axhline(var_d, color='red', linestyle=':', alpha=0.5)
axes[0].set_xlabel('Coeficiente de Correlación ρ(X,Y)', fontsize=12)
axes[0].set_ylabel('Var(D = 2X + 3Y)', fontsize=12)
axes[0].set_title('Efecto de la Correlación en la Varianza',
                  fontsize=13, fontweight='bold')
axes[0].legend(fontsize=10)
axes[0].grid(alpha=0.3)

## Subplot 2: Distribución simulada de D
axes[1].hist(D_sim, bins=100, density=True, alpha=0.7, color='skyblue',
             edgecolor='black', label='Distribución simulada')
axes[1].axvline(0, color='red', linestyle='--', linewidth=2,
                label=f'E[D] = 0 (centrado)')
axes[1].axvline(std_d, color='orange', linestyle='--', linewidth=2,
                label=f'σ(D) = {std_d:.2f}')
axes[1].axvline(-std_d, color='orange', linestyle='--', linewidth=2)
axes[1].set_xlabel('Valor de D = 2X + 3Y', fontsize=12)
axes[1].set_ylabel('Densidad', fontsize=12)
axes[1].set_title('Distribución Simulada de D (N=100,000)',
                  fontsize=13, fontweight='bold')
axes[1].legend(fontsize=10)
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()

## 7. Interpretación final
print("\n" + "="*70)
print("INTERPRETACIÓN EN CIENCIA DE MATERIALES")
print("="*70)
print("""
La correlación NEGATIVA entre X y Y actúa como un mecanismo de
ESTABILIZACIÓN del desempeño:

• Cuando X es alto → Y tiende a ser bajo
• Esta compensación reduce la variabilidad total
• Resultado: Índice D más predecible y robusto

Implicación práctica:
  - Var(D) = 44.2 (con correlación)
  - Var(D) = 145.0 (sin correlación)
  - Reducción del 70% en varianza

Esto sugiere un TRADE-OFF natural entre las propiedades X e Y,
lo que es beneficioso para el control de calidad del polímero.
""")
```

#### Interpretación en el Contexto del Problema

La varianza del índice de desempeño $D$ es de **$44.2$**.

  * **Implicación en Nanotecnología:** La $\text{Var}(D)$ mide la **incertidumbre total** en el desempeño del polímero. El factor clave es la **correlación negativa $\rho=-0.7$ ($\text{Cov}=-8.4$)**. Esta correlación negativa reduce significativamente la varianza total: si $X$ es alto, $Y$ tiende a ser bajo, compensando el efecto en la suma. Si los términos de covarianza no existieran, la varianza sería mucho mayor ($\text{Var}(D) = 64 + 81 = 145$). La varianza de $44.2$ indica una **alta estabilidad** del índice de desempeño, gracias a la relación de *trade-off* entre las dos propiedades del polímero.

### Conclusión

En mi futuro como profesional, podré aplicar este conocimiento para:

Evaluar la Confiabilidad: Determinar qué tan estable y predecible es una propiedad física crítica (como la resistencia o la conductividad) en materiales complejos como polímeros, compuestos o nanomateriales.

Diseñar con Menos Riesgo: Entender que cuando dos variables críticas se mueven en direcciones opuestas (correlación negativa), se produce un efecto de compensación. Esta compensación es oro molido, pues logra reducir la variabilidad total del material.

### 8. Simulación de la Distribución Triangular (Python)
La longitud total de un nanorobot $Z = X_1 + X_2$, donde $X_1, X_2 \sim U(0, 1)$ son independientes.
**Tarea (Python):**
Genere $N=10000$ muestras de $Z$ (sumando dos uniformes). **Grafique el histograma de $Z$** y verifique visualmente la forma triangular predicha por la convolución.

#### Solución Analítica

La suma de dos variables uniformes i.i.d. $U(0, 1)$ es la **distribución triangular** (o de Irwin-Hall para $n=2$).
La PDF es:
$$f_Z(z) = \begin{cases} z & 0 \le z \le 1 \\ 2 - z & 1 < z \le 2 \\ 0 & \text{otro caso} \end{cases}$$
El soporte es $[0, 2]$, con un pico en $z=1$.

#### Solución Computacional (Python) mejorado por Claude

```python
def triangular_pdf(z):
    return np.where((z >= 0) & (z <= 1), z,
                    np.where((z > 1) & (z <= 2), 2 - z, 0))

## Generate samples from the sum of two U(0,1) distributions
np.random.seed(42) # for reproducibility
num_samples = 10000
X_samples = np.random.rand(num_samples)
Y_samples = np.random.rand(num_samples)
Z_samples = X_samples + Y_samples

z_teorico = np.linspace(0, 2, 100)
pdf_teorico = triangular_pdf(z_teorico)  # Vectorizado

## Verificación de momentos
print(f"Media teórica: 1.0, Media simulada: {np.mean(Z_samples):.4f}")
print(f"Varianza teórica: 1/6 ≈ 0.1667, Varianza simulada: {np.var(Z_samples):.4f}")
from scipy import stats
## CDF teórica de la triangular
cdf_teorica = lambda z: np.where(z <= 1, z**2/2, 1 - (2-z)**2/2)
ks_stat, p_value = stats.kstest(Z_samples, cdf_teorica)
print(f"Test K-S: estadístico={ks_stat:.4f}, p-valor={p_value:.4f}")
plt.figure(figsize=(10, 6))
plt.hist(Z_samples, bins=50, density=True, color='lightcoral',
         edgecolor='black', alpha=0.7, label='Simulación (N=10000)')
plt.plot(z_teorico, pdf_teorico, 'b-', linewidth=2.5,
         label='PDF Teórica')
plt.axvline(1, color='red', linestyle='--', linewidth=1.5,
            label='Moda (z=1)')
plt.fill_between(z_teorico, pdf_teorico, alpha=0.2, color='blue')
plt.title('Distribución Triangular: Suma de dos U(0,1)', fontsize=14)
plt.xlabel('Longitud Total Z (μm)', fontsize=12)
plt.ylabel('Densidad de Probabilidad', fontsize=12)
plt.legend(fontsize=11)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

#### Interpretación en el Contexto del Problema

El histograma generado por la simulación reproduce la forma triangular de la PDF analítica.

  * **Implicación en Nanotecnología:** La longitud total $Z$ del nanorobot (suma de dos subsistemas) es más probable que sea de $\mathbf{1.0\ \mu\text{m}}$ (el pico de la distribución). Es mucho menos probable que sea extremadamente corta (cercana a 0) o extremadamente larga (cercana a 2). El hecho de que la suma de variables de entrada no uniformes produzca una **distribución concentrada** es un fenómeno de **regularización** estadístico (precursor del Teorema del Límite Central), lo que permite a los diseñadores predecir que la variación de la longitud total será menor que la suma simple de los rangos de las partes.

### Conclusión

El conocimiento de estas distribuciones nos ayuda a:

Predecir la variabilidad: Nos permite anticipar qué tanto van a variar las dimensiones críticas (como el grosor de una capa o el largo de un componente) o las propiedades de funcionamiento (como qué tan rápido responde el aparato).

Asegurar la calidad: Si sabemos que la forma de la distribución (por ejemplo, si es un triángulo o una campana) nos dice dónde estará la mayoría de nuestros resultados, podemos diseñar procesos que reduzcan esa variación y nos aseguremos de que casi todos los productos funcionen correctamente.

## III. Vectores Aleatorios y la Gaussiana Multidimensional (5.6 - 5.7)

### 9. Vector de Medias y Covarianza Muestral (Datos de Recubrimiento) 📊
Se miden tres variables de un recubrimiento cerámico en 5 muestras: Dureza ($X_1$), Adherencia ($X_2$), y Rugosidad ($X_3$).

$$\mathbf{D} = \begin{pmatrix} 7.5 & 8.2 & 0.5 \\ 8.0 & 7.9 & 0.4 \\ 7.2 & 8.5 & 0.6 \\ 7.8 & 8.0 & 0.5 \\ 8.1 & 8.3 & 0.3 \end{pmatrix}$$

**Tarea (Python):**
Calcule el **vector de medias muestral** ($\bar{\mathbf{x}}$) y la **matriz de covarianza muestral** ($\mathbf{S}$) de los datos.

#### Solución Analítica (Fórmulas)

El **Vector de Medias Muestral** $\bar{\mathbf{x}}$ se calcula tomando el promedio de cada columna (propiedad):
$$\bar{\mathbf{x}} = \begin{pmatrix} \bar{X}_1 \\ \bar{X}_2 \\ \bar{X}_3 \end{pmatrix}$$
El cálculo de la **Matriz de Covarianza Muestral** $\mathbf{S}$ (tamaño $3 \times 3$) usa la fórmula general:
$$S_{ij} = \frac{1}{N-1} \sum_{k=1}^{N} (X_{k,i} - \bar{X}_i)(X_{k,j} - \bar{X}_j)$$

#### Solución Computacional (Python)

Utilizaremos las funciones `numpy.mean` y `numpy.cov`.

```python
import numpy as np

## Datos: Filas = Muestras (5), Columnas = Variables (3)
data_matrix = np.array([
    [7.5, 8.2, 0.5],
    [8.0, 7.9, 0.4],
    [7.2, 8.5, 0.6],
    [7.8, 8.0, 0.5],
    [8.1, 8.3, 0.3]
])

## 1. Calcular el Vector de Medias Muestral (promedio por columna)
mean_vector = np.mean(data_matrix, axis=0)

## 2. Calcular la Matriz de Covarianza Muestral
## rowvar=False indica que las variables están en las columnas (como es estándar)
covariance_matrix = np.cov(data_matrix, rowvar=False)

print("--- Vector de Medias Muestral ---")
print(f"X1 (Dureza): {mean_vector[0]:.2f}")
print(f"X2 (Adherencia): {mean_vector[1]:.2f}")
print(f"X3 (Rugosidad): {mean_vector[2]:.2f}")
print(f"Vector de Medias (x̄):\n{mean_vector}")

print("\n--- Matriz de Covarianza Muestral (S) ---")
print(covariance_matrix)
```

#### Interpretación en el Contexto del Problema

**Vector de Medias:** $\bar{\mathbf{x}} \approx (7.72, 8.18, 0.46)^T$. El lote promedio tiene una dureza de 7.72, una adherencia de 8.18 y una rugosidad de 0.46.

**Matriz de Covarianza Muestral ($\mathbf{S}$):**

$$\mathbf{S} \approx \begin{pmatrix} 0.1070 & -0.0150 & -0.0405 \\ -0.0150 & 0.0570 & 0.0035 \\ -0.0405 & 0.0035 & 0.0128 \end{pmatrix}$$

  * **Varianza (Diagonal):** La dureza ($X_1$) tiene la mayor varianza (0.1070), lo que indica que es la propiedad **menos controlada o más variable** del recubrimiento. La rugosidad ($X_3$) tiene la menor varianza (0.0128).
  * **Covarianza (No Diagonal):**
      * $\text{Cov}(X_1, X_2) \approx -0.0150$ (Negativa): Una mayor dureza tiende a relacionarse ligeramente con una menor adherencia.
      * $\text{Cov}(X_1, X_3) \approx -0.0405$ (Negativa): La dureza y la rugosidad tienen la **correlación más fuerte y negativa** entre los pares. Esto es una relación deseada: el proceso que produce mayor dureza también produce menor rugosidad (superficie más lisa).
      * $\text{Cov}(X_2, X_3) \approx 0.0035$ (Cercana a cero): Adherencia y Rugosidad son prácticamente independientes.

Este análisis revela las **relaciones internas** del recubrimiento, vitales para el control de procesos.

### Conclusión

Saber Dónde Enfocarse (Vector de Medias): El vector de promedios nos dice el valor típico o central de cada propiedad (dureza promedio, adherencia promedio, etc.). Esto establece el punto de referencia de nuestro material.

Ver Cómo Se Mueven Juntas (Matriz de Covarianza): La matriz de dispersión es lo más interesante. Nos muestra:

Variabilidad: Cuánto se dispersa o cambia cada propiedad. Si una propiedad cambia mucho (alta dispersión), la calidad del material es inestable y necesita control.

Relación: Cómo se afectan entre sí las propiedades. Por ejemplo, si al aumentar la dureza, la adherencia tiende a bajar, sabemos que existe un compromiso (trade-off) entre ellas.

### 10. Distancia de Mahalanobis y Probabilidad Gaussiana (Python) 🚨
Un vector de temperatura y presión $\mathbf{X} \sim \mathcal{N}(\mathbf{\mu}, \mathbf{\Sigma})$ con $\mathbf{\mu} = \begin{pmatrix} 50 \\ 1 \end{pmatrix}$ y $\mathbf{\Sigma} = \begin{pmatrix} 1 & 0.2 \\ 0.2 & 0.04 \end{pmatrix}$. Se detecta una anomalía en $\mathbf{x}_{\text{anom}} = \begin{pmatrix} 52 \\ 1.5 \end{pmatrix}$.
**Tarea (Python):**
Calcule la **Distancia de Mahalanobis $\mathbf{D}^2$** de $\mathbf{x}_{\text{anom}}$ al centro. Luego, calcule la **densidad de probabilidad $f_{\mathbf{X}}(\mathbf{x}_{\text{anom}})$** usando `scipy.stats.multivariate_normal`.

#### Solución Analítica (Fórmulas)

La **Distancia de Mahalanobis al cuadrado ($\mathbf{D}^2$)** es:
$$\mathbf{D}^2 = (\mathbf{x} - \mathbf{\mu})^T \mathbf{\Sigma}^{-1} (\mathbf{x} - \mathbf{\mu})$$

El vector de diferencia es $\mathbf{d} = \mathbf{x}_{\text{anom}} - \mathbf{\mu} = \begin{pmatrix} 52-50 \\ 1.5-1 \end{pmatrix} = \begin{pmatrix} 2 \\ 0.5 \end{pmatrix}$.

**Cálculo Analítico de $\mathbf{\Sigma}^{-1}$:**
Para una matriz $2 \times 2$, $\mathbf{\Sigma} = \begin{pmatrix} a & b \\ b & c \end{pmatrix}$, $\det(\mathbf{\Sigma}) = ac - b^2$.
$$\det(\mathbf{\Sigma}) = (1)(0.04) - (0.2)^2 = 0.04 - 0.04 = \mathbf{0}$$

**¡Advertencia Analítica\!** La matriz $\mathbf{\Sigma}$ **no es invertible** ($\det(\mathbf{\Sigma}) = 0$).

Esto implica que las variables $X_1$ y $X_2$ están **perfectamente correlacionadas** o **linealmente dependientes** (en este caso, $\rho=1$). Esto es un caso degenerado de la Gaussiana Multivariada.

  * $\mathbf{X_2} = a\mathbf{X_1} + b$. Analizando la varianza: $\text{Var}(X_2) = a^2 \text{Var}(X_1) \implies 0.04 = a^2(1) \implies a=0.2$. La covarianza: $\text{Cov}(X_1, X_2) = a\text{Var}(X_1) \implies 0.2 = a(1) \implies a=0.2$.

La relación es $X_2 = 0.2X_1 + \text{constante}$. Si $\mu_2 = 0.2\mu_1 + b$, entonces $1 = 0.2(50) + b \implies b=-9$. La relación es $\mathbf{X_2 = 0.2X_1 - 9}$.

El punto $\mathbf{x}_{\text{anom}}$ **no cae en este subespacio lineal**. Si $X_1=52$, $X_2$ debería ser $0.2(52) - 9 = 1.4$. El punto es $(52, 1.5)$, que viola la dependencia lineal perfecta.

#### Solución Computacional (Python)

En la práctica, las librerías manejan esto. `scipy.stats` utiliza la pseudo-inversa o detecta la degeneración.

```python
import numpy as np
from scipy.stats import multivariate_normal

## Parámetros del modelo
mu = np.array([50, 1])
Sigma = np.array([
    [1, 0.2],
    [0.2, 0.04]
])
x_anom = np.array([52, 1.5])

## 1. Calcular la Distancia de Mahalanobis D^2
## NumPy utiliza un método de solución robusta para sistemas singulares
diff = x_anom - mu

try:
## Intento de cálculo de la inversa y D^2
    Sigma_inv = np.linalg.inv(Sigma)
    d2 = diff.T @ Sigma_inv @ diff
    print("--- CÁLCULO TRADICIONAL FALLIDO ---")
    print("El determinante es cero. La matriz es singular/degenerada.")

except np.linalg.LinAlgError:
    print("--- CÁLCULO DEGENERADO ---")

## 2. Calcular la Densidad de Probabilidad (f_X(x))
## multivariate_normal.pdf usa pseudo-inversa para rangos incompletos

## El punto (52, 1.5) NO está en el subespacio lineal X2 = 0.2*X1 - 9.
## El punto en el subespacio sería (52, 1.4).
## La densidad de un punto fuera del subespacio en una Gaussiana degenerada es CERO.

    density_anom = multivariate_normal.pdf(x_anom, mean=mu, cov=Sigma)

## Calculamos la densidad para un punto DENTRO del subespacio (para comparación)
    x_in_subspace = np.array([52, 1.4])
    density_in_subspace = multivariate_normal.pdf(x_in_subspace, mean=mu, cov=Sigma)

    print(f"Distancia D^2 (Punto {x_anom}): No computable (Fuera del Subespacio)")
    print(f"Densidad f(x_anom): {density_anom:.2e}")
    print(f"Densidad f(x_in_subspace: {density_in_subspace:.2e} (Punto {x_in_subspace})")
```

#### Interpretación en el Contexto del Problema

El determinante cero ($\det(\mathbf{\Sigma})=0$) revela una **dependencia lineal perfecta** entre la temperatura ($X_1$) y la presión ($X_2$). Esto es físicamente sospechoso (probablemente un error en el modelo o en los datos).

  * **Implicación en Nanotecnología:** La matriz de covarianza nos dice que $\mathbf{X_2}$ (presión) es exactamente $0.2$ veces la variación de $\mathbf{X_1}$ (temperatura). El punto de anomalía $(52, 1.5)$ está **fuera** de la línea de operación normal $X_2 = 0.2X_1 - 9$.
  * La densidad de probabilidad calculada es **cero** ($0.00$), lo cual es la respuesta matemática correcta para un punto fuera del soporte de una distribución degenerada. Esto confirma que el evento $(52, 1.5)$ es **imposible** bajo el modelo actual, lo que es una fuerte señal de una **falla de sensor o una fuga catastrófica** que rompió la relación normal de control.

### Conclusión

Comprender esta técnica es crucial para el mundo real, especialmente en sistemas donde no podemos permitirnos fallos:

Identificación de "Sorpresas": La distancia de Mahalanobis nos da una puntuación de rareza. Si esa puntuación es alta, es una señal de que algo se está comportando de manera anómala o diferente a lo esperado.

Monitoreo Inteligente: Esta capacidad es vital para controlar procesos complejos como la fabricación de materiales a nivel nanométrico o en la supervisión de grandes plantas industriales.

Ejemplos de Fallos: Permite identificar rápidamente desviaciones críticas—por ejemplo, si la presión y la temperatura suben juntas de una forma que nunca antes habían hecho, indicando un fallo inminente en el equipo o un defecto en el producto.

### 11. Transformación Lineal de la Covarianza (Python)
El vector $\mathbf{X}$ tiene $\mathbf{\Sigma}_{\mathbf{X}} = \begin{pmatrix} 4 & 1 \\ 1 & 2 \end{pmatrix}$. Se aplica la transformación lineal $\mathbf{Y} = \mathbf{A}\mathbf{X}$ con $\mathbf{A} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.
**Tarea (Python):**
**Calcule la nueva matriz de covarianza $\mathbf{\Sigma}_{\mathbf{Y}} = \mathbf{A}\mathbf{\Sigma}_{\mathbf{X}}\mathbf{A}^T$** usando operaciones matriciales de `numpy`.

#### Solución Analítica

La nueva matriz de covarianza es:
$$\mathbf{\Sigma}_{\mathbf{Y}} = \mathbf{A}\mathbf{\Sigma}_{\mathbf{X}}\mathbf{A}^T$$
Donde $\mathbf{A}^T = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$.

1.  **Cálculo de $\mathbf{B} = \mathbf{A}\mathbf{\Sigma}_{\mathbf{X}}$:**
  $$\mathbf{B} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 4 & 1 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} (1)(4)+(1)(1) & (1)(1)+(1)(2) \\ (0)(4)+(1)(1) & (0)(1)+(1)(2) \end{pmatrix} = \begin{pmatrix} 5 & 3 \\ 1 & 2 \end{pmatrix}$$

2.  **Cálculo de $\mathbf{\Sigma}_{\mathbf{Y}} = \mathbf{B}\mathbf{A}^T$:**
  $$\mathbf{\Sigma}_{\mathbf{Y}} = \begin{pmatrix} 5 & 3 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} (5)(1)+(3)(1) & (5)(0)+(3)(1) \\ (1)(1)+(2)(1) & (1)(0)+(2)(1) \end{pmatrix} = \begin{pmatrix} \mathbf{8} & \mathbf{3} \\ \mathbf{3} & \mathbf{2} \end{pmatrix}$$

#### Solución Computacional (Python)

```python
import numpy as np

## Matrices dadas
Sigma_x = np.array([
    [4, 1],
    [1, 2]
])
A = np.array([
    [1, 1],
    [0, 1]
])

## 1. Calcular la transpuesta de A
A_T = A.T

## 2. Calcular Sigma_Y = A * Sigma_X * A^T (usando el operador @ para multiplicación matricial)
Sigma_y = A @ Sigma_x @ A_T

print("Matriz de Covarianza Inicial (Sigma_X):\n", Sigma_x)
print("\nMatriz de Transformación (A):\n", A)
print("\nMatriz de Covarianza Transformada (Sigma_Y = A * Sigma_X * A^T):\n", Sigma_y)
```

#### Interpretación en el Contexto del Problema

La matriz de covarianza transformada es $\mathbf{\Sigma}_{\mathbf{Y}} = \begin{pmatrix} 8 & 3 \\ 3 & 2 \end{pmatrix}$.

  * **Variables de $Y$:** $Y_1 = X_1 + X_2$ (la suma de las variables originales) y $Y_2 = X_2$ (la segunda variable sin cambios).
  * **Implicación en Nanotecnología:** La transformación lineal ha **aumentado la varianza** de la primera componente, $\text{Var}(Y_1) = 8$ (antes la varianza era 4 y 2, respectivamente, pero la covarianza de 1 influyó), y ha introducido una **fuerte correlación positiva** $\text{Cov}(Y_1, Y_2)=3$. La transformación $Y_1 = X_1 + X_2$ mezcla la incertidumbre de ambas variables originales, resultando en una mayor dispersión general. Los ingenieros deben entender cómo la combinación de las mediciones amplifica o atenúa la incertidumbre inicial del sistema.

### Conclusión

Lo que aprendí al trabajar con la transformación lineal de la covarianza es que las operaciones matemáticas que le hacemos a un grupo de números (variables) no solo cambian sus valores, sino que también afectan su relación y su dispersión (qué tan separados están).

Cada paso que doy en el cálculo tiene un efecto directo y predecible sobre la variabilidad y la interdependencia de los datos, lo cual es vital para construir modelos científicos que sean robustos y confiables.

### 12. Demostración de Semidefinida Positiva (Python) 🧐
Se propone la matriz de covarianza $\mathbf{\Sigma} = \begin{pmatrix} 5 & 2 & 1 \\ 2 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}$ para un material.
**Tarea (Python):**
Calcule los **eigenvalores** de $\mathbf{\Sigma}$ usando `numpy.linalg.eig`. **Verifique computacionalmente** que la matriz es PSD (es decir, que todos los eigenvalores son no negativos).

#### Solución Analítica (Criterio)

Una matriz simétrica $\mathbf{\Sigma}$ es **Semidefinida Positiva (PSD)** si y solo si **todos sus eigenvalores $\lambda_i$ son no negativos** ($\lambda_i \ge 0$). Físicamente, esto garantiza que la varianza de cualquier combinación lineal $\mathbf{z}^T\mathbf{X}$ es no negativa.

#### Solución Computacional (Python)

```python
import numpy as np

## Matriz propuesta
Sigma = np.array([
    [5, 2, 1],
    [2, 1, 0],
    [1, 0, 1]
])

## 1. Calcular los eigenvalores
## W contiene los eigenvalores (valores propios)
eigenvalues = np.linalg.eigvals(Sigma)

## 2. Verificar la condición PSD
is_psd = np.all(eigenvalues >= 0)

print("Matriz Sigma:\n", Sigma)
print("\nEigenvalores calculados:\n", eigenvalues)
print(f"\n¿La matriz es Semidefinida Positiva (PSD)? {is_psd}")

if is_psd:
    print("Conclusión: Sí, todos los eigenvalores son no negativos. La matriz es una matriz de covarianza válida (PSD).")
else:
    print("Conclusión: No, al menos un eigenvalor es negativo. La matriz no es una matriz de covarianza válida.")
```

#### Interpretación en el Contexto del Problema

Los eigenvalores calculados son aproximadamente $\lambda_1 \approx 5.449$, $\lambda_2 \approx 0.500$, $\lambda_3 \approx 0.051$. **Todos son no negativos**.

  * **Implicación en Nanotecnología:** La verificación PSD es fundamental. Si una matriz de covarianza no fuera PSD, implicaría que alguna **combinación lineal de las mediciones del material tiene varianza negativa**, lo cual es **físicamente imposible** (la varianza es el promedio de una cantidad al cuadrado). El resultado confirma que la matriz propuesta $\mathbf{\Sigma}$ es una descripción estadísticamente válida de la dispersión de las propiedades del material. Además, dado que $\lambda_3 > 0$, la matriz es también **Definida Positiva (PD)** y es invertible, lo que significa que no hay redundancia de información perfecta.

### Conclusión

Esta verificación actúa como un filtro de realidad para nuestros modelos estadísticos que describen materiales o procesos a escala atómica. Garantizar que la matriz es "semidefinida positiva" nos asegura dos cosas clave:

Consistencia Física y Modelos Estables

### 13. Gaussian Whitening (Python)
Utilice la matriz $\mathbf{\Sigma} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.
**Tarea (Python):**
**a) Implemente la matriz de blanqueamiento $\mathbf{W}$** (usando la descomposición de eigen $\mathbf{\Sigma} = \mathbf{V}\mathbf{D}\mathbf{V}^T$).
**b) Verifique computacionalmente** que $\mathbf{W}\mathbf{\Sigma}\mathbf{W}^T$ es la matriz identidad $\mathbf{I}$.

#### Solución Analítica (Fórmulas)

La matriz de blanqueamiento $\mathbf{W}$ se define como:
$$\mathbf{W} = \mathbf{D}^{-1/2} \mathbf{V}^T$$
Donde $\mathbf{V}$ es la matriz de eigenvectores (que diagonaliza $\mathbf{\Sigma}$) y $\mathbf{D}$ es la matriz diagonal de eigenvalores.

La verificación es:
$$\mathbf{W}\mathbf{\Sigma}\mathbf{W}^T = (\mathbf{D}^{-1/2} \mathbf{V}^T) (\mathbf{V}\mathbf{D}\mathbf{V}^T) (\mathbf{V}\mathbf{D}^{-1/2})$$
$$= \mathbf{D}^{-1/2} \mathbf{V}^T \mathbf{V} \mathbf{D} \mathbf{V}^T \mathbf{V} \mathbf{D}^{-1/2}$$
$$= \mathbf{D}^{-1/2} \mathbf{I} \mathbf{D} \mathbf{I} \mathbf{D}^{-1/2} = \mathbf{D}^{-1/2} \mathbf{D} \mathbf{D}^{-1/2} = \mathbf{I}$$

#### Solución Computacional (Python)

```python
import numpy as np

## Matriz de Covarianza
Sigma = np.array([
    [2, 1],
    [1, 2]
])

## 1. Descomposición de eigen (V: eigenvectores, D_diag: eigenvalores)
## La función devuelve (eigenvalores, eigenvectores)
D_diag, V = np.linalg.eig(Sigma)

## 2. Construir D^(-1/2) (raíz cuadrada inversa de la matriz diagonal de eigenvalores)
D_inv_sqrt = np.diag(1.0 / np.sqrt(D_diag))

## 3. Implementar la matriz de Blanqueamiento W
## W = D^(-1/2) * V^T
## Nota: La convención de numpy es que las columnas de V son los eigenvectores.
W = D_inv_sqrt @ V.T

print("Matriz de Covarianza Sigma:\n", Sigma)
print("\nMatriz de Blanqueamiento W:\n", W)

## 4. Verificación computacional: Sigma_Z = W * Sigma * W^T
Sigma_z = W @ Sigma @ W.T

print("\nMatriz de Covarianza Blanqueada (Sigma_Z = W * Sigma * W^T):\n", Sigma_z)

## Verificación de que Sigma_z es aproximadamente la matriz identidad I
identity_matrix = np.eye(2)
is_identity = np.allclose(Sigma_z, identity_matrix)

print(f"\n¿El resultado es la matriz identidad I? {is_identity}")
```

#### Interpretación en el Contexto del Problema

El resultado $\mathbf{\Sigma}_{\mathbf{Z}} \approx \mathbf{I}$ verifica que la transformación de blanqueamiento es exitosa.

  * **Implicación en Nanotecnología:** El blanqueamiento (o *whitening*) se usa para transformar datos correlacionados $(\mathbf{X})$ en datos descorrelacionados con varianza unitaria $(\mathbf{Z})$.
      * **$\mathbf{\Sigma}_{\mathbf{Z}}$ es diagonal:** $\text{Cov}(Z_1, Z_2)=0$. Las nuevas variables $Z_1$ y $Z_2$ son **independientes** (si $\mathbf{X}$ era Gaussiana). Esto elimina la redundancia de información.
      * **Diagonal son unos:** $\text{Var}(Z_1)=\text{Var}(Z_2)=1$. Esto significa que la incertidumbre de ambas variables es la misma, evitando que algoritmos posteriores (como clasificadores o modelos de ML) den importancia indebida a la variable con mayor varianza original. El blanqueamiento es un pre-procesamiento estándar en *Machine Learning* aplicado a datos de caracterización de materiales.

### Conclusión

En esencia, dominar el 'Gaussian Whitening' me equipa con la habilidad de ir más allá de la simple observación de datos, permitiéndome descubrir las verdaderas relaciones ocultas en las complejas mediciones de la nanociencia para optimizar los procesos de producción y avanzar en la investigación.

## IV. Análisis de Componentes Principales (PCA) (5.8)

### 14. PCA: Varianza Explicada (Datos de Sensores) 📊
Se analizan 4 mediciones de un sensor. La matriz de covarianza estandarizada tiene los siguientes eigenvalores: $\lambda_1=2.8$, $\lambda_2=0.7$, $\lambda_3=0.3$, $\lambda_4=0.2$.
**Tarea (Python):**
**a) Calcule la varianza total** (traza).
**b) Calcule el porcentaje de varianza explicada acumulada** por los dos primeros componentes principales ($PC_1$ y $PC_2$).

#### Solución Analítica

1.  **Varianza Total:** La varianza total es la suma de las varianzas de las variables originales, que es igual a la suma de los eigenvalores (la traza de $\mathbf{\Sigma}$).
  $$\text{Varianza Total} = \sum_{i=1}^{4} \lambda_i = 2.8 + 0.7 + 0.3 + 0.2 = \mathbf{4.0}$$
    *(Dado que la matriz de covarianza fue estandarizada, la varianza total es igual al número de variables, $p=4$)*.

2.  **Varianza Explicada por $PC_1$ y $PC_2$:**
    $$\text{Varianza Explicada Acumulada} = \lambda_1 + \lambda_2 = 2.8 + 0.7 = \mathbf{3.5}$$

3.  **Porcentaje Acumulado:**
    $$\text{Porcentaje Acumulado} = \frac{\lambda_1 + \lambda_2}{\text{Varianza Total}} \times 100\% = \frac{3.5}{4.0} \times 100\% = \mathbf{87.5\%}$$

#### Solución Computacional (Python) mejorado por Claude

```python
import numpy as np
import matplotlib.pyplot as plt

## Eigenvalores dados (ya ordenados de mayor a menor)
eigenvalues = np.array([2.8, 0.7, 0.3, 0.2])
n_components = len(eigenvalues)

## =========================
## CÁLCULOS BÁSICOS
## =========================
total_variance = np.sum(eigenvalues)
explained_variance_ratio = eigenvalues / total_variance
cumulative_variance_ratio = np.cumsum(explained_variance_ratio)

## Varianza explicada por PC1 + PC2
explained_variance_pc1_pc2 = np.sum(eigenvalues[0:2])
cumulative_ratio_pc2 = cumulative_variance_ratio[1]

## =========================
## RESULTADOS
## =========================
print("="*70)
print("ANÁLISIS DE COMPONENTES PRINCIPALES (PCA)")
print("="*70)
print(f"\nEigenvalores: {eigenvalues}")
print(f"\na) Varianza Total (Traza de Σ): {total_variance:.1f}")
print(f"   (Nota: Para matriz estandarizada, traza = # variables = {n_components})")
print(f"\nb) Varianza Explicada por PC1+PC2: {explained_variance_pc1_pc2:.1f}")
print(f"   Porcentaje Acumulado: {cumulative_ratio_pc2*100:.1f}%")

## Tabla detallada
print("\n" + "-"*70)
print(f"{'PC':<6} {'Eigenvalor':<12} {'% Varianza':<15} {'% Acumulado':<15}")
print("-"*70)
for i in range(n_components):
    print(f"PC{i+1:<4} {eigenvalues[i]:<12.1f} "
          f"{explained_variance_ratio[i]*100:<15.1f} "
          f"{cumulative_variance_ratio[i]*100:<15.1f}")
print("="*70)
## (Añadir aquí las visualizaciones del punto 1)
```

#### Interpretación en el Contexto del Problema

Los dos primeros Componentes Principales ($PC_1$ y $PC_2$) explican el **$87.5\%$ de la varianza total** del sistema de sensores.

  * **Implicación en Nanotecnología:** Este alto porcentaje justifica la **reducción de la dimensionalidad** de 4 a 2. El ingeniero puede ahora modelar la variabilidad del sensor utilizando solo dos variables ($PC_1$ y $PC_2$) en lugar de las cuatro originales, simplificando los modelos, acelerando el procesamiento y eliminando gran parte del ruido (que suele estar asociado a los PCs de baja varianza, $\lambda_3$ y $\lambda_4$).

### Conclusión

En resumen: El PCA no solo simplifica los números, sino que nos da una visión clara y enfocada de lo que impulsa el rendimiento de cualquier sistema nanotecnológico, permitiendo una toma de decisiones más ágil y precisa.

### 15. PCA: Eigenvector y Cargas (Python)
Para los datos del Problema 14, el eigenvector asociado a $\lambda_1=2.8$ es $\mathbf{v}_1 = (0.55, 0.55, 0.45, 0.45)^T$.
**Tarea (Python):**
**a) Normalice $\mathbf{v}_1$** (calcule $\mathbf{v}_1/\|\mathbf{v}_1\|$).
**b) Cree un gráfico de barras** que muestre la contribución (cargas absolutas) de cada variable original $X_1, X_2, X_3, X_4$ al $PC_1$.

#### Solución Analítica (Normalización)

Un eigenvector debe tener una norma euclidiana (longitud) de 1.
$$\|\mathbf{v}_1\| = \sqrt{0.55^2 + 0.55^2 + 0.45^2 + 0.45^2} = \sqrt{0.3025 + 0.3025 + 0.2025 + 0.2025} = \sqrt{1.01}$$
El valor correcto es $\sqrt{1.01} \approx 1.005$. El vector dado ya está **casi normalizado**.

El vector normalizado $\mathbf{u}_1$ es:
$$\mathbf{u}_1 = \frac{\mathbf{v}_1}{\|\mathbf{v}_1\|} \approx (0.547, 0.547, 0.448, 0.448)^T$$

#### Solución Computacional (Python)

```python
import numpy as np
import matplotlib.pyplot as plt

## Eigenvector no normalizado dado
v1 = np.array([0.55, 0.55, 0.45, 0.45])
variable_names = ['X1', 'X2', 'X3', 'X4']

## 1. Normalización del eigenvector (u1)
norm_v1 = np.linalg.norm(v1)
u1 = v1 / norm_v1

print(f"Vector v1 dado: {v1}")
print(f"Norma de v1: {norm_v1:.4f}")
print(f"a) Eigenvector Normalizado (u1):\n{u1}")

## 2. Cargas (Contribuciones Absolutas)
## Las cargas son los elementos del eigenvector. Usamos el valor absoluto para la magnitud.
loadings = np.abs(u1)

print("\nCargas (Contribución) al PC1:")
for name, load in zip(variable_names, loadings):
    print(f"  {name}: {load:.4f}")

## 3. Graficar las cargas
plt.figure(figsize=(7, 5))
plt.bar(variable_names, loadings, color=['blue', 'blue', 'red', 'red'], edgecolor='black')
plt.title('Contribución de Variables al Primer Componente Principal (PC1)')
plt.xlabel('Variable Original del Sensor')
plt.ylabel('Magnitud de la Carga (Valor Absoluto)')
plt.grid(axis='y', linestyle='--')
plt.show()
```

#### Interpretación en el Contexto del Problema

Las cargas del $PC_1$ son: $X_1\approx 0.547$, $X_2\approx 0.547$, $X_3\approx 0.448$, $X_4\approx 0.448$.

  * **Implicación en Nanotecnología:** El $PC_1$, que es el eje de máxima varianza, está dominado por las variables $\mathbf{X_1}$ y $\mathbf{X_2}$.
      * **$PC_1 \propto (X_1 + X_2)$:** La principal fuente de variación en el sistema de sensores es un **efecto combinado** de las mediciones $X_1$ y $X_2$. Esto podría significar que estas dos variables miden el mismo fenómeno físico subyacente (por ejemplo, el tamaño de la partícula) de maneras ligeramente diferentes.
      * **Control de Calidad:** Para el control de calidad, es más eficiente monitorear el valor de $PC_1$ que monitorear $X_1$ y $X_2$ por separado, ya que $PC_1$ resume la mayor parte de la información relevante.

### Conclusión

El PCA me equipa para ser un analista de datos más eficiente y tomar decisiones fundamentadas que aceleren el desarrollo y la producción fiable de nanomateriales.

### 16. PCA: Proyección de un Punto (Python)
Utilice la matriz de datos estandarizada $\mathbf{D}_{\text{estandarizada}}$ del Problema 9. Los primeros dos eigenvectores de $\mathbf{S}$ son: $\mathbf{v}_1$ y $\mathbf{v}_2$.
**Tarea (Python):**
**a) Use `sklearn.decomposition.PCA`** para encontrar $\mathbf{v}_1$ y $\mathbf{v}_2$.
**b) Proyecte la primera fila de datos** $\mathbf{x}_{\text{1}}$ en el subespacio de los dos PCs, calculando $\mathbf{x}_{\text{proyectada}} = \mathbf{x}_{\text{1}} \cdot \begin{pmatrix} \mathbf{v}_1 & \mathbf{v}_2 \end{pmatrix}$.

#### Solución Analítica (Fórmulas)

La matriz de datos $\mathbf{D}$ es:
$$\mathbf{D} = \begin{pmatrix} 7.5 & 8.2 & 0.5 \\ 8.0 & 7.9 & 0.4 \\ 7.2 & 8.5 & 0.6 \\ 7.8 & 8.0 & 0.5 \\ 8.1 & 8.3 & 0.3 \end{pmatrix}$$
La proyección de un punto $\mathbf{x}$ en el nuevo subespacio es $\mathbf{z} = \mathbf{x}\mathbf{V}_k$, donde $\mathbf{V}_k$ es la matriz de los $k$ principales eigenvectores. Aquí $k=2$.

#### Solución Computacional (Python) mejorado por Claude

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

## Datos del Problema 9
data_matrix = np.array([
    [7.5, 8.2, 0.5],
    [8.0, 7.9, 0.4],
    [7.2, 8.5, 0.6],
    [7.8, 8.0, 0.5],
    [8.1, 8.3, 0.3]
])
feature_names = ['Dureza', 'Adherencia', 'Rugosidad']

print("=== EJERCICIO 16: PROYECCIÓN PCA ===\n")

## 1. Estandarización
scaler = StandardScaler()
data_standardized = scaler.fit_transform(data_matrix)

print("Matriz de datos estandarizada:")
print(data_standardized)
print(f"\nMedia de datos estandarizados: {data_standardized.mean(axis=0)}")
print(f"Desv. estándar de datos estand.: {data_standardized.std(axis=0, ddof=1)}")

## 2. PCA con 2 componentes
pca = PCA(n_components=2)
pca.fit(data_standardized)

## a) Eigenvectores
V_k = pca.components_.T  # (3, 2): columnas son v1, v2

print("\n--- a) EIGENVECTORES ---")
print(f"Forma de V_k: {V_k.shape}")
print(f"\nEigenvector v1 (PC1):\n{pca.components_[0]}")
print(f"\nEigenvector v2 (PC2):\n{pca.components_[1]}")

## Varianza explicada
print(f"\nVarianza explicada:")
print(f"  PC1: {pca.explained_variance_ratio_[0]:.2%}")
print(f"  PC2: {pca.explained_variance_ratio_[1]:.2%}")
print(f"  Total: {pca.explained_variance_ratio_.sum():.2%}")

## Interpretación de eigenvectores
print("\nInterpretación de PC1:")
for name, coef in zip(feature_names, pca.components_[0]):
    print(f"  {name}: {coef:+.3f}")

## b) Proyección de x1
x1_standardized = data_standardized[0]
z1_projected = x1_standardized @ V_k

print("\n--- b) PROYECCIÓN DE x1 ---")
print(f"x1 original: {data_matrix[0]}")
print(f"x1 estandarizado: {x1_standardized}")
print(f"z1 proyectado (PC1, PC2): {z1_projected}")

## Verificación usando sklearn
z1_sklearn = pca.transform(data_standardized[0].reshape(1, -1))
print(f"Verificación (sklearn.transform): {z1_sklearn[0]}")
print(f"Diferencia: {np.linalg.norm(z1_projected - z1_sklearn[0]):.2e}")

## 3. Visualización
all_projected = pca.transform(data_standardized)

fig, ax = plt.subplots(figsize=(10, 7))

## Todas las muestras
ax.scatter(all_projected[:, 0], all_projected[:, 1],
           s=150, alpha=0.6, c='steelblue', edgecolors='black',
           label='Muestras de recubrimiento')

## Anotar muestras
for i, (x, y) in enumerate(all_projected):
    ax.annotate(f'M{i+1}', (x, y), xytext=(5, 5),
                textcoords='offset points', fontsize=10)

## Primera muestra destacada
ax.scatter(z1_projected[0], z1_projected[1],
           s=300, c='red', marker='*',
           label='M1 (primera muestra)', zorder=5,
           edgecolors='darkred', linewidths=2)

## Ejes de referencia
ax.axhline(0, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)
ax.axvline(0, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)

ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%} de varianza)',
              fontsize=12)
ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%} de varianza)',
              fontsize=12)
ax.set_title('Proyección de Recubrimientos en Subespacio PCA (2D)',
             fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()

## 4. Reconstrucción (información adicional)
x1_reconstructed_std = z1_projected @ V_k.T
x1_reconstructed = scaler.inverse_transform(x1_reconstructed_std.reshape(1, -1))

print("\n--- RECONSTRUCCIÓN ---")
print(f"x1 reconstruido (estandarizado): {x1_reconstructed_std}")
print(f"x1 reconstruido (escala original): {x1_reconstructed[0]}")
print(f"x1 original: {data_matrix[0]}")
print(f"Error de reconstrucción: {np.linalg.norm(data_matrix[0] - x1_reconstructed[0]):.4f}")
```

#### Interpretación en el Contexto del Problema

La proyección del primer punto en el subespacio 2D de los Componentes Principales es el vector $\mathbf{z}_1$.

  * **Implicación en Nanotecnología:** La proyección transforma la muestra de recubrimiento (definida por 3 propiedades $\mathbf{x}_1$) en un nuevo punto en un espacio 2D ($\mathbf{z}_1$).
      * **$\mathbf{z}_1$** ahora contiene la **información más importante** sobre ese punto de datos (Dureza, Adherencia, Rugosidad) en solo dos coordenadas.
      * Esto es esencial para la **visualización y análisis de clústeres** (agrupamientos) de diferentes lotes de materiales, permitiendo al ingeniero ver rápidamente la posición de este recubrimiento respecto a las tendencias generales de variabilidad del sistema. La distancia del origen en el espacio de PCs refleja cuánto se desvía el material de la media de la producción.

### Conclusión

El ejercicio práctico de Análisis de Componentes Principales (PCA), en particular la proyección de puntos, ha sido una revelación fundamental para mi carrera. En el campo de la nanotecnología, a menudo lidiamos con datos extremadamente complejos provenientes de caracterizaciones —pensemos en la composición química, el tamaño de nanopartículas y sus propiedades ópticas, todo a la vez.

### 17. PCA: Reconstrucción de Imagen (Eigenfaces en Espectros) 🖼️
Imagine que un "espectro promedio" es la media de las filas de una matriz de datos $5 \times 500$ (500 longitudes de onda, 5 muestras). PCA se usa en esta matriz de datos.
**Tarea (Python):**
**Simule una matriz de datos $5 \times 500$** con una señal fuerte en la primera dimensión (e.g., $X_1 \propto X_2$) y ruido en el resto. **Aplique PCA con `n_components=1`**. **Reconstruya la matriz de datos** $\mathbf{D}_{\text{recons}}$ y calcule el error de reconstrucción (Frobenius norm).

#### Solución Computacional (Python)

```python
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

## Parámetros de la simulación
N_samples = 5    # Número de espectros (filas)
P_features = 500 # Número de longitudes de onda (columnas)

## 1. Simulación de la Matriz de Datos (D)
np.random.seed(42)
## Generar la señal principal (alta correlación)
signal = np.random.normal(0, 1, size=(N_samples, 20)) # Las primeras 20 columnas son señal

## Generar el ruido de fondo (las 480 columnas restantes)
noise = np.random.normal(0, 0.1, size=(N_samples, P_features - 20))

## Construir la matriz de datos (D)
D = np.hstack([signal, noise])

## 2. Estandarización de los datos (Centrado en la media)
## PCA se realiza sobre la matriz centrada para encontrar eigenvectores de la covarianza
D_scaled = StandardScaler().fit_transform(D)

## 3. Aplicar PCA con k=1
pca = PCA(n_components=1)
D_projected = pca.fit_transform(D_scaled) # Proyección (puntos en el subespacio 1D)

## 4. Reconstrucción de la Matriz (D_recons)
## D_recons = (D_projected @ V_k.T) + mean_vector
D_recons_scaled = pca.inverse_transform(D_projected) # Reconstrucción en el espacio estandarizado

## 5. Cálculo del Error de Reconstrucción (Frobenius Norm)
## Mide la diferencia total entre la matriz original centrada y la reconstruida
error_matrix = D_scaled - D_recons_scaled
error_frobenius = np.linalg.norm(error_matrix, ord='fro')

print("--- Análisis PCA para Espectros ---")
print(f"Dimensiones de la matriz original (N x P): {D.shape}")
print(f"Varianza Explicada por PC1: {pca.explained_variance_ratio_[0]*100:.2f}%")
print(f"Dimensiones de la matriz proyectada (N x k): {D_projected.shape}")
print(f"Dimensiones de la matriz reconstruida: {D_recons_scaled.shape}")
print(f"\nError de Reconstrucción (Norma de Frobenius): {error_frobenius:.2f}")
```

#### Interpretación en el Contexto del Problema

Al usar solo $PC_1$, la varianza explicada debería ser muy alta (más del $85\%$), y el error de reconstrucción (Norma de Frobenius) será pequeño.

  * **Implicación en Nanotecnología:** Esto simula el uso de **Eigenfaces/Eigen-Espectros**. Cada columna del eigenvector es un "Eigen-Espectro" (la tendencia fundamental de variación). Al reconstruir el espectro usando solo $PC_1$, estamos **filtrando el ruido** que reside en los componentes de varianza baja (PCs 2, 3, 4, 5). El bajo error de reconstrucción (norma de Frobenius pequeña) significa que la mayor parte de la señal física real del espectro fue capturada por el $PC_1$. Esto es esencial para el **reconocimiento de patrones** y la eliminación de ruido en datos de alta dimensión (FTIR, Raman, etc.).

### Conclusión

Este trabajo demuestra que el uso de métodos como el Análisis de Componentes Principales (PCA) no es solo un truco matemático, sino una herramienta vital para estudiar materiales a escala nanométrica. Al reconstruir espectros con PCA, logramos separar la señal importante del "ruido" (datos irrelevantes o errores de medición). Es como enfocar una cámara borrosa: de repente, se ve clara la información esencial sobre cómo se comportan los nanoestructuras.

### 18. PCA: Comparación de Covarianza vs. Correlación (Python)
Genere un conjunto de datos $2\text{D}$ donde $X_1$ tiene una varianza muy grande (e.g., $100$) y $X_2$ muy pequeña (e.g., $1$), con correlación $\rho=0.5$.
**Tarea (Python):**
**a) Aplique PCA a los datos sin escalar** y calcule la varianza explicada.
**b) Aplique PCA a los datos después de escalarlos** (estandarización) y recalcule la varianza explicada. **Compare** los resultados y explique el impacto de la escala.

#### Solución Computacional (Python)

```python
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

## Parámetros
N = 1000
mu = np.array([0, 0])
Sigma_high_var = np.array([
    [100, 5],  # Var(X1)=100, Cov=5. (rho=5/sqrt(100*1)=0.5)
    [5, 1]     # Var(X2)=1
])

## Generar datos
D_high_var = np.random.multivariate_normal(mu, Sigma_high_var, size=N)

print("--- Comparación de PCA (Sin Escalar vs. Estandarizado) ---")

## 1. PCA SIN ESCALAR (Basado en la Matriz de Covarianza)
pca_unscaled = PCA(n_components=2)
pca_unscaled.fit(D_high_var)

exp_ratio_unscaled = pca_unscaled.explained_variance_ratio_
print(f"a) PCA SIN ESCALAR: PC1 explica {exp_ratio_unscaled[0]*100:.2f}% de la varianza.")
print(f"   (PC1 capta casi toda la varianza de X1)")

## 2. PCA CON ESCALADO (Basado en la Matriz de Correlación)
scaler = StandardScaler()
D_scaled = scaler.fit_transform(D_high_var) # Estandariza a media 0, varianza 1

pca_scaled = PCA(n_components=2)
pca_scaled.fit(D_scaled)

exp_ratio_scaled = pca_scaled.explained_variance_ratio_
print(f"\nb) PCA CON ESCALADO: PC1 explica {exp_ratio_scaled[0]*100:.2f}% de la varianza.")
print(f"   (La varianza se distribuye de forma más equitativa)")
```

#### Interpretación en el Contexto del Problema

La **escala de las variables** domina el análisis PCA.

  * **PCA Sin Escalar (Problema de Unidades):** El $PC_1$ explica casi el **$100\%$ de la varianza**. Esto se debe a que la varianza de $X_1$ (100) es 100 veces mayor que la de $X_2$ (1). PCA simplemente alinea el $PC_1$ con el eje $X_1$, ignorando la estructura de $X_2$. En Nanotecnología, si $X_1$ es "longitud en Å" y $X_2$ es "rugosidad en nm", la variable con la escala de unidades mayor dominará.
  * **PCA Con Escalado (Solución):** Al estandarizar, ambas variables tienen varianza 1. El $PC_1$ ahora explica aproximadamente **$75\%$ de la varianza**. El resto ($25\%$) es explicado por $PC_2$. El PCA con escalado revela la verdadera estructura de correlación de los datos.

**Conclusión:** Para la Ciencia de Materiales, donde las variables pueden tener unidades y rangos drásticamente diferentes (eV, nm, GPa, $\text{mol/L}$), es **obligatorio estandarizar** los datos antes de aplicar PCA.

### Conclusión

En definitiva, aprender a preparar correctamente los datos es la diferencia entre obtener una interpretación errónea que nos haga perder tiempo y recursos, y lograr un descubrimiento real y preciso a nivel nanométrico.

## V. Problemas Integrales y Aplicaciones Avanzadas

### 19. Análisis de la Descorrelación de un Recubrimiento 🧱
La resistencia al impacto ($X_1$) y la dureza ($X_2$) de un recubrimiento tienen $\mathbf{\mu} = \begin{pmatrix} 10 \\ 5 \end{pmatrix}$ y $\mathbf{\Sigma} = \begin{pmatrix} 2 & -1.5 \\ -1.5 & 3 \end{pmatrix}$.
**Tarea (Python):**
**a) Calcule los eigenvectores** de $\mathbf{\Sigma}$.
**b) Use los eigenvectores para rotar el sistema de coordenadas**. Calcule la matriz de covarianza en el nuevo sistema de coordenadas $\mathbf{\Sigma}_{\text{rotada}}$. **Verifique** que $\mathbf{\Sigma}_{\text{rotada}}$ es diagonal.

#### Solución Analítica (Fórmulas)

La rotación de coordenadas se realiza mediante la matriz de eigenvectores $\mathbf{V}$. Si $\mathbf{Z} = \mathbf{V}^T \mathbf{X}$, la nueva matriz de covarianza es:
$$\mathbf{\Sigma}_{\mathbf{Z}} = \mathbf{V}^T \mathbf{\Sigma} \mathbf{V} = \mathbf{\Lambda}$$
Donde $\mathbf{\Lambda}$ es la matriz diagonal de eigenvalores. Este proceso **descorrela** las variables, y la varianza de las nuevas variables $Z_i$ es exactamente el eigenvalor $\lambda_i$.

#### Solución Computacional (Python)

```python
import numpy as np

## Matriz de Covarianza
Sigma = np.array([
    [2, -1.5],
    [-1.5, 3]
])

## 1. Calcular los eigenvalores (Lambda) y eigenvectores (V)
## V tiene los eigenvectores como COLUMNAS
Lambda_diag, V = np.linalg.eig(Sigma)

## 2. Construir la matriz diagonal Lambda a partir de los eigenvalores
Lambda_matrix = np.diag(Lambda_diag)

## 3. Calcular la matriz de covarianza rotada (Sigma_rotada)
## Sigma_rotada = V^T @ Sigma @ V
Sigma_rotada = V.T @ Sigma @ V

print("Matriz de Covarianza Inicial (Sigma):\n", Sigma)
print(f"\nEigenvalores (Lambda_diag): {Lambda_diag}")
print("Matriz de Eigenvectores (V):\n", V)
print(f"\nMatriz Diagonal de Eigenvalores (Lambda_matrix):\n{Lambda_matrix.round(4)}")
print(f"\nMatriz de Covarianza Rotada (Sigma_rotada = V^T * Sigma * V):\n{Sigma_rotada.round(4)}")

## Verificación de que Sigma_rotada es diagonal (cercana a Lambda_matrix)
is_diagonal = np.allclose(Sigma_rotada, Lambda_matrix)
print(f"\n¿Sigma_rotada es diagonal? {is_diagonal}")
```

#### Interpretación en el Contexto del Problema

La matriz $\mathbf{\Sigma}_{\text{rotada}}$ es diagonal, con entradas que son los eigenvalores $\lambda_1 \approx 4.19$ y $\lambda_2 \approx 0.81$.

  * **Implicación en Nanotecnología:** La correlación negativa original entre resistencia ($X_1$) y dureza ($X_2$) ha desaparecido en el nuevo sistema de coordenadas ($Z_1, Z_2$).
      * **$Z_1$ (PC1)** es una combinación de $X_1$ y $X_2$ que tiene una varianza de **4.19** (el eje de mayor variación).
      * **$Z_2$ (PC2)** es una combinación ortogonal que tiene una varianza de **0.81**.
  * El análisis confirma que al rotar el sistema de coordenadas por $\mathbf{V}$, se obtiene un nuevo conjunto de propiedades ($\mathbf{Z}$) que son **estadísticamente independientes** (su covarianza es cero). Esto simplifica el modelado físico, ya que la incertidumbre de $Z_1$ no afecta a la incertidumbre de $Z_2$.

### Conclusión

Este ejercicio demuestra cómo la descorrelación mediante eigenvectores permite transformar variables dependientes en componentes independientes, facilitando el análisis y modelado de propiedades de materiales.

### 20. Simulación de Control de Calidad Multivariado (Python) 🏭
Utilice la distribución $\mathcal{N}(\mathbf{\mu}, \mathbf{\Sigma})$ del Problema 19. El control de calidad (QC) rechaza el lote si la medición cae en el $5\%$ menos probable.
**Tarea (Python):**
**Simule $N=1000$ puntos**. Calcule la **Distancia de Mahalanobis $\mathbf{D}^2$** para cada punto. Determine el umbral $\mathbf{D}^2_{\text{umbral}}$ que corresponde al cuantil 0.95 (el $5\%$ más atípico) de la distribución muestral de $\mathbf{D}^2$.

#### Solución Analítica (Fórmulas)

La distancia de Mahalanobis al cuadrado $\mathbf{D}^2$ de un vector Gaussiano $\mathbf{X} \sim \mathcal{N}(\mathbf{\mu}, \mathbf{\Sigma})$ sigue una **distribución Chi-cuadrado ($\chi^2$)** con $p$ grados de libertad, donde $p$ es la dimensión del vector. Aquí $p=2$.

$$\mathbf{D}^2 \sim \chi^2_p$$

El umbral del $5\%$ se calcula usando el cuantil 0.95 de la $\chi^2_2$.

#### Solución Computacional (Python)

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2, kstest
from scipy.spatial.distance import mahalanobis

## Parámetros (del Problema 19)
np.random.seed(42)
mu = np.array([10, 5])
Sigma = np.array([[2, -1.5], [-1.5, 3]])
N = 1000
p = 2  # Dimensionalidad

print(f"Parámetros del proceso:")
print(f"  μ = {mu}")
print(f"  Σ =\n{Sigma}")
print(f"  Correlación: ρ = {Sigma[0,1]/np.sqrt(Sigma[0,0]*Sigma[1,1]):.3f}\n")

## 1. Simular datos
X_samples = np.random.multivariate_normal(mu, Sigma, size=N)

## 2. Calcular D² (VECTORIZADO)
Sigma_inv = np.linalg.inv(Sigma)
X_centered = X_samples - mu
d2_samples = np.sum(X_centered @ Sigma_inv * X_centered, axis=1)

## 3. Umbrales
d2_threshold_theoretical = chi2.ppf(0.95, df=p)
d2_threshold_simulated = np.percentile(d2_samples, 95)

print(f"--- UMBRALES DE CONTROL ---")
print(f"Nivel de confianza: 95% (rechazar 5% más extremo)")
print(f"Umbral teórico (χ²(2), q=0.95): {d2_threshold_theoretical:.4f}")
print(f"Umbral simulado (percentil 95): {d2_threshold_simulated:.4f}")
print(f"Diferencia: {abs(d2_threshold_theoretical - d2_threshold_simulated):.4f}")

## 4. Pruebas de bondad de ajuste
ks_stat, ks_pval = kstest(d2_samples, 'chi2', args=(p,))
print(f"\n--- BONDAD DE AJUSTE ---")
print(f"Test KS: estadístico={ks_stat:.4f}, p-valor={ks_pval:.4f}")
print(f"Conclusión: {'Ajuste adecuado' if ks_pval > 0.05 else 'Ajuste pobre'} a χ²({p})")
```

#### Interpretación en el Contexto del Problema

El umbral teórico y simulado de $\mathbf{D}^2$ es de aproximadamente **5.99**.

  * **Implicación en Nanotecnología:** Cualquier nueva medición de resistencia y dureza que resulte en una $\mathbf{D}^2 > 5.99$ debe ser **rechazada** como una muestra atípica. La distancia de Mahalanobis proporciona un criterio de control de calidad que considera **conjuntamente** la variación y la correlación de las variables. Esto es mucho más robusto que usar umbrales simples de desviación estándar en cada variable, ya que respeta la forma elíptica de la distribución de los datos normales. Si una medición excede este umbral, el reactor está operando fuera de las condiciones estadísticas esperadas.

### Conclusión

Este trabajo nos ha permitido ver la utilidad de la distancia de Mahalanobis. Esta no es una simple medida de distancia, sino una herramienta estadística avanzada crucial para el control de calidad en sistemas donde hay muchas variables a la vez (multivariado).

### 21. Estimación de $E[Y|X]$ a partir de Datos (Python) 💡
Simule $N=1000$ puntos $(X_i, Y_i)$ donde $X \sim U(0, 10)$ y $Y = 5 + 2X + \epsilon$, con $\epsilon \sim \mathcal{N}(0, 1)$ (simulando una relación de eficiencia con ruido).
**Tarea (Python):**
**Estime la función de esperanza condicional $E[Y|X]$** ajustando un modelo de **regresión lineal** de $Y$ en función de $X$ a los datos simulados (`sklearn.linear_model.LinearRegression`). Imprima los coeficientes.

#### Solución Analítica

La esperanza condicional es el valor esperado de $Y$ dado $X$:
$$E[Y|X=x] = E[5 + 2x + \epsilon | X=x]$$
Dado que $\epsilon$ es ruido independiente con $E[\epsilon]=0$:
$$E[Y|X=x] = 5 + 2x + E[\epsilon] = \mathbf{5 + 2x}$$

La estimación por regresión lineal debería aproximarse a la **pendiente ($\beta_1$) de 2** y la **intersección ($\beta_0$) de 5**.

#### Solución Computacional (Python)

```python
import numpy as np
from sklearn.linear_model import LinearRegression

## Parámetros de la simulación
N = 1000
## Relación teórica: Y = 5 + 2X + epsilon

## 1. Simular X y epsilon
X = np.random.uniform(0, 10, size=N)
epsilon = np.random.normal(0, 1, size=N)

## 2. Generar Y
Y = 5 + 2 * X + epsilon

## 3. Ajustar el modelo de Regresión Lineal para estimar E[Y|X]
## X debe ser una matriz 2D para sklearn
X_matrix = X.reshape(-1, 1)

model = LinearRegression()
model.fit(X_matrix, Y)

## Coeficientes estimados
beta_0_estimated = model.intercept_
beta_1_estimated = model.coef_[0]

print("--- Estimación de la Esperanza Condicional ---")
print("Relación Verdadera E[Y|X] = 5 + 2X")
print(f"Intersección (β0) Estimada: {beta_0_estimated:.4f}")
print(f"Pendiente (β1) Estimada: {beta_1_estimated:.4f}")
```

#### Interpretación en el Contexto del Problema

Los coeficientes de regresión estimados (intersección $\approx 5.0$ y pendiente $\approx 2.0$) coinciden estrechamente con la relación lineal verdadera $E[Y|X]=5+2X$.

  * **Implicación en Nanotecnología:** La regresión lineal es un estimador para la función de **esperanza condicional**. Si $X$ es la concentración de un dopante y $Y$ es la conductividad, la relación $E[Y|X]=5+2X$ es el **modelo predictivo óptimo** (en el sentido de minimizar el error cuadrático medio) para la conductividad dado un nivel de dopante. Este modelo permite a los ingenieros predecir el resultado promedio del material y optimizar la concentración $X$ para alcanzar la conductividad deseada $Y$.

### Conclusión

Este trabajo demuestra de manera contundente cómo la herramienta estadística de regresión lineal nos permite descubrir y cuantificar la conexión directa entre variables que medimos en el laboratorio. Esto es fundamental para trabajar con materiales a escala nanométrica.

### 22. Determinación del Tipo de Distribución (Python)
Se midieron 1000 muestras de la longitud total $Z$ de un nano-alambre (suma de muchas etapas de crecimiento, $Z = X_1 + X_2 + \dots + X_k$).
**Tarea (Python):**
**Simule $Z$** como la suma de 50 variables Uniformes independientes $U(0, 1)$. **Realice una prueba de normalidad** sobre $Z$ (e.g., Shapiro-Wilk o Kolmogorov-Smirnov de `scipy.stats`) para **verificar el Teorema del Límite Central (TLC)**.

#### Solución Analítica (TLC)

El **Teorema del Límite Central (TLC)** establece que la suma (o promedio) de un gran número de variables aleatorias independientes (i.i.d.), independientemente de su distribución original, tiende a una **distribución Normal (Gaussiana)**. Dado que $k=50$ es grande, $Z = \sum_{i=1}^{50} X_i$ debe ser aproximadamente $\mathcal{N}(\mu_Z, \sigma_Z^2)$.

  * $\mu_Z = 50 \cdot E[X_i] = 50 \cdot 0.5 = 25$
  * $\sigma_Z^2 = 50 \cdot \text{Var}(X_i) = 50 \cdot (1/12) \approx 4.167$

#### Solución Computacional (Python)

```python
import numpy as np
from scipy.stats import shapiro

## Parámetros
N_samples = 1000
k_uniform_vars = 50  # Número de variables a sumar (grande para el TLC)

## 1. Simular la suma Z
## Generar una matriz de k_uniform_vars (columnas) x N_samples (filas)
X_matrix = np.random.uniform(0, 1, size=(N_samples, k_uniform_vars))

## Z es la suma a lo largo de las columnas
Z_samples = np.sum(X_matrix, axis=1)

## 2. Realizar la Prueba de Normalidad de Shapiro-Wilk
## Hipótesis Nula (H0): Los datos provienen de una distribución Normal.
## Hipótesis Alternativa (Ha): Los datos NO provienen de una distribución Normal.
statistic, p_value = shapiro(Z_samples)

alpha = 0.05

print("--- Verificación del Teorema del Límite Central ---")
print(f"Media muestral de Z: {np.mean(Z_samples):.4f} (Teórico: 25.0)")
print(f"Varianza muestral de Z: {np.var(Z_samples):.4f} (Teórico: 4.167)")
print(f"\nResultado de la prueba de Shapiro-Wilk:")
print(f"Estadístico W: {statistic:.4f}")
print(f"Valor p: {p_value:.4f}")

if p_value > alpha:
    print(f"\nConclusión: No se rechaza H0 (p-valor > {alpha}). Los datos siguen una distribución Normal (verificando el TLC).")
else:
    print(f"\nConclusión: Se rechaza H0 (p-valor < {alpha}). La distribución no es Normal.")
```

#### Interpretación en el Contexto del Problema

El valor $p$ de la prueba de Shapiro-Wilk es alto ($p > 0.05$), lo que significa que **no hay evidencia suficiente para rechazar la hipótesis de que $Z$ es Gaussiana**.

  * **Implicación en Nanotecnología:** La longitud final $Z$ de un nano-alambre, resultado de la acumulación de errores o etapas de crecimiento independientes ($X_i$), se modela de manera segura como una **Distribución Normal**. Esto permite a los ingenieros utilizar todas las herramientas estadísticas basadas en la normalidad (control de calidad $3\sigma$, prueba t, etc.) para el monitoreo de la producción, incluso si las etapas individuales tienen distribuciones de probabilidad no-normales.

### Conclusión

El Teorema del Límite Central es el puente estadístico que transforma datos experimentales variables en un proceso industrial predecible y optimizado dentro del mundo nanométrico.

### 23. Covarianza en Espacios de Alta Dimensión (Python)
Se monitorean 1000 nanopartículas y se miden 50 características de forma, tamaño y composición. La matriz de datos $\mathbf{D}$ es $1000 \times 50$.
**Tarea (Python):**
**Simule una matriz de datos $1000 \times 50$** (por ejemplo, con ruido Gaussiano). **Calcule y visualice** la matriz de covarianza muestral $\mathbf{S}$. **Calcule el número de condición** de $\mathbf{S}$ para evaluar su estabilidad numérica.

#### Solución Computacional (Python)

```python
import numpy as np
import matplotlib.pyplot as plt

## Parámetros
N_samples = 1000
P_features = 50

## 1. Simular la Matriz de Datos (D)
## Simulación de datos con cierta estructura (alta correlación dentro de bloques de 10 features)
np.random.seed(0)
## Crear una matriz de covarianza estructural (Toeplitz) para asegurar correlación
def generate_cov_matrix(p, rho=0.5):
    cov = np.zeros((p, p))
    for i in range(p):
        for j in range(p):
## Correlación decayendo con la distancia
            cov[i, j] = rho**np.abs(i - j)
    return cov

Sigma_true = generate_cov_matrix(P_features, rho=0.8)
D = np.random.multivariate_normal(np.zeros(P_features), Sigma_true, size=N_samples)

## 2. Calcular la Matriz de Covarianza Muestral (S)
S = np.cov(D, rowvar=False)

## 3. Visualizar S (Mapa de calor)
plt.figure(figsize=(8, 7))
plt.imshow(S, cmap='viridis')
plt.colorbar(label='Covarianza')
plt.title('Mapa de Calor de la Matriz de Covarianza Muestral (S)')
plt.xlabel('Feature Index')
plt.ylabel('Feature Index')
plt.show()

## 4. Calcular el Número de Condición (Condition Number)
## Cond(S) = lambda_max / lambda_min
eigenvalues = np.linalg.eigvals(S)
condition_number = np.linalg.cond(S)

print("--- Análisis de Matriz de Covarianza en Alta Dimensión ---")
print(f"Dimensiones de S: {S.shape}")
print(f"Eigenvalor Máximo (λ_max): {np.max(eigenvalues):.2f}")
print(f"Eigenvalor Mínimo (λ_min): {np.min(eigenvalues):.2e}")
print(f"Número de Condición Cond(S): {condition_number:.2e}")
```

#### Interpretación en el Contexto del Problema

El mapa de calor visualiza la **estructura de correlación** de las 50 características. Las regiones claras/oscuras indican correlaciones fuertes/débiles entre los pares de características.

El **Número de Condición (Cond(S))** es la relación entre el eigenvalor máximo y el mínimo.

  * **Implicación en Nanotecnología:** Un $\text{Cond}(S)$ **grande** (típicamente $\gg 1000$) indica que la matriz $\mathbf{S}$ está cerca de ser **singular** (no invertible) y es **numéricamente inestable**. Esto es común en datos de alta dimensión (donde $P$ es grande y $N$ es relativamente pequeño). Un número de condición alto implica que:
      * La matriz inversa $\mathbf{S}^{-1}$ (necesaria para la Distancia de Mahalanobis y la Gaussiana) es propensa a errores de cálculo.
      * Existe una **alta redundancia** o **colinealidad** en las 50 características, lo que sugiere que PCA o técnicas similares son necesarias para reducir la dimensión y estabilizar el sistema de ecuaciones.

### Conclusión

Al trabajar con sistemas nanométricos complejos, analizar la covarianza y evaluar la estabilidad numérica de nuestros modelos con el número de condición no es un lujo, sino una necesidad fundamental. Solo así garantizamos que las decisiones que tomemos para fabricar un nanodispositivo o mejorar un material sean sólidas y estén libres de interpretaciones erróneas.

### 24. Reconstrucción PCA y Reducción de Ruido (Python)
Simule un conjunto de datos $100 \times 3$ con $X_1$ y $X_2$ fuertemente correlacionadas ($\rho=0.99$) y $X_3$ como ruido Gaussiano puro e independiente $\mathcal{N}(0, 0.1^2)$.
**Tarea (Python):**
**a) Aplique PCA** y calcule la varianza explicada.
**b) Reconstruya el dataset usando solo $PC_1$**. Calcule la **varianza de la variable $X_3$ en el dataset reconstruido** para demostrar que el ruido ha sido reducido significativamente.

#### Solución Computacional (Python)

```python
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

## Parámetros de la simulación
N = 100
rho = 0.99
sigma_noise_sq = 0.1**2  # Varianza de X3 (ruido)

## 1. Simulación de la Matriz de Datos (D)
## Matriz de Covarianza verdadera para [X1, X2, X3]
## Asumimos Var(X1)=1, Var(X2)=1
Sigma_true = np.array([
    [1, rho, 0],
    [rho, 1, 0],
    [0, 0, sigma_noise_sq]
])
D = np.random.multivariate_normal(np.zeros(3), Sigma_true, size=N)

## 2. Estandarización y PCA
scaler = StandardScaler()
D_scaled = scaler.fit_transform(D)

## a) Aplicar PCA (n_components=1)
pca = PCA(n_components=1)
D_projected = pca.fit_transform(D_scaled)

print("--- PCA para Denoising ---")
print(f"Varianza Explicada por PC1: {pca.explained_variance_ratio_[0]*100:.2f}%")

## 3. Reconstrucción con solo PC1
D_recons_scaled = pca.inverse_transform(D_projected)

## 4. Cálculo de la Varianza del Ruido (X3)
## Varianza de X3 original (escalada): Debería ser ~1.0 (tras escalado)
var_x3_original_scaled = np.var(D_scaled[:, 2])

## Varianza de X3 en la reconstrucción (contiene el ruido restante)
var_x3_reconstructed = np.var(D_recons_scaled[:, 2])

print(f"\nVarianza de X3 original (tras escalado): {var_x3_original_scaled:.4f}")
print(f"Varianza de X3 en la Matriz Reconstruida (usando solo PC1): {var_x3_reconstructed:.4f}")
```

#### Interpretación en el Contexto del Problema

La varianza original de $X_3$ (el ruido) es cercana a $1.0$ (debido a la estandarización). Después de la reconstrucción con solo $PC_1$, la varianza de $X_3$ **cae drásticamente** (típicamente a un valor cercano a $0.01$).

  * **Implicación en Nanotecnología:** El $PC_1$ (que explica $\approx 99.5\%$ de la varianza) capta la **señal común** de $X_1$ y $X_2$ (correlacionadas). El ruido $X_3$ es independiente y tiene baja varianza, por lo que se asocia a los $PC$s de alta orden (PC2 y PC3). Al reconstruir usando solo $PC_1$, el ruido se **elimina efectivamente** porque esa información fue descartada. PCA actúa como un potente filtro para **separar la señal física coherente de las mediciones del ruido aleatorio** en datos de caracterización, un proceso llamado **Denoising** o **Compresión de Datos**.

### Conclusión

En el mundo tan sensible de la nanotecnología, los datos suelen venir con mucho "ruido" o interferencias. Usar PCA nos permite esencialmente limpiar esa información.

### 25. Varianza de la Combinación Lineal (Python)

Un investigador propone el **Índice de Estabilidad Estructural $I$** como la combinación lineal $I = 4X_1 + 2X_2 - X_3$, donde $\mathbf{X}=(X_1, X_2, X_3)^T$ tiene la matriz de covarianza $\mathbf{\Sigma}$ del Problema 12:

$$\mathbf{\Sigma} = \begin{pmatrix} 5 & 2 & 1 \\ 2 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}$$

**Tarea (Python):**
**Calcule la matriz $\mathbf{A}$** que representa la transformación lineal. **Calcule $\text{Var}(I)$** usando $\mathbf{A}\mathbf{\Sigma}\mathbf{A}^T$.

#### Solución Analítica

1.  **Matriz de Transformación $\mathbf{A}$:**
  La variable $I$ es una combinación lineal $I = \mathbf{A}\mathbf{X}$. Como $I$ es escalar, $\mathbf{A}$ debe ser un vector fila.
  $$I = (4)X_1 + (2)X_2 + (-1)X_3$$
  $$\mathbf{A} = \begin{pmatrix} 4 & 2 & -1 \end{pmatrix}$$

2.  **Cálculo de la Varianza:**
  $$\text{Var}(I) = \mathbf{A}\mathbf{\Sigma}\mathbf{A}^T$$

  $$\mathbf{A}\mathbf{\Sigma} = \begin{pmatrix} 4 & 2 & -1 \end{pmatrix} \begin{pmatrix} 5 & 2 & 1 \\ 2 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix} = \begin{pmatrix} (20+4-1) & (8+2-0) & (4+0-1) \end{pmatrix} = \begin{pmatrix} 23 & 10 & 3 \end{pmatrix}$$

  $$\mathbf{A}\mathbf{\Sigma}\mathbf{A}^T = \begin{pmatrix} 23 & 10 & 3 \end{pmatrix} \begin{pmatrix} 4 \\ 2 \\ -1 \end{pmatrix} = (23)(4) + (10)(2) + (3)(-1) = 92 + 20 - 3 = \mathbf{109}$$

#### Solución Computacional (Python) mejorado por Claude

```python
import numpy as np

## Matriz de Covarianza (Problema 12)
Sigma = np.array([
    [5, 2, 1],
    [2, 1, 0],
    [1, 0, 1]
])

## Vector de Transformación para I = 4X₁ + 2X₂ - X₃
A = np.array([4, 2, -1])

## Cálculo de Var(I) = A Σ A^T
variance_I = A @ Sigma @ A

print("=" * 50)
print("VARIANZA DEL ÍNDICE DE ESTABILIDAD ESTRUCTURAL")
print("=" * 50)
print(f"\nVector de coeficientes A: {A}")
print(f"\nMatriz de covarianza Σ:\n{Sigma}")
print(f"\nVar(I) = {variance_I:.2f}")

## Análisis de contribuciones
print("\n" + "=" * 50)
print("DESCOMPOSICIÓN DE LA VARIANZA")
print("=" * 50)
contributions = A**2 * np.diag(Sigma)
cov_terms = 2 * (A[0]*A[1]*Sigma[0,1] +
                 A[0]*A[2]*Sigma[0,2] +
                 A[1]*A[2]*Sigma[1,2])

for i, var_name in enumerate(['X₁', 'X₂', 'X₃']):
    print(f"Contribución de {var_name}: {contributions[i]:6.2f} ({100*contributions[i]/variance_I:5.1f}%)")
print(f"Contribución de covarianzas: {cov_terms:6.2f} ({100*cov_terms/variance_I:5.1f}%)")
```

#### Interpretación en el Contexto del Problema

La varianza del Índice de Estabilidad Estructural $I$ es **$109.0$**.

  * **Implicación en Nanotecnología:** La varianza de 109 indica que el índice $I$ tiene una **alta dispersión** a lo largo de los lotes de materiales. La alta magnitud de los coeficientes (4 y 2) en $\mathbf{A}$ **amplifica** la varianza de las variables originales y su covarianza. Si el objetivo del investigador es que el índice de estabilidad sea preciso (baja varianza), este diseño de índice es subóptimo debido a su alta sensibilidad a las variaciones en $X_1$ y $X_2$. El resultado indica que se debe rediseñar el índice o mejorar el control de las variables $X_1$ y $X_2$ para reducir la $\text{Var}(I)$.

### Conclusión

Al final, este conocimiento es fundamental para diseñar procesos de síntesis de nanopartículas o el ensamblaje de estructuras avanzadas que sean robustos y confiables. Nos ayuda a ajustar las "recetas" (los coeficientes del modelo) para que la inestabilidad inherente de trabajar a escala nanométrica se minimice, impulsando así el éxito y la confianza en el desarrollo de materiales avanzados.

## Tarea
Problemas avanzados de probabilidad y estadística con el tema de la nanotecnología, integrando todos los conceptos clave del **Capítulo 5: Distribuciones Conjuntas** [cite: 935] del libro de texto.

---

## Problema 1: Síntesis y Degradación de Nanopartículas de Oro (Joint Distribution, Conditional Expectation, Covariance)

En un proceso para la fabricación de un **nanosensor biológico** a base de **nanopartículas de oro (AuNPs)**, se estudian dos características críticas:
* $X$: el **Diámetro** de la nanopartícula (en $\text{nm}$).
* $Y$: la **Tasa de Degradación** del recubrimiento (en $\text{nm/semana}$).

$X$ y $Y$ son variables aleatorias continuas con la siguiente **Función de Densidad de Probabilidad Conjunta (Joint PDF)**, válida para $x \ge 0$ y $y \ge 0$:

$$f_{X,Y}(x, y) = c \cdot x \cdot e^{-(x+2y)} \cdot \mathbb{I}_{\{x \ge 0, y \ge 0\}}$$

Donde $c$ es la constante de normalización.

1.  **Normalización y Función Marginal (5.1.4, 5.1.5):** Determine el valor de la constante de normalización $c$. Luego, calcule la **Función de Densidad Marginal** $f_Y(y)$.

2. **Probabilidad Condicional (5.3.2):** Calcule la **Función de Densidad Condicional** $f_{X|Y}(x|y)$ para un valor de tasa de degradación $Y=y$ dado. ¿Son $X$ y $Y$ variables aleatorias independientes? Justifique su respuesta.

3.  **Esperanza Condicional (5.4.1):** Calcule la **Esperanza Condicional** del diámetro, dado un valor de tasa de degradación, $E[X | Y=y]$.
4.  **Covarianza (5.2.2):** Calcule la **Covarianza** $\text{Cov}[X, Y]$. ¿Qué implica este valor acerca de la relación entre el diámetro de la nanopartícula y su tasa de degradación?.

## Análisis
Tenemos la función de densidad de probabilidad conjunta (PDF) para $X$ (Diámetro) y $Y$ (Tasa de Degradación):
$$f_{X,Y}(x, y) = c \cdot x \cdot e^{-(x+2y)}, \quad \text{para } x \ge 0, y \ge 0$$

### 1\. Normalización y Función Marginal

**Objetivo:** Determinar la constante $c$ y la PDF marginal $f_Y(y)$.

**a) Constante de Normalización $c$**

Para que $f_{X,Y}(x, y)$ sea una PDF válida, su integral sobre todo el dominio debe ser 1.

$$\int_{0}^{\infty} \int_{0}^{\infty} f_{X,Y}(x, y) \,dx \,dy = 1$$
$$\int_{0}^{\infty} \int_{0}^{\infty} c \cdot x \cdot e^{-(x+2y)} \,dx \,dy = 1$$

Podemos separar la exponencial $e^{-(x+2y)} = e^{-x} e^{-2y}$ y, dado que las variables $x$ y $y$ son separables en la función y en los límites, podemos separar la integral:

$$c \cdot \left( \int_{0}^{\infty} x e^{-x} \,dx \right) \cdot \left( \int_{0}^{\infty} e^{-2y} \,dy \right) = 1$$

Resolvemos cada integral:

  * **Integral en $x$:** $\int_{0}^{\infty} x e^{-x} \,dx$. Esta es la integral de la función Gamma $\Gamma(2)$, que es igual a $(2-1)! = 1! = 1$. (Se puede resolver por partes).
  * **Integral en $y$:** $\int_{0}^{\infty} e^{-2y} \,dy = \left[ -\frac{1}{2} e^{-2y} \right]_{0}^{\infty} = (0) - \left(-\frac{1}{2} e^{0}\right) = \frac{1}{2}$.

Sustituimos los resultados:
$$c \cdot (1) \cdot \left( \frac{1}{2} \right) = 1$$
$$\frac{c}{2} = 1 \implies \mathbf{c = 2}$$

La PDF conjunta completa es: $f_{X,Y}(x, y) = 2 x e^{-(x+2y)}$ para $x \ge 0, y \ge 0$.

**b) Función de Densidad Marginal $f_Y(y)$**

Para encontrar la PDF marginal de $Y$, integramos la PDF conjunta sobre todos los posibles valores de $X$.

$$f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \,dx = \int_{0}^{\infty} 2 x e^{-(x+2y)} \,dx$$
$$f_Y(y) = \int_{0}^{\infty} 2 x e^{-x} e^{-2y} \,dx$$

Sacamos los términos de $y$ (que son constantes respecto a $x$) fuera de la integral:
$$f_Y(y) = 2 e^{-2y} \int_{0}^{\infty} x e^{-x} \,dx$$

Ya sabemos que $\int_{0}^{\infty} x e^{-x} \,dx = 1$.
$$f_Y(y) = 2 e^{-2y} \cdot (1)$$
$$\mathbf{f_Y(y) = 2 e^{-2y}}, \quad \text{para } y \ge 0$$

#### Interpretación y Conclusión

  * El valor $\mathbf{c=2}$ es requerido para que la probabilidad total de todas las combinaciones de diámetro y tasa de degradación sea del 100%.
  * La función marginal $\mathbf{f_Y(y) = 2e^{-2y}}$ (para $y \ge 0$) describe la distribución de probabilidad de la **Tasa de Degradación ($Y$)** únicamente, ignorando el diámetro. Esta es una **distribución Exponencial** con parámetro $\lambda = 2$. Esto implica que las tasas de degradación bajas son mucho más probables que las tasas altas.

### 2\. Probabilidad Condicional e Independencia

**Objetivo:** Calcular la PDF condicional $f_{X|Y}(x|y)$ y determinar si $X$ y $Y$ son independientes.

**a) Función de Densidad Condicional $f_{X|Y}(x|y)$**

La fórmula para la densidad condicional es:
$$f_{X|Y}(x|y) = \frac{f_{X,Y}(x, y)}{f_Y(y)}, \quad \text{siempre que } f_Y(y) > 0$$

Sustituimos las funciones que encontramos en el Paso 1:
$$f_{X|Y}(x|y) = \frac{2 x e^{-(x+2y)}}{2 e^{-2y}}$$
$$f_{X|Y}(x|y) = \frac{2 x e^{-x} e^{-2y}}{2 e^{-2y}}$$

Cancelamos los términos $2$ y $e^{-2y}$:
$$\mathbf{f_{X|Y}(x|y) = x e^{-x}}, \quad \text{para } x \ge 0$$

**b) Independencia**

Para que $X$ y $Y$ sean independientes, debe cumplirse una de estas condiciones equivalentes:

1.  $f_{X,Y}(x, y) = f_X(x) f_Y(y)$
2.  $f_{X|Y}(x|y) = f_X(x)$

Probemos la **Condición 2**:
Acabamos de encontrar $f_{X|Y}(x|y) = x e^{-x}$.
Ahora calculemos la PDF marginal $f_X(x)$ (aunque no se pidió, la necesitamos para la prueba):
$$f_X(x) = \int_{0}^{\infty} f_{X,Y}(x, y) \,dy = \int_{0}^{\infty} 2 x e^{-x} e^{-2y} \,dy$$
$$f_X(x) = 2 x e^{-x} \int_{0}^{\infty} e^{-2y} \,dy$$
Sabemos que $\int_{0}^{\infty} e^{-2y} \,dy = 1/2$.
$$f_X(x) = 2 x e^{-x} \cdot \left(\frac{1}{2}\right) = x e^{-x}$$

**Justificación:**
Comparamos $f_{X|Y}(x|y)$ y $f_X(x)$:

  * $f_{X|Y}(x|y) = x e^{-x}$
  * $f_X(x) = x e^{-x}$

Dado que $\mathbf{f_{X|Y}(x|y) = f_X(x)}$, las variables aleatorias $X$ y $Y$ **SÍ son independientes**.

#### Interpretación y Conclusión

  * La función condicional $\mathbf{f_{X|Y}(x|y) = xe^{-x}}$ nos dice la distribución del diámetro $X$ *dado que* sabemos que la tasa de degradación es $Y=y$.
  * El resultado clave es que la variable $y$ *desaparece* de la fórmula final. Esto significa que el valor de $y$ (la tasa de degradación) no tiene ningún impacto en la distribución de probabilidad de $x$ (el diámetro).
  * **Conclusión:** El diámetro de la nanopartícula ($X$) y la tasa de degradación de su recubrimiento ($Y$) son **estadísticamente independientes**. En este proceso de fabricación, conocer el tamaño de una partícula no da información sobre la estabilidad de su recubrimiento, y viceversa.

### 3\. Esperanza Condicional

**Objetivo:** Calcular la esperanza condicional $E[X | Y=y]$.

**Usando la Definición de Esperanza Condicional**

La $E[X | Y=y]$ es el valor esperado (la media) de $X$ usando la distribución de probabilidad condicional $f_{X|Y}(x|y)$.

$$E[X | Y=y] = \int_{-\infty}^{\infty} x \cdot f_{X|Y}(x|y) \,dx$$

Usamos la $f_{X|Y}(x|y) = x e^{-x}$ que encontramos en el Paso 2:
$$E[X | Y=y] = \int_{0}^{\infty} x \cdot (x e^{-x}) \,dx$$
$$E[X | Y=y] = \int_{0}^{\infty} x^2 e^{-x} \,dx$$

Esta integral es la definición de la función Gamma $\Gamma(3)$, que es igual a $(3-1)! = 2! = 2$.
(Se puede resolver con dos integraciones por partes).

$\\mathbf{\1}$

#### Interpretación y Conclusión

  * El resultado $\mathbf{E[X | Y=y] = 2}$ (en nm) significa que el **diámetro promedio esperado** para una nanopartícula es de $2 \text{ nm}$, **sin importar** cuál sea su tasa de degradación ($y$).
  * Si un técnico mide una partícula y encuentra que tiene una tasa de degradación muy alta (p.ej., $Y=5$) o muy baja (p.ej., $Y=0.1$), la mejor estimación para el diámetro de esa partícula sigue siendo $2 \text{ nm}$. Esto es una consecuencia directa de la independencia.

### 4\. Covarianza

**Objetivo:** Calcular la covarianza $\text{Cov}[X, Y]$ y interpretar su significado.

**Usando la Fórmula $\text{Cov}[X, Y] = E[XY] - E[X]E[Y]$**

Verifiquemos este resultado calculando todos los términos:

  * **$E[X]$:** Ya la calculamos en el Paso 3. $E[X] = 2$.
  * **$E[Y]$:** Usamos la PDF marginal $f_Y(y) = 2 e^{-2y}$.
    $ E[Y] = \int_{0}^{\infty} y \cdot f_Y(y) \,dy = \int_{0}^{\infty} y \cdot (2 e^{-2y}) \,dy$$
    Esta es la media de una distribución Exponencial($\lambda=2$), que es $1/\lambda$.
    $$E[Y] = \frac{1}{2}$$
  * **$E[XY]$:** Usamos la PDF conjunta $f_{X,Y}(x, y) = 2 x e^{-x} e^{-2y}$.
   $$E[XY] = \int_{0}^{\infty} \int_{0}^{\infty} (xy) \cdot f_{X,Y}(x, y) \,dx \,dy$$

$$E[XY] = \int_{0}^{\infty} \int_{0}^{\infty} (xy) \cdot (2 x e^{-x} e^{-2y}) \,dx \,dy$$

Como las variables son independientes, $E[XY] = E[X]E[Y]$. Pero si no lo supiéramos, separamos la integral:

$$E[XY] = 2 \cdot \left( \int_{0}^{\infty} x (x e^{-x}) \,dx \right) \cdot \left( \int_{0}^{\infty} y e^{-2y} \,dy \right)$$

$$E[XY] = 2 \cdot \left( \int_{0}^{\infty} x^2 e^{-x} \,dx \right) \cdot \left( \int_{0}^{\infty} y e^{-2y} \,dy \right)$$

* Integral en $x$: $\int_{0}^{\infty} x^2 e^{-x} \,dx = \Gamma(3) = 2$.
* Integral en $y$: $\int_{0}^{\infty} y e^{-2y} \,dy$. (Por partes da $1/4$).

$$E[XY] = 2 \cdot (2) \cdot \left( \frac{1}{4} \right) = 1$$

Ahora calculamos la covarianza:
$$\text{Cov}[X, Y] = E[XY] - E[X]E[Y]$$
$$\text{Cov}[X, Y] = 1 - (2) \cdot \left( \frac{1}{2} \right)$$
$$\text{Cov}[X, Y] = 1 - 1 = 0$$

#### Interpretación y Conclusión

  * **Interpretación del valor:** La covarianza mide la fuerza y dirección de una **relación lineal** entre dos variables. Un valor de $\mathbf{Cov}[X, Y] = 0$ significa que no existe ninguna relación lineal entre $X$ (diámetro) y $Y$ (tasa de degradación).
  * **Conclusión general:** El resultado de cero covarianza confirma analíticamente lo que encontramos en el Paso 2: las variables no solo no están correlacionadas linealmente, sino que son totalmente independientes. Para este nanosensor, el proceso que determina el tamaño final de la nanopartícula de oro es completamente independiente del proceso que determina la estabilidad (tasa de degradación) de su recubrimiento.

## Python

```python
import sympy
from sympy import symbols, exp, integrate, oo, N

x, y, c = symbols('x y c', real=True, positive=True)

## f_XY(x, y) = c * x * exp(-(x + 2*y))
f_unnormalized = x * exp(-(x + 2*y))

## a) Determinar la constante de normalización c
integral_total = integrate(f_unnormalized, (x, 0, oo), (y, 0, oo))
c_val = 1 / integral_total
f_joint = c_val * f_unnormalized

print(f"1. Normalización y Marginal")
print(f"   Integral de la función no normalizada: {integral_total}")
print(f"   Constante de Normalización (c): {c_val}")
print(f"   Función de Densidad Conjunta f_XY(x, y) = {f_joint}")

## b) Calcular la Función de Densidad Marginal f_Y(y)
f_Y = integrate(f_joint, (x, 0, oo))

print(f"   Función de Densidad Marginal f_Y(y) = {f_Y}")
## a) Calcular la Función de Densidad Condicional f_X|Y(x|y)
f_X_given_Y = f_joint / f_Y

print("\n2. Probabilidad Condicional e Independencia")
print(f"   Función de Densidad Condicional f_X|Y(x|y) = {f_X_given_Y}")
f_X = integrate(f_joint, (y, 0, oo))
print(f"   Función de Densidad Marginal f_X(x) = {f_X}")

independientes = (f_X_given_Y.simplify() == f_X.simplify())

print(f"   ¿Son X e Y independientes? {independientes}")
print("   Justificación: f_X|Y(x|y) es idéntica a f_X(x).")

## E[X | Y=y] = Integral de x * f_X|Y(x|y) dx
E_X_given_Y = integrate(x * f_X_given_Y, (x, 0, oo))

print("\n3. Esperanza Condicional")
print(f"   Esperanza Condicional E[X | Y=y] = {E_X_given_Y}")
print("   (La esperanza no depende de 'y', confirmando la independencia)")

## Cov[X, Y] = E[XY] - E[X]E[Y]
E_X = integrate(x * f_X, (x, 0, oo))
E_Y = integrate(y * f_Y, (y, 0, oo))
E_XY = integrate(x * y * f_joint, (x, 0, oo), (y, 0, oo))
Cov_XY = E_XY - E_X * E_Y

print("\n4. Covarianza")
print(f"   E[X] = {E_X} (nm)")
print(f"   E[Y] = {E_Y} (nm/semana)")
print(f"   E[XY] = {E_XY}")
print(f"   Cov[X, Y] = E[XY] - E[X]E[Y] = {Cov_XY.simplify()}")
```

## Problema 2: Control de Calidad de Nanochips (Random Vectors, PCA, Sum of Random Variables)

En la producción masiva de un **nanochip** de memoria, dos parámetros de rendimiento, $P_1$ y $P_2$, se miden al final de la línea de montaje. Estos parámetros se modelan como un **Vector Aleatorio** $\mathbf{X} = [P_1, P_2]^T$, con un vector de medias $\mathbf{\mu} = [5, 10]^T$ y la siguiente **Matriz de Covarianza (Covariance Matrix)** $\mathbf{C}$:

$$\mathbf{C} = \begin{pmatrix} 2 & 1 \\ 1 & 5 \end{pmatrix}$$

1.  **Correlación y Dependencia (5.2.2, 5.6.3):** Calcule el **coeficiente de correlación** $\rho$ entre los parámetros $P_1$ y $P_2$.

2. **Análisis de Componentes Principales (PCA) (5.7.2, 5.8.1):** Para realizar un análisis de **Componentes Principales (PCA)** y comprender la máxima varianza del sistema, obtenga los **Eigenvalores** $\lambda_1$ y $\lambda_2$ de la matriz de covarianza $\mathbf{C}$. ¿Cuál es la varianza total del vector aleatorio $\mathbf{X}$ y cómo se relaciona con sus eigenvalores?.

3.  **Transformación y Suma de Variables Aleatorias (5.5.2):** Un nuevo índice de rendimiento del chip, R, se define como la suma ponderada $R = 2P_1 + P_2$. Calcule la **Varianza** de este nuevo índice, $\text{Var}[R]$.

4.  **Distribución Multidimensional (5.6.4):** Asumiendo que $\mathbf{X}$ sigue una **Distribución Gaussiana Multidimensional**. Si el control de calidad requiere que el índice R sea superior a 25. Describa detalladamente los pasos a seguir para calcular la probabilidad de que un chip pase el control de calidad, $P[R > 25]$, utilizando la función de distribución acumulada (CDF) de una variable Gaussiana unidimensional.

## Análisis

El **Vector Aleatorio** es $\mathbf{X} = [P_1, P_2]^T$ con vector de medias $\mathbf{\mu} = [5, 10]^T$ y **Matriz de Covarianza** $\mathbf{C}$:

$$\mathbf{C} = \begin{pmatrix} 2 & 1 \\ 1 & 5 \end{pmatrix}$$

### 1\. Coeficiente de Correlación

El coeficiente de correlación $\rho$ entre $P_1$ y $P_2$ se define como:
$$\rho = \frac{\text{Cov}[P_1, P_2]}{\sqrt{\text{Var}[P_1] \text{Var}[P_2]}}$$

De la matriz $\mathbf{C}$:

  * $\text{Var}[P_1] = C_{11} = 2$
  * $\text{Var}[P_2] = C_{22} = 5$
  * $\text{Cov}[P_1, P_2] = C_{12} = 1$

Sustituyendo:
$$\rho = \frac{1}{\sqrt{2 \cdot 5}} = \frac{1}{\sqrt{10}}$$

$$\rho \approx 0.3162$$

**Interpretación:** El coeficiente de correlación es **positivo y relativamente bajo** (más cerca de 0 que de 1). Esto indica una **dependencia lineal débil** entre los parámetros de rendimiento $P_1$ y $P_2$. Al aumentar el rendimiento $P_1$, hay una ligera tendencia a que $P_2$ también aumente, pero no es una relación fuerte.

### 2\. Análisis de Componentes Principales (PCA)

Para obtener los **Eigenvalores** $\lambda$ de $\mathbf{C}$, resolvemos la ecuación característica: $\det(\mathbf{C} - \lambda \mathbf{I}) = 0$.

$$\det \begin{pmatrix} 2-\lambda & 1 \\ 1 & 5-\lambda \end{pmatrix} = 0$$
$$(2-\lambda)(5-\lambda) - (1)(1) = 0$$
$$10 - 7\lambda + \lambda^2 - 1 = 0$$
$$\lambda^2 - 7\lambda + 9 = 0$$

Usando la fórmula cuadrática $\lambda = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$:
$$\lambda = \frac{7 \pm \sqrt{(-7)^2 - 4(1)(9)}}{2} = \frac{7 \pm \sqrt{49 - 36}}{2} = \frac{7 \pm \sqrt{13}}{2}$$

Los eigenvalores son:
$$\lambda_1 = \frac{7 + \sqrt{13}}{2} \approx \frac{7 + 3.6056}{2} \approx 5.3028$$
$$\lambda_2 = \frac{7 - \sqrt{13}}{2} \approx \frac{7 - 3.6056}{2} \approx 1.6972$$

**Varianza Total del Vector Aleatorio:**

La varianza total es la suma de las varianzas de las variables individuales (la **traza** de $\mathbf{C}$):
$$\text{Var}_{\text{Total}} = \text{Var}[P_1] + \text{Var}[P_2] = 2 + 5 = **7**$$

**Relación con los Eigenvalores:**

La varianza total del vector aleatorio es **igual a la suma de sus eigenvalores**.
$$\lambda_1 + \lambda_2 = \frac{7 + \sqrt{13}}{2} + \frac{7 - \sqrt{13}}{2} = \frac{7 + \sqrt{13} + 7 - \sqrt{13}}{2} = \frac{14}{2} = **7$$

**Interpretación:**
      * La **Varianza Total** del sistema es **7**, que es la suma de las varianzas individuales ($2+5$).
      * La suma de los eigenvalores ($\lambda_1 + \lambda_2 \approx 7$) **confirma** que la varianza total se mantiene en la transformación de PCA.
      * $\lambda_1$ concentra la mayor parte de la varianza ($\frac{5.3028}{7} \approx 75.75\%$). La primera componente principal, asociada a $\lambda_1$, captura la **dirección de máxima variación** en el sistema.

### 3\. Varianza de la Suma Ponderada

El nuevo índice es $R = 2P_1 + P_2$. La varianza de una combinación lineal de variables aleatorias $\mathbf{a}^T \mathbf{X}$ es $\mathbf{a}^T \mathbf{C} \mathbf{a}$.
Aquí, el vector de pesos es $\mathbf{a} = [2, 1]^T$.

$$\text{Var}[R] = \text{Var}[2P_1 + P_2] = \mathbf{a}^T \mathbf{C} \mathbf{a}$$
$$\text{Var}[R] = \begin{pmatrix} 2 & 1 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 1 & 5 \end{pmatrix} \begin{pmatrix} 2 \\ 1 \end{pmatrix}$$

Primero, multiplicamos $\mathbf{C} \mathbf{a}$:
$$\begin{pmatrix} 2 & 1 \\ 1 & 5 \end{pmatrix} \begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 2(2) + 1(1) \\ 1(2) + 5(1) \end{pmatrix} = \begin{pmatrix} 5 \\ 7 \end{pmatrix}$$

Luego, multiplicamos $\mathbf{a}^T (\mathbf{C} \mathbf{a})$:
$$\text{Var}[R] = \begin{pmatrix} 2 & 1 \end{pmatrix} \begin{pmatrix} 5 \\ 7 \end{pmatrix} = 2(5) + 1(7) = 10 + 7 = **17**$$

**Interpretación:** La varianza del nuevo índice de rendimiento $R = 2P_1 + P_2$ es **17**. Esta varianza es significativamente mayor que la suma de las varianzas individuales ($2+5=7$), debido al peso de $2$ aplicado a $P_1$ y la covarianza positiva entre $P_1$ y $P_2$, que al ser linealmente combinadas, **aumentan la dispersión total** del índice R.

### 4\. Probabilidad del Control de Calidad

**Variable Aleatoria R bajo Supuesto Gaussiano:**

Dado que $\mathbf{X}$ sigue una Distribución Gaussiana Multidimensional, cualquier combinación lineal de sus componentes, como $R = 2P_1 + P_2$, también sigue una **Distribución Gaussiana** (unidimensional).

Necesitamos la **media** $\mu_R$ y la **varianza** $\sigma_R^2$ de R.

1.  **Media de R:**
    $$\mu_R = E[R] = E[2P_1 + P_2] = 2E[P_1] + E[P_2] = 2(5) + 10 = 10 + 10 = 20$$
2.  **Varianza de R:**
    $$\sigma_R^2 = \text{Var}[R] = 17 \quad \text{(Calculado en el punto 3)}$$

Por lo tanto, $R \sim \mathcal{N}(20, 17)$. El control de calidad requiere $R > 25$. Queremos calcular $P[R > 25]$.

**Pasos para el Cálculo de la Probabilidad $P[R > 25]$:**

1.  **Estandarización (Normalización):** Transformar la variable R a la **Variable Normal Estándar** $Z \sim \mathcal{N}(0, 1)$ usando la fórmula:
$$Z = \frac{R - \mu_R}{\sigma_R}$$

Donde $\sigma_R$ es la desviación estándar de R, y se calcula como:

$$\sigma_R = \sqrt{\text{Var}[R]} = \sqrt{17} \approx 4.1231$$

2.  **Cálculo del Puntuación Z (Z-score):** Sustituir el valor de umbral $R=25$:

$$Z_{\text{umbral}} = \frac{25 - \mu_R}{\sqrt{\text{Var}[R]}}$$

Sustituyendo los valores conocidos ($\mu_R=20$ y $\text{Var}[R]=17$):

$$Z_{\text{umbral}} = \frac{25 - 20}{\sqrt{17}} = \frac{5}{\sqrt{17}} \approx 1.2126$$

3.  **Uso de la Función de Distribución Acumulada (CDF):** La probabilidad $P[R > 25]$ se convierte en $P[Z > Z_{\text{umbral}}]$. Usando la CDF de la Normal Estándar, $\Phi(z)$:
    $$P[R > 25] = P[Z > 1.2126] = 1 - P[Z \le 1.2126] = 1 - \Phi(1.2126)$$

4.  **Consulta/Cálculo del Valor de $\Phi(Z_{\text{umbral}})$:** Se usa una tabla Z o una función de la librería matemática (como `scipy.stats.norm.cdf` en Python) para encontrar $\Phi(1.2126)$.

5.  **Resultado Final:** El valor $1 - \Phi(1.2126)$ es la probabilidad buscada.

**Interpretación:** Asumiendo una distribución Gaussiana, la probabilidad de que un chip **pase el control de calidad** (es decir, $R > 25$) es de aproximadamente **11.26%**. Esto indica que, en el estado actual de la producción, la mayoría de los chips (casi el 89%) no cumplen con el exigente requisito de rendimiento $R > 25$.

## Python

```python
import numpy as np
from scipy.linalg import eig
from scipy.stats import norm
mu = np.array([5, 10])
C = np.array([
    [2, 1],
    [1, 5]
])

## --- 1. Coeficiente de Correlación ---
print("1. Coeficiente de Correlación")
var_P1 = C[0, 0]
var_P2 = C[1, 1]
cov_P1P2 = C[0, 1]

rho = cov_P1P2 / np.sqrt(var_P1 * var_P2)
print(f"Varianza P1 (Var[P1]): {var_P1}")
print(f"Varianza P2 (Var[P2]): {var_P2}")
print(f"Covarianza (Cov[P1, P2]): {cov_P1P2}")
print(f"Coeficiente de Correlación (rho): {rho:.4f}")

## --- 2. Análisis de Componentes Principales (PCA) ---
print("\n2. PCA: Eigenvalores y Varianza Total")
## Calcular Eigenvalores
eigenvalues, _ = eig(C)
lambda1 = np.real(eigenvalues[0])
lambda2 = np.real(eigenvalues[1])
if lambda2 > lambda1:
    lambda1, lambda2 = lambda2, lambda1

varianza_total_C = np.trace(C)
varianza_total_eigen = lambda1 + lambda2

print(f"Eigenvalor 1 (lambda1 - Mayor): {lambda1:.4f}")
print(f"Eigenvalor 2 (lambda2 - Menor): {lambda2:.4f}")
print(f"Varianza Total (Traza de C): {varianza_total_C:.4f}")
print(f"Suma de Eigenvalores: {varianza_total_eigen:.4f}")

## --- 3. Varianza de la Suma Ponderada R = 2P1 + P2 ---
print("\n3. Varianza de R = 2P1 + P2")
a = np.array([2, 1])
## Var[R] = a^T * C * a
Var_R = a.T @ C @ a
print(f"Vector de pesos a: {a}")
print(f"Varianza de R (Var[R]): {Var_R:.4f}")

## --- 4. Probabilidad del Control de Calidad P[R > 25] ---
print("\n4. Probabilidad de Control de Calidad P[R > 25]")
## E[R] = a^T * mu
mu_R = a.T @ mu
sigma_R = np.sqrt(Var_R)
umbral = 25
Z_score = (umbral - mu_R) / sigma_R
P_R_mayor_25 = 1 - norm.cdf(Z_score)

print(f"Media de R (E[R]): {mu_R:.4f}")
print(f"Desviación Estándar de R (sigma_R): {sigma_R:.4f}")
print(f"Z-score para R=25: {Z_score:.4f}")
print(f"Probabilidad P[R > 25]: {P_R_mayor_25:.4f}")
```

---

## PROBABILIDAD Y ESTADÍSTICA

**INGENIERÍA EN NANOTECNOLOGÍA**

**Universidad de La Ciénega del Estado de Michoacán de Ocampo**

*Capítulo 5 secciones 5.3 a 5.8: Distribuciones Conjuntas, Condicionales, Convolución Vectores Aleatorios, Transformaciones Gaussianas y Análisis de Compnentes Principales*

## Tarea
Problemas avanzados de probabilidad y estadística con el tema de la nanotecnología, integrando todos los conceptos clave del **Capítulo 5: Distribuciones Conjuntas** [cite: 935] del libro de texto.

---

## Problema 1: Síntesis y Degradación de Nanopartículas de Oro (Joint Distribution, Conditional Expectation, Covariance)

En un proceso para la fabricación de un **nanosensor biológico** a base de **nanopartículas de oro (AuNPs)**, se estudian dos características críticas:
* $X$: el **Diámetro** de la nanopartícula (en $\text{nm}$).
* $Y$: la **Tasa de Degradación** del recubrimiento (en $\text{nm/semana}$).

$X$ y $Y$ son variables aleatorias continuas con la siguiente **Función de Densidad de Probabilidad Conjunta (Joint PDF)**, válida para $x \ge 0$ y $y \ge 0$:

$$f_{X,Y}(x, y) = c \cdot x \cdot e^{-(x+2y)} \cdot \mathbb{I}_{\{x \ge 0, y \ge 0\}}$$

Donde $c$ es la constante de normalización.

1.  [cite_start]**Normalización y Función Marginal (5.1.4, 5.1.5):** Determine el valor de la constante de normalización $c$[cite: 935]. [cite_start]Luego, calcule la **Función de Densidad Marginal** $f_Y(y)$[cite: 935].
2.  [cite_start]**Probabilidad Condicional (5.3.2):** Calcule la **Función de Densidad Condicional** $f_{X|Y}(x|y)$ para un valor de tasa de degradación $Y=y$ dado[cite: 936]. ¿Son $X$ y $Y$ variables aleatorias independientes? [cite_start]Justifique su respuesta[cite: 935].
3.  **Esperanza Condicional (5.4.1):** Calcule la **Esperanza Condicional** del diámetro, dado un valor de tasa de degradación, $E[X | [cite_start]Y=y]$[cite: 936].
4.  **Covarianza (5.2.2):** Calcule la **Covarianza** $\text{Cov}[X, Y]$. [cite_start]¿Qué implica este valor acerca de la relación entre el diámetro de la nanopartícula y su tasa de degradación?[cite: 936].

### Solución: Síntesis y Degradación de Nanopartículas de Oro

## Datos del Problema

Tenemos la función de densidad de probabilidad conjunta:
$$f_{X,Y}(x, y) = c \cdot x \cdot e^{-(x+2y)} \cdot \mathbb{I}_{\{x \ge 0, y \ge 0\}}$$

---

## 1. Normalización y Función Marginal

### Determinación de la constante $c$

Para que $f_{X,Y}(x,y)$ sea una función de densidad válida, debe cumplirse:
$$\int_{0}^{\infty} \int_{0}^{\infty} c \cdot x \cdot e^{-(x+2y)} \, dx \, dy = 1$$

Separamos la exponencial:
$$c \int_{0}^{\infty} \int_{0}^{\infty} x \cdot e^{-x} \cdot e^{-2y} \, dx \, dy = 1$$

$$c \left(\int_{0}^{\infty} x \cdot e^{-x} \, dx\right) \left(\int_{0}^{\infty} e^{-2y} \, dy\right) = 1$$

**Calculamos cada integral:**

- Para $\int_{0}^{\infty} x \cdot e^{-x} \, dx$: Esta es $\Gamma(2) = 1! = 1$

- Para $\int_{0}^{\infty} e^{-2y} \, dy = \left[-\frac{1}{2}e^{-2y}\right]_{0}^{\infty} = \frac{1}{2}$

Por lo tanto:
$$c \cdot 1 \cdot \frac{1}{2} = 1 \implies c = 2$$

### Función de Densidad Marginal $f_Y(y)$

$$f_Y(y) = \int_{0}^{\infty} f_{X,Y}(x,y) \, dx = \int_{0}^{\infty} 2x \cdot e^{-(x+2y)} \, dx$$

$$= 2e^{-2y} \int_{0}^{\infty} x \cdot e^{-x} \, dx = 2e^{-2y} \cdot 1 = 2e^{-2y}, \quad y \ge 0$$

**Respuesta:** $\boxed{c = 2}$ y $\boxed{f_Y(y) = 2e^{-2y}, \, y \ge 0}$

---

## 2. Probabilidad Condicional e Independencia

### Función de Densidad Condicional $f_{X|Y}(x|y)$

$$f_{X|Y}(x|y) = \frac{f_{X,Y}(x,y)}{f_Y(y)} = \frac{2x \cdot e^{-(x+2y)}}{2e^{-2y}} = x \cdot e^{-x}, \quad x \ge 0$$

### ¿Son $X$ y $Y$ independientes?

Para que $X$ y $Y$ sean independientes, debe cumplirse que:
$$f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$$

Primero calculamos $f_X(x)$:
$$f_X(x) = \int_{0}^{\infty} 2x \cdot e^{-(x+2y)} \, dy = 2x \cdot e^{-x} \int_{0}^{\infty} e^{-2y} \, dy = 2x \cdot e^{-x} \cdot \frac{1}{2} = x \cdot e^{-x}$$

Verificamos:
$$f_X(x) \cdot f_Y(y) = (x \cdot e^{-x}) \cdot (2e^{-2y}) = 2x \cdot e^{-(x+2y)} = f_{X,Y}(x,y) \checkmark$$

**Respuesta:** $\boxed{f_{X|Y}(x|y) = x \cdot e^{-x}, \, x \ge 0}$

**Sí, $X$ y $Y$ son independientes** porque la densidad conjunta se factoriza como el producto de las marginales.

---

## 3. Esperanza Condicional

$$E[X | Y=y] = \int_{0}^{\infty} x \cdot f_{X|Y}(x|y) \, dx = \int_{0}^{\infty} x \cdot (x \cdot e^{-x}) \, dx$$

$$= \int_{0}^{\infty} x^2 \cdot e^{-x} \, dx = \Gamma(3) = 2! = 2$$

Observemos que como $X$ y $Y$ son independientes, $E[X|Y=y] = E[X]$ (no depende de $y$).

**Respuesta:** $\boxed{E[X | Y=y] = 2 \text{ nm}}$

---

## 4. Covarianza

Para variables aleatorias independientes, la covarianza es cero:
$$\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$$

Como $X$ y $Y$ son independientes:
$$E[XY] = E[X] \cdot E[Y]$$

Por lo tanto:
$$\text{Cov}(X,Y) = E[X] \cdot E[Y] - E[X] \cdot E[Y] = 0$$

**Verificación directa:**
- $E[X] = 2$ (calculado arriba)
- $E[Y] = \int_{0}^{\infty} y \cdot 2e^{-2y} \, dy = 2 \int_{0}^{\infty} y \cdot e^{-2y} \, dy = 2 \cdot \frac{1}{4} = \frac{1}{2}$
- $E[XY] = E[X] \cdot E[Y] = 2 \cdot \frac{1}{2} = 1$
- $\text{Cov}(X,Y) = 1 - 2 \cdot \frac{1}{2} = 0$

**Respuesta:** $\boxed{\text{Cov}(X,Y) = 0}$

**Interpretación:** La covarianza cero confirma que **no existe relación lineal entre el diámetro de la nanopartícula y su tasa de degradación**. Esto tiene sentido dado que las variables son estadísticamente independientes: conocer el diámetro de la nanopartícula no proporciona información sobre su tasa de degradación, y viceversa. En el contexto del nanosensor, esto sugiere que estos dos parámetros están controlados por mecanismos diferentes e independientes en el proceso de fabricación.

### Interpretación del Problema en Nanotecnología

El problema matemático se enmarca en la modelización de las propiedades de las **nanopartículas de oro (NPO)**, cruciales para aplicaciones en **nanosensores** y **sistemas de administración de fármacos**.

| Variable Aleatoria | Interpretación Nanotecnológica | Unidad |
| :--- | :--- | :--- |
| **$X$** | **Diámetro (o tamaño)** de la nanopartícula de oro (NPO). | $\text{nm}$ (nanómetros) |
| **$Y$** | **Tasa de degradación** (o velocidad de disolución) de la nanopartícula en un medio biológico/solución. | $\text{unidades de tasa}$ |
| **$f_{X,Y}(x, y)$** | **Función de Densidad Conjunta** que describe la probabilidad de que una NPO sintetizada tenga simultáneamente un **diámetro $x$** y una **tasa de degradación $y$**. | |

---

### Puntos Clave de la Solución y su Significado

#### 1. Normalización y Distribuciones

* **Constante $c=2$**: Asegura que la probabilidad total de todas las combinaciones posibles de tamaño y tasa de degradación sea igual a 1.
* **Marginal $f_Y(y) = 2e^{-2y}$**: Esta es la distribución de probabilidad de la **Tasa de Degradación ($Y$)** por sí sola. Indica cómo de probables son las diferentes velocidades de degradación, ignorando el tamaño. Es una **distribución exponencial**, lo que sugiere que las tasas de degradación bajas son más probables que las altas.
* **Marginal $f_X(x) = x \cdot e^{-x}$**: Esta es la distribución de probabilidad del **Diámetro ($X$)** por sí solo. Es una forma de la **distribución Gamma** (con parámetros $\alpha=2, \beta=1$), que es común para modelar el tamaño de las partículas en un proceso de síntesis. La distribución indica que los diámetros muy pequeños son improbables, la mayoría de las partículas tienen un tamaño alrededor de un valor modal (en este caso, 1 nm), y los tamaños muy grandes son cada vez más raros.

#### 2. Independencia Estadística

* **Resultado**: Las variables $X$ (Diámetro) y $Y$ (Tasa de Degradación) son **independientes**.
* **Significado Nanotecnológico**: Esto implica que la forma en que el proceso de síntesis controla el **tamaño final** de las nanopartículas **no influye** en la **velocidad a la que se degradan** en el medio, y viceversa. Si fueran dependientes, por ejemplo, al saber que una partícula tiene un diámetro de 5 nm, se podría predecir mejor si se degradará rápido o lento. La independencia sugiere que dos mecanismos o factores de control totalmente separados rigen estas dos propiedades.

#### 3. Esperanza Condicional

* **Resultado**: $E[X | Y=y] = 2\text{ nm}$.
* **Significado Nanotecnológico**: $\mathbf{E[X] = 2\text{ nm}}$ es el **diámetro promedio esperado** de las nanopartículas en el lote sintetizado. Dado que la independencia fue demostrada, esta media no depende de la tasa de degradación ($Y$). Esto refuerza el punto de independencia: conocer la tasa de degradación de una partícula **no cambia** nuestra expectativa sobre su tamaño medio.

#### 4. Covarianza

* **Resultado**: $\text{Cov}(X,Y) = 0$.
* **Significado Nanotecnológico**: Una covarianza de cero es consistente con la independencia y significa que **no hay una relación lineal** entre el diámetro y la tasa de degradación. Si la covarianza hubiera sido positiva, indicaría que las nanopartículas grandes tienden a degradarse más rápido (y viceversa para negativa). El resultado cero corrobora que estos dos parámetros no están linealmente relacionados.

---

##  Importancia para la Ingeniería en Nanotecnología

Este tipo de análisis es fundamental para la **Ingeniería de Nanomateriales** por varias razones:

1.  **Control de Calidad y Rendimiento (Yield)**: En la fabricación de nanomateriales, el objetivo es maximizar la cantidad de partículas con las **propiedades deseadas** (por ejemplo, diámetros entre 1.5 y 2.5 nm). Los ingenieros en Nanotecnología usan este tipo de modelos de distribución para:
    * **Cuantificar la Monodispersidad**: Medir qué tan estrecho es el rango de tamaños ($X$) de las partículas.
    * **Predecir el Lote**: Estimar el porcentaje del lote total que cumplirá con los requisitos de tamaño y estabilidad.

2.  **Diseño de Nanosistemas (Ej. Terapia)**:
    * Para la **administración de fármacos**, el **diámetro ($X$)** determina cómo la nanopartícula interactúa con las células y tejidos.
    * La **tasa de degradación ($Y$)** determina la **cinética de liberación** del fármaco. Si el fármaco debe liberarse lentamente, se necesita una tasa de degradación baja.
    * La **independencia** es clave aquí: si se puede optimizar el tamaño para la focalización y la tasa de degradación para la liberación, **sin que afecte uno al otro**, el proceso de optimización del nanosistema es mucho más sencillo y robusto.

3.  **Optimización de Síntesis**: La función de densidad conjunta ($f_{X,Y}$) es la "huella digital" del **proceso de síntesis**. Un ingeniero podría modificar parámetros como la temperatura, el pH o la concentración de precursores. Al medir los cambios en $f_{X,Y}$ (y sus marginales), se puede entender cómo cada ajuste afecta el tamaño, la estabilidad, y la relación entre ambos, permitiendo una **optimización sistemática** del proceso de fabricación a escala nanométrica.

En resumen, este problema usa la **Probabilidad y la Estadística** como una **herramienta matemática de control de procesos** para describir y predecir la variabilidad inherente en las propiedades de las nanopartículas, esencial para pasar de la investigación al desarrollo de productos nanotecnológicos fiables.

---

### Solución de Pyhton

```python
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

## ---------------------------------------------------------------
## 1) DEFINICIÓN DE VARIABLES Y FUNCIÓN CONJUNTA
## ---------------------------------------------------------------
x, y, c = sp.symbols('x y c', positive=True)

## Función de densidad conjunta
f_xy = c * x * sp.exp(-(x + 2*y))  # f_{X,Y}(x,y) = c*x*e^{-(x+2y)}

## ---------------------------------------------------------------
## 2) NORMALIZACIÓN -> encontrar c
## ---------------------------------------------------------------
integral_total = sp.integrate(sp.integrate(f_xy, (x, 0, sp.oo)), (y, 0, sp.oo))
c_value = sp.solve(sp.Eq(integral_total, 1), c)[0]

print(f"Constante de normalización: c = {c_value}")

## Sustituimos c en la función conjunta
f_xy_c = f_xy.subs(c, c_value)

## ---------------------------------------------------------------
## 3) FUNCIONES MARGINALES
## ---------------------------------------------------------------
f_x = sp.simplify(sp.integrate(f_xy_c, (y, 0, sp.oo)))
f_y = sp.simplify(sp.integrate(f_xy_c, (x, 0, sp.oo)))

print("\nFunción marginal f_X(x):", f_x)
print("Función marginal f_Y(y):", f_y)

## ---------------------------------------------------------------
## 4) FUNCIÓN CONDICIONAL f_{X|Y}(x|y)
## ---------------------------------------------------------------
f_x_given_y = sp.simplify(f_xy_c / f_y)
print("\nFunción de densidad condicional f_{X|Y}(x|y):", f_x_given_y)

## ---------------------------------------------------------------
## 5) ESPERANZA CONDICIONAL E[X|Y=y]
## ---------------------------------------------------------------
E_X_given_y = sp.simplify(sp.integrate(x * f_x_given_y, (x, 0, sp.oo)))
print("\nEsperanza condicional E[X|Y=y] =", E_X_given_y)

## ---------------------------------------------------------------
## 6) ESPERANZAS INDIVIDUALES Y COVARIANZA
## ---------------------------------------------------------------
E_X = sp.integrate(x * f_x, (x, 0, sp.oo))
E_Y = sp.integrate(y * f_y, (y, 0, sp.oo))
E_XY = sp.integrate(sp.integrate(x * y * f_xy_c, (x, 0, sp.oo)), (y, 0, sp.oo))
Cov_XY = sp.simplify(E_XY - E_X * E_Y)

print("\nE[X] =", E_X)
print("E[Y] =", E_Y)
print("E[XY] =", E_XY)
print("Cov(X,Y) =", Cov_XY)

## ---------------------------------------------------------------
## 7) VERIFICACIÓN DE INDEPENDENCIA
## ---------------------------------------------------------------
factorization_check = sp.simplify(f_x * f_y - f_xy_c)
print("\nVerificación independencia (f_X * f_Y - f_{X,Y}):", factorization_check)
if factorization_check == 0:
    print("✅ X y Y son independientes.")
else:
    print("❌ X y Y no son independientes.")

## ---------------------------------------------------------------
## 8) RESULTADOS RESUMIDOS
## ---------------------------------------------------------------
print("\n===== RESULTADOS FINALES =====")
print(f"Constante de normalización c = {c_value}")
print(f"f_X(x) = {f_x}")
print(f"f_Y(y) = {f_y}")
print(f"f_{{X|Y}}(x|y) = {f_x_given_y}")
print(f"E[X|Y=y] = {E_X_given_y}")
print(f"E[X] = {E_X},   E[Y] = {E_Y}")
print(f"Cov(X,Y) = {Cov_XY}")

## ---------------------------------------------------------------
## 9) GRAFICAR DENSIDADES MARGINALES
## ---------------------------------------------------------------
f_x_func = sp.lambdify(x, f_x, 'numpy')
f_y_func = sp.lambdify(y, f_y, 'numpy')

x_vals = np.linspace(0, 10, 400)
y_vals = np.linspace(0, 5, 400)

plt.figure(figsize=(6,4))
plt.plot(x_vals, f_x_func(x_vals))
plt.title("Densidad marginal f_X(x) = x·e^{-x}")
plt.xlabel("x (nm)")
plt.ylabel("f_X(x)")
plt.grid(True)
plt.show()

plt.figure(figsize=(6,4))
plt.plot(y_vals, f_y_func(y_vals))
plt.title("Densidad marginal f_Y(y) = 2·e^{-2y}")
plt.xlabel("y (nm/semana)")
plt.ylabel("f_Y(y)")
plt.grid(True)
plt.show()
```

## Problema 2: Control de Calidad de Nanochips (Random Vectors, PCA, Sum of Random Variables)

En la producción masiva de un **nanochip** de memoria, dos parámetros de rendimiento, $P_1$ y $P_2$, se miden al final de la línea de montaje. Estos parámetros se modelan como un **Vector Aleatorio** $\mathbf{X} = [P_1, P_2]^T$, con un vector de medias $\mathbf{\mu} = [5, 10]^T$ y la siguiente **Matriz de Covarianza (Covariance Matrix)** $\mathbf{C}$:

$$\mathbf{C} = \begin{pmatrix} 2 & 1 \\ 1 & 5 \end{pmatrix}$$

1.  [cite_start]**Correlación y Dependencia (5.2.2, 5.6.3):** Calcule el **coeficiente de correlación** $\rho$ entre los parámetros $P_1$ y $P_2$[cite: 936].
2.  [cite_start]**Análisis de Componentes Principales (PCA) (5.7.2, 5.8.1):** Para realizar un análisis de **Componentes Principales (PCA)** y comprender la máxima varianza del sistema, obtenga los **Eigenvalores** $\lambda_1$ y $\lambda_2$ de la matriz de covarianza $\mathbf{C}$[cite: 936]. [cite_start]¿Cuál es la varianza total del vector aleatorio $\mathbf{X}$ y cómo se relaciona con sus eigenvalores?[cite: 936].
3.  **Transformación y Suma de Variables Aleatorias (5.5.2):** Un nuevo índice de rendimiento del chip, R, se define como la suma ponderada $R = 2P_1 + P_2$. [cite_start]Calcule la **Varianza** de este nuevo índice, $\text{Var}[R]$[cite: 936].
4.  [cite_start]**Distribución Multidimensional (5.6.4):** Asumiendo que $\mathbf{X}$ sigue una **Distribución Gaussiana Multidimensional**[cite: 936]. [cite_start]Si el control de calidad requiere que el índice R sea superior a 25. Describa detalladamente los pasos a seguir para calcular la probabilidad de que un chip pase el control de calidad, $P[R > 25]$, utilizando la función de distribución acumulada (CDF) de una variable Gaussiana unidimensional[cite: 936].

### Solución: Control de Calidad de Nanochips

## Datos del Problema

Vector aleatorio: $\mathbf{X} = [P_1, P_2]^T$

Vector de medias: $\mathbf{\mu} = [5, 10]^T$

Matriz de covarianza: $\mathbf{C} = \begin{pmatrix} 2 & 1 \\ 1 & 5 \end{pmatrix}$

---

## 1. Coeficiente de Correlación

El **coeficiente de correlación** entre $P_1$ y $P_2$ se calcula como:

$$\rho(P_1, P_2) = \frac{\text{Cov}(P_1, P_2)}{\sqrt{\text{Var}(P_1)} \cdot \sqrt{\text{Var}(P_2)}}$$

De la matriz de covarianza:
- $\text{Var}(P_1) = C_{11} = 2$
- $\text{Var}(P_2) = C_{22} = 5$
- $\text{Cov}(P_1, P_2) = C_{12} = 1$

Por lo tanto:
$$\rho = \frac{1}{\sqrt{2} \cdot \sqrt{5}} = \frac{1}{\sqrt{10}} = \frac{\sqrt{10}}{10} \approx 0.316$$

**Respuesta:** $\boxed{\rho = \frac{1}{\sqrt{10}} \approx 0.316}$

**Interpretación:** Existe una correlación positiva débil entre los parámetros $P_1$ y $P_2$, lo que indica que tienden a aumentar juntos, pero la relación lineal no es fuerte.

---

## 2. Análisis de Componentes Principales (PCA)

### Cálculo de Eigenvalores

Los eigenvalores se obtienen resolviendo:
$$\det(\mathbf{C} - \lambda \mathbf{I}) = 0$$

$$\det\begin{pmatrix} 2-\lambda & 1 \\ 1 & 5-\lambda \end{pmatrix} = 0$$

$$(2-\lambda)(5-\lambda) - 1 = 0$$

$$10 - 2\lambda - 5\lambda + \lambda^2 - 1 = 0$$

$$\lambda^2 - 7\lambda + 9 = 0$$

Usando la fórmula cuadrática:
$$\lambda = \frac{7 \pm \sqrt{49 - 36}}{2} = \frac{7 \pm \sqrt{13}}{2}$$

$$\lambda_1 = \frac{7 + \sqrt{13}}{2} \approx 5.303$$

$$\lambda_2 = \frac{7 - \sqrt{13}}{2} \approx 1.697$$

### Varianza Total

La **varianza total** del vector aleatorio es:
$$\text{Var}_{\text{total}} = \text{Var}(P_1) + \text{Var}(P_2) = 2 + 5 = 7$$

**Propiedad fundamental:** La varianza total es igual a la suma de los eigenvalores:
$$\text{Var}_{\text{total}} = \lambda_1 + \lambda_2 = \frac{7 + \sqrt{13}}{2} + \frac{7 - \sqrt{13}}{2} = 7 \checkmark$$

**Respuesta:**
$$\boxed{\lambda_1 = \frac{7 + \sqrt{13}}{2} \approx 5.303, \quad \lambda_2 = \frac{7 - \sqrt{13}}{2} \approx 1.697}$$

$$\boxed{\text{Var}_{\text{total}} = 7}$$

**Interpretación PCA:** El primer componente principal (asociado a $\lambda_1$) captura aproximadamente el 75.8% de la varianza total del sistema, mientras que el segundo componente captura el 24.2% restante.

---

## 3. Varianza del Índice de Rendimiento

Dado $R = 2P_1 + P_2$, podemos expresarlo como:
$$R = \mathbf{a}^T \mathbf{X}$$

donde $\mathbf{a} = [2, 1]^T$.

La varianza de una transformación lineal es:
$$\text{Var}(R) = \mathbf{a}^T \mathbf{C} \mathbf{a}$$

Calculamos:
$$\mathbf{C} \mathbf{a} = \begin{pmatrix} 2 & 1 \\ 1 & 5 \end{pmatrix} \begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 4 + 1 \\ 2 + 5 \end{pmatrix} = \begin{pmatrix} 5 \\ 7 \end{pmatrix}$$

$$\mathbf{a}^T (\mathbf{C} \mathbf{a}) = [2, 1] \begin{pmatrix} 5 \\ 7 \end{pmatrix} = 10 + 7 = 17$$

**Verificación alternativa:**
$$\text{Var}(R) = \text{Var}(2P_1 + P_2) = 4\text{Var}(P_1) + \text{Var}(P_2) + 2 \cdot 2 \cdot 1 \cdot \text{Cov}(P_1, P_2)$$
$$= 4(2) + 5 + 4(1) = 8 + 5 + 4 = 17 \checkmark$$

**Respuesta:** $\boxed{\text{Var}(R) = 17}$

---

## 4. Probabilidad de Control de Calidad

### Distribución de R

Si $\mathbf{X} \sim \mathcal{N}(\mathbf{\mu}, \mathbf{C})$, entonces cualquier combinación lineal de sus componentes también sigue una distribución normal.

Para $R = 2P_1 + P_2$:

**Media de R:**
$$E[R] = 2E[P_1] + E[P_2] = 2(5) + 10 = 20$$

**Desviación estándar de R:**
$$\sigma_R = \sqrt{\text{Var}(R)} = \sqrt{17} \approx 4.123$$

Por lo tanto:
$$R \sim \mathcal{N}(20, 17)$$

### Pasos para Calcular $P(R > 25)$

**Paso 1:** Estandarizar la variable aleatoria

Transformamos R a una variable normal estándar $Z \sim \mathcal{N}(0,1)$ usando:
$$Z = \frac{R - E[R]}{\sigma_R} = \frac{R - 20}{\sqrt{17}}$$

**Paso 2:** Expresar la probabilidad en términos de Z

$$P(R > 25) = P\left(\frac{R - 20}{\sqrt{17}} > \frac{25 - 20}{\sqrt{17}}\right) = P\left(Z > \frac{5}{\sqrt{17}}\right)$$

**Paso 3:** Calcular el valor estandarizado

$$z = \frac{5}{\sqrt{17}} \approx \frac{5}{4.123} \approx 1.213$$

**Paso 4:** Usar la función de distribución acumulada (CDF)

La función CDF de la normal estándar es $\Phi(z) = P(Z \leq z)$

Por la propiedad de complemento:
$$P(R > 25) = P(Z > 1.213) = 1 - \Phi(1.213)$$

**Paso 5:** Consultar tabla o usar software

Usando tablas estándar o software estadístico:
$$\Phi(1.213) \approx 0.8874$$

Por lo tanto:
$$P(R > 25) = 1 - 0.8874 = 0.1126$$

**Respuesta:**

$$\boxed{P(R > 25) = 1 - \Phi\left(\frac{5}{\sqrt{17}}\right) \approx 0.113 \text{ o } 11.3\%}$$

**Interpretación:** Aproximadamente el 11.3% de los nanochips pasarán el control de calidad con un índice de rendimiento superior a 25. Esto sugiere que el estándar de calidad es relativamente exigente dado los parámetros de producción actuales.

### Interpretación del Problema en Nanotecnología

El problema se centra en el **Control de Calidad (QC)** de un dispositivo crítico en la nanoelectrónica: un **nanochip** de memoria o procesador.

* **Vector Aleatorio $\mathbf{X} = [P_1, P_2]^T$**: Representa la variación inherente en las propiedades físicas y eléctricas de los componentes nanométricos (como transistores o celdas de memoria) que, en última instancia, definen el rendimiento del chip.
    * **$P_1$ y $P_2$** son dos **parámetros de rendimiento clave** que pueden representar, por ejemplo: la velocidad de conmutación de un nanotubo de carbono (CNT) en $\text{GHz}$, la corriente de fuga de un transistor de efecto de campo (FET) a escala nanométrica en $\text{nA}$, o la confiabilidad de una celda de memoria $\text{MRAM}$.

* **Matriz de Covarianza $\mathbf{C}$**: Contiene la información esencial sobre la **variabilidad de la producción**.
    * Las entradas diagonales ($\text{Var}(P_1)=2$ y $\text{Var}(P_2)=5$) indican la varianza individual de cada parámetro.
    * La entrada fuera de la diagonal ($\text{Cov}(P_1, P_2)=1$) describe cómo el proceso de fabricación acopla los dos parámetros.

---

## Significado Nanotecnológico de los Resultados

### 1. Correlación y Dependencia

* **Resultado**: $\rho \approx 0.316$ (Correlación positiva débil).
* **Significado ING-NT**: Esta correlación implica que si los factores de producción (temperatura, tiempo de deposición, litografía) hacen que el parámetro $P_1$ sea mayor de lo esperado, es **ligeramente más probable** que $P_2$ también lo sea. La correlación débil sugiere que $P_1$ y $P_2$ son en gran medida **controlados por mecanismos de proceso diferentes o independientes**, lo que es una buena noticia para la robustez del chip, ya que el fallo en un parámetro no implica un fallo total en el otro.

### 2. Análisis de Componentes Principales (PCA)

* **Resultado**: $\lambda_1 \approx 5.303$ y $\lambda_2 \approx 1.697$. Varianza Total $= 7$.
* **Significado ING-NT**: PCA permite a los ingenieros de procesos identificar la **fuente principal de variabilidad** en el nanochip.
    * El primer componente principal (asociado a $\lambda_1$) explica el $75.8\%$ de la varianza total. Este componente es una combinación lineal de $P_1$ y $P_2$ que representa la **dirección de máxima inestabilidad o dispersión** en la producción.
    * Al identificar la **eigenvector** asociado a $\lambda_1$, el ingeniero sabe **exactamente qué combinación de $P_1$ y $P_2$ debe optimizar o estabilizar** para mejorar la uniformidad del lote. Por ejemplo, si el vector indica que $P_2$ tiene un peso mucho mayor, las acciones de control de calidad deben enfocarse principalmente en reducir la variabilidad del proceso que afecta a $P_2$ (como el espesor de una capa atómica).

### 3. Varianza del Índice de Rendimiento

* **Resultado**: $\text{Var}[R] = 17$. El índice $R = 2P_1 + P_2$.
* **Significado ING-NT**: En la práctica, a menudo se combinan las especificaciones para obtener un **índice de mérito** o un **índice de rendimiento total** (R).
    * La fórmula $\text{Var}[R] = \mathbf{a}^T \mathbf{C} \mathbf{a}$ permite **predecir la dispersión del rendimiento final (R)** con base en la varianza individual y la covarianza de los parámetros constituyentes.
    * En este caso, $P_1$ tiene el doble de peso. La varianza $\text{Var}[R]=17$ es mucho mayor que la suma de varianzas individuales (considerando pesos), lo que subraya la importancia de considerar la **covarianza** y los **pesos** en el diseño de chips. Un alto valor de $\text{Var}[R]$ significa una **mayor tasa de chips desechados** debido a la amplia dispersión en el rendimiento final.

### 4. Probabilidad de Control de Calidad

* **Resultado**: $P[R > 25] \approx 11.3\%$.
* **Significado ING-NT**: Esta es la métrica de producción más crítica. Representa el **rendimiento ($Yield$)** del proceso de fabricación. Un rendimiento del $11.3\%$ significa que casi el $89\%$ de los nanochips no cumplen con el estándar de calidad y deben ser descartados.
    * **Acción del Ingeniero**: Un valor tan bajo es inaceptable en producción masiva. El ingeniero debe usar los resultados de **PCA** y **Correlación** para:
        1.  Identificar y estabilizar la fuente de la varianza principal (relacionada con $\lambda_1$).
        2.  Ajustar el proceso para aumentar el vector de medias $\mathbf{\mu}$ (el rendimiento promedio) de $[5, 10]^T$ a valores más altos.
    * El uso de la distribución Gaussiana Multidimensional es la herramienta estándar para modelar estas variaciones en la micro y nanoelectrónica, ya que asume que las variaciones provienen de la acumulación de muchos errores aleatorios de procesamiento.

---

## Importancia para la Carrera de Ing. en Nanotecnología

Este problema es la base de la **Ingeniería de Procesos a Nanoescala**:

1.  **Diseño Robusto (Design for Manufacturing - DFM)**: Un ingeniero de NT debe diseñar nanochips que funcionen correctamente incluso con las inevitables variaciones atómicas del proceso. Este análisis permite cuantificar la robustez del diseño.
2.  **Optimización de Producción y Costos**: El rendimiento ($Yield$) se relaciona directamente con los costos de fabricación. Un ingeniero debe usar estas técnicas para subir el rendimiento del $11.3\%$ a un valor comercialmente viable ($>80\%$).
3.  **Análisis de Grandes Datos (Big Data)**: En una fábrica moderna de nanochips, se recogen miles de datos de parámetros. Las técnicas de **PCA** son esenciales para reducir la dimensionalidad de estos datos, aislar las variables más importantes y tomar decisiones de ajuste de procesos basadas en la varianza. El dominio de la **Estadística Multivariada** es una competencia técnica esencial para cualquier ingeniero de procesos en Nanotecnología.

### Solución en Python

```python
import numpy as np
import sympy as sp
from scipy.stats import norm

## ---------------------------
## Datos del problema
## ---------------------------
mu = np.array([5, 10])  # vector de medias [E[P1], E[P2]]
C = np.array([[2, 1],    # matriz de covarianza
              [1, 5]])

## ---------------------------
## 1. Coeficiente de Correlación
## ---------------------------
Var_P1 = C[0, 0]
Var_P2 = C[1, 1]
Cov_P1P2 = C[0, 1]

rho = Cov_P1P2 / np.sqrt(Var_P1 * Var_P2)

print("1️ Coeficiente de correlación (ρ):")
print(f"ρ = {rho:.3f}")
print("Interpretación: correlación positiva débil.\n")

## ---------------------------
## 2. Análisis de Componentes Principales (PCA)
## ---------------------------
## Cálculo de eigenvalores y eigenvectores
eigenvalores, eigenvectores = np.linalg.eig(C)

lambda1, lambda2 = sorted(eigenvalores, reverse=True)
var_total = np.trace(C)

print("2️ PCA - Eigenvalores y Varianza Total:")
print(f"λ₁ = {lambda1:.3f}, λ₂ = {lambda2:.3f}")
print(f"Varianza total = {var_total}")
print(f"Comprobación: suma de eigenvalores = {sum(eigenvalores):.3f}\n")

## Porcentaje de varianza explicada
perc1 = lambda1 / var_total * 100
perc2 = lambda2 / var_total * 100
print(f"Componente principal 1 explica {perc1:.1f}% de la varianza total.")
print(f"Componente principal 2 explica {perc2:.1f}% de la varianza total.\n")

## ---------------------------
## 3. Varianza del índice R = 2P1 + P2
## ---------------------------
a = np.array([2, 1])  # vector de pesos
Var_R = a.T @ C @ a   # Var(R) = aᵀ * C * a

print("3️ Varianza del índice R = 2P1 + P2:")
print(f"Var[R] = {Var_R:.3f}\n")

## ---------------------------
## 4. Probabilidad de Control de Calidad: P(R > 25)
## ---------------------------
## Media y desviación estándar de R
E_R = a.T @ mu
sigma_R = np.sqrt(Var_R)

## Estandarización y probabilidad
z = (25 - E_R) / sigma_R
P_R_mayor_25 = 1 - norm.cdf(z)

print("4️ Probabilidad de que el chip pase control de calidad (R > 25):")
print(f"E[R] = {E_R:.3f}")
print(f"σ_R = {sigma_R:.3f}")
print(f"z = {z:.3f}")
print(f"P(R > 25) = {P_R_mayor_25:.4f}  →  {P_R_mayor_25*100:.2f}%\n")

## ---------------------------
## Interpretación final
## ---------------------------
print(" Interpretación Nanotecnológica:")
print(f"- Correlación ρ ≈ {rho:.3f}: dependencia débil entre P1 y P2.")
print(f"- PCA: λ₁ ≈ {lambda1:.3f} explica {perc1:.1f}% de la variabilidad.")
print(f"- Varianza del índice R = {Var_R:.1f}: alta dispersión del rendimiento.")
print(f"- Solo {P_R_mayor_25*100:.1f}% de los chips superan el control de calidad.")
```

---

## Resumen del Protocolo Maestro
- **Solución Analítica Resaltada**: $\boxed{\text{Verificado con SymPy y SciPy stats}}$
- **Verificación Simbólica (SymPy)**:


---

## 10. Módulo de Simulación: Método de Monte Carlo para Eventos Probabilísticos Complejos

La **Simulación de Monte Carlo** permite estimar probabilidades de eventos aleatorios complejos mediante la generación repetida de números seudoaleatorios según la Ley Fuerte de los Grandes Números.

### 20.1 Teorema Fundamental de Monte Carlo
Sea $E$ un evento de interés con probabilidad $P(E) = p$. Al generar $N$ simulaciones independientes donde $X_i = 1$ si ocurre $E$ y $0$ en otro caso:
$$\lim_{N \o \infty} \frac{1}{N} \sum_{i=1}^N X_i = P(E) \quad \text{con probabilidad 1}$$

### 20.2 Simulación de Filtrado de Nanopartículas por Monte Carlo
```python
import numpy as np
import scipy.stats as stats
from IPython.display import display, Math

## Simulación de Monte Carlo (N = 100,000 experimentos)
N = 100_000
np.random.seed(42)

## Dos filtros coloidales independientes con probabilidades de paso p1=0.85, p2=0.90
paso_filtro1 = stats.bernoulli.rvs(p=0.85, size=N)
paso_filtro2 = stats.bernoulli.rvs(p=0.90, size=N)

## Evento: La partícula atraviesa ambos filtros
exito_ambos = paso_filtro1 & paso_filtro2
prob_simulada = np.mean(exito_ambos)
prob_teorica = 0.85 * 0.90

display(Math(fr"\text{{Probabilidad Teórica }} P(A \cap B): {prob_teorica:.4f}"))
display(Math(fr"\text{{Probabilidad Simulada Monte Carlo (N={N:,}): }} {prob_simulada:.4f}"))
display(Math(fr"\text{{Error Relativo: }} {abs(prob_simulada - prob_teorica)/prob_teorica * 100:.3f}\%"))
```


---
## 9. Verificación Simbólica y Expresión Formal con SymPy

En combinatoria y probabilidad, **SymPy** permite verificar analíticamente las fórmulas de permutaciones, combinaciones y el Teorema de Bayes.

### 9.1 Demostración Simbólica del Coeficiente Binomial $C(n,k)$

$$\boxed{C(n,k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}}$$

```python
import sympy as sp
from IPython.display import display, Math

# Definición de variables simbólicas
n, k = sp.symbols('n k', positive=True, integer=True)
comb_simbolica = sp.binomial(n, k)
formula_factorial = sp.factorial(n) / (sp.factorial(k) * sp.factorial(n - k))

display(Math(r'\text{Expresión Simbólica de Combinaciones } C(n,k): ' + sp.latex(comb_simbolica)))
display(Math(r'\text{Fórmula Analítica con Factoriales: } ' + sp.latex(formula_factorial)))

# Evaluación exacta para muestra de n=10 elementos en grupos de k=3
evaluacion = comb_simbolica.subs({n: 10, k: 3})
display(Math(fr'\text{{Resultado Exacto SymPy }} C(10, 3) = \mathbf{{{evaluacion}}}'))
```
