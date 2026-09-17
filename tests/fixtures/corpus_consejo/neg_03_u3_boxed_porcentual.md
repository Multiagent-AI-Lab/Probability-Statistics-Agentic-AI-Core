### 2.9 Profundización: PMF Completa, CDF y Aplicaciones por Dominio

Las subsecciones 2.1 a 2.8 dan la definición mínima de cada familia. Esta subsección profundiza las 8 distribuciones discretas del curso con su CDF explícita, código de comparación gráfica en `scipy.stats`, y ejemplos de uso concretos en **Nanotecnología**, **Inteligencia Artificial** y **Diseño de Experimentos (DOE)**.

#### 2.9.1 Distribución Bernoulli — Profundización

* **CDF**: $F(x) = 0$ si $x<0$; $F(x) = 1-p$ si $0\le x<1$; $F(x)=1$ si $x\ge 1$.
* Caso especial de la Binomial con $n=1$: `scipy.stats.bernoulli` es un atajo de `binom(n=1, p)`.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

## PMF de Bernoulli: probabilidad de que un nanosensor individual
## detecte correctamente un analito en una sola prueba (p=0.7)
p = 0.7
dist = bernoulli(p)
valores = [0, 1]
probabilidades = dist.pmf(valores)

plt.figure(figsize=(6, 4))
plt.bar(valores, probabilidades, color=["lightcoral", "skyblue"], edgecolor="black")
plt.xticks(valores, ["0 (fallo)", "1 (éxito)"])
plt.title(f"PMF Bernoulli(p={p})")
plt.ylabel("Probabilidad")
plt.ylim(0, 1)
plt.show()
```

**Nota de implementación**: como `bernoulli(p)` es exactamente `binom(n=1, p)`, ambas clases de `scipy.stats` son intercambiables — es común encontrar código que usa una u otra según la fuente. El siguiente fragmento reproduce el mismo resultado del bloque anterior usando `binom` directamente, para un nanosensor que detecta la presencia de un contaminante con probabilidad $p=0.9$ de operar correctamente en una sola prueba:

```python
from scipy.stats import binom

p_exito = 0.9
x = 1  # exito: sensor no contaminado

probabilidad_pmf = binom.pmf(k=x, n=1, p=p_exito)         # equivalente a bernoulli.pmf(x, p_exito)
probabilidad_cdf = binom.cdf(k=x, n=1, p=p_exito)         # equivalente a bernoulli.cdf(x, p_exito)

