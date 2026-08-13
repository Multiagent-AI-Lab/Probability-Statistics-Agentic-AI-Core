# UNIDAD 4: Distribuciones de Probabilidad Conjuntas y Bivariadas
## Asignatura: Probabilidad y Estadística Inferencial
### UCEMICH — Ingeniería en IA y Nanotecnología
### Autor y Profesor: Mtro. Luis José Yudico Anaya

---

## 1. Fundamentación Teórica y Conceptos Clave

## Universidad de La Ciénega del Estado de Michoacán de Ocampo

## Capítulo 5 secciones 5.3 a 5.8: Distribuciones Conjuntas, Condicionales, Convolución Vectores Aleatorios, Transformaciones Gaussianas y Análisis de Compnentes Principales

## 1 – Distribuciones Conjuntas

### 1.1 Concepto General

Cuando dos o más variables aleatorias se analizan simultáneamente, su comportamiento combinado se describe mediante una **distribución conjunta**.

* **Definición:**
  La distribución conjunta de $(X,Y)$ indica la probabilidad de que $X$ y $Y$ tomen determinados valores simultáneamente.

Para variables **discretas**, la función de masa de probabilidad conjunta (PMF) se denota:
$$
\displaystyle P_{X,Y}(x,y) = P(X = x,, Y = y)
$$

Para variables **continuas**, se utiliza la función de densidad de probabilidad conjunta (PDF):
$$
\displaystyle f_{X,Y}(x,y)
$$

---

### 1.2 Propiedades Básicas

1. **No-negatividad:**
   $$
   P_{X,Y}(x,y)\ge0,\qquad f_{X,Y}(x,y)\ge0
   $$
2. **Normalización:**

   * Discretas: $\displaystyle\sum_x\sum_y P_{X,Y}(x,y)=1$
   * Continuas: $\displaystyle\int_{-\infty}^{\infty}!!\int_{-\infty}^{\infty} f_{X,Y}(x,y),dx,dy = 1$

---

### 1.3 Ejemplo (Intuitivo)

Sea $X$ = número de bolas rojas extraídas y $Y$ = número de bolas azules extraídas de una urna.
Cada par $(x,y)$ tiene una probabilidad $P_{X,Y}(x,y)$ que indica cuántas combinaciones producen ese resultado.

---

## 2 – Distribuciones Marginales

### 2.1 Concepto y Definición

La **distribución marginal** de una variable se obtiene a partir de la conjunta **eliminando** (sumando o integrando) la otra variable.

* Para variables discretas:
  $$
  P_X(x)=\sum_y P_{X,Y}(x,y), \qquad
  P_Y(y)=\sum_x P_{X,Y}(x,y)
  $$
* Para variables continuas:
  $$
  f_X(x)=\int_{-\infty}^{\infty} f_{X,Y}(x,y),dy,\qquad
  f_Y(y)=\int_{-\infty}^{\infty} f_{X,Y}(x,y),dx
  $$

---

### 2.2 Ejemplo (Discreto)

Suponga la siguiente tabla de probabilidades conjuntas:

| X \ Y |   0  |   1  |  2  |
| :---: | :--: | :--: | :-: |
|   0   | 1/15 | 2/15 |  0  |
|   1   | 3/15 | 6/15 |  0  |
|   2   | 1/15 | 2/15 |  0  |

**Distribución marginal de X:**
$$
P_X(0)=\tf\frac{3}{15},\quad
P_X(1)=\tf\frac{9}{15},\quad
P_X(2)=\tf\frac{3}{15}
$$

**Distribución marginal de Y:**
$$
P_Y(0)=\tf\frac{5}{15},\quad
P_Y(1)=\tf\frac{10}{15},\quad
P_Y(2)=0
$$

---

### 2.3 Interpretación

Las marginales resumen la información individual de cada variable sin considerar su relación conjunta.
Permiten calcular expectativas o probabilidades univariadas.

---

## 3 – Independencia de Variables Aleatorias

### 3.1 Concepto y Criterio

Dos variables aleatorias $X$ y $Y$ son **independientes** si el conocimiento de una **no afecta** la distribución de la otra.

Matemáticamente:
$$
P_{X,Y}(x,y)=P_X(x),P_Y(y)
$$
o, en el caso continuo,
$$
f_{X,Y}(x,y)=f_X(x),f_Y(y)
$$

---

### 3.2 Propiedades Claves

1. Si $X$ e $Y$ son independientes:
   $$
   E[X,Y]=E[X];E[Y]
   $$
2. La covarianza es cero:
   $$
   \mathrm{Cov}(X,Y)=E[(X-E[X])(Y-E[Y])]=0
   $$

---

### 3.3 Ejemplo (Comprobación de Independencia)

Dadas las marginales y conjuntas anteriores:

$$
P_X(1)=\tf\frac{9}{15}, \quad
P_Y(1)=\tf\frac{10}{15}, \quad
P_{X,Y}(1,1)=\tf\frac{6}{15}
$$

Si fueran independientes se debería cumplir:

$$
P_X(1),P_Y(1)=\tf\frac{9}{15}\cdot\tf\frac{10}{15}=\tf\frac{90}{225}=0.4
$$

Mientras que $P_{X,Y}(1,1)=0.4$; si la igualdad se mantiene para todos los pares $(x,y)$, las variables son independientes.

---

### 3.4 Ejemplo (Continuo)

Sea $f_{X,Y}(x,y)=2$ en el triángulo $0\le y\le x\le1$ y 0 en otro caso.

* **Marginal de X:**
  $$
  f_X(x)=\int_0^{x}2,dy=2x
  $$
* **Marginal de Y:**
  $$
  f_Y(y)=\int_y^{1}2,dx=2(1-y)
  $$
* **Producto:**
  $$
  f_X(x)f_Y(y)=4x(1-y)
  $$
  que **no coincide** con $f_{X,Y}(x,y)=2$; luego $X$ y $Y$ **no son independientes**.

---

## 4 – Distribuciones Condicionales

### 4.1 Motivación

Cuando se conoce el valor de una variable $X=x$, la incertidumbre sobre otra variable $Y$ cambia.
La distribución resultante se denomina **distribución condicional**.

---

### 4.2 PMF Condicional (Discreta)

**Definición:**
$$
\displaystyle P_{Y|X}(y|x)=\frac{P_{X,Y}(x,y)}{P_X(x)},\qquad P_X(x)>0
$$

**Propiedades:**

1. $\displaystyle \sum_y P_{Y|X}(y|x)=1$
2. Regla de multiplicación:
   $$
   P_{X,Y}(x,y)=P_X(x),P_{Y|X}(y|x)
   $$

**Ejemplo (discreto):**

Para el caso de bolas rojas ($X$) y azules ($Y$):

* $P_X(1)=9/15$
* $P_{X,Y}(1,0)=3/15$, $P_{X,Y}(1,1)=6/15$

Cálculo:

| y | $P_{X,Y}(1,y)$ | $P_{Y|X}(y|1)$ |
|:--:|:--:|:--:|
| 0 | $3/15$ | $(3/15)/(9/15)=1/3$ |
| 1 | $6/15$ | $(6/15)/(9/15)=2/3$ |

Por tanto,
$$
P_{Y|X}(0|1)=\tf\frac{1}{3},\quad P_{Y|X}(1|1)=\tf\frac{2}{3}.
$$

---

### 4.3 PDF Condicional (Continua)

**Definición:**
$$
\displaystyle f_{Y|X}(y|x)=\frac{f_{X,Y}(x,y)}{f_X(x)},\qquad f_X(x)>0
$$

**Independencia:**
Si $X$ y $Y$ son independientes,
$$
f_{Y|X}(y|x)=f_Y(y).
$$

**Ejemplo:**

Sea $f_{X,Y}(x,y)=x+y$ para $0\le x,y\le1$.
Entonces
$$
f_X(x)=\int_0^1 (x+y),dy=x+\tfrac12.
$$
Por tanto:
$$
f_{Y|X}(y|x)=\frac{x+y}{x+1/2}.
$$

Calcular $P(Y<0.5,|,X=0.5)$:

1. Sustituir $x=0.5$:
   $$
   f_{Y|X}(y|0.5)=0.5+y.
   $$
2. Integrar:
   $$
   P(Y<0.5|X=0.5)=\int_0^{0.5}(0.5+y),dy=0.375.
   $$

---

### 4.4 Implementación en Python (Ejemplo Condicional Discreto)

```python
import numpy as np
## Probabilidades conjuntas P(X,Y)
joint = {(1,0):3/15, (1,1):6/15}
PX1 = 9/15
## PMF condicional de Y|X=1
cond = {y: joint[(1,y)]/PX1 for y in [0,1]}
cond
```

Salida esperada:
`{0: 0.333..., 1: 0.666...}`

**Código ejecutable**

```python
import numpy as np
## Probabilidades conjuntas P(X,Y)
joint = {(1,0):3/15, (1,1):6/15}
PX1 = 9/15
## PMF condicional de Y|X=1
cond = {y: joint[(1,y)]/PX1 for y in [0,1]}
cond
```

## 5 – Esperanza Condicional

### 5.1 Definición General

La **esperanza condicional** de una variable aleatoria $Y$ dado que $X=x$ es el valor esperado de $Y$ respecto a su distribución condicional:

$$
\displaystyle E[Y|X=x] = \sum_y y,P_{Y|X}(y|x)
$$
para el caso **discreto**, y

$$
\displaystyle E[Y|X=x] = \int_{-\infty}^{\infty} y,f_{Y|X}(y|x),dy
$$
para el caso **continuo**.

---

### 5.2 Propiedades Fundamentales

1. **Linealidad:**
   $$
   E[aY+b|X]=aE[Y|X]+b
   $$

2. **Reducción de Varianza (Ley de iteración):**
   $$
   E[Y]=E[E[Y|X]]
   $$

3. **Independencia:**
   Si $X$ y $Y$ son independientes, entonces:
   $$
   E[Y|X]=E[Y].
   $$

---

### 5.3 Ejemplo Discreto

Sea $P_{Y|X}(y|1)$ el ejemplo anterior:
$$
P_{Y|X}(0|1)=\tf\frac{1}{3},\quad P_{Y|X}(1|1)=\tf\frac{2}{3}.
$$

Entonces:
$$
E[Y|X=1]=0\cdot\tf\frac{1}{3}+1\cdot\tf\frac{2}{3}=\tf\frac{2}{3}.
$$

En Python:

```python
y_vals = np.array([0, 1])
p_cond = np.array([1/3, 2/3])
E_Y_given_X1 = np.sum(y_vals * p_cond)
E_Y_given_X1
```

Salida esperada:
`0.666...`

---

### 5.4 Ejemplo Continuo

Sea $f_{Y|X}(y|x)=2y$ para $0\le y\le1$ (no depende de $x$).
Entonces:

$$
E[Y|X=x]=\int_0^1 y(2y),dy=2\int_0^1 y^2,dy=\frac{2}{3}.
$$

---

**Código ejecutable 5.3**

```python
import numpy as np

y_vals = np.array([0, 1])
p_cond = np.array([1/3, 2/3])
E_Y_given_X1 = np.sum(y_vals * p_cond)
E_Y_given_X1
```

## 6 – Distribución de la Suma de Variables Aleatorias

### 6.1 Concepto General

Sea $Z=X+Y$.
Queremos determinar la distribución de $Z$ a partir de la conjunta $f_{X,Y}(x,y)$.

**NOTA:** Dada la relación anterior, se tiene $Y=Z-X$
---

### 6.2 Caso Discreto

Para variables discretas independientes:

$$
P_Z(z) = \sum_x P_X(x),P_Y(z-x)
$$

Esto se conoce como **convolución discreta**.

**Ejemplo:**

Si $X$ e $Y$ son resultados de dos dados:

$$
P_X(x)=P_Y(y)=\frac{1}{6},\quad x,y\in{1,2,3,4,5,6}
$$

Entonces:

$$
P_Z(7)=\sum_{x=1}^6 P_X(x)P_Y(7-x)=\frac{6}{36}=\frac{1}{6}.
$$

---

### 6.3 Caso Continuo (Convolución)

Si $X$ y $Y$ son **independientes** y continuas, entonces la densidad de $Z=X+Y$ es:

$$
f_Z(z)=\int_{-\infty}^{\infty} f_X(x),f_Y(z-x),dx
$$

---

### 6.4 Ejemplo Continuo

Si $X$ y $Y$ son uniformes en $[0,1]$, entonces:

$$
f_X(x)=f_Y(y)=1,\quad 0\le x,y\le1
$$

La densidad de $Z=X+Y$ se obtiene mediante:

$$
f_Z(z)=
\begin{cases}
z, & 0\le z\le1[4pt]
2-z, & 1<z\le2[4pt]
0, & \text{en otro caso.}
\end{cases}
$$

Gráficamente, esta densidad tiene forma de triángulo.

```python
import matplotlib.pyplot as plt
z = np.linspace(0, 2, 200)
fZ = np.piecewise(z, [z<=1, (z>1)&(z<=2)], [lambda z: z, lambda z: 2-z, 0])
plt.plot(z, fZ)
plt.title("Densidad de Z = X + Y (Uniformes[0,1])")
plt.xlabel("z")
plt.ylabel("f_Z(z)")
plt.grid(True)
plt.show()
```

---

**Código para gráficar la función de densidad**

```python
import matplotlib.pyplot as plt
z = np.linspace(0, 2, 200)
fZ = np.piecewise(z, [z<=1, (z>1)&(z<=2)], [lambda z: z, lambda z: 2-z, 0])
plt.plot(z, fZ)
plt.title("Densidad de Z = X + Y (Uniformes[0,1])")
plt.xlabel("z")
plt.ylabel("f_Z(z)")
plt.grid(True)
plt.show()
```

## 7 – Propiedades de la Convolución

### 7.1 Propiedades Claves

1. **Conmutatividad:**
   $$
   f_X * f_Y = f_Y * f_X
   $$

2. **Asociatividad:**
   $$
   (f_X * f_Y) * f_Z = f_X * (f_Y * f_Z)
   $$

3. **Normalización:**
   $$
   \int_{-\infty}^{\infty} f_Z(z),dz = 1
   $$

4. **Transformada de Fourier:**
   La convolución en el dominio del tiempo equivale a la **multiplicación** de transformadas:
   $$
   \mathcal{F}{f_X * f_Y} = \mathcal{F}{f_X}\cdot \mathcal{F}{f_Y}.
   $$

---

### 7.2 Interpretación Probabilística

La convolución expresa la probabilidad de que **la suma** de dos variables tome un valor dado, considerando todas las combinaciones posibles de sus valores individuales.

---

### 7.3 Ejemplo Numérico

Supón:
$$
f_X(x)=
\begin{cases}
1, & 0\le x\le1\
0, & \text{otro caso}
\end{cases},\quad
f_Y(y)=
\begin{cases}
1, & 0\le y\le1\
0, & \text{otro caso.}
\end{cases}
$$

Calculamos $f_Z(1.5)$:

$$
f_Z(1.5)=\int_{-\infty}^{\infty} f_X(x)f_Y(1.5-x),dx
$$

El integrando es no nulo solo cuando $x\in[0,1]$ y $1.5-x\in[0,1]$, es decir $x\in[0.5,1]$.

Por tanto:

$$
f_Z(1.5)=\int_{0.5}^{1}1,dx=0.5.
$$

---

### 7.4 Implementación Numérica (Python)

```python
from scipy.signal import convolve
## Definición de funciones discretizadas
x = np.linspace(0, 1, 100)
fX = np.ones_like(x)
fY = np.ones_like(x)
## Convolución discreta normalizada
fZ = convolve(fX, fY, mode='full') / len(x)
plt.plot(np.linspace(0, 2, len(fZ)), fZ)
plt.title("Convolución de dos Uniformes[0,1]")
plt.xlabel("z")
plt.ylabel("f_Z(z)")
plt.grid(True)
plt.show()
```

---

```python
from scipy.signal import convolve
import numpy as np
import matplotlib.pyplot as plt

## Definición de funciones discretizadas
x = np.linspace(0, 1, 100)
fX = np.ones_like(x)
fY = np.ones_like(x)
## Convolución discreta normalizada
fZ = convolve(fX, fY, mode='full') / len(x)
plt.plot(np.linspace(0, 2, len(fZ)), fZ)
plt.title("Convolución de dos Uniformes[0,1]")
plt.xlabel("z")
plt.ylabel("f_Z(z)")
plt.grid(True)
plt.show()
```

## 8 – Aplicaciones y Ejercicios

### 8.1 Aplicaciones Reales

1. **Procesamiento de señales:**
   El ruido y las respuestas de sistemas lineales se modelan mediante convolución.
2. **Probabilidad de suma de tiempos de espera:**
   La suma de variables exponenciales produce una distribución Gamma.
3. **Modelos financieros:**
   Los retornos agregados en periodos sucesivos se tratan mediante sumas de variables aleatorias.

---

### 8.2 Ejercicio 1 (Discreto)

Sean $X$ y $Y$ independientes con:
$$
P_X(0)=0.4,\quad P_X(1)=0.6
$$
$$
P_Y(0)=0.5,\quad P_Y(1)=0.5
$$

Calcular $P_Z(z)$ donde $Z=X+Y$.

Solución:
$$
P_Z(0)=P_X(0)P_Y(0)=0.2
$$
$$
P_Z(1)=P_X(0)P_Y(1)+P_X(1)P_Y(0)=0.4+0.3=0.5
$$
$$
P_Z(2)=P_X(1)P_Y(1)=0.3
$$

---

### 8.3 Ejercicio 2 (Continuo)

Sea $X\sim U[0,1]$, $Y\sim U[0,2]$ independientes.

Entonces:
$$
f_Z(z)=\int_{-\infty}^{\infty} f_X(x),f_Y(z-x),dx
$$

Tras calcular el intervalo de superposición se obtiene:

$$
f_Z(z)=
\begin{cases}
\tf\frac{z}{2}, & 0\le z\le1[4pt]
\tf\frac{1}{2}, & 1<z\le2[4pt]
\tf\frac{3-z}{2}, & 2<z\le3[4pt]
0, & \text{otro caso.}
\end{cases}
$$

---

### 8.4 Ejercicio 3 (Esperanza Condicional)

Sea $E[Y|X=x]=2x+1$ y $E[X]=3$.

Entonces:
$$
E[Y]=E[E[Y|X]]=E[2X+1]=2E[X]+1=7.
$$

## Resumen Distribuciones y Esperanzas Condicionales

Estas son fundamentales para entender cómo la información de una variable aleatoria afecta a otra.

---

## Capítulo 5: Distribuciones Conjuntas

### 5.3 PMF y PDF Condicionales

Cuando tenemos dos variables aleatorias $X$ e $Y$, las *distribuciones condicionales* nos permiten estudiar la distribución de una variable **dada una observación específica de la otra**.
Este concepto es la base de la inferencia estadística, pues modela la dependencia entre variables.

---

### 5.3.1 PMF Condicional (Conditional PMF)

La *Probabilidad de Masa Condicional (PMF)* se utiliza para variables aleatorias **discretas**.
Se define de manera análoga a la probabilidad condicional simple:

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

#### Definición

Dadas dos variables aleatorias discretas $X$ e $Y$ con PMF conjunta $P_{X,Y}(x, y)$, la PMF de $Y$ dado que $X$ ha tomado el valor $x$ se define como:

$$
P_{Y|X}(y|x) = P(Y=y | X=x) = \frac{P_{X,Y}(x, y)}{P_X(x)}
$$

para todos los valores $x$ donde $P_X(x) > 0$.

#### Propiedades Clave

1. **Suma a 1:**
   Para un valor fijo $x$, la suma sobre todos los posibles valores de $y$ debe ser 1:
   $$
   \sum_{y} P_{Y|X}(y|x) = 1
   $$
2. **Regla de Multiplicación:**
   La PMF conjunta se puede obtener multiplicando la marginal por la condicional:
   $$
   P_{X,Y}(x, y) = P_{Y|X}(y|x) P_X(x)
   $$

#### Ejemplo Práctico (Discreto)

Retomando el ejercicio con **3 bolas rojas (R), 2 azules (A) y 1 verde (V)** en **2 extracciones**, donde $X=$ Rojas y $Y=$ Azules.
Calcularemos la PMF condicional de $Y$ dado que **$X=1$**.

**Datos de la PMF Conjunta y Marginal (corregidos):**

* $P_{X,Y}(1, 0) = 3/15$
* $P_{X,Y}(1, 1) = 6/15$
* $P_{X,Y}(1, 2) = 0$
* $P_X(1) = 9/15$

**Cálculo de $P_{Y|X}(y|1)$:**

1. Para $y=0$:
   $$
   P_{Y|X}(0|1) = \frac{P_{X,Y}(1, 0)}{P_X(1)} = \frac{3/15}{9/15} = \frac{1}{3}
   $$

2. Para $y=1$:
   $$
   P_{Y|X}(1|1) = \frac{P_{X,Y}(1, 1)}{P_X(1)} = \frac{6/15}{9/15} = \frac{2}{3}
   $$

3. Para $y=2$:
   $$
   P_{Y|X}(2|1) = \frac{0}{9/15} = 0
   $$

**Verificación:**
$$
\sum_{y} P_{Y|X}(y|1) = \frac{1}{3} + \frac{2}{3} + 0 = 1
$$

```python
## Código Python para PMF Condicional (Ejemplo)
import numpy as np
from fractions import Fraction

## PMF Conjunta P(x, y)
P_XY = {(0, 0): 0, (0, 1): Fraction(2, 15), (0, 2): Fraction(1, 15),
        (1, 0): Fraction(3, 15), (1, 1): Fraction(6, 15), (1, 2): 0,
        (2, 0): Fraction(3, 15), (2, 1): 0, (2, 2): 0}

## PMF Marginal de X
P_X_1 = Fraction(9, 15)
print(f"PMF Marginal P_X(1) = {P_X_1}")

## Calcular PMF Condicional P(Y | X=1)
print("\nPMF Condicional P(Y | X=1):")
for y in range(3):
    P_Y_cond_X = P_XY[(1, y)] / P_X_1
    print(f"P(Y={y} | X=1) = {P_Y_cond_X}")
```

---

### 5.3.2 PDF Condicional (Conditional PDF)

La *Probabilidad de Densidad Condicional (PDF)* se utiliza para variables aleatorias **continuas**.

#### Definición

Dadas dos variables aleatorias continuas $X$ e $Y$ con PDF conjunta $f_{X,Y}(x, y)$, la PDF de $Y$ dado que $X=x$ se define como:

$$
f_{Y|X}(y|x) = \frac{f_{X,Y}(x, y)}{f_X(x)}
$$

para todos los valores $x$ donde $f_X(x) > 0$.

#### Propiedades Clave

1. **Integración a 1:**
   $$
   \int_{-\infty}^{\infty} f_{Y|X}(y|x),dy = 1
   $$
2. **Regla de Multiplicación:**
   $$
   f_{X,Y}(x, y) = f_{Y|X}(y|x) f_X(x)
   $$
3. **Independencia:**
   Si $X$ e $Y$ son independientes, entonces:
   $$
   f_{Y|X}(y|x) = f_Y(y)
   $$

#### Ejemplo Práctico (Continuo)

Sea $f_{X,Y}(x, y) = x + y$ para $0 \leq x, y \leq 1$.
La marginal calculada fue $f_X(x) = x + \frac{1}{2}$.

Entonces:
$$
f_{Y|X}(y|x) = \frac{x + y}{x + \frac{1}{2}}, \quad 0 \leq x,y \leq 1
$$

**Cálculo de $P(Y < 0.5 | X = 0.5)$:**

$$
f_{Y|X}(y|0.5) = 0.5 + y
$$
$$
P(Y < 0.5 | X = 0.5) = \int_{0}^{0.5} (0.5 + y),dy = 0.375
$$

---

## 5.4 Esperanza Condicional

La **esperanza condicional** $E[Y|X=x]$ es el valor promedio de $Y$ que se espera dada la información de que $X$ ha tomado un valor específico.

#### Definición

**Discreta:**
$$
E[Y|X=x] = \sum_y y \cdot P_{Y|X}(y|x)
$$

**Continua:**
$$
E[Y|X=x] = \int_{-\infty}^{\infty} y \cdot f_{Y|X}(y|x),dy
$$

#### Ejemplo Discreto

Usando el ejemplo anterior:

* $P_{Y|X}(0|1) = 1/3$
* $P_{Y|X}(1|1) = 2/3$

Entonces:
$$
E[Y|X=1] = 0\cdot\frac{1}{3} + 1\cdot\frac{2}{3} = \frac{2}{3}
$$

---

### 5.4.1 Ley de la Esperanza Total (Ley de la Esperanza Iterada)

La **Ley de la Esperanza Total (LET)** indica que:

$$
E[Y] = E[E[Y|X]]
$$

Esto implica que la esperanza incondicional puede calcularse promediando las esperanzas condicionales.

**Discreta:**
$$
E[Y] = \sum_x E[Y|X=x] P_X(x)
$$

**Continua:**
$$
E[Y] = \int_{-\infty}^{\infty} E[Y|X=x] f_X(x),dx
$$

#### Ejemplo

Del ejemplo de las bolas:

$$
E[Y|X=0]=\frac{4}{3}, \quad E[Y|X=1]=\frac{2}{3}, \quad E[Y|X=2]=0
$$

Aplicamos la ley:

$$
E[Y]=\frac{4}{3}\frac{3}{15}+\frac{2}{3}\frac{9}{15}+0\cdot\frac{3}{15}=\frac{2}{3}
$$

---

## 5.5 Suma de Dos Variables Aleatorias: $Z = X + Y$

Cuando se suman dos variables aleatorias, la distribución de $Z$ se obtiene mediante **convolución**.

### 5.5.1 Convolución Discreta

$$
P_Z(z) = \sum_x P_X(x) P_Y(z-x)
$$

### 5.5.2 Convolución Continua

$$
f_Z(z) = \int_{-\infty}^{\infty} f_X(x) f_Y(z-x),dx
$$

---

### 5.5.3 Propiedades de la Suma

**Esperanza:**
$$
E[X+Y] = E[X] + E[Y]
$$

**Varianza general:**
$$
\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2,\text{Cov}(X,Y)
$$

