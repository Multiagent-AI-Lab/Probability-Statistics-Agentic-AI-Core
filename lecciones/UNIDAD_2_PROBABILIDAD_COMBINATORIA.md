# UNIDAD 2: Probabilidad, Teoría de Conjuntos y Combinatoria

**Duración:** 2 semanas (12 horas)

**Curso:** Probabilidad y Estadística Inferencial

**Institución:** Universidad de la Ciénega del Estado de Michoacán de Ocampo (UCEMICH)

**Profesor:** Luis José Yudico Anaya

**Carrera:** Ingeniería en Nanotecnología

**Nivel:** Tercer Semestre

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Multiagent-AI-Lab/Probability-Statistics-Agentic-AI-Core/blob/master/notebooks/UNIDAD_2_PROBABILIDAD_COMBINATORIA.ipynb)

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

---

## 2. Técnicas de Conteo y Combinatoria

Cuando los resultados de un espacio muestral finito $\Omega$ son equiprobables (regla de Laplace), el cálculo de probabilidades se reduce a contar el número de elementos en eventos y espacios muestrales:
$$P(A) = \frac{|A|}{|\Omega|}$$

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

### 2.4 Ejemplos Resueltos de Técnicas de Conteo Aplicadas a Nanotecnología

Reconocer *cuál* técnica de conteo aplica a un problema dado es más difícil que ejecutar la fórmula una vez identificada. Los siguientes cuatro ejemplos cortos, cada uno con una técnica distinta, sirven de referencia rápida antes de enfrentar el banco de ejercicios de la Sección 9.

**Ejemplo A (Principio Multiplicativo — configuración binaria)**: Un arreglo de biosensores nanoelectrónicos tiene $8$ interruptores independientes, cada uno en estado ON/OFF. ¿Cuántas configuraciones distintas del arreglo son posibles?
$$\underbrace{2 \times 2 \times \cdots \times 2}_{8 \text{ veces}} = 2^8 = \boxed{256 \text{ configuraciones}}$$
Es un caso particular del principio multiplicativo donde los $8$ pasos tienen siempre $n_i = 2$ opciones — patrón que reaparece constantemente en el conteo de estados de sistemas binarios (bits de memoria, arreglos de sensores, rutas de un autómata).

**Ejemplo B (Principio Multiplicativo — material compuesto en capas)**: Un material nanocompuesto se fabrica apilando, en orden, una capa base (3 tipos de polímero disponibles), una capa intermedia (4 tipos de nanopartícula catalizadora) y una capa de recubrimiento (2 tipos de sellado). ¿Cuántos materiales distintos pueden ensamblarse?
$$3 \times 4 \times 2 = \boxed{24 \text{ materiales distintos}}$$
A diferencia del Ejemplo A, aquí cada paso tiene un número distinto de opciones ($n_1=3$, $n_2=4$, $n_3=2$) — la esencia del principio multiplicativo es que el número de pasos y de opciones por paso puede variar libremente, siempre que los pasos sean secuenciales e independientes entre sí.

**Ejemplo C (Combinación simple — selección sin orden)**: De un lote de $12$ nanopartículas de plata (AgNPs) sintetizadas, se seleccionan al azar $4$ para un ensayo de dispersión dinámica de luz (DLS). El orden en que se colocan en el equipo no afecta la medición. ¿Cuántas selecciones distintas de $4$ nanopartículas son posibles?
$$\binom{12}{4} = \frac{12!}{4! \, 8!} = \boxed{495 \text{ selecciones}}$$

**Ejemplo D (Combinación mixta — dos grupos disjuntos)**: Un laboratorio tiene $6$ nanotubos de carbono de pared simple (SWCNT) y $4$ de pared múltiple (MWCNT). Para un experimento se necesitan exactamente $2$ SWCNT y $1$ MWCNT. ¿De cuántas formas puede formarse el grupo experimental?

A diferencia del Ejemplo C (una sola combinación), aquí hay **dos decisiones independientes que se combinan multiplicativamente**: elegir el subgrupo de SWCNT y, por separado, el de MWCNT.
$$\binom{6}{2} \times \binom{4}{1} = 15 \times 4 = \boxed{60 \text{ grupos experimentales distintos}}$$
Este patrón —una combinación por cada grupo disjunto, multiplicadas entre sí— es la técnica que subyace a ejercicios donde el enunciado exige "exactamente $k_1$ de un tipo y $k_2$ de otro": se resuelve como combinaciones independientes conectadas por el principio multiplicativo, nunca como una sola combinación sobre el total combinado.