print(f"P(X={x}) via binom(n=1): {probabilidad_pmf:.4f}")
print(f"F({x}) via binom(n=1):   {probabilidad_cdf:.4f}")
```

**Aplicaciones**: (1) *Nanotecnología*: resultado binario de una sola prueba de control de calidad sobre un nanodispositivo (pasa/no pasa la especificación de espesor). (2) *IA*: unidad básica de clasificación binaria — la salida de una neurona con activación sigmoide seguida de umbral se modela como Bernoulli con $p$ igual a la probabilidad predicha. (3) *DOE*: resultado de un único ensayo experimental con dos desenlaces posibles (p. ej., una réplica de síntesis produce o no el polimorfo deseado).

#### 2.9.2 Distribución Binomial — Profundización

* **CDF**: $F(x) = P(X\le x) = \sum_{i=0}^{\lfloor x\rfloor} \binom{n}{i}p^i(1-p)^{n-i}$.
* Suma de $n$ Bernoulli($p$) independientes: modela el conteo total de éxitos en un número fijo de ensayos idénticos.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

## PMF Binomial: numero de nanoparticulas defectuosas en un lote de
## n=20 con probabilidad de defecto p=0.05 por particula
n, p = 20, 0.05
dist = binom(n, p)
k = np.arange(0, n + 1)

plt.figure(figsize=(8, 5))
plt.bar(k, dist.pmf(k), color="steelblue", edgecolor="black")
plt.title(f"PMF Binomial(n={n}, p={p})")
plt.xlabel("Número de defectos (k)")
plt.ylabel("Probabilidad")
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: número de nanopartículas defectuosas en un lote de tamaño fijo bajo una tasa de defecto constante por partícula — control de calidad de síntesis. (2) *IA*: número de predicciones correctas de un clasificador binario sobre un conjunto de prueba de tamaño fijo, bajo el supuesto de accuracy constante; fundamento del intervalo de confianza binomial para accuracy reportada. (3) *DOE*: número de réplicas exitosas de un experimento (p. ej., síntesis que alcanza la pureza objetivo) de un total de $n$ réplicas planeadas, para dimensionar el tamaño de muestra necesario.

#### 2.9.3 Distribución de Poisson — Profundización

* **CDF**: $F(x) = P(X\le x) = \sum_{i=0}^{\lfloor x\rfloor} \dfrac{\lambda^i e^{-\lambda}}{i!}$.
* Límite de la Binomial cuando $n\to\infty$, $p\to 0$ con $np=\lambda$ constante — modela conteos raros en un intervalo continuo de tiempo o espacio.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

## PMF Poisson: numero de fallas de un nano-dispositivo por cada
## 1000 horas de operacion, con tasa promedio lambda=4
lam = 4
dist = poisson(lam)
k = np.arange(0, 16)

plt.figure(figsize=(8, 5))
plt.bar(k, dist.pmf(k), color="darkorange", edgecolor="black")
plt.title(f"PMF Poisson($\\lambda$={lam})")
plt.xlabel("Número de eventos (k)")
plt.ylabel("Probabilidad")
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: número de fallas de un nano-dispositivo por unidad de tiempo de operación, o número de defectos puntuales por unidad de área en una película delgada. (2) *IA*: número de solicitudes que llega a un servidor de inferencia por unidad de tiempo, modelo base para dimensionar la capacidad de un sistema de predicción en producción. (3) *DOE*: número de eventos raros observados en un experimento de conteo (p. ej., número de núcleos de cristalización espontánea por unidad de volumen), fundamento de las pruebas de bondad de ajuste para procesos de conteo.

**Ejemplo — Análisis de doble cola de riesgo (dopaje de nanotransistores)**: en la fabricación de un nanotransistor, el número de átomos dopantes que terminan en el canal de conducción sigue $X \sim \text{Poisson}(\lambda=3)$ por unidad de volumen del canal. Un canal con **cero átomos dopantes** ($X=0$) es un fallo crítico (el transistor no conmuta); un canal con **6 o más** ($X\ge 6$) introduce variabilidad excesiva de voltaje umbral. A diferencia de los ejemplos anteriores, que evalúan un solo extremo de la distribución, aquí interesan **ambas colas simultáneamente**:

$$P(X=0) = \frac{3^0 e^{-3}}{0!} = e^{-3} \approx 0.0498, \qquad P(X\ge 6) = 1 - P(X\le 5) = 1 - F(5)$$

```python
from scipy.stats import poisson

lam = 3
riesgo_canal_vacio = poisson.pmf(0, mu=lam)        # PMF en un extremo: fallo por ausencia de dopantes
riesgo_exceso_dopantes = 1 - poisson.cdf(5, mu=lam)  # 1 - CDF en el otro extremo: fallo por exceso

