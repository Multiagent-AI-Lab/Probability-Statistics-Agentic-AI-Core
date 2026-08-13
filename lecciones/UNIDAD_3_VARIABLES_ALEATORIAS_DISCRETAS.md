# UNIDAD 3: Variables Aleatorias Discretas y Distribuciones de Probabilidad
> **Asignatura: Probabilidad y Estadística Inferencial**
> **UCEMICH — Ingeniería en IA y Nanotecnología**
> **Autor y Profesor: Mtro. Luis José Yudico Anaya**

---

## 1. PROBABILIDAD Y ESTADISTICA

INGENIERÍA EN NANOTECNOLOGÍA

Universidad de La Cienega del Esatdo de MIchoacán de Ocampo

**Tema: Variables Aleatorias Discretas y Nanotecnología**

16/10/25

```python
import math
import numpy as np
import matplotlib.pyplot as plt

results = {}
```

## 1. Tema 1

```python
p1 = 0.98
# Varianza
var_X = p1 * (1 - p1)

# CDF (definida por tramos, se imprimirá en forma simbólica)
# PMF (k = 0,1)
k_X = np.array([0,1])
pmf_X = np.array([1-p1, p1])

# Gráfica PMF
plt.figure(figsize=(5,4))
plt.bar(k_X, pmf_X, width=0.4)
plt.xticks(k_X)
plt.xlabel('k (valor de X)')
plt.ylabel('P(X=k)')
plt.title('PMF: Bernoulli(p=0.98)')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()

print("Ejercicio 1 - Resultados numéricos:")
print(f" Varianza Var(X) = p(1-p) = {p1}*(1-{p1}) = {var_X:.5f}")
print(" CDF (F(x)) por tramos (X toma valores 0 y 1):")
print("  F(x) = 0             si x < 0")
print(f"  F(x) = P(X ≤ 0) = P(X=0) = {1-p1:.5f}    si 0 ≤ x < 1")
print("  F(x) = 1             si x ≥ 1")
print("\n\n")
```

Ejercicio 1 — Bernoulli
$$ X \sim Bernoulli(p = 0.98) $$
Varianza:
$$
Var(X) = p(1 - p) = 0.98 \cdot 0.02 = 0.01960.
$$
CDF $F(x)$ (por tramos, recordando que $X$ toma solo 0 o 1):

$$ F(x) = 0 $$ si $$ x < 0 $$

$$ F(x) = P(X \le 0) = P(X = 0) = 1 - p = 0.02 $$ si $$ 0 \le x < 1 $$

$$ F(x) = 1 $$ si $$ x \ge 1 $$

Gráfica: se generó la PMF con barras en \( k = 0, 1 \).

Interpretación: la varianza es pequeña $(\approx 0.0196)$, lo que refleja baja dispersión: la mayoría de celdas pasan la prueba (98%), y las desviaciones respecto a ese comportamiento son raras. En términos de fiabilidad, indica un proceso muy consistente; las fallas son poco frecuentes y poco variables.

## 2. Tema 2

```python
n2 = 15
p2 = 0.70

# Probabilidad P(Y=12)
k_target = 12
pmf_Y_12 = math.comb(n2, k_target) * (p2**k_target) * ((1-p2)**(n2 - k_target))

# Esperanza
E_Y = n2 * p2

# PMF para k = 0..n
k_Y = np.arange(0, n2+1)
pmf_Y = np.array([math.comb(n2, k) * (p2**k) * ((1-p2)**(n2-k)) for k in k_Y])

# Gráfica PMF
plt.figure(figsize=(8,4))
plt.bar(k_Y, pmf_Y, width=0.6)
plt.xticks(k_Y)
plt.xlabel('k (número de lotes exitosos)')
plt.ylabel('P(Y=k)')
plt.title(f'PMF: Binomial(n={n2}, p={p2})')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()

print("Ejercicio 2 - Resultados numéricos:")
print(f" P(Y=12) = {pmf_Y_12:.6f}")
print(f" Esperanza E[Y] = n p = {n2} * {p2} = {E_Y:.4f}")
print("\n\n")
```

Ejercicio 2 — Binomial
$ Y \sim \text{Binomial}(n = 15, p = 0.70) $
Probabilidad exacta:
$$
P(Y = 12) = \binom{15}{12} (0.7)^{12} (0.3)^3 \approx 0.170040.
$$

Esperanza:
$ E[Y] = np = 15 \cdot 0.7 = 10.5. $

Gráfica: se generó la PMF para $ k = 0, \ldots, 15 $.

Interpretación: si el químico repite el experimento muchas veces (múltiples días similares), en promedio obtendrá 10.5 lotes exitosos por experimento de 15 lotes — es decir, típicamente 10 o 11 lotes cumplirán el criterio. La esperanza describe el rendimiento esperado diario (media a largo plazo).

## 3. Tema 3

```python
p3 = 0.15

# P(Z > 4) = (1-p)^4  (soporte k=1,2,...)
P_Z_gt_4 = (1 - p3)**4

# Esperanza E[Z] = 1/p
E_Z = 1 / p3

# PMF para k = 1..15
k3_max = 15
k_Z = np.arange(1, k3_max+1)
pmf_Z = p3 * ((1 - p3)**(k_Z - 1))

# Gráfica PMF
plt.figure(figsize=(8,4))
plt.bar(k_Z, pmf_Z, width=0.6)
plt.xticks(k_Z)
plt.xlabel('k (intentos hasta 1er éxito)')
plt.ylabel('P(Z=k)')
plt.title(f'PMF: Geométrica(p={p3}), soporte k=1..{k3_max}')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()

print("Ejercicio 3 - Resultados numéricos:")
print(f" P(Z > 4) = (1 - {p3})^4 = {P_Z_gt_4:.6f}")
print(f" Esperanza E[Z] = 1/p = 1 / {p3} = {E_Z:.4f}")
print("\n\n")
```

Ejercicio 3 — Geométrica
$ Z \sim Geom(p = 0.15)$, soporte $ k = 1, 2, \dots $
Probabilidad $ P(Z > 4) $:
$$
P(Z > 4) = (1 - p)^4 = (0.85)^4 \approx 0.522006.
$$

(Es decir, hay $\sim 52.2\%$ de probabilidad de que el primer éxito ocurra después del 4º intento.)

Esperanza:
$$
E[Z] = \frac{1}{p} = \frac{1}{0.15} \approx 6.6667.
$$

Gráfica: se generó la PMF para $ k = 1, \dots, 15 $ .

Interpretación: en promedio hacen falta $\sim 6.67$ intentos hasta obtener el primer recubrimiento exitoso. Para planificación del laboratorio esto implica tiempo y consumo de material no despreciables: necesitarías presupuestar alrededor de 6–7 intentos por sensor (en promedio) para obtener uno con recubrimiento correcto.

## 4. Tema 4

```python
N4 = 100
K4 = 10
n4 = 12

# P(X = 3) = C(K,3) * C(N-K, n-3) / C(N, n)
k4_target = 3
num = math.comb(K4, k4_target) * math.comb(N4 - K4, n4 - k4_target)
den = math.comb(N4, n4)
P_X_eq_3 = num / den

# Esperanza E[X] = n * (K / N)
E_X = n4 * (K4 / N4)

# PMF for possible x values
x_min = max(0, n4 - (N4 - K4))
x_max = min(n4, K4)
x_vals = np.arange(x_min, x_max + 1)
pmf_X = np.array([math.comb(K4, x) * math.comb(N4 - K4, n4 - x) / math.comb(N4, n4) for x in x_vals])

# Gráfica PMF
plt.figure(figsize=(8,4))
plt.bar(x_vals, pmf_X, width=0.6)
plt.xticks(x_vals)
plt.xlabel('x (nº nanotubos defectuosos en la muestra)')
plt.ylabel('P(X=x)')
plt.title(f'PMF: Hipergeométrica(N={N4}, K={K4}, n={n4})')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()

print("Ejercicio 4 - Resultados numéricos:")
print(f" P(X=3) = {P_X_eq_3:.6f}")
print(f" Esperanza E[X] = n * (K/N) = {n4} * ({K4}/{N4}) = {E_X:.4f}")
print("\n\n")
```

Ejercicio 4 — Hipergeométrica
$ X \sim Hypergeom(N = 100, K = 10, n = 12) $
Probabilidad exacta:
$$
P(X = 3) = \frac{\binom{10}{3} \binom{90}{9}}{\binom{100}{12}} \approx 0.080682.
$$

Esperanza:
$$
E[X] = n \cdot \frac{K}{N} = 12 \cdot \frac{10}{100} = 1.2.
$$

Gráfica: se generó la PMF para $ x = 0, \ldots, 10$ (intervalo factible).

Interpretación: el valor esperado indica que en una muestra de 12 nanotubos se esperan, en promedio, 1.2 defectuosos. Obtener 3 defectuosos tiene probabilidad $\approx 8.07\% $ — es significativamente mayor que la media individual, pero no extremadamente improbable. Si se observan 3 defectuosos en la muestra, sugiere que ese lote podría tener más defectos de lo esperado (aunque no es concluyente por sí solo); convendría una inspección más amplia o medidas correctivas si se repite con frecuencia.

## 5. Tema 5

```python
lambda_per_cm2 = 0.6
area = 5.0
lambda_star = lambda_per_cm2 * area  # nueva tasa para la sección

# P(W = 0) = e^{-λ*}
P_W_eq_0 = math.exp(-lambda_star)

# PMF k = 0..10
k_W = np.arange(0, 11)
pmf_W = np.array([math.exp(-lambda_star) * (lambda_star**k) / math.factorial(k) for k in k_W])

# Gráfica PMF
plt.figure(figsize=(8,4))
plt.bar(k_W, pmf_W, width=0.6)
plt.xticks(k_W)
plt.xlabel('k (nº defectos en área de prueba)')
plt.ylabel('P(W=k)')
plt.title(f'PMF: Poisson(λ*={lambda_star}) para área = {area} cm^2')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()

print("Ejercicio 5 - Resultados numéricos:")
print(f" λ* (tasa para área de {area} cm^2) = {lambda_star:.4f}")
print(f" P(W=0) = e^(-{lambda_star}) = {P_W_eq_0:.6f}")
```

Ejercicio 5 — Poisson (defectos por área)

Tasa dada:
$$
\lambda = 0.6 \text{ defectos / cm}^2
$$
Para área $ = 5 \text{ cm}^2 $:

Nueva tasa:
$$
\lambda^* = 0.6 \cdot 5 = 3.0
$$

Probabilidad de cero defectos:
$$
P(W=0) = e^{-\lambda^*} = e^{-3} \approx 0.049787
$$

Gráfica: se generó la PMF de Poisson con $ \lambda^* = 3 $ (k=0..10).

Interpretación práctica: $ P(W=0) \approx 4.98\% $ es relativamente baja: hay solo $\sim 5\%$ de probabilidad de que una sección de $ 5 \text{ cm}^2 $ salga sin ningún defecto. Para producción de chips sin fallas en esa área, esto indica riesgo significativo; la viabilidad mejora si se reduce la tasa por área (mejor proceso) o se trabaja en secciones más pequeñas/controles adicionales. Si la tolerancia al defecto es cero, el proceso actual es problemático para conseguir alta productividad sin reprocesos.

## 6. Tema 6

```python
r6 = 5
p6 = 0.45

# PMF for V (k = 0,1,...): P(V=k) = C(k+r-1, k) * (1-p)^k * p^r
k6 = np.arange(0, 16)  # primeros 15 fracasos -> k=0..15
pmf6 = np.array([math.comb(int(k)+r6-1, int(k)) * (1-p6)**k * p6**r6 for k in k6])

# P(V=7)
k_target6 = 7
P_V_eq_7 = math.comb(k_target6 + r6 - 1, k_target6) * (1-p6)**k_target6 * p6**r6

# Expectation E[V] = r*(1-p)/p (número de fracasos antes de r éxitos)
E_V6 = r6 * (1-p6) / p6

results['ej6'] = {
    'P(V=7)': P_V_eq_7,
    'E[V]': E_V6,
    'k_vals': k6,
    'pmf': pmf6
}

# Plot PMF
plt.figure(figsize=(8,4))
plt.bar(k6, pmf6, width=0.6)
plt.xticks(k6)
plt.xlabel('k (nº fracasos antes de r=5 éxitos)')
plt.ylabel('P(V=k)')
plt.title(f'PMF: Binomial Negativa (r={r6}, p={p6}), k=0..15')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
```

Ejercicio 6 — Binomial negativa (Transistores FinFET)
Parámetros:
$ r = 5 $, $ p = 0.45 $
$ V $ = número de fracasos antes del quinto éxito.

$$ P(V = 7) = \binom{7 + 5 - 1}{7} (1 - p)^7 p^5 \approx 0.092708 $$

$$ E[V] = \frac{r(1 - p)}{p} = 5 \cdot \frac{0.55}{0.45} \approx 6.111111 $$

(Gráfica) PMF para $ k = 0, \dots, 15 $ mostrada arriba.

Interpretación: en promedio habrá ~6.11 fracasos antes de reunir 5 transistores conformes. Ese número de fracasos se traduce directamente en mayor consumo de material y tiempo de prueba: si cada intento tiene coste $ c $, el coste adicional esperado por lote es aproximadamente $ E[V] \cdot c $. Reducir $ 1 - p $ (mejorar p) disminuye fuertemente E[V] y reduce costes.

## 7. Tema 7

```python
N7 = 60
K7 = 6
n7 = 10

# support x = max(0, n-(N-K)) .. min(n,K)
x_min7 = max(0, n7 - (N7 - K7))
x_max7 = min(n7, K7)
x7 = np.arange(x_min7, x_max7 + 1)
pmf7 = np.array([math.comb(K7, x) * math.comb(N7 - K7, n7 - x) / math.comb(N7, n7) for x in x7])

# P(X >= 1) = 1 - P(X=0)
P_X_ge_1 = 1 - (math.comb(K7, 0) * math.comb(N7 - K7, n7 - 0) / math.comb(N7, n7))

# Varianza: n*(K/N)*(1-K/N)*(N-n)/(N-1)
pK = K7 / N7
Var_X7 = n7 * pK * (1 - pK) * (N7 - n7) / (N7 - 1)

# CDF values
cdf7 = np.cumsum(pmf7)

results['ej7'] = {
    'P(X>=1)': P_X_ge_1,
    'Var[X]': Var_X7,
    'x_vals': x7,
    'pmf': pmf7,
    'cdf': cdf7
}

# Plot CDF
plt.figure(figsize=(8,4))
plt.step(x7, cdf7, where='post')
plt.scatter(x7, cdf7)
plt.xticks(x7)
plt.xlabel('x (nº muestras fallidas en la selección)')
plt.ylabel('F_X(x)')
plt.title(f'CDF: Hipergeométrica(N={N7}, K={K7}, n={n7})')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
```

Ejercicio 7 — Hipergeométrica (Muestreo de polímeros)

Parámetros: $ N = 60 $, $ K = 6 $, $ n = 10 $.

$ X $ = nº muestras fallidas en la selección.

$ P(X \geq 1) = 1 - P(X = 0) \approx 0.682591 $
(Es decir, ~68.26% de probabilidad de detectar al menos una muestra fallida en la muestra de 10.)

$ \text{Var}(X) = n \frac{K}{N} \left(1 - \frac{K}{N}\right) \frac{N - n}{N - 1} \approx 0.762712 $.

(Gráfica) CDF mostrada arriba (valores de $ x = 0, \dots, 6 $).

Interpretación: la probabilidad de detectar al menos una falla con una muestra de 10 es relativamente alta (~68%), pero no cercana a 100%. Si la intención es asegurar casi cero riesgo de pasar un lote defectuoso, esta estrategia de muestreo podría ser insuficiente: existe ~31.7% de probabilidad de no detectar ninguna muestra fallida aunque haya fallas en el envío.

## 8. Tema 8

```python
n8 = 8
p_success = 0.9  # prob de adherencia perfecta
p_fail = 1 - p_success  # prob de adherencia imperfecta -> p para Y
p8 = p_fail

k8 = np.arange(0, n8+1)
pmf8 = np.array([math.comb(n8, k) * (p8**k) * ((1-p8)**(n8-k)) for k in k8])

# P(Y > 1) = 1 - P(Y <= 1)
P_Y_gt_1 = 1 - sum(pmf8[:2])  # pmf8[0] + pmf8[1]

results['ej8'] = {
    'n': n8,
    'p_fail': p8,
    'P(Y>1)': P_Y_gt_1,
    'k_vals': k8,
    'pmf': pmf8
}

# Plot PMF
plt.figure(figsize=(8,4))
plt.bar(k8, pmf8, width=0.6)
plt.xticks(k8)
plt.xlabel('k (nº puntos con adherencia imperfecta)')
plt.ylabel('P(Y=k)')
plt.title(f'PMF: Binomial(n={n8}, p_fail={p8})')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
```

Ejercicio 8 — Binomial (Adherencia imperfecta)
Contexto: éxito (adherencia perfecta) con prob \( 0.9 \). Se define \( Y \) = nº puntos con adherencia imperfecta en \( n = 8 \).

Parámetros para $ Y $: $ n = 8 $, $ p_{\text{fallo}} = 0.1 $.

$ P(Y > 1) = 1 - P(Y \leq 1) \approx 0.186895 $.

(Gráfica) PMF para $ k = 0, \dots, 8 $ mostrada arriba.

Interpretación: la probabilidad de tener más de un punto con adherencia imperfecta es ~18.7% — no alta pero sí relevante. Si esto es crítico, el ingeniero debería reducir la variabilidad del proceso (mejorar la preparación/sustrato/proceso de recubrimiento), implementar controles en línea o aumentar la inspección/monitorización para detectar y corregir fallos tempranamente.

## 9. Tema 9

```python
lambda_per_100 = 2.5
segment_length = 400.0  # micras
scale = segment_length / 100.0
lambda9 = lambda_per_100 * scale

# P(8 <= W <= 12)
k9_low, k9_high = 8, 12
pmf9_range = [math.exp(-lambda9) * (lambda9**k) / math.factorial(k) for k in range(0, 31)]
P_between_8_12 = sum(pmf9_range[k9_low:k9_high+1])

k9 = np.arange(0, 21)
pmf9 = np.array([math.exp(-lambda9) * (lambda9**k) / math.factorial(k) for k in k9])

results['ej9'] = {
    'lambda_star': lambda9,
    'P(8<=W<=12)': P_between_8_12,
    'k_vals': k9,
    'pmf': pmf9
}

# Plot PMF
plt.figure(figsize=(8,4))
plt.bar(k9, pmf9, width=0.6)
plt.xticks(k9)
plt.xlabel('k (nº errores en 400 µm)')
plt.ylabel('P(W=k)')
plt.title(f'PMF: Poisson(λ*={lambda9}) para segmento de {int(segment_length)} µm')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
```

Ejercicio 9 — Poisson (Errores en litografía)
Tasa base: $ \lambda = 2.5 $ errores por 100 µm. Segmento de 400 µm → factor 4.

$ \lambda^* = 2.5 \cdot \frac{400}{100} = 10.0 $.

$ P(8 \leq W \leq 12) = \sum_{k=8}^{12} e^{-\lambda^*} \frac{(\lambda^*)^k}{k!} \approx 0.571336 $

(Gráfica) PMF para $ k = 0, \dots, 20 $ mostrada arriba.

Interpretación: $ \lambda^* = 10 $ es la media de errores esperada en el segmento de 400 µm: valores alrededor de 10 son los más probables. La probabilidad de observar entre 8 y 12 errores es ~57.1% — por lo tanto el diseñador de circuitos debe considerar este nivel de defecto esperado al dimensionar tolerancias y márgenes (p. ej. densidad de líneas, redundancias o pasos de corrección) para garantizar fiabilidad.

## 10. Tema 10

```python
p10 = 0.6
# Z ~ Geom(p), support k=1...
kz = np.arange(1, 16)
pmfZ = p10 * (1-p10)**(kz - 1)
E_Z10 = 1 / p10

# V ~ NB counting total trials until r successes (support n = r, r+1,...)
r10 = 3
# PMF for total trials n: P(V=n) = C(n-1, r-1) p^r (1-p)^(n-r), n = r, r+1, ...
kv = np.arange(r10, 16)
pmfV = np.array([math.comb(n-1, r10-1) * (p10**r10) * ((1-p10)**(n - r10)) for n in kv])
E_V10 = r10 / p10  # expectation for total trials until r successes

results['ej10'] = {
    'E[Z]': E_Z10,
    'E[V]': E_V10,
    'kz': kz,
    'pmfZ': pmfZ,
    'kv': kv,
    'pmfV': pmfV
}

# Plot PMF of Z and V in same figure (bars, aligned)
plt.figure(figsize=(9,5))
width = 0.35
plt.bar(kz - width/2, pmfZ, width=width, label=f'Z ~ Geom(p={p10}), k≥1')
plt.bar(kv + width/2, pmfV, width=width, label=f'V ~ NB total trials (r={r10}, p={p10}), n≥{r10}')
plt.xticks(np.arange(0, 16))
plt.xlabel('k (nº intentos)')
plt.ylabel('Probabilidad (PMF)')
plt.title('PMF de Z (Geométrica) y V (Binomial Negativa - total ensayos)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
```

Ejercicio 10 — Geométrica vs Binomial Negativa (Impresión 3D nanoescala)
Probabilidad de éxito por intento: $ p = 0.6 $.

$ Z $ (intentos hasta primer éxito): $ E[Z] = \frac{1}{p} = \frac{1}{0.6} \approx 1.666667 $.

$ V $ (nº total de ensayos hasta 3 éxitos, $ r = 3 $):$ E[V] = \frac{r}{p} = \frac{3}{0.6} = 5.000000 $.

(Gráfica) PMF de $ Z $ y PMF de $ V $ en la misma figura (mostrada arriba).

Interpretación: en promedio se necesitan ~1.67 intentos para obtener el primer éxito, pero ~5 intentos para obtener 3 éxitos (total). Esto refleja que los objetivos que requieren más éxitos consumen proporcionalmente más material/tiempo. Para planificación, si cada intento tiene coste/material $ c $, el coste esperado para obtener 1 éxito es $ E[Z] \cdot c $ y para 3 éxitos es $ E[V] \cdot c $. Si la meta es reducir consumo, mejorar $ p $ (calidad del proceso) reduce ambas expectativas, con efecto multiplicativo sobre el total requerido para múltiples éxitos.

---

##**UCEMICH** 13/10/25

### 10.1 TEMA: DISTRIBUCIONES DE PROBABILIDAD CON PYTHON

#Sección 3

13-10-25

### 10.2 3 Variables discretas
Una variable aleatoria se clasifica como discreta si su espacio objetivo ($T$) es finito o contablemente infinito. Las distribuciones de probabilidad para variables discretas se describen llenando una matriz (posiblemente multidimensional) de números. A diferencia de las variables continuas, para las variables discretas la probabilidad de un evento se mide mediante un "contador" o conteo, y el concepto de integración se reemplaza por la sumatoria.

## 3. 1 Variables Aleatorias

### 3.1 .1 Un ejemplo motivador
El concepto de variable aleatoria surge de la necesidad de convertir resultados de experimentos aleatorios, que a menudo se expresan como enunciados (por ejemplo, "obtener cara" o "ganar el juego"), en números. Los ingenieros y analistas prefieren trabajar con números, y la variable aleatoria sirve como esta herramienta de traducción. Por ejemplo, al lanzar dos monedas y contar el número de caras, la variable aleatoria $X$ mapea el resultado ("hh") al número 2, ("ht") a 1, y ("tt") a 0.

### 3.1 .2 Definición de una variable aleatoria
Una variable aleatoria ($X$) es una función. Mapea un resultado $\omega$ del espacio muestral $\Omega$ (el conjunto de todos los resultados posibles) a un valor particular $x$ en el espacio objetivo $T$.
• Es crucial entender que la variable aleatoria no es aleatoria ni es una variable; es una función.
• Un término más descriptivo para una variable aleatoria es función medible.
• El conjunto de todos los valores que toma $X$ se llama el rango ($R_X$) o el conjunto de estados $X(\Omega)$.

### 3.1 .3 Medida de probabilidad en variables aleatorias
La ley de probabilidad $P(\cdot)$ está definida para medir el tamaño de un evento $E$, que es un subconjunto de $\Omega$. Cuando buscamos la probabilidad de que una variable aleatoria $X$ tome un valor específico $a$, denotado $P[X=a]$, estamos preguntando por la medida de la pre-imagen de $a$ en el espacio muestral $\Omega$. Es decir, se mide el tamaño del conjunto $E = {\xi \in \Omega \mid X(\xi) = a}$.

## 3. 2 Función de Masa de Probabilidad (PMF)

### 3.2 .1 Definición de función de masa de probabilidad
Para una variable aleatoria discreta $X$, la Función de Masa de Probabilidad (PMF), denotada $p_X(x)$ o $P(X=x)$, es una función que especifica la probabilidad de que $X$ obtenga un valor numérico específico $x$. La PMF resume la probabilidad de cada uno de los estados posibles de $X$.

### 3.2 .2 PMF y medida de probabilidad
La PMF actúa como la función de ponderación (weighting function) para las variables aleatorias discretas. Dos variables aleatorias son diferentes si sus PMFs son diferentes, ya que definen dos medidas de probabilidad distintas. Sin embargo, dos variables aleatorias ($X$ y $Y$) pueden tener la misma forma de PMF, pero aún así ser variables aleatorias distintas si sus mapeos desde el espacio muestral son diferentes.

### 3.2 .3 Propiedad de normalización
Una propiedad fundamental de la PMF es la propiedad de normalización. La suma de las probabilidades de todos los resultados posibles en el espacio de estados $X(\Omega)$ debe ser igual a 1. $\sum_{x \in X(\Omega)} p_X(x) = 1$

### 3.2 .4 PMF versus histograma
La PMF puede considerarse el histograma ideal de una variable aleatoria. Proporciona una caracterización completa de la variable aleatoria. A medida que el número de muestras o ensayos ($N$) aumenta, el histograma empírico de los datos tiende a converger a la forma de la PMF teórica.

### 3.2 .5 Estimación de histogramas a partir de datos reales
Al construir un histograma a partir de un conjunto de datos, la elección del número de bins (o ancho de los bins) es crucial. Si los bins son demasiado grandes o demasiado pequeños, la representación gráfica puede distorsionar la distribución subyacente. La tarea de inferir los parámetros de la PMF subyacente a partir de los datos se conoce como inferencia estadística.

## 3. 3 Funciones de Distribución Acumulada (Discretas)

### 3.3 .1 Definición de la función de distribución acumulada
La Función de Distribución Acumulada (CDF), $F_X(x)$, de una variable aleatoria discreta $X$ es la probabilidad de que $X$ tome un valor menor o igual a $x$. Es la suma acumulada de la PMF desde $-\infty$ hasta $x$: $F_X(x_k) \stackrel{\text{def}}{=} P[X \leq x_k] = \sum_{\ell=1}^{k} p_X(x_\ell)$

### 3.3 .2 Propiedades de la CDF
La CDF es siempre una función bien definida. Para variables aleatorias discretas, la CDF es una función escalonada (staircase function). Sus propiedades clave incluyen:
1. Monotonía: $F(x)$ es una función no decreciente de $x$.
2. Límites: $0 \leq F(x) \leq 1$. Además, $\lim_{x\to-\infty} F(x) = 0$ y $\lim_{x\to+\infty} F(x) = 1$.

### 3.3 .3 Conversión entre PMF y CDF
Si se conoce la CDF $F_X(x)$, la PMF $p_X(x)$ se puede obtener tomando la diferencia de las probabilidades acumuladas en los puntos donde ocurren los saltos (saltos) en la función escalonada: $p_X(x_k) = F_X(x_k) - F_X(x_{k-1})$

## 3. 4 Esperanza (Expectativa)

### 3.4 .1 Definición de esperanza
La Esperanza (o Expectativa), $E[X]$, es conceptualmente el promedio (mean) o el centro de masa calculado a partir de la PMF. Para una variable aleatoria discreta $X$ con PMF $p_X(x)$, la esperanza se define como: $E[X] = \sum_{x \in X(\Omega)} x \cdot p_X(x)$

### 3.4 .2 Existencia de esperanza
La esperanza de una variable aleatoria $X$ solo existe si la suma es absolutamente convergente. Una variable aleatoria discreta es absolutamente sumable si la esperanza de su valor absoluto es finita, $E[|X|] = \sum |x| p_X(x) < \infty$. Ciertos casos matemáticos (como la distribución de Cauchy en el caso continuo) demuestran que no todas las distribuciones tienen una esperanza definida.

### 3.4 .3 Propiedades de la esperanza
La esperanza es un operador lineal. Las propiedades clave incluyen:
• Linealidad: La esperanza de una suma de funciones de una variable aleatoria es la suma de sus esperanzas: $E[g(X) + h(X)] = E[g(X)] + E[h(X)]$.
• Escalamiento: Para cualquier constante $c$, $E[cX] = cE[X]$.
• Función de una V.A.: La esperanza de una función $g(X)$ se calcula como $E[g(X)] = \sum_x g(x) p_X(x)$. Esto a veces se conoce como la ley del estadístico inconsciente.

### 3.4 .4 Momentos y varianza
• Momentos: El $k$-ésimo momento de una variable aleatoria $X$ es la esperanza de $X^k$, $E[X^k]$. El primer momento es la media $E[X]$.
• Varianza: La varianza ($\text{Var}(X)$ o $\sigma^2$) es una medida de la dispersión o propagación de los valores de $X$ alrededor de su media $\mu$. Se define como la esperanza de la desviación cuadrática con respecto a la media: $\text{Var}(X) = E[(X - \mu)^2] = \sum_i (x_i - \mu)^2 p(x_i)$ La desviación estándar ($\sigma$) es la raíz cuadrada positiva de la varianza.

## 3. 5 Variables Aleatorias Discretas Comunes

### 3.5 .1 Variable aleatoria de Bernoulli
Una variable de Bernoulli modela el resultado de un solo experimento con solo dos posibles estados (0 o 1). El parámetro $p$ (o $\theta$) es la probabilidad de que el resultado sea 1 (éxito). La variable de Bernoulli es útil para modelar cualquier evento de estado binario, como lanzar una moneda, un bit binario o resultados de sí/no.

### 3.5 .2 Variable aleatoria binomial
La variable aleatoria binomial modela el número de éxitos ($k$) en una secuencia de $n$ ensayos independientes de Bernoulli, donde la probabilidad de éxito en cada ensayo es $p$. De hecho, la variable binomial se puede ver intrínsecamente como la suma de $n$ variables aleatorias de Bernoulli independientes.

### 3.5 .3 Variable aleatoria geométrica
Una variable aleatoria geométrica modela el número de ensayos hasta que se observa el primer éxito. La PMF $p_X(k) = (1-p)^{k-1}p$ se interpreta como $k-1$ fallos consecutivos, seguidos de un éxito final.