```python
import math

## Ejemplo A: configuraciones binarias de un arreglo de biosensores
n_interruptores = 8
configuraciones = 2 ** n_interruptores

## Ejemplo B: material compuesto en 3 capas con distinto número de opciones
opciones_capa_base, opciones_capa_intermedia, opciones_capa_sellado = 3, 4, 2
materiales_distintos = opciones_capa_base * opciones_capa_intermedia * opciones_capa_sellado

## Ejemplo C: combinación simple para ensayo DLS
seleccion_agnps = math.comb(12, 4)

## Ejemplo D: combinación mixta de dos grupos disjuntos (SWCNT y MWCNT)
grupos_swcnt = math.comb(6, 2)
grupos_mwcnt = math.comb(4, 1)
grupos_experimentales = grupos_swcnt * grupos_mwcnt

print(f"Ejemplo A — Configuraciones del arreglo de biosensores: {configuraciones}")
print(f"Ejemplo B — Materiales nanocompuestos distintos: {materiales_distintos}")
print(f"Ejemplo C — Selecciones de 4 AgNPs de un lote de 12: {seleccion_agnps}")
print(f"Ejemplo D — Grupos experimentales (2 SWCNT y 1 MWCNT): {grupos_experimentales}")
```

---

## 3. Probabilidad Condicional e Independencia

### 3.1 Probabilidad Condicional
La **probabilidad condicional** $P(A|B)$ mide la probabilidad de que ocurra el evento $A$ sabiendo con certeza que el evento $B$ ha ocurrido ($P(B) > 0$):

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

Regla General del Producto:
$$P(A \cap B) = P(B) \cdot P(A|B) = P(A) \cdot P(B|A)$$

### 3.2 Eventos Independientes
Dos eventos $A$ y $B$ son **estocásticamente independientes** si y solo si la ocurrencia de uno no altera la probabilidad del otro:

$$P(A|B) = P(A) \quad \iff \quad P(A \cap B) = P(A) \cdot P(B)$$

> ⚠️ **Distinción Crítica**: Eventos mutuamente excluyentes ($A \cap B = \emptyset$) NO son independientes si $P(A)>0$ y $P(B)>0$, ya que la ocurrencia de uno imposibilita por completo la ocurrencia del otro ($P(A|B) = 0 \neq P(A)$).

### 3.3 Ejemplos Resueltos: Despejar la Intersección y Verificar Independencia

**Ejemplo E (despejar $P(A\cap B)$ desde una condicional dada)**: en un control de calidad de nanotransistores, el $40\%$ de las obleas provienen de la Máquina A ($P(M)=0.40$), y de esas, el $80\%$ pasa la prueba de continuidad eléctrica ($P(\text{Apta}|M)=0.80$). Se sabe además que, considerando toda la producción (ambas máquinas), el $60\%$ de las obleas son aptas ($P(\text{Apta})=0.60$). ¿Cuál es la probabilidad de que una oblea apta haya salido de la Máquina A, $P(M|\text{Apta})$?

El dato $P(\text{Apta}|M)$ no puede aplicarse directamente en Bayes sin antes obtener la intersección:
$$P(M \cap \text{Apta}) = P(M) \cdot P(\text{Apta}|M) = 0.40 \times 0.80 = 0.32$$
$$P(M|\text{Apta}) = \frac{P(M \cap \text{Apta})}{P(\text{Apta})} = \frac{0.32}{0.60} = \frac{8}{15} \approx \boxed{0.5333}$$
Esta técnica —despejar primero la intersección con la Regla General del Producto (§3.1) antes de invocar Bayes— es la que con más frecuencia se olvida al enfrentar un problema donde el enunciado da $P(B|A)$ y $P(B)$ pero pide $P(A|B)$.

**Ejemplo F (contraejemplo de NO independencia — falacia de la intuición)**: un laboratorio tiene dos monedas usadas para asignar aleatoriamente muestras a un grupo de control: una moneda justa ($P(\text{Cara})=0.5$) y una moneda cargada ($P(\text{Cara})=0.7$), elegida cada una con probabilidad $0.5$ al inicio del experimento. Sea $A$ = "se usó la moneda cargada" y $B$ = "el primer lanzamiento fue cara". ¿Son $A$ y $B$ independientes?

Por el Teorema de la Probabilidad Total (§4.1, adelantando su uso):
$$P(B) = P(B|A)P(A) + P(B|A^c)P(A^c) = (0.7)(0.5) + (0.5)(0.5) = 0.60$$
Comparando $P(B|A) = 0.70$ contra $P(B) = 0.60$: **no son iguales**, por lo tanto $A$ y $B$ **no son independientes** — saber que salió cara sí actualiza la creencia sobre qué moneda se usó (de hecho, es exactamente el mecanismo detrás del Teorema de Bayes: si no hubiera dependencia entre el origen y el resultado, condicionar no aportaría ninguna información). Este contraejemplo es útil para evitar el error inverso al de "Distinción Crítica" de arriba: así como excluyentes no implica independiente, tampoco toda situación que *parece* simétrica es independiente — hay que verificar la igualdad $P(B|A)=P(B)$ explícitamente, nunca asumirla.

```python
## Ejemplo E: despejar la interseccion antes de aplicar Bayes
p_maquina_a = 0.40
p_apta_dado_a = 0.80
p_apta_total = 0.60

interseccion_a_apta = p_maquina_a * p_apta_dado_a
p_a_dado_apta = interseccion_a_apta / p_apta_total

## Ejemplo F: contraejemplo de NO independencia (monedas justa vs cargada)
p_moneda_cargada = 0.5
p_cara_dado_cargada = 0.7
p_cara_dado_justa = 0.5

p_cara_total = p_cara_dado_cargada * p_moneda_cargada + p_cara_dado_justa * (1 - p_moneda_cargada)
son_independientes = abs(p_cara_dado_cargada - p_cara_total) < 1e-9

print(f"Ejemplo E — P(Maquina A | Apta) = {p_a_dado_apta:.4f}")
print(f"Ejemplo F — P(Cara) marginal = {p_cara_total:.4f} vs P(Cara | Cargada) = {p_cara_dado_cargada:.4f}")
print(f"Ejemplo F — ¿A y B independientes?: {son_independientes}")
```

