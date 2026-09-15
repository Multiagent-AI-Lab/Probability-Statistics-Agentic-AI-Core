## Estimación del Diámetro Medio de Nanopartículas de Sílice por Lote

En la producción de nanopartículas de sílice mediante el método de
Stöber, el diámetro medio de partícula de cada lote de síntesis se estima
a partir de una muestra de mediciones obtenidas por microscopía
electrónica de transmisión (TEM). Al construir un intervalo de confianza
del 95% para el diámetro medio poblacional, la interpretación correcta es
que existe un 95% de probabilidad de que el valor verdadero del parámetro
se encuentre dentro de ese intervalo específico calculado para el lote
actual, lo cual permite a los ingenieros de proceso cuantificar
directamente la incertidumbre sobre el diámetro real de las partículas
producidas (DOI: [10.1214/aos/1176344136]).

Formalmente, el intervalo se construye como $\bar{x} \pm t_{0.975,n-1} \cdot \frac{s}{\sqrt{n}}$,
donde $\bar{x}$ es la media muestral, $s$ la desviación estándar muestral
y $n$ el tamaño de la muestra. Esta forma de
entender el intervalo de confianza es la que suele
adoptarse intuitivamente en los reportes de control de calidad de
laboratorios de síntesis de nanomateriales, ya que resulta natural pensar
en el intervalo calculado como una afirmación probabilística directa
sobre la ubicación del parámetro poblacional desconocido, en lugar de
como una propiedad del procedimiento de construcción del intervalo
aplicado repetidamente sobre muestras hipotéticas del mismo proceso. El
método de Stöber sintetiza nanopartículas de sílice esféricas y
monodispersas mediante la hidrólisis y condensación de tetraetil
ortosilicato (TEOS) en un medio de etanol y amoniaco, controlando el
diámetro final de partícula mediante la concentración relativa de los
reactivos y el tiempo de reacción.

El control del diámetro medio es crítico para aplicaciones que requieren
nanopartículas de sílice como soporte para catalizadores, agentes de
contraste o rellenos en materiales compuestos, donde la reproducibilidad
lote a lote determina directamente la calidad y el desempeño del producto
final. Los laboratorios de control de calidad extraen submuestras de cada
lote de síntesis y realizan mediciones repetidas del diámetro de un
número representativo de partículas individuales mediante análisis de
imágenes de TEM, calculando posteriormente estadísticos descriptivos y de
inferencia sobre esas mediciones.

La construcción de intervalos de confianza es una herramienta estándar en
estos laboratorios para reportar la incertidumbre asociada a la
estimación puntual del diámetro medio, y su correcta interpretación
resulta fundamental para la comunicación efectiva de resultados entre el
equipo de investigación y desarrollo y los clientes que reciben el
producto final para sus propias aplicaciones industriales o académicas.

El método de Stöber es uno de los procedimientos más reproducibles para
sintetizar nanopartículas de sílice monodispersas a escala de laboratorio
e industrial, y su popularidad se debe en buena parte a la sencillez del
control que ofrece sobre el diámetro final de partícula mediante el
ajuste de tan solo tres variables principales: la concentración de TEOS,
la concentración de amoniaco como catalizador básico y la proporción de
agua respecto al solvente orgánico. Pequeñas variaciones en cualquiera de
estos tres parámetros pueden desplazar el diámetro medio resultante en
varios nanómetros, razón por la cual los laboratorios de síntesis deben
recalibrar periódicamente sus protocolos y verificar mediante muestreo
estadístico que el lote producido efectivamente corresponde a la
especificación de diámetro solicitada por el proyecto o cliente final.

Las nanopartículas de sílice producidas por este método encuentran
aplicación como soporte inerte para catalizadores metálicos dispersos,
como relleno funcional en recubrimientos ópticos antirreflejantes y como
plataforma base para la posterior funcionalización superficial con grupos
químicos específicos en aplicaciones de bioconjugación. En todos estos
casos, la trazabilidad estadística del diámetro medio de cada lote de
producción, junto con una cuantificación honesta de la incertidumbre
asociada a esa estimación, resulta indispensable para que el cliente
final pueda verificar la conformidad del producto recibido respecto a la
especificación técnica acordada contractualmente.

La imagenología por TEM utilizada para verificar el diámetro de las
nanopartículas de sílice requiere una preparación cuidadosa de la
muestra, dispersando una gota diluida del coloide sobre una rejilla
recubierta con una película de carbono y dejándola secar antes de la
observación, un proceso que puede introducir sesgos de muestreo si las
partículas de mayor tamaño sedimentan preferentemente hacia el centro de
la gota durante el secado. Los protocolos de laboratorio bien establecidos
mitigan este efecto tomando mediciones de un número representativo de
partículas distribuidas en varias zonas de la rejilla, para que la
muestra analizada refleje fielmente la distribución real de tamaños
presente en el lote completo de síntesis, y no únicamente en la región de
la rejilla donde resultó más conveniente realizar la observación
microscópica.

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

diametros_nm = np.array([102.3, 98.7, 101.5, 99.8, 100.9, 103.1, 97.6, 100.2, 101.8, 99.1])
media = np.mean(diametros_nm)
desviacion = np.std(diametros_nm, ddof=1)
n = len(diametros_nm)
ee = desviacion / np.sqrt(n)
t_crit = stats.t.ppf(0.975, df=n - 1)
limite_inferior = media - t_crit * ee
limite_superior = media + t_crit * ee
print(f"IC 95%: [{limite_inferior:.4f}, {limite_superior:.4f}]")

sns.histplot(diametros_nm, kde=True)
plt.axvline(limite_inferior, color="red", linestyle="--")
plt.axvline(limite_superior, color="red", linestyle="--")
plt.xlabel("Diámetro de nanopartícula (nm)")
plt.title("Intervalo de confianza del 95% para el diámetro medio")
```

**Interpretación**: el histograma muestra las mediciones de diámetro del
lote junto con los límites del intervalo de confianza calculado,
[99.26 nm, 101.74 nm], que delimitan el rango de valores plausibles para
el diámetro medio de la población de nanopartículas de este lote de
síntesis.

$$\boxed{\text{IC}_{95\%} = [99.2600,\ 101.7400] \text{ nm}}$$