print(f"P(X=0) — riesgo de canal sin dopar:        {riesgo_canal_vacio:.4f}")
print(f"P(X>=6) — riesgo de exceso de dopantes:    {riesgo_exceso_dopantes:.4f}")
print(f"Riesgo total combinado (ambas colas):      {riesgo_canal_vacio + riesgo_exceso_dopantes:.4f}")
```
El patrón de combinar `pmf` en un extremo con `1 - cdf` en el otro —ya usado de forma parcial en la Sección 3.4 para $P(X\ge1)$— se generaliza aquí a un análisis de **dos colas de riesgo distintas** sobre la misma distribución, típico de especificaciones de manufactura con límites tanto inferior como superior.

#### 2.9.4 Distribución Geométrica — Profundización

* **CDF**: $F(x) = P(X\le x) = 1-(1-p)^{\lfloor x\rfloor}$.
* Modela el número de ensayos Bernoulli($p$) independientes hasta (e incluyendo) el primer éxito; análogo discreto de la propiedad de falta de memoria de la Exponencial.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom

## PMF Geometrica: numero de intentos de sintesis hasta obtener el
## primer lote de nanoparticulas dentro de especificacion (p=0.3)
p = 0.3
dist = geom(p)
k = np.arange(1, 15)

plt.figure(figsize=(8, 5))
plt.bar(k, dist.pmf(k), color="seagreen", edgecolor="black")
plt.title(f"PMF Geométrica(p={p})")
plt.xlabel("Número de ensayos hasta el primer éxito (k)")
plt.ylabel("Probabilidad")
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: número de intentos de síntesis necesarios hasta obtener el primer lote de nanopartículas dentro de especificación, útil para estimar el costo esperado de un protocolo de bajo rendimiento. (2) *IA*: número de consultas a un modelo generativo hasta obtener la primera salida que pasa un filtro de calidad, relevante en técnicas de *rejection sampling*. (3) *DOE*: número de réplicas experimentales necesarias hasta observar el primer resultado exitoso, para planear el presupuesto de un experimento secuencial.

> ⚠️ **Cuidado con la convención de "fallas" vs. "ensayos"**: no todas las fuentes parametrizan la Geométrica igual. `scipy.stats.geom.pmf(x, p)` da la probabilidad de que el **ensayo número $x$** sea el primer éxito (soporte $x \in \{1,2,3,\dots\}$, la convención de esta lección). Otra convención común (usada, por ejemplo, en el paquete `stats` de R con `dgeom(k, p)`) da la probabilidad de observar exactamente $k$ **fallas antes** del éxito (soporte $k \in \{0,1,2,\dots\}$). Ambas describen el mismo fenómeno, pero difieren en un desplazamiento de índice: $k_{\text{fallas}} = x_{\text{ensayo}} - 1$, de modo que para obtener el mismo valor numérico hay que convertir explícitamente: `geom.pmf(k_fallas + 1, p)`. Confundir ambas convenciones al traducir una fórmula o código de una fuente a otra es un error silencioso — el código corre sin errores, pero calcula la probabilidad de un evento distinto (desplazado en 1) al que se pretendía.

#### 2.9.5 Distribución Binomial Negativa — Profundización

* **CDF**: sin forma cerrada simple; se evalúa numéricamente (`scipy.stats.nbinom.cdf`).
* Generaliza la Geométrica: modela el número de ensayos hasta obtener $r$ éxitos (no solo el primero). Para $r=1$ recupera la Geométrica.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nbinom

## PMF Binomial Negativa: numero de lotes de sintesis necesarios
## hasta obtener r=5 lotes dentro de especificacion (p=0.4)
r, p = 5, 0.4
dist = nbinom(r, p)
k = np.arange(0, 31)

plt.figure(figsize=(8, 5))
plt.bar(k, dist.pmf(k), color="mediumpurple", edgecolor="black")
plt.title(f"PMF Binomial Negativa(r={r}, p={p})")
plt.xlabel("Número de fallos antes del r-ésimo éxito (k)")
plt.ylabel("Probabilidad")
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: número de lotes de síntesis necesarios hasta acumular $r$ lotes dentro de especificación, para planificar la producción de un número fijo de muestras válidas. (2) *IA*: modelado de conteos con sobre-dispersión (varianza mayor que la media) en datos de conteo del mundo real, donde la Poisson resulta demasiado restrictiva — común en modelos de recuento de eventos raros con heterogeneidad. (3) *DOE*: número de réplicas experimentales necesarias hasta acumular un número objetivo de resultados exitosos, extendiendo el caso geométrico a metas de más de un éxito.

#### 2.9.6 Distribución Hipergeométrica — Profundización

* **CDF**: $F(x) = \sum_{j=0}^{\lfloor x\rfloor} \dfrac{\binom{K}{j}\binom{N-K}{n-j}}{\binom{N}{n}}$.
* A diferencia de la Binomial, modela muestreo **sin reemplazo** de una población finita — las probabilidades cambian con cada extracción.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom

## PMF Hipergeometrica: numero de nanoparticulas defectuosas al
## extraer una muestra de n=15 de un lote finito N=50 con K=10 defectuosas
N, K, n = 50, 10, 15
dist = hypergeom(N, K, n)
k = np.arange(0, min(K, n) + 1)

plt.figure(figsize=(8, 5))
plt.bar(k, dist.pmf(k), color="indianred", edgecolor="black")
plt.title(f"PMF Hipergeométrica(N={N}, K={K}, n={n})")
plt.xlabel("Número de defectuosas en la muestra (k)")
plt.ylabel("Probabilidad")
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: número de nanopartículas defectuosas al extraer una muestra de inspección de un lote finito de producción, sin reponer las unidades muestreadas — el caso realista de control de calidad destructivo. (2) *IA*: muestreo de un conjunto de datos finito (p. ej., seleccionar un subconjunto de validación sin reemplazo de un dataset fijo), relevante para el diseño de validación cruzada. (3) *DOE*: número de muestras con una característica de interés (p. ej., un lote de materia prima defectuoso) al extraer una muestra de auditoría de un envío finito, sin reposición.

#### 2.9.7 Distribución Uniforme Discreta — Profundización

* **CDF**: $F(x) = \dfrac{\lfloor x\rfloor - a + 1}{k}$ para $a\le x\le b$, con $k=b-a+1$.
* Todos los $k$ valores del rango $\{a,\dots,b\}$ son igualmente probables — es el generador discreto base para simulación por muestreo aleatorio simple.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import randint

## PMF Uniforme Discreta: seleccion aleatoria de una posicion de
## un chip de 6 sitios de reaccion en un ensayo de sintesis paralela
a, b = 1, 6
dist = randint(a, b + 1)
valores = np.arange(a, b + 1)

plt.figure(figsize=(7, 4))
plt.bar(valores, dist.pmf(valores), color="gold", edgecolor="black")
plt.title(f"PMF Uniforme Discreta en [{a}, {b}]")
plt.xlabel("Valor (x)")
plt.ylabel("Probabilidad")
plt.show()
```

