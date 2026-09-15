## Prerequisitos de esta unidad

- **Estadística Descriptiva y EDA** (Unidad 1) — las frecuencias relativas de una muestra son la antesala empírica del concepto de probabilidad; aquí se formaliza ese límite.
- **Teoría de conjuntos básica** — unión, intersección, complemento y diferencia, para manipular eventos como subconjuntos del espacio muestral y aplicar las leyes de De Morgan.
- **Ciclo de Verificación Triple** (ver `GOVERNANCE.md`) — como en todas las unidades del curso, cada concepto con forma cerrada se verifica primero simbólicamente (SymPy) y luego se reproduce con las herramientas de producción (SciPy/statsmodels) antes de interpretarse.

---

## 1. Fundamentación Teórica y Conceptos Clave

La **Teoría de la Probabilidad** proporciona el marco matemático formal para cuantificar la incertidumbre y razonar bajo información incompleta. En la Ingeniería en Inteligencia Artificial y Nanotecnología, la probabilidad permite desde modelar la fluctuación térmica de nanopartículas en suspensión coloidal hasta calcular la probabilidad posterior en clasificadores bayesianos de imágenes microscópicas.

### 1.1 Experimento Aleatorio, Espacio Muestral y Eventos
* **Experimento Aleatorio ($\mathcal{E}$)**: Proceso cuyo resultado exacto no se puede predecir con certeza antes de su ejecución, pero cuyo conjunto de todos los resultados posibles es conocido.
* **Espacio Muestral ($\Omega$)**: Conjunto de todos los resultados posibles de un experimento aleatorio.
* **Evento o Sucesos ($A \subseteq \Omega$)**: Cualquier subconjunto del espacio muestral.

### 1.2 Álgebra de Conjuntos y Operaciones Eventuales
Las relaciones entre eventos se expresan mediante la teoría de conjuntos:
* **Unión ($A \cup B$)**: Ocurre al menos uno de los dos eventos.
* **Intersección ($A \cap B$)**: Ocurren ambos eventos simultáneamente.
* **Complemento ($A^c$ o $\bar{A}$)**: Ocurre cualquier resultado que no pertenece a $A$.
* **Eventos Mutuamente Excluyentes (Disjuntos)**: $A \cap B = \emptyset$.

Leyes de De Morgan:
$$(A \cup B)^c = A^c \cap B^c, \quad (A \cap B)^c = A^c \cup B^c$$

**Ejemplo verificando De Morgan (dos criterios de falla de un sensor)**: un lote de $10$ sensores nanoelectrónicos de gas, numerados $1$ a $10$, se somete a dos pruebas de falla independientes: $A$ = "falla por deriva de línea base" y $B$ = "falla por saturación del sensor". Supóngase que, tras la caracterización, $A = \{1,2,3,4\}$ y $B = \{3,4,5,6,7\}$ dentro del espacio muestral $\Omega = \{1,2,\dots,10\}$. Enumerando explícitamente cada conjunto:
$$A^c = \{5,6,7,8,9,10\}, \quad B^c = \{1,2,8,9,10\}$$
$$(A \cup B)^c = \Omega \setminus \{1,2,3,4,5,6,7\} = \boxed{\{8,9,10\}}$$
$$A^c \cap B^c = \{5,6,7,8,9,10\} \cap \{1,2,8,9,10\} = \boxed{\{8,9,10\}}$$
Ambos conjuntos coinciden elemento a elemento, verificando numéricamente $(A \cup B)^c = A^c \cap B^c$ sobre este espacio muestral discreto.

```python
## Verificacion de la Primera Ley de De Morgan con conteo explicito de sensores
omega = set(range(1, 11))  # 10 sensores nanoelectronicos de gas

A = {1, 2, 3, 4}       # sensores que fallan por deriva de linea base
B = {3, 4, 5, 6, 7}    # sensores que fallan por saturacion

A_c = omega - A
B_c = omega - B

complemento_union = omega - (A | B)
interseccion_complementos = A_c & B_c

primera_ley_de_morgan = complemento_union == interseccion_complementos

print(f"(A U B)^c = {complemento_union}")
print(f"A^c ∩ B^c = {interseccion_complementos}")
print(f"¿Se cumple (A U B)^c = A^c ∩ B^c?: {primera_ley_de_morgan}")
```

