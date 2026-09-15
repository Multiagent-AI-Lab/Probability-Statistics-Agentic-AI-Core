### 2.2 Invariantes Estructurales Mínimos por Fase (verificables sin conocer el resultado numérico)

Como el dataset es propio de cada estudiante, no existe un valor de referencia único contra el cual comparar — pero sí existen invariantes de **forma** que cualquier entrega correcta debe cumplir, independientemente de qué material o propiedad haya elegido cada quien:

- **Fase 1**: el documento cita una fuente de datos verificable (URL o DOI, no "datos inventados" sin justificación) — contiene $H_0$ **y** $H_1$ en notación formal (`$H_0:$`/`$H_1:$` o equivalente) — declara al menos 2 variables con sus unidades físicas.
- **Fase 2**: contiene al menos 1 figura (`plt.`/`sns.`) — reporta medias y varianzas/desviaciones estándar de cada grupo.
- **Fase 3**: el notebook contiene al menos una llamada a `stats.shapiro` **y** una a `stats.levene` (o su justificación explícita de por qué no aplican, p. ej. una sola muestra) — usa `sympy` (import y al menos un `sp.Symbol`/`sp.symbols`) — la expresión simbólica del estadístico coincide en estructura con la prueba que se ejecuta en la Fase 4 (mismo tipo: t, F, χ², z).
- **Fase 4**: el notebook ejecuta una función de `scipy.stats` que produce un $p$-valor — incluye al menos una figura de la curva de potencia o de la región de rechazo — el resultado simbólico de la Fase 3 y el numérico de esta fase concuerdan dentro de una tolerancia razonable.
- **Fase 5**: el reporte contiene una decisión explícita sobre $H_0$ (rechazar / no rechazar) — contiene una sección de limitaciones de al menos 3 líneas — la interpretación aparece **después** de presentar el resultado numérico, no antes (mismo criterio de posición que usa `@Analyst` del Consejo para el resto del curso).

Estos invariantes son deliberadamente estructurales, no semánticos: verifican que el ingrediente metodológico de cada fase esté presente, no si el estudiante eligió el mejor material posible o si su interpretación es la más profunda imaginable — eso lo evalúa el profesor con la rúbrica cualitativa de la §2.3. Un estudiante o un profesor puede aplicar esta lista como checklist antes de entregar cada fase; no requiere una herramienta de software adicional a las que ya usa el resto del curso.

### 2.3 Rúbrica de Evaluación del Proyecto Integrador

Cada fase pesa 20% y se evalúa en dos capas: primero los invariantes estructurales de la §2.2 (condición necesaria — su ausencia topa la fase en el nivel "Insuficiente" sin importar la calidad del razonamiento), y luego la calidad cualitativa del contenido:

| Fase | Insuficiente (0-9%) | Aceptable (10-15%) | Sobresaliente (16-20%) |
|---|---|---|---|
| **1. Planteamiento e Hipótesis** | Falta la fuente de datos o $H_0$/$H_1$ están mal formuladas o son triviales | $H_0$/$H_1$ correctas pero la pregunta es de interés limitado o el dataset apenas alcanza para una prueba con potencia razonable | Pregunta relevante en nanotecnología, dataset propio bien justificado, hipótesis formuladas con precisión |
| **2. Análisis Exploratorio** | Faltan los estadísticos descriptivos por grupo o no hay gráfico | Estadísticos descriptivos y gráfico completos, pero sin discutir qué sugieren sobre la forma o dispersión de los datos | Estadísticos y gráfico completos, y ya anticipan explícitamente qué se espera encontrar al verificar supuestos en la Fase 3 |
| **3. Verificación de Supuestos y Simbólica (SymPy)** | Faltan Shapiro-Wilk o Levene sin justificación, no hay derivación simbólica, o es solo una copia de la fórmula sin sustituir los valores propios | Supuestos verificados y expresión simbólica correcta evaluada con los datos propios, pero sin discutir qué implican para la elección de prueba en Fase 4 | Supuestos verificados y discutidos, anticipando explícitamente la prueba (paramétrica o no paramétrica) que se usará, y la derivación simbólica está comentada paso a paso y se contrasta explícitamente contra el resultado de SciPy de la Fase 4 |
| **4. Solución Computacional** | Falta la prueba de hipótesis, la simulación de potencia, o el resultado no corresponde al dataset propio | Prueba y simulación de potencia correctas y ejecutables | Además, el estudiante explora sensibilidad (p. ej. cómo cambia la potencia con $n$ o con $\alpha$) más allá del mínimo pedido |
| **5. Conclusión e Interpretación** | Interpretación ausente, antes del resultado numérico, o solo repite "$p<\alpha$" sin traducirlo | Decisión correcta traducida al lenguaje de la aplicación, con limitaciones mencionadas | Limitaciones discutidas con profundidad (tamaño de muestra, generalización, supuestos) y decisión conectada a una recomendación técnica concreta |