**Si son independientes:**
$$
\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y)
$$

---

### 5.5.4 Suma de Distribuciones Comunes

<table>
  <thead>
    <tr>
      <th style="text-align:center; width:30%;">Distribución de <i>X</i></th>
      <th style="text-align:center; width:30%;">Distribución de <i>Y</i></th>
      <th style="text-align:center; width:40%;">Distribución de la suma <i>Z = X + Y</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:center;">$\text{Binomial}(n_1, p)$</td>
      <td style="text-align:center;">$\text{Binomial}(n_2, p)$</td>
      <td style="text-align:center;">$\text{Binomial}(n_1 + n_2, p)$</td>
    </tr>
    <tr>
      <td style="text-align:center;">$\text{Poisson}(\lambda_1)$</td>
      <td style="text-align:center;">$\text{Poisson}(\lambda_2)$</td>
      <td style="text-align:center;">$\text{Poisson}(\lambda_1 + \lambda_2)$</td>
    </tr>
    <tr>
      <td style="text-align:center;">$\text{Normal}(\mu_1, \sigma_1^2)$</td>
      <td style="text-align:center;">$\text{Normal}(\mu_2, \sigma_2^2)$</td>
      <td style="text-align:center;">$\text{Normal}(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$</td>
    </tr>
    <tr>
      <td style="text-align:center;">$\text{Gamma}(\alpha_1, \theta)$</td>
      <td style="text-align:center;">$\text{Gamma}(\alpha_2, \theta)$</td>
      <td style="text-align:center;">$\text{Gamma}(\alpha_1 + \alpha_2, \theta)$</td>
    </tr>
  </tbody>
</table>

<p style="text-align:center;"><em>Estas relaciones son válidas únicamente si las variables aleatorias</em> $X$ <em>e</em> $Y$ <em>son independientes.</em></p>

---

**Observaciones finales:**

* La suma de normales independientes **siempre es normal**, fundamento del Teorema del Límite Central.
* La suma de uniformes **no es uniforme** (produce una distribución triangular).
* Estas propiedades de “cierre” se cumplen **solo si las variables son independientes**.

---

## 5.3 PMF y PDF Condicionales (extensión completa)

### Introducción ampliada (qué, por qué y cuándo)

Cuando trabajamos con dos variables aleatorias $X$ e $Y$, a menudo queremos describir la distribución de una **condicionada** a la observación de la otra. Esto es central en inferencia (p. ej. actualización de creencias), en modelos de regresión y en procesos estocásticos que evolucionan con información parcial.

* **¿Qué?** La distribución condicional $P_{Y|X=x}$ o $f_{Y|X}(y|x)$ describe la probabilidad/densidad de $Y$ cuando sabemos que $X$ vale $x$.
* **¿Para qué?** Para actualizar predicciones, calcular esperanzas condicionadas, construir estimadores condicionales (regresión) y calcular probabilidades compuestas.
* **¿Cuándo?** Siempre que haya dependencia entre variables o cuando queremos explotar información disponible sobre alguna variable para mejorar la predicción de otra.

---

## 5.3.1 PMF Condicional (variables discretas)

### Definición formal

Para variables discretas $X,Y$ con PMF conjunta $P_{X,Y}(x,y)$ y marginal $P_X(x)>0$:

$$
\displaystyle P_{Y|X}(y|x) ;=; \frac{P_{X,Y}(x,y)}{P_X(x)}.
$$

Es la aplicación directa de la probabilidad condicional clásica a variables aleatorias.

### Propiedades fundamentales (recordatorio ampliado)

1. **No-negatividad:** $P_{Y|X}(y|x)\ge0$.
2. **Normalización (para $x$ fijo):** $\displaystyle\sum_y P_{Y|X}(y|x)=1$.
3. **Reconstrucción de la conjunta:** $\displaystyle P_{X,Y}(x,y)=P_X(x)P_{Y|X}(y|x)$.
4. **Si $X$ e $Y$ son independientes:** $P_{Y|X}(y|x)=P_Y(y)$ (no depende de $x$).

---

### Ejemplo completo (analítico + código): urna con 3R,2A,1V — 2 extracciones sin reemplazo

**Planteamiento:** Urna con 6 bolas: 3 rojas (R), 2 azules (A), 1 verde (V). Se extraen 2 sin reemplazo.
Definimos:

* $X =$ número de rojas extraídas ($x\in{0,1,2}$)
* $Y =$ número de azules extraídas ($y\in{0,1,2}$)
  (Nótese que $X+Y\le2$ y algunas combinaciones son imposibles.)

**Paso 1 — Calcular PMF conjunta** (combinatoria)
Para dar un par $(x,y)$ compatible con $x+y \le 2$, el número de formas es:
$$
\binom{3}{x}\binom{2}{y}\binom{1}{2-x-y}
$$
dividido entre $\binom{6}{2}=15$.

Los valores relevantes (resumidos) son:

* $P_{X,Y}(1,0)=3/15$
* $P_{X,Y}(1,1)=6/15$
* $P_{X,Y}(1,2)=0$
* y así sucesivamente (se puede construir la tabla completa).

**Paso 2 — Marginal de $X$**:
$$P_X(1)=\sum_y P_{X,Y}(1,y)=\frac{3}{15}+\frac{6}{15}+0=\frac{9}{15}.$$

**Paso 3 — PMF condicional $P_{Y|X}(y|1)$**:
$$
P_{Y|X}(y|1)=\frac{P_{X,Y}(1,y)}{P_X(1)}.
$$

Cálculos explícitos:

* $P_{Y|X}(0|1)=\frac{3/15}{9/15}=\frac{1}{3}$.
* $P_{Y|X}(1|1)=\frac{6/15}{9/15}=\frac{2}{3}$.
* $P_{Y|X}(2|1)=0$.

**Verificación suma a 1:** $1/3 + 2/3 + 0 = 1$.

---

#### Código Python (comprobación exacta con `fractions` y simulación con `numpy`)

```python
## Código de comprobación en Colab
from fractions import Fraction
import numpy as np
from collections import Counter

## PMF conjunta (fracciones exactas)
P_XY = {
    (0,0): Fraction(0,15), (0,1): Fraction(2,15), (0,2): Fraction(1,15),
    (1,0): Fraction(3,15), (1,1): Fraction(6,15), (1,2): Fraction(0,15),
    (2,0): Fraction(3,15), (2,1): Fraction(0,15), (2,2): Fraction(0,15)
}

## Marginal P_X(1)
P_X_1 = sum(P for (x,y),P in P_XY.items() if x==1)
print("P_X(1) =", P_X_1)  # Esperado: 9/15

## PMF condicional exacta
print("P(Y|X=1):")
for y in [0,1,2]:
    val = P_XY[(1,y)] / P_X_1
    print(f" y={y}: {val} = {float(val):.6f}")

## Simulación para validar (aprox.)
urn = [ 'R' ]*3 + [ 'A' ]*2 + [ 'V' ]*1
N = 200000
counts = Counter()
for _ in range(N):
    draw = np.random.choice(urn, size=2, replace=False)
    x = sum(1 for b in draw if b=='R')
    y = sum(1 for b in draw if b=='A')
    counts[(x,y)] += 1

print("\nFrecuencias simuladas (normalizadas) para (1,0) y (1,1):")
print("P_sim(1,0) = ", counts[(1,0)]/N)
print("P_sim(1,1) = ", counts[(1,1)]/N)
print("P_sim(Y|X=1) estimada (condicional) =")
## condicional simulada: P(Y=y | X=1) = P_sim(1,y) / sum_y P_sim(1,y)
total_X1 = sum(counts[(1,y)] for y in [0,1,2])
for y in [0,1,2]:
    print(f" y={y}: {counts[(1,y)]/total_X1:.6f}")
```

**Explicación del código:**

* Se usa `Fraction` para operar con exactitud racional y evitar errores de punto flotante en las fracciones teóricas.
* Se incluye una simulación (Monte Carlo) para validar que las probabilidades teóricas coinciden con la estimación empírica al aumentar N.

---

### Interpretación práctica

* Con la información *X=1* (una roja ya extraída), la distribución de azules se concentra en $y=0$ y $y=1$, con probabilidades 1/3 y 2/3: saber que extrajimos una roja reduce el espacio de resultados permitidos para $Y$ y repondera sus probabilidades.

---

## 5.3.2 PDF Condicional (variables continuas) — explicación extendida

### Contexto y observaciones

Para variables continuas, los eventos puntuales tienen probabilidad cero, pero las densidades condicionadas son herramientas válidas para describir cómo la masa de probabilidad "se reparte" sobre $y$ cuando $x$ está fijado. La PDF condicional se usa tanto para calcular probabilidades condicionales (integrando la densidad sobre un intervalo) como para calcular esperanzas condicionales.

### Definición formal

Si $f_{X,Y}(x,y)$ es la densidad conjunta y $f_X(x)>0$ la marginal:

$$
\displaystyle f_{Y|X}(y|x) = \frac{f_{X,Y}(x,y)}{f_X(x)},\qquad f_X(x)=\int_{-\infty}^{\infty} f_{X,Y}(x,y),dy.
$$

### Propiedades

1. **Normalización en $y$ para $x$ fijo:** $\displaystyle \int_{-\infty}^{\infty} f_{Y|X}(y|x),dy = 1$.
2. **Reconstrucción:** $f_{X,Y}(x,y)=f_X(x)f_{Y|X}(y|x)$.
3. **Independencia:** Si $f_{X,Y}(x,y)=f_X(x)f_Y(y)$, entonces $f_{Y|X}(y|x)=f_Y(y)$.

---

### Ejemplo completo (analítico + código): $f_{X,Y}(x,y)=x+y$ en $[0,1]^2$

**Enunciado:** Sea $f_{X,Y}(x,y)=x+y$ para $0\le x,y\le1$ y cero fuera. Calcular la marginal $f_X(x)$, la condicional $f_{Y|X}(y|x)$, y la probabilidad condicional $P(Y<0.5 | X=0.5)$.

**Paso A — Marginal de $X$**:
$$
f_X(x)=\int_0^1 (x+y),dy = x\cdot 1 + \frac{1}{2}= x + \frac{1}{2}, \quad 0\le x\le1.
$$

**Paso B — PDF condicional**:
$$
f_{Y|X}(y|x)=\frac{x+y}{x+\tfrac12},\qquad 0\le y\le1,; 0\le x\le1.
$$

**Verificación de normalización (analítica):**
Para un $x$ fijo,
[
\int_0^1 \frac{x+y}{x+\tfrac12},dy
= \frac{1}{x+\tfrac12}\left[ x y + \frac{y^2}{2} \right]_0^1
= \frac{x + \tfrac12}{x+\tfrac12} = 1.
]

**Paso C — Probabilidad condicional $P(Y<0.5 | X=0.5)$:**
Sustituir $x=0.5$:
$$
f_{Y|X}(y|0.5) = \frac{0.5 + y}{0.5 + 0.5} = 0.5 + y, \quad 0\le y\le1.
$$
Integrar:
$$
P(Y<0.5|X=0.5) = \int_0^{0.5} (0.5 + y),dy
= \left[0.5y + \frac{y^2}{2}\right]_0^{0.5}
= 0.25 + 0.125 = 0.375.
$$

---

#### Código Python (analítico simbólico con `sympy` y numérico con `scipy`)

```python
## Código para Colab: cálculo simbólico y numérico
import sympy as sp
from scipy.integrate import quad

## Símbolos
x, y = sp.symbols('x y')

## Definición simbólica
f_xy = x + y  # válido en [0,1]^2

## Marginal f_X(x) simbólico (integral en y de 0 a 1)
fX_sym = sp.integrate(f_xy, (y, 0, 1))
sp.simplify(fX_sym)  # resultado: x + 1/2

## PDF condicional simbólica
fY_given_X = (f_xy) / fX_sym
sp.simplify(fY_given_X)  # (x+y)/(x+1/2)

## Evaluar P(Y < 0.5 | X = 0.5) numéricamente
f_cond_numeric = lambda Y: 0.5 + Y  # derivado de sustituir x = 0.5
prob, _ = quad(f_cond_numeric, 0, 0.5)
print("P(Y < 0.5 | X = 0.5) =", prob)
```

**Explicación del código:**

* `sympy` se usa para mostrar derivaciones simbólicas limpias (marginal y forma condicional).
* `scipy.integrate.quad` se usa para la integral numérica (rápida y precisa).

---

**5.3.1 PMF Condicional (Conditional PMF)**

```python
## Código Python para PMF Condicional (Ejemplo)
import numpy as np
from fractions import Fraction

## PMF Conjunta P(x, y)
P_XY = {(0, 0): 0, (0, 1): Fraction(2, 15), (0, 2): Fraction(1, 15),
        (1, 0): Fraction(3, 15), (1, 1): Fraction(6, 15), (1, 2): 0,
        (2, 0): Fraction(3, 15), (2, 1): 0, (2, 2): 0}

## PMF Marginal de X
P_X_1 = Fraction(9, 15)
print(f"PMF Marginal P_X(1) = {P_X_1}")

## Calcular PMF Condicional P(Y | X=1)
print("\nPMF Condicional P(Y | X=1):")
for y in range(3):
    P_Y_cond_X = P_XY[(1, y)] / P_X_1
    print(f"P(Y={y} | X=1) = {P_Y_cond_X}")
```

**5.3.1 PMF Condicional (variables discretas)**

Código Python (comprobación exacta con fractions y simulación con numpy)

```python
## Código de comprobación en Colab
from fractions import Fraction
import numpy as np
from collections import Counter

## PMF conjunta (fracciones exactas)
P_XY = {
    (0,0): Fraction(0,15), (0,1): Fraction(2,15), (0,2): Fraction(1,15),
    (1,0): Fraction(3,15), (1,1): Fraction(6,15), (1,2): Fraction(0,15),
    (2,0): Fraction(3,15), (2,1): Fraction(0,15), (2,2): Fraction(0,15)
}

## Marginal P_X(1)
P_X_1 = sum(P for (x,y),P in P_XY.items() if x==1)
print("P_X(1) =", P_X_1)  # Esperado: 9/15

## PMF condicional exacta
print("P(Y|X=1):")
for y in [0,1,2]:
    val = P_XY[(1,y)] / P_X_1
    print(f" y={y}: {val} = {float(val):.6f}")

## Simulación para validar (aprox.)
urn = [ 'R' ]*3 + [ 'A' ]*2 + [ 'V' ]*1
N = 200000
counts = Counter()
for _ in range(N):
    draw = np.random.choice(urn, size=2, replace=False)
    x = sum(1 for b in draw if b=='R')
    y = sum(1 for b in draw if b=='A')
    counts[(x,y)] += 1

print("\nFrecuencias simuladas (normalizadas) para (1,0) y (1,1):")
print("P_sim(1,0) = ", counts[(1,0)]/N)
print("P_sim(1,1) = ", counts[(1,1)]/N)
print("P_sim(Y|X=1) estimada (condicional) =")
## condicional simulada: P(Y=y | X=1) = P_sim(1,y) / sum_y P_sim(1,y)
total_X1 = sum(counts[(1,y)] for y in [0,1,2])
for y in [0,1,2]:
    print(f" y={y}: {counts[(1,y)]/total_X1:.6f}")
```

Explicación del código:

Se usa Fraction para operar con exactitud racional y evitar errores de punto flotante en las fracciones teóricas.

Se incluye una simulación (Monte Carlo) para validar que las probabilidades teóricas coinciden con la estimación empírica al aumentar N.

## 5.4 Esperanza Condicional — desarrollo ampliado

### Intuición y utilidad profunda

La esperanza condicional $E[Y|X=x]$ resume en un solo número la distribución condicional de $Y$ cuando $X$ es conocido. Es la **regresión poblacional**: la función $g(x)=E[Y|X=x]$ es la curva de regresión (verdadera) que minimiza el error cuadrático medio (MSE) entre $Y$ y cualquier predictor medible en función de $X$.

**Propiedad optimizadora:** si buscamos $\hat{g}(X)$ que minimice $\mathbb{E}[(Y - \hat{g}(X))^2]$, la solución es $\hat{g}(X) = E[Y|X]$.

---

### Definición formal (recordatorio)

* **Discreta:**
  $$
  E[Y|X=x] = \sum_y y,P_{Y|X}(y|x).
  $$
* **Continua:**
  $$
  E[Y|X=x] = \int_{-\infty}^{\infty} y,f_{Y|X}(y|x),dy.
  $$

### Propiedades importantes

1. **Linealidad en $Y$:** $E[aY + b \mid X] = a E[Y|X] + b$.
2. **Iteración (Ley de la Esperanza Total):** $E[Y] = E[E[Y|X]]$.
3. **Si $X$ e $Y$ independientes:** $E[Y|X] = E[Y]$ (constante).

---

### Ejemplo completo (discreto): Esperanza condicional y Ley de la Expectativa Total (Urna)

Reusamos los resultados previos del ejemplo de la urna.

**Condicionales ya calculadas (resumen):**

* $E[Y|X=0] = 4/3$ (esto se obtiene al calcular la distribución condicional $P_{Y|X}(y|0)$ y aplicar la suma).
* $E[Y|X=1] = 2/3$.
* $E[Y|X=2] = 0$.

**Marginales de $X$:**

* $P_X(0)=3/15$, $P_X(1)=9/15$, $P_X(2)=3/15$.

**Aplicación de LET:**
$$
E[Y] = \sum_{x} E[Y|X=x] P_X(x)
= \frac{4}{3}\cdot\frac{3}{15} + \frac{2}{3}\cdot\frac{9}{15} + 0\cdot\frac{3}{15}
= \frac{4}{15} + \frac{6}{15} = \frac{10}{15} = \frac{2}{3}.
$$

**Interpretación:** la esperanza incondicional que obtuvimos (2/3) coincide con el promedio ponderado de las esperanzas condicionales, tal como establece la LET.

---

#### Código Python: cálculo de $E[Y|X=x]$ y verificación de LET (exacto y por simulación)

```python
## Cálculo de E[Y|X=x] exacto usando Fracciones y verificación de LET
from fractions import Fraction
import numpy as np

## PMF conjunta (fracciones)
P_XY = {
    (0,0): Fraction(0,15), (0,1): Fraction(2,15), (0,2): Fraction(1,15),
    (1,0): Fraction(3,15), (1,1): Fraction(6,15), (1,2): Fraction(0,15),
    (2,0): Fraction(3,15), (2,1): Fraction(0,15), (2,2): Fraction(0,15)
}

## Marginal P_X
P_X = {x: sum(P for (xx,yy),P in P_XY.items() if xx==x) for x in [0,1,2]}

## E[Y | X=x] exacto
E_Y_given_X = {}
for x in [0,1,2]:
## sumar y * P_{Y|X}(y|x) = sum_y y * P(x,y) / P_X(x)
    if P_X[x] == 0:
        E_Y_given_X[x] = None
    else:
        E_Y_given_X[x] = sum(Fraction(y,1) * P_XY[(x,y)] for y in [0,1,2]) / P_X[x]

print("P_X:", P_X)
print("E[Y | X=x]:", E_Y_given_X)

## Verificación Ley de la Expectativa Total
E_Y = sum(E_Y_given_X[x] * P_X[x] for x in [0,1,2])
print("E[Y] (por LET) =", E_Y, " = ", float(E_Y))
```

**Salida esperada (fracciones):**

* $P_X = {0:3/15, 1:9/15, 2:3/15}$
* $E[Y|X=0]=4/3$, $E[Y|X=1]=2/3$, $E[Y|X=2]=0$
* $E[Y]$ por LET = $2/3$.

---

### Comentarios finales sobre 5.4

* En problemas reales, $E[Y|X]$ puede no ser una simple función algebraica; con frecuencia se estima por métodos no paramétricos (kernel regression) o paramétricos (regresión lineal, GLM).
* La LET es extremadamente útil cuando la marginal $f_Y$ es difícil de obtener pero las condicionales $f_{Y|X}$ o $P_{Y|X}$ son manejables.

**Código Python: cálculo de  E[Y|X=x]  y verificación de LET (exacto y por simulación)**

```python
## Cálculo de E[Y|X=x] exacto usando Fracciones y verificación de LET
from fractions import Fraction
import numpy as np

## PMF conjunta (fracciones)
P_XY = {
    (0,0): Fraction(0,15), (0,1): Fraction(2,15), (0,2): Fraction(1,15),
    (1,0): Fraction(3,15), (1,1): Fraction(6,15), (1,2): Fraction(0,15),
    (2,0): Fraction(3,15), (2,1): Fraction(0,15), (2,2): Fraction(0,15)
}

## Marginal P_X
P_X = {x: sum(P for (xx,yy),P in P_XY.items() if xx==x) for x in [0,1,2]}

## E[Y | X=x] exacto
E_Y_given_X = {}
for x in [0,1,2]:
## sumar y * P_{Y|X}(y|x) = sum_y y * P(x,y) / P_X(x)
    if P_X[x] == 0:
        E_Y_given_X[x] = None
    else:
        E_Y_given_X[x] = sum(Fraction(y,1) * P_XY[(x,y)] for y in [0,1,2]) / P_X[x]

print("P_X:", P_X)
print("E[Y | X=x]:", E_Y_given_X)

## Verificación Ley de la Expectativa Total
E_Y = sum(E_Y_given_X[x] * P_X[x] for x in [0,1,2])
print("E[Y] (por LET) =", E_Y, " = ", float(E_Y))
```

## 5.5 Suma de Dos Variables Aleatorias — Convolución (Parte B extendida)

## 5.5 Introducción y motivación

Sea $Z=X+Y$. Conocer la distribución de $Z$ es fundamental en muchas aplicaciones: tiempo total de servicio, suma de errores, agregación de retornos, combinación de señales, y muchas más. La herramienta matemática que permite construir la distribución de la suma a partir de las distribuciones individuales es la **convolución**.

---

## 5.5.1 Definición (discreta y continua)

**Discreta (si $X,Y$ independientes):**

$$
\displaystyle P_Z(z)=P(X+Y=z)=\sum_{x} P_X(x)\,P_Y(z-x).
$$

**Continua (si $X,Y$ independientes):**

$$
\displaystyle f_Z(z)=\int_{-\infty}^{\infty} f_X(x)\,f_Y(z-x)\,dx.
$$

En ambos casos la convolución suma la contribución de todas las parejas $(x,y)$ tales que $x+y=z$.

---

## 5.5.2 Intuición geométrica y mecánica

* **Geometría (continua):** piensa en $f_X(x)$ como una “forma” sobre el eje $x$. Para obtener $f_Z(z)$ tomas la función $f_Y$, la inviertes y la desplazas (o equivalente: la deslizas sobre $f_X$), multiplicas punto a punto y luego integras, obteniendo el área de superposición.  
* **Intuición (discreta):** para cada posible $x$ que $X$ puede tomar, la probabilidad de que $Z=z$ y $X=x$ es $P_X(x)P_Y(z-x)$; sumas sobre todos esos $x$.

---

## 5.5.3 Propiedades fundamentales

1. **Conmutatividad:** $f_X * f_Y = f_Y * f_X$  
2. **Asociatividad:** $(f_X * f_Y) * f_W = f_X * (f_Y * f_W)$  
3. **Linealidad:** $a(f*g)+b(f*h)=(af+bh)*g$ (con precauciones)  
4. **Normalización:** Si $f_X,f_Y$ son densidades, $f_X * f_Y$ está normalizada  
5. **Transformadas:** $\mathcal{F}\{f*g\} = \mathcal{F}\{f\}\cdot\mathcal{F}\{g\}$ (las transformadas de Fourier o MGFs convierten convoluciones en productos)  
6. **Momentos:** $E[X+Y]=E[X]+E[Y]$, y $\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)+2\mathrm{Cov}(X,Y)$.  
   Si son independientes, $\mathrm{Cov}=0$ y las varianzas se suman.

---

## 5.5.4 Ejemplos analíticos completos

### Ejemplo A — Discreto: Suma de dos dados justos ($1,\ldots,6$)

**Enunciado:** $X$ y $Y$ son dos dados justos independientes con $P_X(k)=1/6$ para $k=1,\dots,6$. Calcular $P_Z(z)$ para $Z=X+Y$.

**Solución analítica (paso a paso):**

Para $z\in\{2,\dots,12\}$:

$$
P_Z(z)=\sum_{x=1}^{6} P_X(x)P_Y(z-x)=\sum_{x=1}^{6} \frac{1}{6}\cdot \frac{1}{6}\,\mathbf{1}_{1\le z-x\le6}.
$$

El número de pares $(x,y)$ con $x+y=z$ es:

* para $z=2$: 1 par $(1,1)$ → $1/36$  
* $z=3$: 2 pares → $2/36$  
* ...  
* $z=7$: 6 pares → $6/36$  
* luego decrece simétricamente hasta $z=12$: 1 par → $1/36$  

Se obtiene la distribución triangular clásica.

**Código NumPy / visualización:**

```python
import numpy as np
import matplotlib.pyplot as plt

p = np.ones(6)/6  # pmf de un dado
## convolución discreta (modo 'full')
pz = np.convolve(p, p)
z_vals = np.arange(2, 13)
print("P(Z=z) para z=2..12:", np.round(pz, 4))

plt.stem(z_vals, pz, basefmt=" ")
plt.xlabel("z")
plt.ylabel("P(Z=z)")
plt.title("PMF de la suma de dos dados justos")
plt.grid(True)
plt.show()
````

---

### Ejemplo B — Discreto: Suma de Binomiales (demostración combinatoria)

**Enunciado:** Si $X\sim \mathrm{Binomial}(n_1,p)$ y $Y\sim \mathrm{Binomial}(n_2,p)$ independientes, demostrar que $Z=X+Y\sim\mathrm{Binomial}(n_1+n_2,p)$.

**Demostración (combinatoria simple):**

Interpreta $X$ como número de éxitos en un conjunto $A$ de $n_1$ ensayos independientes con probabilidad $p$, e $Y$ como número de éxitos en un conjunto $B$ de $n_2$ ensayos disjuntos. Entonces la unión $A\cup B$ contiene $n_1+n_2$ ensayos independientes con probabilidad $p$; el número total de éxitos en la unión es $X+Y$. Por la definición binomial:

$$
P(Z=k) = \binom{n_1+n_2}{k} p^k(1-p)^{n_1+n_2-k}.
$$

Formalmente se puede deducir por convolución:

$$
P_Z(k)=\sum_{i=0}^k \binom{n_1}{i}p^i(1-p)^{n_1-i}\cdot \binom{n_2}{k-i}p^{k-i}(1-p)^{n_2-(k-i)}.
$$

Factorizando $p^k(1-p)^{n_1+n_2-k}$ y usando la identidad de Vandermonde para binomios:

$$
\sum_{i=0}^k \binom{n_1}{i}\binom{n_2}{k-i} = \binom{n_1+n_2}{k},
$$

se obtiene el resultado.

**Código (verificación numérica con NumPy):**

```python
import numpy as np
from scipy.stats import binom

