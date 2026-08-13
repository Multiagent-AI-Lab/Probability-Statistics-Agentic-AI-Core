"""
Reemplaza los bloques de código SymPy sintéticos/placeholders
por demostraciones matemáticas reales y relevantes para cada Unidad en lecciones/*.md
"""

import os
import glob

u2_sympy_real = """
## 9. Verificación Simbólica y Expresión Formal con SymPy

En combinatoria y probabilidad, **SymPy** permite verificar analíticamente las fórmulas de permutaciones, combinaciones y el Teorema de Bayes.

### 9.1 Demostración Simbólica del Coeficiente Binomial $C(n,k)$

$$\\boxed{C(n,k) = \\binom{n}{k} = \\frac{n!}{k!(n-k)!}}$$

```python
import sympy as sp
from IPython.display import display, Math

# Definición de variables simbólicas
n, k = sp.symbols('n k', positive=True, integer=True)
comb_simbolica = sp.binomial(n, k)
formula_factorial = sp.factorial(n) / (sp.factorial(k) * sp.factorial(n - k))

display(Math(r'\\text{Expresión Simbólica de Combinaciones } C(n,k): ' + sp.latex(comb_simbolica)))
display(Math(r'\\text{Fórmula Analítica con Factoriales: } ' + sp.latex(formula_factorial)))

# Evaluación exacta para muestra de n=10 elementos en grupos de k=3
evaluacion = comb_simbolica.subs({n: 10, k: 3})
display(Math(fr'\\text{{Resultado Exacto SymPy }} C(10, 3) = \\mathbf{{{evaluacion}}}'))
```
"""

u3_sympy_real = """
## 9. Verificación Simbólica y Expresión Formal con SymPy

Para variables aleatorias discretas, la Media $\\mu = E[X]$ y Varianza $\\sigma^2 = V(X)$ se verifican analíticamente a través del operador de suma simbólica de **SymPy**.

### 9.1 Valor Esperado $E[X]$ y Varianza $Var(X)$ para Distribución Poisson

$$\\boxed{E[X] = \\lambda, \\quad Var(X) = \\lambda}$$

```python
import sympy as sp
from IPython.display import display, Math

x, lmbda = sp.symbols('x lambda', positive=True)
k = sp.Symbol('k', integer=True, nonnegative=True)

# Función de Masa de Probabilidad (PMF) de Poisson
pmf_poisson = (lmbda**k * sp.exp(-lmbda)) / sp.factorial(k)

# Esperanza Matemática: Suma k * P(X=k) de k=0 a infinito
esperanza = sp.summation(k * pmf_poisson, (k, 0, sp.oo))

display(Math(r'\\text{PMF Simbólica de Poisson: } ' + sp.latex(pmf_poisson)))
display(Math(r'\\text{Esperanza Analítica Demostrada } E[X]: ' + sp.latex(esperanza)))
```
"""

u4_sympy_real = """
## 9. Verificación Simbólica y Expresión Formal con SymPy

En distribuciones conjuntas, las densidades marginales y la condición de normalización $\\int \\int f(x,y) dx dy = 1$ se derivan por integración simbólica multivariada en **SymPy**.

### 9.1 Integración Simbólica de Densidad Bivariada

$$\\boxed{\\int_{-\\infty}^{\\infty} \\int_{-\\infty}^{\\infty} f(x,y) dx dy = 1}$$

```python
import sympy as sp
from IPython.display import display, Math

x, y = sp.symbols('x y', real=True)
c = sp.Symbol('c', positive=True)

# Densidad conjunta f(x,y) = c * x * y en [0,1]x[0,1]
f_xy = c * x * y

# Cálculo de la constante de normalización 'c'
integral_doble = sp.integrate(f_xy, (x, 0, 1), (y, 0, 1))
c_resuelto = sp.solve(integral_doble - 1, c)[0]

display(Math(r'\\text{Constante de Normalización } c: ' + sp.latex(c_resuelto)))
display(Math(r'\\text{Densidad Conjunta Validada } f(x,y): ' + sp.latex(c_resuelto * x * y)))
```
"""

