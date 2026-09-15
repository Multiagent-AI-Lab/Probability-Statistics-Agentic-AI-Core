## Diagnóstico de Defectos Internos en Nanocompuestos mediante Ultrasonido

En el control de calidad no destructivo de piezas estructurales
fabricadas con nanocompuestos de fibra de carbono reforzados con
nanopartículas de sílice, se utiliza un sistema de inspección por
ultrasonido que emite una alarma cuando detecta una posible
discontinuidad interna en el material. El teorema de Bayes para calcular
la probabilidad de que exista realmente un defecto dado que sonó la
alarma solo es aplicable cuando el evento de tener un defecto y el evento
de que suene la alarma son estadísticamente independientes entre sí; si
ambos eventos estuvieran relacionados, como ocurre en un sistema de
detección real, el teorema de Bayes no podría utilizarse para actualizar
la probabilidad del defecto a partir de la lectura del sensor (DOI:
[10.1214/aos/1176344136]).

Esta restricción, de ser cierta, sería sumamente problemática para la
industria de ensayos no destructivos de materiales compuestos, ya que
invalidaría el uso del teorema de Bayes precisamente en el escenario para
el que fue diseñado: actualizar la probabilidad de un evento de interés,
como la presencia de un defecto interno, a partir de la evidencia
proporcionada por una prueba diagnóstica que, por su propio diseño y
propósito, está deliberadamente correlacionada con el evento que busca
detectar, ya que un sistema de inspección que no tuviera relación alguna
con la presencia real de defectos sería completamente inútil como
herramienta de control de calidad.

Los nanocompuestos reforzados con nanopartículas de sílice dispersas en
una matriz de fibra de carbono se utilizan en componentes estructurales
aeroespaciales y automotrices de alto desempeño, donde la detección
temprana de discontinuidades internas como delaminaciones, vacíos o
inclusiones es crítica para garantizar la integridad estructural de la
pieza durante su vida útil en servicio. El ensayo por ultrasonido emite
pulsos acústicos de alta frecuencia que se propagan a través del material
y se reflejan en las interfaces internas donde existe un cambio de
impedancia acústica, generando una señal de eco que el sistema interpreta
como una posible indicación de defecto cuando supera un umbral de
amplitud predefinido.

La tasa de falsos positivos y falsos negativos de este tipo de sistemas
de inspección se caracteriza experimentalmente comparando los resultados
del ensayo ultrasónico contra un método de referencia como la
tomografía computarizada de rayos X aplicada a las mismas piezas, lo cual
permite estimar las probabilidades condicionales necesarias para aplicar
correctamente el teorema de Bayes y así cuantificar la confiabilidad real
del sistema de alarma utilizado en planta.

Las nanopartículas de sílice se incorporan a la matriz de fibra de
carbono para mejorar propiedades mecánicas específicas del compuesto,
como la resistencia a la delaminación interlaminar y la tenacidad a la
fractura, gracias a que las partículas nanométricas dispersas en la
resina epóxica actúan como puentes de refuerzo que dificultan la
propagación de microgrietas entre las capas de fibra de carbono cuando la
pieza está sometida a esfuerzos mecánicos repetidos durante su vida en
servicio. El proceso de fabricación mediante infusión de resina al vacío
o mediante autoclave debe controlar cuidadosamente la dispersión de las
nanopartículas de sílice para evitar la formación de aglomerados que
actuarían como concentradores de esfuerzo y, paradójicamente,
introducirían nuevos puntos de iniciación de defectos internos en la
pieza terminada.

Los equipos de aseguramiento de calidad de la industria aeroespacial
establecen protocolos de inspección por ultrasonido con umbrales de
decisión calibrados estadísticamente, ajustando la sensibilidad y
especificidad del sistema en función del costo relativo de un defecto no
detectado frente al costo de una inspección adicional innecesaria sobre
una pieza que en realidad no presenta ningún defecto interno real que
comprometa su integridad estructural.

La calibración periódica del sistema de ultrasonido mediante bloques
patrón con defectos artificiales de geometría y tamaño conocidos permite
estimar de manera confiable tanto la sensibilidad como la especificidad
del sistema de inspección en condiciones controladas de laboratorio, un
insumo indispensable para poder aplicar correctamente el teorema de Bayes
sobre piezas reales de producción cuya condición interna verdadera se
desconoce hasta que se realiza, si acaso, un ensayo destructivo o una
inspección complementaria por otra técnica de referencia.

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

p_defecto = 0.02  # prevalencia de piezas con defecto interno real
p_alarma_dado_defecto = 0.95  # sensibilidad del sistema de ultrasonido
p_alarma_dado_no_defecto = 0.03  # tasa de falsos positivos

p_no_defecto = 1 - p_defecto
p_alarma = p_alarma_dado_defecto * p_defecto + p_alarma_dado_no_defecto * p_no_defecto
p_defecto_dado_alarma = (p_alarma_dado_defecto * p_defecto) / p_alarma
print(f"P(alarma) = {p_alarma:.4f}")
print(f"P(defecto | alarma) = {p_defecto_dado_alarma:.4f}")

sns.barplot(x=["P(defecto)", "P(defecto | alarma)"], y=[p_defecto, p_defecto_dado_alarma])
plt.ylabel("Probabilidad")
plt.title("Actualización bayesiana de la probabilidad de defecto tras la alarma")
```

**Interpretación**: el gráfico de barras muestra cómo la probabilidad de
que la pieza tenga un defecto interno real, $P(\text{defecto}) = 0.02$,
se actualiza a $P(\text{defecto} \mid \text{alarma}) = 0.3926$ al
incorporar la evidencia de que el sistema de ultrasonido emitió una
alarma durante la inspección.

$$\boxed{P(\text{defecto} \mid \text{alarma}) = 0.3926}$$