---

## 4. Teorema de la Probabilidad Total y Teorema de Bayes

### 4.1 Teorema de la Probabilidad Total
Sea $A_1, A_2, \dots, A_k$ una **partición** del espacio muestral $\Omega$ (eventos mutuamente excluyentes cuya unión es $\Omega$), con $P(A_i) > 0$. Para cualquier evento $B \subseteq \Omega$:

$$P(B) = \sum_{i=1}^k P(B \cap A_i) = \sum_{i=1}^k P(B|A_i) P(A_i)$$

### 4.2 Teorema de Bayes
Bajo la misma partición $A_1, A_2, \dots, A_k$, la probabilidad a posteriori del evento causa $A_j$ dada la evidencia observada $B$ es:

$$\boxed{P(A_j|B) = \frac{P(B|A_j) P(A_j)}{\sum_{i=1}^k P(B|A_i) P(A_i)}}$$

* $P(A_j)$: Probabilidad **a priori** de la hipótesis $A_j$.
* $P(B|A_j)$: **Verosimilitud** (Likelihood) de observar la evidencia $B$ bajo $A_j$.
* $P(B)$: Probabilidad marginal o **factor de normalización** de la evidencia.
* $P(A_j|B)$: Probabilidad **a posteriori** actualizada.

---

## 5. Ejemplo Analítico Paso a Paso: Clasificación Nanotecnológica de Nanopartículas

### 5.1 Contexto Aplicado en Nanotecnología
En una línea de síntesis coloidal de nanopartículas de oro (AuNPs) utilizadas para diagnóstico de biomarcadores tumorales, tres reactores químicos ($R_1$, $R_2$, $R_3$) producen el total de la producción diaria de la planta. El reactor $R_1$ sintetiza el $45\%$ de las nanopartículas, el reactor $R_2$ sintetiza el $35\%$ y el reactor $R_3$ produce el $20\%$ restante. 

Debido a ligeras variaciones de temperatura en las camisas de calefacción, el porcentaje de nanopartículas fuera de especificación de tamaño (diámetro fuera del rango óptimo de $15 \pm 2\text{ nm}$, presentando agregación coloidal) varía según el reactor de origen:
* El reactor $R_1$ produce un $4\%$ de nanopartículas defectuosas.
* El reactor $R_2$ produce un $2\%$ de nanopartículas defectuosas.
* El reactor $R_3$ produce un $8\%$ de nanopartículas defectuosas.

Si los ingenieros en nanotecnología toman una nanopartícula al azar del lote unificado al final de la jornada y, mediante microscopía electrónica de transmisión (TEM), confirman que la nanopartícula está **defectuosa** ($D$), determine la probabilidad a posteriori de que dicha nanopartícula haya sido sintetizada específicamente por el reactor $R_3$.

### 5.2 Paso 1: Definición de Eventos y Probabilidades a Priori
Sea la partición por reactores $R_1, R_2, R_3$:
$$P(R_1) = 0.45, \quad P(R_2) = 0.35, \quad P(R_3) = 0.20$$
Nótese que $P(R_1) + P(R_2) + P(R_3) = 0.45 + 0.35 + 0.20 = 1.0$.

Sea $D$ el evento: "La nanopartícula está defectuosa (fuera de especificación)".
Las verosimilitudes condicionales de defecto por reactor son:
$$P(D|R_1) = 0.04, \quad P(D|R_2) = 0.02, \quad P(D|R_3) = 0.08$$

### 5.3 Paso 2: Cálculo de la Probabilidad Total de Defecto $P(D)$
Aplicando el Teorema de la Probabilidad Total:
$$P(D) = P(D|R_1)P(R_1) + P(D|R_2)P(R_2) + P(D|R_3)P(R_3)$$
$$P(D) = (0.04 \times 0.45) + (0.02 \times 0.35) + (0.08 \times 0.20)$$
$$P(D) = 0.0180 + 0.0070 + 0.0160 = 0.0410 \quad (4.1\%)$$

### 5.4 Paso 3: Aplicación del Teorema de Bayes para $P(R_3|D)$
$$\boxed{P(R_3|D) = \frac{P(D|R_3)P(R_3)}{P(D)} = \frac{0.08 \times 0.20}{0.0410} = \frac{0.0160}{0.0410} = \frac{16}{41} \approx 0.39024}$$

**Interpretación**: Aunque el reactor $R_3$ solo sintetiza el $20\%$ del volumen total de nanopartículas, si descubrimos que una nanopartícula está defectuosa, la probabilidad de que provenga de $R_3$ se duplica casi al $39.02\%$ debido a su mayor tasa individual de defectos ($8\%$).