n1, n2, p = 5, 3, 0.4
x = np.arange(0, n1+1)
y = np.arange(0, n2+1)
pmf_x = binom.pmf(x, n1, p)
pmf_y = binom.pmf(y, n2, p)

pmf_z = np.convolve(pmf_x, pmf_y)
k = np.arange(0, n1+n2+1)
pmf_z_binom = binom.pmf(k, n1+n2, p)

np.testing.assert_allclose(pmf_z, pmf_z_binom, atol=1e-12)
print("Convolución coincide con Binomial(n1+n2,p).")
```

---

### Ejemplo C — Discreto: Suma de Poissons (prueba vía PGF / MGF)

**Enunciado:** Si $X\sim \mathrm{Poisson}(\lambda_1)$ y $Y\sim \mathrm{Poisson}(\lambda_2)$ independientes, entonces $Z=X+Y\sim\mathrm{Poisson}(\lambda_1+\lambda_2)$.

**Demostración (usando MGFs o PGFs):**

La función generadora de probabilidad (PGF) de Poisson es:

$$
G_X(s)=\mathbb{E}[s^X]=\exp(\lambda_1(s-1)), \quad G_Y(s)=\exp(\lambda_2(s-1)).
$$

Para la suma de independientes:

$$
G_Z(s)=G_X(s)G_Y(s)=\exp((\lambda_1+\lambda_2)(s-1)),
$$

que es la PGF de $\mathrm{Poisson}(\lambda_1+\lambda_2)$. Por unicidad, la distribución es Poisson con parámetro $\lambda_1+\lambda_2$.

**Código (verificación numérica):**

```python
import numpy as np
from scipy.stats import poisson

lam1, lam2 = 2.5, 1.7
kmax = 20
pmf_x = poisson.pmf(np.arange(kmax+1), lam1)
pmf_y = poisson.pmf(np.arange(kmax+1), lam2)
pmf_z_conv = np.convolve(pmf_x, pmf_y)[:kmax+1]
pmf_z_exact = poisson.pmf(np.arange(kmax+1), lam1+lam2)

print("Max diff approx:", np.max(np.abs(pmf_z_conv - pmf_z_exact)))
```

---

### Ejemplo D — Continua: Convolución de dos Uniformes $U[0,1]$ (triangular)

**Enunciado y objetivo:** Sea $X,Y\sim U[0,1]$ independientes. Calcular $f_Z(z)$ para $Z=X+Y$.

**Solución analítica (integral):**

$$
f_Z(z) = \int_{-\infty}^{\infty} f_X(x) f_Y(z-x),dx
= \int_{0}^{1} 1\cdot \mathbf{1}_{0\le z-x\le1},dx.
$$

El intervalo de integración efectivo es $x\in[\max(0,z-1),\min(1,z)]$.
Por tanto:

$$
f_Z(z) = z \quad \text{para } 0 \le z \le 1
$$
$$
f_Z(z) = 2-z \quad \text{para } 1 < z \le 2
$$
$$
f_Z(z) = 0 \quad \text{en otro caso}
$$

Con lo que $f_Z$ es la distribución triangular clásica en $[0,2]$.

**Demostración simbólica con SymPy:**

```python
import sympy as sp
x, z = sp.symbols('x z', real=True)
fZ = sp.integrate(1, (x, sp.Max(0, z-1), sp.Min(1, z)))
sp.simplify(fZ)
```

**Código Numérico (convolución FFT y comparación):**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve

N = 1000
x = np.linspace(0, 1, N)
dx = x[1]-x[0]
fX = np.ones_like(x)
fY = np.ones_like(x)
fZ_num = fftconvolve(fX, fY) * dx
z = np.linspace(0, 2, len(fZ_num))
fZ_theo = np.where(z<=1, z, 2-z)
fZ_theo = np.where((z<0)|(z>2), 0, fZ_theo)

plt.plot(z, fZ_num, label='numérica (fft conv)')
plt.plot(z, fZ_theo, '--', label='teórica')
plt.legend()
plt.xlabel('z'); plt.ylabel('f_Z(z)')
plt.title('Convolución Uniformes[0,1]')
plt.show()
```

---

### Ejemplo E — Continua: Suma de Normales

**Enunciado:** Si $X\sim N(\mu_1,\sigma_1^2)$ y $Y\sim N(\mu_2,\sigma_2^2)$ independientes, entonces $Z=X+Y\sim N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$.

**Demostración (función característica):**

$$
\phi_X(t)=\exp\big(i\mu_1 t - \tfrac12 \sigma_1^2 t^2\big),\quad
\phi_Y(t)=\exp\big(i\mu_2 t - \tfrac12 \sigma_2^2 t^2\big).
$$

Para suma de independientes:

$$
\phi_Z(t)=\phi_X(t)\phi_Y(t)=\exp\big(i(\mu_1+\mu_2)t - \tfrac12(\sigma_1^2+\sigma_2^2)t^2\big),
$$

que corresponde a una $N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$.

**Código Numérico:**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.signal import fftconvolve

x = np.linspace(-10, 10, 10000)
dx = x[1]-x[0]
fX = norm.pdf(x, loc=1.0, scale=2.0)
fY = norm.pdf(x, loc=-0.5, scale=1.5)
fZ_num = fftconvolve(fX, fY) * dx
z = np.linspace(2*x[0], 2*x[-1], len(fZ_num))
mu = 1.0 + (-0.5)
sigma = np.sqrt(2.0**2 + 1.5**2)
fZ_theo = norm.pdf(z, loc=mu, scale=sigma)

plt.plot(z, fZ_num, label='numérica (conv)')
plt.plot(z, fZ_theo, '--', label='teórica')
plt.legend(); plt.xlim(-5,7)
plt.show()
```

---

## 5.5.6 Tabla 5.5.4 — Suma de distribuciones comunes

<table style="border-collapse:collapse; width:100%; text-align:center; font-family:'Times New Roman',serif; font-size:15px;">
  <thead style="background-color:#f2f2f2;">
    <tr>
      <th style="border:1px solid #ccc; padding:8px; width:20%;">Distribución de <i>X</i></th>
      <th style="border:1px solid #ccc; padding:8px; width:20%;">Distribución de <i>Y</i></th>
      <th style="border:1px solid #ccc; padding:8px; width:40%;">Distribución de <i>Z = X + Y</i></th>
      <th style="border:1px solid #ccc; padding:8px; width:20%;">Demostración rápida / nota</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Binomial}(n_1,p)$</td>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Binomial}(n_2,p)$</td>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Binomial}(n_1+n_2,p)$</td>
      <td style="border:1px solid #ccc; text-align:left; padding:6px;">
        Identidad de Vandermonde aplicada a la convolución de PMFs; interpretación como unión de ensayos independientes.
      </td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Poisson}(\lambda_1)$</td>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Poisson}(\lambda_2)$</td>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Poisson}(\lambda_1+\lambda_2)$</td>
      <td style="border:1px solid #ccc; text-align:left; padding:6px;">
        Uso de PGF o MGF: el producto de PGFs da la PGF de Poisson con parámetro $\lambda_1+\lambda_2$.
      </td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Normal}(\mu_1,\sigma_1^2)$</td>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Normal}(\mu_2,\sigma_2^2)$</td>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Normal}(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$</td>
      <td style="border:1px solid #ccc; text-align:left; padding:6px;">
        Derivado mediante transformada característica o completando cuadrados en la integral de convolución.
      </td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Gamma}(\alpha_1,\theta)$</td>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Gamma}(\alpha_2,\theta)$</td>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Gamma}(\alpha_1+\alpha_2,\theta)$</td>
      <td style="border:1px solid #ccc; text-align:left; padding:6px;">
        Convolución de densidades Gamma con mismo <em>scale</em>; identidad por propiedades de la función Gamma.
      </td>
    </tr>
  </tbody>
</table>

---

### Código de referencia consolidado

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve, convolve
from scipy.stats import norm, poisson, binom
import sympy as sp
from scipy.integrate import quad
```

## Análisis Multivariado: Vectores Aleatorios, Covarianza y PCA

## 5.6 Vectores Aleatorios y Matrices de Covarianza

### 5.6.1 Definición e Intuición Geométrica

Un **vector aleatorio** $\mathbf{X}$ en $\mathbb{R}^p$ es una colección de $p$ variables aleatorias:

$$
\mathbf{X} = \begin{pmatrix} X_1 \\ X_2 \\ \vdots \\ X_p \end{pmatrix}
$$

**Intuición geométrica:** Cada realización de $\mathbf{X}$ representa un punto en el espacio $p$-dimensional. La nube de puntos resultante revela la estructura de dependencia entre variables.

**Ejemplo visual:** Consideremos el caso bidimensional $(X,Y)$:
- Si $X$ e $Y$ son independientes: nube de puntos isotrópica
- Si $X$ e $Y$ están correlacionadas: nube de puntos elipsoidal
- Si $X$ e $Y$ tienen correlación perfecta: puntos alineados

### 5.6.2 Función de Densidad de Probabilidad Conjunta

Para variables continuas, la PDF conjunta $f_{\mathbf{X}}(\mathbf{x})$ satisface:

$$
P(\mathbf{X} \in R) = \int_R f_{\mathbf{X}}(\mathbf{x})  d\mathbf{x}
$$

**Caso especial - Independencia:**
$$
f_{\mathbf{X}}(\mathbf{x}) = \prod_{i=1}^p f_{X_i}(x_i)
$$

**Ejemplo detallado:** Distribución uniforme en región triangular

Sea $f_{X,Y}(x,y) = 2$ para $0 \le x \le 1$, $0 \le y \le x$, y $0$ en otro caso.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

## Verificación de normalización
result, error = integrate.dblquad(lambda y, x: 2, 0, 1, lambda x: 0, lambda x: x)
print(f"Integral de la PDF: {result}, Error: {error}")

## Visualización
x_vals = np.linspace(0, 1, 100)
y_vals = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = np.where(Y <= X, 2, 0)

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, levels=20)
plt.colorbar()
plt.title('PDF Conjunta en Región Triangular')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```

### 5.6.3 Vector de Esperanza (Media)

$$
\mathbb{E}[\mathbf{X}] = \begin{pmatrix} \mathbb{E}[X_1] \\ \mathbb{E}[X_2] \\ \vdots \\ \mathbb{E}[X_p] \end{pmatrix}
$$

**Ejemplo analítico extendido:** Para la distribución triangular anterior:

```python
## Cálculo de esperanzas marginales
E_X = integrate.dblquad(lambda y, x: x * 2, 0, 1, lambda x: 0, lambda x: x)[0]
E_Y = integrate.dblquad(lambda y, x: y * 2, 0, 1, lambda x: 0, lambda x: x)[0]

print(f"E[X] = {E_X:.3f}")
print(f"E[Y] = {E_Y:.3f}")

## Cálculo usando sympy para precisión analítica
import sympy as sp
x, y = sp.symbols('x y', real=True, positive=True)
f_xy = 2

E_X_sym = sp.integrate(x * f_xy, (y, 0, x), (x, 0, 1))
E_Y_sym = sp.integrate(y * f_xy, (y, 0, x), (x, 0, 1))

print(f"E[X] (analítico) = {E_X_sym} = {float(E_X_sym):.3f}")
print(f"E[Y] (analítico) = {E_Y_sym} = {float(E_Y_sym):.3f}")
```

### 5.6.4 Matriz de Covarianza - Teoría Profunda

La matriz de covarianza $\mathbf{\Sigma}$ se define como:

$$
\mathbf{\Sigma} = \mathbb{E}[(\mathbf{X} - \mathbf{\mu})(\mathbf{X} - \mathbf{\mu})^T]
$$

**Descomposición en componentes:**

- **Elementos diagonales:** $\Sigma_{ii} = \text{Var}(X_i)$
- **Elementos no diagonales:** $\Sigma_{ij} = \text{Cov}(X_i, X_j)$

**Propiedades fundamentales:**
1. **Simetría:** $\mathbf{\Sigma} = \mathbf{\Sigma}^T$
2. **Positivo semidefinida:** $\mathbf{z}^T\mathbf{\Sigma}\mathbf{z} \ge 0$ para todo $\mathbf{z}$
3. **Rango:** Indica dependencias lineales entre variables

**Ejemplo computacional detallado:**

```python
def calcular_covarianza_analitica():
    """Cálculo analítico completo de la matriz de covarianza"""
## Para la distribución triangular f(x,y)=2, 0≤y≤x≤1
    
## Esperanzas
    E_X = 2/3
    E_Y = 1/3
    
## Segundos momentos
    E_X2 = sp.integrate(x**2 * f_xy, (y, 0, x), (x, 0, 1))
    E_Y2 = sp.integrate(y**2 * f_xy, (y, 0, x), (x, 0, 1))
    E_XY = sp.integrate(x*y * f_xy, (y, 0, x), (x, 0, 1))
    
## Varianzas y covarianza
    Var_X = E_X2 - E_X**2
    Var_Y = E_Y2 - E_Y**2
    Cov_XY = E_XY - E_X * E_Y
    
    Sigma = np.array([[Var_X, Cov_XY], [Cov_XY, Var_Y]])
    return Sigma

Sigma_analitica = calcular_covarianza_analitica()
print("Matriz de covarianza analítica:")
print(Sigma_analitica)

## Verificación por simulación
def generar_muestra_triangular(n=10000):
    """Genera muestras de la distribución triangular"""
    u1 = np.random.uniform(0, 1, n)
    u2 = np.random.uniform(0, 1, n)
    x = np.maximum(u1, u2)
    y = np.minimum(u1, u2)
    return np.column_stack([x, y])

muestra = generar_muestra_triangular(100000)
Sigma_muestral = np.cov(muestra, rowvar=False)

print("\nMatriz de covarianza muestral:")
print(Sigma_muestral)
```

### 5.6.5 Distribución Normal Multivariada

La PDF de una normal $p$-dimensional $\mathbf{X} \sim \mathcal{N}(\mathbf{\mu}, \mathbf{\Sigma})$ es:

$$
f(\mathbf{x}) = \frac{1}{(2\pi)^{p/2}|\mathbf{\Sigma}|^{1/2}} \exp\left(-\frac{1}{2}(\mathbf{x}-\mathbf{\mu})^T\mathbf{\Sigma}^{-1}(\mathbf{x}-\mathbf{\mu})\right)
$$

**Interpretación geométrica de la distancia de Mahalanobis:**

```python
def visualizar_normal_multivariada():
    """Visualización completa de distribución normal bivariada"""
    mu = np.array([0, 0])
    Sigma = np.array([[2, 1], [1, 1]])
    
## Generar puntos en la elipse de confianza
    theta = np.linspace(0, 2*np.pi, 100)
    circle = np.column_stack([np.cos(theta), np.sin(theta)])
    
## Descomposición espectral para transformar círculo a elipse
    eigenvals, eigenvecs = np.linalg.eig(Sigma)
    ellipse = circle @ np.diag(np.sqrt(eigenvals)) @ eigenvecs.T
    ellipse += mu
    
## Gráfico
    plt.figure(figsize=(10, 8))
    plt.plot(ellipse[:, 0], ellipse[:, 1], 'r-', linewidth=2, label='Elipse 1-sigma')
    plt.quiver(mu[0], mu[1], eigenvecs[0,0]*np.sqrt(eigenvals[0]),
               eigenvecs[1,0]*np.sqrt(eigenvals[0]),
               angles='xy', scale_units='xy', scale=1, color='blue', width=0.01, label='PC1')
    plt.quiver(mu[0], mu[1], eigenvecs[0,1]*np.sqrt(eigenvals[1]),
               eigenvecs[1,1]*np.sqrt(eigenvals[1]),
               angles='xy', scale_units='xy', scale=1, color='green', width=0.01, label='PC2')
    
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.legend()
    plt.title('Distribución Normal Bivariada y Componentes Principales')
    plt.show()

visualizar_normal_multivariada()
```

EJEMPLO A

```python
import numpy as np
import matplotlib.pyplot as plt

p = np.ones(6)/6  # pmf de un dado
## convolución discreta (modo 'full')
pz = np.convolve(p, p)
z_vals = np.arange(2, 13)
print("P(Z=z) para z=2..12:", np.round(pz, 4))

plt.stem(z_vals, pz, basefmt=" ")
plt.xlabel("z")
plt.ylabel("P(Z=z)")
plt.title("PMF de la suma de dos dados justos")
plt.grid(True)
plt.show()
```

EJEMPLO B

```python
import numpy as np
from scipy.stats import binom

n1, n2, p = 5, 3, 0.4
x = np.arange(0, n1+1)
y = np.arange(0, n2+1)
pmf_x = binom.pmf(x, n1, p)
pmf_y = binom.pmf(y, n2, p)

pmf_z = np.convolve(pmf_x, pmf_y)
k = np.arange(0, n1+n2+1)
pmf_z_binom = binom.pmf(k, n1+n2, p)

np.testing.assert_allclose(pmf_z, pmf_z_binom, atol=1e-12)
print("Convolución coincide con Binomial(n1+n2,p).")
```

EJEMPLO C

```python
import numpy as np
from scipy.stats import poisson

lam1, lam2 = 2.5, 1.7
kmax = 20
pmf_x = poisson.pmf(np.arange(kmax+1), lam1)
pmf_y = poisson.pmf(np.arange(kmax+1), lam2)
pmf_z_conv = np.convolve(pmf_x, pmf_y)[:kmax+1]
pmf_z_exact = poisson.pmf(np.arange(kmax+1), lam1+lam2)

print("Max diff approx:", np.max(np.abs(pmf_z_conv - pmf_z_exact)))
```

EJEMPLO D

```python
import sympy as sp
x, z = sp.symbols('x z', real=True)
fZ = sp.integrate(1, (x, sp.Max(0, z-1), sp.Min(1, z)))
sp.simplify(fZ)
```

**Código Numérico (convolución FFT y comparación):**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve

N = 1000
x = np.linspace(0, 1, N)
dx = x[1]-x[0]
fX = np.ones_like(x)
fY = np.ones_like(x)
fZ_num = fftconvolve(fX, fY) * dx
z = np.linspace(0, 2, len(fZ_num))
fZ_theo = np.where(z<=1, z, 2-z)
fZ_theo = np.where((z<0)|(z>2), 0, fZ_theo)

plt.plot(z, fZ_num, label='numérica (fft conv)')
plt.plot(z, fZ_theo, '--', label='teórica')
plt.legend()
plt.xlabel('z'); plt.ylabel('f_Z(z)')
plt.title('Convolución Uniformes[0,1]')
plt.show()
```

EJEMPLO E

**Código numérico**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.signal import fftconvolve

x = np.linspace(-10, 10, 10000)
dx = x[1]-x[0]
fX = norm.pdf(x, loc=1.0, scale=2.0)
fY = norm.pdf(x, loc=-0.5, scale=1.5)
fZ_num = fftconvolve(fX, fY) * dx
z = np.linspace(2*x[0], 2*x[-1], len(fZ_num))
mu = 1.0 + (-0.5)
sigma = np.sqrt(2.0**2 + 1.5**2)
fZ_theo = norm.pdf(z, loc=mu, scale=sigma)

plt.plot(z, fZ_num, label='numérica (conv)')
plt.plot(z, fZ_theo, '--', label='teórica')
plt.legend(); plt.xlim(-5,7)
plt.show()
```

**Importar librerías**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve, convolve
from scipy.stats import norm, poisson, binom
import sympy as sp
from scipy.integrate import quad
```

**5.6.2 Función de Densidad de Probabilidad Conjunta**

Distribución uniforme triangular

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

## Verificación de normalización
result, error = integrate.dblquad(lambda y, x: 2, 0, 1, lambda x: 0, lambda x: x)
print(f"Integral de la PDF: {result}, Error: {error}")

## Visualización
x_vals = np.linspace(0, 1, 100)
y_vals = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = np.where(Y <= X, 2, 0)

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, levels=20)
plt.colorbar()
plt.title('PDF Conjunta en Región Triangular')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```

**5.6.3 Vector de Esperanza (Media)**

Ejemplo analítico extendido: Para la distribución triangular anterior:

```python
## Cálculo de esperanzas marginales
E_X = integrate.dblquad(lambda y, x: x * 2, 0, 1, lambda x: 0, lambda x: x)[0]
E_Y = integrate.dblquad(lambda y, x: y * 2, 0, 1, lambda x: 0, lambda x: x)[0]

print(f"E[X] = {E_X:.3f}")
print(f"E[Y] = {E_Y:.3f}")

## Cálculo usando sympy para precisión analítica
import sympy as sp
x, y = sp.symbols('x y', real=True, positive=True)
f_xy = 2

E_X_sym = sp.integrate(x * f_xy, (y, 0, x), (x, 0, 1))
E_Y_sym = sp.integrate(y * f_xy, (y, 0, x), (x, 0, 1))

print(f"E[X] (analítico) = {E_X_sym} = {float(E_X_sym):.3f}")
print(f"E[Y] (analítico) = {E_Y_sym} = {float(E_Y_sym):.3f}")
```

**5.6.4 Matriz de Covarianza - Teoría Profunda**

Ejemplo computacional detallado

```python
import sympy as sp
import numpy as np

def calcular_covarianza_analitica():
    """Cálculo analítico completo de la matriz de covarianza"""
## Para la distribución triangular f(x,y)=2, 0≤y≤x≤1

## Esperanzas
    E_X = 2/3
    E_Y = 1/3

## Define symbols and function within the function scope
    x, y = sp.symbols('x y', real=True, positive=True)
    f_xy = 2

## Segundos momentos
    E_X2 = sp.integrate(x**2 * f_xy, (y, 0, x), (x, 0, 1))
    E_Y2 = sp.integrate(y**2 * f_xy, (y, 0, x), (x, 0, 1))
    E_XY = sp.integrate(x*y * f_xy, (y, 0, x), (x, 0, 1))

## Convert SymPy results to float for numpy array
    Var_X = float(E_X2 - E_X**2)
    Var_Y = float(E_Y2 - E_Y**2)
    Cov_XY = float(E_XY - E_X * E_Y)

    Sigma = np.array([[Var_X, Cov_XY], [Cov_XY, Var_Y]])
    return Sigma

Sigma_analitica = calcular_covarianza_analitica()
print("Matriz de covarianza analítica:")
print(Sigma_analitica)

## Verificación por simulación
def generar_muestra_triangular(n=10000):
    """Genera muestras de la distribución triangular"""
    u1 = np.random.uniform(0, 1, n)
    u2 = np.random.uniform(0, 1, n)
    x = np.maximum(u1, u2)
    y = np.minimum(u1, u2)
    return np.column_stack([x, y])

muestra = generar_muestra_triangular(100000)
Sigma_muestral = np.cov(muestra, rowvar=False)

print("\nMatriz de covarianza muestral:")
print(Sigma_muestral)
```

**5.6.5 Distribución Normal Multivariada**

Interpretación geométrica de la distancia de Mahalanobis:

```python
def visualizar_normal_multivariada():
    """Visualización completa de distribución normal bivariada"""
    mu = np.array([0, 0])
    Sigma = np.array([[2, 1], [1, 1]])

## Generar puntos en la elipse de confianza
    theta = np.linspace(0, 2*np.pi, 100)
    circle = np.column_stack([np.cos(theta), np.sin(theta)])

## Descomposición espectral para transformar círculo a elipse
    eigenvals, eigenvecs = np.linalg.eig(Sigma)
    ellipse = circle @ np.diag(np.sqrt(eigenvals)) @ eigenvecs.T
    ellipse += mu

## Gráfico
    plt.figure(figsize=(10, 8))
    plt.plot(ellipse[:, 0], ellipse[:, 1], 'r-', linewidth=2, label='Elipse 1-sigma')
    plt.quiver(mu[0], mu[1], eigenvecs[0,0]*np.sqrt(eigenvals[0]),
               eigenvecs[1,0]*np.sqrt(eigenvals[0]),
               angles='xy', scale_units='xy', scale=1, color='blue', width=0.01, label='PC1')
    plt.quiver(mu[0], mu[1], eigenvecs[0,1]*np.sqrt(eigenvals[1]),
               eigenvecs[1,1]*np.sqrt(eigenvals[1]),
               angles='xy', scale_units='xy', scale=1, color='green', width=0.01, label='PC2')

    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.legend()
    plt.title('Distribución Normal Bivariada y Componentes Principales')
    plt.show()

visualizar_normal_multivariada()
```

## 5.7 Transformaciones de Gaussianas Multidimensionales

### 5.7.1 Transformaciones Lineales - Teoría Extendida

Sea $\mathbf{Y} = \mathbf{A}\mathbf{X} + \mathbf{b}$ con $\mathbf{X} \sim \mathcal{N}(\mathbf{\mu}_X, \mathbf{\Sigma}_X)$. Entonces:

$$
\mathbf{Y} \sim \mathcal{N}(\mathbf{A}\mathbf{\mu}_X + \mathbf{b}, \mathbf{A}\mathbf{\Sigma}_X\mathbf{A}^T)
$$

**Ejemplo multidimensional:**

```python
def transformacion_lineal_multivariada():
    """Ejemplo completo de transformación lineal de vector gaussiano"""
## Distribución original
    mu_X = np.array([1, 2, 3])
    Sigma_X = np.array([[4, 1, 0.5],
                       [1, 3, 0.8],
                       [0.5, 0.8, 2]])
    
## Matriz de transformación (reducción de dimensionalidad)
    A = np.array([[1, 0.5, 0],
                  [0, 1, 1]])
    b = np.array([-1, 2])
    
