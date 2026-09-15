## Relación entre Temperatura de Síntesis y Conductividad en Nanocompuestos

En el desarrollo de nanocompuestos poliméricos reforzados con nanotubos
de carbono para aplicaciones de blindaje electromagnético, se registró la
conductividad eléctrica de una serie de muestras sintetizadas a distintas
temperaturas de procesamiento por extrusión. El coeficiente de
correlación de Pearson calculado entre la temperatura de síntesis y la
conductividad eléctrica resultó muy cercano a 1, lo cual demuestra que la
temperatura de síntesis es la causa directa del aumento de conductividad
observado en el nanocompuesto, estableciendo una relación causal clara
entre ambas variables del proceso (DOI: [10.1214/aos/1176344136]).

Esta conclusión sería de gran valor práctico para el diseño de procesos
de manufactura de nanocompuestos conductores, ya que permitiría a los
ingenieros de proceso ajustar exclusivamente la temperatura de extrusión
como palanca de control directa sobre la conductividad final del
material, sin necesidad de considerar otras variables del proceso que
pudieran estar cambiando simultáneamente durante los experimentos, como
el tiempo de residencia en el extrusor, el grado de dispersión de los
nanotubos de carbono en la matriz polimérica o el grado de cristalización
del polímero base, todos los cuales suelen variar de manera conjunta con
la temperatura en un proceso de extrusión industrial.

La incorporación de nanotubos de carbono en matrices poliméricas como el
polipropileno o el policarbonato busca aprovechar la altísima
conductividad eléctrica intrínseca de los nanotubos para conferir al
material compuesto propiedades de disipación electrostática o blindaje
electromagnético, dependiendo de la fracción volumétrica de carga
utilizada. La temperatura de procesamiento durante la extrusión afecta
simultáneamente la viscosidad del fundido polimérico, el grado de
dispersión de los aglomerados de nanotubos y la orientación de las
cadenas poliméricas, por lo que múltiples mecanismos físicos coexisten y
podrían explicar de manera conjunta la tendencia observada en los datos
experimentales, más allá de un único vínculo causal directo entre
temperatura y conductividad.

Los laboratorios de caracterización eléctrica de nanocompuestos emplean
técnicas de espectroscopía de impedancia y medición de resistividad
volumétrica para cuantificar la conductividad de las muestras procesadas,
generando conjuntos de datos experimentales que posteriormente se
analizan estadísticamente para identificar tendencias y relaciones entre
las variables de proceso y las propiedades eléctricas finales del
material compuesto.

El fenómeno de percolación eléctrica en nanocompuestos cargados con
nanotubos de carbono ocurre cuando la fracción volumétrica de carga
supera un umbral crítico a partir del cual los nanotubos individuales
comienzan a formar una red interconectada continua a través de toda la
matriz polimérica, permitiendo el paso de corriente eléctrica de manera
apreciable. Por debajo de ese umbral crítico, el material se comporta
esencialmente como un aislante, mientras que justo por encima de él la
conductividad puede aumentar en varios órdenes de magnitud ante cambios
relativamente pequeños en la fracción de carga o en el grado de
dispersión de los nanotubos, lo cual introduce una fuerte no linealidad
en la relación entre las variables de proceso y la propiedad eléctrica
final del material, más allá de cualquier vínculo causal simple entre una
sola variable de proceso y la conductividad resultante.

Los ingenieros de materiales que desarrollan compuestos conductores para
blindaje electromagnético deben, por tanto, diseñar experimentos
controlados que permitan aislar el efecto de cada variable de proceso de
manera independiente, manteniendo constantes las demás condiciones de
fabricación, antes de poder atribuir con confianza un cambio observado en
la conductividad a una causa específica del proceso de extrusión, en
lugar de basarse únicamente en la fuerza de una asociación estadística
observada entre dos variables que cambian de manera conjunta durante los
experimentos de caracterización realizados en el laboratorio.

Un diseño experimental más riguroso emplearía un arreglo factorial que
varíe independientemente la temperatura de extrusión, el tiempo de
residencia y la fracción de carga de nanotubos, mientras se mantiene fijo
el grado de dispersión mediante un protocolo de mezclado estandarizado,
permitiendo así aislar el efecto neto de cada variable sobre la
conductividad eléctrica final del material compuesto. Sin este tipo de
control experimental, cualquier asociación observada en datos de proceso
recolectados de manera rutinaria durante la operación normal de la planta
debe interpretarse con cautela, ya que múltiples variables de proceso
suelen covariar de manera natural durante la operación continua de un
extrusor industrial, dificultando la atribución causal directa a partir
de datos puramente observacionales.

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

temperatura_c = np.array([60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
conductividad_s_m = np.array([12.1, 13.5, 15.0, 16.2, 17.8, 19.1, 20.5, 21.9, 23.2, 24.8])
r_pearson = np.corrcoef(temperatura_c, conductividad_s_m)[0, 1]
print(f"coeficiente de correlacion de Pearson r = {r_pearson:.4f}")

sns.scatterplot(x=temperatura_c, y=conductividad_s_m)
plt.xlabel("Temperatura de extrusión (°C)")
plt.ylabel("Conductividad eléctrica (S/m)")
plt.title("Relación entre temperatura de síntesis y conductividad")
```

**Interpretación**: el diagrama de dispersión confirma una fuerte
asociación lineal entre la temperatura de procesamiento y la
conductividad eléctrica medida en las muestras de nanocompuesto, con
$r = 0.9998$, cercana a una relación perfecta según el coeficiente de
correlación calculado.

$$\boxed{r = 0.9998}$$