### 5.5 Prueba Unitaria con pytest

Antes de reportar $P(R_3|D)\approx 0.39$ como resultado final, se verifica computacionalmente cada paso de la derivación — la partición de probabilidades a priori, la probabilidad total y el propio Teorema de Bayes — para blindar el cálculo contra errores de álgebra o de redondeo manual:

```python
import ipytest
import pytest

ipytest.autoconfig()

p_r1, p_r2, p_r3 = 0.45, 0.35, 0.20
p_d_dado_r1, p_d_dado_r2, p_d_dado_r3 = 0.04, 0.02, 0.08


def test_las_probabilidades_a_priori_de_los_reactores_suman_uno():
    assert (p_r1 + p_r2 + p_r3) == pytest.approx(1.0)


def test_probabilidad_total_de_defecto():
    p_d = p_d_dado_r1 * p_r1 + p_d_dado_r2 * p_r2 + p_d_dado_r3 * p_r3
    assert p_d == pytest.approx(0.041, rel=1e-6)


def test_teorema_de_bayes_para_r3_dado_defecto():
    p_d = p_d_dado_r1 * p_r1 + p_d_dado_r2 * p_r2 + p_d_dado_r3 * p_r3
    p_r3_dado_d = (p_d_dado_r3 * p_r3) / p_d
    assert p_r3_dado_d == pytest.approx(16 / 41, rel=1e-6)


def test_posterior_de_r3_es_mayor_que_su_prior_por_su_alta_tasa_de_defecto():
    ## R3 duplica su probabilidad al condicionar en "defectuosa": esto NO
    ## ocurriria si su tasa de defecto fuera igual al promedio del lote.
    p_d = p_d_dado_r1 * p_r1 + p_d_dado_r2 * p_r2 + p_d_dado_r3 * p_r3
    p_r3_dado_d = (p_d_dado_r3 * p_r3) / p_d
    assert p_r3_dado_d > p_r3


ipytest.run("-vv")
```

---

## 5.6 Estudio de Caso: El Problema de los Tres Prisioneros

El ejemplo de los reactores (Sección 5) resuelve Bayes en un caso donde la intuición y el cálculo coinciden. El siguiente caso clásico —isomorfo al problema de Monty Hall— es célebre precisamente porque la intuición falla: sirve para poner a prueba si el Teorema de Bayes se aplicó por comprensión o solo por sustitución mecánica en una fórmula.

**Planteamiento**: tres prisioneros, $A$, $B$ y $C$, esperan sentencia. Se sabe que exactamente uno de los tres será indultado (liberado) y los otros dos ejecutados, con probabilidad uniforme a priori:
$$P(A) = P(B) = P(C) = \frac{1}{3}$$
El prisionero $A$ le pide al guardia (que conoce el resultado, pero no puede revelárselo directamente a $A$) que le diga el nombre de **uno de los otros dos** ($B$ o $C$) que será ejecutado con certeza. El guardia responde: "$B$ será ejecutado". La pregunta es: ¿cambia esta información la probabilidad de que $A$ sea el indultado?

**Solución vía Bayes**: sea $G_B$ el evento "el guardia dice que $B$ será ejecutado". Las verosimilitudes dependen de la regla que sigue el guardia cuando tiene más de una opción válida (si $A$ es el indultado, el guardia puede decir "$B$" o "$C$" con igual probabilidad, por simetría):

$$P(G_B|A) = \frac{1}{2}, \qquad P(G_B|B) = 0, \qquad P(G_B|C) = 1$$

Nótese que estas dos últimas verosimilitudes son valores extremos (0 y 1), no intermedios: si $B$ fuera el indultado, el guardia jamás diría "$B$ será ejecutado" (sería falso); si $C$ fuera el indultado, el guardia está obligado a decir "$B$" porque es la única opción de ejecutado que no es $A$.

Aplicando el Teorema de la Probabilidad Total (§4.1):
$$P(G_B) = P(G_B|A)P(A) + P(G_B|B)P(B) + P(G_B|C)P(C) = \left(\frac{1}{2}\right)\left(\frac{1}{3}\right) + (0)\left(\frac{1}{3}\right) + (1)\left(\frac{1}{3}\right) = \frac{1}{6} + \frac{1}{3} = \frac{1}{2}$$

Y aplicando Bayes (§4.2) para cada hipótesis:
$$P(A|G_B) = \frac{P(G_B|A)P(A)}{P(G_B)} = \frac{(1/2)(1/3)}{1/2} = \frac{1}{3} \qquad P(C|G_B) = \frac{P(G_B|C)P(C)}{P(G_B)} = \frac{(1)(1/3)}{1/2} = \frac{2}{3}$$

$$\boxed{P(A|G_B) = \frac{1}{3} \text{ (no cambia)}, \qquad P(C|G_B) = \frac{2}{3} \text{ (se duplica)}}$$