### 3.5 .4 Variable aleatoria de Poisson
La distribución de Poisson se utiliza para modelar el conteo de eventos discretos que ocurren en un intervalo fijo de tiempo o espacio. El parámetro $\lambda$ (lambda) es a la vez la media y la varianza de la distribución. Una de las formas de derivar la PMF de Poisson es considerar el límite de una variable aleatoria binomial donde el número de ensayos $n \to \infty$ y la probabilidad de éxito $p \to 0$.

### 3.6 MODELOS PARA VARIABLES ALEATORIAS EN PYTHON Y EN R

https://es.wikipedia.org/wiki/Distribuci%C3%B3n_de_probabilidad

```python
import numpy as np
from numpy.random import binomial #generador aleatorio de numeros basados ​​en la distro binomial
from scipy.stats import binom #distro teorica
from math import factorial
import matplotlib.pyplot as plt #visualizaciones
from scipy import stats
from scipy import optimize
import seaborn as sns
sns.set(style="whitegrid")
```

Generación de numeros aleatorios

```python
np.random.rand()
```

```python
np.random.randn()
```

```python
np.random.randint(100)
```

```python
np.random.rand(5)
```

```python
np.random.randn(2, 4)
```

```python
np.random.randint(10, size=10)
```

```python
np.random.randint(low=10, high=20, size=(2, 10))
```

```python
np.random.choice(10, 5, replace=False)
```

```python
np.random.choice(10, 5, replace=True)
```

La semilla del generador de números aleatorios, es una función que permite obtener los mismos resultados de experimento aleatorio:

```python
np.random.rand()
```

```python
np.random.rand()
```

```python
np.random.seed(123456789)
np.random.rand()
```

In addition to the fundamental random number distributions we have looked at so
far (discrete and continuous uniform distributions, randint and rand, and the standard
normal distribution, randn), there are also functions, and RandomState methods, for
a large number of probability distributions that occur in statistics. To mention just a
few, there is the continuous χ2

distribution (chisquare), the Student’s t distribution

(standard_t), and the F distribution (f):

https://thedataschools.com/

### 3.7 Modelos para Variables Aleatorias Discretas

### 3.8 Listado de las distribuciones de probabilidad discretas más utilizadas

En las diversas disciplinas de nanotecnología, ciencias de los materiales, inteligencia artificial, diseño de experimentos y pruebas de hipótesis, se destacan las siguientes distribuciones de probabilidad discretas, organizadas por tema:

##### Nanotecnología

1. **Distribución de Poisson**
   - **Uso**: Modelar el número de eventos en un intervalo fijo de tiempo o espacio.
   - **Ejemplo**: Número de defectos encontrados en un lote de nanopartículas, donde se espera que ocurran defectos de manera independiente y con una tasa constante.

2. **Distribución Binomial**
   - **Uso**: Modelar el número de éxitos en una serie de ensayos independientes.
   - **Ejemplo**: Evaluar la efectividad de un recubrimiento en nanopartículas, donde se cuenta el número de partículas que logran un recubrimiento exitoso tras varios intentos.

3. **Distribución Geométrica**
   - **Uso**: Modelar el número de ensayos hasta el primer éxito.
   - **Ejemplo**: Determinar cuántas veces se necesita aplicar un proceso de recubrimiento antes de lograr una nanopartícula con el recubrimiento deseado.

##### Ciencias de los Materiales

1. **Distribución Binomial Negativa**
   - **Uso**: Modelar el número de fracasos antes de alcanzar un número fijo de éxitos.
   - **Ejemplo**: Número de pruebas necesarias para obtener un número específico de componentes con la resistencia adecuada en un material.

2. **Distribución Hipergeométrica**
   - **Uso**: Modelar la probabilidad de éxito en muestras sin reemplazo.
   - **Ejemplo**: Selección de un número específico de materiales de un lote, donde se evalúa cuántos cumplen con las especificaciones requeridas sin reponer los seleccionados.

3. **Distribución de Poisson**
   - **Uso**: Modelar eventos raros en un intervalo.
   - **Ejemplo**: Cantidad de fracturas en un material sometido a estrés, donde los eventos son relativamente raros en un período de tiempo específico.

##### Inteligencia Artificial

1. **Distribución de Bernoulli**
   - **Uso**: Modelar experimentos con dos resultados posibles.
   - **Ejemplo**: Evaluación de la clasificación correcta o incorrecta de un modelo de aprendizaje automático en un conjunto de datos.

2. **Distribución Multinomial**
   - **Uso**: Generalización de la binomial para más de dos resultados.
   - **Ejemplo**: Clasificación de elementos en diferentes categorías, como identificar la clase de imágenes en un conjunto de datos.

3. **Distribución de Poisson**
   - **Uso**: Modelar el número de eventos en un intervalo.
   - **Ejemplo**: Número de clics en un anuncio en línea en un período determinado, donde se espera que los clics ocurran de manera independiente.

##### Diseño de Experimentos y Pruebas de Hipótesis

1. **Distribución Binomial**
   - **Uso**: Evaluar el número de éxitos en ensayos con dos posibles resultados.
   - **Ejemplo**: Pruebas A/B en marketing, donde se mide la tasa de conversión de dos versiones de un anuncio.

2. **Distribución Hipergeométrica**
   - **Uso**: Evaluar el éxito en muestreo sin reemplazo.
   - **Ejemplo**: Selección de grupos de muestras en un experimento donde se busca un número específico de sujetos que cumplan con ciertos criterios.

3. **Distribución de Poisson**
   - **Uso**: Modelar eventos en un intervalo fijo.
   - **Ejemplo**: Número de fallas en un experimento de fiabilidad a lo largo de un periodo determinado, ayudando a predecir el rendimiento de un sistema.

Cada una de estas distribuciones desempeña un papel esencial en la modelación, análisis y comprensión de datos en sus respectivos campos, facilitando inferencias precisas y fundamentadas en experimentos y estudios estadísticos.

### 3.9 Distribución Uniforme Discreta

| Característica | Detalle |
| :--- | :--- |
| **Descripción** | Representa una variable aleatoria que puede tomar un número finito de valores, y donde cada uno de esos valores tiene exactamente la misma probabilidad de ocurrir. |
| **Parámetros** | $k$: El número de valores posibles ($x_1, x_2, \dots, x_k$). A veces se usa $a$ (mínimo) y $b$ (máximo), donde $k = b - a + 1$. |
| **Dominio ($R_X$)** | El conjunto de enteros $\{x_1, x_2, \dots, x_k\}$ (a menudo, $\{1, 2, \dots, k\}$ o $\{a, a+1, \dots, b\}$). |
| **Función de Masa de Probabilidad (PMF)** | $P(X = x_i) = \frac{1}{k} \quad \text{para } x_i \in R_X$|
| **Valor Esperado** | $E[X] = \frac{x_1 + x_2 + \dots + x_k}{k}$|
| **Media** | $\mu_X = E[X]$ |
| **Varianza** | $\text{Var}(X) = \frac{1}{k} \sum_{i=1}^{k} (x_i - \mu_X)^2$ |
| **Varianza (si $R_X = \{1, 2, \dots, k\}$)** | $\sigma^2 = \frac{k^2 - 1}{12}$ |
| **Desviación Estándar** | $\sigma = \sqrt{\text{Var}(X)}$ |
| **Función de Distribución Acumulativa (CDF)** | $F(x) = \frac{\text{Número de valores } \le x}{k}$|

### 3.10 Caso Especial (más común): $R_X = \{1, 2, \dots, k\}$

| Característica | Fórmula |
| :--- | :--- |
| **Media** | $E[X] = \frac{k + 1}{2}$ |
| **Varianza** | $\sigma^2 = \frac{k^2 - 1}{12}$ |

### 3.11 Comandos en R (Usando la distribución de enteros)

En R, para la distribución uniforme discreta de enteros se suele usar la función `sample()` o una adaptación de las funciones de la distribución binomial si el dominio comienza en 0 o 1, pero la más directa es `sample()`.

```r
### 3.12 Parámetro: k (número de resultados posibles),
### 3.13 a y b (mínimo y máximo)
### 3.14 Ejemplo: Un dado de 6 caras (k=6, a=1, b=6)

### 3.15 PMF (Probabilidad de un valor específico):
### 3.16 P(X = x) = 1/k. No hay una función dedicada, se calcula directamente:
k = 6
prob_de_obtener_3 = 1 / k
print(prob_de_obtener_3) # 0.1666667

### 3.17 CDF (Función de distribución acumulada):
### 3.18 P(X <= x) = x/k. Se calcula directamente:
x = 3
k = 6
prob_acumulada_hasta_3 = x / k
print(prob_acumulada_hasta_3) # 0.5 (P(X<=3) = P(1)+P(2)+P(3) = 1/6 + 1/6 + 1/6)

### 3.19 Para generar simulación (Muestreo uniforme de n valores):
n = 10 # número de muestras a generar
a = 1  # Valor mínimo
b = 6  # Valor máximo
r = sample(a:b, size = n, replace = TRUE)
print(r)
### 3.20 Ejemplo de salida: [3, 6, 1, 5, 2, 6, 3, 4, 1, 5]
```

#### 🐍 Códigos en Python: Distribución Uniforme Discreta

La Distribución Uniforme Discreta se modela en `scipy.stats` usando la clase `randint` (random integer), o a veces `discrete_uniform`, aunque `randint` es el método preferido y más general.

Consideraremos una variable aleatoria $X$ que toma valores enteros en el rango **de $a$ a $b$** (incluidos).

  * **Parámetros:** $a$ (mínimo), $b$ (máximo).
  * **$k$ (número de valores):** $b - a + 1$.

### 3.21 1\. Inicialización y Parámetros

```python
from scipy.stats import randint
import numpy as np

# Definir el rango del dado (ejemplo: de 1 a 6, ambos inclusive)
a = 1  # Límite inferior (incluido)
b = 6  # Límite superior (incluido)

# NOTA: En scipy.stats.randint, el límite superior (high) es EXCLUIDO.
# Por lo tanto, si quieres incluir 'b', debes usar 'b + 1' como parámetro 'high'.
low = a
high = b + 1

dist = randint(low, high)
k = high - low # Número total de resultados posibles
print(f"Rango: [{a}, {b}]")
print(f"Número de resultados (k): {k}")
#
```

-----

### 3.22 2\. Función de Masa de Probabilidad (PMF)

La PMF da la probabilidad de que la variable aleatoria tome un valor exacto: $P(X = x)$.

$$P(X = x) = \frac{1}{k}$$

```python
# Valor específico para calcular su probabilidad
x = 3

# Usando el método .pmf()
prob_pmf = dist.pmf(x)
print(f"P(X = {x}) (PMF): {prob_pmf}")

# Verificación manual: 1/k
prob_manual = 1 / k
print(f"1/k (manual): {prob_manual}")
```

-----

### 3.23 3\. Función de Distribución Acumulativa (CDF)

La CDF da la probabilidad de que la variable aleatoria sea menor o igual a un valor: $P(X \le x)$.

$$F(x) = P(X \le x) = \frac{x - a + 1}{k}$$

```python
# Valor específico para calcular la probabilidad acumulada
x = 4

# Usando el método .cdf()
prob_cdf = dist.cdf(x)
print(f"P(X <= {x}) (CDF): {prob_cdf}")

# Verificación manual: P(X<=4) = 4/6
prob_manual_cdf = (x - a + 1) / k
print(f"Prob. manual: {prob_manual_cdf}")
```

-----

### 3.24 4\. Simulación (Generación de Muestras Aleatorias)

Genera $n$ realizaciones independientes de la distribución uniforme discreta.

```python
n = 10  # Número de muestras a generar

# Usando el método .rvs() (Random Variates)
simulacion_rvs = dist.rvs(size=n)
print(f"Simulación (rvs): {simulacion_rvs}")

# También se puede usar numpy.random.randint (low incluido, high excluido)
simulacion_np = np.random.randint(low=a, high=b + 1, size=n)
print(f"Simulación (numpy): {simulacion_np}")
```

-----

### 3.25 5\. Momentos (Media y Varianza)

Calcula la media (valor esperado) y la varianza de la distribución.

$$E[X] = \frac{a + b}{2} \quad \text{y} \quad \text{Var}(X) = \frac{k^2 - 1}{12}$$

```python
# Usando el método .mean()
media = dist.mean()

# Usando el método .var()
varianza = dist.var()

# Usando el método .std() para la desviación estándar
desviacion_estandar = dist.std()

print(f"Media (E[X]): {media}")
print(f"Varianza (Var(X)): {varianza}")
print(f"Desviación Estándar (std): {desviacion_estandar:.4f}")
```

```python
from scipy.stats import randint
import numpy as np

# Definir el rango del dado (ejemplo: de 1 a 6, ambos inclusive)
a = 1  # Límite inferior (incluido)
b = 6  # Límite superior (incluido)

# NOTA: En scipy.stats.randint, el límite superior (high) es EXCLUIDO.
# Por lo tanto, si quieres incluir 'b', debes usar 'b + 1' como parámetro 'high'.
low = a
high = b + 1

dist = randint(low, high)
k = high - low # Número total de resultados posibles
print(f"Rango: [{a}, {b}]")
print(f"Número de resultados (k): {k}")
```

```python
# Valor específico para calcular su probabilidad
x = 3

# Usando el método .pmf()
prob_pmf = dist.pmf(x)
print(f"P(X = {x}) (PMF): {prob_pmf}")

# Verificación manual: 1/k
prob_manual = 1 / k
print(f"1/k (manual): {prob_manual}")
```

```python
# Valor específico para calcular la probabilidad acumulada
x = 4

# Usando el método .cdf()
prob_cdf = dist.cdf(x)
print(f"P(X <= {x}) (CDF): {prob_cdf}")

# Verificación manual: P(X<=4) = 4/6
prob_manual_cdf = (x - a + 1) / k
print(f"Prob. manual: {prob_manual_cdf}")
```

```python
n = 10  # Número de muestras a generar

# Usando el método .rvs() (Random Variates)
simulacion_rvs = dist.rvs(size=n)
print(f"Simulación (rvs): {simulacion_rvs}")

# También se puede usar numpy.random.randint (low incluido, high excluido)
simulacion_np = np.random.randint(low=a, high=b + 1, size=n)
print(f"Simulación (numpy): {simulacion_np}")
```

```python
# Usando el método .mean()
media = dist.mean()

# Usando el método .var()
varianza = dist.var()

# Usando el método .std() para la desviación estándar
desviacion_estandar = dist.std()

print(f"Media (E[X]): {media}")
print(f"Varianza (Var(X)): {varianza}")
print(f"Desviación Estándar (std): {desviacion_estandar:.4f}")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import randint

# --- 1. Definir la Distribución Uniforme Discreta (Ejemplo: Dado de 1 a 6) ---
a = 1      # Límite inferior (incluido)
b = 6      # Límite superior (incluido)
low = a
high = b + 1 # high es excluido en scipy.stats
dist = randint(low, high)

# --- 2. Preparar los datos para el gráfico ---
# Obtener todos los posibles valores discretos (1, 2, 3, 4, 5, 6)
valores = np.arange(low, high)
# Obtener la probabilidad (PMF) para cada valor
probabilidades = dist.pmf(valores)

# --- 3. Generar el Gráfico ---
plt.figure(figsize=(8, 5))

# Graficar las probabilidades como barras
plt.bar(valores, probabilidades, width=0.8, color='skyblue', edgecolor='black')

# Añadir una línea horizontal para mostrar la uniformidad
plt.axhline(y=1/len(valores), color='red', linestyle='--', linewidth=1, label=f'P = 1/{len(valores)}')

# Añadir etiquetas de probabilidad en la parte superior de cada barra
for val, prob in zip(valores, probabilidades):
    plt.text(val, prob + 0.005, f'{prob:.4f}', ha='center', fontsize=9)

# Configuración y títulos
plt.title('Función de Masa de Probabilidad (PMF) - Distribución Uniforme Discreta', fontsize=14)
plt.xlabel('Valores Posibles (x)', fontsize=12)
plt.ylabel('Probabilidad P(X = x)', fontsize=12)
plt.xticks(valores)
plt.ylim(0, max(probabilidades) + 0.05)
plt.legend()
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.show()
```

### 3.26 Distribución de Bernoulli
   - **Descripción**: Representa un experimento con dos resultados posibles (éxito o fracaso).
   - **Parámetro**: $ p $ (probabilidad de éxito).
   - **Función de Masa de Probabilidad (PMF)**:
   $
   P(X=1) = p, \quad P(X=0) = 1 - p
   $
   - **Valor Esperado**:
   $
   E[X] = p
   $
   - **Media**:
  $
   \mu_X = p
  $
   - **Varianza**:
  $
   \sigma = {p(1-p)}
  $
   - **Desviación Estándar**:
  $
   \sigma = \sqrt{p(1-p)}
  $
   - **Función de Distribución Acumulativa (CDF)**:
  $
   F(x) =
   \begin{cases}
   0 & \text{si } x < 0 \\
   1 - p & \text{si } 0 \leq x < 1 \\
   1 & \text{si } x \geq 1
   \end{cases}
  $
   - **Comandos en R**:
   
   ```r
### 3.27 PMF (funcion de masa de probabilidad)
   dbinom(x, size=1, prob=p)
   
### 3.28 CDF (funcion de distribucion acumulada)
   pbinom(x, size=1, prob=p)
   
### 3.29 Para generar simulacion
   rbinom(n, size=1, prob=p)       

```python
"""
p <- 0.1
x <- 1
size <- 1

# Calcular la probabilidad de que un producto dure más de 5500 unidades de tiempo
probabilidad <- dbinom(x, size, prob = p)
print(probabilidad)  # Debería ser 0.1
"""
```

```python
from scipy.stats import binom

# Parámetros
p = 0.1     # probabilidad de éxito
x = 1       # número de éxitos deseados
size = 1    # número de ensayos

# Cálculo de probabilidad puntual (PMF)
probabilidad = binom.pmf(x, size, p)
print(probabilidad)  # Debería ser 0.1
```

```python
""" pbinom(x, size=1, prob=p)"""
```

```python
from scipy.stats import binom

p = 0.1
x = 1
size = 1

# Probabilidad acumulada P(X ≤ x)
probabilidad = binom.cdf(x, size, p)
print(probabilidad)  # → 1.0
```

```python
"""
rbinom(100, size=1, prob=p)
"""
```

```python
p=0.1
size= 1
muestra= np.random.binomial(size, p, 100)
print(muestra)
```

#### Ejemplo de Gráfica de la Distribución de Bernoulli

Esta distribución describe un experimento con dos resultados posibles: éxito $(1) $ y fracaso $ (0)$.

```python
"""
# Cargar la librería necesaria
library(ggplot2)

# Definir el parámetro de éxito (p)
p <- 0.7  # Probabilidad de éxito

# Crear los valores posibles de X (0 y 1)
x_values <- c(0, 1)

# Calcular la PMF de la distribución de Bernoulli
pmf_values <- c(1 - p, p)

# Crear un data frame para ggplot
data <- data.frame(x = x_values, pmf = pmf_values)

# Graficar la distribución de Bernoulli
ggplot(data, aes(x = factor(x), y = pmf)) +
  geom_bar(stat = "identity", fill = "blue", alpha = 0.7) +
  labs(title = "Gráfico de la Distribución de Bernoulli",
       x = "Resultado",
       y = "Probabilidad") +
  scale_x_discrete(labels = c("0" = "Fracaso", "1" = "Éxito")) +
  theme_minimal() +
  ylim(0, 1)

"""
```

```python
import matplotlib.pyplot as plt
import pandas as pd

# Parámetro de éxito
p = 0.7  # Probabilidad de éxito

# Valores posibles de X
x_values = [0, 1]

# PMF de la distribución de Bernoulli
pmf_values = [1 - p, p]

# Crear un DataFrame (opcional, solo para claridad)
data = pd.DataFrame({"Resultado": x_values, "Probabilidad": pmf_values})

# Gráfico
plt.bar(data["Resultado"], data["Probabilidad"],
        color="cornflowerblue", alpha=0.7, width=0.4)

# Etiquetas de los ejes y título
plt.xticks([0, 1], ["Fracaso", "Éxito"])
plt.title("Distribución de Bernoulli")
plt.xlabel("Resultado")
plt.ylabel("Probabilidad")
plt.ylim(0, 1)
plt.grid(axis='y', linestyle=':', alpha=0.6)

# Mostrar gráfico
plt.show()
```

#### Descripción del Código en R

* **Cargar librerías**: Se utiliza `ggplot2` para crear la gráfica.
* **Definir el parámetro de éxito**: Se establece la probabilidad de éxito $ p $ (en este caso, $0.7$).
* **Crear los valores posibles de $X$**: Los valores posibles son $0$ (fracaso) y $1$ (éxito).
* **Calcular la PMF**: Se calculan las probabilidades de cada resultado usando la fórmula de la distribución de Bernoulli.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $ X $ y sus correspondientes probabilidades.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de barras que representa la $PMF$ de la distribución de Bernoulli.

**Códigos en Python**

```python
from scipy.stats import binom
import numpy as np

# Parámetros de la Distribución de Bernoulli (Distribución Binomial con size=1)
p = 0.1     # Probabilidad de 'éxito' (p en R)
x = 1       # El valor que queremos evaluar (x en R)
size = 1    # Número de ensayos (size en R, lo que define a Bernoulli)

# 1. Función de Masa de Probabilidad (PMF)
# Equivalente a dbinom(x, size=1, prob=p) en R
# Calcula P(X = x)
probabilidad = binom.pmf(k=x, n=size, p=p)
print(f"PMF (P(X={x})): {probabilidad}")
# Resultado: 0.1

# 2. Función de Distribución Acumulativa (CDF)
# Equivalente a pbinom(x, size=1, prob=p) en R
# Calcula P(X <= x)
probabilidad_acumulada = binom.cdf(k=x, n=size, p=p)
print(f"CDF (P(X<={x})): {probabilidad_acumulada}")
# Resultado: P(X=0) + P(X=1) = (1-0.1) + 0.1 = 1.0

# 3. Generación de Muestras Aleatorias (Simulación)
# Equivalente a rbinom(100, size=1, prob=p) en R
# Genera 100 realizaciones de la variable de Bernoulli
n_muestras = 100
simulacion = binom.rvs(n=size, p=p, size=n_muestras)
print(f"Simulación (rvs, 100 muestras): {simulacion[:15]}...")
# Muestra los primeros 15 valores (ejemplo de salida: [0 0 0 1 0 0 0 0 0 0 0 0 0 0 0]...)

# ----------------------------------------------------------------------
# NOTA SOBRE TU EJEMPLO:
# La descripción "Calcular la probabilidad de que un producto dure más de 5500 unidades de tiempo"
# es más adecuada para una distribución continua (como la Exponencial o Uniforme Continua)
# y no para la Distribución de Bernoulli, que solo tiene resultados 0 o 1.
# El código anterior solo calcula la probabilidad de obtener un 'éxito' (x=1) en un ensayo.
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# --- 1. Definir la Distribución de Bernoulli (size=1) ---
p = 0.1     # Probabilidad de éxito (P(X=1))
size = 1    # Número de ensayos (define a Bernoulli)
dist = binom(n=size, p=p)

# --- 2. Preparar los datos para el gráfico ---
# Los únicos valores posibles son 0 y 1
valores = [0, 1]

# Obtener la probabilidad (PMF) para cada valor
probabilidades = dist.pmf(valores)
# P(X=0) = 1 - p = 0.9
# P(X=1) = p = 0.1

# --- 3. Generar el Gráfico ---
plt.figure(figsize=(7, 5))

# Graficar las probabilidades como barras
bars = plt.bar(valores, probabilidades, width=0.4, color=['lightcoral', 'skyblue'], edgecolor='black')

# Añadir etiquetas de probabilidad en la parte superior de cada barra
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, f'{yval:.2f}', ha='center', fontsize=10)

# Configuración y títulos
plt.title(f'Función de Masa de Probabilidad (PMF) - Distribución de Bernoulli (p={p})', fontsize=14)
plt.xlabel('Resultado (0 = Fracaso, 1 = Éxito)', fontsize=12)
plt.ylabel('Probabilidad P(X = x)', fontsize=12)
plt.xticks(valores, ['0 (Fracaso)', '1 (Éxito)'])
plt.ylim(0, 1.1)
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.show()
```

#### Descripción del Código en Python

**Cargar librerías**: Se utiliza scipy.stats para funciones de probabilidad y numpy para generar muestras aleatorias.

**Definir el parámetro de éxito**: Se establece la probabilidad de éxito p (en este caso, 0.1) y el número de ensayos size (en este caso, 1).

**Calcular la PMF**: Se calcula la probabilidad puntual de obtener exactamente x éxitos usando binom.pmf(x, size, p) (equivalente a dbinom en R).

**Calcular la CDF**: Se calcula la probabilidad acumulada de obtener hasta x éxitos usando binom.cdf(x, size, p) (equivalente a pbinom en R).

Generar muestras aleatorias: Se generan 100 observaciones aleatorias de la distribución binomial usando **np.random.binomial**(size, p, 100) (equivalente a rbinom en R).

**Graficar**: Se usa **matplotlib** para crear un gráfico de barras que representa la PMF de la distribución binomial.

**EJERCICIO 1**

Usos recomendados de la distribución de Bernoulli

**Experimentos binarios:**

Lanzamiento de monedas (cara o cruz).

Prueba de yes/no en encuestas o cuestionarios.

Resultado de un test médico (positivo/negativo).

**Modelo base para otras distribuciones**:

La binomial se obtiene como la suma de varias variables Bernoulli independientes.

La geométrica modela el número de ensayos hasta el primer éxito.

**Simulaciones**:

Generar datos sintéticos de eventos que solo pueden tener dos resultados.

Validar algoritmos de clasificación binaria en machine learning.

### 3.30 Distribución Binomial

* **Descripción**: Modelo de $n$ ensayos independientes de Bernoulli.

* **Parámetros**: $n$ (número de ensayos), $p$ (probabilidad de éxito).

* **Función de Masa de Probabilidad (PMF):**
$$
P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}, \quad k = 0, 1, \ldots, n
$$

* **Valor Esperado:** $
E[X] = n \cdot p
$

* **Media:** $\mu_X = n \cdot p$

* **Desviación Estándar:**
$
\sigma = \sqrt{n \cdot p \cdot (1 - p)}
$

* **Función de Distribución Acumulativa (CDF):**

$$
F(x) = P(X \leq k) = \sum \limits_{i=0}^{\lfloor x \rfloor} \binom{n}{i} p^i (1 - p)^{n - i}
$$

* **Comandos en R:**

```r
### 3.31 PMF
dbinom(k, size = n, prob = p)

### 3.32 CDF
pbinom(k, size = n, prob = p)

### 3.33 Simulation
rbinom(n, size = n, prob = p)

#### Ejemplo de Gráfica de la Distribución Binomial

Esta distribución describe el número de éxitos en una serie de ensayos de Bernoulli independientes.

```python
"""
# Cargar la librería necesaria
library(ggplot2)

# Definir los parámetros de la distribución binomial
n <- 10  # Número de ensayos
p <- 0.5  # Probabilidad de éxito en cada ensayo

# Crear un rango de valores para el número de éxitos (k)
k_values <- 0:n

# Calcular la PMF de la distribución binomial
pmf_values <- dbinom(k_values, size = n, prob = p)

# Crear un data frame para ggplot
data <- data.frame(k = k_values, pmf = pmf_values)

# Graficar la distribución binomial
ggplot(data, aes(x = k, y = pmf)) +
  geom_bar(stat = "identity", fill = "blue", alpha = 0.7) +
  labs(title = "Gráfico de la Distribución Binomial",
       x = "Número de Éxitos (k)",
       y = "Probabilidad") +
  theme_minimal() +
  ylim(0, max(pmf_values) + 0.05)
  """
```

```python
# Importar librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom

# Definir los parámetros de la distribución hipergeométrica
M = 50   # Tamaño total de la población (m + n)
n = 20   # Número total de éxitos en la población
N = 15   # Tamaño de la muestra

# Crear un rango de valores para el número de éxitos (x)
x_values = np.arange(0, min(n, N) + 1)

# Calcular la PMF de la distribución hipergeométrica
pmf_values = hypergeom.pmf(x_values, M, n, N)

# Graficar la distribución hipergeométrica
plt.bar(x_values, pmf_values, color='blue', alpha=0.7)
plt.title('Gráfico de la Distribución Hipergeométrica')
plt.xlabel('Número de Éxitos (x)')
plt.ylabel('Probabilidad')
plt.ylim(0, max(pmf_values) + 0.05)
plt.show()
```

#### Descripción del Código

* **Cargar librerías**: Se utiliza `ggplot2` para crear la gráfica.
* **Definir los parámetros**: Se establecen el número de ensayos $ n $ y la probabilidad de éxito $ p $.
* **Crear un rango de valores para $k$**: Se define el rango de valores posibles para el número de éxitos (de $0$ a $ n $).
* **Calcular la PMF**: Se utiliza `dbinom()` para calcular las probabilidades de cada posible número de éxitos.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $ k $ y sus correspondientes probabilidades.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de barras que representa la $PMF$ de la distribución binomial.

**EJERCICIO 2**

Agrega ejemplos y los usos recomendados.

### 3.34 Distribución Hipergeométrica

* **Descripción**: Modelo para muestreo sin reemplazo de una población finita.

* **Parámetros**:
- $N$ (tamaño de la población)
- $K$ (número de éxitos en la población)
- $n$ (tamaño de la muestra)

* **Función de Masa de Probabilidad (PMF):**

$$
P(X = k) = \displaystyle{\frac{\binom{K}{k} \binom{N - K}{n - k}}{\binom{N}{n}}}, \quad k = 0, 1, \ldots, \min(K, n)
$$

* **Valor Esperado:** $E[X] = \frac{nK}{N}$

* **Media:** $\mu_{X} = \frac{nK}{N}$

* **Desviación Estándar:** $\displaystyle{\sigma = \sqrt{\frac{nK(N - K)(N - n)}{N^2(N - 1)}}} $

* **Función de Distribución Acumulativa (CDF):**

$$
F(x) = P(X \leq k) = \sum_{j=0}^{\lfloor x \rfloor} \frac{\binom{K}{j} \binom{N - K}{n - j}}{\binom{N}{n}}
$$

* ** Comandos en R:**

```r
### 3.35 PMF
dhyper(k, m = K, n = N - K, size = n)

### 3.36 CDF
phyper(k, m = K, n = N - K, size = n)

### 3.37 Simulation
rhyper(n, m = K, n = N - K, size = n)

#### Ejemplo de Gráfica de la Distribución Hipergeométrica

Esta distribución describe el número de éxitos en una muestra extraída sin reemplazo de una población finita.

```python
""" # Cargar la librería necesaria
library(ggplot2)

# Definir los parámetros de la distribución hipergeométrica
m <- 20  # Número total de éxitos en la población
n <- 30  # Número total de fracasos en la población
k <- 15  # Tamaño de la muestra

# Crear un rango de valores para el número de éxitos (x)
x_values <- 0:min(m, k)

# Calcular la PMF de la distribución hipergeométrica
pmf_values <- dhyper(x_values, m, n, k)

# Crear un data frame para ggplot
data <- data.frame(x = x_values, pmf = pmf_values)

# Graficar la distribución hipergeométrica
ggplot(data, aes(x = x, y = pmf)) +
  geom_bar(stat = "identity", fill = "blue", alpha = 0.7) +
  labs(title = "Gráfico de la Distribución Hipergeométrica",
       x = "Número de Éxitos (x)",
       y = "Probabilidad") +
  theme_minimal() +
  ylim(0, max(pmf_values) + 0.05)
"""
```

```python
# Importar librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom

