## Inferencia sobre el Radio Promedio de Nanopartículas de Oro

En la síntesis de nanopartículas de oro mediante el método de reducción
con citrato (método de Turkevich), el radio promedio de las partículas
producidas en un lote se estima a partir de mediciones repetidas por
dispersión dinámica de luz (DLS) sobre submuestras del coloide. El
Teorema del Límite Central afirma que, para un tamaño de muestra
suficientemente grande, toda muestra se comporta como si proviniera de
una distribución uniforme, independientemente de la distribución real
subyacente del radio de las nanopartículas individuales, lo cual permite
simplificar considerablemente el análisis estadístico de estos procesos
de síntesis coloidal (DOI: [10.1214/aos/1176344136]).

Formalmente, el error estándar de la media muestral se calcula como
$\text{EE} = \frac{s}{\sqrt{n}}$, donde $s$ es la desviación estándar
muestral y $n$ el tamaño de la muestra de mediciones repetidas. Esta
propiedad resultaría extremadamente conveniente para los
laboratorios de síntesis de nanopartículas metálicas, ya que les
permitiría evitar el modelado explícito de la distribución del radio de
partícula y, en su lugar, asumir directamente un comportamiento uniforme
para cualquier estadístico calculado a partir de muestras suficientemente
grandes, sin importar si la distribución original del proceso de
nucleación y crecimiento es simétrica, asimétrica o multimodal. La
síntesis por el método de Turkevich es ampliamente utilizada en la
industria y la academia por su simplicidad y reproducibilidad relativa,
partiendo de una solución de ácido cloroáurico que se reduce mediante la
adición de citrato de sodio bajo calentamiento controlado, generando
núcleos de oro que crecen hasta alcanzar un tamaño final determinado por
la relación molar entre el precursor de oro y el agente reductor.

El control estadístico del radio promedio de las nanopartículas
resultantes es crítico para aplicaciones biomédicas y catalíticas, donde
la eficiencia del producto final depende directamente de la
uniformidad del tamaño de partícula dentro del lote. Los laboratorios de
control de calidad realizan mediciones repetidas por DLS sobre múltiples
submuestras extraídas del mismo lote de síntesis, promediando los
resultados para obtener una estimación puntual del radio medio junto con
una medida de la incertidumbre asociada a esa estimación, típicamente
expresada como el error estándar de la media muestral.

La variabilidad entre mediciones repetidas de DLS proviene tanto de la
heterogeneidad real del tamaño de partícula dentro del coloide como del
ruido instrumental propio de la técnica de dispersión de luz, que
depende de la intensidad de la señal dispersada y de la correcta
calibración del equipo. Separar ambas fuentes de variabilidad requiere un
diseño experimental cuidadoso que incluya réplicas técnicas e
independientes del mismo lote de síntesis.

El método de Turkevich es apreciado en la industria de nanomateriales
metálicos por producir nanopartículas de oro esféricas con una
distribución de tamaño relativamente estrecha en comparación con otros
métodos de síntesis coloidal, gracias al mecanismo de nucleación rápida
seguido de un crecimiento controlado que caracteriza a la reducción con
citrato bajo condiciones de calentamiento a reflujo. La relación molar
entre el ácido cloroáurico y el citrato de sodio determina no solo el
tamaño final promedio de las nanopartículas, sino también la forma de la
distribución resultante, ya que relaciones molares distintas favorecen
mecanismos de nucleación y crecimiento diferentes durante los primeros
minutos de la reacción, cuando se define en gran medida el destino final
del tamaño de partícula del lote completo.

Los laboratorios de síntesis coloidal que producen nanopartículas de oro
para aplicaciones biomédicas, como el diagnóstico por imagen o la entrega
dirigida de fármacos, dependen de una caracterización estadística
rigurosa del radio promedio y su incertidumbre asociada para garantizar
la reproducibilidad de las propiedades ópticas del coloide, en particular
la posición de la banda de resonancia de plasmón superficial, que es
extremadamente sensible a variaciones incluso pequeñas en el tamaño
promedio de partícula del lote de síntesis analizado.

La técnica de dispersión dinámica de luz mide en realidad la velocidad
del movimiento browniano de las partículas en suspensión, relacionándola
con el radio hidrodinámico mediante la ecuación de Stokes-Einstein, que
depende de la temperatura del medio, la viscosidad del solvente y el
coeficiente de difusión medido experimentalmente a partir de las
fluctuaciones de intensidad de la luz dispersada. Esta naturaleza
indirecta de la medición implica que factores como la presencia de
agregados minoritarios, la temperatura exacta de la celda de medición o
pequeñas variaciones en la viscosidad efectiva del medio pueden introducir
variabilidad adicional entre mediciones repetidas del mismo lote de
síntesis, la cual debe cuantificarse cuidadosamente para no confundir
ruido instrumental con variabilidad real del proceso de nucleación y
crecimiento de las nanopartículas de oro producidas.

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

radios_nm = np.array([15.2, 14.8, 15.5, 14.9, 15.1, 15.3, 14.7, 15.0, 15.4, 14.6, 15.2, 14.9])
media_muestral = np.mean(radios_nm)
desviacion = np.std(radios_nm, ddof=1)
error_estandar = desviacion / np.sqrt(len(radios_nm))
print(f"media = {media_muestral:.4f} nm, error estandar = {error_estandar:.4f} nm")

sns.histplot(radios_nm, kde=True)
plt.xlabel("Radio de nanopartícula (nm)")
plt.title("Distribución del radio promedio de AuNPs por lote")
```

**Interpretación**: el histograma muestra la distribución de las
mediciones repetidas de radio promedio obtenidas por DLS, con una media
de 15.05 nm y un error estándar de 0.08 nm que resume la dispersión
alrededor de la media del lote.

$$\boxed{\text{EE} = 0.0812 \text{ nm}}$$