**Interpretación**: la información del guardia **no cambia** la probabilidad de que $A$ sea el indultado —sigue siendo $1/3$, igual que antes de preguntar—, pero **sí concentra** la probabilidad restante casi por completo sobre $C$ ($2/3$), en vez de repartirla equitativamente entre $B$ (que ya se descartó, $P=0$) y $C$. La falacia intuitiva más común es asumir que, al eliminar a $B$ como opción, la probabilidad se reparte $50/50$ entre $A$ y $C$ — esto ignora que la respuesta del guardia no es una elección al azar entre los dos no-$A$, sino una elección **forzada** cuando $C$ es el indultado ($P(G_B|C)=1$) y solo parcialmente libre cuando $A$ lo es ($P(G_B|A)=1/2$). Esa asimetría en la verosimilitud, no en el prior, es lo que rompe la simetría aparente del resultado.

**Pregunta de reflexión**: ¿por qué el resultado sería diferente si, en cambio de pedirle al guardia que nombre a un ejecutado, $A$ pudiera *ver* directamente si $B$ fue ejecutado por una causa totalmente ajena (por ejemplo, un evento aleatorio independiente del indulto)? Piensa en qué verosimilitud $P(\text{evidencia}|A)$, $P(\text{evidencia}|B)$, $P(\text{evidencia}|C)$ correspondería a ese escenario alternativo, y si seguiría siendo asimétrica de la misma forma.

```python
## Verificacion del Problema de los Tres Prisioneros
p_a, p_b, p_c = 1/3, 1/3, 1/3

## Verosimilitudes de que el guardia diga "B sera ejecutado"
p_gb_dado_a = 1/2  ## A es el indultado: el guardia elige entre B y C al azar
p_gb_dado_b = 0    ## B es el indultado: el guardia nunca diria que B sera ejecutado
p_gb_dado_c = 1    ## C es el indultado: el guardia esta obligado a decir "B"

p_gb = p_gb_dado_a * p_a + p_gb_dado_b * p_b + p_gb_dado_c * p_c

p_a_dado_gb = (p_gb_dado_a * p_a) / p_gb
p_c_dado_gb = (p_gb_dado_c * p_c) / p_gb

print(f"P(G_B) = {p_gb:.4f}")
print(f"P(A | G_B) = {p_a_dado_gb:.4f}  (antes de preguntar: {p_a:.4f}, no cambia)")
print(f"P(C | G_B) = {p_c_dado_gb:.4f}  (antes de preguntar: {p_c:.4f}, se duplica)")
```

---

## 6. Código de Verificación Simbólica (SymPy)

```python
import sympy as sp
from IPython.display import display, Math

## 1. Definición de variables simbólicas para prioris y verosimilitudes
p_r1, p_r2, p_r3 = sp.symbols('P(R1) P(R2) P(R3)', real=True, positive=True)
p_d_r1, p_d_r2, p_d_r3 = sp.symbols('P(D|R1) P(D|R2) P(D|R3)', real=True, positive=True)

## 2. Expresión simbólica de la Probabilidad Total P(D)
p_d_total = p_d_r1 * p_r1 + p_d_r2 * p_r2 + p_d_r3 * p_r3

## 3. Expresión simbólica del Teorema de Bayes para P(R3|D)
p_r3_d = (p_d_r3 * p_r3) / p_d_total

display(Math(fr"\text{{Teorema de Bayes Simbólico: }} P(R_3|D) = {sp.latex(p_r3_d)}"))

## 4. Sustitución de valores numéricos de la síntesis de nanopartículas
valores = {
    p_r1: sp.Rational(45, 100),
    p_r2: sp.Rational(35, 100),
    p_r3: sp.Rational(20, 100),
    p_d_r1: sp.Rational(4, 100),
    p_d_r2: sp.Rational(2, 100),
    p_d_r3: sp.Rational(8, 100)
}

resultado_exacto = p_r3_d.subs(valores)
resultado_decimal = float(resultado_exacto)

print(f"Resultado exacto en fracción: {resultado_exacto}")
print(f"Resultado numérico decimal: {resultado_decimal:.5f}")
```

---

## 7. Solución Computacional en Python (SciPy & Statsmodels)