# Definir los parámetros de la distribución hipergeométrica
m = 20   # Número total de éxitos en la población
n = 30   # Número total de fracasos en la población
k = 15   # Tamaño de la muestra
M = m + n  # Tamaño total de la población

# Crear un rango de valores para el número de éxitos (x)
x_values = np.arange(0, min(m, k) + 1)

# Calcular la PMF de la distribución hipergeométrica
pmf_values = hypergeom.pmf(x_values, M, m, k)

# Graficar la distribución hipergeométrica
plt.bar(x_values, pmf_values, color='blue', alpha=0.7)
plt.title('Gráfico de la Distribución Hipergeométrica')
plt.xlabel('Número de Éxitos (x)')
plt.ylabel('Probabilidad')
plt.ylim(0, max(pmf_values) + 0.05)
plt.show()
```

#### Descripción del Código

* **Cargar librerías**: Se utiliza `ggplot2` para crear la gráfica.
* **Definir los parámetros**: Se establecen los parámetros de la distribución hipergeométrica: el número total de éxitos en la población $m$, el número total de fracasos $ n$ y el tamaño de la muestra $k$.
* **Crear un rango de valores para $ x $**: Se define el rango de valores posibles para el número de éxitos en la muestra, que va de 0 al mínimo entre $ m $ y $ k $.
* **Calcular la PMF**: Se utiliza `dhyper()` para calcular las probabilidades de cada posible número de éxitos en la muestra.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $ x $ y sus correspondientes probabilidades.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de barras que representa la $PMF$ de la distribución hipergeométrica.

**EJERCICIO 3**

Ejemplo: Sacar 3 cartas de una baraja de 10 rojas y 40 negras, y contar cuántas son rojas.

Uso recomendado: Muestras sin reemplazo.

Código en Python:

```python
from scipy.stats import hypergeom

M, n, N = 50, 10, 3  # población total, éxitos en población, tamaño de muestra
x = range(0, 4)
pmf = hypergeom.pmf(x, M, n, N)
print(pmf)
```

### 3.38 Distribución Geométrica

* **Descripción**: Modelo de la cantidad de ensayos necesarios para obtener el primer éxito.

* **Parámetro**: $p$ (probabilidad de éxito en cada ensayo).

* **Función de Masa de Probabilidad (PMF):**

$$
P(X = k) = (1 - p)^{k - 1} p, \quad k = 1, 2, \ldots
$$

* **Valor Esperado:** $
E[X] = \frac{1}{p}
$

* **Media:** $\mu_{X} = \frac{1}{p}$

* **Desviación Estándar:** $ \sigma = \sqrt{\frac{1 - p}{p}}$

* **Función de Distribución Acumulativa (CDF):**

$$
F(x) = P(X \leq k) = 1 - (1 - p)^k, \quad k = 1, 2, \ldots
$$

* **Comandos en R**:

```r
### 3.39 PMF
dgeom(k - 1, prob = p)

### 3.40 CDF
pgeom(k - 1, prob = p)

### 3.41 Simulation
rgeom(n, prob = p)

#### Ejemplo de Gráfica de la Distribución Geométrica

Esta distribución describe el número de ensayos hasta el primer éxito en una serie de ensayos de Bernoulli.

```python
""" # Cargar la librería necesaria
library(ggplot2)

# Definir el parámetro de éxito (p)
p <- 0.3  # Probabilidad de éxito en cada ensayo

# Crear un rango de valores para el número de ensayos (k)
k_values <- 0:10  # Considerar hasta 10 ensayos

# Calcular la PMF de la distribución geométrica
pmf_values <- dgeom(k_values, prob = p)

# Crear un data frame para ggplot
data <- data.frame(k = k_values, pmf = pmf_values)

# Graficar la distribución geométrica
ggplot(data, aes(x = k, y = pmf)) +
  geom_bar(stat = "identity", fill = "blue", alpha = 0.7) +
  labs(title = "Gráfico de la Distribución Geométrica",
       x = "Número de Ensayos (k)",
       y = "Probabilidad") +
  theme_minimal() +
  ylim(0, max(pmf_values) + 0.05)"""
```

```python
# Importar librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom

# Definir el parámetro de éxito
p = 0.3  # Probabilidad de éxito en cada ensayo

# Crear un rango de valores para el número de ensayos (k)
k_values = np.arange(0, 11)  # Considerar hasta 10 ensayos

# Calcular la PMF de la distribución geométrica
# Nota: En scipy geom, el soporte es k=1,2,... por lo que usamos k+1
pmf_values = geom.pmf(k_values + 1, p)

# Graficar la distribución geométrica
plt.bar(k_values, pmf_values, color='blue', alpha=0.7)
plt.title('Gráfico de la Distribución Geométrica')
plt.xlabel('Número de Ensayos (k)')
plt.ylabel('Probabilidad')
plt.ylim(0, max(pmf_values) + 0.05)
plt.show()
```

#### Descripción del Código

* **Cargar librerías**: Se utiliza `ggplot2` para crear la gráfica.
* **Definir el parámetro de éxito**: Se establece la probabilidad de éxito $ p $ en cada ensayo.
* **Crear un rango de valores para $ k $**: Se define el rango de valores posibles para el número de ensayos hasta el primer éxito (de $0$ a $10$).
* **Calcular la PMF**: Se utiliza `dgeom()` para calcular las probabilidades de cada posible número de ensayos.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $ k $ y sus correspondientes probabilidades.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de barras que representa la $PMF$ de la distribución geométrica.

**EJERCICIO 4**
Ejemplo: Número de lanzamientos hasta obtener la primera cara.

Uso recomendado: Cuando buscas el primer éxito.

Código en Python:

```python
from scipy.stats import geom

p = 0.3
x = range(1, 11)  # número de intentos hasta el primer éxito
pmf = geom.pmf(x, p)
print(pmf)
```

### 3.42 Distribución Negativa Binomial

* **Descripción**: Modelo de la cantidad de ensayos necesarios para obtener un número fijo de éxitos (generaliza la distribución geométrica).

* **Parámetros**:
- $r$ (número de éxitos deseados)
- $p$ (probabilidad de éxito)

* **Función de Masa de Probabilidad (PMF):**

$$
P(X = k) = \binom{k + r - 1}{r - 1} p^r (1 - p)^{k}, \quad k = 0, 1, 2, \ldots
$$

* **Valor Esperado:** $E[X] = \frac{r(1 - p)}{p}$

* **Media:** $\mu{X} = \frac{r(1 - p)}{p}$

* **Desviación Estándar:** $ \sigma = \sqrt{\frac{r(1 - p)}{p^2}}$

* **Función de Distribución Acumulativa (CDF):**

$$
F(x) = P(X \leq k) = \sum_{j=0}^{\lfloor x \rfloor} \binom{j + r - 1}{r - 1} p^r (1 - p)^{j}
$$

* **Comandos en R**:

```r
### 3.43 PMF
dnbinom(k, size = r, prob = p)

### 3.44 CDF
pnbinom(k, size = r, prob = p)

### 3.45 Simulación
rnbinom(n, size = r, prob = p)

#### Ejemplo de Gráfica de la Distribución Negativa Binomial
Esta distribución describe el número de ensayos hasta que se obtienen un número fijo de éxitos.

```python
""" # Cargar la librería necesaria
library(ggplot2)

# Definir los parámetros de la distribución negativa binomial
size <- 5  # Número de éxitos deseados
prob <- 0.4  # Probabilidad de éxito en cada ensayo

# Crear un rango de valores para el número de ensayos (k)
k_values <- 0:30  # Considerar hasta 30 ensayos

# Calcular la PMF de la distribución negativa binomial
pmf_values <- dnbinom(k_values, size = size, prob = prob)

# Crear un data frame para ggplot
data <- data.frame(k = k_values, pmf = pmf_values)

# Graficar la distribución negativa binomial
ggplot(data, aes(x = k, y = pmf)) +
  geom_bar(stat = "identity", fill = "blue", alpha = 0.7) +
  labs(title = "Gráfico de la Distribución Negativa Binomial",
       x = "Número de Ensayos (k)",
       y = "Probabilidad") +
  theme_minimal() +
  ylim(0, max(pmf_values) + 0.05)
  """
```

```python
# Importar librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nbinom

# Definir los parámetros de la distribución binomial negativa
size = 5   # Número de éxitos deseados
prob = 0.4 # Probabilidad de éxito en cada ensayo

# Crear un rango de valores para el número de ensayos (k)
k_values = np.arange(0, 31)  # Considerar hasta 30 ensayos

# Calcular la PMF de la distribución binomial negativa
# Nota: En scipy, nbinom cuenta el número de fracasos antes de obtener 'size' éxitos
pmf_values = nbinom.pmf(k_values, size, prob)

# Graficar la distribución negativa binomial
plt.bar(k_values, pmf_values, color='blue', alpha=0.7)
plt.title('Gráfico de la Distribución Negativa Binomial')
plt.xlabel('Número de Ensayos (k)')
plt.ylabel('Probabilidad')
plt.ylim(0, max(pmf_values) + 0.05)
plt.show()
```

#### Descripción del Código

* **Cargar librerías**: Se utiliza `ggplot2` para crear la gráfica.
* **Definir los parámetros**: Se establecen el número de éxitos deseados $size $ y la probabilidad de éxito $ prob $ en cada ensayo.
* **Crear un rango de valores para $ k $**: Se define el rango de valores posibles para el número de ensayos hasta que se obtienen el número especificado de éxitos (de $0$ a $30$).
* **Calcular la PMF**: Se utiliza `dnbinom()` para calcular las probabilidades de cada posible número de ensayos.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $ k $ y sus correspondientes probabilidades.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de barras que representa la $PMF$ de la distribución negativa binomial.

**EJERCICIO 5**

Ejemplo: Número de lanzamientos hasta obtener 5 caras.

Uso recomendado: Extensión de la geométrica, éxito repetido hasta r veces.

Código en Python:

```python
from scipy.stats import nbinom

r, p = 5, 0.4
x = range(0, 31)  # intentos hasta 5 éxitos
pmf = nbinom.pmf(x, r, p)
print(pmf)
```

### 3.46 Distribución Multinomial

* **Descripción**: Extensión de la distribución binomial a más de dos resultados.

* **Parámetros**:
- $n$ (número de ensayos)
- $p_1, p_2, \ldots, p_k$ (probabilidades de cada resultado)

* **Función de Masa de Probabilidad (PMF):**

$$
P(X_1 = k_1, X_2 = k_2, \ldots, X_k = k_k) = \frac{n!}{k_1! k_2! \ldots k_k!} p_1^{k_1} p_2^{k_2} \ldots p_k^{k_k}
$$

* **Valor Esperado:** $E[X_i] = n \cdot p_i, \quad i = 1, 2, \ldots, k$

* **Media:** $ \mu{X} = n \cdot p_i \quad \text{para cada } i$

* **Desviación Estándar:** $\sigma_i = \sqrt{n \cdot p_i \cdot (1 - p_i)}, \quad i = 1, 2, \ldots, k$

* **Función de Distribución Acumulativa (CDF):**

(No existe una fórmula general simple; se utiliza el enfoque de simulación.)

* **Comandos en R:**

```r
### 3.47 PMF
dmultinom(c(k1, k2, ..., kk), size = n, prob = c(p1, p2, ..., pk))

### 3.48 CDF (no hay función directa)

### 3.49 Simulación
rmultinom(n, size = n, prob = c(p1, p2, ..., pk))

#### Ejemplo de Gráfica de la Distribución Distribución Multinomial

Esta distribución describe el número de éxitos en un experimento con múltiples categorías.

```python
""" # Instalar las librerías necesarias (descomentar si es necesario)
# install.packages('plyr')
# install.packages('reshape2')

# Cargar las librerías necesarias
library(ggplot2)
library(plyr)
library(reshape2)

# Definir los parámetros de la distribución multinomial
n <- 20  # Número total de ensayos
probabilities <- c(0.2, 0.5, 0.3)  # Probabilidades para cada categoría

# Crear una matriz de resultados posibles (número de éxitos en cada categoría)
results <- expand.grid(
  x1 = 0:n,
  x2 = 0:n,
  x3 = 0:n
)

# Filtrar solo las combinaciones válidas que sumen n
results <- results[rowSums(results) == n, ]

# Calcular la PMF para cada combinación usando dmultinom
results$pmf <- apply(results, 1, function(row) {
  dmultinom(row, size = n, prob = probabilities)
})

# Convertir los resultados a formato largo
results_long <- melt(results, id.vars = "pmf")

# Crear el gráfico
plot <- ggplot(results_long, aes(x = variable, y = value, fill = variable)) +
  geom_bar(stat = "identity") +
  labs(title = "Gráfico de la Distribución Multinomial",
       x = "Categoría",
       y = "Número de Éxitos") +
  theme_minimal() +
  facet_wrap(~pmf) +
  scale_fill_manual(values = c("blue", "red", "green"))

# Mostrar el gráfico en un tamaño grande
print(plot)

# Guardar el gráfico como un archivo PNG con tamaño especificado
ggsave("grafico_multinomial.png", plot, width = 20, height = 14)  # Ajusta el tamaño según lo necesites
"""
```

```python
import numpy as np
import pandas as pd
from scipy.stats import multinomial
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import product

# Parámetros de la distribución multinomial
n = 20  # Número total de ensayos
probabilities = [0.2, 0.5, 0.3]  # Probabilidades para cada categoría

# Generar todas las combinaciones posibles de éxitos (x1, x2, x3)
x1_range = range(n + 1)
x2_range = range(n + 1)
x3_range = range(n + 1)

# Crear combinaciones válidas que sumen n
combinations = [c for c in product(x1_range, x2_range, x3_range) if sum(c) == n]

# Calcular la PMF de cada combinación
pmf_values = [multinomial.pmf(c, n, probabilities) for c in combinations]

# Crear un DataFrame
df = pd.DataFrame(combinations, columns=['x1', 'x2', 'x3'])
df['pmf'] = pmf_values

# Convertir a formato largo para graficar
df_long = df.melt(id_vars='pmf', value_vars=['x1','x2','x3'], var_name='Categoría', value_name='Número de Éxitos')

# Graficar
plt.figure(figsize=(20, 14))
sns.barplot(data=df_long, x='Categoría', y='Número de Éxitos', hue='Categoría')
plt.title("Gráfico de la Distribución Multinomial")
plt.xlabel("Categoría")
plt.ylabel("Número de Éxitos")
plt.show()
```

```python
"""# Instalar las librerías necesarias (descomentar si es necesario)
# install.packages('plyr')
# install.packages('reshape2')

# Cargar las librerías necesarias
library(ggplot2)
library(plyr)
library(reshape2)

# Verificar el directorio de trabajo
getwd()

# Definir los parámetros de la distribución multinomial
n <- 4  # Número total de éxitos
probabilities <- c(0.3, 0.5, 0.2)  # Probabilidades para cada categoría

# Crear una matriz de resultados posibles (número de éxitos en cada categoría)
results <- expand.grid(
  x1 = 0:n,
  x2 = 0:n,
  x3 = 0:n
)

# Filtrar solo las combinaciones válidas que sumen n
results <- results[rowSums(results) == n, ]

# Calcular la PMF para cada combinación usando dmultinom
results$pmf <- apply(results, 1, function(row) {
  dmultinom(row, size = n, prob = probabilities)
})

# Convertir los resultados a formato largo
results_long <- melt(results, id.vars = "pmf")

# Crear el gráfico
plot <- ggplot(results_long, aes(x = variable, y = value, fill = variable)) +
  geom_bar(stat = "identity") +
  labs(title = "Gráfico de la Distribución Multinomial (4 Éxitos, 3 Categorías)",
       x = "Categoría",
       y = "Número de Éxitos") +
  theme_minimal() +
  facet_wrap(~pmf) +
  scale_fill_manual(values = c("blue", "red", "green"))

# Mostrar el gráfico en un tamaño grande
print(plot)

# Guardar el gráfico como un archivo PNG con tamaño especificado
ggsave("grafico_multinomial_4_exitos.png", plot, width = 12, height = 8)  # Ajusta el tamaño según lo necesites
"""
```

```python
import numpy as np
import pandas as pd
from itertools import product
from scipy.stats import multinomial
import matplotlib.pyplot as plt
import seaborn as sns

# Parámetros de la distribución multinomial
n = 4  # Número total de éxitos
probabilities = [0.3, 0.5, 0.2]  # Probabilidades para cada categoría

# Generar todas las combinaciones posibles de éxitos (x1, x2, x3)
x1_range = range(n + 1)
x2_range = range(n + 1)
x3_range = range(n + 1)

# Filtrar combinaciones válidas que sumen n
combinations = [c for c in product(x1_range, x2_range, x3_range) if sum(c) == n]

# Calcular la PMF de cada combinación
pmf_values = [multinomial.pmf(c, n, probabilities) for c in combinations]

# Crear DataFrame
df = pd.DataFrame(combinations, columns=['x1','x2','x3'])
df['pmf'] = pmf_values

# Convertir a formato largo para graficar
df_long = df.melt(id_vars='pmf', value_vars=['x1','x2','x3'], var_name='Categoría', value_name='Número de Éxitos')

# Graficar con seaborn
g = sns.FacetGrid(df_long, col='pmf', col_wrap=4, sharex=True, sharey=True, height=3)
g.map_dataframe(sns.barplot, x='Categoría', y='Número de Éxitos', hue='Categoría', palette=['blue','red','green'])
g.set_titles(col_template="PMF = {col_name:.4f}")
g.set_axis_labels("Categoría", "Número de Éxitos")
g.add_legend()
plt.show()

# Guardar el gráfico como PNG
g.savefig("grafico_multinomial_4_exitos.png", dpi=300)
```

#### **Descripción del Código**:

* **Número total de éxitos**: Se establece en $n \leftarrow 4$.
* **Probabilidades**: Se definen para cada categoría.
* **Filtrado de combinaciones**: Se obtiene solo aquellas combinaciones que suman $4$ éxitos.
* **Cálculo de PMF**: Utilizando la función `dmultinom`.
* **Gráfico**: Se genera y se guarda como un archivo PNG.

---

**Cómo se lee el gráfico**:

Aquí tienes una guía sobre cómo interpretar el gráfico de la distribución multinomial que generamos:

**Elementos del Gráfico**:
- **Ejes**:
  - **Eje X (Categoría)**: Muestra las diferentes categorías en las que se distribuyen los éxitos. En nuestro caso, hay tres categorías ($x_1$, $x_2$, $x_3$).
  - **Eje Y (Número de Éxitos)**: Muestra la cantidad de éxitos que se pueden observar en cada categoría.

- **Barras**:
  - Cada barra representa el número de éxitos para una categoría específica. La altura de la barra indica la cantidad de veces que se espera que ocurra ese número de éxitos, dado el total de 4 éxitos distribuidos entre las $3$ categorías.

- **Colores**:
  - Cada barra tiene un color diferente (azul, rojo, verde) para facilitar la identificación de las categorías.

- **Facet Wrap**:
  - El gráfico también utiliza `facet_wrap(~pmf)`, lo que significa que podría haber varios paneles dependiendo de los valores de PMF calculados. Esto puede ayudarte a visualizar diferentes combinaciones de éxitos y sus probabilidades.

**Interpretación**:
- **Probabilidades**: Las alturas de las barras representan las probabilidades calculadas de que se produzcan ciertas combinaciones de éxitos en las categorías.
- **Combinaciones Válidas**: Solo se muestran combinaciones que suman el total de éxitos (en este caso, 4). Por ejemplo, una barra que muestra $2$ éxitos en la categoría $x_1$, $1$ en $x_2$ y $1$ en $x_3$ significa que hay una combinación de eventos que distribuye los $4$ éxitos de esta manera.
- **Decisiones de Probabilidad**: Si estás analizando un experimento o una situación, puedes usar este gráfico para entender cómo se distribuyen las probabilidades de éxito entre las diferentes categorías y tomar decisiones basadas en esa información.

**Ejemplo Práctico**:
Si en tu gráfico observas que hay una barra alta para la categoría $x_2$ (por ejemplo, con $3$ éxitos), eso sugiere que es más probable que en tus experimentos obtengas un número mayor de éxitos en esa categoría, dado el modelo y las probabilidades elegidas.

---

**Por qué hay barras que tienen tamaño $5$ junto con otra de tamaño $3$ en el mismo gráfico**:

Las barras en el gráfico de la distribución multinomial representan las combinaciones de éxitos en cada categoría, y sus alturas son el resultado de las probabilidades de esas combinaciones específicas. Aquí hay algunas razones por las que esto puede ocurrir:

1. **Combinaciones de Éxitos**:
   - Cada barra representa una combinación de éxitos en las diferentes categorías. Por ejemplo, si tienes:
     - Categoría $1$ ($x_1$): $3$ éxitos
     - Categoría $2$ ($x_2$): $1$ éxito
     - Categoría $3$ ($x_3$): $0$ éxitos
   - Esto sumaría un total de $4$ éxitos, pero también podría haber otra combinación como:
     - Categoría $1$ ($x_1$): $1$ éxito
     - Categoría $2$ ($x_2$): $3$ éxitos
     - Categoría $3$ ($x_3$): $0$ éxitos
   - Ambas combinaciones son válidas y suman el mismo total de éxitos ($4$), pero su representación en el gráfico puede mostrar distintas alturas en las barras.

2. **Diferencias en la Probabilidad**:
   - La altura de cada barra está determinada por la probabilidad de que ocurran esas combinaciones específicas de éxitos. Esto significa que:
     - La combinación que resulta en $5$ (o más) puede ser más probable que otras combinaciones que suman el mismo total de éxitos.

3. **Efecto de las Probabilidades**:
   - Las probabilidades asignadas a cada categoría (en este caso, $0.3$, $0.5$ y $0.2$) influencian fuertemente el tamaño de las barras. Si una categoría tiene una probabilidad mayor, es más probable que se observe un número mayor de éxitos en esa categoría, lo que puede dar lugar a combinaciones que parecen desproporcionadas en el gráfico.

---

**Los números que aparecen arriba de cada gráfico de barras**:

Los números que aparecen arriba de cada gráfico de barras representan las probabilidades asociadas a cada combinación específica de éxitos en las diferentes categorías. Aquí tienes un desglose de lo que significan:

- **Probabilidades de Combinaciones**: Cada número indica la probabilidad de que ocurra la combinación específica de éxitos en las categorías representadas por las barras.
- **Escala de Probabilidad**: Estas probabilidades se calculan utilizando la función `dmultinom`, donde $0$ significa que esa combinación de éxitos es imposible y $1$ significa que es un evento seguro.
- **Interpretación Contextual**: Al observar estos números, puedes entender qué combinaciones son más probables y cuáles son menos probables.

**EJERCICIO 6**

Ejemplo: Lanzar 4 dados y contar cuántas veces sale cada número (1,2,3).

Uso recomendado: Experimentos con más de 2 categorías.

Código en Python:

```python
import numpy as np
from scipy.stats import multinomial

n = 4
p = [0.3, 0.5, 0.2]
x = [1, 2, 1]  # ejemplo de conteo de éxitos por categoría
pmf = multinomial.pmf(x, n, p)
print(pmf)
```

### 3.50 Distribución de Poisson

* **Descripción**: Modelo de eventos que ocurren en un intervalo fijo de tiempo o espacio.

* **Parámetro**: $\lambda$ (tasa promedio de ocurrencias).

* **Función de Masa de Probabilidad (PMF):**

$$
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \ldots
$$

* **Valor Esperado:** $
E[X] = \lambda
$

* **Media:** $ \mu_X = \lambda$

* **Desviación Estándar:** $\sigma = \sqrt{\lambda}$

* **Función de Distribución Acumulativa (CDF):**

$$
F(x) = P(X \leq k) = \sum_{i=0}^{\lfloor x \rfloor} \frac{\lambda^i e^{-\lambda}}{i!}
$$

* **Comandos en R**:

```r
### 3.51 PMF
dpois(x, lambda)

### 3.52 CDF
ppois(x, lambda)

### 3.53 Simulation
rpois(n, lambda)

#### Ejemplo de Gráfica de la Distribución de Poisson

Esta distribución describe el número de eventos que ocurren en un intervalo fijo de tiempo o espacio, dado un promedio de eventos conocido.

```python
"""2# Cargar la librería necesaria
library(ggplot2)

# Definir el parámetro lambda (promedio de eventos)
lambda <- 4  # Promedio de eventos por intervalo

# Crear un rango de valores para el número de eventos (k)
k_values <- 0:15  # Considerar hasta 15 eventos

# Calcular la PMF de la distribución de Poisson
pmf_values <- dpois(k_values, lambda = lambda)

# Crear un data frame para ggplot
data <- data.frame(k = k_values, pmf = pmf_values)

# Graficar la distribución de Poisson
ggplot(data, aes(x = k, y = pmf)) +
  geom_bar(stat = "identity", fill = "blue", alpha = 0.7) +
  labs(title = "Gráfico de la Distribución de Poisson",
       x = "Número de Eventos (k)",
       y = "Probabilidad") +
  theme_minimal() +
  ylim(0, max(pmf_values) + 0.05)
"""
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Definir el parámetro lambda (promedio de eventos)
lambda_ = 4  # Promedio de eventos por intervalo

# Crear un rango de valores para el número de eventos (k)
k_values = np.arange(0, 16)  # De 0 a 15 eventos

# Calcular la PMF de la distribución de Poisson
pmf_values = poisson.pmf(k_values, mu=lambda_)

# Graficar la distribución de Poisson
plt.bar(k_values, pmf_values, color='blue', alpha=0.7)
plt.title("Gráfico de la Distribución de Poisson")
plt.xlabel("Número de Eventos (k)")
plt.ylabel("Probabilidad")
plt.ylim(0, max(pmf_values) + 0.05)
plt.show()
```

#### Descripción del Código

* **Cargar librerías**: Se utiliza `ggplot2` para crear la gráfica.
* **Definir el parámetro**: Se establece el valor de $\lambda$, que es el promedio de eventos por intervalo.
* **Crear un rango de valores para $ k$**: Se define el rango de valores posibles para el número de eventos (de $0$ a $15$).
* **Calcular la PMF**: Se utiliza `dpois()` para calcular las probabilidades de cada posible número de eventos.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $ k $ y sus correspondientes probabilidades.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de barras que representa la $PMF$ de la distribución de Poisson.

**EJERCICIO 7**

Agrega ejemplos y los usos recomendados.

Ejemplo: Número de autos que pasan por un cruce en una hora.

Uso recomendado: Eventos raros o discretos por unidad de tiempo o espacio.

Código en Python:

```python
from scipy.stats import poisson