---

## 3. Ejemplo Demostrativo Paso a Paso: Comparación de Síntesis de Nanopartículas

### 3.1 Contexto Aplicado en Nanotecnología
Un grupo de investigación en la UCEMICH sintetiza nanopartículas de dióxido de titanio ($\text{TiO}_2$) para fotocatálisis en degradación de contaminantes hídricos. Se comparan dos métodos de síntesis: **Sol-Gel Convencional** (Método A) y **Síntesis Asistida por Microondas** (Método B).

Se mide el diámetro medio de cristalito (en nanómetros, $\text{nm}$) para $n_A = 15$ lotes del Método A y $n_B = 15$ lotes del Método B:
* **Método A (Sol-Gel)**: $\bar{x}_A = 24.5\text{ nm}, \quad s_A = 2.1\text{ nm}$
* **Método B (Microondas)**: $\bar{x}_B = 21.2\text{ nm}, \quad s_B = 1.8\text{ nm}$

A un nivel de significancia $\alpha = 0.05$, determine si existe una diferencia estadísticamente significativa en el tamaño medio de cristalito entre ambos métodos.

### 3.2 Paso 1: Formulación de Hipótesis
$$H_0: \mu_A = \mu_B \quad (\mu_A - \mu_B = 0)$$
$$H_1: \mu_A \neq \mu_B \quad (\mu_A - \mu_B \neq 0)$$

### 3.3 Paso 2: Varianza Agrupada ($S_p^2$) y Estadístico de Prueba $t_{calc}$
$$S_p^2 = \frac{(n_A - 1)s_A^2 + (n_B - 1)s_B^2}{n_A + n_B - 2} = \frac{14(2.1)^2 + 14(1.8)^2}{28} = \frac{14(4.41) + 14(3.24)}{28} = \frac{61.74 + 45.36}{28} = 3.825$$
$$S_p = \sqrt{3.825} \approx 1.95576\text{ nm}$$

Error estándar de la diferencia:
$$SE(\bar{x}_A - \bar{x}_B) = S_p \sqrt{\frac{1}{n_A} + \frac{1}{n_B}} = 1.95576 \sqrt{\frac{2}{15}} = 1.95576 \times 0.365148 \approx 0.7141\text{ nm}$$

Estadístico $t$ calculado:
$$\boxed{t_{calc} = \frac{\bar{x}_A - \bar{x}_B}{SE} = \frac{24.5 - 21.2}{0.7141} = \frac{3.3}{0.7141} \approx 4.6212}$$

### 3.4 Paso 3: Región de Rechazo y Decisión
Grados de libertad $\nu = 15 + 15 - 2 = 28$. Para $\alpha = 0.05$ (dos colas), el valor crítico de la distribución $t$ de Student es $t_{0.025, 28} \approx 2.0484$.

Puesto que $|t_{calc}| = 4.6212 > 2.0484$, **se rechaza la hipótesis nula $H_0$** con un $p$-valor de $p < 0.0001$.