```python
import math
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## Configuración visual
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)

## --- PARTE A: Combinatoria y Probabilidad Clásica ---
n_lote = 20
r_muestra = 5
total_combinaciones = math.comb(n_lote, r_muestra)
total_permutaciones = math.perm(n_lote, r_muestra)

print(f"Combinaciones C(20, 5) para seleccionar nanopartículas: {total_combinaciones}")
print(f"Permutaciones P(20, 5) considerando orden de medición: {total_permutaciones}")

## --- PARTE B: Simulación Monte Carlo del Teorema de Bayes ---
N_simulaciones = 1_000_000

## Asignación de reactores según prioris: R1=0, R2=1, R3=2
reactores = np.random.choice([1, 2, 3], size=N_simulaciones, p=[0.45, 0.35, 0.20])

## Generación de defectos según verosimilitud de cada reactor
prob_defecto_segun_reactor = np.where(reactores == 1, 0.04,
                              np.where(reactores == 2, 0.02, 0.08))

defectuosas = np.random.rand(N_simulaciones) < prob_defecto_segun_reactor

## Filtrado Bayesiano: Condicionar a las nanopartículas que resultaron defectuosas
solo_defectuosas = reactores[defectuosas]

p_r1_d_sim = np.mean(solo_defectuosas == 1)
p_r2_d_sim = np.mean(solo_defectuosas == 2)
p_r3_d_sim = np.mean(solo_defectuosas == 3)

print("\n--- RESULTADOS SIMULACIÓN MONTE CARLO (1,000,000 partículas) ---")
print(f"P(R1|D) Simulado: {p_r1_d_sim:.5f} | Teórico: {0.0180/0.0410:.5f}")
print(f"P(R2|D) Simulado: {p_r2_d_sim:.5f} | Teórico: {0.0070/0.0410:.5f}")
print(f"P(R3|D) Simulado: {p_r3_d_sim:.5f} | Teórico: {0.0160/0.0410:.5f}")

## --- PARTE C: Visualización Profesional ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

## Gráfico 1: Comparación Prior vs. Posterior
df_bayes = pd.DataFrame({
    'Reactor': ['Reactor 1', 'Reactor 2', 'Reactor 3'],
    'Prior P(R_i)': [0.45, 0.35, 0.20],
    'Posterior P(R_i|D)': [0.0180/0.0410, 0.0070/0.0410, 0.0160/0.0410]
})

df_melted = df_bayes.melt(id_vars='Reactor', var_name='Tipo Probabilidad', value_name='Probabilidad')
sns.barplot(data=df_melted, x='Reactor', y='Probabilidad', hue='Tipo Probabilidad', palette='magma', ax=axes[0])
axes[0].set_title("Actualización de Probabilidades: Prior vs. Posterior (Bayes)", fontsize=12, fontweight='bold')
axes[0].set_ylabel("Probabilidad")

## Gráfico 2: Simulación de Convergencia Monte Carlo
pasos_sim = np.linspace(1000, N_simulaciones, 100, dtype=int)
convergencia_r3 = [np.mean(solo_defectuosas[:n] == 3) for n in pasos_sim if n <= len(solo_defectuosas)]
pasos_validos = pasos_sim[:len(convergencia_r3)]

axes[1].plot(pasos_validos, convergencia_r3, color='crimson', label='Monte Carlo P(R3|D)', linewidth=2)
axes[1].axhline(y=16/41, color='black', linestyle='--', label=f'Teórico (16/41 ≈ {16/41:.4f})')
axes[1].set_title("Convergencia Estocástica de P(R3|D) por Ley de Grandes Números", fontsize=12, fontweight='bold')
axes[1].set_xlabel("Número de Nanopartículas Defectuosas Evaluadas")
axes[1].set_ylabel("Frecuencia Relativa P(R3|D)")
axes[1].legend()

plt.tight_layout()
plt.show()
```

---

## 8. Interpretación Post-Gráfico & Diccionario de Variables

### 8.1 Interpretación de Resultados Computacionales
1. **Actualización Bayesiana de Creencias**: En el gráfico de barra comparativo se aprecia el efecto directo del Teorema de Bayes. Aunque el **Reactor 1** dominaba la producción a priori con un $45\%$, su baja tasa de defectos ($4\%$) reduce su responsabilidad a posteriori al $43.9\%$. Por el contrario, el **Reactor 3**, que solo producía el $20\%$ de las nanopartículas, pasa a representar casi el $39.02\%$ de todas las piezas defectuosas debido a su alta tasa de falla ($8\%$).
2. **Convergencia Monte Carlo**: El segundo gráfico demuestra empíricamente la Ley de los Grandes Números. Al incrementar el tamaño muestral de la simulación hacia $1,000,000$ de ensayos, la frecuencia relativa simulada converge con precisión de tres decimales hacia el valor teórico de $\frac{16}{41} \approx 0.39024$.

### 8.2 Diccionario de Variables de la Unidad

Notación general introducida en las Secciones 1-4 y 5.6, independiente del ejemplo aplicado específico:

* $\mathcal{E}$: experimento aleatorio.
* $\Omega$: espacio muestral (conjunto de todos los resultados posibles).
* $A, B \subseteq \Omega$: eventos o sucesos (subconjuntos del espacio muestral).
* $A \cup B$: unión de eventos (ocurre al menos uno).
* $A \cap B$: intersección de eventos (ocurren ambos).
* $A^c$ o $\bar{A}$: complemento de un evento.
* $\emptyset$: evento imposible o conjunto vacío.
* $P: \mathcal{F} \rightarrow [0,1]$: función de probabilidad definida sobre los eventos.
* $P(A)$: probabilidad del evento $A$.
* $n!$: factorial de $n$, número de permutaciones de $n$ objetos distintos.
* $P(n)$: permutaciones de $n$ objetos distintos.
* $P(n, r)$: permutaciones de $n$ objetos tomados de $r$ en $r$.
* $P(n; n_1, n_2, \dots, n_k)$: permutaciones con repetición (multiset) de $n$ objetos agrupados en $k$ tipos.
* $\binom{n}{r}$ o $C(n, r)$: combinaciones de $n$ objetos tomados de $r$ en $r$ (el orden no importa).
* $P(A|B)$: probabilidad condicional de $A$ dado que ocurrió $B$.
* $A_1, A_2, \dots, A_k$: partición del espacio muestral $\Omega$ (eventos mutuamente excluyentes cuya unión es $\Omega$).
* $P(A_j)$: probabilidad a priori de la hipótesis o causa $A_j$.
* $P(B|A_j)$: verosimilitud (likelihood) de observar la evidencia $B$ bajo la hipótesis $A_j$.
* $P(A_j|B)$: probabilidad a posteriori de $A_j$ dada la evidencia $B$ (Teorema de Bayes).