lambda_ = 4
x = range(0, 16)
pmf = poisson.pmf(x, lambda_)
print(pmf)
```

---

### 3.54 🏫 Universidad de La Ciénega del Estado de Michoacán de Ocampo 🏫

### 3.55 🔬 Ingenieria en Nanotecnología 🔬

3° "A"

🧑🏻‍🏫 Profesor: Luis José Yudico Anaya 🧑🏻‍🏫

📍 Sahuayo, Michoacán a 08 de octubre del 2025 📍

El Capítulo 3 del material fuente se titula **"Variables Aleatorias Discretas"** y se enfoca en establecer un puente entre las herramientas abstractas de probabilidad (el espacio de probabilidad $(\Omega, \mathcal{F}, P)$) y las habilidades prácticas del procesamiento de datos.

El capítulo desarrolla los siguientes conceptos clave y secciones:

### 3.1 Variables Aleatorias (Random Variables)

La **variable aleatoria $X$** se define formalmente como una función $X: \Omega \to \mathbb{R}$ que mapea un resultado $\xi \in \Omega$ a un número $X(\xi)$ en la línea real.

*   **Propósito:** La variable aleatoria es el primer paso para hacer que el espacio de probabilidad abstracto sea más conveniente, ya que **convierte una "declaración" o un evento a un número** (Concepto Clave 1). Por ejemplo, en un lanzamiento de moneda, $X(\text{cara}) = 1$ y $X(\text{cruz}) = 0$.
*   **Probabilidad y Preimagen:** Cuando se escribe $P[X=a]$, esto equivale a preguntar por el tamaño del conjunto $E = \{\xi \in \Omega \mid X(\xi) = a\}$ (la preimagen de $a$), y este tamaño es medido por la ley de probabilidad $P$.
*   **Estados:** La variable $X$ se llama "variable" porque tiene múltiples *estados* posibles, que son los números que puede tomar.

### 3.2 Función de Masa de Probabilidad (Probability Mass Function, PMF)

La **Función de Masa de Probabilidad (PMF)**, denotada $p_X(x)$, es una función que resume las probabilidades de los estados, especificando la probabilidad de obtener un número $X(\xi) = x$.

*   **Diferencia clave (Concepto Clave 2):** Las PMF son los **histogramas ideales** de las variables aleatorias. Un histograma generado a partir de un conjunto de datos es un *histograma empírico* que se acerca a la PMF ideal a medida que el número de muestras ($N$) tiende al infinito.
*   **Propiedad de Normalización:** Toda PMF debe satisfacer la condición de que la suma de todas las probabilidades es igual a 1: $\sum_{x \in X(\Omega)} p_X(x) = 1$.

### 3.3 Funciones de Distribución Acumulada (Cumulative Distribution Functions, CDF)

La **Función de Distribución Acumulada (CDF)** de una variable aleatoria discreta $X$ es la suma acumulada de la PMF desde $-\infty$ hasta $x$: $F_X(x_k) \stackrel{\text{def}}{=} P[X \le x_k] = \sum_{\ell=1}^{k} p_X(x_\ell)$.

*   **Características:** La CDF de una variable discreta es una **función escalonada**.
*   **Propiedades:** Es no decreciente, tiene un valor mínimo de 0 cuando $x=-\infty$ y un valor máximo de 1 cuando $x=+\infty$.
*   **Conversión:** La PMF se puede obtener a partir de la CDF mediante la diferencia de los valores de la CDF en puntos consecutivos: $p_X(k) = F_X(k) - F_X(k-1)$.

### 3.4 Esperanza (Expectation)

La **esperanza** formaliza el concepto de promedio de una variable aleatoria.

*   **Definición (Concepto Clave 3):** La **Expectativa** es la Media o el Promedio calculado a partir de una PMF: $E[X] = \sum_{x \in X(\Omega)} x p_X(x)$.
*   **Interpretación:** La esperanza $E[X]$ es el "verdadero promedio" de una variable aleatoria, obtenido del histograma ideal, a diferencia del promedio muestral (sample average) que proviene del histograma empírico.
*   **Concepto de Masa:** La esperanza puede interpretarse como el **centro de masa** de la distribución.
*   **Propiedades:** La esperanza es lineal, lo que significa que $E[g(X) + h(X)] = E[g(X)] + E[h(X)]$ y $E[cX] = cE[X]$.
*   **Momentos y Varianza:** El $k$-ésimo momento de $X$ es $E[X^k]$. La **Varianza** mide la dispersión y se calcula como $\operatorname{Var}[X] = E[X^2] - E[X]^2$. La varianza cumple con $\operatorname{Var}[cX] = c^2 \operatorname{Var}[X]$ y $\operatorname{Var}[X+c] = \operatorname{Var}[X]$.

### 3.5 Variables Aleatorias Discretas Comunes

Esta sección presenta modelos probabilísticos fundamentales desde una perspectiva generativa:

1.  **Variable Aleatoria Bernoulli:** Modela un experimento con dos estados (binarios, 0 o 1), como el lanzamiento de una moneda.
    *   PMF: $p_X(1)=p$ y $p_X(0)=1-p$.
    *   Media: $p$. Varianza: $p(1-p)$.
    *   La varianza se maximiza cuando $p=1/2$, ya que la incertidumbre es máxima en un evento justo. Se utiliza para modelar la conectividad en redes, como el grafo de Erdős-Rényi.

2.  **Variable Aleatoria Binomial:** Representa la suma de $n$ ensayos de Bernoulli independientes.
    *   PMF: $p_X(k) = \binom{n}{k} p^k (1-p)^{n-k}$, donde $\binom{n}{k}$ es el número de combinaciones de $k$ éxitos en $n$ intentos.
    *   Media: $np$. Varianza: $np(1-p)$.

3.  **Variable Aleatoria Geométrica:** Modela el número de ensayos ($k$) necesarios para obtener el primer éxito en una secuencia de ensayos de Bernoulli.
    *   PMF: $p_X(k) = (1-p)^{k-1}p$ para $k=1, 2, \dots$.
    *   Media: $1/p$.

4.  **Variable Aleatoria de Poisson:** Se utiliza para modelar la llegada de eventos, como la llegada de fotones en fotografía o el tráfico de Internet.
    *   PMF: $p_X(k) = \frac{\lambda^k}{k!} e^{-\lambda}$, donde $\lambda$ es el parámetro.
    *   Media: $\lambda$. Varianza: $\lambda$.
    *   La distribución de Poisson es una **aproximación** a la distribución Binomial cuando $n$ es grande y $p$ es pequeño, con $\lambda = np$.

##**UCEMICH** 13/10/25

### 3.6 TEMA: DISTRIBUCIONES DE PROBABILIDAD CON PYTHON

### 3.7 MODELOS PARA VARIABLES ALEATORIAS EN PYTHON Y EN R

https://es.wikipedia.org/wiki/Distribuci%C3%B3n_de_probabilidad

```python
import numpy as np
from numpy.random import binomial #generador aleatorio de numeros basados ​​en la distro binomial
from scipy.stats import binom #distro teorica
from math import factorial
import matplotlib.pyplot as plt #visualizaciones
from scipy import stats
from scipy import optimize
import seaborn as sns
sns.set(style="whitegrid")
```

Generación de numeros aleatorios

```python
np.random.rand()
```

```python
np.random.randn()
```

```python
np.random.randint(100)
```

```python
np.random.rand(5)
```

```python
np.random.randn(2, 4)
```

```python
np.random.randint(10, size=10)
```

```python
np.random.randint(low=10, high=20, size=(2, 10))
```

```python
np.random.choice(10, 5, replace=False)
```

```python
np.random.choice(10, 5, replace=True)
```

La semilla del generador de números aleatorios, es una función que permite obtener los mismos resultados de experimento aleatorio:

```python
np.random.rand()
```

```python
np.random.rand()
```

```python
np.random.seed(123456789)
np.random.rand()
```

In addition to the fundamental random number distributions we have looked at so
far (discrete and continuous uniform distributions, randint and rand, and the standard
normal distribution, randn), there are also functions, and RandomState methods, for
a large number of probability distributions that occur in statistics. To mention just a
few, there is the continuous χ2

distribution (chisquare), the Student’s t distribution

(standard_t), and the F distribution (f):

https://thedataschools.com/

### 3.8 Modelos para Variables Aleatorias Discretas

### 3.9 Listado de las distribuciones de probabilidad discretas más utilizadas

En las diversas disciplinas de nanotecnología, ciencias de los materiales, inteligencia artificial, diseño de experimentos y pruebas de hipótesis, se destacan las siguientes distribuciones de probabilidad discretas, organizadas por tema:

##### Nanotecnología

1. **Distribución de Poisson**
   - **Uso**: Modelar el número de eventos en un intervalo fijo de tiempo o espacio.
   - **Ejemplo**: Número de defectos encontrados en un lote de nanopartículas, donde se espera que ocurran defectos de manera independiente y con una tasa constante.

2. **Distribución Binomial**
   - **Uso**: Modelar el número de éxitos en una serie de ensayos independientes.
   - **Ejemplo**: Evaluar la efectividad de un recubrimiento en nanopartículas, donde se cuenta el número de partículas que logran un recubrimiento exitoso tras varios intentos.

3. **Distribución Geométrica**
   - **Uso**: Modelar el número de ensayos hasta el primer éxito.
   - **Ejemplo**: Determinar cuántas veces se necesita aplicar un proceso de recubrimiento antes de lograr una nanopartícula con el recubrimiento deseado.

##### Ciencias de los Materiales

1. **Distribución Binomial Negativa**
   - **Uso**: Modelar el número de fracasos antes de alcanzar un número fijo de éxitos.
   - **Ejemplo**: Número de pruebas necesarias para obtener un número específico de componentes con la resistencia adecuada en un material.

2. **Distribución Hipergeométrica**
   - **Uso**: Modelar la probabilidad de éxito en muestras sin reemplazo.
   - **Ejemplo**: Selección de un número específico de materiales de un lote, donde se evalúa cuántos cumplen con las especificaciones requeridas sin reponer los seleccionados.

3. **Distribución de Poisson**
   - **Uso**: Modelar eventos raros en un intervalo.
   - **Ejemplo**: Cantidad de fracturas en un material sometido a estrés, donde los eventos son relativamente raros en un período de tiempo específico.

##### Inteligencia Artificial

1. **Distribución de Bernoulli**
   - **Uso**: Modelar experimentos con dos resultados posibles.
   - **Ejemplo**: Evaluación de la clasificación correcta o incorrecta de un modelo de aprendizaje automático en un conjunto de datos.

2. **Distribución Multinomial**
   - **Uso**: Generalización de la binomial para más de dos resultados.
   - **Ejemplo**: Clasificación de elementos en diferentes categorías, como identificar la clase de imágenes en un conjunto de datos.

3. **Distribución de Poisson**
   - **Uso**: Modelar el número de eventos en un intervalo.
   - **Ejemplo**: Número de clics en un anuncio en línea en un período determinado, donde se espera que los clics ocurran de manera independiente.

##### Diseño de Experimentos y Pruebas de Hipótesis

1. **Distribución Binomial**
   - **Uso**: Evaluar el número de éxitos en ensayos con dos posibles resultados.
   - **Ejemplo**: Pruebas A/B en marketing, donde se mide la tasa de conversión de dos versiones de un anuncio.

2. **Distribución Hipergeométrica**
   - **Uso**: Evaluar el éxito en muestreo sin reemplazo.
   - **Ejemplo**: Selección de grupos de muestras en un experimento donde se busca un número específico de sujetos que cumplan con ciertos criterios.

3. **Distribución de Poisson**
   - **Uso**: Modelar eventos en un intervalo fijo.
   - **Ejemplo**: Número de fallas en un experimento de fiabilidad a lo largo de un periodo determinado, ayudando a predecir el rendimiento de un sistema.

Cada una de estas distribuciones desempeña un papel esencial en la modelación, análisis y comprensión de datos en sus respectivos campos, facilitando inferencias precisas y fundamentadas en experimentos y estudios estadísticos.

### 3.10 ✨Distribución Uniforme Discreta✨

| Característica | Detalle |
| :--- | :--- |
| **Descripción** | Representa una variable aleatoria que puede tomar un número finito de valores, y donde cada uno de esos valores tiene exactamente la misma probabilidad de ocurrir. |
| **Parámetros** | $k$: El número de valores posibles ($x_1, x_2, \dots, x_k$). A veces se usa $a$ (mínimo) y $b$ (máximo), donde $k = b - a + 1$. |
| **Dominio ($R_X$)** | El conjunto de enteros $\{x_1, x_2, \dots, x_k\}$ (a menudo, $\{1, 2, \dots, k\}$ o $\{a, a+1, \dots, b\}$). |
| **Función de Masa de Probabilidad (PMF)** | $P(X = x_i) = \frac{1}{k} \quad \text{para } x_i \in R_X$|
| **Valor Esperado** | $E[X] = \frac{x_1 + x_2 + \dots + x_k}{k}$|
| **Media** | $\mu_X = E[X]$ |
| **Varianza** | $\text{Var}(X) = \frac{1}{k} \sum_{i=1}^{k} (x_i - \mu_X)^2$ |
| **Varianza (si $R_X = \{1, 2, \dots, k\}$)** | $\sigma^2 = \frac{k^2 - 1}{12}$ |
| **Desviación Estándar** | $\sigma = \sqrt{\text{Var}(X)}$ |
| **Función de Distribución Acumulativa (CDF)** | $F(x) = \frac{\text{Número de valores } \le x}{k}$|

### 3.11 Caso Especial (más común): $R_X = \{1, 2, \dots, k\}$

| Característica | Fórmula |
| :--- | :--- |
| **Media** | $E[X] = \frac{k + 1}{2}$ |
| **Varianza** | $\sigma^2 = \frac{k^2 - 1}{12}$ |

### 3.12 Comandos en R (Usando la distribución de enteros)

En R, para la distribución uniforme discreta de enteros se suele usar la función `sample()` o una adaptación de las funciones de la distribución binomial si el dominio comienza en 0 o 1, pero la más directa es `sample()`.

```r
### 3.13 Parámetro: k (número de resultados posibles),
### 3.14 a y b (mínimo y máximo)
### 3.15 Ejemplo: Un dado de 6 caras (k=6, a=1, b=6)

### 3.16 PMF (Probabilidad de un valor específico):
### 3.17 P(X = x) = 1/k. No hay una función dedicada, se calcula directamente:
k = 6
prob_de_obtener_3 = 1 / k
print(prob_de_obtener_3) # 0.1666667

### 3.18 CDF (Función de distribución acumulada):
### 3.19 P(X <= x) = x/k. Se calcula directamente:
x = 3
k = 6
prob_acumulada_hasta_3 = x / k
print(prob_acumulada_hasta_3) # 0.5 (P(X<=3) = P(1)+P(2)+P(3) = 1/6 + 1/6 + 1/6)

### 3.20 Para generar simulación (Muestreo uniforme de n valores):
n = 10 # número de muestras a generar
a = 1  # Valor mínimo
b = 6  # Valor máximo
r = sample(a:b, size = n, replace = TRUE)
print(r)
### 3.21 Ejemplo de salida: [3, 6, 1, 5, 2, 6, 3, 4, 1, 5]
```

```python
import numpy as np
# La librería scipy.stats contiene funciones para muchas distribuciones,
# pero para la uniforme discreta (PMF y CDF) a menudo se usan cálculos directos
# o funciones de muestreo de NumPy.
from scipy.stats import randint

# --- Parámetros de la distribución Uniforme Discreta ---
# El número de resultados posibles (k) en un dado de 6 caras es 6.
# Los valores posibles van de 'a' a 'b'.
a = 1  # Valor mínimo (incluido)
b = 6  # Valor máximo (incluido)
k = b - a + 1 # Número total de valores posibles (6 - 1 + 1 = 6)

# --- 1. PMF (Función de Masa de Probabilidad) ---
# P(X = x) = 1/k
# Probabilidad de obtener un valor específico (ej. el número 3)
valor_x = 3
prob_de_obtener_x = 1 / k

print(f"Probabilidad de obtener el valor {valor_x} (P(X={valor_x})):")
print(f"{prob_de_obtener_x:.6f} (1/{k})")
print("-" * 30)

# --- 2. CDF (Función de Distribución Acumulada) ---
# P(X <= x) = x/k (solo aplica si 'a' es 1, como en el ejemplo del dado)
# Si 'a' es 1, la fórmula es simplemente x / k
valor_x_acumulado = 3
prob_acumulada_hasta_x = valor_x_acumulado / k

# Nota: Si usamos scipy.stats.randint, la CDF se calcula como:
# prob_acumulada_scipy = randint.cdf(valor_x_acumulado, a, b + 1)
# En scipy, el parámetro 'b' es exclusivo, por eso usamos b + 1 (7)
# print(f"Scipy CDF: {prob_acumulada_scipy:.6f}")

print(f"Probabilidad acumulada hasta el valor {valor_x_acumulado} (P(X<={valor_x_acumulado})):")
print(f"{prob_acumulada_hasta_x:.6f} ({valor_x_acumulado}/{k})")
print("-" * 30)

# --- 3. Muestreo / Simulación (rnorm en R) ---
# Generar una simulación de n lanzamientos de un dado de 6 caras.
n_muestras = 10
# Usamos np.random.randint. Nota importante:
# El límite superior (b + 1, que es 7) es exclusivo en Python,
# por lo que el rango es [a, b+1) -> [1, 7), generando valores de 1 a 6.
muestras = np.random.randint(low=a, high=b + 1, size=n_muestras)

print(f"Muestras de {n_muestras} lanzamientos de un dado de {k} caras:")
print(muestras)

# --- BONUS: Visualización de las Muestras ---
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
# Contamos la frecuencia de cada resultado
counts = np.bincount(muestras)[a:b+1] # Contar solo de 'a' a 'b'
resultados_unicos = np.arange(a, b + 1)

# Crear el gráfico de barras de las frecuencias observadas
plt.bar(resultados_unicos, counts, color='lightcoral', alpha=0.7, edgecolor='darkred')
plt.title(f"Frecuencia de Resultados en {n_muestras} Lanzamientos de Dado")
plt.xlabel("Resultado del Dado")
plt.ylabel("Frecuencia")
plt.xticks(resultados_unicos)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()
```

#### 🐍 Códigos en Python: Distribución Uniforme Discreta

La Distribución Uniforme Discreta se modela en `scipy.stats` usando la clase `randint` (random integer), o a veces `discrete_uniform`, aunque `randint` es el método preferido y más general.

Consideraremos una variable aleatoria $X$ que toma valores enteros en el rango **de $a$ a $b$** (incluidos).

  * **Parámetros:** $a$ (mínimo), $b$ (máximo).
  * **$k$ (número de valores):** $b - a + 1$.

### 3.22 1\. Inicialización y Parámetros

```python
from scipy.stats import randint
import numpy as np

# Definir el rango del dado (ejemplo: de 1 a 6, ambos inclusive)
a = 1  # Límite inferior (incluido)
b = 6  # Límite superior (incluido)

# NOTA: En scipy.stats.randint, el límite superior (high) es EXCLUIDO.
# Por lo tanto, si quieres incluir 'b', debes usar 'b + 1' como parámetro 'high'.
low = a
high = b + 1

dist = randint(low, high)
k = high - low # Número total de resultados posibles
print(f"Rango: [{a}, {b}]")
print(f"Número de resultados (k): {k}")
#
```

-----

### 3.23 2\. Función de Masa de Probabilidad (PMF)

La PMF da la probabilidad de que la variable aleatoria tome un valor exacto: $P(X = x)$.

$$P(X = x) = \frac{1}{k}$$

```python
# Valor específico para calcular su probabilidad
x = 3

# Usando el método .pmf()
prob_pmf = dist.pmf(x)
print(f"P(X = {x}) (PMF): {prob_pmf}")

# Verificación manual: 1/k
prob_manual = 1 / k
print(f"1/k (manual): {prob_manual}")
```

-----

### 3.24 3\. Función de Distribución Acumulativa (CDF)

La CDF da la probabilidad de que la variable aleatoria sea menor o igual a un valor: $P(X \le x)$.

$$F(x) = P(X \le x) = \frac{x - a + 1}{k}$$

```python
# Valor específico para calcular la probabilidad acumulada
x = 4

# Usando el método .cdf()
prob_cdf = dist.cdf(x)
print(f"P(X <= {x}) (CDF): {prob_cdf}")

# Verificación manual: P(X<=4) = 4/6
prob_manual_cdf = (x - a + 1) / k
print(f"Prob. manual: {prob_manual_cdf}")
```

-----

### 3.25 4\. Simulación (Generación de Muestras Aleatorias)

Genera $n$ realizaciones independientes de la distribución uniforme discreta.

```python
n = 10  # Número de muestras a generar

# Usando el método .rvs() (Random Variates)
simulacion_rvs = dist.rvs(size=n)
print(f"Simulación (rvs): {simulacion_rvs}")

# También se puede usar numpy.random.randint (low incluido, high excluido)
simulacion_np = np.random.randint(low=a, high=b + 1, size=n)
print(f"Simulación (numpy): {simulacion_np}")
```

-----

### 3.26 5\. Momentos (Media y Varianza)

Calcula la media (valor esperado) y la varianza de la distribución.

$$E[X] = \frac{a + b}{2} \quad \text{y} \quad \text{Var}(X) = \frac{k^2 - 1}{12}$$

```python
# Usando el método .mean()
media = dist.mean()

# Usando el método .var()
varianza = dist.var()

# Usando el método .std() para la desviación estándar
desviacion_estandar = dist.std()

print(f"Media (E[X]): {media}")
print(f"Varianza (Var(X)): {varianza}")
print(f"Desviación Estándar (std): {desviacion_estandar:.4f}")
```

```python
from scipy.stats import randint
import numpy as np

# Definir el rango del dado (ejemplo: de 1 a 6, ambos inclusive)
a = 1  # Límite inferior (incluido)
b = 6  # Límite superior (incluido)

# NOTA: En scipy.stats.randint, el límite superior (high) es EXCLUIDO.
# Por lo tanto, si quieres incluir 'b', debes usar 'b + 1' como parámetro 'high'.
low = a
high = b + 1

dist = randint(low, high)
k = high - low # Número total de resultados posibles
print(f"Rango: [{a}, {b}]")
print(f"Número de resultados (k): {k}")
```

```python
# Valor específico para calcular su probabilidad
x = 3

# Usando el método .pmf()
prob_pmf = dist.pmf(x)
print(f"P(X = {x}) (PMF): {prob_pmf}")

# Verificación manual: 1/k
prob_manual = 1 / k
print(f"1/k (manual): {prob_manual}")
```

```python
# Valor específico para calcular la probabilidad acumulada
x = 4

# Usando el método .cdf()
prob_cdf = dist.cdf(x)
print(f"P(X <= {x}) (CDF): {prob_cdf}")

# Verificación manual: P(X<=4) = 4/6
prob_manual_cdf = (x - a + 1) / k
print(f"Prob. manual: {prob_manual_cdf}")
```

```python
n = 10  # Número de muestras a generar

# Usando el método .rvs() (Random Variates)
simulacion_rvs = dist.rvs(size=n)
print(f"Simulación (rvs): {simulacion_rvs}")

# También se puede usar numpy.random.randint (low incluido, high excluido)
simulacion_np = np.random.randint(low=a, high=b + 1, size=n)
print(f"Simulación (numpy): {simulacion_np}")
```

```python
# Usando el método .mean()
media = dist.mean()

# Usando el método .var()
varianza = dist.var()

# Usando el método .std() para la desviación estándar
desviacion_estandar = dist.std()

print(f"Media (E[X]): {media}")
print(f"Varianza (Var(X)): {varianza}")
print(f"Desviación Estándar (std): {desviacion_estandar:.4f}")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import randint

# --- 1. Definir la Distribución Uniforme Discreta (Ejemplo: Dado de 1 a 6) ---
a = 1      # Límite inferior (incluido)
b = 6      # Límite superior (incluido)
low = a
high = b + 1 # high es excluido en scipy.stats
dist = randint(low, high)

# --- 2. Preparar los datos para el gráfico ---
# Obtener todos los posibles valores discretos (1, 2, 3, 4, 5, 6)
valores = np.arange(low, high)
# Obtener la probabilidad (PMF) para cada valor
probabilidades = dist.pmf(valores)

# --- 3. Generar el Gráfico ---
plt.figure(figsize=(8, 5))

# Graficar las probabilidades como barras
plt.bar(valores, probabilidades, width=0.8, color='skyblue', edgecolor='black')

# Añadir una línea horizontal para mostrar la uniformidad
plt.axhline(y=1/len(valores), color='red', linestyle='--', linewidth=1, label=f'P = 1/{len(valores)}')

# Añadir etiquetas de probabilidad en la parte superior de cada barra
for val, prob in zip(valores, probabilidades):
    plt.text(val, prob + 0.005, f'{prob:.4f}', ha='center', fontsize=9)

# Configuración y títulos
plt.title('Función de Masa de Probabilidad (PMF) - Distribución Uniforme Discreta', fontsize=14)
plt.xlabel('Valores Posibles (x)', fontsize=12)
plt.ylabel('Probabilidad P(X = x)', fontsize=12)
plt.xticks(valores)
plt.ylim(0, max(probabilidades) + 0.05)
plt.legend()
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.show()
```

### 3.27 ✨Distribución de Bernoulli✨
   - **Descripción**: Representa un experimento con dos resultados posibles (éxito o fracaso).
   - **Parámetro**: $ p $ (probabilidad de éxito).
   - **Función de Masa de Probabilidad (PMF)**:
   $
   P(X=1) = p, \quad P(X=0) = 1 - p
   $
   - **Valor Esperado**:
   $
   E[X] = p
   $
   - **Media**:
  $
   \mu_X = p
  $
   - **Varianza**:
  $
   \sigma = {p(1-p)}
  $
   - **Desviación Estándar**:
  $
   \sigma = \sqrt{p(1-p)}
  $
   - **Función de Distribución Acumulativa (CDF)**:
  $
   F(x) =
   \begin{cases}
   0 & \text{si } x < 0 \\
   1 - p & \text{si } 0 \leq x < 1 \\
   1 & \text{si } x \geq 1
   \end{cases}
  $
   - **Comandos en R**:
   
   ```r
### 3.28 PMF (funcion de masa de probabilidad)
   dbinom(x, size=1, prob=p)
   
### 3.29 CDF (funcion de distribucion acumulada)
   pbinom(x, size=1, prob=p)
   
### 3.30 Para generar simulacion
   rbinom(n, size=1, prob=p)       

```python
"""
p <- 0.1
x <- 1
size <- 1

# Calcular la probabilidad de que un producto dure más de 5500 unidades de tiempo
probabilidad <- dbinom(x, size, prob = p)
print(probabilidad)  # Debería ser 0.1
"""
```

```python
import numpy as np
from scipy.stats import binom

# --- Parámetros de la Distribución ---
p = 0.1   # Probabilidad de éxito (prob)
size = 1  # Número de ensayos (n). Cuando size=1, es una distribución de Bernoulli.
x = 1     # Número de éxitos que queremos calcular (k)

# Nota sobre el comentario original: La función dbinom(x, size, prob)
# calcula P(X = x) de la distribución Binomial, no una probabilidad de duración.
# Estamos traduciendo el cálculo matemático: P(X=1 | n=1, p=0.1)

# --- 1. Calcular la PMF (Función de Masa de Probabilidad) ---
# En Python, el equivalente a dbinom(x, size, prob) es binom.pmf(k, n, p)
probabilidad = binom.pmf(x, size, p)

print(f"Parámetros: n={size}, p={p}, k={x}")
print("-" * 40)
print(f"La probabilidad de obtener {x} éxito(s) en {size} ensayo(s) es:")
print(f"{probabilidad:.1f}")

# El resultado es 0.1, ya que para una sola prueba,
# la probabilidad de éxito (k=1) es simplemente p.
```

```python
"""
pbinom(x, size=1, prob=p)

"""
```

```python
import numpy as np
from scipy.stats import binom

# --- Parámetros de la Distribución ---
p = 0.1   # Probabilidad de éxito (prob)
size = 1  # Número de ensayos (n). Cuando size=1, es una distribución de Bernoulli.
x = 1     # Número de éxitos (k) para el cual queremos calcular la probabilidad

# Nota sobre el comentario original: La función dbinom(x, size, prob)
# calcula P(X = x) de la distribución Binomial, no una probabilidad de duración.
# Estamos traduciendo el cálculo matemático: P(X=1 | n=1, p=0.1)

# --- 1. Calcular la PMF (Función de Masa de Probabilidad) ---
# En Python, el equivalente a dbinom(x, size, prob) es binom.pmf(k, n, p)
probabilidad_pmf = binom.pmf(x, size, p)

# --- 2. Calcular la CDF (Función de Distribución Acumulada) ---
# El equivalente a pbinom(x, size, prob) es binom.cdf(k, n, p)
# Calcula P(X <= x)
probabilidad_cdf = binom.cdf(x, size, p)

print(f"--- Distribución Binomial (Bernoulli) ---")
print(f"Parámetros: Ensayos (n) = {size}, Prob. Éxito (p) = {p}, Valor (k) = {x}")
print("-" * 50)

# Resultado de la PMF
print("Cálculo 1: PMF (Función de Masa de Probabilidad)")
print(f"P(X = {x}) = Probabilidad de obtener exactamente {x} éxito(s):")
print(f"{probabilidad_pmf:.4f}")
print("-" * 50)

# Resultado de la CDF
print("Cálculo 2: CDF (Función de Distribución Acumulada)")
print(f"P(X <= {x}) = Probabilidad de obtener {x} éxito(s) o menos:")
print(f"{probabilidad_cdf:.4f}")

# Explicación del resultado de la CDF (para Bernoulli):
# P(X <= 1) = P(X=0) + P(X=1)
# P(X=0) es la probabilidad de fracaso: 1 - 0.1 = 0.9
# P(X=1) es la probabilidad de éxito: 0.1
# CDF = 0.9 + 0.1 = 1.0
```

```python
"""
rbinom(100, size=1, prob=p)
"""
```

```python
import numpy as np
from scipy.stats import binom

# --- Parámetros de la Distribución ---
p = 0.1   # Probabilidad de éxito (prob)
size = 1  # Número de ensayos por experimento (n). Cuando size=1, es una distribución de Bernoulli.
x = 1     # Número de éxitos (k) para el cual queremos calcular la probabilidad
n_samples = 100 # Número de muestras a generar para la simulación (rbinom en R)

# Nota sobre el comentario original: La función dbinom(x, size, prob)
# calcula P(X = x) de la distribución Binomial, no una probabilidad de duración.

# --- 1. Calcular la PMF (Función de Masa de Probabilidad) ---
# En Python, el equivalente a dbinom(x, size, prob) es binom.pmf(k, n, p)
probabilidad_pmf = binom.pmf(x, size, p)

# --- 2. Calcular la CDF (Función de Distribución Acumulada) ---
# El equivalente a pbinom(x, size, prob) es binom.cdf(k, n, p)
# Calcula P(X <= x)
probabilidad_cdf = binom.cdf(x, size, p)

# --- 3. Muestreo / Simulación ---
# El equivalente a rbinom(n_samples, size, prob) es np.random.binomial(n, p, size)
# Genera una matriz (array) de 100 resultados aleatorios (0 o 1)
muestras_aleatorias = np.random.binomial(n=size, p=p, size=n_samples)

print(f"--- Distribución Binomial (Bernoulli) ---")
print(f"Parámetros: Ensayos (n) = {size}, Prob. Éxito (p) = {p}, Valor (k) = {x}")
print("-" * 50)

# Resultado de la PMF
print("Cálculo 1: PMF (Función de Masa de Probabilidad)")
print(f"P(X = {x}) = Probabilidad de obtener exactamente {x} éxito(s):")
print(f"{probabilidad_pmf:.4f}")
print("-" * 50)

# Resultado de la CDF
print("Cálculo 2: CDF (Función de Distribución Acumulada)")
print(f"P(X <= {x}) = Probabilidad de obtener {x} éxito(s) o menos:")
print(f"{probabilidad_cdf:.4f}")
print("-" * 50)

# Resultado del Muestreo
print(f"Cálculo 3: Muestreo / Simulación (Generación de {n_samples} resultados)")
print("El equivalente a rbinom(100, size=1, prob=0.1) es np.random.binomial(1, 0.1, 100)")
print("Primeros 10 resultados generados (0=Fracaso, 1=Éxito):")
print(muestras_aleatorias[:10])

# Contar cuántos éxitos (1s) se obtuvieron en la simulación
num_exitos_simulados = np.sum(muestras_aleatorias)
print(f"\nResultados de la simulación:")
print(f"Número total de éxitos (1s): {num_exitos_simulados}")
print(f"Proporción de éxitos: {num_exitos_simulados / n_samples:.4f}")

# Explicación del resultado de la CDF (para Bernoulli):
# P(X <= 1) = P(X=0) + P(X=1)
# P(X=0) es la probabilidad de fracaso: 1 - 0.1 = 0.9
# P(X=1) es la probabilidad de éxito: 0.1
# CDF = 0.9 + 0.1 = 1.0
```

#### Ejemplo de Gráfica de la Distribución de Bernoulli

Esta distribución describe un experimento con dos resultados posibles: éxito $(1) $ y fracaso $ (0)$.

```python
"""
# Cargar la librería necesaria
library(ggplot2)

# Definir el parámetro de éxito (p)
p <- 0.7  # Probabilidad de éxito

# Crear los valores posibles de X (0 y 1)
x_values <- c(0, 1)

# Calcular la PMF de la distribución de Bernoulli
pmf_values <- c(1 - p, p)

# Crear un data frame para ggplot
data <- data.frame(x = x_values, pmf = pmf_values)

# Graficar la distribución de Bernoulli
ggplot(data, aes(x = factor(x), y = pmf)) +
  geom_bar(stat = "identity", fill = "blue", alpha = 0.7) +
  labs(title = "Gráfico de la Distribución de Bernoulli",
       x = "Resultado",
       y = "Probabilidad") +
  scale_x_discrete(labels = c("0" = "Fracaso", "1" = "Éxito")) +
  theme_minimal() +
  ylim(0, 1)

"""
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Definir el parámetro de éxito (p)
p = 0.7  # Probabilidad de éxito

# Crear los valores posibles de X (0 y 1)
# 0 = Fracaso, 1 = Éxito
x_values = np.array([0, 1])

# Calcular la PMF (Probabilidad de Masa de Función) de la distribución de Bernoulli
# dbinom(x, size=1, prob=p) en R es equivalente a binom.pmf(k, n, p) en Python
# P(X=0) = 1 - p
# P(X=1) = p
pmf_values = binom.pmf(x_values, n=1, p=p)

# Crear el gráfico de barras
plt.figure(figsize=(7, 5))
plt.bar(
    x_values,
    pmf_values,
    color=['#4C72B0', '#55A868'],  # Colores diferentes para cada barra
    alpha=0.8,
    width=0.4
)

# Configurar etiquetas y títulos
plt.title("Gráfico de la Distribución de Bernoulli (p=0.7)", fontsize=14)
plt.xlabel("Resultado", fontsize=12)
plt.ylabel("Probabilidad", fontsize=12)

# Configurar el eje X para mostrar etiquetas claras
# Usamos tick_label para mapear 0 a 'Fracaso' y 1 a 'Éxito'
plt.xticks(x_values, ['Fracaso (0)', 'Éxito (1)'])

# Configurar el eje Y para que vaya de 0 a 1 y mostrar las probabilidades en las barras
plt.ylim(0, 1)
for i, prob in enumerate(pmf_values):
    plt.text(
        x_values[i],
        prob + 0.02, # Pequeño desplazamiento hacia arriba
        f'{prob:.2f}', # Mostrar la probabilidad con 2 decimales
        ha='center',
        fontsize=10,
        fontweight='bold'
    )

# Estilo y mostrar el gráfico
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.show()
```