### 1.3 Axiomas de Kolmogorov
Dado un espacio muestral $\Omega$, una función de probabilidad $P: \mathcal{F} \rightarrow [0, 1]$ asigna a cada evento $A$ un número real sujeto a tres axiomas universales:

1. **Axioma de No-Negatividad**: $P(A) \ge 0$ para todo evento $A$.
2. **Axioma de Normalización**: $P(\Omega) = 1$.
3. **Axioma de Aditividad Contable**: Si $A_1, A_2, A_3, \dots$ es una secuencia de eventos mutuamente excluyentes ($A_i \cap A_j = \emptyset$ para todo $i \neq j$), entonces:
$$P\left( \bigcup_{i=1}^\infty A_i \right) = \sum_{i=1}^\infty P(A_i)$$

Propiedades fundamentales derivadas:
* $P(\emptyset) = 0$
* $P(A^c) = 1 - P(A)$
* Regla General de la Adición: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$

**Ejemplo verificando los 3 Axiomas de Kolmogorov**: un lote de nanopartículas de oro (AuNPs) se clasifica, según el diámetro medido por microscopía electrónica de transmisión (TEM), en tres categorías mutuamente excluyentes: pequeña ($<10\text{ nm}$), mediana ($10$–$20\text{ nm}$) y grande ($>20\text{ nm}$), con probabilidades asignadas $P(\text{pequeña})=0.25$, $P(\text{mediana})=0.45$, $P(\text{grande})=0.30$.
* **Axioma 1 (no-negatividad)**: las tres probabilidades son $\ge 0$.
* **Axioma 2 (normalización)**: $0.25 + 0.45 + 0.30 = \boxed{1.0}$, es decir $P(\Omega)=1$.
* **Axioma 3 (aditividad)**: como "pequeña" y "mediana" son disjuntas, $P(\text{pequeña} \cup \text{mediana}) = P(\text{pequeña}) + P(\text{mediana}) = 0.25 + 0.45 = \boxed{0.70}$.

```python
## Verificacion de los 3 Axiomas de Kolmogorov sobre una clasificacion de AuNPs por tamano
espacio_muestral = {"pequena_menor_10nm": 0.25, "mediana_10_20nm": 0.45, "grande_mayor_20nm": 0.30}

## Axioma 1: no-negatividad
axioma_1_no_negatividad = all(p >= 0 for p in espacio_muestral.values())

## Axioma 2: normalizacion P(Omega) = 1
axioma_2_normalizacion = abs(sum(espacio_muestral.values()) - 1.0) < 1e-9

## Axioma 3: aditividad para eventos disjuntos (pequena U mediana)
p_union_disjunta = espacio_muestral["pequena_menor_10nm"] + espacio_muestral["mediana_10_20nm"]

print(f"Axioma 1 (no-negatividad): {axioma_1_no_negatividad}")
print(f"Axioma 2 (normalizacion), suma = {sum(espacio_muestral.values())}: {axioma_2_normalizacion}")
print(f"Axioma 3, P(pequena U mediana) = {p_union_disjunta}")
```

Esta unidad, como el resto del curso, sigue el **Ciclo de Verificación Triple** documentado en `GOVERNANCE.md`: Teoría → Verificación Simbólica (SymPy) → Solución Computacional (SciPy) → Interpretación. La Sección 5 desarrolla el ejemplo aplicado, la Sección 6 lo verifica simbólicamente, y la Sección 7 reproduce el resultado con las herramientas de producción.

---

## 2. Técnicas de Conteo y Combinatoria

Cuando los resultados de un espacio muestral finito $\Omega$ son equiprobables (regla de Laplace), el cálculo de probabilidades se reduce a contar el número de elementos en eventos y espacios muestrales:
$$P(A) = \frac{|A|}{|\Omega|}$$

**Ejemplo dedicado de la Regla de Laplace (conteo explícito de $|\Omega|$ y $|A|$)**: un lote contiene $15$ nanotubos de carbono indistinguibles al tacto: $9$ de pared simple (SWCNT) y $6$ de pared múltiple (MWCNT). Se selecciona una muestra de $3$ nanotubos al azar para inspección por microscopía. Sea $A$ el evento "los 3 nanotubos seleccionados son SWCNT".