### 8.3 Diccionario de Variables Nanotecnológicas del Ejemplo Aplicado
* $R_1, R_2, R_3$: Eventos que representan el reactor químico de síntesis coloidal de origen.
* $D$: Evento binario que indica si una nanopartícula se encuentra defectuosa (fuera del rango de tamaño óptimo $15 \pm 2\text{ nm}$).
* $P(R_i)$: Probabilidad a priori de selección de una nanopartícula del reactor $i$.
* $P(D|R_i)$: Verosimilitud de falla por imperfección térmica en el reactor $i$.
* $P(R_i|D)$: Probabilidad a posteriori inferida mediante diagnóstico microscópico TEM.

## Errores Comunes / Misconceptions

* **Error**: Calcular $P(A \cap B) = P(A) \times P(B)$ sin verificar que $A$ y $B$ sean independientes.
  **Correcto**: la regla del producto simple solo aplica bajo independencia; en general $P(A \cap B) = P(A) \times P(B|A)$. Confundirlas subestima o sobrestima sistemáticamente la probabilidad conjunta cuando existe dependencia real entre eventos.

* **Error**: Al aplicar el Teorema de Bayes, invertir $P(A|B)$ con $P(B|A)$ asumiendo que son iguales o intercambiables.
  **Correcto**: $P(A|B) = \dfrac{P(B|A)\,P(A)}{P(B)}$ — ambas cantidades solo coinciden cuando $P(A) = P(B)$. Ignorar la probabilidad a priori $P(A)$ (el "prior") es el error clásico de razonamiento bayesiano conocido como *base rate fallacy*.

* **Error**: Tratar "eventos mutuamente excluyentes" y "eventos independientes" como sinónimos o como conceptos compatibles en el caso general.
  **Correcto**: si $A$ y $B$ son mutuamente excluyentes ($A \cap B = \emptyset$) y ambos tienen probabilidad positiva, entonces necesariamente son dependientes, porque $P(A \cap B) = 0 \neq P(A)\,P(B)$. Son propiedades distintas que rara vez coexisten.

* **Error**: Asumir que, al descartar una de $k$ opciones igualmente probables mediante evidencia adicional, la probabilidad restante se reparte equitativamente entre las opciones sobrevivientes (falacia del "50/50 automático").
  **Correcto**: como demuestra el Problema de los Tres Prisioneros (§5.6), la forma en que se genera la evidencia determina cómo se redistribuye la probabilidad — si la evidencia es más probable bajo una hipótesis que bajo otra ($P(G_B|C)=1$ vs. $P(G_B|A)=1/2$), la redistribución es asimétrica. Repartir siempre por igual ignora la verosimilitud de la evidencia bajo cada hipótesis.

## Ejercicio Propuesto

Una planta de síntesis de puntos cuánticos (Quantum Dots, QDs) de CdSe produce su lote diario en tres líneas de reacción, $L_1$, $L_2$ y $L_3$, con las siguientes proporciones de producción y tasas de defecto (fuera de especificación de emisión fotoluminiscente):

| Línea | Proporción de producción $P(L_i)$ | Tasa de defecto $P(D\mid L_i)$ |
|:---:|:---:|:---:|
| $L_1$ | $0.50$ | $0.03$ |
| $L_2$ | $0.30$ | $0.06$ |
| $L_3$ | $0.20$ | $0.10$ |

1. Calcula la probabilidad total $P(D)$ de que un QD elegido al azar del lote unificado sea defectuoso.
2. Aplica el Teorema de Bayes para calcular $P(L_2 \mid D)$ y $P(L_3 \mid D)$.
3. De un lote de 15 QDs, ¿cuántas combinaciones distintas de 4 QDs pueden seleccionarse para control de calidad ($C(15,4)$)?

Escribe tu solución en una celda de código nueva en tu notebook. La celda de autoevaluación de la siguiente sección verificará tu resultado.

### Ejercicios Adicionales de Práctica

Los siguientes tres ejercicios no forman parte del Ejercicio Propuesto que verifica la Autoevaluación, pero se recomienda resolverlos como práctica adicional antes de continuar a la Unidad 3:

1. **(Regla de la Cadena con 3+ eventos)** De un mazo de $52$ cartas se extraen $3$ cartas **sin reemplazo**. ¿Cuál es la probabilidad de que las tres sean figuras (J, Q o K)? Generaliza la Regla General del Producto de la Sección 3.1 (que solo cubre 2 eventos) a tres eventos encadenados:
   $$P(A_1 \cap A_2 \cap A_3) = P(A_1) \cdot P(A_2|A_1) \cdot P(A_3|A_1 \cap A_2)$$
   donde cada factor refleja que el mazo tiene una carta menos, y una figura menos, tras cada extracción.