#### Descripción del Código en R

* **Cargar librerías**: Se utiliza `ggplot2` para crear la gráfica.
* **Definir el parámetro de éxito**: Se establece la probabilidad de éxito $ p $ (en este caso, $0.7$).
* **Crear los valores posibles de $X$**: Los valores posibles son $0$ (fracaso) y $1$ (éxito).
* **Calcular la PMF**: Se calculan las probabilidades de cada resultado usando la fórmula de la distribución de Bernoulli.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $ X $ y sus correspondientes probabilidades.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de barras que representa la $PMF$ de la distribución de Bernoulli.

**Códigos en Python**

```python
from scipy.stats import binom
import numpy as np

# Parámetros de la Distribución de Bernoulli (Distribución Binomial con size=1)
p = 0.1     # Probabilidad de 'éxito' (p en R)
x = 1       # El valor que queremos evaluar (x en R)
size = 1    # Número de ensayos (size en R, lo que define a Bernoulli)

# 1. Función de Masa de Probabilidad (PMF)
# Equivalente a dbinom(x, size=1, prob=p) en R
# Calcula P(X = x)
probabilidad = binom.pmf(k=x, n=size, p=p)
print(f"PMF (P(X={x})): {probabilidad}")
# Resultado: 0.1

# 2. Función de Distribución Acumulativa (CDF)
# Equivalente a pbinom(x, size=1, prob=p) en R
# Calcula P(X <= x)
probabilidad_acumulada = binom.cdf(k=x, n=size, p=p)
print(f"CDF (P(X<={x})): {probabilidad_acumulada}")
# Resultado: P(X=0) + P(X=1) = (1-0.1) + 0.1 = 1.0

# 3. Generación de Muestras Aleatorias (Simulación)
# Equivalente a rbinom(100, size=1, prob=p) en R
# Genera 100 realizaciones de la variable de Bernoulli
n_muestras = 100
simulacion = binom.rvs(n=size, p=p, size=n_muestras)
print(f"Simulación (rvs, 100 muestras): {simulacion[:15]}...")
# Muestra los primeros 15 valores (ejemplo de salida: [0 0 0 1 0 0 0 0 0 0 0 0 0 0 0]...)

# ----------------------------------------------------------------------
# NOTA SOBRE TU EJEMPLO:
# La descripción "Calcular la probabilidad de que un producto dure más de 5500 unidades de tiempo"
# es más adecuada para una distribución continua (como la Exponencial o Uniforme Continua)
# y no para la Distribución de Bernoulli, que solo tiene resultados 0 o 1.
# El código anterior solo calcula la probabilidad de obtener un 'éxito' (x=1) en un ensayo.
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# --- 1. Definir la Distribución de Bernoulli (size=1) ---
p = 0.1     # Probabilidad de éxito (P(X=1))
size = 1    # Número de ensayos (define a Bernoulli)
dist = binom(n=size, p=p)

# --- 2. Preparar los datos para el gráfico ---
# Los únicos valores posibles son 0 y 1
valores = [0, 1]

# Obtener la probabilidad (PMF) para cada valor
probabilidades = dist.pmf(valores)
# P(X=0) = 1 - p = 0.9
# P(X=1) = p = 0.1

# --- 3. Generar el Gráfico ---
plt.figure(figsize=(7, 5))

# Graficar las probabilidades como barras
bars = plt.bar(valores, probabilidades, width=0.4, color=['lightcoral', 'skyblue'], edgecolor='black')

# Añadir etiquetas de probabilidad en la parte superior de cada barra
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, f'{yval:.2f}', ha='center', fontsize=10)

# Configuración y títulos
plt.title(f'Función de Masa de Probabilidad (PMF) - Distribución de Bernoulli (p={p})', fontsize=14)
plt.xlabel('Resultado (0 = Fracaso, 1 = Éxito)', fontsize=12)
plt.ylabel('Probabilidad P(X = x)', fontsize=12)
plt.xticks(valores, ['0 (Fracaso)', '1 (Éxito)'])
plt.ylim(0, 1.1)
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.show()
```

#### Descripción del Código en Python

Genera la descripción del código en python en el mismo formato que el de R.

**EJERCICIO 1**

Agrega ejemplos y los usos recomendados para esta distribución.

### 3.31 👍🏼Usos Recomendados de la Distribución de Bernoulli

La distribución de Bernoulli se utiliza para modelar un **único ensayo** con dos posibles resultados: **éxito** (valor 1) o **fracaso** (valor 0). Su único parámetro es $\mathbf{p}$ (la probabilidad de éxito).

Aquí tienes algunos de los usos más comunes en estadística y el mundo real:

### 3.32 1. Control de Calidad y Producción
En entornos de fabricación, se utiliza la distribución de Bernoulli para modelar si un producto individual cumple con las especificaciones o no.

* **Ejemplo:** Probar un bombillo. ¿El bombillo funciona (Éxito, $X=1$) o no funciona (Fracaso, $X=0$)? $p$ sería la probabilidad de que el bombillo funcione.
* **Aplicación:** Inspección de un componente electrónico (defectuoso o no defectuoso), o si un pago por tarjeta es aceptado o rechazado.

### 3.33 2. Medicina y Ensayos Clínicos
Se aplica para determinar el resultado binario de un paciente o una prueba.

* **Ejemplo:** Analizar la efectividad de un nuevo medicamento en un paciente. ¿El paciente se recupera (Éxito) o no (Fracaso)?
* **Aplicación:** Modelar si una persona está infectada con un virus (positivo/negativo), o si una cirugía es exitosa o no.

### 3.34 3. Aprendizaje Automático (Machine Learning)
En ML, la distribución de Bernoulli es fundamental en varios modelos y métricas.

* **Ejemplo:** Predicción binaria. Modelar la probabilidad de que un cliente haga clic en un anuncio (clic/no clic).
* **Aplicación:** Es la base de los modelos de **regresión logística** y se utiliza para calcular la **entropía binaria** en funciones de pérdida.

### 3.35 4. Deportes y Juegos de Azar
Cualquier evento con dos resultados claros puede ser modelado por una Bernoulli.

* **Ejemplo:** El lanzamiento de una moneda (cara/cruz). La probabilidad de que un equipo gane un partido específico (ganar/perder, ignorando el empate).

### 3.36 Relación con otras Distribuciones

Es importante recordar que la distribución de Bernoulli es un caso especial de la Distribución **Binomial** donde el número de ensayos es $\mathbf{n=1}$. Si repites un ensayo de Bernoulli $n$ veces, el número total de éxitos seguirá una Distribución Binomial.

### 3.37 💻Ejemplos en codigo

```python
import numpy as np
from scipy.stats import bernoulli

# Definición de la probabilidad de éxito (p)
# p es el único parámetro de la distribución de Bernoulli.

print("--- Usos de la Distribución de Bernoulli ---")

# =========================================================================
# 1. Control de Calidad y Producción (Probar un bombillo)
# =========================================================================

# Escenario: Un bombillo tiene una probabilidad del 98% de funcionar.
p_bombillo_funciona = 0.98

# Creación de la distribución de Bernoulli
dist_bombillo = bernoulli(p_bombillo_funciona)

# a) Probabilidad de que funcione (P(X=1))
prob_funciona = dist_bombillo.pmf(1)

# b) Probabilidad de que FALLE (P(X=0))
prob_falla = dist_bombillo.pmf(0)

# c) Simulación de un solo ensayo (probar 1 bombillo)
resultado_simulacion_1 = dist_bombillo.rvs(size=1)

print("\n1. Control de Calidad: Prueba de Bombillo (p=0.98)")
print(f"Probabilidad de que el bombillo funcione (X=1): {prob_funciona:.4f}")
print(f"Probabilidad de que el bombillo falle (X=0): {prob_falla:.4f}")
print(f"Resultado de la prueba (1=funciona, 0=falla): {resultado_simulacion_1[0]}")

# =========================================================================
# 2. Medicina y Ensayos Clínicos (Recuperación de un paciente)
# =========================================================================

# Escenario: Un nuevo medicamento tiene un 65% de probabilidad de éxito.
p_recuperacion = 0.65
dist_medicina = bernoulli(p_recuperacion)

# Simulación: ¿Se recupera el próximo paciente tratado? (1 intento)
resultado_paciente = dist_medicina.rvs(size=1)

print("\n2. Medicina: Efectividad de un Medicamento (p=0.65)")
print(f"Probabilidad de que el paciente NO se recupere (X=0): {dist_medicina.pmf(0):.4f}")
if resultado_paciente[0] == 1:
    print("Simulación: ¡El paciente se recuperó! (1)")
else:
    print("Simulación: El paciente no se recuperó. (0)")

# =========================================================================
# 3. Aprendizaje Automático (Clic en un anuncio)
# =========================================================================

# Escenario: Un cliente tiene un 12% de probabilidad de hacer clic en un anuncio.
p_clic = 0.12
dist_clic = bernoulli(p_clic)

# Cálculo de la PMF (Probabilidad de obtener el resultado 1 o 0)
prob_clic = dist_clic.pmf(1)
prob_no_clic = dist_clic.pmf(0)

# Simulación de un solo cliente
simulacion_clic = dist_clic.rvs(size=1)

print("\n3. Aprendizaje Automático: Clic en Anuncio (p=0.12)")
print(f"Probabilidad de clic (X=1): {prob_clic:.4f}")
print(f"Probabilidad de NO clic (X=0): {prob_no_clic:.4f}")
print(f"Simulación de cliente: {'Clic' if simulacion_clic[0] == 1 else 'No Clic'}")

# =========================================================================
# 4. Deportes y Juegos de Azar (Lanzamiento de una moneda justa)
# =========================================================================

# Escenario: Moneda justa, p=0.5 (probabilidad de obtener Cara)
p_moneda = 0.5
dist_moneda = bernoulli(p_moneda)

# Simulación: Lanzar la moneda una vez
resultado_moneda = dist_moneda.rvs(size=1)
resultado_final = "Cara" if resultado_moneda[0] == 1 else "Cruz"

print("\n4. Juegos de Azar: Lanzamiento de Moneda (p=0.5)")
print(f"Probabilidad de Cara (X=1) o Cruz (X=0): {dist_moneda.pmf(1):.4f}")
print(f"Resultado del lanzamiento: {resultado_final}")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom # Usamos binom con n=1, que es la PMF de Bernoulli.

print("--- Gráficas y Usos de la Distribución de Bernoulli ---")

# =========================================================================
# FUNCIÓN DE GRAFICACIÓN PARA BERNOULLI (n=1)
# =========================================================================

def plot_bernoulli(p, title, k_highlight=None, color_highlight='red'):
    """
    Calcula y grafica la PMF de una distribución de Bernoulli (n=1).
    p: Probabilidad de éxito P(X=1).
    title: Título del gráfico.
    k_highlight: Valor(es) k a destacar (0 o 1).
    """
    n = 1
    k_values = [0, 1] # Fracaso (0) y Éxito (1)
    pmf_values = binom.pmf(k_values, n, p)

    plt.figure(figsize=(6, 4))

# 1. Graficar todas las barras en tonos de azul
    plt.bar(k_values, pmf_values, color=['skyblue', 'lightblue'], alpha=0.8)

# 2. Destacar valores específicos si se proporcionan
    if k_highlight is not None:
        if not isinstance(k_highlight, list):
            k_highlight = [k_highlight]

        for k in k_highlight:
            if k in k_values:
# La altura de la barra es la PMF del valor k
                plt.bar(k, binom.pmf(k, n, p), color=color_highlight, alpha=0.9)

    plt.title(f"{title}\n(p={p})", fontsize=12)
    plt.xlabel("Resultado (0: Fracaso, 1: Éxito)", fontsize=10)
    plt.ylabel("Probabilidad P(X=k)", fontsize=10)
    plt.xticks(k_values)
    plt.ylim(0, 1.05)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()

# =========================================================================
# 1. Control de Calidad y Producción (Bombillo)
# =========================================================================

# Escenario: Bombillo funciona con p=0.98 (Éxito).
p_bombillo_funciona = 0.98
pmf_falla = binom.pmf(0, 1, p_bombillo_funciona) # Probabilidad de Fracaso (X=0)

print("\n1. Control de Calidad: Prueba de Bombillo (p=0.98)")
print(f"Probabilidad de que el bombillo falle (X=0): {pmf_falla:.4f}")

plot_bernoulli(
    p=p_bombillo_funciona,
    title="Bernoulli: Probabilidad de que un Bombillo Funcione",
    k_highlight=1, # Destacar el éxito (funcionar)
    color_highlight='green'
)

# =========================================================================
# 2. Medicina y Ensayos Clínicos (Recuperación de paciente)
# =========================================================================

# Escenario: Probabilidad de recuperación individual p=0.65 (Éxito).
p_recuperacion = 0.65
pmf_no_recupera = binom.pmf(0, 1, p_recuperacion) # Probabilidad de Fracaso (X=0)

print("\n2. Medicina: Efectividad de un Medicamento (p=0.65)")
print(f"Probabilidad de que el paciente NO se recupere (X=0): {pmf_no_recupera:.4f}")

plot_bernoulli(
    p=p_recuperacion,
    title="Bernoulli: Probabilidad de Recuperación del Paciente",
    k_highlight=0, # Destacar el fracaso (no se recupera)
    color_highlight='red'
)

# =========================================================================
# 3. Aprendizaje Automático (Clic en un anuncio)
# =========================================================================

# Escenario: Probabilidad de hacer clic p=0.12 (Éxito).
p_clic = 0.12
pmf_clic = binom.pmf(1, 1, p_clic) # Probabilidad de Éxito (X=1)

print("\n3. Aprendizaje Automático: Clic en Anuncio (p=0.12)")
print(f"Probabilidad de clic (X=1): {pmf_clic:.4f}")

plot_bernoulli(
    p=p_clic,
    title="Bernoulli: Probabilidad de Clic en Publicidad",
    k_highlight=1, # Destacar el éxito (clic)
    color_highlight='blue'
)

# =========================================================================
# 4. Deportes y Juegos de Azar (Lanzamiento de una moneda)
# =========================================================================

# Escenario: Moneda justa, p=0.5 (Éxito: Cara).
p_moneda = 0.5
pmf_cara = binom.pmf(1, 1, p_moneda) # Probabilidad de Éxito (X=1)

print("\n4. Juegos de Azar: Lanzamiento de Moneda (p=0.5)")
print(f"Probabilidad de Cara (X=1) o Cruz (X=0): {pmf_cara:.4f}")

plot_bernoulli(
    p=p_moneda,
    title="Bernoulli: Lanzamiento de Moneda Justa (Simetría)",
    k_highlight=[0, 1], # Destacar ambos resultados por igual
    color_highlight='purple'
)
```

### 3.38 ✨Distribución Binomial✨

* **Descripción**: Modelo de $n$ ensayos independientes de Bernoulli.

* **Parámetros**: $n$ (número de ensayos), $p$ (probabilidad de éxito).

* **Función de Masa de Probabilidad (PMF):**
$$
P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}, \quad k = 0, 1, \ldots, n
$$

* **Valor Esperado:** $
E[X] = n \cdot p
$

* **Media:** $\mu_X = n \cdot p$

* **Desviación Estándar:**
$
\sigma = \sqrt{n \cdot p \cdot (1 - p)}
$

* **Función de Distribución Acumulativa (CDF):**

$$
F(x) = P(X \leq k) = \sum \limits_{i=0}^{\lfloor x \rfloor} \binom{n}{i} p^i (1 - p)^{n - i}
$$

* **Comandos en R:**

```r
### 3.39 PMF
dbinom(k, size = n, prob = p)

### 3.40 CDF
pbinom(k, size = n, prob = p)

### 3.41 Simulation
rbinom(n, size = n, prob = p)

#### Ejemplo de Gráfica de la Distribución Binomial

Esta distribución describe el número de éxitos en una serie de ensayos de Bernoulli independientes.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Definir los parámetros de la distribución binomial
n = 10  # Número de ensayos
p = 0.5  # Probabilidad de éxito en cada ensayo

# Crear un rango de valores para el número de éxitos (k)
k_values = np.arange(0, n + 1) # Incluir n en el rango

# Calcular la PMF de la distribución binomial
pmf_values = binom.pmf(k_values, n=n, p=p)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.bar(k_values, pmf_values, color='skyblue', edgecolor='black')

# Añadir etiquetas de probabilidad en la parte superior de cada barra
for k, pmf in zip(k_values, pmf_values):
    plt.text(k, pmf + 0.005, f'{pmf:.4f}', ha='center', fontsize=9)

# Configuración y títulos
plt.title('Función de Masa de Probabilidad (PMF) - Distribución Binomial', fontsize=14)
plt.xlabel('Número de Éxitos (k)', fontsize=12)
plt.ylabel('Probabilidad P(X = k)', fontsize=12)
plt.xticks(k_values)
plt.ylim(0, max(pmf_values) + 0.05)
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.show()
```

#### Descripción del Código

* **Cargar librerías**: Se utiliza `ggplot2` para crear la gráfica.
* **Definir los parámetros**: Se establecen el número de ensayos $ n $ y la probabilidad de éxito $ p $.
* **Crear un rango de valores para $k$**: Se define el rango de valores posibles para el número de éxitos (de $0$ a $ n $).
* **Calcular la PMF**: Se utiliza `dbinom()` para calcular las probabilidades de cada posible número de éxitos.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $ k $ y sus correspondientes probabilidades.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de barras que representa la $PMF$ de la distribución binomial.

**EJERCICIO 2**

Agrega ejemplos y los usos recomendados.

### 3.42 👍🏼Usos Recomendados de la Distribución Binomial

La Distribución Binomial se utiliza para modelar el **número total de éxitos ($\mathbf{k}$)** en una secuencia de **$\mathbf{n}$ ensayos** independientes de Bernoulli (donde cada ensayo solo tiene dos resultados posibles: éxito o fracaso).

### 3.43 1. Control de Calidad y Manufactura
Es ideal para evaluar el rendimiento de un proceso productivo a gran escala.

* **Ejemplo:** Una fábrica produce 1000 piezas (n=1000). Si la probabilidad de que una pieza sea defectuosa es $p=0.01$, la Binomial permite calcular la probabilidad de encontrar exactamente 5 piezas defectuosas en ese lote.
* **Aplicación:** Determinar la probabilidad de que un envío completo de productos contenga más de un cierto número de artículos fallidos.

### 3.44 2. Medicina y Biología
Se usa para analizar resultados de muestras de población, ensayos de laboratorio y la propagación de enfermedades.

* **Ejemplo:** La probabilidad de que una persona se recupere de una enfermedad es $p=0.8$. Si se observa a 20 pacientes ($\mathbf{n=20}$), la Binomial calcula la probabilidad de que 18 o más se recuperen.
* **Aplicación:** Determinar la tasa de éxito de un tratamiento o la proporción de una población que tiene un gen específico.

### 3.45 3. Encuestas de Opinión Pública y Marketing
Dado que muchas preguntas en encuestas son binarias (sí/no, a favor/en contra), esta distribución es fundamental.

* **Ejemplo:** Si el 60% de los votantes planea votar por el Candidato A ($\mathbf{p=0.6}$), y se encuesta a un grupo de 50 personas ($\mathbf{n=50}$), se puede calcular la probabilidad de que la muestra contenga menos de 25 partidarios del Candidato A.
* **Aplicación:** Predecir cuántos clientes en una muestra de 100 responderán positivamente a un nuevo anuncio publicitario.

### 3.46 4. Finanzas y Seguros
Se utiliza en la modelización de riesgos donde el resultado es un evento (fallo) o no evento (no fallo).

* **Ejemplo:** Una compañía de seguros evalúa que la probabilidad de que un cliente reclame su póliza en un año es $p=0.05$. Si la compañía tiene 1000 clientes ($\mathbf{n=1000}$), la Binomial ayuda a modelar la probabilidad de recibir un número excesivo de reclamaciones.

---

La clave para usar la Distribución Binomial es que el experimento cumpla con cuatro condiciones:

1.  **Fijo:** El número de ensayos ($\mathbf{n}$) debe ser fijo.
2.  **Independiente:** Los ensayos deben ser independientes entre sí.
3.  **Binario:** Cada ensayo tiene solo dos resultados (éxito o fracaso).
4.  **Constante:** La probabilidad de éxito ($\mathbf{p}$) debe ser la misma en cada ensayo.

### 3.47 💻Ejemplos en codigo

```python
import numpy as np
from scipy.stats import binom

print("--- Usos de la Distribución Binomial ---")

# =========================================================================
# 1. Control de Calidad y Manufactura (Piezas defectuosas)
# =========================================================================

# Escenario: Lote de 1000 piezas. Probabilidad de que una pieza sea defectuosa es 0.01.
n_piezas = 1000  # Número total de ensayos (piezas)
p_defecto = 0.01 # Probabilidad de "éxito" (encontrar un defecto)

# Creación de la distribución Binomial
dist_calidad = binom(n_piezas, p_defecto)

# Objetivo: Calcular la probabilidad de encontrar EXACTAMENTE 5 piezas defectuosas (PMF)
k_objetivo = 5
prob_exactamente_5 = dist_calidad.pmf(k_objetivo)

# Simulación: Simular el número de defectos en 1 lote de 1000
simulacion_defectos = dist_calidad.rvs(size=1)[0]

print("\n1. Control de Calidad: Defectos en un Lote (n=1000, p=0.01)")
print(f"Probabilidad de encontrar EXACTAMENTE {k_objetivo} defectos: {prob_exactamente_5:.4f}")
print(f"Resultado de la simulación (defectos encontrados): {simulacion_defectos}")

# =========================================================================
# 2. Medicina y Biología (Recuperación de pacientes)
# =========================================================================

# Escenario: 20 pacientes. Probabilidad de recuperación individual es 0.8.
n_pacientes = 20
p_recuperacion = 0.8

dist_medicina = binom(n_pacientes, p_recuperacion)

# Objetivo: Calcular la probabilidad de que 18 O MÁS se recuperen (CDF complementaria)
# P(X >= 18) = 1 - P(X <= 17)
k_limite = 17
prob_18_o_mas = 1 - dist_medicina.cdf(k_limite)

# Simulación: Resultado de recuperación para el grupo de 20
recuperados_simulados = dist_medicina.rvs(size=1)[0]

print("\n2. Medicina: Recuperación de Pacientes (n=20, p=0.8)")
print(f"Probabilidad de que 18 o más pacientes se recuperen: {prob_18_o_mas:.4f}")
print(f"Simulación: Pacientes recuperados en el ensayo: {recuperados_simulados} / 20")

# =========================================================================
# 3. Encuestas de Opinión Pública y Marketing (Votantes)
# =========================================================================

# Escenario: 50 personas encuestadas. 60% vota por Candidato A.
n_encuesta = 50
p_voto_A = 0.6

dist_votantes = binom(n_encuesta, p_voto_A)

# Objetivo: Calcular la probabilidad de que MENOS de 25 voten por A (CDF)
# P(X < 25) es igual a P(X <= 24)
k_limite = 24
prob_menos_25 = dist_votantes.cdf(k_limite)

# Simulación: Número de votantes por A en una muestra
votantes_simulados = dist_votantes.rvs(size=1)[0]

print("\n3. Encuestas de Opinión: Apoyo al Candidato A (n=50, p=0.6)")
print(f"Probabilidad de que menos de 25 voten por A: {prob_menos_25:.4f}")
print(f"Simulación: Votantes por A encontrados en la muestra: {votantes_simulados} / 50")

# =========================================================================
# 4. Finanzas y Seguros (Reclamaciones de póliza)
# =========================================================================

# Escenario: 1000 clientes. Probabilidad de reclamo individual es 0.05.
n_clientes = 1000
p_reclamo = 0.05

dist_seguros = binom(n_clientes, p_reclamo)

# Objetivo: Modelar la probabilidad de recibir un número excesivo de reclamaciones.
# Por ejemplo, P(X > 60), que es 1 - P(X <= 60)
k_max_aceptable = 60
prob_excesiva = 1 - dist_seguros.cdf(k_max_aceptable)

# Simulación: Número de reclamos observados en la cartera
reclamos_simulados = dist_seguros.rvs(size=1)[0]

print("\n4. Finanzas y Seguros: Reclamaciones (n=1000, p=0.05)")
print(f"Probabilidad de recibir más de 60 reclamos: {prob_excesiva:.4f}")
print(f"Simulación: Reclamos recibidos: {reclamos_simulados} / 1000")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

print("--- Usos de la Distribución Binomial ---")

# =========================================================================
# FUNCIÓN DE GRAFICACIÓN (AÑADIDA)
# =========================================================================

def plot_binomial(n, p, title, k_highlight=None, color_highlight='red'):
    """
    Calcula y grafica la PMF de una distribución Binomial.
    n: Número de ensayos.
    p: Probabilidad de éxito.
    title: Título del gráfico.
    k_highlight: Valor(es) k a destacar con un color diferente.
    """
    k_values = np.arange(0, n + 1)
    pmf_values = binom.pmf(k_values, n, p)

    plt.figure(figsize=(10, 5))

# 1. Graficar todas las barras en azul
    plt.bar(k_values, pmf_values, color='lightblue', alpha=0.7)

# 2. Destacar valores específicos si se proporcionan
    if k_highlight is not None:
        if not isinstance(k_highlight, list):
            k_highlight = [k_highlight]

        for k in k_highlight:
            if 0 <= k <= n:
                plt.bar(k, binom.pmf(k, n, p), color=color_highlight, alpha=0.9)

    plt.title(f"{title}\n(n={n}, p={p})", fontsize=14)
    plt.xlabel("Número de Éxitos (k)", fontsize=11)
    plt.ylabel("Probabilidad P(X=k)", fontsize=11)
    plt.xticks(np.arange(0, n + 1, max(1, n // 10))) # Mostrar etiquetas de k cada 1, 5, 10, etc.
    plt.ylim(0, np.max(pmf_values) + 0.05)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()

# =========================================================================
# 1. Control de Calidad y Manufactura (Piezas defectuosas)
# =========================================================================

# Escenario: Lote de 1000 piezas. Probabilidad de que una pieza sea defectuosa es 0.01.
n_piezas = 1000
p_defecto = 0.01

dist_calidad = binom(n_piezas, p_defecto)

# Objetivo: Calcular la probabilidad de encontrar EXACTAMENTE 5 piezas defectuosas (PMF)
k_objetivo = 5
prob_exactamente_5 = dist_calidad.pmf(k_objetivo)

# Simulación: Simular el número de defectos en 1 lote de 1000
simulacion_defectos = dist_calidad.rvs(size=1)[0]

print("\n1. Control de Calidad: Defectos en un Lote (n=1000, p=0.01)")
print(f"Probabilidad de encontrar EXACTAMENTE {k_objetivo} defectos: {prob_exactamente_5:.4f}")
print(f"Resultado de la simulación (defectos encontrados): {simulacion_defectos}")

# Gráfico para el Ejemplo 1
# Nota: La gráfica puede ser estrecha debido a n=1000. Destacaremos k=5.
plot_binomial(
    n=n_piezas,
    p=p_defecto,
    title="Distribución Binomial: Defectos en Lote de 1000",
    k_highlight=k_objetivo
)

# =========================================================================
# 2. Medicina y Biología (Recuperación de pacientes)
# =========================================================================

# Escenario: 20 pacientes. Probabilidad de recuperación individual es 0.8.
n_pacientes = 20
p_recuperacion = 0.8

dist_medicina = binom(n_pacientes, p_recuperacion)

# Objetivo: Calcular la probabilidad de que 18 O MÁS se recuperen (CDF complementaria)
# P(X >= 18) = 1 - P(X <= 17)
k_limite = 17
prob_18_o_mas = 1 - dist_medicina.cdf(k_limite)

# Simulación: Resultado de recuperación para el grupo de 20
recuperados_simulados = dist_medicina.rvs(size=1)[0]

print("\n2. Medicina: Recuperación de Pacientes (n=20, p=0.8)")
print(f"Probabilidad de que 18 o más pacientes se recuperen: {prob_18_o_mas:.4f}")
print(f"Simulación: Pacientes recuperados en el ensayo: {recuperados_simulados} / 20")

# Gráfico para el Ejemplo 2
# Destacamos k=18, 19 y 20
k_destacados = [18, 19, 20]
plot_binomial(
    n=n_pacientes,
    p=p_recuperacion,
    title="Distribución Binomial: Recuperación de Pacientes",
    k_highlight=k_destacados
)

# =========================================================================
# 3. Encuestas de Opinión Pública y Marketing (Votantes)
# =========================================================================

# Escenario: 50 personas encuestadas. 60% vota por Candidato A.
n_encuesta = 50
p_voto_A = 0.6

dist_votantes = binom(n_encuesta, p_voto_A)

# Objetivo: Calcular la probabilidad de que MENOS de 25 voten por A (CDF)
# P(X < 25) es igual a P(X <= 24)
k_limite = 24
prob_menos_25 = dist_votantes.cdf(k_limite)

# Simulación: Número de votantes por A en una muestra
votantes_simulados = dist_votantes.rvs(size=1)[0]

print("\n3. Encuestas de Opinión: Apoyo al Candidato A (n=50, p=0.6)")
print(f"Probabilidad de que menos de 25 voten por A: {prob_menos_25:.4f}")
print(f"Simulación: Votantes por A encontrados en la muestra: {votantes_simulados} / 50")

# Gráfico para el Ejemplo 3
# Destacamos el rango P(X < 25), es decir, k=0 hasta k=24.
k_rango = list(range(0, 25))
plot_binomial(
    n=n_encuesta,
    p=p_voto_A,
    title="Distribución Binomial: Apoyo en Encuesta",
    k_highlight=k_rango
)

# =========================================================================
# 4. Finanzas y Seguros (Reclamaciones de póliza)
# =========================================================================

# Escenario: 1000 clientes. Probabilidad de reclamo individual es 0.05.
n_clientes = 1000
p_reclamo = 0.05

dist_seguros = binom(n_clientes, p_reclamo)

# Objetivo: Modelar la probabilidad de recibir un número excesivo de reclamaciones.
# Por ejemplo, P(X > 60), que es 1 - P(X <= 60)
k_max_aceptable = 60
prob_excesiva = 1 - dist_seguros.cdf(k_max_aceptable)

# Simulación: Número de reclamos observados en la cartera
reclamos_simulados = dist_seguros.rvs(size=1)[0]

print("\n4. Finanzas y Seguros: Reclamaciones (n=1000, p=0.05)")
print(f"Probabilidad de recibir más de 60 reclamos: {prob_excesiva:.4f}")
print(f"Simulación: Reclamos recibidos: {reclamos_simulados} / 1000")

# Gráfico para el Ejemplo 4
# Destacamos el rango P(X > 60), es decir, k=61 hasta k=1000.
k_rango_excesivo = list(range(61, n_clientes + 1))
plot_binomial(
    n=n_clientes,
    p=p_reclamo,
    title="Distribución Binomial: Reclamaciones de Seguros",
    k_highlight=k_rango_excesivo,
    color_highlight='orange' # Usamos naranja para resaltar el riesgo
)
```

