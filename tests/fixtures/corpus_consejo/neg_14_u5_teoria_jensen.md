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

### 1.4 La Desigualdad de Jensen: $\mathbb{E}[g(X)]$ vs. $g(\mathbb{E}[X])$

Un error frecuente al transformar una variable aleatoria es asumir que $\mathbb{E}[g(X)] = g(\mathbb{E}[X])$ — es decir, que "el promedio de la función es la función del promedio". Esto es **falso en general** cuando $g$ no es lineal. La propia fórmula de la varianza de arriba ya lo evidencia: si fuera cierto que $\mathbb{E}[X^2]=(\mathbb{E}[X])^2$, la varianza de cualquier variable no constante sería siempre cero.

La **Desigualdad de Jensen** precisa la dirección del error: si $g$ es una función **convexa** (como $g(x)=x^2$),
$$\mathbb{E}[g(X)] \ge g(\mathbb{E}[X])$$
(la desigualdad se invierte para $g$ cóncava). Intuitivamente, una función convexa "premia más" los valores alejados de la media de lo que "penaliza" los cercanos, por lo que promediar después de transformar da un resultado mayor o igual que transformar el promedio.

**Ejemplo aplicado**: la temperatura de un reactor de síntesis varía uniformemente $X\sim U(20,80)\ ^\circ\text{C}$ dentro de la ventana operativa. Si el consumo energético del sistema de calentamiento es proporcional al cuadrado de la temperatura, $Y=X^2$:
$$\mathbb{E}[X] = \frac{20+80}{2}=50, \qquad g(\mathbb{E}[X]) = 50^2 = 2500$$
$$\mathbb{E}[X^2] = \text{Var}(X) + (\mathbb{E}[X])^2 = \frac{(80-20)^2}{12} + 2500 = 300 + 2500 = \boxed{2800 \ne 2500}$$

```python
import numpy as np

a, b = 20, 80  # X ~ U(a, b): temperatura del reactor en grados C

E_X = (a + b) / 2
Var_X = (b - a) ** 2 / 12
E_X2 = Var_X + E_X ** 2  # E[X^2] via Var(X) = E[X^2] - (E[X])^2
g_de_E_X = E_X ** 2       # g(E[X]) = (E[X])^2

print(f"E[X] = {E_X}")
print(f"g(E[X]) = (E[X])^2 = {g_de_E_X}")
print(f"E[X^2] (via Var(X) + E[X]^2) = {E_X2}")
print(f"¿Se cumple Jensen (E[X^2] >= g(E[X]))? {E_X2 >= g_de_E_X}")

## Verificacion por simulacion Monte Carlo
rng = np.random.default_rng(0)
muestras = rng.uniform(a, b, size=500_000)
print(f"\nE[X^2] simulado: {np.mean(muestras ** 2):.2f}  (teorico: {E_X2})")
```

**Verificación simbólica (SymPy)**: en vez de sustituir $a=20,b=80$ desde el inicio, se puede integrar la densidad uniforme dejando $a,b$ como símbolos y sustituir al final, confirmando que la fórmula cerrada coincide con los valores numéricos ya publicados.

```python
import sympy as sp

## 1. Definicion de simbolos
x = sp.Symbol('x', real=True)
a, b = sp.symbols('a b', real=True)
a_val, b_val = 20, 80  # X ~ U(20, 80): temperatura del reactor en grados C

## 2. Densidad uniforme simbolica f(x) = 1/(b-a) en [a, b]
pdf_uniforme = 1 / (b - a)

## 3. E[X] simbolico via integracion, luego sustitucion numerica
E_X_simbolico = sp.simplify(sp.integrate(x * pdf_uniforme, (x, a, b)))
E_X_num = E_X_simbolico.subs({a: a_val, b: b_val})
print(f"E[X] simbolico = {E_X_simbolico}  ->  E[X] = {E_X_num}")

## 4. g(E[X]) = (E[X])^2
g_de_E_X = E_X_num ** 2
print(f"g(E[X]) = {g_de_E_X}")

## 5. E[X^2] simbolico via integracion, luego sustitucion numerica
E_X2_simbolico = sp.simplify(sp.integrate(x**2 * pdf_uniforme, (x, a, b)))
E_X2_num = E_X2_simbolico.subs({a: a_val, b: b_val})
print(f"E[X^2] simbolico = {E_X2_simbolico}  ->  E[X^2] = {E_X2_num}")

## 6. Diferencia = Var(X), confirmando Jensen para g(x) = x^2
diferencia = sp.simplify(E_X2_num - g_de_E_X)
print(f"E[X^2] - g(E[X]) = {diferencia}  (debe ser Var(X) = 300)")
```

La integración simbólica reproduce exactamente los valores ya calculados: $\mathbb{E}[X]=50$, $g(\mathbb{E}[X])=2500$, $\mathbb{E}[X^2]=2800$ y la diferencia $=300$, confirmando de forma independiente (sin depender de la fórmula atajo $\text{Var}(X)=\mathbb{E}[X^2]-(\mathbb{E}[X])^2$) que el resultado numérico es correcto.

La diferencia de $300$ entre ambos valores **no es un error de cálculo**: es exactamente $\text{Var}(X)$, lo cual no es casualidad — reordenando la fórmula de la varianza, $\mathbb{E}[X^2]-(\mathbb{E}[X])^2=\text{Var}(X)\ge0$ siempre, que es precisamente la Desigualdad de Jensen aplicada al caso particular $g(x)=x^2$. En ingeniería de procesos, ignorar esta distinción al estimar consumo energético o cualquier magnitud que dependa de forma no lineal de una variable de proceso lleva a subestimar sistemáticamente el promedio real de esa magnitud.

Esta unidad, como el resto del curso, sigue el **Ciclo de Verificación Triple** documentado en `GOVERNANCE.md`: Teoría → Verificación Simbólica (SymPy) → Solución Computacional (SciPy) → Interpretación. El ejemplo de Jensen anterior ya lo aplicó de forma inline; la Sección 4 lo repite de manera formal para la familia Normal.

---

## 2. Familias Principales de Distribuciones Continuas