## Distribución transformada
    mu_Y = A @ mu_X + b
    Sigma_Y = A @ Sigma_X @ A.T
    
    print("Distribución original:")
    print(f"μ_X = {mu_X}")
    print(f"Σ_X =\n{Sigma_X}")
    
    print("\nDistribución transformada:")
    print(f"μ_Y = {mu_Y}")
    print(f"Σ_Y =\n{Sigma_Y}")
    
## Verificación por simulación
    X = np.random.multivariate_normal(mu_X, Sigma_X, 10000)
    Y_sim = (A @ X.T + b.reshape(-1, 1)).T
    
    print("\nVerificación por simulación:")
    print(f"μ_Y_sim = {np.mean(Y_sim, axis=0)}")
    print(f"Σ_Y_sim =\n{np.cov(Y_sim, rowvar=False)}")

transformacion_lineal_multivariada()
```

### 5.7.2 Descomposición Espectral y Geometría

La descomposición $\mathbf{\Sigma} = \mathbf{V}\mathbf{\Lambda}\mathbf{V}^T$ revela:

- **Eigenvectores:** Direcciones principales de variación
- **Eigenvalores:** Magnitud de variación en cada dirección

**Análisis geométrico completo:**

```python
def analisis_espectral_completo(Sigma):
    """Análisis completo de la descomposición espectral"""
    eigenvals, eigenvecs = np.linalg.eig(Sigma)
    
    print("Descomposición Espectral:")
    print(f"Eigenvalores: {eigenvals}")
    print(f"Eigenvectores:\n{eigenvecs}")
    
## Verificación de ortogonalidad
    print(f"\nOrtogonalidad (V·V^T):\n{eigenvecs @ eigenvecs.T}")
    
## Proporción de varianza explicada
    var_total = np.sum(eigenvals)
    prop_var = eigenvals / var_total
    print(f"\nProporción de varianza explicada: {prop_var}")
    
    return eigenvals, eigenvecs

Sigma_ejemplo = np.array([[5, 2, 1],
                         [2, 3, 0.5],
                         [1, 0.5, 2]])
analisis_espectral_completo(Sigma_ejemplo)
```

### 5.7.3 Blanqueamiento (Whitening) - Implementación Completa

El blanqueamiento transforma los datos para tener covarianza identidad:

```python
class WhiteningTransformer:
    """Implementación completa de blanqueamiento gaussiano"""
    
    def __init__(self, method='zca'):
        self.method = method  # 'zca', 'pca', 'cholesky'
        
    def fit(self, X):
        self.mu = np.mean(X, axis=0)
        X_centered = X - self.mu
        self.Sigma = np.cov(X_centered, rowvar=False)
        
## Descomposición espectral
        self.eigenvals, self.eigenvecs = np.linalg.eig(self.Sigma)
        
        if self.method == 'pca':
## Blanqueamiento PCA
            self.W = self.eigenvecs @ np.diag(1.0 / np.sqrt(self.eigenvals)) @ self.eigenvecs.T
        elif self.method == 'zca':
## Blanqueamiento ZCA (Mahalanobis)
            self.W = np.linalg.inv(self.eigenvecs @ np.diag(np.sqrt(self.eigenvals)) @ self.eigenvecs.T)
        else:  # Cholesky
            self.W = np.linalg.cholesky(np.linalg.inv(self.Sigma))
        
        return self
    
    def transform(self, X):
        X_centered = X - self.mu
        return X_centered @ self.W.T
    
    def inverse_transform(self, Z):
        return Z @ np.linalg.inv(self.W.T) + self.mu

## Ejemplo de uso
X_data = np.random.multivariate_normal([1, 2], [[4, 2], [2, 3]], 1000)
whitener = WhiteningTransformer(method='zca').fit(X_data)
Z_white = whitener.transform(X_data)

print("Covarianza original:\n", np.cov(X_data.T))
print("\nCovarianza después de blanqueamiento:\n", np.cov(Z_white.T))
```

**5.7.1 Transformaciones Lineales - Teoría Extendida**

Ejemplo multidimensional:

```python
def transformacion_lineal_multivariada():
    """Ejemplo completo de transformación lineal de vector gaussiano"""
## Distribución original
    mu_X = np.array([1, 2, 3])
    Sigma_X = np.array([[4, 1, 0.5],
                       [1, 3, 0.8],
                       [0.5, 0.8, 2]])

## Matriz de transformación (reducción de dimensionalidad)
    A = np.array([[1, 0.5, 0],
                  [0, 1, 1]])
    b = np.array([-1, 2])

## Distribución transformada
    mu_Y = A @ mu_X + b
    Sigma_Y = A @ Sigma_X @ A.T

    print("Distribución original:")
    print(f"μ_X = {mu_X}")
    print(f"Σ_X =\n{Sigma_X}")

    print("\nDistribución transformada:")
    print(f"μ_Y = {mu_Y}")
    print(f"Σ_Y =\n{Sigma_Y}")

## Verificación por simulación
    X = np.random.multivariate_normal(mu_X, Sigma_X, 10000)
    Y_sim = (A @ X.T + b.reshape(-1, 1)).T

    print("\nVerificación por simulación:")
    print(f"μ_Y_sim = {np.mean(Y_sim, axis=0)}")
    print(f"Σ_Y_sim =\n{np.cov(Y_sim, rowvar=False)}")

transformacion_lineal_multivariada()
```

**5.7.2 Descomposición Espectral y Geometría**

Análisis geométrico completo

```python
def analisis_espectral_completo(Sigma):
    """Análisis completo de la descomposición espectral"""
    eigenvals, eigenvecs = np.linalg.eig(Sigma)

    print("Descomposición Espectral:")
    print(f"Eigenvalores: {eigenvals}")
    print(f"Eigenvectores:\n{eigenvecs}")

## Verificación de ortogonalidad
    print(f"\nOrtogonalidad (V·V^T):\n{eigenvecs @ eigenvecs.T}")

## Proporción de varianza explicada
    var_total = np.sum(eigenvals)
    prop_var = eigenvals / var_total
    print(f"\nProporción de varianza explicada: {prop_var}")

    return eigenvals, eigenvecs

Sigma_ejemplo = np.array([[5, 2, 1],
                         [2, 3, 0.5],
                         [1, 0.5, 2]])
analisis_espectral_completo(Sigma_ejemplo)
```

**5.7.3 Blanqueamiento (Whitening) - Implementación Completa**

El blanqueamiento transforma los datos para tener covarianza identidad:

```python
class WhiteningTransformer:
    """Implementación completa de blanqueamiento gaussiano"""

    def __init__(self, method='zca'):
        self.method = method  # 'zca', 'pca', 'cholesky'

    def fit(self, X):
        self.mu = np.mean(X, axis=0)
        X_centered = X - self.mu
        self.Sigma = np.cov(X_centered, rowvar=False)

## Descomposición espectral
        self.eigenvals, self.eigenvecs = np.linalg.eig(self.Sigma)

        if self.method == 'pca':
## Blanqueamiento PCA
            self.W = self.eigenvecs @ np.diag(1.0 / np.sqrt(self.eigenvals)) @ self.eigenvecs.T
        elif self.method == 'zca':
## Blanqueamiento ZCA (Mahalanobis)
            self.W = np.linalg.inv(self.eigenvecs @ np.diag(np.sqrt(self.eigenvals)) @ self.eigenvecs.T)
        else:  # Cholesky
            self.W = np.linalg.cholesky(np.linalg.inv(self.Sigma))

        return self

    def transform(self, X):
        X_centered = X - self.mu
        return X_centered @ self.W.T

    def inverse_transform(self, Z):
        return Z @ np.linalg.inv(self.W.T) + self.mu

## Ejemplo de uso
X_data = np.random.multivariate_normal([1, 2], [[4, 2], [2, 3]], 1000)
whitener = WhiteningTransformer(method='zca').fit(X_data)
Z_white = whitener.transform(X_data)

print("Covarianza original:\n", np.cov(X_data.T))
print("\nCovarianza después de blanqueamiento:\n", np.cov(Z_white.T))
```

## 5.8 Análisis de Componentes Principales (PCA) - Profundización

### 5.8.1 Fundamentos Matemáticos Completos

Dado datos $\mathbf{X} \in \mathbb{R}^{n \times p}$, PCA encuentra:

1. **Centrado:** $\mathbf{X}_c = \mathbf{X} - \mathbf{1}\mathbf{\mu}^T$
2. **Descomposición:** $\mathbf{X}_c^T\mathbf{X}_c = \mathbf{V}\mathbf{\Lambda}\mathbf{V}^T$
3. **Proyección:** $\mathbf{Y} = \mathbf{X}_c\mathbf{V}_k$

**Implementación desde cero:**

```python
class PCAFromScratch:
    """Implementación completa de PCA desde primeros principios"""
    
    def __init__(self, n_components=None):
        self.n_components = n_components
        
    def fit(self, X):
## Centrado
        self.mean_ = np.mean(X, axis=0)
        X_centered = X - self.mean_
        
## Matriz de covarianza
        n_samples = X.shape[0]
        self.cov_matrix_ = (X_centered.T @ X_centered) / (n_samples - 1)
        
## Descomposición espectral
        eigenvals, eigenvecs = np.linalg.eig(self.cov_matrix_)
        
## Ordenar por eigenvalores descendentes
        idx = np.argsort(eigenvals)[::-1]
        self.eigenvalues_ = eigenvals[idx]
        self.components_ = eigenvecs[:, idx]
        
## Seleccionar componentes
        if self.n_components is not None:
            self.components_ = self.components_[:, :self.n_components]
            self.eigenvalues_ = self.eigenvalues_[:self.n_components]
            
## Varianza explicada
        self.explained_variance_ratio_ = self.eigenvalues_ / np.sum(self.eigenvalues_)
        
        return self
    
    def transform(self, X):
        X_centered = X - self.mean_
        return X_centered @ self.components_
    
    def inverse_transform(self, Y):
        return Y @ self.components_.T + self.mean_

## Comparación con scikit-learn
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

## Datos de ejemplo
iris = load_iris()
X = iris.data

## Nuestra implementación
pca_scratch = PCAFromScratch(n_components=2).fit(X)
X_pca_scratch = pca_scratch.transform(X)

## Scikit-learn
pca_sklearn = PCA(n_components=2).fit(X)
X_pca_sklearn = pca_sklearn.transform(X)

print("Varianza explicada (scratch):", pca_scratch.explained_variance_ratio_)
print("Varianza explicada (sklearn):", pca_sklearn.explained_variance_ratio_)
```

### 5.8.2 PCA en 2D y 3D - Ejemplos Visuales Completos

**Caso 2D - Rotación de datos correlacionados:**

```python
def pca_2d_demo():
    """Demo visual de PCA en 2 dimensiones"""
## Generar datos correlacionados
    np.random.seed(42)
    n_points = 300
    theta = np.random.uniform(0, 2*np.pi, n_points)
    r = np.random.normal(0, 0.3, n_points)
    
## Elipse rotada
    rotation_angle = np.pi/4
    rotation_matrix = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)],
                              [np.sin(rotation_angle), np.cos(rotation_angle)]])
    
    X_ellipse = np.column_stack([2*np.cos(theta) + r, 0.5*np.sin(theta) + r])
    X = X_ellipse @ rotation_matrix.T + [1, 2]
    
## Aplicar PCA
    pca = PCAFromScratch(n_components=2).fit(X)
    X_pca = pca.transform(X)
    
## Visualización
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
## Datos originales
    axes[0].scatter(X[:, 0], X[:, 1], alpha=0.6)
    axes[0].set_title('Datos Originales')
    axes[0].set_xlabel('X1')
    axes[0].set_ylabel('X2')
    axes[0].grid(True, alpha=0.3)
    axes[0].axis('equal')
    
## Datos + componentes principales
    axes[1].scatter(X[:, 0], X[:, 1], alpha=0.6)
    for length, vector in zip(pca.eigenvalues_, pca.components_.T):
        v = vector * np.sqrt(length) * 3  # Escalar para visualización
        axes[1].arrow(pca.mean_[0], pca.mean_[1], v[0], v[1],
                     head_width=0.1, head_length=0.1, fc='red', ec='red')
    axes[1].set_title('Componentes Principales')
    axes[1].set_xlabel('X1')
    axes[1].set_ylabel('X2')
    axes[1].grid(True, alpha=0.3)
    axes[1].axis('equal')
    
## Datos transformados
    axes[2].scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.6)
    axes[2].set_title('Espacio PCA (Decorrelacionado)')
    axes[2].set_xlabel('PC1')
    axes[2].set_ylabel('PC2')
    axes[2].grid(True, alpha=0.3)
    axes[2].axis('equal')
    
    plt.tight_layout()
    plt.show()

pca_2d_demo()
```

**Caso 3D - Reducción a 2D:**

```python
def pca_3d_demo():
    """Demo visual de PCA en 3 dimensiones con reducción a 2D"""
## Generar datos 3D correlacionados
    np.random.seed(42)
    n_points = 500
    
## Tres variables con diferentes correlaciones
    X1 = np.random.normal(0, 2, n_points)
    X2 = 0.7 * X1 + np.random.normal(0, 1, n_points)
    X3 = 0.5 * X1 + 0.3 * X2 + np.random.normal(0, 0.5, n_points)
    
    X_3d = np.column_stack([X1, X2, X3])
    
## Aplicar PCA
    pca_3d = PCAFromScratch(n_components=2).fit(X_3d)
    X_2d = pca_3d.transform(X_3d)
    
## Visualización 3D
    fig = plt.figure(figsize=(15, 5))
    
## Subplot 1: Datos originales 3D
    ax1 = fig.add_subplot(131, projection='3d')
    scatter = ax1.scatter(X_3d[:, 0], X_3d[:, 1], X_3d[:, 2],
                         c=X_3d[:, 0], cmap='viridis', alpha=0.6)
    ax1.set_title('Datos Originales 3D')
    ax1.set_xlabel('X1')
    ax1.set_ylabel('X2')
    ax1.set_zlabel('X3')
    
## Subplot 2: Componentes principales en 3D
    ax2 = fig.add_subplot(132, projection='3d')
    ax2.scatter(X_3d[:, 0], X_3d[:, 1], X_3d[:, 2], alpha=0.3)
    
## Dibujar componentes principales
    for length, vector in zip(pca_3d.eigenvalues_, pca_3d.components_.T):
        v = vector * np.sqrt(length) * 3
        ax2.quiver(pca_3d.mean_[0], pca_3d.mean_[1], pca_3d.mean_[2],
                  v[0], v[1], v[2], color='red', linewidth=3)
    
    ax2.set_title('Componentes Principales 3D')
    ax2.set_xlabel('X1')
    ax2.set_ylabel('X2')
    ax2.set_zlabel('X3')
    
## Subplot 3: Proyección 2D
    ax3 = fig.add_subplot(133)
    scatter_2d = ax3.scatter(X_2d[:, 0], X_2d[:, 1], c=X_3d[:, 0], cmap='viridis', alpha=0.6)
    ax3.set_title(f'Proyección PCA 2D\n(Varianza explicada: {np.sum(pca_3d.explained_variance_ratio_):.2%})')
    ax3.set_xlabel('PC1')
    ax3.set_ylabel('PC2')
    ax3.grid(True, alpha=0.3)
    
    plt.colorbar(scatter_2d, ax=ax3, label='Valor X1 original')
    plt.tight_layout()
    plt.show()
    
    print(f"Varianza explicada por cada componente: {pca_3d.explained_variance_ratio_}")
    print(f"Varianza total explicada: {np.sum(pca_3d.explained_variance_ratio_):.2%}")

pca_3d_demo()
```

### 5.8.3 Aplicaciones Avanzadas y Limitaciones

**Reconstrucción de datos con diferentes números de componentes:**

```python
def analisis_reconstruccion_pca():
    """Análisis de calidad de reconstrucción vs número de componentes"""
    from sklearn.datasets import load_digits
    
    digits = load_digits()
    X_digits = digits.data
    y_digits = digits.target
    
    n_components_range = [2, 5, 10, 20, 30, 50, 64]
    mse_values = []
    var_explained = []
    
    for n_comp in n_components_range:
        pca = PCAFromScratch(n_components=n_comp).fit(X_digits)
        X_transformed = pca.transform(X_digits)
        X_reconstructed = pca.inverse_transform(X_transformed)
        
## Error de reconstrucción
        mse = np.mean((X_digits - X_reconstructed) ** 2)
        mse_values.append(mse)
        var_explained.append(np.sum(pca.explained_variance_ratio_))
    
## Gráfico de trade-off
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    ax1.plot(n_components_range, mse_values, 'bo-', linewidth=2)
    ax1.set_xlabel('Número de Componentes')
    ax1.set_ylabel('Error Cuadrático Medio')
    ax1.set_title('Error de Reconstrucción vs Complejidad')
    ax1.grid(True, alpha=0.3)
    
    ax2.plot(n_components_range, var_explained, 'ro-', linewidth=2)
    ax2.set_xlabel('Número de Componentes')
    ax2.set_ylabel('Varianza Explicada')
    ax2.set_title('Varianza Explicada vs Complejidad')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

analisis_reconstruccion_pca()
```

**Limitaciones importantes del PCA:**

1. **Linealidad:** Solo captura relaciones lineales
2. **Varianza vs Información:** Maximiza varianza, no necesariamente información relevante
3. **Sensibilidad a escala:** Requiere estandarización previa
4. **Outliers:** Muy sensible a valores atípicos

**Alternativas no lineales (mencionar brevemente):**
- **t-SNE:** Para visualización de alta dimensión
- **UMAP:** Preserva mejor la estructura global
- **Autoencoders:** PCA no lineal mediante redes neuronales

**5.8.1 Fundamentos Matemáticos Completos**

```python
class PCAFromScratch:
    """Implementación completa de PCA desde primeros principios"""

    def __init__(self, n_components=None):
        self.n_components = n_components

    def fit(self, X):
## Centrado
        self.mean_ = np.mean(X, axis=0)
        X_centered = X - self.mean_

## Matriz de covarianza
        n_samples = X.shape[0]
        self.cov_matrix_ = (X_centered.T @ X_centered) / (n_samples - 1)

## Descomposición espectral
        eigenvals, eigenvecs = np.linalg.eig(self.cov_matrix_)

## Ordenar por eigenvalores descendentes
        idx = np.argsort(eigenvals)[::-1]
        self.eigenvalues_ = eigenvals[idx]
        self.components_ = eigenvecs[:, idx]

## Seleccionar componentes
        if self.n_components is not None:
            self.components_ = self.components_[:, :self.n_components]
            self.eigenvalues_ = self.eigenvalues_[:self.n_components]

## Varianza explicada
        self.explained_variance_ratio_ = self.eigenvalues_ / np.sum(self.eigenvalues_)

        return self

    def transform(self, X):
        X_centered = X - self.mean_
        return X_centered @ self.components_

    def inverse_transform(self, Y):
        return Y @ self.components_.T + self.mean_

## Comparación con scikit-learn
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

## Datos de ejemplo
iris = load_iris()
X = iris.data

## Nuestra implementación
pca_scratch = PCAFromScratch(n_components=2).fit(X)
X_pca_scratch = pca_scratch.transform(X)

## Scikit-learn
pca_sklearn = PCA(n_components=2).fit(X)
X_pca_sklearn = pca_sklearn.transform(X)

print("Varianza explicada (scratch):", pca_scratch.explained_variance_ratio_)
print("Varianza explicada (sklearn):", pca_sklearn.explained_variance_ratio_)
```

**5.8.2 PCA en 2D y 3D - Ejemplos Visuales Completos**

Caso 2D - Rotación de datos correlacionados:

```python
def pca_2d_demo():
    """Demo visual de PCA en 2 dimensiones"""
## Generar datos correlacionados
    np.random.seed(42)
    n_points = 300
    theta = np.random.uniform(0, 2*np.pi, n_points)
    r = np.random.normal(0, 0.3, n_points)

## Elipse rotada
    rotation_angle = np.pi/4
    rotation_matrix = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)],
                              [np.sin(rotation_angle), np.cos(rotation_angle)]])

    X_ellipse = np.column_stack([2*np.cos(theta) + r, 0.5*np.sin(theta) + r])
    X = X_ellipse @ rotation_matrix.T + [1, 2]

## Aplicar PCA
    pca = PCAFromScratch(n_components=2).fit(X)
    X_pca = pca.transform(X)

## Visualización
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

## Datos originales
    axes[0].scatter(X[:, 0], X[:, 1], alpha=0.6)
    axes[0].set_title('Datos Originales')
    axes[0].set_xlabel('X1')
    axes[0].set_ylabel('X2')
    axes[0].grid(True, alpha=0.3)
    axes[0].axis('equal')

## Datos + componentes principales
    axes[1].scatter(X[:, 0], X[:, 1], alpha=0.6)
    for length, vector in zip(pca.eigenvalues_, pca.components_.T):
        v = vector * np.sqrt(length) * 3  # Escalar para visualización
        axes[1].arrow(pca.mean_[0], pca.mean_[1], v[0], v[1],
                     head_width=0.1, head_length=0.1, fc='red', ec='red')
    axes[1].set_title('Componentes Principales')
    axes[1].set_xlabel('X1')
    axes[1].set_ylabel('X2')
    axes[1].grid(True, alpha=0.3)
    axes[1].axis('equal')

## Datos transformados
    axes[2].scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.6)
    axes[2].set_title('Espacio PCA (Decorrelacionado)')
    axes[2].set_xlabel('PC1')
    axes[2].set_ylabel('PC2')
    axes[2].grid(True, alpha=0.3)
    axes[2].axis('equal')

    plt.tight_layout()
    plt.show()

pca_2d_demo()
```

Caso 3D - Reducción a 2D:

```python
def pca_3d_demo():
    """Demo visual de PCA en 3 dimensiones con reducción a 2D"""
## Generar datos 3D correlacionados
    np.random.seed(42)
    n_points = 500

## Tres variables con diferentes correlaciones
    X1 = np.random.normal(0, 2, n_points)
    X2 = 0.7 * X1 + np.random.normal(0, 1, n_points)
    X3 = 0.5 * X1 + 0.3 * X2 + np.random.normal(0, 0.5, n_points)

    X_3d = np.column_stack([X1, X2, X3])

## Aplicar PCA
    pca_3d = PCAFromScratch(n_components=2).fit(X_3d)
    X_2d = pca_3d.transform(X_3d)

## Visualización 3D
    fig = plt.figure(figsize=(15, 5))

## Subplot 1: Datos originales 3D
    ax1 = fig.add_subplot(131, projection='3d')
    scatter = ax1.scatter(X_3d[:, 0], X_3d[:, 1], X_3d[:, 2],
                         c=X_3d[:, 0], cmap='viridis', alpha=0.6)
    ax1.set_title('Datos Originales 3D')
    ax1.set_xlabel('X1')
    ax1.set_ylabel('X2')
    ax1.set_zlabel('X3')

## Subplot 2: Componentes principales en 3D
    ax2 = fig.add_subplot(132, projection='3d')
    ax2.scatter(X_3d[:, 0], X_3d[:, 1], X_3d[:, 2], alpha=0.3)

## Dibujar componentes principales
    for length, vector in zip(pca_3d.eigenvalues_, pca_3d.components_.T):
        v = vector * np.sqrt(length) * 3
        ax2.quiver(pca_3d.mean_[0], pca_3d.mean_[1], pca_3d.mean_[2],
                  v[0], v[1], v[2], color='red', linewidth=3)

    ax2.set_title('Componentes Principales 3D')
    ax2.set_xlabel('X1')
    ax2.set_ylabel('X2')
    ax2.set_zlabel('X3')

## Subplot 3: Proyección 2D
    ax3 = fig.add_subplot(133)
    scatter_2d = ax3.scatter(X_2d[:, 0], X_2d[:, 1], c=X_3d[:, 0], cmap='viridis', alpha=0.6)
    ax3.set_title(f'Proyección PCA 2D\n(Varianza explicada: {np.sum(pca_3d.explained_variance_ratio_):.2%})')
    ax3.set_xlabel('PC1')
    ax3.set_ylabel('PC2')
    ax3.grid(True, alpha=0.3)

    plt.colorbar(scatter_2d, ax=ax3, label='Valor X1 original')
    plt.tight_layout()
    plt.show()

    print(f"Varianza explicada por cada componente: {pca_3d.explained_variance_ratio_}")
    print(f"Varianza total explicada: {np.sum(pca_3d.explained_variance_ratio_):.2%}")

pca_3d_demo()
```

**5.8.3 Aplicaciones Avanzadas y Limitaciones**

Reconstrucción de datos con diferentes números de componentes:

```python
def analisis_reconstruccion_pca():
    """Análisis de calidad de reconstrucción vs número de componentes"""
    from sklearn.datasets import load_digits

    digits = load_digits()
    X_digits = digits.data
    y_digits = digits.target

    n_components_range = [2, 5, 10, 20, 30, 50, 64]
    mse_values = []
    var_explained = []

    for n_comp in n_components_range:
        pca = PCAFromScratch(n_components=n_comp).fit(X_digits)
        X_transformed = pca.transform(X_digits)
        X_reconstructed = pca.inverse_transform(X_transformed)

## Error de reconstrucción
        mse = np.mean((X_digits - X_reconstructed) ** 2)
        mse_values.append(mse)
        var_explained.append(np.sum(pca.explained_variance_ratio_))

## Gráfico de trade-off
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(n_components_range, mse_values, 'bo-', linewidth=2)
    ax1.set_xlabel('Número de Componentes')
    ax1.set_ylabel('Error Cuadrático Medio')
    ax1.set_title('Error de Reconstrucción vs Complejidad')
    ax1.grid(True, alpha=0.3)

    ax2.plot(n_components_range, var_explained, 'ro-', linewidth=2)
    ax2.set_xlabel('Número de Componentes')
    ax2.set_ylabel('Varianza Explicada')
    ax2.set_title('Varianza Explicada vs Complejidad')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

