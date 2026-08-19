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

### 8.2 Diccionario de Variables Nanotecnológicas
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

## Referencias

* Chan, S. H. (2021). *Introduction to Probability for Data Science*. Michigan Publishing. Capítulos sobre fundamentos de probabilidad, combinatoria y Teorema de Bayes.
* Virtanen, P. et al. (2020). SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. *Nature Methods*, 17, 261-272. Documentación: [docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html)

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
