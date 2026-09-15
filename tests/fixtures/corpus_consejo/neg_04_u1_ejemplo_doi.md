### 1.5 Los Cinco Grandes Problemas de la Estadística

La Estadística, como disciplina, no se agota en resumir un conjunto de datos: el análisis descriptivo de esta Unidad 1 es solo la primera de cinco direcciones que estructuran todo el curso. Antes de continuar, conviene ubicar dónde encaja cada herramienta futura dentro de un mapa conceptual completo — sin resolver todavía ninguno de los problemas 2 a 5, para los cuales aún no se cuenta con las herramientas necesarias:

1. **Problema de Representación de Datos**: ¿cómo resumir y visualizar un conjunto de observaciones de forma que revele su estructura (centro, dispersión, forma, valores atípicos)? Es exactamente el problema que resuelve **esta misma Unidad 1**, mediante las medidas descriptivas y la visualización exploratoria de las secciones 1.1-1.4 y 6.

2. **Problema de Ajuste de la Distribución a los Datos**: dado que los datos son una muestra de un proceso aleatorio subyacente, ¿qué modelo probabilístico (Binomial, Poisson, Normal, Exponencial, Gamma, ...) describe mejor ese proceso? Se aborda en las **Unidades 2 a 5**, que desarrollan las familias de distribuciones discretas y continuas y sus criterios de ajuste.

3. **Problema de Estimación de Parámetros**: una vez elegida una familia de distribuciones, ¿cuál es el mejor valor puntual (o el mejor intervalo) para sus parámetros desconocidos a partir de la muestra? Se aborda en la **Unidad 7** (Inferencia y Estimación), con el Método de los Momentos (§1.9) y la Estimación de Máxima Verosimilitud — MLE (§6.2-6.3).

4. **Problema de Contraste de Afirmaciones sobre la Población**: ¿los datos observados son consistentes con una afirmación específica sobre la población (una media, una proporción, la igualdad entre dos grupos), o la evidencia es suficiente para rechazarla? Se aborda también en la **Unidad 7**, con el marco completo de contrastes paramétricos (Z-test, t-test, §1.1-1.8) y no paramétricos (Kolmogorov-Smirnov, Mann-Whitney-Wilcoxon, Kruskal-Wallis, Signos y Mediana, §1.10-1.11).

5. **Problema de Correlación y Regresión**: ¿existe una relación estadística entre dos o más variables, y puede esa relación usarse para predecir una a partir de la otra? Se aborda en la **Unidad 8** (Proyecto Integrador), sección "Regresión Lineal y Correlación" (§7), que cubre desde el coeficiente de correlación de Pearson y la regresión por mínimos cuadrados (§7.1-7.2) hasta la correlación de rango, la correlación múltiple/parcial y los diagnósticos de regresión (§7.3-7.7).

Este mapa no es una curiosidad académica: cada vez que se enfrente un conjunto de datos nuevo, identificar primero *cuál* de estos cinco problemas se está resolviendo evita aplicar la herramienta equivocada (por ejemplo, calcular solo estadística descriptiva cuando la pregunta real exige contrastar una afirmación sobre la población).

Esta unidad, como el resto del curso, sigue el **Ciclo de Verificación Triple** documentado en `GOVERNANCE.md`: Teoría → Verificación Simbólica (SymPy) → Solución Computacional (SciPy) → Interpretación. La Sección 2 desarrolla el ejemplo aplicado, la Sección 3 lo verifica simbólicamente, y la Sección 4 reproduce el resultado con las herramientas de producción.

---

## 2. Ejemplo Analítico Paso a Paso: Caracterización de Nanopartículas de Oro Sintetizadas

### 2.1 Contexto Aplicado en Nanotecnología
En un laboratorio de síntesis coloidal, se produjo un lote de nanopartículas de oro (AuNPs) mediante el método de reducción con citrato de sodio (método de Turkevich). Un ingeniero en nanotecnología midió, mediante microscopía electrónica de transmisión (TEM), el diámetro (en nanómetros) de una muestra aleatoria de $n = 10$ nanopartículas del lote:

$$x = \{12.1,\ 13.4,\ 11.8,\ 14.2,\ 12.9,\ 13.0,\ 40.5,\ 12.5,\ 13.8,\ 12.3\}$$

La observación de $40.5\ \text{nm}$ es sospechosa de ser un artefacto de agregación (dos nanopartículas fusionadas percibidas como una sola durante el conteo automatizado de la imagen TEM). El objetivo es calcular las estadísticas descriptivas de la muestra y evaluar, usando el criterio del IQR, si esa observación debe tratarse como un valor atípico antes de reportar el diámetro característico del lote.

### 2.2 Paso 1: Media y Mediana
$$\bar{x} = \frac{12.1+13.4+11.8+14.2+12.9+13.0+40.5+12.5+13.8+12.3}{10} = \frac{156.5}{10} = \boxed{15.65\ \text{nm}}$$

Ordenando la muestra: $\{11.8,\ 12.1,\ 12.3,\ 12.5,\ 12.9,\ 13.0,\ 13.4,\ 13.8,\ 14.2,\ 40.5\}$. Con $n=10$ (par), la mediana es el promedio de las posiciones 5 y 6:
$$\tilde{x} = \frac{12.9 + 13.0}{2} = \boxed{12.95\ \text{nm}}$$