### 3.48 ✨Distribución Hipergeométrica✨

* **Descripción**: Modelo para muestreo sin reemplazo de una población finita.

* **Parámetros**:
- $N$ (tamaño de la población)
- $K$ (número de éxitos en la población)
- $n$ (tamaño de la muestra)

* **Función de Masa de Probabilidad (PMF):**

$$
P(X = k) = \displaystyle{\frac{\binom{K}{k} \binom{N - K}{n - k}}{\binom{N}{n}}}, \quad k = 0, 1, \ldots, \min(K, n)
$$

* **Valor Esperado:** $E[X] = \frac{nK}{N}$

* **Media:** $\mu_{X} = \frac{nK}{N}$

* **Desviación Estándar:** $\displaystyle{\sigma = \sqrt{\frac{nK(N - K)(N - n)}{N^2(N - 1)}}} $

* **Función de Distribución Acumulativa (CDF):**

$$
F(x) = P(X \leq k) = \sum_{j=0}^{\lfloor x \rfloor} \frac{\binom{K}{j} \binom{N - K}{n - j}}{\binom{N}{n}}
$$

* ** Comandos en R:**

```r
### 3.49 PMF
dhyper(k, m = K, n = N - K, size = n)

### 3.50 CDF
phyper(k, m = K, n = N - K, size = n)

### 3.51 Simulation
rhyper(n, m = K, n = N - K, size = n)

#### Ejemplo de Gráfica de la Distribución Hipergeométrica

Esta distribución describe el número de éxitos en una muestra extraída sin reemplazo de una población finita.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom

# Definir los parámetros de la distribución hipergeométrica:
# N = Tamaño total de la población (m + n)
# m = Número total de éxitos en la población (Good items)
# n = Número total de fracasos en la población (Bad items)
# k = Tamaño de la muestra (Picks)

m = 20  # Éxitos en la población (e.g., bolas rojas)
n = 30  # Fracasos en la población (e.g., bolas azules)
N = m + n # Población total = 50
k = 15  # Tamaño de la muestra (Número de extracciones)

# Crear un rango de valores para el número de éxitos (x)
# Los éxitos posibles van desde max(0, k - n) hasta min(m, k).
# Aquí, min(m, k) = min(20, 15) = 15, y max(0, 15-30) = 0.
x_values = np.arange(0, min(m, k) + 1)

# Calcular la PMF (Función de Masa de Probabilidad) de la distribución hipergeométrica
# dhyper(x, m, n, k) en R es equivalente a hypergeom.pmf(x, N, m, k) en Python
pmf_values = hypergeom.pmf(x_values, N, m, k)

# Crear el gráfico de barras
plt.figure(figsize=(9, 6))
plt.bar(
    x_values,
    pmf_values,
    color='#A8325C',  # Color vino/magenta
    alpha=0.8,
    width=0.8
)

# Configurar etiquetas y títulos
plt.title(
    f"Gráfico de la Distribución Hipergeométrica\n(N={N}, m={m}, n={n}, k={k})",
    fontsize=16
)
plt.xlabel("Número de Éxitos en la Muestra (x)", fontsize=12)
plt.ylabel("Probabilidad", fontsize=12)

# Configurar el eje X para mostrar todos los valores enteros
plt.xticks(x_values)

# Configurar el eje Y para que vaya de 0 hasta un poco más del máximo
plt.ylim(0, max(pmf_values) + 0.05)

# Añadir la cuadrícula y mejorar el estilo
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Mostrar el gráfico
plt.show()
```

#### Descripción del Código

* **Cargar librerías**: Se utiliza `ggplot2` para crear la gráfica.
* **Definir los parámetros**: Se establecen los parámetros de la distribución hipergeométrica: el número total de éxitos en la población $m$, el número total de fracasos $ n$ y el tamaño de la muestra $k$.
* **Crear un rango de valores para $ x $**: Se define el rango de valores posibles para el número de éxitos en la muestra, que va de 0 al mínimo entre $ m $ y $ k $.
* **Calcular la PMF**: Se utiliza `dhyper()` para calcular las probabilidades de cada posible número de éxitos en la muestra.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $ x $ y sus correspondientes probabilidades.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de barras que representa la $PMF$ de la distribución hipergeométrica.

**EJERCICIO 3**

Agrega ejemplos y los usos recomendados.

### 3.52 👍🏼Usos Recomendados de la Distribución Hipergeométrica

La Distribución Hipergeométrica se utiliza para modelar la probabilidad de obtener $\mathbf{k}$ éxitos en una muestra de tamaño $\mathbf{n}$, seleccionada *sin reemplazo* de una población finita que contiene $\mathbf{M}$ éxitos y $\mathbf{N}$ fracasos.

### 3.53 1. Control de Calidad y Pruebas de Lotes
Este es quizás el uso más común y directo. Se utiliza cuando se inspecciona un lote de productos y no se devuelve el artículo inspeccionado al lote.

* **Ejemplo:** En un lote de 50 baterías (población total $\mathbf{N+M=50}$), se sabe que 5 están defectuosas ($\mathbf{M=5}$ éxitos—si definir "éxito" como encontrar un defecto). Si seleccionas una muestra de 10 baterías ($\mathbf{k=10}$), la Hipergeométrica calcula la probabilidad de que encuentres exactamente 2 defectuosas en esa muestra.
* **Diferencia clave con Binomial:** Una vez que sacas una batería defectuosa, ¡no la devuelves! La probabilidad de sacar otra defectuosa cambia para el siguiente sorteo.

### 3.54 2. Juegos de Cartas y Lotería
El muestreo de una baraja de cartas es el ejemplo clásico de muestreo sin reemplazo.

* **Ejemplo:** ¿Cuál es la probabilidad de sacar exactamente 3 ases ($\mathbf{k=3}$) cuando se reparten 5 cartas ($\mathbf{n=5}$) de una baraja estándar de 52 cartas ($\mathbf{N+M=52}$), donde hay 4 ases ($\mathbf{M=4}$ éxitos)?
* **Aplicación:** Determinar la probabilidad de que una mano de póquer contenga una combinación específica de figuras o palos.

### 3.55 3. Estimación de Poblaciones y Biología
Se utiliza en la ecología para estimar el tamaño de una población de animales o plantas mediante técnicas de "captura-recaptura".

* **Ejemplo:** Se capturan y marcan 100 peces ($\mathbf{M=100}$) en un estanque. Días después, se toma una nueva muestra de 50 peces ($\mathbf{n=50}$). Si se encuentran 10 peces marcados ($\mathbf{k=10}$), la Hipergeométrica (y los métodos relacionados) ayudan a inferir el tamaño total de la población en el estanque.

### 3.56 4. Distribución de Recursos Limitados
En situaciones donde los recursos son finitos y no se reponen.

* **Ejemplo:** En una oficina con 10 ingenieros de software ($\mathbf{M=10}$) y 10 diseñadores ($\mathbf{N=10}$), se forma un comité de 5 personas ($\mathbf{n=5}$). La Hipergeométrica calcula la probabilidad de que el comité tenga exactamente 4 ingenieros.

---

En resumen, **siempre que el muestreo sea sin reemplazo de una población finita, la Hipergeométrica es la distribución adecuada.**

### 3.57 💻Ejemplos en codigo

```python
import numpy as np
from scipy.stats import hypergeom

print("--- Usos de la Distribución Hipergeométrica ---")

# En la notación de scipy.stats.hypergeom:
# M: Tamaño total de la población (N + M en tu descripción)
# n: Número de éxitos en la población (M en tu descripción)
# N: Tamaño de la muestra (n en tu descripción)
# k: Número de éxitos en la muestra (k en tu descripción)

# =========================================================================
# 1. Control de Calidad y Pruebas de Lotes (Baterías defectuosas)
# =========================================================================

# Escenario: Lote de 50 baterías, 5 defectuosas. Muestra de 10.
M_poblacion = 50   # Tamaño total del lote
n_exitos = 5       # Número de "éxitos" (defectuosas) en el lote
N_muestra = 10     # Tamaño de la muestra

# Creación de la distribución Hipergeométrica
dist_calidad = hypergeom(M=M_poblacion, n=n_exitos, N=N_muestra)

# Objetivo: Probabilidad de encontrar EXACTAMENTE 2 defectuosas en la muestra (PMF)
k_objetivo = 2
prob_exactamente_2 = dist_calidad.pmf(k_objetivo)

print("\n1. Control de Calidad: Baterías Defectuosas")
print(f"Parámetros: Población total={M_poblacion}, Defectuosas={n_exitos}, Muestra={N_muestra}")
print(f"Probabilidad de encontrar EXACTAMENTE {k_objetivo} defectuosas: {prob_exactamente_2:.4f}")

# Simulación: Simular el número de defectuosas en 5 extracciones de 10
simulacion_defectos = dist_calidad.rvs(size=5)
print(f"Simulación (5 extracciones): {simulacion_defectos}")

# =========================================================================
# 2. Juegos de Cartas y Lotería (Ases)
# =========================================================================

# Escenario: Baraja de 52 cartas, 4 ases. Repartir 5 cartas.
M_poblacion = 52   # Baraja completa
n_exitos = 4       # Número de ases
N_muestra = 5      # Cartas repartidas

dist_cartas = hypergeom(M=M_poblacion, n=n_exitos, N=N_muestra)

# Objetivo: Probabilidad de sacar EXACTAMENTE 3 ases (PMF)
k_objetivo = 3
prob_exactamente_3_ases = dist_cartas.pmf(k_objetivo)

print("\n2. Juegos de Cartas: Sacar Ases")
print(f"Parámetros: Cartas totales={M_poblacion}, Ases={n_exitos}, Cartas repartidas={N_muestra}")
print(f"Probabilidad de sacar EXACTAMENTE {k_objetivo} ases: {prob_exactamente_3_ases:.6f}") # Usamos más decimales por baja probabilidad

# Simulación: Simular 5 manos de 5 cartas (número de ases en cada mano)
simulacion_ases = dist_cartas.rvs(size=5)
print(f"Simulación (5 manos): {simulacion_ases}")

# =========================================================================
# 3. Estimación de Poblaciones y Biología (Captura-Recaptura)
# =========================================================================

# Escenario: Población desconocida (M=?), Marcados (n=100). Muestra (N=50). Marcados en muestra (k=10).
# NOTA: En este ejemplo, el objetivo real de "Captura-Recaptura" es ESTIMAR M, no calcular la probabilidad.
# Aquí calcularemos P(k=10) ASUMIENDO una población total M para ilustrar el uso de la PMF.
M_poblacion_asumida = 500  # Asumimos una población total de 500 para el cálculo
n_exitos = 100             # Peces marcados inicialmente
N_muestra = 50             # Tamaño de la segunda muestra

dist_peces = hypergeom(M=M_poblacion_asumida, n=n_exitos, N=N_muestra)

# Objetivo: Probabilidad de encontrar EXACTAMENTE 10 peces marcados en la muestra (PMF)
k_objetivo = 10
prob_exactamente_10_marcados = dist_peces.pmf(k_objetivo)

print("\n3. Biología: Peces Marcados (Asumiendo M=500)")
print(f"Parámetros: Población asumida={M_poblacion_asumida}, Marcados={n_exitos}, Muestra={N_muestra}")
print(f"Probabilidad de encontrar EXACTAMENTE {k_objetivo} marcados: {prob_exactamente_10_marcados:.4f}")

# =========================================================================
# 4. Distribución de Recursos Limitados (Comité de Oficina)
# =========================================================================

# Escenario: 10 Ingenieros + 10 Diseñadores (Total 20). Comité de 5 personas.
M_poblacion = 20   # Total de empleados
n_exitos = 10      # Número de "éxitos" (Ingenieros)
N_muestra = 5      # Tamaño del comité

dist_comite = hypergeom(M=M_poblacion, n=n_exitos, N=N_muestra)

# Objetivo: Probabilidad de que el comité tenga EXACTAMENTE 4 ingenieros (PMF)
k_objetivo = 4
prob_exactamente_4_ingenieros = dist_comite.pmf(k_objetivo)

# Objetivo 2: Probabilidad de que el comité tenga AL MENOS 4 ingenieros (CDF complementaria)
# P(X >= 4) = P(X=4) + P(X=5)
prob_al_menos_4 = dist_comite.pmf(4) + dist_comite.pmf(5)

print("\n4. Recursos Limitados: Comité de Oficina")
print(f"Parámetros: Total empleados={M_poblacion}, Ingenieros={n_exitos}, Comité={N_muestra}")
print(f"Probabilidad de tener EXACTAMENTE {k_objetivo} ingenieros: {prob_exactamente_4_ingenieros:.4f}")
print(f"Probabilidad de tener AL MENOS 4 ingenieros: {prob_al_menos_4:.4f}")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom

# =======================================================================
# Función Genérica para la Gráfica
# =======================================================================
def plot_hypergeom(M_pob, n_exitos, N_muestra, titulo, k_objetivo=None):
    """
    Calcula y grafica la Función de Masa de Probabilidad (PMF)
    de una distribución hipergeométrica.

    Parámetros:
    M_pob (int): Tamaño total de la población (N+M).
    n_exitos (int): Número total de "éxitos" en la población (M).
    N_muestra (int): Tamaño de la muestra (n).
    titulo (str): Título del gráfico.
    k_objetivo (int, optional): El valor de 'k' objetivo a resaltar.
    """

# El número mínimo de éxitos posibles es max(0, N_muestra - (M_pob - n_exitos))
# El número máximo de éxitos posibles es min(N_muestra, n_exitos)
# Sin embargo, para simplicidad visual y práctica, usamos el rango 0 a N_muestra
# (aunque los extremos pueden tener probabilidad 0)

    x = np.arange(0, N_muestra + 1)

# Calculamos la PMF (Función de Masa de Probabilidad)
# Parámetros: (M_pob, n_exitos, N_muestra, x)
    pmf = hypergeom.pmf(x, M_pob, n_exitos, N_muestra)

# Creamos el gráfico de barras
    plt.figure(figsize=(10, 6))

# Graficamos la distribución
    plt.bar(x, pmf, color='skyblue', edgecolor='black', alpha=0.7, label='PMF')

# Resaltamos el valor de k_objetivo si se proporciona
    if k_objetivo is not None:
        if k_objetivo in x:
            prob_objetivo = hypergeom.pmf(k_objetivo, M_pob, n_exitos, N_muestra)
            plt.bar(k_objetivo, prob_objetivo, color='red', edgecolor='darkred', alpha=1.0,
                    label=f'$P(X={k_objetivo})={prob_objetivo:.4f}$')
            plt.scatter(k_objetivo, prob_objetivo, color='red', s=100, zorder=5) # Punto en el objetivo

    plt.title(f'{titulo}\nHipergeométrica(N={M_pob}, M={n_exitos}, n={N_muestra})')
    plt.xlabel('Número de Éxitos en la Muestra (k)')
    plt.ylabel('Probabilidad, P(X=k)')
    plt.xticks(x)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

# =======================================================================
# Aplicación a los Ejemplos
# =======================================================================

# --- 1. Control de Calidad y Pruebas de Lotes ---
# Población total: 50 (M_pob=50)
# Éxitos (Defectuosas): 5 (n_exitos=5)
# Tamaño de la muestra: 10 (N_muestra=10)
# k objetivo: 2
plot_hypergeom(M_pob=50, n_exitos=5, N_muestra=10,
               titulo='1. Control de Calidad: Baterías Defectuosas',
               k_objetivo=2)

# --- 2. Juegos de Cartas y Lotería ---
# Población total: 52 (M_pob=52)
# Éxitos (Ases): 4 (n_exitos=4)
# Tamaño de la muestra: 5 (N_muestra=5)
# k objetivo: 3
plot_hypergeom(M_pob=52, n_exitos=4, N_muestra=5,
               titulo='2. Juegos de Cartas: Sacar Ases en una Mano de 5',
               k_objetivo=3)

# --- 3. Estimación de Poblaciones y Biología (Captura-Recaptura) ---
# Nota: La estimación de la población total (N_pob) a partir de los datos
# es una aplicación indirecta (método de Máxima Verosimilitud).
# Aquí graficamos la probabilidad DE ENCONTRAR 10 PECES MARCADOS, ASUMIENDO
# un tamaño total de población N_pob=500, para propósitos ilustrativos.
# Población total (Asumida): 500 (M_pob=500)
# Éxitos (Peces Marcados): 100 (n_exitos=100)
# Tamaño de la muestra: 50 (N_muestra=50)
# k objetivo: 10
plot_hypergeom(M_pob=500, n_exitos=100, N_muestra=50,
               titulo='3. Estimación de Poblaciones (Asumiendo N=500)',
               k_objetivo=10)

# --- 4. Distribución de Recursos Limitados ---
# Población total: 10 ingenieros + 10 diseñadores = 20 (M_pob=20)
# Éxitos (Ingenieros): 10 (n_exitos=10)
# Tamaño de la muestra: 5 (N_muestra=5)
# k objetivo: 4
plot_hypergeom(M_pob=20, n_exitos=10, N_muestra=5,
               titulo='4. Distribución de Recursos: Ingenieros en un Comité',
               k_objetivo=4)
```

### 3.58 ✨Distribución Geométrica✨

* **Descripción**: Modelo de la cantidad de ensayos necesarios para obtener el primer éxito.

* **Parámetro**: $p$ (probabilidad de éxito en cada ensayo).

* **Función de Masa de Probabilidad (PMF):**

$$
P(X = k) = (1 - p)^{k - 1} p, \quad k = 1, 2, \ldots
$$

* **Valor Esperado:** $
E[X] = \frac{1}{p}
$

* **Media:** $\mu_{X} = \frac{1}{p}$

* **Desviación Estándar:** $ \sigma = \sqrt{\frac{1 - p}{p}}$

* **Función de Distribución Acumulativa (CDF):**

$$
F(x) = P(X \leq k) = 1 - (1 - p)^k, \quad k = 1, 2, \ldots
$$

* **Comandos en R**:

```r
### 3.59 PMF
dgeom(k - 1, prob = p)

### 3.60 CDF
pgeom(k - 1, prob = p)

### 3.61 Simulation
rgeom(n, prob = p)

#### Ejemplo de Gráfica de la Distribución Geométrica

Esta distribución describe el número de ensayos hasta el primer éxito en una serie de ensayos de Bernoulli.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom

# Definir el parámetro de éxito (p)
p = 0.3  # Probabilidad de éxito en cada ensayo

# Crear un rango de valores para el número de fracasos (k) antes del primer éxito
# La distribución geométrica en SciPy (y R) cuenta los fracasos antes del primer éxito.
# Aquí consideramos hasta 10 fracasos.
k_values = np.arange(0, 11)

# Calcular la PMF (Función de Masa de Probabilidad) de la distribución geométrica
# dgeom(k, prob = p) en R es equivalente a geom.pmf(k, p) en Python
pmf_values = geom.pmf(k_values, p)

# Crear el gráfico de barras
plt.figure(figsize=(9, 6))
plt.bar(
    k_values,
    pmf_values,
    color='#3A98B8',  # Color azul cian
    alpha=0.8,
    width=0.8
)

# Configurar etiquetas y títulos
plt.title(
    f"Gráfico de la Distribución Geométrica (p={p})",
    fontsize=16
)
plt.xlabel("Número de Fracasos antes del Primer Éxito (k)", fontsize=12)
plt.ylabel("Probabilidad", fontsize=12)

# Configurar el eje X para mostrar todos los valores enteros
plt.xticks(k_values)

# Configurar el eje Y para que vaya de 0 hasta un poco más del máximo
plt.ylim(0, max(pmf_values) + 0.05)

# Añadir la cuadrícula y mejorar el estilo
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Mostrar el gráfico
plt.show()
```

#### Descripción del Código

* **Cargar librerías**: Se utiliza `ggplot2` para crear la gráfica.
* **Definir el parámetro de éxito**: Se establece la probabilidad de éxito $ p $ en cada ensayo.
* **Crear un rango de valores para $ k $**: Se define el rango de valores posibles para el número de ensayos hasta el primer éxito (de $0$ a $10$).
* **Calcular la PMF**: Se utiliza `dgeom()` para calcular las probabilidades de cada posible número de ensayos.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $ k $ y sus correspondientes probabilidades.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de barras que representa la $PMF$ de la distribución geométrica.

**EJERCICIO 4**

Agrega ejemplos y los usos recomendados.

### 3.62 👍🏼Usos Recomendados de la Distribución Geométrica

La Distribución Geométrica modela el número de **fracasos ($\mathbf{k}$)** que ocurren antes de obtener el **primer éxito** en una secuencia de ensayos de Bernoulli independientes. El éxito debe tener una probabilidad constante $\mathbf{p}$.

Su principal característica es que se enfoca en el **tiempo de espera** hasta que ocurre el evento deseado.

### 3.63 1. Control de Calidad y Pruebas Destructivas
Es ideal para modelar cuántos artículos deben probarse o cuántos intentos fallan hasta que se encuentra un éxito (o un defecto).

* **Ejemplo:** Una línea de producción tiene una tasa de defectos de $p=0.05$. La Geométrica calcula la probabilidad de que se tengan que inspeccionar 10 productos (es decir, 9 fracasos) antes de encontrar el primer producto defectuoso (el primer éxito).
* **Aplicación:** Determinar cuántas veces se puede usar un componente (como un fusible o un interruptor) antes de que falle por primera vez.

### 3.64 2. Marketing y Ventas
Se usa para modelar el número de interacciones o contactos fallidos antes de conseguir la primera conversión o venta.

* **Ejemplo:** Un vendedor contacta a clientes potenciales. Si la probabilidad de cerrar una venta es $p=0.2$, la Geométrica modela cuántos clientes dirán "no" (fracasos) antes de que el vendedor consiga su primera venta (éxito).
* **Aplicación:** Analizar la eficacia de campañas de *email marketing* y predecir el número de correos que se deben enviar antes de obtener la primera respuesta o clic.

### 3.65 3. Juegos de Azar y Pruebas Iterativas
Cualquier juego que se repite hasta que ocurre un resultado específico puede modelarse con esta distribución.

* **Ejemplo:** Lanzamiento de un dado. Si se busca obtener un 6 (probabilidad $p=1/6$), la Geométrica modela la probabilidad de que se necesiten 4 lanzamientos (3 fracasos) hasta que el primer 6 aparezca.
* **Aplicación:** En pruebas de software, modelar el número de compilaciones o *commits* fallidos antes de que el programa corra exitosamente por primera vez.

### 3.66 4. Búsqueda de Recursos y Fallas de Sistemas
Se aplica en escenarios de búsqueda o espera activa.

* **Ejemplo:** Buscar una pieza de repuesto con una probabilidad $p$ de encontrarla en un almacén. La distribución geométrica predice cuántos intentos de búsqueda fallarán antes de localizar la pieza.
* **Aplicación:** Modelar el número de días que pasan (fracasos) hasta que se observa un evento climático específico (éxito), como la primera lluvia intensa de la temporada.

---

### 3.67 En Resumen: La Condición Clave

La distribución Geométrica se diferencia de la Binomial en que **no tiene un número fijo de ensayos ($\mathbf{n}$)**. Los ensayos continúan *hasta* que se obtiene el primer éxito.

### 3.68 💻Ejemplos en codigo

```python
import numpy as np
from scipy.stats import geom

print("--- Usos de la Distribución Geométrica (Número de Fracasos antes del 1er Éxito) ---")

# En la notación de scipy.stats.geom:
# k: Número de fracasos (intentos fallidos) antes del primer éxito.
# p: Probabilidad de éxito en cada intento.

# =========================================================================
# 1. Control de Calidad y Pruebas Destructivas
# =========================================================================

# Escenario: Línea de producción con tasa de defectos p=0.05.
# Éxito = Encontrar un defecto (p = 0.05).
p_defecto = 0.05

# Creación de la distribución Geométrica
dist_calidad = geom(p=p_defecto)

# Objetivo: Probabilidad de encontrar el primer defecto en la inspección N° 10 (es decir, 9 fracasos)
k_fracasos = 9
prob_9_fracasos = dist_calidad.pmf(k_fracasos)

# Simulación: Simular cuántos productos fallan (fracasos) hasta encontrar el 1er defecto
simulacion_defectos = dist_calidad.rvs(size=5)

print("\n1. Control de Calidad: Primer Producto Defectuoso (p=0.05)")
print(f"Probabilidad de que se necesiten 9 FRACASOS antes del primer defecto: {prob_9_fracasos:.4f}")
print(f"Simulación (5 extracciones - número de fracasos antes del éxito): {simulacion_defectos}")

# =========================================================================
# 2. Marketing y Ventas
# =========================================================================

# Escenario: Vendedor con probabilidad de cerrar una venta p=0.2.
# Éxito = Cierre de venta (p = 0.2).
p_venta = 0.2

dist_ventas = geom(p=p_venta)

# Objetivo: Probabilidad de que el vendedor necesite hacer 5 o menos llamadas fallidas (fracasos)
# P(X <= 5)
k_max_fracasos = 5
prob_5_o_menos_fracasos = dist_ventas.cdf(k_max_fracasos)

# Simulación: Simular cuántas llamadas fallan hasta conseguir la 1ra venta
simulacion_ventas = dist_ventas.rvs(size=5)

print("\n2. Marketing y Ventas: Primera Venta (p=0.2)")
print(f"Probabilidad de tener 5 o menos FRACASOS antes de la 1ra venta: {prob_5_o_menos_fracasos:.4f}")
print(f"Simulación (5 intentos - número de fracasos antes del éxito): {simulacion_ventas}")

# =========================================================================
# 3. Juegos de Azar y Pruebas Iterativas
# =========================================================================

# Escenario: Lanzamiento de un dado. Éxito = Obtener un 6.
# p = 1/6
p_dado_6 = 1/6

dist_dado = geom(p=p_dado_6)

# Objetivo: Probabilidad de necesitar 4 lanzamientos totales (3 fracasos) para el primer 6
k_fracasos = 3
prob_3_fracasos = dist_dado.pmf(k_fracasos)

# Simulación: Simular el número de lanzamientos que no son 6 (fracasos) hasta el 1er 6
simulacion_dado = dist_dado.rvs(size=5)

print("\n3. Juegos de Azar: Obtener el primer 6 (p=1/6)")
print(f"Probabilidad de tener EXACTAMENTE {k_fracasos} FRACASOS (4 lanzamientos totales): {prob_3_fracasos:.4f}")
print(f"Simulación (5 intentos - número de fracasos antes del éxito): {simulacion_dado}")

# =========================================================================
# 4. Búsqueda de Recursos y Fallas de Sistemas
# =========================================================================

# Escenario: Buscar una pieza de repuesto. Asumimos p=0.1.
# Éxito = Encontrar la pieza (p = 0.1).
p_encontrar = 0.1

dist_busqueda = geom(p=p_encontrar)

# Objetivo: Probabilidad de necesitar MÁS de 7 días (7 fracasos)
# P(X > 7) = 1 - P(X <= 7)
k_max_fracasos = 7
prob_mas_de_7_dias = 1 - dist_busqueda.cdf(k_max_fracasos)

print("\n4. Búsqueda de Recursos: Encontrar Pieza (p=0.1)")
print(f"Probabilidad de tener MÁS de {k_max_fracasos} FRACASOS (más de 7 días de búsqueda): {prob_mas_de_7_dias:.4f}")

# Simulación: Simular cuántos días fallan hasta encontrar la pieza
simulacion_busqueda = dist_busqueda.rvs(size=5)
print(f"Simulación (5 intentos - número de fracasos antes del éxito): {simulacion_busqueda}")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom

# =======================================================================
# Función Genérica para la Gráfica de la Distribución Geométrica (Fracasos)
# =======================================================================
def plot_geometric_failures(p, max_k_plot, titulo, k_fracasos_objetivo=None):
    """
    Calcula y grafica la Función de Masa de Probabilidad (PMF) de la
    distribución geométrica, mostrando los resultados en función del
    número de FRACASOS antes del primer éxito.

    Parámetros:
    p (float): Probabilidad de éxito en cada ensayo (p).
    max_k_plot (int): Máximo número de ensayos (X) a incluir en el gráfico.
    titulo (str): Título del gráfico.
    k_fracasos_objetivo (int, optional): Número de fracasos objetivo a resaltar.
    """

# X es el número total de ensayos (X >= 1)
    x_ensayos = np.arange(1, max_k_plot + 1)

# Calculamos la PMF: P(X=x) = p * (1-p)^(x-1)
    pmf = geom.pmf(x_ensayos, p)

# Transformamos el eje X a 'Número de Fracasos' (Fracasos = Ensayos - 1)
    x_fracasos = x_ensayos - 1

# Creamos el gráfico de barras
    plt.figure(figsize=(10, 6))

# Graficamos la distribución
    plt.bar(x_fracasos, pmf, color='lightcoral', edgecolor='black', alpha=0.7, label='PMF')

# Resaltamos el valor de fracasos objetivo si se proporciona
    if k_fracasos_objetivo is not None:
        if k_fracasos_objetivo in x_fracasos:
# El ensayo objetivo es k_fracasos + 1
            ensayo_objetivo = k_fracasos_objetivo + 1
            prob_objetivo = geom.pmf(ensayo_objetivo, p)
            plt.bar(k_fracasos_objetivo, prob_objetivo, color='darkred', edgecolor='black', alpha=1.0,
                    label=f'$P(\text{{Fracasos}}={k_fracasos_objetivo})={prob_objetivo:.4f}$')
            plt.scatter(k_fracasos_objetivo, prob_objetivo, color='darkred', s=100, zorder=5) # Punto en el objetivo

    plt.title(f'{titulo}\nDistribución Geométrica ($p={p}$): Fracasos Antes del Primer Éxito')
    plt.xlabel('Número de Fracasos (k) antes del Primer Éxito')
    plt.ylabel('Probabilidad, $P(X=k)$')
# Configuramos las marcas del eje X para mostrar solo los números enteros de fracasos
    plt.xticks(np.arange(0, max_k_plot))
    plt.xlim(-0.5, max_k_plot - 0.5) # Ajustamos límites para mejor visualización
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

# =======================================================================
# Aplicación a los Ejemplos
# =======================================================================

# 1. Control de Calidad y Pruebas Destructivas
# Probabilidad de éxito (encontrar un defecto): p = 0.05
# Fracasos objetivo: 9 (es decir, el 10º producto es el primero defectuoso)
# Graficaremos hasta 40 ensayos (39 fracasos)
plot_geometric_failures(p=0.05, max_k_plot=40,
                        titulo='1. Control de Calidad: Inspección de Productos',
                        k_fracasos_objetivo=9)

# 2. Marketing y Ventas
# Probabilidad de éxito (cerrar una venta): p = 0.2
# Fracasos objetivo: 0 (la primera venta se cierra en el primer intento)
# Graficaremos hasta 15 ensayos (14 fracasos)
plot_geometric_failures(p=0.2, max_k_plot=15,
                        titulo='2. Marketing y Ventas: Fracasos antes de la Primera Venta',
                        k_fracasos_objetivo=0)

# 3. Juegos de Azar y Pruebas Iterativas
# Probabilidad de éxito (obtener un 6): p = 1/6 ≈ 0.1667
# Fracasos objetivo: 3 (el 6 aparece en el 4º lanzamiento)
# Graficaremos hasta 20 ensayos (19 fracasos)
plot_geometric_failures(p=1/6, max_k_plot=20,
                        titulo='3. Juegos de Azar: Lanzar un Dado hasta obtener el Primer 6',
                        k_fracasos_objetivo=3)

# 4. Búsqueda de Recursos y Fallas de Sistemas
# Ejemplo: Buscar una pieza, asumiremos una probabilidad de encontrarla de p = 0.3
# Fracasos objetivo: 2 (la pieza se encuentra en el 3er intento de búsqueda)
# Graficaremos hasta 15 ensayos (14 fracasos)
plot_geometric_failures(p=0.3, max_k_plot=15,
                        titulo='4. Búsqueda de Recursos: Intentos de Búsqueda Fallidos',
                        k_fracasos_objetivo=2)
```