**Aplicaciones**: (1) *Nanotecnología*: selección aleatoria de un sitio de reacción entre $k$ posiciones equivalentes en un chip de síntesis paralela, cuando no hay razón física para preferir una posición sobre otra. (2) *IA*: asignación aleatoria uniforme de ejemplos a particiones de entrenamiento/validación cuando se desea que cada partición tenga igual probabilidad de recibir cualquier ejemplo. (3) *DOE*: aleatorización del orden de corrida de los tratamientos de un experimento (randomización), un requisito metodológico estándar para evitar sesgos por efectos temporales.

#### 2.9.8 Distribución Multinomial — Profundización

* Generaliza la Binomial a $k>2$ categorías; no tiene una CDF cerrada de uso práctico — se trabaja directamente con la PMF conjunta o vía simulación.
* Cada componente marginal $X_i$ es por sí sola Binomial($n$, $p_i$), pero las componentes no son independientes entre sí (están ligadas por $\sum_i X_i = n$).

```python
import numpy as np
from scipy.stats import multinomial

## PMF Multinomial: clasificacion de n=20 nanoparticulas en 3
## categorias de tamano (pequena, mediana, grande) segun el proceso
n = 20
probabilidades = [0.2, 0.5, 0.3]
dist = multinomial(n, probabilidades)

## Probabilidad de obtener exactamente 4 pequenas, 10 medianas, 6 grandes
conteo_observado = [4, 10, 6]
prob = dist.pmf(conteo_observado)
print(f"P(4 pequeñas, 10 medianas, 6 grandes) = {prob:.4f}")

## Esperanza por categoria: E[X_i] = n * p_i
esperanza = n * np.array(probabilidades)
print(f"Esperanza por categoría: {esperanza}")
```

**Aplicaciones**: (1) *Nanotecnología*: clasificación de un lote de $n$ nanopartículas en $k$ categorías de tamaño (pequeña/mediana/grande) según las probabilidades conocidas de un proceso de síntesis sol-gel. (2) *IA*: distribución de probabilidad de salida de un clasificador multiclase (capa *softmax*) sobre $k$ categorías — la Multinomial es la distribución muestral subyacente a los conteos de predicciones correctas por clase. (3) *DOE*: resultado de un experimento con más de dos desenlaces categóricos posibles por unidad experimental (p. ej., clasificar cada muestra en "aprobada", "reprocesable" o "rechazada"), base de las pruebas de bondad de ajuste $\chi^2$ sobre datos categóricos.

**Más allá de un solo punto: enumerar y comparar todos los resultados posibles.** El código de 2.9.8 evalúa la PMF en un único conteo observado $(4,10,6)$. Con frecuencia interesa además saber **qué otros resultados** son igual o más probables que el observado — por ejemplo, para juzgar si el conteo real de un lote es consistente con el proceso esperado. Esto requiere enumerar todas las combinaciones $(x_1,x_2,x_3)$ con $x_1+x_2+x_3=n$ y ordenarlas por probabilidad:

```python
import numpy as np
import pandas as pd
from scipy.stats import multinomial

## Nanoreactor de sintesis sol-gel: n=20 nanoparticulas, 3 categorias de
## tamano con probabilidades del proceso (pequena, mediana, grande)
n = 20
probabilidades = [0.2, 0.5, 0.3]

resultados_validos = []
for x1 in range(n + 1):
    for x2 in range(n - x1 + 1):
        x3 = n - x1 - x2
        resultados_validos.append([x1, x2, x3])

resultados_array = np.array(resultados_validos)
pmf_valores = multinomial.pmf(x=resultados_array, n=n, p=probabilidades)

tabla = pd.DataFrame(resultados_array, columns=["pequeñas", "medianas", "grandes"])
tabla["pmf"] = pmf_valores
top_10 = tabla.sort_values(by="pmf", ascending=False).head(10)

print(f"Total de combinaciones válidas con suma {n}: {len(tabla)}")
print("\nTop 10 combinaciones más probables:")
print(top_10.to_string(index=False))
```