analisis_reconstruccion_pca()
```

---

#PROBABILIDAD Y ESTADÍSTICA

**INGENIERÍA EN NANOTECNOLOGÍA**

**Universidad de La Ciénega del Estado de Michoacán de Ocampo**

*Capítulo 5 secciones 5.3 a 5.8: Distribuciones Conjuntas, Condicionales, Convolución Vectores Aleatorios, Transformaciones Gaussianas y Análisis de Compnentes Principales*

## Resumen Distribuciones y Esperanzas Condicionales

Estas son fundamentales para entender cómo la información de una variable aleatoria afecta a otra.

---

## Capítulo 5: Distribuciones Conjuntas

### 5.3 PMF y PDF Condicionales

Cuando tenemos dos variables aleatorias $X$ e $Y$, las *distribuciones condicionales* nos permiten estudiar la distribución de una variable **dada una observación específica de la otra**.
Este concepto es la base de la inferencia estadística, pues modela la dependencia entre variables.

---

### 5.3.1 PMF Condicional (Conditional PMF)

La *Probabilidad de Masa Condicional (PMF)* se utiliza para variables aleatorias **discretas**.
Se define de manera análoga a la probabilidad condicional simple:

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

#### Definición

Dadas dos variables aleatorias discretas $X$ e $Y$ con PMF conjunta $P_{X,Y}(x, y)$, la PMF de $Y$ dado que $X$ ha tomado el valor $x$ se define como:

$$
P_{Y|X}(y|x) = P(Y=y | X=x) = \frac{P_{X,Y}(x, y)}{P_X(x)}
$$

para todos los valores $x$ donde $P_X(x) > 0$.

#### Propiedades Clave

1. **Suma a 1:**
   Para un valor fijo $x$, la suma sobre todos los posibles valores de $y$ debe ser 1:
   $$
   \sum_{y} P_{Y|X}(y|x) = 1
   $$
2. **Regla de Multiplicación:**
   La PMF conjunta se puede obtener multiplicando la marginal por la condicional:
   $$
   P_{X,Y}(x, y) = P_{Y|X}(y|x) P_X(x)
   $$

#### Ejemplo Práctico (Discreto)

Retomando el ejercicio con **3 bolas rojas (R), 2 azules (A) y 1 verde (V)** en **2 extracciones**, donde $X=$ Rojas y $Y=$ Azules.
Calcularemos la PMF condicional de $Y$ dado que **$X=1$**.

**Datos de la PMF Conjunta y Marginal (corregidos):**

* $P_{X,Y}(1, 0) = 3/15$
* $P_{X,Y}(1, 1) = 6/15$
* $P_{X,Y}(1, 2) = 0$
* $P_X(1) = 9/15$

**Cálculo de $P_{Y|X}(y|1)$:**

1. Para $y=0$:
   $$
   P_{Y|X}(0|1) = \frac{P_{X,Y}(1, 0)}{P_X(1)} = \frac{3/15}{9/15} = \frac{1}{3}
   $$

2. Para $y=1$:
   $$
   P_{Y|X}(1|1) = \frac{P_{X,Y}(1, 1)}{P_X(1)} = \frac{6/15}{9/15} = \frac{2}{3}
   $$

3. Para $y=2$:
   $$
   P_{Y|X}(2|1) = \frac{0}{9/15} = 0
   $$

**Verificación:**
$$
\sum_{y} P_{Y|X}(y|1) = \frac{1}{3} + \frac{2}{3} + 0 = 1
$$

```python
## Código Python para PMF Condicional (Ejemplo)
import numpy as np
from fractions import Fraction

## PMF Conjunta P(x, y)
P_XY = {(0, 0): 0, (0, 1): Fraction(2, 15), (0, 2): Fraction(1, 15),
        (1, 0): Fraction(3, 15), (1, 1): Fraction(6, 15), (1, 2): 0,
        (2, 0): Fraction(3, 15), (2, 1): 0, (2, 2): 0}

## PMF Marginal de X
P_X_1 = Fraction(9, 15)
print(f"PMF Marginal P_X(1) = {P_X_1}")

## Calcular PMF Condicional P(Y | X=1)
print("\nPMF Condicional P(Y | X=1):")
for y in range(3):
    P_Y_cond_X = P_XY[(1, y)] / P_X_1
    print(f"P(Y={y} | X=1) = {P_Y_cond_X}")
```

---

### 5.3.2 PDF Condicional (Conditional PDF)

La *Probabilidad de Densidad Condicional (PDF)* se utiliza para variables aleatorias **continuas**.

#### Definición

Dadas dos variables aleatorias continuas $X$ e $Y$ con PDF conjunta $f_{X,Y}(x, y)$, la PDF de $Y$ dado que $X=x$ se define como:

$$
f_{Y|X}(y|x) = \frac{f_{X,Y}(x, y)}{f_X(x)}
$$

para todos los valores $x$ donde $f_X(x) > 0$.

#### Propiedades Clave

1. **Integración a 1:**
   $$
   \int_{-\infty}^{\infty} f_{Y|X}(y|x),dy = 1
   $$
2. **Regla de Multiplicación:**
   $$
   f_{X,Y}(x, y) = f_{Y|X}(y|x) f_X(x)
   $$
3. **Independencia:**
   Si $X$ e $Y$ son independientes, entonces:
   $$
   f_{Y|X}(y|x) = f_Y(y)
   $$

#### Ejemplo Práctico (Continuo)

Sea $f_{X,Y}(x, y) = x + y$ para $0 \leq x, y \leq 1$.
La marginal calculada fue $f_X(x) = x + \frac{1}{2}$.

Entonces:
$$
f_{Y|X}(y|x) = \frac{x + y}{x + \frac{1}{2}}, \quad 0 \leq x,y \leq 1
$$

**Cálculo de $P(Y < 0.5 | X = 0.5)$:**

$$
f_{Y|X}(y|0.5) = 0.5 + y
$$
$$
P(Y < 0.5 | X = 0.5) = \int_{0}^{0.5} (0.5 + y),dy = 0.375
$$

---

## 5.4 Esperanza Condicional

La **esperanza condicional** $E[Y|X=x]$ es el valor promedio de $Y$ que se espera dada la información de que $X$ ha tomado un valor específico.

#### Definición

**Discreta:**
$$
E[Y|X=x] = \sum_y y \cdot P_{Y|X}(y|x)
$$

**Continua:**
$$
E[Y|X=x] = \int_{-\infty}^{\infty} y \cdot f_{Y|X}(y|x),dy
$$

#### Ejemplo Discreto

Usando el ejemplo anterior:

* $P_{Y|X}(0|1) = 1/3$
* $P_{Y|X}(1|1) = 2/3$

Entonces:
$$
E[Y|X=1] = 0\cdot\frac{1}{3} + 1\cdot\frac{2}{3} = \frac{2}{3}
$$

---

### 5.4.1 Ley de la Esperanza Total (Ley de la Esperanza Iterada)

La **Ley de la Esperanza Total (LET)** indica que:

$$
E[Y] = E[E[Y|X]]
$$

Esto implica que la esperanza incondicional puede calcularse promediando las esperanzas condicionales.

**Discreta:**
$$
E[Y] = \sum_x E[Y|X=x] P_X(x)
$$

**Continua:**
$$
E[Y] = \int_{-\infty}^{\infty} E[Y|X=x] f_X(x),dx
$$

#### Ejemplo

Del ejemplo de las bolas:

$$
E[Y|X=0]=\frac{4}{3}, \quad E[Y|X=1]=\frac{2}{3}, \quad E[Y|X=2]=0
$$

Aplicamos la ley:

$$
E[Y]=\frac{4}{3}\frac{3}{15}+\frac{2}{3}\frac{9}{15}+0\cdot\frac{3}{15}=\frac{2}{3}
$$

---

## 5.5 Suma de Dos Variables Aleatorias: $Z = X + Y$

Cuando se suman dos variables aleatorias, la distribución de $Z$ se obtiene mediante **convolución**.

### 5.5.1 Convolución Discreta

$$
P_Z(z) = \sum_x P_X(x) P_Y(z-x)
$$

### 5.5.2 Convolución Continua

$$
f_Z(z) = \int_{-\infty}^{\infty} f_X(x) f_Y(z-x),dx
$$

---

### 5.5.3 Propiedades de la Suma

**Esperanza:**
$$
E[X+Y] = E[X] + E[Y]
$$

**Varianza general:**
$$
\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2,\text{Cov}(X,Y)
$$

**Si son independientes:**
$$
\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y)
$$

---

### 5.5.4 Suma de Distribuciones Comunes

<table>
  <thead>
    <tr>
      <th style="text-align:center; width:30%;">Distribución de <i>X</i></th>
      <th style="text-align:center; width:30%;">Distribución de <i>Y</i></th>
      <th style="text-align:center; width:40%;">Distribución de la suma <i>Z = X + Y</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:center;">$\text{Binomial}(n_1, p)$</td>
      <td style="text-align:center;">$\text{Binomial}(n_2, p)$</td>
      <td style="text-align:center;">$\text{Binomial}(n_1 + n_2, p)$</td>
    </tr>
    <tr>
      <td style="text-align:center;">$\text{Poisson}(\lambda_1)$</td>
      <td style="text-align:center;">$\text{Poisson}(\lambda_2)$</td>
      <td style="text-align:center;">$\text{Poisson}(\lambda_1 + \lambda_2)$</td>
    </tr>
    <tr>
      <td style="text-align:center;">$\text{Normal}(\mu_1, \sigma_1^2)$</td>
      <td style="text-align:center;">$\text{Normal}(\mu_2, \sigma_2^2)$</td>
      <td style="text-align:center;">$\text{Normal}(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$</td>
    </tr>
    <tr>
      <td style="text-align:center;">$\text{Gamma}(\alpha_1, \theta)$</td>
      <td style="text-align:center;">$\text{Gamma}(\alpha_2, \theta)$</td>
      <td style="text-align:center;">$\text{Gamma}(\alpha_1 + \alpha_2, \theta)$</td>
    </tr>
  </tbody>
</table>

<p style="text-align:center;"><em>Estas relaciones son válidas únicamente si las variables aleatorias</em> $X$ <em>e</em> $Y$ <em>son independientes.</em></p>

---

**Observaciones finales:**

* La suma de normales independientes **siempre es normal**, fundamento del Teorema del Límite Central.
* La suma de uniformes **no es uniforme** (produce una distribución triangular).
* Estas propiedades de “cierre” se cumplen **solo si las variables son independientes**.

---

```python
## Código Python para PMF Condicional (Ejemplo)
import numpy as np
from fractions import Fraction

## PMF Conjunta P(x, y)
P_XY = {(0, 0): 0, (0, 1): Fraction(2, 15), (0, 2): Fraction(1, 15),
        (1, 0): Fraction(3, 15), (1, 1): Fraction(6, 15), (1, 2): 0,
        (2, 0): Fraction(3, 15), (2, 1): 0, (2, 2): 0}

## PMF Marginal de X
P_X_1 = Fraction(9, 15)
print(f"PMF Marginal P_X(1) = {P_X_1}")

## Calcular PMF Condicional P(Y | X=1)
print("\nPMF Condicional P(Y | X=1):")
for y in range(3):
    P_Y_cond_X = P_XY[(1, y)] / P_X_1
    print(f"P(Y={y} | X=1) = {P_Y_cond_X}")
```

## 5.3 PMF y PDF Condicionales (extensión completa)

### Introducción ampliada (qué, por qué y cuándo)

Cuando trabajamos con dos variables aleatorias $X$ e $Y$, a menudo queremos describir la distribución de una **condicionada** a la observación de la otra. Esto es central en inferencia (p. ej. actualización de creencias), en modelos de regresión y en procesos estocásticos que evolucionan con información parcial.

* **¿Qué?** La distribución condicional $P_{Y|X=x}$ o $f_{Y|X}(y|x)$ describe la probabilidad/densidad de $Y$ cuando sabemos que $X$ vale $x$.
* **¿Para qué?** Para actualizar predicciones, calcular esperanzas condicionadas, construir estimadores condicionales (regresión) y calcular probabilidades compuestas.
* **¿Cuándo?** Siempre que haya dependencia entre variables o cuando queremos explotar información disponible sobre alguna variable para mejorar la predicción de otra.

---

## 5.3.1 PMF Condicional (variables discretas)

### Definición formal

Para variables discretas $X,Y$ con PMF conjunta $P_{X,Y}(x,y)$ y marginal $P_X(x)>0$:

$$
\displaystyle P_{Y|X}(y|x) ;=; \frac{P_{X,Y}(x,y)}{P_X(x)}.
$$

Es la aplicación directa de la probabilidad condicional clásica a variables aleatorias.

### Propiedades fundamentales (recordatorio ampliado)

1. **No-negatividad:** $P_{Y|X}(y|x)\ge0$.
2. **Normalización (para $x$ fijo):** $\displaystyle\sum_y P_{Y|X}(y|x)=1$.
3. **Reconstrucción de la conjunta:** $\displaystyle P_{X,Y}(x,y)=P_X(x)P_{Y|X}(y|x)$.
4. **Si $X$ e $Y$ son independientes:** $P_{Y|X}(y|x)=P_Y(y)$ (no depende de $x$).

---

### Ejemplo completo (analítico + código): urna con 3R,2A,1V — 2 extracciones sin reemplazo

**Planteamiento:** Urna con 6 bolas: 3 rojas (R), 2 azules (A), 1 verde (V). Se extraen 2 sin reemplazo.
Definimos:

* $X =$ número de rojas extraídas ($x\in{0,1,2}$)
* $Y =$ número de azules extraídas ($y\in{0,1,2}$)
  (Nótese que $X+Y\le2$ y algunas combinaciones son imposibles.)

**Paso 1 — Calcular PMF conjunta** (combinatoria)
Para dar un par $(x,y)$ compatible con $x+y \le 2$, el número de formas es:
$$
\binom{3}{x}\binom{2}{y}\binom{1}{2-x-y}
$$
dividido entre $\binom{6}{2}=15$.

Los valores relevantes (resumidos) son:

* $P_{X,Y}(1,0)=3/15$
* $P_{X,Y}(1,1)=6/15$
* $P_{X,Y}(1,2)=0$
* y así sucesivamente (se puede construir la tabla completa).

**Paso 2 — Marginal de $X$**:
$$P_X(1)=\sum_y P_{X,Y}(1,y)=\frac{3}{15}+\frac{6}{15}+0=\frac{9}{15}.$$

**Paso 3 — PMF condicional $P_{Y|X}(y|1)$**:
$$
P_{Y|X}(y|1)=\frac{P_{X,Y}(1,y)}{P_X(1)}.
$$

Cálculos explícitos:

* $P_{Y|X}(0|1)=\frac{3/15}{9/15}=\frac{1}{3}$.
* $P_{Y|X}(1|1)=\frac{6/15}{9/15}=\frac{2}{3}$.
* $P_{Y|X}(2|1)=0$.

**Verificación suma a 1:** $1/3 + 2/3 + 0 = 1$.

---

#### Código Python (comprobación exacta con `fractions` y simulación con `numpy`)

```python
## Código de comprobación en Colab
from fractions import Fraction
import numpy as np
from collections import Counter

## PMF conjunta (fracciones exactas)
P_XY = {
    (0,0): Fraction(0,15), (0,1): Fraction(2,15), (0,2): Fraction(1,15),
    (1,0): Fraction(3,15), (1,1): Fraction(6,15), (1,2): Fraction(0,15),
    (2,0): Fraction(3,15), (2,1): Fraction(0,15), (2,2): Fraction(0,15)
}

## Marginal P_X(1)
P_X_1 = sum(P for (x,y),P in P_XY.items() if x==1)
print("P_X(1) =", P_X_1)  # Esperado: 9/15

## PMF condicional exacta
print("P(Y|X=1):")
for y in [0,1,2]:
    val = P_XY[(1,y)] / P_X_1
    print(f" y={y}: {val} = {float(val):.6f}")

## Simulación para validar (aprox.)
urn = [ 'R' ]*3 + [ 'A' ]*2 + [ 'V' ]*1
N = 200000
counts = Counter()
for _ in range(N):
    draw = np.random.choice(urn, size=2, replace=False)
    x = sum(1 for b in draw if b=='R')
    y = sum(1 for b in draw if b=='A')
    counts[(x,y)] += 1

print("\nFrecuencias simuladas (normalizadas) para (1,0) y (1,1):")
print("P_sim(1,0) = ", counts[(1,0)]/N)
print("P_sim(1,1) = ", counts[(1,1)]/N)
print("P_sim(Y|X=1) estimada (condicional) =")
## condicional simulada: P(Y=y | X=1) = P_sim(1,y) / sum_y P_sim(1,y)
total_X1 = sum(counts[(1,y)] for y in [0,1,2])
for y in [0,1,2]:
    print(f" y={y}: {counts[(1,y)]/total_X1:.6f}")
```

**Explicación del código:**

* Se usa `Fraction` para operar con exactitud racional y evitar errores de punto flotante en las fracciones teóricas.
* Se incluye una simulación (Monte Carlo) para validar que las probabilidades teóricas coinciden con la estimación empírica al aumentar N.

---

### Interpretación práctica

* Con la información *X=1* (una roja ya extraída), la distribución de azules se concentra en $y=0$ y $y=1$, con probabilidades 1/3 y 2/3: saber que extrajimos una roja reduce el espacio de resultados permitidos para $Y$ y repondera sus probabilidades.

---

## 5.3.2 PDF Condicional (variables continuas) — explicación extendida

### Contexto y observaciones

Para variables continuas, los eventos puntuales tienen probabilidad cero, pero las densidades condicionadas son herramientas válidas para describir cómo la masa de probabilidad "se reparte" sobre $y$ cuando $x$ está fijado. La PDF condicional se usa tanto para calcular probabilidades condicionales (integrando la densidad sobre un intervalo) como para calcular esperanzas condicionales.

### Definición formal

Si $f_{X,Y}(x,y)$ es la densidad conjunta y $f_X(x)>0$ la marginal:

$$
\displaystyle f_{Y|X}(y|x) = \frac{f_{X,Y}(x,y)}{f_X(x)},\qquad f_X(x)=\int_{-\infty}^{\infty} f_{X,Y}(x,y),dy.
$$

### Propiedades

1. **Normalización en $y$ para $x$ fijo:** $\displaystyle \int_{-\infty}^{\infty} f_{Y|X}(y|x),dy = 1$.
2. **Reconstrucción:** $f_{X,Y}(x,y)=f_X(x)f_{Y|X}(y|x)$.
3. **Independencia:** Si $f_{X,Y}(x,y)=f_X(x)f_Y(y)$, entonces $f_{Y|X}(y|x)=f_Y(y)$.

---

### Ejemplo completo (analítico + código): $f_{X,Y}(x,y)=x+y$ en $[0,1]^2$

**Enunciado:** Sea $f_{X,Y}(x,y)=x+y$ para $0\le x,y\le1$ y cero fuera. Calcular la marginal $f_X(x)$, la condicional $f_{Y|X}(y|x)$, y la probabilidad condicional $P(Y<0.5 | X=0.5)$.

**Paso A — Marginal de $X$**:
$$
f_X(x)=\int_0^1 (x+y),dy = x\cdot 1 + \frac{1}{2}= x + \frac{1}{2}, \quad 0\le x\le1.
$$

**Paso B — PDF condicional**:
$$
f_{Y|X}(y|x)=\frac{x+y}{x+\tfrac12},\qquad 0\le y\le1,; 0\le x\le1.
$$

**Verificación de normalización (analítica):**
Para un $x$ fijo,
[
\int_0^1 \frac{x+y}{x+\tfrac12},dy
= \frac{1}{x+\tfrac12}\left[ x y + \frac{y^2}{2} \right]_0^1
= \frac{x + \tfrac12}{x+\tfrac12} = 1.
]

**Paso C — Probabilidad condicional $P(Y<0.5 | X=0.5)$:**
Sustituir $x=0.5$:
$$
f_{Y|X}(y|0.5) = \frac{0.5 + y}{0.5 + 0.5} = 0.5 + y, \quad 0\le y\le1.
$$
Integrar:
$$
P(Y<0.5|X=0.5) = \int_0^{0.5} (0.5 + y),dy
= \left[0.5y + \frac{y^2}{2}\right]_0^{0.5}
= 0.25 + 0.125 = 0.375.
$$

---

#### Código Python (analítico simbólico con `sympy` y numérico con `scipy`)

```python
## Código para Colab: cálculo simbólico y numérico
import sympy as sp
from scipy.integrate import quad

## Símbolos
x, y = sp.symbols('x y')

## Definición simbólica
f_xy = x + y  # válido en [0,1]^2

## Marginal f_X(x) simbólico (integral en y de 0 a 1)
fX_sym = sp.integrate(f_xy, (y, 0, 1))
sp.simplify(fX_sym)  # resultado: x + 1/2

## PDF condicional simbólica
fY_given_X = (f_xy) / fX_sym
sp.simplify(fY_given_X)  # (x+y)/(x+1/2)

## Evaluar P(Y < 0.5 | X = 0.5) numéricamente
f_cond_numeric = lambda Y: 0.5 + Y  # derivado de sustituir x = 0.5
prob, _ = quad(f_cond_numeric, 0, 0.5)
print("P(Y < 0.5 | X = 0.5) =", prob)
```

**Explicación del código:**

* `sympy` se usa para mostrar derivaciones simbólicas limpias (marginal y forma condicional).
* `scipy.integrate.quad` se usa para la integral numérica (rápida y precisa).

---

```python
## Código de comprobación en Colab
from fractions import Fraction
import numpy as np
from collections import Counter

## PMF conjunta (fracciones exactas)
P_XY = {
    (0,0): Fraction(0,15), (0,1): Fraction(2,15), (0,2): Fraction(1,15),
    (1,0): Fraction(3,15), (1,1): Fraction(6,15), (1,2): Fraction(0,15),
    (2,0): Fraction(3,15), (2,1): Fraction(0,15), (2,2): Fraction(0,15)
}

## Marginal P_X(1)
P_X_1 = sum(P for (x,y),P in P_XY.items() if x==1)
print("P_X(1) =", P_X_1)  # Esperado: 9/15

## PMF condicional exacta
print("P(Y|X=1):")
for y in [0,1,2]:
    val = P_XY[(1,y)] / P_X_1
    print(f" y={y}: {val} = {float(val):.6f}")

## Simulación para validar (aprox.)
urn = [ 'R' ]*3 + [ 'A' ]*2 + [ 'V' ]*1
N = 200000
counts = Counter()
for _ in range(N):
    draw = np.random.choice(urn, size=2, replace=False)
    x = sum(1 for b in draw if b=='R')
    y = sum(1 for b in draw if b=='A')
    counts[(x,y)] += 1

print("\nFrecuencias simuladas (normalizadas) para (1,0) y (1,1):")
print("P_sim(1,0) = ", counts[(1,0)]/N)
print("P_sim(1,1) = ", counts[(1,1)]/N)
print("P_sim(Y|X=1) estimada (condicional) =")
## condicional simulada: P(Y=y | X=1) = P_sim(1,y) / sum_y P_sim(1,y)
total_X1 = sum(counts[(1,y)] for y in [0,1,2])
for y in [0,1,2]:
    print(f" y={y}: {counts[(1,y)]/total_X1:.6f}")
```

```python
## Código para Colab: cálculo simbólico y numérico
import sympy as sp
from scipy.integrate import quad

## Símbolos
x, y = sp.symbols('x y')

## Definición simbólica
f_xy = x + y  # válido en [0,1]^2

## Marginal f_X(x) simbólico (integral en y de 0 a 1)
fX_sym = sp.integrate(f_xy, (y, 0, 1))
sp.simplify(fX_sym)  # resultado: x + 1/2

## PDF condicional simbólica
fY_given_X = (f_xy) / fX_sym
sp.simplify(fY_given_X)  # (x+y)/(x+1/2)

## Evaluar P(Y < 0.5 | X = 0.5) numéricamente
f_cond_numeric = lambda Y: 0.5 + Y  # derivado de sustituir x = 0.5
prob, _ = quad(f_cond_numeric, 0, 0.5)
print("P(Y < 0.5 | X = 0.5) =", prob)
```

## 5.4 Esperanza Condicional — desarrollo ampliado

### Intuición y utilidad profunda

La esperanza condicional $E[Y|X=x]$ resume en un solo número la distribución condicional de $Y$ cuando $X$ es conocido. Es la **regresión poblacional**: la función $g(x)=E[Y|X=x]$ es la curva de regresión (verdadera) que minimiza el error cuadrático medio (MSE) entre $Y$ y cualquier predictor medible en función de $X$.

**Propiedad optimizadora:** si buscamos $\hat{g}(X)$ que minimice $\mathbb{E}[(Y - \hat{g}(X))^2]$, la solución es $\hat{g}(X) = E[Y|X]$.

---

### Definición formal (recordatorio)

* **Discreta:**
  $$
  E[Y|X=x] = \sum_y y,P_{Y|X}(y|x).
  $$
* **Continua:**
  $$
  E[Y|X=x] = \int_{-\infty}^{\infty} y,f_{Y|X}(y|x),dy.
  $$

### Propiedades importantes

1. **Linealidad en $Y$:** $E[aY + b \mid X] = a E[Y|X] + b$.
2. **Iteración (Ley de la Esperanza Total):** $E[Y] = E[E[Y|X]]$.
3. **Si $X$ e $Y$ independientes:** $E[Y|X] = E[Y]$ (constante).

---

### Ejemplo completo (discreto): Esperanza condicional y Ley de la Expectativa Total (Urna)

Reusamos los resultados previos del ejemplo de la urna.

**Condicionales ya calculadas (resumen):**

* $E[Y|X=0] = 4/3$ (esto se obtiene al calcular la distribución condicional $P_{Y|X}(y|0)$ y aplicar la suma).
* $E[Y|X=1] = 2/3$.
* $E[Y|X=2] = 0$.

**Marginales de $X$:**

* $P_X(0)=3/15$, $P_X(1)=9/15$, $P_X(2)=3/15$.

**Aplicación de LET:**
$$
E[Y] = \sum_{x} E[Y|X=x] P_X(x)
= \frac{4}{3}\cdot\frac{3}{15} + \frac{2}{3}\cdot\frac{9}{15} + 0\cdot\frac{3}{15}
= \frac{4}{15} + \frac{6}{15} = \frac{10}{15} = \frac{2}{3}.
$$

**Interpretación:** la esperanza incondicional que obtuvimos (2/3) coincide con el promedio ponderado de las esperanzas condicionales, tal como establece la LET.

---

#### Código Python: cálculo de $E[Y|X=x]$ y verificación de LET (exacto y por simulación)

```python
## Cálculo de E[Y|X=x] exacto usando Fracciones y verificación de LET
from fractions import Fraction
import numpy as np