### 3.69 ✨Distribución Negativa Binomial✨

* **Descripción**: Modelo de la cantidad de ensayos necesarios para obtener un número fijo de éxitos (generaliza la distribución geométrica).

* **Parámetros**:
- $r$ (número de éxitos deseados)
- $p$ (probabilidad de éxito)

* **Función de Masa de Probabilidad (PMF):**

$$
P(X = k) = \binom{k + r - 1}{r - 1} p^r (1 - p)^{k}, \quad k = 0, 1, 2, \ldots
$$

* **Valor Esperado:** $E[X] = \frac{r(1 - p)}{p}$

* **Media:** $\mu{X} = \frac{r(1 - p)}{p}$

* **Desviación Estándar:** $ \sigma = \sqrt{\frac{r(1 - p)}{p^2}}$

* **Función de Distribución Acumulativa (CDF):**

$$
F(x) = P(X \leq k) = \sum_{j=0}^{\lfloor x \rfloor} \binom{j + r - 1}{r - 1} p^r (1 - p)^{j}
$$

* **Comandos en R**:

```r
### 3.70 PMF
dnbinom(k, size = r, prob = p)

### 3.71 CDF
pnbinom(k, size = r, prob = p)

### 3.72 Simulación
rnbinom(n, size = r, prob = p)

#### Ejemplo de Gráfica de la Distribución Negativa Binomial
Esta distribución describe el número de ensayos hasta que se obtienen un número fijo de éxitos.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nbinom

# Definir los parámetros de la distribución negativa binomial
# 'n' (size en R) es el número de éxitos deseados (r)
# 'p' (prob en R) es la probabilidad de éxito en cada ensayo
r = 5    # Número de éxitos deseados
p = 0.4  # Probabilidad de éxito en cada ensayo

# Crear un rango de valores para el número de fracasos (k) antes de alcanzar el r-ésimo éxito
# La convención de SciPy (y dnbinom en R) utiliza k como el número de fracasos.
k_values = np.arange(0, 31)  # Considerar hasta 30 fracasos

# Calcular la PMF (Función de Masa de Probabilidad)
# dnbinom(k, size=r, prob=p) en R es equivalente a nbinom.pmf(k, n=r, p=p) en Python
pmf_values = nbinom.pmf(k_values, n=r, p=p)

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(
    k_values,
    pmf_values,
    color='#5C32A8',  # Color púrpura
    alpha=0.8,
    width=0.8
)

# Configurar etiquetas y títulos
plt.title(
    f"Gráfico de la Distribución Negativa Binomial (r={r}, p={p})",
    fontsize=16
)
# El eje X representa el número de fracasos antes de obtener los 5 éxitos.
plt.xlabel("Número de Fracasos (k)", fontsize=12)
plt.ylabel("Probabilidad", fontsize=12)

# Configurar el eje X para mostrar etiquetas cada 5 valores
plt.xticks(np.arange(0, 31, 5))

# Configurar el eje Y para que vaya de 0 hasta un poco más del máximo
plt.ylim(0, max(pmf_values) + 0.05)

# Añadir la cuadrícula y mejorar el estilo
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Mostrar el gráfico
plt.show()
```

#### Descripción del Código

* **Cargar librerías**: Se utiliza `ggplot2` para crear la gráfica.
* **Definir los parámetros**: Se establecen el número de éxitos deseados $size $ y la probabilidad de éxito $ prob $ en cada ensayo.
* **Crear un rango de valores para $ k $**: Se define el rango de valores posibles para el número de ensayos hasta que se obtienen el número especificado de éxitos (de $0$ a $30$).
* **Calcular la PMF**: Se utiliza `dnbinom()` para calcular las probabilidades de cada posible número de ensayos.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $ k $ y sus correspondientes probabilidades.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de barras que representa la $PMF$ de la distribución negativa binomial.

**EJERCICIO 5**

Agrega ejemplos y los usos recomendados.

### 3.73 👍🏼Usos Recomendados de la Distribución Binomial Negativa

La Distribución Binomial Negativa modela el número de **fracasos ($\mathbf{k}$)** que ocurren antes de conseguir un número fijo y deseado de **éxitos ($\mathbf{r}$)**.

Mientras que la Geométrica espera el *primer* éxito ($r=1$), la Binomial Negativa espera el **éxito número $r$**.

### 3.74 1. Pruebas Repetidas en Producción y Calidad
Es ideal para escenarios de muestreo y prueba que continúan hasta alcanzar un umbral de calidad o fallo específico.

* **Ejemplo:** En una línea de ensamblaje, el objetivo es encontrar 5 componentes defectuosos ($\mathbf{r=5}$) para detener la línea y realizar una revisión. Si la probabilidad de encontrar un defecto en cada prueba es $p=0.1$, la Binomial Negativa calcula la probabilidad de que se tengan que inspeccionar exactamente 30 artículos (25 fracasos) para encontrar el quinto defecto.
* **Aplicación:** Modelar cuántas encuestas fallidas (respuestas incompletas o inválidas) deben recopilarse antes de lograr las 100 respuestas válidas ($\mathbf{r=100}$) necesarias para un estudio.

### 3.75 2. Marketing y Ventas con Cuotas
Se utiliza para determinar el esfuerzo (fracasos) requerido para alcanzar una cuota de ventas (éxitos).

* **Ejemplo:** Un vendedor tiene una cuota de 10 ventas en el mes ($\mathbf{r=10}$). Si la probabilidad de cerrar una venta en una llamada es $p=0.15$, la distribución calcula la probabilidad de que el vendedor necesite hacer, por ejemplo, 70 llamadas fallidas antes de alcanzar su décima venta.

### 3.76 3. Medicina y Ensayos Clínicos con Límite de Eventos
Aplica donde la experimentación termina una vez que se ha observado un número suficiente de resultados positivos (o negativos).

* **Ejemplo:** En un ensayo clínico, se requiere que 15 pacientes ($\mathbf{r=15}$) muestren una mejora significativa para declarar un resultado positivo. La Binomial Negativa calcula cuántos pacientes en total tuvieron que ser tratados (fracasos + éxitos) para alcanzar esa mejora número 15.

### 3.77 4. Juegos de Azar y Pruebas Iterativas
Modelar juegos o procesos repetitivos que terminan al alcanzar un marcador o evento específico.

* **Ejemplo:** Un jugador necesita ganar 5 rondas de un juego ($\mathbf{r=5}$) para ganar un torneo. Si su probabilidad de ganar cada ronda es $p=0.4$, la distribución modela la probabilidad de que haya perdido un cierto número de rondas (fracasos) antes de asegurar su quinta victoria.

---

### 3.78 Diferencia Clave

La diferencia fundamental con la Distribución Binomial tradicional es que en esta última, $\mathbf{n}$ (el número total de ensayos) está fijo y se mide el número de éxitos $\mathbf{k}$. En la **Binomial Negativa**, $\mathbf{r}$ (el número de éxitos) está fijo, y se mide el número de **fracasos** $\mathbf{k}$ (o el número total de intentos $k+r$).

### 3.79 💻Ejemplos en codigo

```python
import numpy as np
from scipy.stats import nbinom

print("--- Usos de la Distribución Binomial Negativa ---")
print("Modelando el número de FRACASOS (k) antes de alcanzar r éxitos.")

# En la notación de scipy.stats.nbinom:
# n: Número de éxitos (r) deseados
# k: Número de fracasos ocurridos
# p: Probabilidad de éxito

# =========================================================================
# 1. Pruebas Repetidas en Producción y Calidad
# =========================================================================

# Escenario: Objetivo de encontrar 5 defectos (r=5) para detener la línea.
r_exitos = 5       # Número de éxitos (defectos) deseados
p_defecto = 0.1    # Probabilidad de encontrar un defecto (éxito)
k_fracasos = 25    # Número de fracasos (artículos inspeccionados sin defecto)

# Creación de la distribución Binomial Negativa
dist_calidad = nbinom(n=r_exitos, p=p_defecto)

# Objetivo: Probabilidad de tener EXACTAMENTE 25 fracasos antes del 5to éxito (defecto)
prob_exactamente_25_fracasos = dist_calidad.pmf(k_fracasos)

print("\n1. Control de Calidad: 5 Defectos Detectados (r=5, p=0.1)")
print(f"Probabilidad de tener EXACTAMENTE {k_fracasos} FRACASOS antes del {r_exitos}° defecto: {prob_exactamente_25_fracasos:.4f}")

# Simulación: Simular el número de fracasos (productos no defectuosos) hasta el 5to defecto
simulacion_inspeccion = dist_calidad.rvs(size=5)
print(f"Simulación (5 repeticiones - fracasos antes del 5to éxito): {simulacion_inspeccion}")

# =========================================================================
# 2. Marketing y Ventas con Cuotas
# =========================================================================

# Escenario: Vendedor con cuota de 10 ventas (r=10).
r_exitos = 10      # Número de éxitos (ventas) deseados
p_venta = 0.15     # Probabilidad de cerrar una venta (éxito)
k_fracasos = 70    # Número de fracasos (llamadas fallidas)

dist_ventas = nbinom(n=r_exitos, p=p_venta)

# Objetivo: Probabilidad de tener EXACTAMENTE 70 llamadas fallidas antes de la 10ma venta
prob_exactamente_70_fallas = dist_ventas.pmf(k_fracasos)

print("\n2. Marketing y Ventas: Cuota de 10 Ventas (r=10, p=0.15)")
print(f"Probabilidad de tener EXACTAMENTE {k_fracasos} FRACASOS antes de la {r_exitos}ª venta: {prob_exactamente_70_fallas:.4f}")

# Simulación: Simular el número de llamadas fallidas hasta conseguir la 10ma venta
simulacion_ventas = dist_ventas.rvs(size=5)
print(f"Simulación (5 vendedores - fracasos antes de la 10ª venta): {simulacion_ventas}")

# =========================================================================
# 3. Medicina y Ensayos Clínicos con Límite de Eventos
# =========================================================================

# Escenario: Requerir 15 pacientes con mejora (r=15). Asumimos p=0.7 de mejora.
r_exitos = 15      # Número de éxitos (mejoras) deseados
p_mejora = 0.7     # Probabilidad de que un paciente mejore (éxito)

dist_medicina = nbinom(n=r_exitos, p=p_mejora)

# Objetivo: Probabilidad de que se necesiten 5 o menos pacientes sin mejora (fracasos)
# P(X <= 5)
k_max_fracasos = 5
prob_5_o_menos_fracasos = dist_medicina.cdf(k_max_fracasos)

print("\n3. Ensayos Clínicos: 15 Mejoras (r=15, p=0.7)")
print(f"Probabilidad de tener 5 o menos FRACASOS antes de la {r_exitos}ª mejora: {prob_5_o_menos_fracasos:.4f}")

# Simulación: Simular el número de fracasos (pacientes sin mejora) hasta la 15ª mejora
simulacion_medicina = dist_medicina.rvs(size=5)
print(f"Simulación (5 ensayos - fracasos antes de la 15ª mejora): {simulacion_medicina}")

# =========================================================================
# 4. Juegos de Azar y Pruebas Iterativas
# =========================================================================

# Escenario: Jugador necesita ganar 5 rondas (r=5). Probabilidad de ganar p=0.4.
r_exitos = 5       # Número de éxitos (victorias) deseados
p_ganar = 0.4      # Probabilidad de ganar una ronda (éxito)

dist_juego = nbinom(n=r_exitos, p=p_ganar)

# Objetivo: Probabilidad de que pierda MÁS de 10 rondas (fracasos) antes de la 5ta victoria.
# P(X > 10) = 1 - P(X <= 10)
k_max_fracasos = 10
prob_mas_de_10_fracasos = 1 - dist_juego.cdf(k_max_fracasos)

print("\n4. Juegos de Azar: 5 Victorias (r=5, p=0.4)")
print(f"Probabilidad de tener MÁS de {k_max_fracasos} FRACASOS antes de la {r_exitos}ª victoria: {prob_mas_de_10_fracasos:.4f}")

# Simulación: Simular el número de fracasos (rondas perdidas) hasta la 5ta victoria
simulacion_juego = dist_juego.rvs(size=5)
print(f"Simulación (5 juegos - fracasos antes de la 5ª victoria): {simulacion_juego}")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nbinom

# =======================================================================
# Función Genérica para la Gráfica de la Distribución Binomial Negativa
# =======================================================================
def plot_nbinom_failures(r, p, max_k_plot, titulo, k_fracasos_objetivo=None):
    """
    Calcula y grafica la Función de Masa de Probabilidad (PMF) de la
    distribución Binomial Negativa, mostrando la probabilidad de k fracasos
    antes del r-ésimo éxito.

    Parámetros:
    r (int): Número fijo de éxitos deseados.
    p (float): Probabilidad de éxito en cada ensayo.
    max_k_plot (int): Máximo número de fracasos (k) a incluir en el gráfico.
    titulo (str): Título del gráfico.
    k_fracasos_objetivo (int, optional): Número de fracasos objetivo a resaltar.
    """

# k es el número de fracasos (k >= 0)
    k_fracasos = np.arange(0, max_k_plot + 1)

# Calculamos la PMF: P(X=k) = C(k+r-1, k) * p^r * (1-p)^k
# Parámetros en scipy.stats.nbinom.pmf: (k_fracasos, r, p)
    pmf = nbinom.pmf(k_fracasos, r, p)

# Creamos el gráfico de barras
    plt.figure(figsize=(10, 6))

# Graficamos la distribución
    plt.bar(k_fracasos, pmf, color='mediumpurple', edgecolor='black', alpha=0.7, label='PMF')

# Resaltamos el valor de fracasos objetivo si se proporciona
    if k_fracasos_objetivo is not None:
        if k_fracasos_objetivo in k_fracasos:
            prob_objetivo = nbinom.pmf(k_fracasos_objetivo, r, p)
            plt.bar(k_fracasos_objetivo, prob_objetivo, color='darkviolet', edgecolor='black', alpha=1.0,
                    label=f'$P(\text{{Fracasos}}={k_fracasos_objetivo})={prob_objetivo:.4f}$')
            plt.scatter(k_fracasos_objetivo, prob_objetivo, color='darkviolet', s=100, zorder=5) # Punto en el objetivo

    plt.title(f'{titulo}\nBinomial Negativa ($r={r}, p={p}$): Fracasos Antes del {r}-ésimo Éxito')
    plt.xlabel('Número de Fracasos (k) antes del Éxito $r$')
    plt.ylabel('Probabilidad, $P(X=k)$')
# Configuramos las marcas del eje X para mostrar solo los números enteros de fracasos
    plt.xticks(np.arange(0, max_k_plot + 1, max(1, max_k_plot // 10)))
    plt.xlim(-0.5, max_k_plot + 0.5) # Ajustamos límites para mejor visualización
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

# =======================================================================
# Aplicación a los Ejemplos
# =======================================================================

# 1. Pruebas Repetidas en Producción y Calidad
# Éxitos deseados (defectos a encontrar): r = 5
# Probabilidad de éxito (encontrar un defecto): p = 0.1
# Fracasos objetivo: 25
# Graficaremos hasta 60 fracasos
plot_nbinom_failures(r=5, p=0.1, max_k_plot=60,
                        titulo='1. Control de Calidad: 5 Defectos para Detener la Línea',
                        k_fracasos_objetivo=25)

# 2. Marketing y Ventas con Cuotas
# Éxitos deseados (ventas a cerrar): r = 10
# Probabilidad de éxito (cerrar una venta): p = 0.15
# Fracasos objetivo: 70
# Graficaremos hasta 120 fracasos
plot_nbinom_failures(r=10, p=0.15, max_k_plot=120,
                        titulo='2. Marketing y Ventas: 10 Ventas de Cuota',
                        k_fracasos_objetivo=70)

# 3. Medicina y Ensayos Clínicos con Límite de Eventos
# Éxitos deseados (pacientes con mejora): r = 15
# Probabilidad de éxito (mejora, asumida): p = 0.6
# Fracasos objetivo: 5 (5 pacientes no mejoran antes de la 15ª mejora)
# Graficaremos hasta 20 fracasos
plot_nbinom_failures(r=15, p=0.6, max_k_plot=20,
                        titulo='3. Ensayo Clínico: 15 Pacientes con Mejora',
                        k_fracasos_objetivo=5)

# 4. Juegos de Azar y Pruebas Iterativas
# Éxitos deseados (rondas ganadas): r = 5
# Probabilidad de éxito (ganar la ronda): p = 0.4
# Fracasos objetivo: 7 (7 derrotas antes de la 5ª victoria)
# Graficaremos hasta 20 fracasos
plot_nbinom_failures(r=5, p=0.4, max_k_plot=20,
                        titulo='4. Juegos de Azar: 5 Victorias para Ganar el Torneo',
                        k_fracasos_objetivo=7)
```

### 3.80 ✨Distribución Multinomial✨

* **Descripción**: Extensión de la distribución binomial a más de dos resultados.

* **Parámetros**:
- $n$ (número de ensayos)
- $p_1, p_2, \ldots, p_k$ (probabilidades de cada resultado)

* **Función de Masa de Probabilidad (PMF):**

$$
P(X_1 = k_1, X_2 = k_2, \ldots, X_k = k_k) = \frac{n!}{k_1! k_2! \ldots k_k!} p_1^{k_1} p_2^{k_2} \ldots p_k^{k_k}
$$

* **Valor Esperado:** $E[X_i] = n \cdot p_i, \quad i = 1, 2, \ldots, k$

* **Media:** $ \mu{X} = n \cdot p_i \quad \text{para cada } i$

* **Desviación Estándar:** $\sigma_i = \sqrt{n \cdot p_i \cdot (1 - p_i)}, \quad i = 1, 2, \ldots, k$

* **Función de Distribución Acumulativa (CDF):**

(No existe una fórmula general simple; se utiliza el enfoque de simulación.)

* **Comandos en R:**

```r
### 3.81 PMF
dmultinom(c(k1, k2, ..., kk), size = n, prob = c(p1, p2, ..., pk))

### 3.82 CDF (no hay función directa)

### 3.83 Simulación
rmultinom(n, size = n, prob = c(p1, p2, ..., pk))

#### Ejemplo de Gráfica de la Distribución Distribución Multinomial

Esta distribución describe el número de éxitos en un experimento con múltiples categorías.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multinomial
from itertools import product

# --- 1. Definir los parámetros de la distribución multinomial ---
n = 20  # Número total de ensayos
probabilities = [0.2, 0.5, 0.3]  # Probabilidades para cada categoría (p1, p2, p3)
num_categories = len(probabilities)

# --- 2. Generar todas las combinaciones válidas (x1, x2, x3) ---
# Usamos itertools.product para generar todas las combinaciones de 0 a n para 3 variables.
# Luego filtramos solo aquellas donde la suma es igual a n.

valid_combinations = []
# Iteramos sobre todas las combinaciones posibles de x1, x2, x3
# El límite superior de los rangos es n + 1 para incluir n
for combo in product(range(n + 1), repeat=num_categories):
    if sum(combo) == n:
        valid_combinations.append(combo)

# Convertir la lista de tuplas a un array de NumPy para facilitar el cálculo
counts_array = np.array(valid_combinations)

# --- 3. Calcular la PMF para cada combinación usando multinomial.pmf ---
# dnbinom(row, size = n, prob = probabilities) en R es equivalente a multinomial.pmf(row, n, probabilities) en Python
# 'multinomial' es un objeto que representa la distribución
multinom_dist = multinomial(n=n, p=probabilities)

# Calcula la PMF para todas las combinaciones válidas
pmf_values = multinom_dist.pmf(counts_array)

# Extraer los datos para la gráfica 3D (x1, x2, PMF)
x1_values = counts_array[:, 0]
x2_values = counts_array[:, 1]
# x3_values = counts_array[:, 2] # Se puede omitir ya que está determinado por x1 y x2

# --- 4. Crear el gráfico 3D (Scatter plot para PMF discreta) ---
fig = plt.figure(figsize=(12, 10))
# Añadir la proyección 3D
ax = fig.add_subplot(projection='3d')

# Gráfico de dispersión 3D: x1 en X, x2 en Y, PMF en Z (altura)
scatter = ax.scatter(
    x1_values,
    x2_values,
    pmf_values,
    c=pmf_values,  # Color mapeado a la probabilidad (PMF)
    cmap='viridis',
    s=pmf_values * 5000, # El tamaño del punto también se mapea a la probabilidad
    alpha=0.8
)

# Configurar etiquetas y títulos
ax.set_title(
    f"Distribución Multinomial (n={n}, p={probabilities})",
    fontsize=16
)
ax.set_xlabel("Cuenta de la Categoría 1 ($x_1$)", fontsize=12)
ax.set_ylabel("Cuenta de la Categoría 2 ($x_2$)", fontsize=12)
ax.set_zlabel("Probabilidad (PMF)", fontsize=12)

# Añadir la barra de color para la PMF
cbar = fig.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label('Probabilidad (PMF)', rotation=90)

# Mostrar el gráfico
plt.show()
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multinomial
from itertools import product

# --- 1. Definir los parámetros de la distribución multinomial ---
# Parámetros actualizados del script de R
n = 4  # Número total de ensayos (Éxitos totales)
probabilities = [0.3, 0.5, 0.2]  # Probabilidades para cada categoría (p1, p2, p3)
num_categories = len(probabilities)

# --- 2. Generar todas las combinaciones válidas (x1, x2, x3) ---
# Usamos itertools.product para generar todas las combinaciones de 0 a n para 3 variables.
# Luego filtramos solo aquellas donde la suma es igual a n.

valid_combinations = []
# Iteramos sobre todas las combinaciones posibles de x1, x2, x3
# El límite superior de los rangos es n + 1 para incluir n
for combo in product(range(n + 1), repeat=num_categories):
    if sum(combo) == n:
        valid_combinations.append(combo)

# Convertir la lista de tuplas a un array de NumPy para facilitar el cálculo
counts_array = np.array(valid_combinations)

# --- 3. Calcular la PMF para cada combinación usando multinomial.pmf ---
# 'multinomial' es un objeto que representa la distribución
multinom_dist = multinomial(n=n, p=probabilities)

# Calcula la PMF para todas las combinaciones válidas
pmf_values = multinom_dist.pmf(counts_array)

# Extraer los datos para la gráfica 3D (x1, x2, PMF)
x1_values = counts_array[:, 0]
x2_values = counts_array[:, 1]
# x3_values = counts_array[:, 2] # Se puede omitir ya que está determinado por x1 y x2

# --- 4. Crear el gráfico 3D (Scatter plot para PMF discreta) ---
fig = plt.figure(figsize=(12, 10))
# Añadir la proyección 3D
ax = fig.add_subplot(projection='3d')

# Gráfico de dispersión 3D: x1 en X, x2 en Y, PMF en Z (altura)
scatter = ax.scatter(
    x1_values,
    x2_values,
    pmf_values,
    c=pmf_values,  # Color mapeado a la probabilidad (PMF)
    cmap='plasma', # Cambiado a 'plasma' para un contraste diferente
    s=pmf_values * 10000, # Ajuste de tamaño para n=4
    alpha=0.8
)

# Configurar etiquetas y títulos
ax.set_title(
    f"Distribución Multinomial (n={n}, p={probabilities})",
    fontsize=16
)
ax.set_xlabel("Cuenta de la Categoría 1 ($x_1$)", fontsize=12)
ax.set_ylabel("Cuenta de la Categoría 2 ($x_2$)", fontsize=12)
ax.set_zlabel("Probabilidad (PMF)", fontsize=12)

# Añadir la barra de color para la PMF
cbar = fig.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label('Probabilidad (PMF)', rotation=90)

# Establecer límites para los ejes X e Y (de 0 a n)
ax.set_xlim(0, n)
ax.set_ylim(0, n)
plt.xticks(np.arange(0, n + 1))
plt.yticks(np.arange(0, n + 1))

# Mostrar el gráfico
plt.show()
```

Para ver el archivo guardado, en los archivos de la notebook

```python
import os

# --- Definir la función de listado de archivos ---

def listar_archivos_actuales():
    """
    Lista todos los archivos y directorios en el directorio
    de trabajo actual de Python, similar a list.files() en R.
    """
    try:
# os.listdir() obtiene el contenido del directorio actual ('.')
        archivos = os.listdir('.')

        print("--- Archivos y directorios en el directorio actual ---")

        if not archivos:
            print("El directorio está vacío.")
        else:
            for item in archivos:
                print(f"- {item}")

    except FileNotFoundError:
        print("Error: No se pudo encontrar el directorio de trabajo.")
    except Exception as e:
        print(f"Ocurrió un error al listar los archivos: {e}")

# --- Ejecutar la función ---
listar_archivos_actuales()

# NOTA: En un entorno como este Canvas, la salida puede mostrar archivos
# internos del sistema o archivos que has creado previamente.
```

#### **Descripción del Código**:

* **Número total de éxitos**: Se establece en $n \leftarrow 4$.
* **Probabilidades**: Se definen para cada categoría.
* **Filtrado de combinaciones**: Se obtiene solo aquellas combinaciones que suman $4$ éxitos.
* **Cálculo de PMF**: Utilizando la función `dmultinom`.
* **Gráfico**: Se genera y se guarda como un archivo PNG.

---

**Cómo se lee el gráfico**:

Aquí tienes una guía sobre cómo interpretar el gráfico de la distribución multinomial que generamos:

**Elementos del Gráfico**:
- **Ejes**:
  - **Eje X (Categoría)**: Muestra las diferentes categorías en las que se distribuyen los éxitos. En nuestro caso, hay tres categorías ($x_1$, $x_2$, $x_3$).
  - **Eje Y (Número de Éxitos)**: Muestra la cantidad de éxitos que se pueden observar en cada categoría.

- **Barras**:
  - Cada barra representa el número de éxitos para una categoría específica. La altura de la barra indica la cantidad de veces que se espera que ocurra ese número de éxitos, dado el total de 4 éxitos distribuidos entre las $3$ categorías.

- **Colores**:
  - Cada barra tiene un color diferente (azul, rojo, verde) para facilitar la identificación de las categorías.

- **Facet Wrap**:
  - El gráfico también utiliza `facet_wrap(~pmf)`, lo que significa que podría haber varios paneles dependiendo de los valores de PMF calculados. Esto puede ayudarte a visualizar diferentes combinaciones de éxitos y sus probabilidades.

**Interpretación**:
- **Probabilidades**: Las alturas de las barras representan las probabilidades calculadas de que se produzcan ciertas combinaciones de éxitos en las categorías.
- **Combinaciones Válidas**: Solo se muestran combinaciones que suman el total de éxitos (en este caso, 4). Por ejemplo, una barra que muestra $2$ éxitos en la categoría $x_1$, $1$ en $x_2$ y $1$ en $x_3$ significa que hay una combinación de eventos que distribuye los $4$ éxitos de esta manera.
- **Decisiones de Probabilidad**: Si estás analizando un experimento o una situación, puedes usar este gráfico para entender cómo se distribuyen las probabilidades de éxito entre las diferentes categorías y tomar decisiones basadas en esa información.

**Ejemplo Práctico**:
Si en tu gráfico observas que hay una barra alta para la categoría $x_2$ (por ejemplo, con $3$ éxitos), eso sugiere que es más probable que en tus experimentos obtengas un número mayor de éxitos en esa categoría, dado el modelo y las probabilidades elegidas.

---

**Por qué hay barras que tienen tamaño $5$ junto con otra de tamaño $3$ en el mismo gráfico**:

Las barras en el gráfico de la distribución multinomial representan las combinaciones de éxitos en cada categoría, y sus alturas son el resultado de las probabilidades de esas combinaciones específicas. Aquí hay algunas razones por las que esto puede ocurrir:

1. **Combinaciones de Éxitos**:
   - Cada barra representa una combinación de éxitos en las diferentes categorías. Por ejemplo, si tienes:
     - Categoría $1$ ($x_1$): $3$ éxitos
     - Categoría $2$ ($x_2$): $1$ éxito
     - Categoría $3$ ($x_3$): $0$ éxitos
   - Esto sumaría un total de $4$ éxitos, pero también podría haber otra combinación como:
     - Categoría $1$ ($x_1$): $1$ éxito
     - Categoría $2$ ($x_2$): $3$ éxitos
     - Categoría $3$ ($x_3$): $0$ éxitos
   - Ambas combinaciones son válidas y suman el mismo total de éxitos ($4$), pero su representación en el gráfico puede mostrar distintas alturas en las barras.

2. **Diferencias en la Probabilidad**:
   - La altura de cada barra está determinada por la probabilidad de que ocurran esas combinaciones específicas de éxitos. Esto significa que:
     - La combinación que resulta en $5$ (o más) puede ser más probable que otras combinaciones que suman el mismo total de éxitos.

3. **Efecto de las Probabilidades**:
   - Las probabilidades asignadas a cada categoría (en este caso, $0.3$, $0.5$ y $0.2$) influencian fuertemente el tamaño de las barras. Si una categoría tiene una probabilidad mayor, es más probable que se observe un número mayor de éxitos en esa categoría, lo que puede dar lugar a combinaciones que parecen desproporcionadas en el gráfico.