El resultado confirma que la combinación $(4,10,6)$ evaluada en 2.9.8 —que coincide exactamente con el valor esperado por categoría, $n\cdot p_i = (4,10,6)$— es precisamente la **moda** de la distribución multinomial: la más probable de las 231 combinaciones válidas para $n=20$. Este patrón de enumeración exhaustiva es la técnica correcta para responder preguntas del tipo "¿qué tan inusual es este conteo observado?", en vez de solo reportar su probabilidad puntual sin contexto de las alternativas.

---

## 3. Ejemplo Analítico Paso a Paso: Inspección Nanotecnológica de Micro-sensores

### 3.1 Contexto Aplicado en Nanotecnología
En una sala limpia de fabricación de nano-sensores piezoresistivos para dispositivos médicos implantables, la probabilidad de que una unidad presente una micro-grieta estructural en el diafragma de silicio durante la etapa de grabado químico es $p = 0.05$. Un ingeniero en control de calidad selecciona una muestra aleatoria de $n = 20$ nano-sensores del lote de producción diaria.

Determine:
1. La probabilidad exacta de encontrar exactamente 2 nano-sensores defectuosos en la muestra.
2. La probabilidad de encontrar al menos 1 nano-sensor defectuoso.
3. El número esperado y la desviación estándar de nano-sensores defectuosos.

### 3.2 Paso 1: Identificación del Modelo y Parámetros
El conteo de nano-sensores defectuosos en $n=20$ ensayos independientes con $p=0.05$ sigue una distribución Binomial:
$$X \sim \text{Binomial}(n = 20, p = 0.05)$$

### 3.3 Paso 2: Cálculo de $P(X = 2)$
$$P(X = 2) = \binom{20}{2} (0.05)^2 (0.95)^{18}$$
$$\binom{20}{2} = \frac{20 \times 19}{2} = 190$$
$$(0.05)^2 = 0.0025, \quad (0.95)^{18} \approx 0.397214$$
$$\boxed{P(X = 2) = 190 \times 0.0025 \times 0.397214 \approx 0.18868 \quad (18.87\%)}$$

### 3.4 Paso 3: Cálculo de $P(X \ge 1)$ por Complemento
$$P(X \ge 1) = 1 - P(X = 0) = 1 - \binom{20}{0} (0.05)^0 (0.95)^{20}$$
$$(0.95)^{20} \approx 0.358486$$
$$\boxed{P(X \ge 1) = 1 - 0.358486 = 0.64151 \quad (64.15\%)}$$

### 3.5 Paso 4: Esperanza y Desviación Estándar
$$\mathbb{E}[X] = n p = 20 \times 0.05 = \boxed{1.0 \text{ nano-sensor}}$$
$$\text{Var}(X) = n p (1-p) = 20 \times 0.05 \times 0.95 = 0.95 \implies \sigma = \sqrt{0.95} \approx \boxed{0.9747\text{ nano-sensores}}$$

### 3.6 Prueba Unitaria con pytest

Se contrasta cada resultado derivado a mano (combinatoria + PMF Binomial) contra `scipy.stats.binom`, que calcula la misma fórmula sin riesgo de error aritmético humano:

```python
import ipytest
import pytest
from scipy.stats import binom

ipytest.autoconfig()

n, p = 20, 0.05


def test_probabilidad_de_exactamente_2_defectuosos():
    assert binom.pmf(2, n, p) == pytest.approx(0.18868, rel=1e-3)


def test_probabilidad_de_al_menos_1_defectuoso_por_complemento():
    prob_al_menos_uno = 1 - binom.pmf(0, n, p)
    assert prob_al_menos_uno == pytest.approx(0.64151, rel=1e-3)


def test_esperanza_y_varianza_binomial():
    assert n * p == pytest.approx(1.0)
    assert n * p * (1 - p) == pytest.approx(0.95)


ipytest.run("-vv")
```

---

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

---

* Li, Y. & Jiang, Z. (2008). An Overview of Reliability and Failure Mode Analysis of Microelectromechanical Systems (MEMS). En *Handbook of Performability Engineering*. Springer, London. DOI: [10.1007/978-1-84800-131-2_58](https://doi.org/10.1007/978-1-84800-131-2_58) — modos de falla y análisis de confiabilidad de micro-sensores, el contexto aplicado del ejemplo analítico de esta unidad (conteo Binomial de defectos en un lote de nano-sensores).