## PMF conjunta (fracciones)
P_XY = {
    (0,0): Fraction(0,15), (0,1): Fraction(2,15), (0,2): Fraction(1,15),
    (1,0): Fraction(3,15), (1,1): Fraction(6,15), (1,2): Fraction(0,15),
    (2,0): Fraction(3,15), (2,1): Fraction(0,15), (2,2): Fraction(0,15)
}

## Marginal P_X
P_X = {x: sum(P for (xx,yy),P in P_XY.items() if xx==x) for x in [0,1,2]}

## E[Y | X=x] exacto
E_Y_given_X = {}
for x in [0,1,2]:
## sumar y * P_{Y|X}(y|x) = sum_y y * P(x,y) / P_X(x)
    if P_X[x] == 0:
        E_Y_given_X[x] = None
    else:
        E_Y_given_X[x] = sum(Fraction(y,1) * P_XY[(x,y)] for y in [0,1,2]) / P_X[x]

print("P_X:", P_X)
print("E[Y | X=x]:", E_Y_given_X)

## Verificación Ley de la Expectativa Total
E_Y = sum(E_Y_given_X[x] * P_X[x] for x in [0,1,2])
print("E[Y] (por LET) =", E_Y, " = ", float(E_Y))
```

**Salida esperada (fracciones):**

* $P_X = {0:3/15, 1:9/15, 2:3/15}$
* $E[Y|X=0]=4/3$, $E[Y|X=1]=2/3$, $E[Y|X=2]=0$
* $E[Y]$ por LET = $2/3$.

---

### Comentarios finales sobre 5.4

* En problemas reales, $E[Y|X]$ puede no ser una simple función algebraica; con frecuencia se estima por métodos no paramétricos (kernel regression) o paramétricos (regresión lineal, GLM).
* La LET es extremadamente útil cuando la marginal $f_Y$ es difícil de obtener pero las condicionales $f_{Y|X}$ o $P_{Y|X}$ son manejables.

```python
## Cálculo de E[Y|X=x] exacto usando Fracciones y verificación de LET
from fractions import Fraction
import numpy as np

## PMF conjunta (fracciones)
P_XY = {
    (0,0): Fraction(0,15), (0,1): Fraction(2,15), (0,2): Fraction(1,15),
    (1,0): Fraction(3,15), (1,1): Fraction(6,15), (1,2): Fraction(0,15),
    (2,0): Fraction(3,15), (2,1): Fraction(0,15), (2,2): Fraction(0,15)
}

## Marginal P_X
P_X = {x: sum(P for (xx,yy),P in P_XY.items() if xx==x) for x in [0,1,2]}

## E[Y | X=x] exacto
E_Y_given_X = {}
for x in [0,1,2]:
## sumar y * P_{Y|X}(y|x) = sum_y y * P(x,y) / P_X(x)
    if P_X[x] == 0:
        E_Y_given_X[x] = None
    else:
        E_Y_given_X[x] = sum(Fraction(y,1) * P_XY[(x,y)] for y in [0,1,2]) / P_X[x]

print("P_X:", P_X)
print("E[Y | X=x]:", E_Y_given_X)

## Verificación Ley de la Expectativa Total
E_Y = sum(E_Y_given_X[x] * P_X[x] for x in [0,1,2])
print("E[Y] (por LET) =", E_Y, " = ", float(E_Y))
```

## 5.5 Suma de Dos Variables Aleatorias — Convolución (Parte B extendida)

## 5.5 Introducción y motivación

Sea $Z=X+Y$. Conocer la distribución de $Z$ es fundamental en muchas aplicaciones: tiempo total de servicio, suma de errores, agregación de retornos, combinación de señales, y muchas más. La herramienta matemática que permite construir la distribución de la suma a partir de las distribuciones individuales es la **convolución**.

---

## 5.5.1 Definición (discreta y continua)

**Discreta (si $X,Y$ independientes):**

$$
\displaystyle P_Z(z)=P(X+Y=z)=\sum_{x} P_X(x)\,P_Y(z-x).
$$

**Continua (si $X,Y$ independientes):**

$$
\displaystyle f_Z(z)=\int_{-\infty}^{\infty} f_X(x)\,f_Y(z-x)\,dx.
$$

En ambos casos la convolución suma la contribución de todas las parejas $(x,y)$ tales que $x+y=z$.

---

## 5.5.2 Intuición geométrica y mecánica

* **Geometría (continua):** piensa en $f_X(x)$ como una “forma” sobre el eje $x$. Para obtener $f_Z(z)$ tomas la función $f_Y$, la inviertes y la desplazas (o equivalente: la deslizas sobre $f_X$), multiplicas punto a punto y luego integras, obteniendo el área de superposición.  
* **Intuición (discreta):** para cada posible $x$ que $X$ puede tomar, la probabilidad de que $Z=z$ y $X=x$ es $P_X(x)P_Y(z-x)$; sumas sobre todos esos $x$.

---

## 5.5.3 Propiedades fundamentales

1. **Conmutatividad:** $f_X * f_Y = f_Y * f_X$  
2. **Asociatividad:** $(f_X * f_Y) * f_W = f_X * (f_Y * f_W)$  
3. **Linealidad:** $a(f*g)+b(f*h)=(af+bh)*g$ (con precauciones)  
4. **Normalización:** Si $f_X,f_Y$ son densidades, $f_X * f_Y$ está normalizada  
5. **Transformadas:** $\mathcal{F}\{f*g\} = \mathcal{F}\{f\}\cdot\mathcal{F}\{g\}$ (las transformadas de Fourier o MGFs convierten convoluciones en productos)  
6. **Momentos:** $E[X+Y]=E[X]+E[Y]$, y $\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)+2\mathrm{Cov}(X,Y)$.  
   Si son independientes, $\mathrm{Cov}=0$ y las varianzas se suman.

---

## 5.5.4 Ejemplos analíticos completos

### Ejemplo A — Discreto: Suma de dos dados justos ($1,\ldots,6$)

**Enunciado:** $X$ y $Y$ son dos dados justos independientes con $P_X(k)=1/6$ para $k=1,\dots,6$. Calcular $P_Z(z)$ para $Z=X+Y$.

**Solución analítica (paso a paso):**

Para $z\in\{2,\dots,12\}$:

$$
P_Z(z)=\sum_{x=1}^{6} P_X(x)P_Y(z-x)=\sum_{x=1}^{6} \frac{1}{6}\cdot \frac{1}{6}\,\mathbf{1}_{1\le z-x\le6}.
$$

El número de pares $(x,y)$ con $x+y=z$ es:

* para $z=2$: 1 par $(1,1)$ → $1/36$  
* $z=3$: 2 pares → $2/36$  
* ...  
* $z=7$: 6 pares → $6/36$  
* luego decrece simétricamente hasta $z=12$: 1 par → $1/36$  

Se obtiene la distribución triangular clásica.

**Código NumPy / visualización:**

```python
import numpy as np
import matplotlib.pyplot as plt

p = np.ones(6)/6  # pmf de un dado
## convolución discreta (modo 'full')
pz = np.convolve(p, p)
z_vals = np.arange(2, 13)
print("P(Z=z) para z=2..12:", np.round(pz, 4))

plt.stem(z_vals, pz, basefmt=" ")
plt.xlabel("z")
plt.ylabel("P(Z=z)")
plt.title("PMF de la suma de dos dados justos")
plt.grid(True)
plt.show()
````

---

### Ejemplo B — Discreto: Suma de Binomiales (demostración combinatoria)

**Enunciado:** Si $X\sim \mathrm{Binomial}(n_1,p)$ y $Y\sim \mathrm{Binomial}(n_2,p)$ independientes, demostrar que $Z=X+Y\sim\mathrm{Binomial}(n_1+n_2,p)$.

**Demostración (combinatoria simple):**

Interpreta $X$ como número de éxitos en un conjunto $A$ de $n_1$ ensayos independientes con probabilidad $p$, e $Y$ como número de éxitos en un conjunto $B$ de $n_2$ ensayos disjuntos. Entonces la unión $A\cup B$ contiene $n_1+n_2$ ensayos independientes con probabilidad $p$; el número total de éxitos en la unión es $X+Y$. Por la definición binomial:

$$
P(Z=k) = \binom{n_1+n_2}{k} p^k(1-p)^{n_1+n_2-k}.
$$

Formalmente se puede deducir por convolución:

$$
P_Z(k)=\sum_{i=0}^k \binom{n_1}{i}p^i(1-p)^{n_1-i}\cdot \binom{n_2}{k-i}p^{k-i}(1-p)^{n_2-(k-i)}.
$$

Factorizando $p^k(1-p)^{n_1+n_2-k}$ y usando la identidad de Vandermonde para binomios:

$$
\sum_{i=0}^k \binom{n_1}{i}\binom{n_2}{k-i} = \binom{n_1+n_2}{k},
$$

se obtiene el resultado.

**Código (verificación numérica con NumPy):**

```python
import numpy as np
from scipy.stats import binom

n1, n2, p = 5, 3, 0.4
x = np.arange(0, n1+1)
y = np.arange(0, n2+1)
pmf_x = binom.pmf(x, n1, p)
pmf_y = binom.pmf(y, n2, p)

pmf_z = np.convolve(pmf_x, pmf_y)
k = np.arange(0, n1+n2+1)
pmf_z_binom = binom.pmf(k, n1+n2, p)

np.testing.assert_allclose(pmf_z, pmf_z_binom, atol=1e-12)
print("Convolución coincide con Binomial(n1+n2,p).")
```

---

### Ejemplo C — Discreto: Suma de Poissons (prueba vía PGF / MGF)

**Enunciado:** Si $X\sim \mathrm{Poisson}(\lambda_1)$ y $Y\sim \mathrm{Poisson}(\lambda_2)$ independientes, entonces $Z=X+Y\sim\mathrm{Poisson}(\lambda_1+\lambda_2)$.

**Demostración (usando MGFs o PGFs):**

La función generadora de probabilidad (PGF) de Poisson es:

$$
G_X(s)=\mathbb{E}[s^X]=\exp(\lambda_1(s-1)), \quad G_Y(s)=\exp(\lambda_2(s-1)).
$$

Para la suma de independientes:

$$
G_Z(s)=G_X(s)G_Y(s)=\exp((\lambda_1+\lambda_2)(s-1)),
$$

que es la PGF de $\mathrm{Poisson}(\lambda_1+\lambda_2)$. Por unicidad, la distribución es Poisson con parámetro $\lambda_1+\lambda_2$.

**Código (verificación numérica):**

```python
import numpy as np
from scipy.stats import poisson

lam1, lam2 = 2.5, 1.7
kmax = 20
pmf_x = poisson.pmf(np.arange(kmax+1), lam1)
pmf_y = poisson.pmf(np.arange(kmax+1), lam2)
pmf_z_conv = np.convolve(pmf_x, pmf_y)[:kmax+1]
pmf_z_exact = poisson.pmf(np.arange(kmax+1), lam1+lam2)

print("Max diff approx:", np.max(np.abs(pmf_z_conv - pmf_z_exact)))
```

---

### Ejemplo D — Continua: Convolución de dos Uniformes $U[0,1]$ (triangular)

**Enunciado y objetivo:** Sea $X,Y\sim U[0,1]$ independientes. Calcular $f_Z(z)$ para $Z=X+Y$.

**Solución analítica (integral):**

$$
f_Z(z) = \int_{-\infty}^{\infty} f_X(x) f_Y(z-x),dx
= \int_{0}^{1} 1\cdot \mathbf{1}_{0\le z-x\le1},dx.
$$

El intervalo de integración efectivo es $x\in[\max(0,z-1),\min(1,z)]$.
Por tanto:

$$
f_Z(z) = z \quad \text{para } 0 \le z \le 1
$$
$$
f_Z(z) = 2-z \quad \text{para } 1 < z \le 2
$$
$$
f_Z(z) = 0 \quad \text{en otro caso}
$$

Con lo que $f_Z$ es la distribución triangular clásica en $[0,2]$.

**Demostración simbólica con SymPy:**

```python
import sympy as sp
x, z = sp.symbols('x z', real=True)
fZ = sp.integrate(1, (x, sp.Max(0, z-1), sp.Min(1, z)))
sp.simplify(fZ)
```

**Código Numérico (convolución FFT y comparación):**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve

N = 1000
x = np.linspace(0, 1, N)
dx = x[1]-x[0]
fX = np.ones_like(x)
fY = np.ones_like(x)
fZ_num = fftconvolve(fX, fY) * dx
z = np.linspace(0, 2, len(fZ_num))
fZ_theo = np.where(z<=1, z, 2-z)
fZ_theo = np.where((z<0)|(z>2), 0, fZ_theo)

plt.plot(z, fZ_num, label='numérica (fft conv)')
plt.plot(z, fZ_theo, '--', label='teórica')
plt.legend()
plt.xlabel('z'); plt.ylabel('f_Z(z)')
plt.title('Convolución Uniformes[0,1]')
plt.show()
```

---

### Ejemplo E — Continua: Suma de Normales

**Enunciado:** Si $X\sim N(\mu_1,\sigma_1^2)$ y $Y\sim N(\mu_2,\sigma_2^2)$ independientes, entonces $Z=X+Y\sim N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$.

**Demostración (función característica):**

$$
\phi_X(t)=\exp\big(i\mu_1 t - \tfrac12 \sigma_1^2 t^2\big),\quad
\phi_Y(t)=\exp\big(i\mu_2 t - \tfrac12 \sigma_2^2 t^2\big).
$$

Para suma de independientes:

$$
\phi_Z(t)=\phi_X(t)\phi_Y(t)=\exp\big(i(\mu_1+\mu_2)t - \tfrac12(\sigma_1^2+\sigma_2^2)t^2\big),
$$

que corresponde a una $N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$.

**Código Numérico:**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.signal import fftconvolve

x = np.linspace(-10, 10, 10000)
dx = x[1]-x[0]
fX = norm.pdf(x, loc=1.0, scale=2.0)
fY = norm.pdf(x, loc=-0.5, scale=1.5)
fZ_num = fftconvolve(fX, fY) * dx
z = np.linspace(2*x[0], 2*x[-1], len(fZ_num))
mu = 1.0 + (-0.5)
sigma = np.sqrt(2.0**2 + 1.5**2)
fZ_theo = norm.pdf(z, loc=mu, scale=sigma)

plt.plot(z, fZ_num, label='numérica (conv)')
plt.plot(z, fZ_theo, '--', label='teórica')
plt.legend(); plt.xlim(-5,7)
plt.show()
```

---

## 5.5.6 Tabla 5.5.4 — Suma de distribuciones comunes

<table style="border-collapse:collapse; width:100%; text-align:center; font-family:'Times New Roman',serif; font-size:15px;">
  <thead style="background-color:#f2f2f2;">
    <tr>
      <th style="border:1px solid #ccc; padding:8px; width:20%;">Distribución de <i>X</i></th>
      <th style="border:1px solid #ccc; padding:8px; width:20%;">Distribución de <i>Y</i></th>
      <th style="border:1px solid #ccc; padding:8px; width:40%;">Distribución de <i>Z = X + Y</i></th>
      <th style="border:1px solid #ccc; padding:8px; width:20%;">Demostración rápida / nota</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Binomial}(n_1,p)$</td>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Binomial}(n_2,p)$</td>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Binomial}(n_1+n_2,p)$</td>
      <td style="border:1px solid #ccc; text-align:left; padding:6px;">
        Identidad de Vandermonde aplicada a la convolución de PMFs; interpretación como unión de ensayos independientes.
      </td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Poisson}(\lambda_1)$</td>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Poisson}(\lambda_2)$</td>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Poisson}(\lambda_1+\lambda_2)$</td>
      <td style="border:1px solid #ccc; text-align:left; padding:6px;">
        Uso de PGF o MGF: el producto de PGFs da la PGF de Poisson con parámetro $\lambda_1+\lambda_2$.
      </td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Normal}(\mu_1,\sigma_1^2)$</td>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Normal}(\mu_2,\sigma_2^2)$</td>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Normal}(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$</td>
      <td style="border:1px solid #ccc; text-align:left; padding:6px;">
        Derivado mediante transformada característica o completando cuadrados en la integral de convolución.
      </td>
    </tr>
    <tr>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Gamma}(\alpha_1,\theta)$</td>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Gamma}(\alpha_2,\theta)$</td>
      <td style="border:1px solid #ccc; padding:6px;">$\mathrm{Gamma}(\alpha_1+\alpha_2,\theta)$</td>
      <td style="border:1px solid #ccc; text-align:left; padding:6px;">
        Convolución de densidades Gamma con mismo <em>scale</em>; identidad por propiedades de la función Gamma.
      </td>
    </tr>
  </tbody>
</table>

---

### Código de referencia consolidado

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve, convolve
from scipy.stats import norm, poisson, binom
import sympy as sp
from scipy.integrate import quad
```

```python
import numpy as np
import matplotlib.pyplot as plt

p = np.ones(6)/6  # pmf de un dado
## convolución discreta (modo 'full')
pz = np.convolve(p, p)
z_vals = np.arange(2, 13)
print("P(Z=z) para z=2..12:", np.round(pz, 4))

plt.stem(z_vals, pz, basefmt=" ")
plt.xlabel("z")
plt.ylabel("P(Z=z)")
plt.title("PMF de la suma de dos dados justos")
plt.grid(True)
plt.show()
```

```python
import numpy as np
from scipy.stats import binom

n1, n2, p = 5, 3, 0.4
x = np.arange(0, n1+1)
y = np.arange(0, n2+1)
pmf_x = binom.pmf(x, n1, p)
pmf_y = binom.pmf(y, n2, p)

pmf_z = np.convolve(pmf_x, pmf_y)
k = np.arange(0, n1+n2+1)
pmf_z_binom = binom.pmf(k, n1+n2, p)

np.testing.assert_allclose(pmf_z, pmf_z_binom, atol=1e-12)
print("Convolución coincide con Binomial(n1+n2,p).")
```

```python
import numpy as np
from scipy.stats import poisson

lam1, lam2 = 2.5, 1.7
kmax = 20
pmf_x = poisson.pmf(np.arange(kmax+1), lam1)
pmf_y = poisson.pmf(np.arange(kmax+1), lam2)
pmf_z_conv = np.convolve(pmf_x, pmf_y)[:kmax+1]
pmf_z_exact = poisson.pmf(np.arange(kmax+1), lam1+lam2)

print("Max diff approx:", np.max(np.abs(pmf_z_conv - pmf_z_exact)))
```

```python
import sympy as sp
x, z = sp.symbols('x z', real=True)
fZ = sp.integrate(1, (x, sp.Max(0, z-1), sp.Min(1, z)))
sp.simplify(fZ)
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve

N = 1000
x = np.linspace(0, 1, N)
dx = x[1]-x[0]
fX = np.ones_like(x)
fY = np.ones_like(x)
fZ_num = fftconvolve(fX, fY) * dx
z = np.linspace(0, 2, len(fZ_num))
fZ_theo = np.where(z<=1, z, 2-z)
fZ_theo = np.where((z<0)|(z>2), 0, fZ_theo)

plt.plot(z, fZ_num, label='numérica (fft conv)')
plt.plot(z, fZ_theo, '--', label='teórica')
plt.legend()
plt.xlabel('z'); plt.ylabel('f_Z(z)')
plt.title('Convolución Uniformes[0,1]')
plt.show()
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.signal import fftconvolve

x = np.linspace(-10, 10, 10000)
dx = x[1]-x[0]
fX = norm.pdf(x, loc=1.0, scale=2.0)
fY = norm.pdf(x, loc=-0.5, scale=1.5)
fZ_num = fftconvolve(fX, fY) * dx
z = np.linspace(2*x[0], 2*x[-1], len(fZ_num))
mu = 1.0 + (-0.5)
sigma = np.sqrt(2.0**2 + 1.5**2)
fZ_theo = norm.pdf(z, loc=mu, scale=sigma)

plt.plot(z, fZ_num, label='numérica (conv)')
plt.plot(z, fZ_theo, '--', label='teórica')
plt.legend(); plt.xlim(-5,7)
plt.show()
```

## Resumen  

## 5.3 — PMF / PDF condicionales

* **Idea:** la distribución condicional describe la distribución de (Y) cuando ya sabemos el valor de (X).
* **Discreto (PMF):**
  $$
  P_{Y|X}(y|x)=\frac{P_{X,Y}(x,y)}{P_X(x)},\qquad P_X(x)>0.
  $$
  Propiedades: no-negatividad, normalización (\sum_y P_{Y|X}(y|x)=1), y reconstrucción (P_{X,Y}=P_XP_{Y|X}). Si independientes (P_{Y|X}=P_Y).
* **Continuo (PDF):**
  $$
  f_{Y|X}(y|x)=\frac{f_{X,Y}(x,y)}{f_X(x)},\qquad f_X(x)=\int f_{X,Y}(x,y),dy.
  $$
  Propiedades análogas: (\int f_{Y|X}(y|x),dy=1), reconstrucción (f_{X,Y}=f_X f_{Y|X}), independencia (\Rightarrow f_{Y|X}=f_Y).

**Ejemplos verificados:**

* Urna (3R,2A,1V), 2 extracciones sin reemplazo. Tabla conjunta correcta; para (X=1):
  $$
  P_{Y|X}(0|1)=\tfrac13,\quad P_{Y|X}(1|1)=\tfrac23,\quad P_{Y|X}(2|1)=0.
  $$
* (f_{X,Y}(x,y)=x+y) en ([0,1]^2). Marginal (f_X(x)=x+\tfrac12). Entonces
  $$
  f_{Y|X}(y|x)=\frac{x+y}{x+\tfrac12},\quad P(Y<0.5\mid X=0.5)=0.375.
  $$

## 5.4 — Esperanza condicional y Ley de la esperanza total

* **Definición:**

* Discreta: $(E[Y|X=x]=\sum_y y,P_{Y|X}(y|x))$.
* Continua: $(E[Y|X=x]=\int y,f_{Y|X}(y|x),dy.)$
* **Propiedades:** linealidad, iteración $(E[Y]=E[E[Y|X]])$, e independencia $(\Rightarrow E[Y|X]=E[Y])$.
* **Urna (verificación):**
  $(;E[Y|X=0]=\tf\frac{4}{3},;E[Y|X=1]=\tf\frac{2}{3},;E[Y|X=2]=0)$.
  Aplicando LET con $(P_X(0)=3/15,;P_X(1)=9/15,;P_X(2)=3/15)$ se obtiene $(E[Y]=\tfrac23)$. (verificado).

---

## 5.5 — Suma (Z=X+Y) y convolución

* **Discreto (si independientes):**
  $$
  P_Z(z)=\sum_x P_X(x)P_Y(z-x).
  $$
  (Si no son independientes, se usa la PMF conjunta: $(P(Z=z)=\sum_x P_{X,Y}(x,z-x)).)$
* **Continuo (si independientes):**
  $$
  f_Z(z)=\int_{-\infty}^{\infty} f_X(x)f_Y(z-x),dx.
  $$
* **Propiedades claves:**

  * $(E[X+Y]=E[X]+E[Y])$.
  * **Corrección tipográfica importante:**
    $$
    \operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y).
    $$
    (En el texto original había una coma entre el 2 y (\operatorname{Cov}); lo correcto es multiplicación.)
  * Si independientes, (\operatorname{Cov}=0) y las varianzas se suman.

**Casos comunes (independientes):**

* Binomiales con mismo (p): suma binomial.
* Poisson: suma con parámetros añadidos.
* Normales: suma normal con medias y varianzas sumadas.
* Uniformes (U[0,1]): la suma tiene distribución triangular en ([0,2]).

---

## Errores / omisiones detectadas y correcciones aplicadas

1. **Varianza:** sustituí la coma tipográfica por el operador multiplicativo en la fórmula de varianza (ver arriba).
2. **Convolución discreta:** aclaré que la fórmula estándar $(P_Z(z)=\sum_x P_X(x)P_Y(z-x))$ **requiere independencia**; si existen dependencias hay que usar la PMF conjunta.
3. **Buenas prácticas numéricas** (sugerencias implementadas en el resumen):

   * Para matrices de covarianza simétricas usar `np.linalg.eigh` (más estable) en vez de `np.linalg.eig`.
   * En whitening usar pseudoinversa `np.linalg.pinv` si hay eigenvalores muy pequeños.
   * En simulaciones fijar `np.random.seed()` para reproducibilidad cuando convenga.
4. **Estabilidad simbólica / numérica:** en ejemplos con `sympy`/`scipy` añadí la observación de comparar simbólico vs numérico y mostrar ambos resultados.

---

## Ejercicios (compactos) — con pistas/soluciones resumidas

### Ej. 1 — Urna (condicionales)

Planteamiento: de la urna 3R/2A/1V extraes 2 sin reemplazo. Calcular $(P(X=0,Y=1)), (P_{Y|X}(1|0)) y (E[Y|X=0])$.

* Pista: cuenta combinatoria $(\binom{3}{x}\binom{2}{y}\binom{1}{2-x-y}/\binom{6}{2})$.
* Solución breve: $(P(0,1)=2/15)$. $(P_X(0)=3/15)$. $(P_{Y|X}(1|0)=(2/15)/(3/15)=2/3)$. $(E[Y|X=0]=0\cdot(1/3)+1\cdot(2/3)+2\cdot(0)=2/3)$ — **nota:** la expectativa total para X=0 según tabla original fue (4/3); eso indica que para X=0 la condicional incluye (y=2) con probabilidad 1/3? — *verificación completa abajo*.

> **Precisión**: Para X=0 la PMF condicional es $(P(Y=0|0)=0,;P(Y=1|0)=2/3,;P(Y=2|0)=1/3)$. De ahí $(E[Y|X=0]=\tf\frac{2}{3}\cdot1 + \tf\frac{1}{3}\cdot2 = \tf\frac{4}{3})$. (Por eso en el texto aparece (4/3).)

---

### Ej.2 — PDF condicional

Sea $(f_{X,Y}(x,y)=x+y)$ en $([0,1]^2)$. Encuentra $(f_X(x))$, $(f_{Y|X}(y|x))$ y $(P(Y<0.2\mid X=0.8))$.

* Pista: $(f_X(x)=\int_0^1 (x+y),dy)$.
* Solución breve: $(f_X(x)=x+\tfrac12)$. $(f_{Y|X}=(x+y)/(x+\tfrac12))$. Para (x=0.8): integrar (0.8+y) renormalizado sobre $(0\le y\le0.2)$.

(Cálculo: $(f_{Y|X}(y|0.8)=\df\frac{0.8+y}{1.3})$. Entonces $(P=\df\frac{1}{1.3}\int_0^{0.2} (0.8+y),dy=\df\frac{1}{1.3}[0.8y+\tf\frac{y^2}{2}]_0^{0.2}=\df\frac{1}{1.3}(0.16+0.02)=\df\frac{0.18}{1.3}\approx0.13846.))$

---

### Ej.3 — Ley de la Esperanza Total

Usando la tabla de la urna, verifica $(E[Y]=E[E[Y|X]])$ (mostrar los pasos).

* Solución: ya está en el texto: $(E[Y]=\tfrac23)$.

---

### Ej.4 — Convolución discreta

Suma de dos dados: calcula $(P(Z=7))$.

* Solución: $(6/36=1/6)$.

---

### Ej.5 — Convolución continua

Suma de $(U[0,1])$. Escribe $(f_Z(z))$ y grafícalo (triangular).

* Solución: $(f_Z(z)=z)$ para $(0\le z\le1)$, $(2-z)$ para $(1<z\le2)$.

---

### Ej.6 — Código: verifica por simulación

Implementa en Python Monte Carlo la comprobación de la PMF conjunta y las condicionales (ya hay un bloque en el notebook).

* Pista de estabilidad: usa `Fraction` para exactitud teórica; para la simulación N grande (p. ej. 200k) para obtener convergencia.

---

## 🔧 Correcciones/implementaciones de código (snippets sugeridos)

1. **Usar `np.linalg.eigh` para covarianzas simétricas**

```python
## en PCAFromScratch o analisis_espectral_completo
eigenvals, eigenvecs = np.linalg.eigh(cov_matrix)  # más estable
idx = np.argsort(eigenvals)[::-1]
eigenvals, eigenvecs = eigenvals[idx], eigenvecs[:, idx]
```

2. **Whitening: usar pseudoinversa para estabilidad**

```python
## dentro de fit()
eps = 1e-12
D_inv_sqrt = np.diag(1.0 / np.sqrt(self.eigenvals + eps))
if self.method == 'pca':
    self.W = self.eigenvecs @ D_inv_sqrt @ self.eigenvecs.T