u5_sympy_real = """
## 9. Verificación Simbólica y Expresión Formal con SymPy

Para variables aleatorias continuas, la Función de Densidad de Probabilidad (PDF) Normal $N(\\mu, \\sigma^2)$ se integra analíticamente en **SymPy**.

### 9.1 Integración de la Densidad Gaussiana

$$\\boxed{f(x) = \\frac{1}{\\sigma \\sqrt{2\\pi}} e^{-\\frac{1}{2}\\left(\\frac{x-\\mu}{\\sigma}\\right)^2}}$$

```python
import sympy as sp
from IPython.display import display, Math

x, mu, sigma = sp.symbols('x mu sigma', real=True)
sigma = sp.Symbol('sigma', positive=True)

pdf_normal = (1 / (sigma * sp.sqrt(2 * sp.pi))) * sp.exp(-((x - mu)**2) / (2 * sigma**2))

# Verificación del área total bajo la curva integral = 1
area_total = sp.integrate(pdf_normal, (x, -sp.oo, sp.oo))

display(Math(r'\\text{PDF Normal Simbólica: } ' + sp.latex(pdf_normal)))
display(Math(r'\\text{Área Total Demostrada } \\int_{-\\infty}^{\\infty} f(x) dx: ' + sp.latex(area_total)))
```
"""

u6_sympy_real = """
## 9. Verificación Simbólica y Expresión Formal con SymPy

En inferencia estadística, la Estimación de Máxima Verosimilitud (MLE) se obtiene diferenciando simbólicamente la función de Log-Verosimilitud $\\frac{d}{d\\theta} \\ln L(\\theta) = 0$ con **SymPy**.

### 9.1 Estimador MLE de la Media Normal $\\hat{\\mu}_{MLE}$

$$\\boxed{\\hat{\\mu}_{MLE} = \\bar{X} = \\frac{1}{n} \\sum_{i=1}^n X_i}$$

```python
import sympy as sp
from IPython.display import display, Math

mu, sigma, n = sp.symbols('mu sigma n', positive=True)
sum_x = sp.Symbol('(\\sum X_i)', real=True)

# Log-Verosimilitud de n observaciones normales
log_L = - (n / 2) * sp.log(2 * sp.pi * sigma**2) - (1 / (2 * sigma**2)) * (sp.Symbol('(\\sum X_i^2)') - 2 * mu * sum_x + n * mu**2)

# Derivada respecto a mu
d_logL_dmu = sp.diff(log_L, mu)
mu_mle = sp.solve(d_logL_dmu, mu)[0]

display(Math(r'\\text{Ecuación de Score } \\frac{d \\ln L}{d\\mu}: ' + sp.latex(d_logL_dmu)))
display(Math(r'\\text{Estimador MLE Resuelto } \\hat{\\mu}: ' + sp.latex(mu_mle)))
```
"""

units_map = {
    "UNIDAD_2_PROBABILIDAD_COMBINATORIA.md": u2_sympy_real,
    "UNIDAD_3_VARIABLES_ALEATORIAS_DISCRETAS.md": u3_sympy_real,
    "UNIDAD_4_DISTRIBUCIONES_CONJUNTAS.md": u4_sympy_real,
    "UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.md": u5_sympy_real,
    "UNIDAD_6_INFERENCIA_ESTIMACION.md": u6_sympy_real,
}

lecciones_dir = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\lecciones'

print("=== REEMPLAZANDO BLOQUES SYMPY SINTÉTICOS POR DEMOSTRACIONES REALES ===")
for filename, real_block in units_map.items():
    filepath = os.path.join(lecciones_dir, filename)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        
    # Eliminar bloque sintético anterior si existía
    if "## 9. Verificación Simbólica" in text:
        text = text[:text.find("## 9. Verificación Simbólica")].strip()
        
    # Concatenar nuevo bloque matemático real
    text = text + "\n\n---\n" + real_block.strip() + "\n"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
        
    print(f"[REEMPLAZADO SYMPY REAL OK] {filename}")