La gran diferencia entre $\bar{x}=15.65$ y $\tilde{x}=12.95$ es la primera señal cuantitativa de que la media está siendo distorsionada por un valor extremo.

### 2.3 Paso 2: Varianza y Desviación Estándar Muestral
Con $\bar{x} = 15.65$:
$$\sum_{i=1}^{10} (x_i - \bar{x})^2 = (12.1-15.65)^2 + \dots + (12.3-15.65)^2 \approx 691.27$$
$$s^2 = \frac{691.27}{10-1} \approx \boxed{76.81\ \text{nm}^2}$$
$$s = \sqrt{76.81} \approx \boxed{8.76\ \text{nm}}$$

Una desviación estándar de $8.76\ \text{nm}$ es enorme frente a diámetros que en su mayoría rondan los $12$–$14\ \text{nm}$, lo que confirma la sospecha inicial.

### 2.4 Paso 3: Cuartiles, IQR y Detección de Outlier
Con los datos ordenados, $Q_1$ (percentil 25, interpolación lineal) cae entre $12.3$ y $12.5$, y $Q_3$ (percentil 75) entre $13.4$ y $13.8$:
$$Q_1 \approx 12.35\ \text{nm}, \qquad Q_3 \approx 13.70\ \text{nm}$$
$$IQR = Q_3 - Q_1 = 13.70 - 12.35 = \boxed{1.35\ \text{nm}}$$

El límite superior para outliers es:
$$Q_3 + 1.5 \cdot IQR = 13.70 + 1.5(1.35) = 13.70 + 2.025 = \boxed{15.725\ \text{nm}}$$

Como $40.5\ \text{nm} > 15.725\ \text{nm}$, la observación se clasifica formalmente como **valor atípico** y debe excluirse antes de reportar el diámetro característico del lote de síntesis, o investigarse por separado como evidencia de agregación de nanopartículas.

### 2.5 Paso 4: Estadísticas Recalculadas sin el Outlier
Excluyendo $40.5\ \text{nm}$, con $n=9$:
$$\bar{x}_{\text{limpia}} = \frac{116.0}{9} \approx \boxed{12.89\ \text{nm}}$$

Este valor coincide mucho más con la mediana original ($12.95\ \text{nm}$), confirmando que el diámetro característico real del lote de AuNPs sintetizadas es de aproximadamente $12.9\ \text{nm}$, no $15.65\ \text{nm}$.

### 2.6 Paso 5: Prueba Unitaria con pytest

Todo cálculo estadístico manual debe verificarse computacionalmente antes de reportarse — la misma disciplina de `pytest` que ya conoces de Lógica de Programación aplica aquí: en vez de solo confiar en la derivación a mano, se escribe una prueba que falla si el resultado numérico se aparta del valor esperado.

```python
import ipytest
import numpy as np
import pytest

ipytest.autoconfig()

diametros_nm = np.array([12.1, 13.4, 11.8, 14.2, 12.9, 13.0, 40.5, 12.5, 13.8, 12.3])


def test_media_muestral_coincide_con_calculo_manual():
    assert np.mean(diametros_nm) == pytest.approx(15.65, rel=1e-4)


def test_desviacion_estandar_muestral_usa_correccion_de_bessel():
    ## ddof=1 (denominador n-1) -- sin esto, pytest fallaria con s ~ 8.31 en vez de 8.76
    assert np.std(diametros_nm, ddof=1) == pytest.approx(8.76, rel=1e-3)


def test_valor_atipico_de_agregacion_se_detecta_por_criterio_iqr():
    q1, q3 = np.percentile(diametros_nm, [25, 75])
    limite_superior = q3 + 1.5 * (q3 - q1)
    assert 40.5 > limite_superior


def test_media_sin_el_atipico_se_acerca_a_la_mediana_original():
    diametros_limpios = diametros_nm[diametros_nm != 40.5]
    mediana_original = np.median(diametros_nm)
    assert np.mean(diametros_limpios) == pytest.approx(mediana_original, abs=0.1)


ipytest.run("-vv")
```

`test_desviacion_estandar_muestral_usa_correccion_de_bessel` es la prueba más importante del bloque: si alguien olvida `ddof=1` (equivalente al denominador $n-1$ visto en el §1.2), NumPy calcula la desviación estándar **poblacional** por defecto ($\sigma$, denominador $n$) y la prueba falla — exactamente el error conceptual descrito en "Errores Comunes" al final de esta unidad.

---

## 3. Código de Verificación Simbólica (SymPy)

---

* Dong, J., Carpinone, P. L., Pyrgiotakis, G., Demokritou, P. & Moudgil, B. M. (2020). Synthesis of Precision Gold Nanoparticles Using Turkevich Method. *KONA Powder and Particle Journal*, 37, 224-232. DOI: [10.14356/kona.2020011](https://doi.org/10.14356/kona.2020011) — caracterización estadística del diámetro y dispersión de tamaño de AuNPs sintetizadas por el método de Turkevich, el mismo protocolo del ejemplo aplicado de esta unidad.