elif self.method == 'zca':
    self.W = self.eigenvecs @ D_inv_sqrt @ self.eigenvecs.T @ self.eigenvecs @ np.diag(np.sqrt(self.eigenvals)) @ self.eigenvecs.T
## (o usar pinv si conviene)
```

3. **Simulación urna (reproducible)**

```python
np.random.seed(0)
N = 200000
## resto del código igual
```

4. **Pequeña corrección tipográfica en el PDF-continua verificación:** al mostrar la integral analítica utiliza `\left[\cdots\right]` para claridad. (Esto no cambia el cálculo, solo mejora presentación.)

---

#Verificaciones rápidas (ya hechas)

* Valores de la urna, condicionales y expectativas: **verificados** (resultados consistentes con los bloques `Fraction` y simulación).
* Integral del caso $(x+y)$ en $([0,1]^2)$: marginal y condicional normalizan correctamente; $(P(Y<0.5|X=0.5)=0.375)$ **verificado**.
* Convoluciones demostrativas (dados, binomiales, Poisson, normales, uniformes): correctas y coherentes con código propuesto.

---

## Análisis Multivariado: Vectores Aleatorios, Covarianza y PCA

## 5.6 Vectores Aleatorios y Matrices de Covarianza

### 5.6.1 Definición e Intuición Geométrica

Un **vector aleatorio** $\mathbf{X}$ en $\mathbb{R}^p$ es una colección de $p$ variables aleatorias:

$$
\mathbf{X} = \begin{pmatrix} X_1 \\ X_2 \\ \vdots \\ X_p \end{pmatrix}
$$

**Intuición geométrica:** Cada realización de $\mathbf{X}$ representa un punto en el espacio $p$-dimensional. La nube de puntos resultante revela la estructura de dependencia entre variables.

**Ejemplo visual:** Consideremos el caso bidimensional $(X,Y)$:
- Si $X$ e $Y$ son independientes: nube de puntos isotrópica
- Si $X$ e $Y$ están correlacionadas: nube de puntos elipsoidal
- Si $X$ e $Y$ tienen correlación perfecta: puntos alineados

### 5.6.2 Función de Densidad de Probabilidad Conjunta

Para variables continuas, la PDF conjunta $f_{\mathbf{X}}(\mathbf{x})$ satisface:

$$
P(\mathbf{X} \in R) = \int_R f_{\mathbf{X}}(\mathbf{x})  d\mathbf{x}
$$

**Caso especial - Independencia:**
$$
f_{\mathbf{X}}(\mathbf{x}) = \prod_{i=1}^p f_{X_i}(x_i)
$$

**Ejemplo detallado:** Distribución uniforme en región triangular

Sea $f_{X,Y}(x,y) = 2$ para $0 \le x \le 1$, $0 \le y \le x$, y $0$ en otro caso.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

## Verificación de normalización
result, error = integrate.dblquad(lambda y, x: 2, 0, 1, lambda x: 0, lambda x: x)
print(f"Integral de la PDF: {result}, Error: {error}")

## Visualización
x_vals = np.linspace(0, 1, 100)
y_vals = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = np.where(Y <= X, 2, 0)

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, levels=20)
plt.colorbar()
plt.title('PDF Conjunta en Región Triangular')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```

### 5.6.3 Vector de Esperanza (Media)

$$
\mathbb{E}[\mathbf{X}] = \begin{pmatrix} \mathbb{E}[X_1] \\ \mathbb{E}[X_2] \\ \vdots \\ \mathbb{E}[X_p] \end{pmatrix}
$$

**Ejemplo analítico extendido:** Para la distribución triangular anterior:

```python
## Cálculo de esperanzas marginales
E_X = integrate.dblquad(lambda y, x: x * 2, 0, 1, lambda x: 0, lambda x: x)[0]
E_Y = integrate.dblquad(lambda y, x: y * 2, 0, 1, lambda x: 0, lambda x: x)[0]

print(f"E[X] = {E_X:.3f}")
print(f"E[Y] = {E_Y:.3f}")

## Cálculo usando sympy para precisión analítica
import sympy as sp
x, y = sp.symbols('x y', real=True, positive=True)
f_xy = 2

E_X_sym = sp.integrate(x * f_xy, (y, 0, x), (x, 0, 1))
E_Y_sym = sp.integrate(y * f_xy, (y, 0, x), (x, 0, 1))

print(f"E[X] (analítico) = {E_X_sym} = {float(E_X_sym):.3f}")
print(f"E[Y] (analítico) = {E_Y_sym} = {float(E_Y_sym):.3f}")
```

### 5.6.4 Matriz de Covarianza - Teoría Profunda

La matriz de covarianza $\mathbf{\Sigma}$ se define como:

$$
\mathbf{\Sigma} = \mathbb{E}[(\mathbf{X} - \mathbf{\mu})(\mathbf{X} - \mathbf{\mu})^T]
$$

**Descomposición en componentes:**

- **Elementos diagonales:** $\Sigma_{ii} = \text{Var}(X_i)$
- **Elementos no diagonales:** $\Sigma_{ij} = \text{Cov}(X_i, X_j)$

**Propiedades fundamentales:**
1. **Simetría:** $\mathbf{\Sigma} = \mathbf{\Sigma}^T$
2. **Positivo semidefinida:** $\mathbf{z}^T\mathbf{\Sigma}\mathbf{z} \ge 0$ para todo $\mathbf{z}$
3. **Rango:** Indica dependencias lineales entre variables

**Ejemplo computacional detallado:**

```python
def calcular_covarianza_analitica():
    """Cálculo analítico completo de la matriz de covarianza"""
## Para la distribución triangular f(x,y)=2, 0≤y≤x≤1
    
## Esperanzas
    E_X = 2/3
    E_Y = 1/3
    
## Segundos momentos
    E_X2 = sp.integrate(x**2 * f_xy, (y, 0, x), (x, 0, 1))
    E_Y2 = sp.integrate(y**2 * f_xy, (y, 0, x), (x, 0, 1))
    E_XY = sp.integrate(x*y * f_xy, (y, 0, x), (x, 0, 1))
    
## Varianzas y covarianza
    Var_X = E_X2 - E_X**2
    Var_Y = E_Y2 - E_Y**2
    Cov_XY = E_XY - E_X * E_Y
    
    Sigma = np.array([[Var_X, Cov_XY], [Cov_XY, Var_Y]])
    return Sigma

Sigma_analitica = calcular_covarianza_analitica()
print("Matriz de covarianza analítica:")
print(Sigma_analitica)

## Verificación por simulación
def generar_muestra_triangular(n=10000):
    """Genera muestras de la distribución triangular"""
    u1 = np.random.uniform(0, 1, n)
    u2 = np.random.uniform(0, 1, n)
    x = np.maximum(u1, u2)
    y = np.minimum(u1, u2)
    return np.column_stack([x, y])

muestra = generar_muestra_triangular(100000)
Sigma_muestral = np.cov(muestra, rowvar=False)

print("\nMatriz de covarianza muestral:")
print(Sigma_muestral)
```

### 5.6.5 Distribución Normal Multivariada

La PDF de una normal $p$-dimensional $\mathbf{X} \sim \mathcal{N}(\mathbf{\mu}, \mathbf{\Sigma})$ es:

$$
f(\mathbf{x}) = \frac{1}{(2\pi)^{p/2}|\mathbf{\Sigma}|^{1/2}} \exp\left(-\frac{1}{2}(\mathbf{x}-\mathbf{\mu})^T\mathbf{\Sigma}^{-1}(\mathbf{x}-\mathbf{\mu})\right)
$$

**Interpretación geométrica de la distancia de Mahalanobis:**

```python
def visualizar_normal_multivariada():
    """Visualización completa de distribución normal bivariada"""
    mu = np.array([0, 0])
    Sigma = np.array([[2, 1], [1, 1]])
    
## Generar puntos en la elipse de confianza
    theta = np.linspace(0, 2*np.pi, 100)
    circle = np.column_stack([np.cos(theta), np.sin(theta)])
    
## Descomposición espectral para transformar círculo a elipse
    eigenvals, eigenvecs = np.linalg.eig(Sigma)
    ellipse = circle @ np.diag(np.sqrt(eigenvals)) @ eigenvecs.T
    ellipse += mu
    
## Gráfico
    plt.figure(figsize=(10, 8))
    plt.plot(ellipse[:, 0], ellipse[:, 1], 'r-', linewidth=2, label='Elipse 1-sigma')
    plt.quiver(mu[0], mu[1], eigenvecs[0,0]*np.sqrt(eigenvals[0]),
               eigenvecs[1,0]*np.sqrt(eigenvals[0]),
               angles='xy', scale_units='xy', scale=1, color='blue', width=0.01, label='PC1')
    plt.quiver(mu[0], mu[1], eigenvecs[0,1]*np.sqrt(eigenvals[1]),
               eigenvecs[1,1]*np.sqrt(eigenvals[1]),
               angles='xy', scale_units='xy', scale=1, color='green', width=0.01, label='PC2')
    
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.legend()
    plt.title('Distribución Normal Bivariada y Componentes Principales')
    plt.show()

visualizar_normal_multivariada()
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

## Verificación de normalización
result, error = integrate.dblquad(lambda y, x: 2, 0, 1, lambda x: 0, lambda x: x)
print(f"Integral de la PDF: {result}, Error: {error}")

## Visualización
x_vals = np.linspace(0, 1, 100)
y_vals = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = np.where(Y <= X, 2, 0)

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, levels=20)
plt.colorbar()
plt.title('PDF Conjunta en Región Triangular')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```

```python
## Cálculo de esperanzas marginales
E_X = integrate.dblquad(lambda y, x: x * 2, 0, 1, lambda x: 0, lambda x: x)[0]
E_Y = integrate.dblquad(lambda y, x: y * 2, 0, 1, lambda x: 0, lambda x: x)[0]

print(f"E[X] = {E_X:.3f}")
print(f"E[Y] = {E_Y:.3f}")

## Cálculo usando sympy para precisión analítica
import sympy as sp
x, y = sp.symbols('x y', real=True, positive=True)
f_xy = 2

E_X_sym = sp.integrate(x * f_xy, (y, 0, x), (x, 0, 1))
E_Y_sym = sp.integrate(y * f_xy, (y, 0, x), (x, 0, 1))

print(f"E[X] (analítico) = {E_X_sym} = {float(E_X_sym):.3f}")
print(f"E[Y] (analítico) = {E_Y_sym} = {float(E_Y_sym):.3f}")
```

```python
def calcular_covarianza_analitica():
    """Cálculo analítico completo de la matriz de covarianza"""
## Para la distribución triangular f(x,y)=2, 0≤y≤x≤1

## Esperanzas
    E_X = 2/3
    E_Y = 1/3

## Segundos momentos
    E_X2 = sp.integrate(x**2 * f_xy, (y, 0, x), (x, 0, 1))
    E_Y2 = sp.integrate(y**2 * f_xy, (y, 0, x), (x, 0, 1))
    E_XY = sp.integrate(x*y * f_xy, (y, 0, x), (x, 0, 1))

## Varianzas y covarianza
    Var_X = E_X2 - E_X**2
    Var_Y = E_Y2 - E_Y**2
    Cov_XY = E_XY - E_X * E_Y

    Sigma = np.array([[Var_X, Cov_XY], [Cov_XY, Var_Y]])
    return Sigma

Sigma_analitica = calcular_covarianza_analitica()
print("Matriz de covarianza analítica:")
print(Sigma_analitica)

## Verificación por simulación
def generar_muestra_triangular(n=10000):
    """Genera muestras de la distribución triangular"""
    u1 = np.random.uniform(0, 1, n)
    u2 = np.random.uniform(0, 1, n)
    x = np.maximum(u1, u2)
    y = np.minimum(u1, u2)
    return np.column_stack([x, y])

muestra = generar_muestra_triangular(100000)
Sigma_muestral = np.cov(muestra, rowvar=False)

print("\nMatriz de covarianza muestral:")
print(Sigma_muestral)
```

```python
def visualizar_normal_multivariada():
    """Visualización completa de distribución normal bivariada"""
    mu = np.array([0, 0])
    Sigma = np.array([[2, 1], [1, 1]])

## Generar puntos en la elipse de confianza
    theta = np.linspace(0, 2*np.pi, 100)
    circle = np.column_stack([np.cos(theta), np.sin(theta)])

## Descomposición espectral para transformar círculo a elipse
    eigenvals, eigenvecs = np.linalg.eig(Sigma)
    ellipse = circle @ np.diag(np.sqrt(eigenvals)) @ eigenvecs.T
    ellipse += mu

## Gráfico
    plt.figure(figsize=(10, 8))
    plt.plot(ellipse[:, 0], ellipse[:, 1], 'r-', linewidth=2, label='Elipse 1-sigma')
    plt.quiver(mu[0], mu[1], eigenvecs[0,0]*np.sqrt(eigenvals[0]),
               eigenvecs[1,0]*np.sqrt(eigenvals[0]),
               angles='xy', scale_units='xy', scale=1, color='blue', width=0.01, label='PC1')
    plt.quiver(mu[0], mu[1], eigenvecs[0,1]*np.sqrt(eigenvals[1]),
               eigenvecs[1,1]*np.sqrt(eigenvals[1]),
               angles='xy', scale_units='xy', scale=1, color='green', width=0.01, label='PC2')

    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.legend()
    plt.title('Distribución Normal Bivariada y Componentes Principales')
    plt.show()

visualizar_normal_multivariada()
```

## 5.7 Transformaciones de Gaussianas Multidimensionales

### 5.7.1 Transformaciones Lineales - Teoría Extendida

Sea $\mathbf{Y} = \mathbf{A}\mathbf{X} + \mathbf{b}$ con $\mathbf{X} \sim \mathcal{N}(\mathbf{\mu}_X, \mathbf{\Sigma}_X)$. Entonces:

$$
\mathbf{Y} \sim \mathcal{N}(\mathbf{A}\mathbf{\mu}_X + \mathbf{b}, \mathbf{A}\mathbf{\Sigma}_X\mathbf{A}^T)
$$

**Ejemplo multidimensional:**

```python
def transformacion_lineal_multivariada():
    """Ejemplo completo de transformación lineal de vector gaussiano"""
## Distribución original
    mu_X = np.array([1, 2, 3])
    Sigma_X = np.array([[4, 1, 0.5],
                       [1, 3, 0.8],
                       [0.5, 0.8, 2]])
    
## Matriz de transformación (reducción de dimensionalidad)
    A = np.array([[1, 0.5, 0],
                  [0, 1, 1]])
    b = np.array([-1, 2])
    
## Distribución transformada
    mu_Y = A @ mu_X + b
    Sigma_Y = A @ Sigma_X @ A.T
    
    print("Distribución original:")
    print(f"μ_X = {mu_X}")
    print(f"Σ_X =\n{Sigma_X}")
    
    print("\nDistribución transformada:")
    print(f"μ_Y = {mu_Y}")
    print(f"Σ_Y =\n{Sigma_Y}")
    
## Verificación por simulación
    X = np.random.multivariate_normal(mu_X, Sigma_X, 10000)
    Y_sim = (A @ X.T + b.reshape(-1, 1)).T
    
    print("\nVerificación por simulación:")
    print(f"μ_Y_sim = {np.mean(Y_sim, axis=0)}")
    print(f"Σ_Y_sim =\n{np.cov(Y_sim, rowvar=False)}")

transformacion_lineal_multivariada()
```

### 5.7.2 Descomposición Espectral y Geometría

La descomposición $\mathbf{\Sigma} = \mathbf{V}\mathbf{\Lambda}\mathbf{V}^T$ revela:

- **Eigenvectores:** Direcciones principales de variación
- **Eigenvalores:** Magnitud de variación en cada dirección

**Análisis geométrico completo:**

```python
def analisis_espectral_completo(Sigma):
    """Análisis completo de la descomposición espectral"""
    eigenvals, eigenvecs = np.linalg.eig(Sigma)
    
    print("Descomposición Espectral:")
    print(f"Eigenvalores: {eigenvals}")
    print(f"Eigenvectores:\n{eigenvecs}")
    
## Verificación de ortogonalidad
    print(f"\nOrtogonalidad (V·V^T):\n{eigenvecs @ eigenvecs.T}")
    
## Proporción de varianza explicada
    var_total = np.sum(eigenvals)
    prop_var = eigenvals / var_total
    print(f"\nProporción de varianza explicada: {prop_var}")
    
    return eigenvals, eigenvecs

Sigma_ejemplo = np.array([[5, 2, 1],
                         [2, 3, 0.5],
                         [1, 0.5, 2]])
analisis_espectral_completo(Sigma_ejemplo)
```

### 5.7.3 Blanqueamiento (Whitening) - Implementación Completa

El blanqueamiento transforma los datos para tener covarianza identidad:

```python
class WhiteningTransformer:
    """Implementación completa de blanqueamiento gaussiano"""
    
    def __init__(self, method='zca'):
        self.method = method  # 'zca', 'pca', 'cholesky'
        
    def fit(self, X):
        self.mu = np.mean(X, axis=0)
        X_centered = X - self.mu
        self.Sigma = np.cov(X_centered, rowvar=False)
        
## Descomposición espectral
        self.eigenvals, self.eigenvecs = np.linalg.eig(self.Sigma)
        
        if self.method == 'pca':
## Blanqueamiento PCA
            self.W = self.eigenvecs @ np.diag(1.0 / np.sqrt(self.eigenvals)) @ self.eigenvecs.T
        elif self.method == 'zca':
## Blanqueamiento ZCA (Mahalanobis)
            self.W = np.linalg.inv(self.eigenvecs @ np.diag(np.sqrt(self.eigenvals)) @ self.eigenvecs.T)
        else:  # Cholesky
            self.W = np.linalg.cholesky(np.linalg.inv(self.Sigma))
        
        return self
    
    def transform(self, X):
        X_centered = X - self.mu
        return X_centered @ self.W.T
    
    def inverse_transform(self, Z):
        return Z @ np.linalg.inv(self.W.T) + self.mu

## Ejemplo de uso
X_data = np.random.multivariate_normal([1, 2], [[4, 2], [2, 3]], 1000)
whitener = WhiteningTransformer(method='zca').fit(X_data)
Z_white = whitener.transform(X_data)

print("Covarianza original:\n", np.cov(X_data.T))
print("\nCovarianza después de blanqueamiento:\n", np.cov(Z_white.T))
```

```python
def transformacion_lineal_multivariada():
    """Ejemplo completo de transformación lineal de vector gaussiano"""
## Distribución original
    mu_X = np.array([1, 2, 3])
    Sigma_X = np.array([[4, 1, 0.5],
                       [1, 3, 0.8],
                       [0.5, 0.8, 2]])

## Matriz de transformación (reducción de dimensionalidad)
    A = np.array([[1, 0.5, 0],
                  [0, 1, 1]])
    b = np.array([-1, 2])

## Distribución transformada
    mu_Y = A @ mu_X + b
    Sigma_Y = A @ Sigma_X @ A.T

    print("Distribución original:")
    print(f"μ_X = {mu_X}")
    print(f"Σ_X =\n{Sigma_X}")

    print("\nDistribución transformada:")
    print(f"μ_Y = {mu_Y}")
    print(f"Σ_Y =\n{Sigma_Y}")

## Verificación por simulación
    X = np.random.multivariate_normal(mu_X, Sigma_X, 10000)
    Y_sim = (A @ X.T + b.reshape(-1, 1)).T

    print("\nVerificación por simulación:")
    print(f"μ_Y_sim = {np.mean(Y_sim, axis=0)}")
    print(f"Σ_Y_sim =\n{np.cov(Y_sim, rowvar=False)}")

transformacion_lineal_multivariada()
```

```python
def analisis_espectral_completo(Sigma):
    """Análisis completo de la descomposición espectral"""
    eigenvals, eigenvecs = np.linalg.eig(Sigma)

    print("Descomposición Espectral:")
    print(f"Eigenvalores: {eigenvals}")
    print(f"Eigenvectores:\n{eigenvecs}")

## Verificación de ortogonalidad
    print(f"\nOrtogonalidad (V·V^T):\n{eigenvecs @ eigenvecs.T}")

## Proporción de varianza explicada
    var_total = np.sum(eigenvals)
    prop_var = eigenvals / var_total
    print(f"\nProporción de varianza explicada: {prop_var}")

    return eigenvals, eigenvecs

Sigma_ejemplo = np.array([[5, 2, 1],
                         [2, 3, 0.5],
                         [1, 0.5, 2]])
analisis_espectral_completo(Sigma_ejemplo)
```

```python
class WhiteningTransformer:
    """Implementación completa de blanqueamiento gaussiano"""

    def __init__(self, method='zca'):
        self.method = method  # 'zca', 'pca', 'cholesky'

    def fit(self, X):
        self.mu = np.mean(X, axis=0)
        X_centered = X - self.mu
        self.Sigma = np.cov(X_centered, rowvar=False)

## Descomposición espectral
        self.eigenvals, self.eigenvecs = np.linalg.eig(self.Sigma)

        if self.method == 'pca':
## Blanqueamiento PCA
            self.W = self.eigenvecs @ np.diag(1.0 / np.sqrt(self.eigenvals)) @ self.eigenvecs.T
        elif self.method == 'zca':
## Blanqueamiento ZCA (Mahalanobis)
            self.W = np.linalg.inv(self.eigenvecs @ np.diag(np.sqrt(self.eigenvals)) @ self.eigenvecs.T)
        else:  # Cholesky
            self.W = np.linalg.cholesky(np.linalg.inv(self.Sigma))

        return self

    def transform(self, X):
        X_centered = X - self.mu
        return X_centered @ self.W.T

    def inverse_transform(self, Z):
        return Z @ np.linalg.inv(self.W.T) + self.mu

## Ejemplo de uso
X_data = np.random.multivariate_normal([1, 2], [[4, 2], [2, 3]], 1000)
whitener = WhiteningTransformer(method='zca').fit(X_data)
Z_white = whitener.transform(X_data)

print("Covarianza original:\n", np.cov(X_data.T))
print("\nCovarianza después de blanqueamiento:\n", np.cov(Z_white.T))
```

## 5.8 Análisis de Componentes Principales (PCA) - Profundización

### 5.8.1 Fundamentos Matemáticos Completos

Dado datos $\mathbf{X} \in \mathbb{R}^{n \times p}$, PCA encuentra:

1. **Centrado:** $\mathbf{X}_c = \mathbf{X} - \mathbf{1}\mathbf{\mu}^T$
2. **Descomposición:** $\mathbf{X}_c^T\mathbf{X}_c = \mathbf{V}\mathbf{\Lambda}\mathbf{V}^T$
3. **Proyección:** $\mathbf{Y} = \mathbf{X}_c\mathbf{V}_k$

**Implementación desde cero:**