2. **(Independencia con/sin reemplazo)** Una urna de control de calidad contiene $6$ canicas que representan nanopartículas conformes y $4$ que representan nanopartículas defectuosas. Se extraen dos canicas. Calcula $P(\text{ambas conformes})$ en dos escenarios: (a) con reemplazo, (b) sin reemplazo. ¿En cuál de los dos escenarios las extracciones son eventos independientes? Justifica en términos de si $P(\text{2da conforme} \mid \text{1ra conforme})$ cambia respecto a $P(\text{2da conforme})$.

3. **(Partición de tres categorías, nanotecnología)** Un laboratorio de síntesis de nanopartículas lipídicas para liberación de fármacos produce partículas con carga superficial positiva ($40\%$), negativa ($35\%$) o neutra ($25\%$), medida por potencial zeta. La tasa de agregación no deseada (formación de agregados que invalidan el lote) es del $12\%$ para carga positiva, $5\%$ para carga negativa y $20\%$ para carga neutra. Si una nanopartícula elegida al azar del lote unificado presenta agregación, calcula la probabilidad de que su carga superficial haya sido neutra. Compara la estructura de este ejercicio con el ejemplo de los reactores de la Sección 5 — es la misma técnica (partición de 3 categorías + Bayes) aplicada a un dataset distinto.

## Referencias

* Chan, S. H. (2021). *Introduction to Probability for Data Science*. Michigan Publishing. Capítulos sobre fundamentos de probabilidad, combinatoria y Teorema de Bayes.
* Chien, C.-F., Hsu, S.-C. & Chen, Y.-J. (2023). Bayesian decision analysis for optimizing in-line metrology and defect inspection strategy for sustainable semiconductor manufacturing and an empirical study. *Computers & Industrial Engineering*, 186, 109421. DOI: [10.1016/j.cie.2023.109421](https://doi.org/10.1016/j.cie.2023.109421) — modelo de decisión bayesiano aplicado a inspección de defectos en manufactura de semiconductores, el mismo tipo de razonamiento (Bayes + priors por reactor) del ejemplo aplicado de esta unidad.
* Virtanen, P. et al. (2020). SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. *Nature Methods*, 17, 261-272. Documentación: [docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html)

## Herramientas de esta Unidad

**StatsTutorAgent** — resuelve tus dudas conceptuales sobre probabilidad y combinatoria citando el contenido exacto de esta unidad, y te hace una pregunta socrática si detecta un error conceptual común en vez de darte la respuesta directa:

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
            "⚠️ [Unidad 2] No se encontró el secreto GEMINI_API_KEY ni GOOGLE_API_KEY en Colab. "
            "Créalo en el ícono de llave 🔑 de la barra lateral izquierda para usar StatsTutorAgent."
        )

from src.multiagent_core.stats_tutor_agent import StatsTutorAgent

tutor = StatsTutorAgent(course_dir=Path("lecciones"))
print(tutor.ask("¿cuál es la diferencia entre una permutación y una combinación al contar arreglos?"))
```

No requiere configuración adicional más allá de tu `GEMINI_API_KEY` (créala en [aistudio.google.com/apikey](https://aistudio.google.com/apikey) y agrégala como secreto de Colab o variable de entorno local).

## Autoevaluación

Guarda tu solución al Ejercicio Propuesto en un archivo separado y evalúala contra el pipeline de auditoría del curso:

```python
%%writefile solucion_ejercicio_u2.py
# Completa aquí tu solución al Ejercicio Propuesto de esta unidad.
from math import comb

p_linea = {"L1": 0.50, "L2": 0.30, "L3": 0.20}
p_defecto_dado_linea = {"L1": 0.03, "L2": 0.06, "L3": 0.10}

# TODO: calcula la probabilidad total P(D) de que un QD elegido al azar sea defectuoso
# TODO: aplica el Teorema de Bayes para calcular P(L2 | D) y P(L3 | D)
# TODO: calcula C(15, 4), el número de combinaciones de 4 QDs de un lote de 15 para control de calidad
```

```python
from src.multiagent_core.code_auditor_agent import CodeAuditorAgent
from external_skills.pedagogy.socratic_debugger import SocraticDebugger

with open("solucion_ejercicio_u2.py", encoding="utf-8") as f:
    codigo_alumno = f.read()

auditor = CodeAuditorAgent()
resultado = auditor.audit_code(codigo_alumno)

if resultado["issues"] or resultado["metrics"]["has_security_risk"]:
    debugger = SocraticDebugger()
    for issue in resultado["issues"]:
        tipo_error = "syntax_error" if "SyntaxError" in issue else "generic"
        print("💡", debugger.generate_socratic_question(tipo_error, "Unidad 2"))
    for issue in resultado["security_issues"]:
        print("🔒", debugger.generate_socratic_question("security_risk", "Unidad 2"))
        print("   ", issue)
    print("\n--- Detalle técnico ---")
    print(resultado)
else:
    print("✅ Tu código pasa las verificaciones automáticas de estilo y seguridad.")
    print(resultado)
```
