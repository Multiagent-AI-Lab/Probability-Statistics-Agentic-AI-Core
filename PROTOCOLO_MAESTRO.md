# PROTOCOLO MAESTRO: ESTÁNDARES DE CALIDAD Y REGLA DE ORO

> [!IMPORTANT]
> Este documento es la **Ley Suprema** para la remediación de las lecciones y notebooks. Ninguna entrega será aprobada por el `@QA` si no cumple estrictamente con los 9 componentes.

---

## 1. Regla de Oro: Los 9 Componentes Obligatorios

Para **CADA** tema o lección presentada, se deben incluir obligatoriamente:

1. **Teoría Completa**: $\ge 800$ palabras con rigor académico y derivaciones.
2. **Ejemplo Analítico Paso a Paso**: Mínimo 5 pasos numéricos explícitos.
3. **Código de Verificación Simbólica (SymPy)**: Validación simbólica exacta del ejemplo analítico.
4. **Contexto de Aplicación Nanotecnológica**: $\ge 150$ palabras sobre relevancia en nanomedicina, nanoestructuras o fotónica.
5. **Solución Analítica Resaltada**: Resultado numérico final contenido en $\boxed{}$.
6. **Solución Computacional (SciPy / Statsmodels)**: Código documentado en Python con type hints.
7. **Gráficos Profesionales**: Mínimo 2 gráficos usando `Seaborn` o `Matplotlib`.
8. **Interpretación Post-Gráfico**: $\ge 150$ palabras de análisis físico/estadístico tras cada visualización.
9. **Diccionario de Variables**: Lista con formato `* $símbolo$: descripción`, mínimo 2 entradas, indicando nombre físico, unidades y descripción de cada variable usada en la unidad.

---

## 2. Formato de Visualización Matemática

Queda prohibido el uso de `print()` plano para fórmulas matemáticas en Python. Se debe emplear:

```python
from IPython.display import display, Math

display(Math(rf"\text{{Media: }} \bar{{x}} = {media:.2f} \text{{ nm}}"))
```