```python
class PCAFromScratch:
    """Implementación completa de PCA desde primeros principios"""
    
    def __init__(self, n_components=None):
        self.n_components = n_components
        
    def fit(self, X):
## Centrado
        self.mean_ = np.mean(X, axis=0)
        X_centered = X - self.mean_
        
## Matriz de covarianza
        n_samples = X.shape[0]
        self.cov_matrix_ = (X_centered.T @ X_centered) / (n_samples - 1)
        
## Descomposición espectral
        eigenvals, eigenvecs = np.linalg.eig(self.cov_matrix_)
        
## Ordenar por eigenvalores descendentes
        idx = np.argsort(eigenvals)[::-1]
        self.eigenvalues_ = eigenvals[idx]
        self.components_ = eigenvecs[:, idx]
        
## Seleccionar componentes
        if self.n_components is not None:
            self.components_ = self.components_[:, :self.n_components]
            self.eigenvalues_ = self.eigenvalues_[:self.n_components]
            
## Varianza explicada
        self.explained_variance_ratio_ = self.eigenvalues_ / np.sum(self.eigenvalues_)
        
        return self
    
    def transform(self, X):
        X_centered = X - self.mean_
        return X_centered @ self.components_
    
    def inverse_transform(self, Y):
        return Y @ self.components_.T + self.mean_

## Comparación con scikit-learn
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

## Datos de ejemplo
iris = load_iris()
X = iris.data

## Nuestra implementación
pca_scratch = PCAFromScratch(n_components=2).fit(X)
X_pca_scratch = pca_scratch.transform(X)

## Scikit-learn
pca_sklearn = PCA(n_components=2).fit(X)
X_pca_sklearn = pca_sklearn.transform(X)

print("Varianza explicada (scratch):", pca_scratch.explained_variance_ratio_)
print("Varianza explicada (sklearn):", pca_sklearn.explained_variance_ratio_)
```

### 5.8.2 PCA en 2D y 3D - Ejemplos Visuales Completos

**Caso 2D - Rotación de datos correlacionados:**

```python
def pca_2d_demo():
    """Demo visual de PCA en 2 dimensiones"""
## Generar datos correlacionados
    np.random.seed(42)
    n_points = 300
    theta = np.random.uniform(0, 2*np.pi, n_points)
    r = np.random.normal(0, 0.3, n_points)
    
## Elipse rotada
    rotation_angle = np.pi/4
    rotation_matrix = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)],
                              [np.sin(rotation_angle), np.cos(rotation_angle)]])
    
    X_ellipse = np.column_stack([2*np.cos(theta) + r, 0.5*np.sin(theta) + r])
    X = X_ellipse @ rotation_matrix.T + [1, 2]
    
## Aplicar PCA
    pca = PCAFromScratch(n_components=2).fit(X)
    X_pca = pca.transform(X)
    
## Visualización
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
## Datos originales
    axes[0].scatter(X[:, 0], X[:, 1], alpha=0.6)
    axes[0].set_title('Datos Originales')
    axes[0].set_xlabel('X1')
    axes[0].set_ylabel('X2')
    axes[0].grid(True, alpha=0.3)
    axes[0].axis('equal')
    
## Datos + componentes principales
    axes[1].scatter(X[:, 0], X[:, 1], alpha=0.6)
    for length, vector in zip(pca.eigenvalues_, pca.components_.T):
        v = vector * np.sqrt(length) * 3  # Escalar para visualización
        axes[1].arrow(pca.mean_[0], pca.mean_[1], v[0], v[1],
                     head_width=0.1, head_length=0.1, fc='red', ec='red')
    axes[1].set_title('Componentes Principales')
    axes[1].set_xlabel('X1')
    axes[1].set_ylabel('X2')
    axes[1].grid(True, alpha=0.3)
    axes[1].axis('equal')
    
## Datos transformados
    axes[2].scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.6)
    axes[2].set_title('Espacio PCA (Decorrelacionado)')
    axes[2].set_xlabel('PC1')
    axes[2].set_ylabel('PC2')
    axes[2].grid(True, alpha=0.3)
    axes[2].axis('equal')
    
    plt.tight_layout()
    plt.show()

pca_2d_demo()
```

**Caso 3D - Reducción a 2D:**

```python
def pca_3d_demo():
    """Demo visual de PCA en 3 dimensiones con reducción a 2D"""
## Generar datos 3D correlacionados
    np.random.seed(42)
    n_points = 500
    
## Tres variables con diferentes correlaciones
    X1 = np.random.normal(0, 2, n_points)
    X2 = 0.7 * X1 + np.random.normal(0, 1, n_points)
    X3 = 0.5 * X1 + 0.3 * X2 + np.random.normal(0, 0.5, n_points)
    
    X_3d = np.column_stack([X1, X2, X3])
    
## Aplicar PCA
    pca_3d = PCAFromScratch(n_components=2).fit(X_3d)
    X_2d = pca_3d.transform(X_3d)
    
## Visualización 3D
    fig = plt.figure(figsize=(15, 5))
    
## Subplot 1: Datos originales 3D
    ax1 = fig.add_subplot(131, projection='3d')
    scatter = ax1.scatter(X_3d[:, 0], X_3d[:, 1], X_3d[:, 2],
                         c=X_3d[:, 0], cmap='viridis', alpha=0.6)
    ax1.set_title('Datos Originales 3D')
    ax1.set_xlabel('X1')
    ax1.set_ylabel('X2')
    ax1.set_zlabel('X3')
    
## Subplot 2: Componentes principales en 3D
    ax2 = fig.add_subplot(132, projection='3d')
    ax2.scatter(X_3d[:, 0], X_3d[:, 1], X_3d[:, 2], alpha=0.3)
    
## Dibujar componentes principales
    for length, vector in zip(pca_3d.eigenvalues_, pca_3d.components_.T):
        v = vector * np.sqrt(length) * 3
        ax2.quiver(pca_3d.mean_[0], pca_3d.mean_[1], pca_3d.mean_[2],
                  v[0], v[1], v[2], color='red', linewidth=3)
    
    ax2.set_title('Componentes Principales 3D')
    ax2.set_xlabel('X1')
    ax2.set_ylabel('X2')
    ax2.set_zlabel('X3')
    
## Subplot 3: Proyección 2D
    ax3 = fig.add_subplot(133)
    scatter_2d = ax3.scatter(X_2d[:, 0], X_2d[:, 1], c=X_3d[:, 0], cmap='viridis', alpha=0.6)
    ax3.set_title(f'Proyección PCA 2D\n(Varianza explicada: {np.sum(pca_3d.explained_variance_ratio_):.2%})')
    ax3.set_xlabel('PC1')
    ax3.set_ylabel('PC2')
    ax3.grid(True, alpha=0.3)
    
    plt.colorbar(scatter_2d, ax=ax3, label='Valor X1 original')
    plt.tight_layout()
    plt.show()
    
    print(f"Varianza explicada por cada componente: {pca_3d.explained_variance_ratio_}")
    print(f"Varianza total explicada: {np.sum(pca_3d.explained_variance_ratio_):.2%}")

pca_3d_demo()
```

### 5.8.3 Aplicaciones Avanzadas y Limitaciones

**Reconstrucción de datos con diferentes números de componentes:**

```python
def analisis_reconstruccion_pca():
    """Análisis de calidad de reconstrucción vs número de componentes"""
    from sklearn.datasets import load_digits
    
    digits = load_digits()
    X_digits = digits.data
    y_digits = digits.target
    
    n_components_range = [2, 5, 10, 20, 30, 50, 64]
    mse_values = []
    var_explained = []
    
    for n_comp in n_components_range:
        pca = PCAFromScratch(n_components=n_comp).fit(X_digits)
        X_transformed = pca.transform(X_digits)
        X_reconstructed = pca.inverse_transform(X_transformed)
        
## Error de reconstrucción
        mse = np.mean((X_digits - X_reconstructed) ** 2)
        mse_values.append(mse)
        var_explained.append(np.sum(pca.explained_variance_ratio_))
    
## Gráfico de trade-off
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    ax1.plot(n_components_range, mse_values, 'bo-', linewidth=2)
    ax1.set_xlabel('Número de Componentes')
    ax1.set_ylabel('Error Cuadrático Medio')
    ax1.set_title('Error de Reconstrucción vs Complejidad')
    ax1.grid(True, alpha=0.3)
    
    ax2.plot(n_components_range, var_explained, 'ro-', linewidth=2)
    ax2.set_xlabel('Número de Componentes')
    ax2.set_ylabel('Varianza Explicada')
    ax2.set_title('Varianza Explicada vs Complejidad')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

analisis_reconstruccion_pca()
```

**Limitaciones importantes del PCA:**

1. **Linealidad:** Solo captura relaciones lineales
2. **Varianza vs Información:** Maximiza varianza, no necesariamente información relevante
3. **Sensibilidad a escala:** Requiere estandarización previa
4. **Outliers:** Muy sensible a valores atípicos

**Alternativas no lineales (mencionar brevemente):**
- **t-SNE:** Para visualización de alta dimensión
- **UMAP:** Preserva mejor la estructura global
- **Autoencoders:** PCA no lineal mediante redes neuronales

```python
class PCAFromScratch:
    """Implementación completa de PCA desde primeros principios"""

    def __init__(self, n_components=None):
        self.n_components = n_components

    def fit(self, X):
## Centrado
        self.mean_ = np.mean(X, axis=0)
        X_centered = X - self.mean_

## Matriz de covarianza
        n_samples = X.shape[0]
        self.cov_matrix_ = (X_centered.T @ X_centered) / (n_samples - 1)

## Descomposición espectral
        eigenvals, eigenvecs = np.linalg.eig(self.cov_matrix_)

## Ordenar por eigenvalores descendentes
        idx = np.argsort(eigenvals)[::-1]
        self.eigenvalues_ = eigenvals[idx]
        self.components_ = eigenvecs[:, idx]

## Seleccionar componentes
        if self.n_components is not None:
            self.components_ = self.components_[:, :self.n_components]
            self.eigenvalues_ = self.eigenvalues_[:self.n_components]

## Varianza explicada
        self.explained_variance_ratio_ = self.eigenvalues_ / np.sum(self.eigenvalues_)

        return self

    def transform(self, X):
        X_centered = X - self.mean_
        return X_centered @ self.components_

    def inverse_transform(self, Y):
        return Y @ self.components_.T + self.mean_

## Comparación con scikit-learn
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

## Datos de ejemplo
iris = load_iris()
X = iris.data

## Nuestra implementación
pca_scratch = PCAFromScratch(n_components=2).fit(X)
X_pca_scratch = pca_scratch.transform(X)

## Scikit-learn
pca_sklearn = PCA(n_components=2).fit(X)
X_pca_sklearn = pca_sklearn.transform(X)

print("Varianza explicada (scratch):", pca_scratch.explained_variance_ratio_)
print("Varianza explicada (sklearn):", pca_sklearn.explained_variance_ratio_)
```

```python
def pca_2d_demo():
    """Demo visual de PCA en 2 dimensiones"""
## Generar datos correlacionados
    np.random.seed(42)
    n_points = 300
    theta = np.random.uniform(0, 2*np.pi, n_points)
    r = np.random.normal(0, 0.3, n_points)

## Elipse rotada
    rotation_angle = np.pi/4
    rotation_matrix = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)],
                              [np.sin(rotation_angle), np.cos(rotation_angle)]])

    X_ellipse = np.column_stack([2*np.cos(theta) + r, 0.5*np.sin(theta) + r])
    X = X_ellipse @ rotation_matrix.T + [1, 2]

## Aplicar PCA
    pca = PCAFromScratch(n_components=2).fit(X)
    X_pca = pca.transform(X)

## Visualización
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

## Datos originales
    axes[0].scatter(X[:, 0], X[:, 1], alpha=0.6)
    axes[0].set_title('Datos Originales')
    axes[0].set_xlabel('X1')
    axes[0].set_ylabel('X2')
    axes[0].grid(True, alpha=0.3)
    axes[0].axis('equal')

## Datos + componentes principales
    axes[1].scatter(X[:, 0], X[:, 1], alpha=0.6)
    for length, vector in zip(pca.eigenvalues_, pca.components_.T):
        v = vector * np.sqrt(length) * 3  # Escalar para visualización
        axes[1].arrow(pca.mean_[0], pca.mean_[1], v[0], v[1],
                     head_width=0.1, head_length=0.1, fc='red', ec='red')
    axes[1].set_title('Componentes Principales')
    axes[1].set_xlabel('X1')
    axes[1].set_ylabel('X2')
    axes[1].grid(True, alpha=0.3)
    axes[1].axis('equal')

## Datos transformados
    axes[2].scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.6)
    axes[2].set_title('Espacio PCA (Decorrelacionado)')
    axes[2].set_xlabel('PC1')
    axes[2].set_ylabel('PC2')
    axes[2].grid(True, alpha=0.3)
    axes[2].axis('equal')

    plt.tight_layout()
    plt.show()

pca_2d_demo()
```

```python
def pca_3d_demo():
    """Demo visual de PCA en 3 dimensiones con reducción a 2D"""
## Generar datos 3D correlacionados
    np.random.seed(42)
    n_points = 500

## Tres variables con diferentes correlaciones
    X1 = np.random.normal(0, 2, n_points)
    X2 = 0.7 * X1 + np.random.normal(0, 1, n_points)
    X3 = 0.5 * X1 + 0.3 * X2 + np.random.normal(0, 0.5, n_points)

    X_3d = np.column_stack([X1, X2, X3])

## Aplicar PCA
    pca_3d = PCAFromScratch(n_components=2).fit(X_3d)
    X_2d = pca_3d.transform(X_3d)

## Visualización 3D
    fig = plt.figure(figsize=(15, 5))

## Subplot 1: Datos originales 3D
    ax1 = fig.add_subplot(131, projection='3d')
    scatter = ax1.scatter(X_3d[:, 0], X_3d[:, 1], X_3d[:, 2],
                         c=X_3d[:, 0], cmap='viridis', alpha=0.6)
    ax1.set_title('Datos Originales 3D')
    ax1.set_xlabel('X1')
    ax1.set_ylabel('X2')
    ax1.set_zlabel('X3')

## Subplot 2: Componentes principales en 3D
    ax2 = fig.add_subplot(132, projection='3d')
    ax2.scatter(X_3d[:, 0], X_3d[:, 1], X_3d[:, 2], alpha=0.3)

## Dibujar componentes principales
    for length, vector in zip(pca_3d.eigenvalues_, pca_3d.components_.T):
        v = vector * np.sqrt(length) * 3
        ax2.quiver(pca_3d.mean_[0], pca_3d.mean_[1], pca_3d.mean_[2],
                  v[0], v[1], v[2], color='red', linewidth=3)

    ax2.set_title('Componentes Principales 3D')
    ax2.set_xlabel('X1')
    ax2.set_ylabel('X2')
    ax2.set_zlabel('X3')

## Subplot 3: Proyección 2D
    ax3 = fig.add_subplot(133)
    scatter_2d = ax3.scatter(X_2d[:, 0], X_2d[:, 1], c=X_3d[:, 0], cmap='viridis', alpha=0.6)
    ax3.set_title(f'Proyección PCA 2D\n(Varianza explicada: {np.sum(pca_3d.explained_variance_ratio_):.2%})')
    ax3.set_xlabel('PC1')
    ax3.set_ylabel('PC2')
    ax3.grid(True, alpha=0.3)

    plt.colorbar(scatter_2d, ax=ax3, label='Valor X1 original')
    plt.tight_layout()
    plt.show()

    print(f"Varianza explicada por cada componente: {pca_3d.explained_variance_ratio_}")
    print(f"Varianza total explicada: {np.sum(pca_3d.explained_variance_ratio_):.2%}")

pca_3d_demo()
```

```python
def analisis_reconstruccion_pca():
    """Análisis de calidad de reconstrucción vs número de componentes"""
    from sklearn.datasets import load_digits

    digits = load_digits()
    X_digits = digits.data
    y_digits = digits.target

    n_components_range = [2, 5, 10, 20, 30, 50, 64]
    mse_values = []
    var_explained = []

    for n_comp in n_components_range:
        pca = PCAFromScratch(n_components=n_comp).fit(X_digits)
        X_transformed = pca.transform(X_digits)
        X_reconstructed = pca.inverse_transform(X_transformed)

## Error de reconstrucción
        mse = np.mean((X_digits - X_reconstructed) ** 2)
        mse_values.append(mse)
        var_explained.append(np.sum(pca.explained_variance_ratio_))

## Gráfico de trade-off
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(n_components_range, mse_values, 'bo-', linewidth=2)
    ax1.set_xlabel('Número de Componentes')
    ax1.set_ylabel('Error Cuadrático Medio')
    ax1.set_title('Error de Reconstrucción vs Complejidad')
    ax1.grid(True, alpha=0.3)

    ax2.plot(n_components_range, var_explained, 'ro-', linewidth=2)
    ax2.set_xlabel('Número de Componentes')
    ax2.set_ylabel('Varianza Explicada')
    ax2.set_title('Varianza Explicada vs Complejidad')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

analisis_reconstruccion_pca()
```

## Resumen General: Análisis Multivariado, Covarianza y PCA

## Vectores Aleatorios y Matrices de Covarianza

### Definición

Un **vector aleatorio**
$$
\mathbf{X} = \begin{pmatrix} X_1 \ X_2 \ \vdots \ X_p \end{pmatrix}
$$
representa $p$ variables aleatorias tratadas como un único objeto en $\mathbb{R}^p$.
Cada observación de $\mathbf{X}$ es un punto en un espacio $p$-dimensional.

### Intuición geométrica

* **Independencia:** nube de puntos esférica o circular.
* **Correlación:** nube elipsoidal (las direcciones principales muestran dependencias lineales).
* **Correlación perfecta:** puntos alineados (una variable es combinación lineal de otra).

### Ejemplo correcto

Distribución uniforme en un triángulo:
$( f_{X,Y}(x,y) = 2 ) para ( 0 \le y \le x \le 1 )$.

* **Verificación de normalización:**
$$
\int_0^1 \int_0^x 2,dy,dx = 1
$$
(correcto).

### Esperanzas marginales (analítico correcto):

$$
E[X] = \frac{2}{3}, \quad E[Y] = \frac{1}{3}
$$

Se verifica mediante integración simbólica o numérica.

### Matriz de Covarianza

Definición:
$$
\Sigma = E[(\mathbf{X} - \mu)(\mathbf{X} - \mu)^T]
$$

Propiedades:

1. Simétrica.
2. Semidefinida positiva.
3. Su rango mide dependencias lineales.

#### Cálculo analítico (corregido):

$$
\begin{aligned}
E[X^2] &= \frac{1}{2}, \
E[Y^2] &= \frac{1}{6}, \
E[XY] &= \frac{1}{4}.
\end{aligned}
$$

$$
\Sigma =
\begin{pmatrix}
E[X^2] - E[X]^2 & E[XY] - E[X]E[Y] \
E[XY] - E[X]E[Y] & E[Y^2] - E[Y]^2
\end{pmatrix}
=============

\begin{pmatrix}
\frac{1}{18} & \frac{1}{36} \
\frac{1}{36} & \frac{1}{18}
\end{pmatrix}
\approx
\begin{pmatrix}
0.0556 & 0.0278 \
0.0278 & 0.0556
\end{pmatrix}
$$

Confirmado por simulación Monte Carlo.

---

## Distribución Normal Multivariada

### Definición general

$$
f(\mathbf{x}) = \frac{1}{(2\pi)^{p/2}|\Sigma|^{1/2}}
\exp\left(-\frac{1}{2}(\mathbf{x}-\mu)^T\Sigma^{-1}(\mathbf{x}-\mu)\right)
$$

La **distancia de Mahalanobis**
$$
D^2 = (\mathbf{x}-\mu)^T\Sigma^{-1}(\mathbf{x}-\mu)
$$
mide la distancia estadística considerando correlación entre variables.

### Interpretación geométrica

* Las curvas de nivel son **elipses (2D)** o **elipsoides (3D)**.
* Sus **ejes principales** son los **autovectores** de $\Sigma$.
* Sus **longitudes** están dadas por $\sqrt{\text{autovalores}}$.

El ejemplo visual en el código genera correctamente una elipse con vectores principales (PC1, PC2).

---

## Transformaciones Lineales de Gaussianas

### Teoría exacta

Si
$$
\mathbf{Y} = \mathbf{A}\mathbf{X} + \mathbf{b}, \quad \mathbf{X}\sim \mathcal{N}(\mu_X, \Sigma_X)
$$
entonces
$$
\mathbf{Y}\sim \mathcal{N}(\mathbf{A}\mu_X + \mathbf{b}, \mathbf{A}\Sigma_X\mathbf{A}^T)
$$

 La simulación confirma la teoría numéricamente.

---

## Descomposición Espectral (Eigen)

$$
\Sigma = V\Lambda V^T
$$

* $V$: matriz de **autovectores ortogonales** (direcciones principales).
* $\Lambda$: matriz diagonal de **autovalores** (varianzas en esas direcciones).
* Proporción de varianza explicada = $\lambda_i / \sum \lambda_j$.

El código `analisis_espectral_completo` es correcto; verifica ortogonalidad y varianza explicada.

---

## Blanqueamiento (Whitening)

### Concepto

Transformación que hace que los datos tengan media cero y covarianza identidad:
$$
Z = W(X - \mu)
$$
donde $( W \Sigma W^T = I )$.

### Métodos:

* **ZCA Whitening:** mantiene orientación original (Mahalanobis).
* **PCA Whitening:** rota los ejes según eigenvectores.
* **Cholesky Whitening:** usa factorización triangular inferior.

El código de `WhiteningTransformer` es correcto y funcional.
🔧 *Nota menor:* al usar `np.linalg.eig`, es mejor usar `np.linalg.eigh` (más estable para matrices simétricas).

---

## Análisis de Componentes Principales (PCA)

### Fundamentos

Objetivo: encontrar nuevas variables no correlacionadas (componentes principales) que capturen la máxima varianza posible.

Pasos:

1. Centrar los datos.
2. Calcular la matriz de covarianza.
3. Obtener autovalores y autovectores.
4. Proyectar:
   $$
   Y = X_c V_k
   $$

### Implementación desde cero

La clase `PCAFromScratch` es **correcta y completa**.
Corrige la ortogonalización automática de `np.linalg.eigh` si se quiere precisión adicional.
Coincide con la implementación de `scikit-learn`.

---

## Visualizaciones y Ejemplos

### 🔹 PCA 2D

* Muestra rotación de una nube elipsoidal.
* PC1 y PC2 aparecen como ejes de máxima varianza.
  ✅ Correcto, con visualización clara.

### 🔹 PCA 3D

* Reducción de 3D → 2D.
* La varianza explicada muestra la pérdida de información.
* El código usa proyecciones coherentes y gráficas interpretables.

---

## Conclusiones Globales

El documento presenta una **cobertura completa, rigurosa y correctamente implementada** del análisis multivariado clásico.

**Errores corregidos / ajustes recomendados:**

1. En la distribución triangular: corregidos los valores analíticos de momentos y matriz de covarianza.
2. En whitening: preferir `np.linalg.eigh` por estabilidad numérica.
3. En PCA: aclarar que los autovectores deben ser ortonormales (usar `eigh` en vez de `eig`).

**Fortalezas:**

* Integración de teoría, código y visualización.
* Ejemplos reproducibles y verificables.
* Enlace natural entre covarianza, normal multivariada y PCA.

---

---

## Resumen del Protocolo Maestro
- **Solución Analítica Resaltada**: $\boxed{\text{Verificado con SymPy y SciPy stats}}$
- **Verificación Simbólica (SymPy)**:


## Contexto de Aplicación en Nanotecnología
En el análisis bivariado de propiedades fisicoquímicas de nanopartículas coloidales, la distribución de probabilidad conjunta permite evaluar el impacto simultáneo del diámetro de partícula y el potencial zeta sobre la estabilidad coloidal y la tasa de aglomeración.

---

## 10. Módulo de Simulación: Generación Bivariada y Descomposición de Cholesky

Para simular vectores aleatorios continuos bivariados $(X, Y)$ con matriz de covarianza especificada $\Sigma$, se utiliza la **Descomposición de Cholesky** $\Sigma = L L^T$.

### 10.1 Algoritmo de Generación Bivariada Correlacionada
Dado $Z = (Z_1, Z_2)^T \sim \mathcal{N}(0, I_2)$ independientes:
$$X = \mu + L Z \implies X \sim \mathcal{N}(\mu, \Sigma)$$

### 10.2 Simulación en Python de Potencial Zeta y Diámetro Nanométrico
```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, Math

## Parámetros: [Diámetro (nm), Potencial Zeta (mV)]
mu = np.array([25.0, -40.0])
cov = np.array([
    [16.0, -18.0],   # Varianza X=16, Cov(X,Y)=-18
    [-18.0, 36.0]    # Varianza Y=36
])

## Descomposición de Cholesky
L = np.linalg.cholesky(cov)

## Muestreo
np.random.seed(99)
Z = stats.norm.rvs(size=(2, 10_000))
muestras_bivariadas = (mu.reshape(2, 1) + L @ Z).T

## Visualización
df_bivariado = pd.DataFrame(muestras_bivariadas, columns=["Diametro_nm", "PotencialZeta_mV"])
g = sns.jointplot(data=df_bivariado, x="Diametro_nm", y="PotencialZeta_mV", kind="kde", cmap="Blues", fill=True)
g.fig.suptitle("Simulación Bivariada por Cholesky: Diámetro vs Potencial Zeta", y=1.02, fontweight="bold")
plt.show()

cov_sim = np.cov(muestras_bivariadas.T)
display(Math(fr"\text{{Covarianza Simulada: }} \text{{Cov}}(X, Y) = {cov_sim[0, 1]:.2f}"))
```


---
## 9. Verificación Simbólica y Expresión Formal con SymPy

En distribuciones conjuntas, las densidades marginales y la condición de normalización $\int \int f(x,y) dx dy = 1$ se derivan por integración simbólica multivariada en **SymPy**.

### 9.1 Integración Simbólica de Densidad Bivariada

$$\boxed{\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) dx dy = 1}$$

```python
import sympy as sp
from IPython.display import display, Math

x, y = sp.symbols('x y', real=True)
c = sp.Symbol('c', positive=True)

## Densidad conjunta f(x,y) = c * x * y en [0,1]x[0,1]
f_xy = c * x * y

## Cálculo de la constante de normalización 'c'
integral_doble = sp.integrate(f_xy, (x, 0, 1), (y, 0, 1))
c_resuelto = sp.solve(integral_doble - 1, c)[0]

display(Math(r'\text{Constante de Normalización } c: ' + sp.latex(c_resuelto)))
display(Math(r'\text{Densidad Conjunta Validada } f(x,y): ' + sp.latex(c_resuelto * x * y)))
```
