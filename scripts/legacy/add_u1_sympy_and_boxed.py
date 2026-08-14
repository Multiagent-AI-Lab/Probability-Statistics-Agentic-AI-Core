"""
Script para agregar Verificación Simbólica en SymPy y Solución Analítica en \\boxed{}
a UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md para cumplir al 100% los 8 componentes del Protocolo Maestro.
"""

u1_sympy_section = """

---

## 9. Verificación Simbólica y Expresión Formal con SymPy

En el análisis estadístico descriptivo, las fórmulas de los momentos muéstrales se derivan de forma analítica exacta utilizando computación simbólica en **SymPy**.

### 9.1 Expresión Simbólica de la Media Muestral ($\bar{X}$) y Varianza ($S^2$)

La media muestral $\bar{X}$ se define axiomáticamente como:
$$\\boxed{\\bar{X} = \\frac{1}{n} \\sum_{i=1}^n X_i}$$

```python
import sympy as sp
from IPython.display import display, Math

# Definición de variables simbólicas
n = sp.Symbol('n', positive=True, integer=True)
x = sp.IndexedBase('x')
i = sp.Symbol('i', integer=True)

# Expresión simbólica de la media muestral
media_simbolica = (1/n) * sp.Sum(x[i], (i, 1, n))

# Expresión simbólica de la varianza muestral sesgada e imparcial (n-1)
varianza_simbolica = (1/(n - 1)) * sp.Sum((x[i] - media_simbolica)**2, (i, 1, n))

display(Math(fr"\\text{{Fórmula Simbólica de la Media Muestral }} \\bar{{X}}: {sp.latex(media_simbolica)}"))
display(Math(fr"\\text{{Fórmula Simbólica de la Varianza Muestral }} S^2: {sp.latex(varianza_simbolica)}"))
```
"""

u1_path = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\lecciones\UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md'

with open(u1_path, 'r', encoding='utf-8') as f:
    text = f.read()

if "Verificación Simbólica y Expresión Formal con SymPy" not in text:
    with open(u1_path, 'w', encoding='utf-8') as f:
        f.write(text + "\n" + u1_sympy_section)
    print("Sección SymPy y \\boxed{} agregada exitosamente a Unidad 1.")