Primero se cuenta el espacio muestral completo, **sin condicionar aún por tipo**: todas las formas de elegir $3$ nanotubos cualesquiera de los $15$ disponibles:
$$|\Omega| = \binom{15}{3} = \boxed{455}$$
Luego se cuenta el evento $A$ por separado: todas las formas de elegir $3$ SWCNT de los $9$ disponibles (sin tocar los MWCNT):
$$|A| = \binom{9}{3} = \boxed{84}$$
Solo ahora, con ambos conteos ya resueltos de forma independiente, se aplica la Regla de Laplace:
$$P(A) = \frac{|A|}{|\Omega|} = \frac{84}{455} \approx \boxed{0.1846}$$

```python
import math

## Regla de Laplace: conteo explicito de |Omega| y |A| antes de dividir
n_total = 15
n_swcnt = 9
n_muestra = 3

## Conteo de |Omega|: todas las formas de elegir 3 nanotubos cualesquiera de 15
omega_tamano = math.comb(n_total, n_muestra)

## Conteo de |A|: todas las formas de elegir 3 SWCNT de los 9 disponibles
A_tamano = math.comb(n_swcnt, n_muestra)

## Regla de Laplace
p_A = A_tamano / omega_tamano

print(f"|Omega| = C(15,3) = {omega_tamano}")
print(f"|A| = C(9,3) = {A_tamano}")
print(f"P(A) = |A|/|Omega| = {p_A:.4f}")
```

### 2.1 Principios Fundamentales
* **Principio Multiplicativo**: Si una operación consiste en $k$ pasos secuenciales con $n_1, n_2, \dots, n_k$ opciones respectivamente, el número total de formas es $n_1 \times n_2 \times \dots \times n_k$.
* **Principio Aditivo**: Si una alternativa se puede elegir de entre $k$ grupos disjuntos con $n_1, n_2, \dots, n_k$ opciones, el número total de alternativas es $n_1 + n_2 + \dots + n_k$.

### 2.2 Permutaciones
Una **permutación** es una ordenación de un conjunto de objetos donde **el orden sí importa**.

* **Permutación de $n$ objetos distintos**:
$$P(n) = n!$$

* **Permutación de $n$ objetos tomados de $r$ en $r$**:
$$P(n, r) = \frac{n!}{(n-r)!}$$

* **Permutaciones con repetición (multiset)**: Si hay $n_1$ objetos de tipo 1, $n_2$ de tipo 2, $\dots$, $n_k$ de tipo $k$:
$$P(n; n_1, n_2, \dots, n_k) = \frac{n!}{n_1! n_2! \dots n_k!}$$

### 2.3 Combinaciones
Una **combinación** es una selección de $r$ objetos de un conjunto de $n$ objetos donde **el orden no importa**.

$$\binom{n}{r} = C(n, r) = \frac{n!}{r!(n-r)!}$$

Propiedades del coeficiente binomial:
* $\binom{n}{0} = \binom{n}{n} = 1$
* $\binom{n}{r} = \binom{n}{n-r}$
* Teorema del Binomio: $(x + y)^n = \sum_{k=0}^n \binom{n}{k} x^{n-k} y^k$

**Ejemplo verificando el Teorema del Binomio**: un recubrimiento nanocompuesto se forma apilando $n=4$ capas, cada una elegida entre dos tipos de nanopartícula (tipo $X$: óxido de titanio, tipo $Y$: plata). Para verificar la identidad numéricamente (sin atarla a un conteo de capas específico), se evalúa $(x+y)^4$ con $x=2$, $y=3$ expandiendo término a término:
$$(x+y)^4 = \sum_{k=0}^4 \binom{4}{k} x^{4-k} y^k = \binom{4}{0}x^4 + \binom{4}{1}x^3y + \binom{4}{2}x^2y^2 + \binom{4}{3}xy^3 + \binom{4}{4}y^4$$
$$= 16 + 96 + 216 + 216 + 81 = \boxed{625}$$
Comparando contra el cálculo directo $(2+3)^4 = 5^4 = \boxed{625}$: ambos coinciden, confirmando la identidad término a término.

```python
import math

## Verificacion del Teorema del Binomio: expansion termino a termino vs calculo directo
n = 4
x, y = 2, 3

suma_binomio = sum(math.comb(n, k) * (x ** (n - k)) * (y ** k) for k in range(n + 1))
resultado_directo = (x + y) ** n

print(f"Suma de terminos binomiales: {suma_binomio}")
print(f"(x+y)^n calculado directo: {resultado_directo}")
print(f"¿Coinciden?: {suma_binomio == resultado_directo}")
```

### 2.4 Ejemplos Resueltos de Técnicas de Conteo Aplicadas a Nanotecnología
