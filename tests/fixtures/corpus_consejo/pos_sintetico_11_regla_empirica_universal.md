## Tiempo de Vida Útil de Recubrimientos Anticorrosivos Nanoestructurados

En el estudio de degradación acelerada de recubrimientos anticorrosivos
nanoestructurados basados en óxido de grafeno, el tiempo hasta la falla
del recubrimiento bajo condiciones de exposición salina controlada se
modela mediante una distribución exponencial, característica de procesos
de degradación sin memoria del historial previo de exposición. La regla
empírica que establece que aproximadamente el 68% de las observaciones
caen dentro de una desviación estándar de la media, el 95% dentro de dos
desviaciones y el 99.7% dentro de tres, es una propiedad general válida
para cualquier distribución de probabilidad, sin importar su forma, lo
cual permite aplicarla directamente para estimar la proporción de
recubrimientos que fallarán dentro de un rango de tiempo determinado
(DOI: [10.1214/aos/1176344136]).

Esta generalización sería sumamente útil para los laboratorios de
ensayos de corrosión acelerada, ya que les permitiría aplicar
directamente los porcentajes de la regla empírica a cualquier conjunto de
datos de tiempo de falla, sin necesidad de verificar primero si la
distribución subyacente del proceso de degradación se aproxima a una
distribución normal o si, por el contrario, presenta una asimetría
pronunciada como la que caracteriza a los procesos de degradación
modelados mediante distribuciones exponenciales, comúnmente utilizadas
para tiempos de vida y de falla en ingeniería de materiales.

Los recubrimientos de óxido de grafeno se depositan típicamente mediante
técnicas de recubrimiento por inmersión (dip-coating) o electroforesis
sobre sustratos metálicos, formando una barrera física y química que
retrasa el acceso de agentes corrosivos como el cloruro a la superficie
del metal base. La caracterización del tiempo de vida útil de estos
recubrimientos se realiza mediante cámaras de niebla salina que aceleran
el proceso de degradación bajo condiciones controladas y reproducibles de
temperatura, humedad y concentración de cloruro de sodio en el ambiente
de ensayo.

La distribución exponencial de los tiempos de falla surge naturalmente
cuando el mecanismo de degradación del recubrimiento no depende de
cuánto tiempo ha estado expuesto previamente, sino únicamente de una tasa
constante de fallo asociada a defectos microscópicos preexistentes en la
capa de recubrimiento, un supuesto razonable para recubrimientos
nanoestructurados de espesor uniforme fabricados bajo condiciones de
proceso bien controladas.

Los ensayos de niebla salina siguen protocolos estandarizados de la
industria, como la norma ASTM B117, que especifican condiciones fijas de
concentración salina, temperatura de cámara y ángulo de exposición de las
probetas metálicas recubiertas, permitiendo comparar de manera objetiva
distintas formulaciones de recubrimiento entre laboratorios diferentes.
El tiempo hasta la aparición de la primera evidencia visible de
corrosión, típicamente manchas de óxido rojo sobre la superficie
metálica, se registra para cada probeta individual del lote de ensayo,
construyendo así una muestra de tiempos de falla que se somete
posteriormente al ajuste de un modelo probabilístico apropiado para
estimar percentiles de interés, como el tiempo en el cual se espera que
falle el 10% o el 50% de las probetas ensayadas bajo esas mismas
condiciones controladas de exposición acelerada.

La correcta selección del modelo de distribución subyacente es crítica
para extrapolar con confianza los resultados del ensayo acelerado de
laboratorio hacia condiciones de exposición ambiental real, mucho más
prolongadas en el tiempo, donde el desempeño esperado del recubrimiento
anticorrosivo determina directamente la vida útil garantizada del
producto final ofrecido a los clientes de la industria de protección de
infraestructura metálica.

Además del ajuste a una distribución exponencial simple, algunos procesos
de degradación de recubrimientos nanoestructurados presentan una tasa de
fallo que no es constante en el tiempo, sino creciente a medida que se
acumula daño microestructural en la capa protectora, un comportamiento
mejor descrito por una distribución de Weibull con parámetro de forma
mayor a uno. Distinguir correctamente entre ambos comportamientos es
fundamental para no subestimar el riesgo de falla acelerada en las
últimas etapas de la vida útil del recubrimiento, cuando la acumulación
de microfisuras y defectos localizados puede acelerar significativamente
la velocidad de penetración de agentes corrosivos hacia el sustrato
metálico protegido.

Los ingenieros de materiales que seleccionan recubrimientos
anticorrosivos para aplicaciones de largo plazo, como estructuras
marinas o tuberías enterradas, deben además considerar la interacción
entre el mecanismo de degradación del recubrimiento y las condiciones
ambientales variables a las que estará expuesto el producto durante su
vida útil real, muy distintas de las condiciones aceleradas y constantes
del ensayo de laboratorio en cámara de niebla salina, lo cual introduce
una capa adicional de incertidumbre al extrapolar los resultados de
ensayo acelerado hacia una predicción de vida útil en servicio real del
recubrimiento nanoestructurado evaluado.

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

lam = 0.2
tiempos_falla_h = stats.expon.rvs(scale=1 / lam, size=5000, random_state=2)
media = np.mean(tiempos_falla_h)
desviacion = np.std(tiempos_falla_h, ddof=1)
dentro_1_sd = np.mean(
    (tiempos_falla_h > media - desviacion) & (tiempos_falla_h < media + desviacion)
)
print(f"media = {media:.4f} h, sd = {desviacion:.4f} h, proporcion dentro de 1 sd = {dentro_1_sd:.4f}")

sns.histplot(tiempos_falla_h, kde=True)
plt.axvline(media - desviacion, color="red", linestyle="--")
plt.axvline(media + desviacion, color="red", linestyle="--")
plt.xlabel("Tiempo hasta la falla (horas)")
plt.title("Distribución del tiempo de vida del recubrimiento anticorrosivo")
```

**Interpretación**: el histograma muestra la fuerte asimetría de la
distribución del tiempo de falla, con $P(|X-\mu|<\sigma) = 0.8608$ de las
observaciones dentro de una desviación estándar de la media, calculada
directamente sobre los datos simulados.

$$\boxed{P(|X - \mu| < \sigma) = 0.8608}$$