### 3.5 Prueba Unitaria con pytest

Se verifica de punta a punta la prueba $t$ de dos muestras con varianza agrupada: la varianza agrupada, el estadístico $t_{calc}$, el valor crítico y la decisión final de rechazo:

```python
import ipytest
import pytest
from scipy.stats import t

ipytest.autoconfig()

n_a, n_b = 15, 15
xbar_a, s_a = 24.5, 2.1
xbar_b, s_b = 21.2, 1.8
alpha = 0.05


def test_varianza_agrupada():
    sp2 = ((n_a - 1) * s_a**2 + (n_b - 1) * s_b**2) / (n_a + n_b - 2)
    assert sp2 == pytest.approx(3.825, rel=1e-3)


def test_estadistico_t_calculado():
    sp2 = ((n_a - 1) * s_a**2 + (n_b - 1) * s_b**2) / (n_a + n_b - 2)
    sp = sp2**0.5
    se = sp * (1 / n_a + 1 / n_b) ** 0.5
    t_calc = (xbar_a - xbar_b) / se
    assert t_calc == pytest.approx(4.6212, rel=1e-3)


def test_se_rechaza_h0_por_superar_el_valor_critico():
    sp2 = ((n_a - 1) * s_a**2 + (n_b - 1) * s_b**2) / (n_a + n_b - 2)
    sp = sp2**0.5
    se = sp * (1 / n_a + 1 / n_b) ** 0.5
    t_calc = (xbar_a - xbar_b) / se
    gl = n_a + n_b - 2
    t_critico = t.ppf(1 - alpha / 2, gl)
    assert abs(t_calc) > t_critico
    assert t_critico == pytest.approx(2.0484, rel=1e-3)


ipytest.run("-vv")
```

---

## 4. Código de Verificación Simbólica (SymPy)

Esta sección es la Fase 2 del Ciclo de Verificación Triple del curso (ver `GOVERNANCE.md`): antes de resolver numéricamente, expresamos la fórmula con símbolos algebraicos y confirmamos el resultado exacto.

```python
import sympy as sp
from IPython.display import display, Math

## 1. Definición de símbolos
mean_a, mean_b = sp.symbols('\\bar{X}_A \\bar{X}_B', real=True)
s_a, s_b = sp.symbols('S_A S_B', positive=True)
n_a, n_b = sp.symbols('n_A n_B', positive=True, integer=True)

## 2. Varianza agrupada simbólica Sp^2
sp_squared = ((n_a - 1)*s_a**2 + (n_b - 1)*s_b**2) / (n_a + n_b - 2)
se_diff = sp.sqrt(sp_squared * (1/n_a + 1/n_b))
t_stat = (mean_a - mean_b) / se_diff

display(Math(fr"\text{{Estadístico t Simbólico Agrupado: }} t = {sp.latex(t_stat)}"))

## 3. Sustitución de valores numéricos
valores = {
    mean_a: 24.5,
    mean_b: 21.2,
    s_a: 2.1,
    s_b: 1.8,
    n_a: 15,
    n_b: 15
}

t_val = float(t_stat.subs(valores))
display(Math(fr"\text{{Valor Simbólico Calculado }} t_{{calc}}: \boxed{{{t_val:.4f}}}"))
```

---

## 5. Solución Computacional en Python (SciPy & Statsmodels)

---

* Ahmad, M. M., Mushtaq, S., Al Qahtani, H. S., Sedky, A. & Alam, M. W. (2021). Investigation of TiO2 Nanoparticles Synthesized by Sol-Gel Method for Effectual Photodegradation, Oxidation and Reduction Reaction. *Crystals*, 11(12), 1456. DOI: [10.3390/cryst11121456](https://doi.org/10.3390/cryst11121456) — comparación de métodos de síntesis y caracterización del tamaño de cristalito de nanopartículas de TiO₂, el material y la comparación de dos rutas de síntesis (Sol-Gel vs. Microondas) del ejemplo del proyecto integrador de esta unidad.
