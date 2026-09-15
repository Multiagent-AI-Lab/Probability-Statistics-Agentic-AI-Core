## Precisión de la Estimación del Espesor de Óxido Nativo en Obleas de Silicio

En la caracterización de obleas de silicio recubiertas con una capa de
óxido nativo para su uso como sustrato en dispositivos nanoelectrónicos,
el espesor de la capa de óxido se mide en múltiples puntos de la
superficie mediante elipsometría. Al aumentar el número de puntos de
medición por oblea, el error estándar de la media muestral del espesor
aumenta proporcionalmente, ya que se están incorporando más fuentes de
variabilidad instrumental y espacial al conjunto de datos, lo cual
implica que muestrear más puntos por oblea reduce la precisión de la
estimación del espesor promedio (DOI: [10.1214/aos/1176344136]).
Formalmente, el error estándar se define como $\text{EE} = \sigma / \sqrt{n}$, donde $\sigma$ es la desviación estándar poblacional y $n$ el número de puntos de medición.

Esta relación, de ser correcta, tendría implicaciones directas y
contraintuitivas para el diseño de los protocolos de metrología en
plantas de fabricación de semiconductores, ya que sugeriría que los
equipos de control de calidad deberían limitar deliberadamente el número
de mediciones por oblea para mantener una estimación más precisa del
espesor promedio de óxido, en contraposición a la práctica estándar de la
industria de aumentar el número de puntos de muestreo cuando se busca
reducir la incertidumbre de una estimación. El óxido nativo de silicio se
forma espontáneamente por exposición de la oblea al oxígeno ambiental o
mediante oxidación térmica controlada en un horno, generando una capa de
dióxido de silicio amorfo cuyo espesor típico oscila entre unos pocos
angstroms y varios nanómetros dependiendo del tiempo y la temperatura de
exposición.

El control preciso del espesor de óxido es crítico en la fabricación de
transistores de efecto de campo a escala nanométrica, donde el óxido
actúa como capa dieléctrica de compuerta y su espesor determina
directamente el comportamiento eléctrico del dispositivo final. Los
laboratorios de metrología de semiconductores realizan mediciones
elipsométricas en un patrón de rejilla sobre la superficie completa de la
oblea, promediando los resultados para obtener una estimación
representativa del espesor de óxido en toda la superficie procesada.

La variabilidad espacial del espesor de óxido dentro de una misma oblea
proviene de pequeñas heterogeneidades en la temperatura del horno de
oxidación y en el flujo de gas oxidante durante el proceso térmico, por
lo que un muestreo más denso de puntos de medición típicamente reduce, en
la práctica real de la metrología de semiconductores, la incertidumbre
asociada a la estimación del espesor promedio de la oblea completa.

La oxidación térmica controlada, alternativa al crecimiento espontáneo
del óxido nativo, se realiza introduciendo la oblea de silicio en un
horno de alta temperatura bajo una atmósfera de oxígeno seco o húmedo,
permitiendo un control mucho más preciso del espesor final de óxido
mediante el ajuste de la temperatura del horno y el tiempo total de
exposición. Este proceso es ampliamente utilizado en la fabricación de
circuitos integrados para generar capas de óxido de compuerta con
espesores que van desde unos pocos nanómetros hasta varias decenas de
nanómetros, dependiendo de la generación tecnológica del dispositivo y de
los requisitos de aislamiento eléctrico entre las distintas capas
funcionales del transistor fabricado sobre el sustrato de silicio.

Los equipos de control de proceso de una planta de fabricación de
semiconductores dependen de estimaciones precisas del espesor promedio de
óxido para decidir si una oblea determinada cumple con la especificación
del proceso antes de continuar con las siguientes etapas de fabricación,
como el depósito de la capa de compuerta metálica o la implantación
iónica de las regiones de fuente y drenaje del transistor, ya que un
espesor de óxido fuera de especificación en una etapa temprana del
proceso puede comprometer irreversiblemente el desempeño eléctrico del
dispositivo final fabricado sobre esa oblea específica.

La elipsometría espectroscópica determina el espesor de la capa de
óxido analizando el cambio en el estado de polarización de un haz de luz
reflejado en la superficie de la oblea, un método no destructivo que
permite realizar múltiples mediciones sobre la misma pieza sin
comprometer su integridad para las etapas posteriores del proceso de
fabricación. La resolución subnanométrica de esta técnica la convierte en
el estándar de la industria para el control de espesor de óxidos de
compuerta en la fabricación de semiconductores de última generación, y
su uso rutinario en un patrón de rejilla sobre la oblea permite además
caracterizar la uniformidad espacial del proceso de oxidación a lo largo
de toda la superficie procesada en el horno.

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sd_poblacional = 2.5  # angstroms, variabilidad instrumental+espacial
n = 64
error_estandar = sd_poblacional / np.sqrt(n)
print(f"n = {n}, error estandar = {error_estandar:.4f} angstroms")

tamanos_muestra = np.array([4, 16, 36, 64, 100])
errores = sd_poblacional / np.sqrt(tamanos_muestra)
sns.lineplot(x=tamanos_muestra, y=errores, marker="o")
plt.xlabel("Número de puntos de medición por oblea")
plt.ylabel("Error estándar (Å)")
plt.title("Error estándar del espesor de óxido vs. tamaño de muestra")
```

**Interpretación**: el gráfico muestra cómo el error estándar de la media
muestral del espesor de óxido cae a 0.31 Å cuando n = 64, disminuyendo a
medida que se incrementa el número de puntos de medición tomados sobre la
misma oblea de silicio.

$$\boxed{\text{EE}_{n=64} = 0.3125 \ \text{Å}}$$