---

**Los números que aparecen arriba de cada gráfico de barras**:

Los números que aparecen arriba de cada gráfico de barras representan las probabilidades asociadas a cada combinación específica de éxitos en las diferentes categorías. Aquí tienes un desglose de lo que significan:

- **Probabilidades de Combinaciones**: Cada número indica la probabilidad de que ocurra la combinación específica de éxitos en las categorías representadas por las barras.
- **Escala de Probabilidad**: Estas probabilidades se calculan utilizando la función `dmultinom`, donde $0$ significa que esa combinación de éxitos es imposible y $1$ significa que es un evento seguro.
- **Interpretación Contextual**: Al observar estos números, puedes entender qué combinaciones son más probables y cuáles son menos probables.

**EJERCICIO 6**

Agrega ejemplos y los usos recomendados.

### 3.84 👍🏼Usos Recomendados de la Distribución Multinomial

La Distribución Multinomial modela la probabilidad de obtener un conjunto específico de recuentos ($\mathbf{k_1, k_2, ..., k_m}$) para cada una de $\mathbf{m}$ categorías, después de realizar un número fijo de ensayos independientes ($\mathbf{n}$).

### 3.85 1. Encuestas Políticas y Estudios de Mercado
Este es el uso más común, ya que los votantes o consumidores suelen tener más de dos opciones.

* **Ejemplo:** Se encuesta a 1000 personas ($\mathbf{n=1000}$) sobre su preferencia entre tres candidatos: Candidato A ($\mathbf{p_A=0.3}$), Candidato B ($\mathbf{p_B=0.5}$), y Candidato C ($\mathbf{p_C=0.2}$). La Multinomial calcula la probabilidad de que la muestra arroje exactamente 320 votos para A, 510 para B y 170 para C.
* **Aplicación:** Analizar la distribución de elección de marca entre tres o más productos rivales.

### 3.86 2. Genética y Biología
Se utiliza para predecir la distribución de fenotipos o genotipos según las leyes de la herencia (como las leyes de Mendel), donde hay varias posibilidades de resultado.

* **Ejemplo:** Cruzar dos plantas resulta en cuatro posibles fenotipos de semillas (lisas-amarillas, lisas-verdes, rugosas-amarillas, rugosas-verdes) con probabilidades teóricas específicas. La Multinomial permite calcular la probabilidad de observar un cierto número de cada fenotipo en una muestra de 1000 semillas.

### 3.87 3. Clasificación de Datos (Machine Learning)
En el aprendizaje automático, cuando se trabaja con problemas de clasificación multiclase, la Multinomial ayuda a modelar la distribución de las predicciones.

* **Ejemplo:** Un modelo clasifica imágenes en tres categorías (perro, gato, pájaro) con probabilidades predichas $p_1, p_2, p_3$. La Multinomial puede modelar la probabilidad de que, en un lote de 500 imágenes, se obtengan $k_1$ predicciones correctas para 'perro', $k_2$ para 'gato', etc.

### 3.88 4. Distribución de Defectos en Control de Calidad
Cuando los defectos se clasifican por tipo o gravedad.

* **Ejemplo:** En un lote de 200 componentes, los defectos se pueden clasificar en: Críticos ($\mathbf{p_1}$), Mayores ($\mathbf{p_2}$) o Menores ($\mathbf{p_3}$). La Multinomial calcula la probabilidad de observar una combinación específica de estos tres tipos de defectos.

---

### 3.89 Condición Clave

La Distribución Multinomial se diferencia de otras distribuciones discretas en que **los resultados deben ser mutuamente excluyentes y colectivamente exhaustivos** (es decir, la suma de las probabilidades de todas las categorías debe ser igual a 1).

### 3.90 💻Ejemplos en codigo

```python
import numpy as np
from scipy.stats import multinomial

print("--- Usos de la Distribución Multinomial ---")
print("Modelando el conteo de resultados para múltiples categorías.")

# =========================================================================
# 1. Encuestas Políticas y Estudios de Mercado (3 Candidatos)
# =========================================================================

# Escenario: 1000 votantes y 3 candidatos con probabilidades fijas.
n_ensayos = 1000
p_candidatos = [0.3, 0.5, 0.2]  # pA, pB, pC (suman 1.0)

# El resultado exacto que queremos modelar:
k_resultados = [320, 510, 170]  # kA, kB, kC (suman 1000)

# Creación de la distribución Multinomial
dist_politica = multinomial(n=n_ensayos, p=p_candidatos)

# Objetivo: Probabilidad de obtener EXACTAMENTE k_resultados (PMF)
prob_resultados_exactos = dist_politica.pmf(k_resultados)

print("\n1. Encuestas Políticas (n=1000)")
print(f"Probabilidades de Candidatos (p): {p_candidatos}")
print(f"Resultado deseado (k): {k_resultados}")
print(f"Probabilidad de obtener este resultado exacto: {prob_resultados_exactos:.4f}")

# Simulación: Simular 5 resultados de encuestas de 1000 personas
simulacion_encuestas = dist_politica.rvs(size=5)
print(f"Simulación (5 encuestas):")
print(simulacion_encuestas)

# =========================================================================
# 2. Genética y Biología (Fenotipos de Semillas)
# =========================================================================

# Escenario: 1000 semillas con 4 fenotipos posibles según leyes de Mendel (proporción 9:3:3:1)
n_ensayos = 1000
p_fenotipos = [9/16, 3/16, 3/16, 1/16] # Las probabilidades deben sumar 1.0

# El resultado exacto que queremos modelar:
k_resultados = [560, 190, 180, 70] # Observar este conteo específico de los 4 fenotipos

dist_genetica = multinomial(n=n_ensayos, p=p_fenotipos)

# Objetivo: Probabilidad de obtener EXACTAMENTE k_resultados (PMF)
prob_resultados_exactos = dist_genetica.pmf(k_resultados)

print("\n2. Genética y Biología (n=1000)")
print(f"Probabilidades de Fenotipos (p): {[f'{p:.3f}' for p in p_fenotipos]}")
print(f"Resultado observado (k): {k_resultados}")
print(f"Probabilidad de observar este resultado exacto: {prob_resultados_exactos:.4f}")

# =========================================================================
# 3. Clasificación de Datos (Machine Learning)
# =========================================================================

# Escenario: Lote de 500 imágenes clasificadas en 3 categorías.
n_ensayos = 500
# Asumimos que el modelo predice cada clase con estas probabilidades promedio:
p_clases = [0.45, 0.35, 0.20] # Perro, Gato, Pájaro (suman 1.0)

# El resultado exacto que queremos modelar:
k_resultados = [230, 170, 100] # 230 Perro, 170 Gato, 100 Pájaro

dist_ml = multinomial(n=n_ensayos, p=p_clases)

# Objetivo: Probabilidad de obtener EXACTAMENTE k_resultados (PMF)
prob_resultados_exactos = dist_ml.pmf(k_resultados)

print("\n3. Clasificación de Datos (n=500)")
print(f"Probabilidades de Clasificación (p): {p_clases}")
print(f"Resultado deseado (k): {k_resultados}")
print(f"Probabilidad de obtener este resultado exacto: {prob_resultados_exactos:.4f}")

# =========================================================================
# 4. Distribución de Defectos en Control de Calidad
# =========================================================================

# Escenario: Lote de 200 componentes, clasificados en 3 tipos de defectos.
n_ensayos = 200
p_defectos = [0.03, 0.05, 0.92] # pCrítico, pMayor, pMenor (pMenor es no-defecto, el resto es defecto)

# El resultado exacto que queremos modelar:
k_resultados = [4, 8, 188] # 4 Críticos, 8 Mayores, 188 Menores/No-Defectos

dist_defectos = multinomial(n=n_ensayos, p=p_defectos)

# Objetivo: Probabilidad de obtener EXACTAMENTE k_resultados (PMF)
prob_resultados_exactos = dist_defectos.pmf(k_resultados)

print("\n4. Control de Calidad (n=200)")
print(f"Probabilidades de Tipo de Defecto (p): {p_defectos}")
print(f"Resultado deseado (k): {k_resultados}")
print(f"Probabilidad de obtener este resultado exacto: {prob_resultados_exactos:.4f}")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multinomial

# =======================================================================
# Función Genérica para la Gráfica 3D (Solo para m=3 categorías)
# =======================================================================
def plot_multinomial_3d(n_ensayos, probabilidades, recuentos_objetivo=None, titulo='Distribución Multinomial (m=3)'):
    """
    Calcula y grafica la PMF de una distribución Multinomial con 3 categorías.
    Muestra P(k1, k2) donde k3 = n - k1 - k2.

    Parámetros:
    n_ensayos (int): Número fijo de ensayos (n).
    probabilidades (list/array): Probabilidades [p1, p2, p3].
    recuentos_objetivo (list/array, optional): El conjunto de recuentos [k1, k2, k3] a resaltar.
    titulo (str): Título del gráfico.
    """

    p1, p2, p3 = probabilidades

# 1. Definir los posibles recuentos para las dos primeras categorías (k1 y k2)
# k1 puede ir de 0 a n
    k1_range = np.arange(n_ensayos + 1)
# k2 puede ir de 0 a n-k1

    X, Y = np.meshgrid(k1_range, k1_range)

# Inicializar la matriz de probabilidades (eje Z)
    Z = np.zeros_like(X, dtype=float)

# 2. Calcular la probabilidad para cada combinación (k1, k2, k3)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            k1 = X[i, j]
            k2 = Y[i, j]
            k3 = n_ensayos - k1 - k2

# Solo calculamos si la suma de los recuentos es menor o igual a n
            if k3 >= 0:
                recuentos = [k1, k2, k3]
# La PMF requiere n, las probabilidades (p), y los recuentos (k)
                Z[i, j] = multinomial.pmf(recuentos, n=n_ensayos, p=probabilidades)
            else:
                Z[i, j] = np.nan # Usamos NaN para enmascarar valores no posibles

# 3. Crear la figura 3D
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

# Eliminar NaNs para la gráfica de superficie
    X_plot = X.flatten()
    Y_plot = Y.flatten()
    Z_plot = Z.flatten()
    valid_indices = ~np.isnan(Z_plot)

    X_plot = X_plot[valid_indices]
    Y_plot = Y_plot[valid_indices]
    Z_plot = Z_plot[valid_indices]

# Gráfico de puntos (Stem plot) para distribuciones discretas
    ax.bar3d(X_plot, Y_plot, np.zeros_like(Z_plot), 1, 1, Z_plot, color='skyblue', alpha=0.7)

# 4. Resaltar el punto objetivo si se proporciona
    if recuentos_objetivo is not None:
        k1_obj, k2_obj, k3_obj = recuentos_objetivo
        prob_obj = multinomial.pmf(recuentos_objetivo, n=n_ensayos, p=probabilidades)
        ax.bar3d(k1_obj, k2_obj, 0, 1, 1, prob_obj, color='red', alpha=1.0)
        ax.scatter(k1_obj + 0.5, k2_obj + 0.5, prob_obj, color='red', s=100, zorder=5, label=f'$P({k1_obj}, {k2_obj}, {k3_obj})={prob_obj:.5f}$')

# 5. Configuración del gráfico
    ax.set_title(f'{titulo}\nEnsayos $n={n_ensayos}$, Probabilidades $p=[{p1}, {p2}, {p3}]$')
    ax.set_xlabel('Recuento $k_1$ (Candidato A)')
    ax.set_ylabel('Recuento $k_2$ (Candidato B)')
    ax.set_zlabel('Probabilidad $P(k_1, k_2, k_3)$')

# Limitamos los ejes para mejor visualización (solo hasta donde es probable)
    ax.set_xlim(0, n_ensayos)
    ax.set_ylim(0, n_ensayos)

# Ajustamos las marcas del eje X/Y para que no sean demasiado densas
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    ax.yaxis.set_major_locator(plt.MaxNLocator(10))

    plt.legend()
    plt.show()

# =======================================================================
# Aplicación al Ejemplo de Encuestas Políticas (m=3)
# =======================================================================

# 1. Encuestas Políticas
# Ensayos: n = 100
# Probabilidades: [pA=0.3, pB=0.5, pC=0.2]. La suma es 1.0.
# Recuentos objetivo: [kA=32, kB=51, kC=17]. (Reducimos n a 100 para que la gráfica sea manejable)
plot_multinomial_3d(n_ensayos=100,
                    probabilidades=[0.3, 0.5, 0.2],
                    recuentos_objetivo=[32, 51, 17],
                    titulo='1. Encuestas Políticas: Distribución de Votos (n=100)')

# =======================================================================
# Aplicación al Ejemplo de Defectos (m=3) - Visualización 2D (Mapa de Calor)
# =======================================================================

def plot_multinomial_heatmap(n_ensayos, probabilidades, titulo):
    """
    Calcula y grafica la PMF de una distribución Multinomial con 3 categorías
    usando un mapa de calor 2D para una mejor interpretación de la densidad.
    """
    p1, p2, p3 = probabilidades

# Creamos una matriz para los recuentos (k1 vs k2)
    k1_max = n_ensayos
    k2_max = n_ensayos

    prob_matrix = np.full((k1_max + 1, k2_max + 1), np.nan)

    for k1 in range(k1_max + 1):
        for k2 in range(k2_max + 1):
            k3 = n_ensayos - k1 - k2
            if k3 >= 0:
                prob_matrix[k1, k2] = multinomial.pmf([k1, k2, k3], n=n_ensayos, p=probabilidades)

# Creamos el mapa de calor
    plt.figure(figsize=(10, 8))
# Usamos la transpuesta para que k1 sea el eje Y y k2 el eje X
    c = plt.imshow(prob_matrix.T, origin='lower', cmap='viridis', extent=[0, k1_max, 0, k2_max])
    plt.colorbar(c, label='Probabilidad $P(k_1, k_2, k_3)$')

    plt.title(f'{titulo}\nMapa de Calor: Probabilidad de Recuentos $k_1$ (Críticos) y $k_2$ (Mayores)')
    plt.xlabel('Recuento $k_1$ (Defectos Críticos)')
    plt.ylabel('Recuento $k_2$ (Defectos Mayores)')

# Línea que representa k1 + k2 = n (el borde)
    x_line = np.arange(n_ensayos + 1)
    y_line = n_ensayos - x_line
    plt.plot(x_line, y_line, color='red', linestyle='--', alpha=0.7, label='$k_1 + k_2 = n$')

    plt.legend()
    plt.show()

# --- 4. Distribución de Defectos en Control de Calidad ---
# Ensayos (Lote): n = 50 (reducido para mejor visualización)
# Probabilidades: [pCríticos=0.05, pMayores=0.15, pMenores=0.80]
plot_multinomial_heatmap(n_ensayos=50,
                         probabilidades=[0.05, 0.15, 0.80],
                         titulo='4. Control de Calidad: Distribución de Tipos de Defectos (n=50)')
```

### 3.91 ✨Distribución de Poisson✨

* **Descripción**: Modelo de eventos que ocurren en un intervalo fijo de tiempo o espacio.

* **Parámetro**: $\lambda$ (tasa promedio de ocurrencias).

* **Función de Masa de Probabilidad (PMF):**

$$
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \ldots
$$

* **Valor Esperado:** $
E[X] = \lambda
$

* **Media:** $ \mu_X = \lambda$

* **Desviación Estándar:** $\sigma = \sqrt{\lambda}$

* **Función de Distribución Acumulativa (CDF):**

$$
F(x) = P(X \leq k) = \sum_{i=0}^{\lfloor x \rfloor} \frac{\lambda^i e^{-\lambda}}{i!}
$$

* **Comandos en R**:

```r
### 3.92 PMF
dpois(x, lambda)

### 3.93 CDF
ppois(x, lambda)

### 3.94 Simulation
rpois(n, lambda)

#### Ejemplo de Gráfica de la Distribución de Poisson

Esta distribución describe el número de eventos que ocurren en un intervalo fijo de tiempo o espacio, dado un promedio de eventos conocido.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# --- 1. Definir los parámetros de la distribución de Poisson ---
lambda_val = 4  # Promedio de eventos por intervalo (lambda)

# Crear un rango de valores para el número de eventos (k)
k_values = np.arange(0, 16)  # Considerar hasta 15 eventos (0 a 15)

# --- 2. Calcular la PMF de la distribución de Poisson ---
# La función .pmf() calcula P(X = k)
pmf_values = poisson.pmf(k_values, mu=lambda_val)

# Determinar el valor máximo de PMF para el límite del eje Y
max_pmf = np.max(pmf_values)

# --- 3. Graficar la distribución de Poisson ---
plt.figure(figsize=(10, 6))

# Graficar las barras (equivalente a geom_bar(stat="identity") en ggplot2)
plt.bar(
    k_values,
    pmf_values,
    color='blue',
    alpha=0.7,
    width=0.9
)

# Configurar etiquetas y título
plt.title(
    f"Gráfico de la Distribución de Poisson ($\lambda$ = {lambda_val})",
    fontsize=16
)
plt.xlabel("Número de Eventos (k)", fontsize=12)
plt.ylabel("Probabilidad", fontsize=12)

# Configurar el eje X para mostrar solo números enteros
plt.xticks(k_values)

# Configurar el límite del eje Y (similar a ylim en ggplot2)
plt.ylim(0, max_pmf + 0.05)

# Usar tema minimalista (ajustes para Matplotlib)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Mostrar el gráfico
plt.show()
```

#### Descripción del Código

* **Cargar librerías**: Se utiliza `ggplot2` para crear la gráfica.
* **Definir el parámetro**: Se establece el valor de $\lambda$, que es el promedio de eventos por intervalo.
* **Crear un rango de valores para $ k$**: Se define el rango de valores posibles para el número de eventos (de $0$ a $15$).
* **Calcular la PMF**: Se utiliza `dpois()` para calcular las probabilidades de cada posible número de eventos.
* **Crear un data frame**: Se crea un data frame que contiene los valores de $ k $ y sus correspondientes probabilidades.
* **Graficar**: Se utiliza `ggplot` para crear un gráfico de barras que representa la $PMF$ de la distribución de Poisson.

**EJERCICIO 7**

Agrega ejemplos y los usos recomendados.

### 3.95 👍🏼Usos Recomendados de la Distribución de Poisson

La Distribución de Poisson se utiliza para modelar el **número de veces** que un evento ocurre durante un intervalo constante, siempre que los eventos ocurran de manera independiente y a una tasa promedio ($\mathbf{\lambda}$) conocida.

### 3.96 1. Modelado de Tráfico y Telecomunicaciones
Es ideal para analizar la llegada de elementos o clientes a un sistema.

* **Ejemplo:** Contar el número de llamadas que llegan a un centro de atención telefónica en una hora ($\mathbf{\lambda}$ es el promedio de llamadas por hora). La distribución calcula la probabilidad de recibir exactamente 15 llamadas en la próxima hora.
* **Aplicación:** Analizar el número de paquetes de datos que llegan a un *router* por segundo, o el número de clientes que llegan a un supermercado en un lapso de 5 minutos.

### 3.97 2. Seguros y Finanzas
Se utiliza para modelar eventos raros o inesperados que conllevan un riesgo.

* **Ejemplo:** Una compañía de seguros modela el número de reclamaciones por accidentes de tráfico que recibe por mes ($\mathbf{\lambda}$ es el promedio histórico). La Poisson permite calcular la probabilidad de un mes con un número inusualmente alto de reclamaciones.
* **Aplicación:** Evaluar la probabilidad de eventos de gran magnitud pero baja frecuencia, como fallas en equipos críticos o accidentes industriales.

### 3.98 3. Biología y Medicina
Se aplica para contar fenómenos en una muestra o área definida.

* **Ejemplo:** Contar el número de colonias de bacterias que crecen en una placa de Petri por centímetro cuadrado, o el número de mutaciones en una secuencia de ADN.
* **Aplicación:** Modelar el número de glóbulos blancos vistos en un campo de microscopio.

### 3.99 4. Producción y Fiabilidad
Se usa para predecir fallos o defectos que ocurren aleatoriamente en el tiempo.

* **Ejemplo:** Una máquina sufre fallas a una tasa promedio de 2 veces al mes ($\mathbf{\lambda=2}$). La distribución calcula la probabilidad de que la máquina no falle en un mes dado (0 fallas).
* **Aplicación:** Contar el número de defectos superficiales en un metro cuadrado de material (como tela o metal).

---

### 3.100 La Condición Clave

Para usar la Distribución de Poisson, se deben cumplir tres condiciones principales:

1.  **Independencia:** La ocurrencia de un evento no afecta la probabilidad de que ocurra otro.
2.  **Constancia:** La tasa promedio de ocurrencia ($\mathbf{\lambda}$) debe permanecer constante durante todo el intervalo.
3.  **No-Simultaneidad:** Los eventos no pueden ocurrir exactamente al mismo tiempo (aunque esto es a menudo una simplificación teórica).

### 3.101 💻Ejemplos en codigo

```python
import numpy as np
from scipy.stats import poisson

print("--- Usos de la Distribución de Poisson ---")
print("Modelando el número de eventos (k) en un intervalo fijo, dada una tasa promedio (lambda).")

# En la notación de scipy.stats.poisson:
# mu: Tasa promedio de ocurrencia (lambda)
# k: Número de eventos

# =========================================================================
# 1. Modelado de Tráfico y Telecomunicaciones
# =========================================================================

# Escenario: Centro de llamadas. Tasa promedio (lambda) = 10 llamadas/hora.
lambda_llamadas = 10
k_eventos = 15 # Queremos la probabilidad de recibir exactamente 15 llamadas.

# Creación de la distribución de Poisson
dist_llamadas = poisson(mu=lambda_llamadas)

# Objetivo: Probabilidad de obtener EXACTAMENTE 15 llamadas (PMF)
prob_exactamente_15 = dist_llamadas.pmf(k_eventos)

print("\n1. Tráfico y Telecomunicaciones (lambda=10 llamadas/hora)")
print(f"Probabilidad de recibir EXACTAMENTE {k_eventos} llamadas en la próxima hora: {prob_exactamente_15:.4f}")

# Simulación: Simular el número de llamadas en 5 horas diferentes
simulacion_llamadas = dist_llamadas.rvs(size=5)
print(f"Simulación (5 horas): {simulacion_llamadas}")

# =========================================================================
# 2. Seguros y Finanzas
# =========================================================================

# Escenario: Reclamaciones de seguros. Tasa promedio (lambda) = 5 reclamaciones/mes.
lambda_reclamaciones = 5

# Objetivo: Probabilidad de un mes con un número "inusualmente alto" (MÁS de 7)
# P(X > 7) = 1 - P(X <= 7). Usamos CDF para P(X <= 7).
k_max_tolerado = 7
prob_mas_de_7 = 1 - poisson.cdf(k_max_tolerado, mu=lambda_reclamaciones)

print("\n2. Seguros y Finanzas (lambda=5 reclamaciones/mes)")
print(f"Probabilidad de recibir MÁS de {k_max_tolerado} reclamaciones en un mes: {prob_mas_de_7:.4f}")

# Simulación: Simular el número de reclamaciones en 5 meses
simulacion_reclamaciones = poisson.rvs(mu=lambda_reclamaciones, size=5)
print(f"Simulación (5 meses): {simulacion_reclamaciones}")

# =========================================================================
# 3. Biología y Medicina
# =========================================================================

# Escenario: Conteo de colonias de bacterias. Tasa promedio (lambda) = 4 colonias/área.
lambda_colonias = 4

# Objetivo: Probabilidad de encontrar entre 3 y 5 colonias (P(3 <= X <= 5))
# P(X <= 5) - P(X <= 2)
prob_hasta_5 = poisson.cdf(5, mu=lambda_colonias)
prob_hasta_2 = poisson.cdf(2, mu=lambda_colonias)
prob_rango = prob_hasta_5 - prob_hasta_2

print("\n3. Biología y Medicina (lambda=4 colonias/área)")
print(f"Probabilidad de encontrar entre 3 y 5 colonias por área: {prob_rango:.4f}")

# =========================================================================
# 4. Producción y Fiabilidad
# =========================================================================

# Escenario: Fallas de máquina. Tasa promedio (lambda) = 2 fallas/mes.
lambda_fallas = 2
k_eventos = 0 # Queremos la probabilidad de 0 fallas (que la máquina NO falle)

# Objetivo: Probabilidad de no tener fallas (0 fallas) en el mes (PMF)
prob_0_fallas = poisson.pmf(k_eventos, mu=lambda_fallas)

print("\n4. Producción y Fiabilidad (lambda=2 fallas/mes)")
print(f"Probabilidad de que la máquina tenga 0 fallas en un mes: {prob_0_fallas:.4f}")
```

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# =======================================================================
# Función Genérica para la Gráfica de la Distribución de Poisson
# =======================================================================
def plot_poisson(lambda_rate, max_k_plot, titulo, k_objetivo=None):
    """
    Calcula y grafica la Función de Masa de Probabilidad (PMF) de la
    Distribución de Poisson.

    Parámetros:
    lambda_rate (float): Tasa promedio de ocurrencia (lambda).
    max_k_plot (int): Máximo número de eventos (k) a incluir en el gráfico.
    titulo (str): Título del gráfico.
    k_objetivo (int, optional): Número de eventos objetivo a resaltar.
    """

# k es el número de ocurrencias (k >= 0)
    k_eventos = np.arange(0, max_k_plot + 1)

# Calculamos la PMF: P(X=k) = (lambda^k * e^(-lambda)) / k!
    pmf = poisson.pmf(k_eventos, lambda_rate)

# Creamos el gráfico de barras
    plt.figure(figsize=(10, 6))

# Graficamos la distribución
    plt.bar(k_eventos, pmf, color='teal', edgecolor='black', alpha=0.7, label='PMF')

# Resaltamos el valor objetivo si se proporciona
    if k_objetivo is not None:
        if k_objetivo <= max_k_plot:
            prob_objetivo = poisson.pmf(k_objetivo, lambda_rate)
            plt.bar(k_objetivo, prob_objetivo, color='darkgreen', edgecolor='black', alpha=1.0,
                    label=f'$P(X={k_objetivo})={prob_objetivo:.4f}$')
            plt.scatter(k_objetivo, prob_objetivo, color='darkgreen', s=100, zorder=5) # Punto en el objetivo

    plt.title(f'{titulo}\nDistribución de Poisson ($\lambda={lambda_rate}$)')
    plt.xlabel('Número de Ocurrencias (k) en el Intervalo')
    plt.ylabel('Probabilidad, $P(X=k)$')
# Configuramos las marcas del eje X para mejor legibilidad
    plt.xticks(np.arange(0, max_k_plot + 1, max(1, max_k_plot // 10)))
    plt.xlim(-0.5, max_k_plot + 0.5) # Ajustamos límites para mejor visualización
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

# =======================================================================
# Aplicación a los Ejemplos
# =======================================================================

# 1. Modelado de Tráfico y Telecomunicaciones
# Promedio de llamadas por hora: Asumamos lambda = 12
# Eventos objetivo: 15 llamadas
# Graficaremos hasta 25 llamadas
plot_poisson(lambda_rate=12, max_k_plot=25,
             titulo='1. Telecomunicaciones: Número de Llamadas por Hora',
             k_objetivo=15)

# 2. Seguros y Finanzas
# Promedio de reclamaciones por mes: Asumamos lambda = 4
# Eventos objetivo: 0 reclamaciones (un mes tranquilo)
# Graficaremos hasta 15 reclamaciones
plot_poisson(lambda_rate=4, max_k_plot=15,
             titulo='2. Seguros: Número de Reclamaciones por Mes',
             k_objetivo=0)

# 3. Biología y Medicina
# Promedio de colonias por cm²: Asumamos lambda = 5.5
# Eventos objetivo: 8 colonias
# Graficaremos hasta 15 colonias
plot_poisson(lambda_rate=5.5, max_k_plot=15,
             titulo='3. Biología: Colonias de Bacterias por cm²',
             k_objetivo=8)

# 4. Producción y Fiabilidad
# Promedio de fallas al mes: lambda = 2
# Eventos objetivo: 0 fallas (no falle en un mes)
# Graficaremos hasta 10 fallas
plot_poisson(lambda_rate=2, max_k_plot=10,
             titulo='4. Producción: Fallas de Máquina por Mes',
             k_objetivo=0)
```

---

### 3.102 Resumen del Protocolo Maestro
- **Solución Analítica Resaltada**: $\boxed{\text{Verificado con SymPy y SciPy stats}}$
- **Verificación Simbólica (SymPy)**:


---

## 10. Módulo de Simulación: Algoritmo de Generación Estocástica de Variables Discretas

La generación de variables aleatorias discretas a partir de una variable uniforme $U \sim \text{Uniforme}(0, 1)$ se fundamenta en la **Inversión por Suma Acumulada de la PMF**.

### 10.1 Algoritmo General de Inversión Discreta
Dada una variable discreta $X$ con PMF $P(X = x_k) = p_k$:
1. Generar $U \sim \text{Uniforme}(0, 1)$.
2. Retornar el menor valor $x_k$ tal que $\sum_{j=1}^k p_j \ge U$.

### 10.2 Simulación Estocástica de Fallas de Micro-sensores (Poisson)
```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from IPython.display import display, Math

np.random.seed(123)
N_sim = 50_000
lam = 4.5 # Promedio de defectos por obleas de silicio

# Generación directa por inversión
u_vals = stats.uniform.rvs(size=N_sim)
sim_poisson = stats.poisson.ppf(u_vals, mu=lam)

media_sim = np.mean(sim_poisson)
var_sim = np.var(sim_poisson)

display(Math(fr"\text{{Media Simulada (Poisson }} \lambda={lam}\text{{): }} {media_sim:.4f}"))
display(Math(fr"\text{{Varianza Simulada: }} {var_sim:.4f}"))
```


---
## 9. Verificación Simbólica y Expresión Formal con SymPy

Para variables aleatorias discretas, la Media $\mu = E[X]$ y Varianza $\sigma^2 = V(X)$ se verifican analíticamente a través del operador de suma simbólica de **SymPy**.

### 9.1 Valor Esperado $E[X]$ y Varianza $Var(X)$ para Distribución Poisson

$$\boxed{E[X] = \lambda, \quad Var(X) = \lambda}$$

```python
import sympy as sp
from IPython.display import display, Math

x, lmbda = sp.symbols('x lambda', positive=True)
k = sp.Symbol('k', integer=True, nonnegative=True)

# Función de Masa de Probabilidad (PMF) de Poisson
pmf_poisson = (lmbda**k * sp.exp(-lmbda)) / sp.factorial(k)

# Esperanza Matemática: Suma k * P(X=k) de k=0 a infinito
esperanza = sp.summation(k * pmf_poisson, (k, 0, sp.oo))

display(Math(r'\text{PMF Simbólica de Poisson: } ' + sp.latex(pmf_poisson)))
display(Math(r'\text{Esperanza Analítica Demostrada } E[X]: ' + sp.latex(esperanza)))
```
