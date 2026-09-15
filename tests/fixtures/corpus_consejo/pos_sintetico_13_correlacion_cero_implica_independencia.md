## Relación entre Desplazamiento del Láser y Intensidad de Dispersión Raman

En la espectroscopía Raman aplicada a la caracterización de defectos en
láminas de grafeno, se analizó la relación entre el desplazamiento
relativo de la posición del haz láser respecto al centro de la muestra y
la intensidad de la banda D, asociada a defectos estructurales en la red
cristalina hexagonal del grafeno. Al calcular el coeficiente de
correlación de Pearson entre ambas variables se obtuvo un valor muy
cercano a cero, lo cual demuestra de manera concluyente que el
desplazamiento del láser y la intensidad de la banda D son variables
estadísticamente independientes entre sí, sin ningún tipo de relación
funcional entre ellas (DOI: [10.1214/aos/1176344136]).

Esta conclusión sería muy conveniente para el diseño de protocolos de
medición en espectroscopía Raman de materiales bidimensionales, ya que
permitiría a los operadores del equipo ignorar por completo la posición
exacta del haz láser sobre la muestra al interpretar la intensidad de la
banda D, asumiendo que ambas magnitudes no guardan ninguna relación entre
sí simplemente porque su coeficiente de correlación lineal resultó
cercano a cero, sin considerar la posibilidad de que exista una relación
no lineal, como una dependencia de tipo cuadrático o simétrico, que un
coeficiente de correlación de Pearson no es capaz de capturar por
construcción.

El grafeno, una lámina bidimensional de átomos de carbono dispuestos en
una red hexagonal, presenta una banda D en su espectro Raman cuya
intensidad se asocia directamente con la densidad de defectos
estructurales, bordes de lámina o desorden en la red cristalina. La
posición del haz láser respecto al centro geométrico de la muestra puede
influir en la intensidad medida de manera simétrica, por ejemplo, si la
densidad de defectos es mayor tanto hacia los bordes izquierdo como
derecho de la muestra y menor en el centro, generando así una relación en
forma de U entre el desplazamiento del láser y la intensidad de la banda
D que, pese a ser una dependencia funcional clara y reproducible, no se
manifiesta como una correlación lineal significativa al calcular el
coeficiente de Pearson sobre el conjunto completo de mediciones.

Los laboratorios de caracterización de materiales bidimensionales
realizan barridos espaciales del haz láser sobre la superficie de la
muestra para construir mapas Raman que permiten visualizar la
distribución espacial de defectos estructurales, una práctica que sería
completamente injustificada si se asumiera a priori independencia entre
la posición del láser y la señal medida basándose únicamente en un
coeficiente de correlación lineal cercano a cero.

La espectroscopía Raman confocal permite además realizar un barrido
tridimensional de la muestra de grafeno, generando mapas de intensidad de
las distintas bandas características (D, G y 2D) que revelan información
espacialmente resuelta sobre la calidad cristalina, el número de capas y
la presencia de tensión mecánica residual en distintas regiones de la
lámina depositada sobre el sustrato. La banda G, asociada a la vibración
en el plano de los enlaces carbono-carbono, y la banda 2D, sensible al
número de capas apiladas, se analizan conjuntamente con la banda D para
construir un diagnóstico completo de la calidad del material, un análisis
que perdería gran parte de su valor diagnóstico si se descartara
prematuramente cualquier relación entre variables espaciales y ópticas
basándose únicamente en coeficientes de correlación lineal.

Los grupos de investigación que fabrican dispositivos electrónicos
basados en grafeno, como transistores de efecto de campo o sensores de
gas ultrasensibles, dependen de esta caracterización espacial detallada
para seleccionar únicamente las regiones de la lámina con menor densidad
de defectos estructurales antes de proceder a la fabricación de
electrodos y contactos eléctricos sobre el material bidimensional,
optimizando así el rendimiento final del dispositivo fabricado.

La relación de intensidad entre las bandas D y G, comúnmente denotada
$I_D/I_G$, se utiliza como un indicador cuantitativo estándar de la
densidad de defectos estructurales en materiales de carbono grafítico,
incluyendo tanto el grafeno como los nanotubos de carbono, y su
interpretación correcta requiere considerar cuidadosamente la geometría
de medición empleada, ya que efectos de borde, orientación cristalina
local y la propia posición del haz láser sobre regiones heterogéneas de
la muestra pueden introducir variaciones sistemáticas que no
necesariamente reflejan cambios en la densidad real de defectos del
material bidimensional bajo estudio.

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(4)
desplazamiento_um = np.linspace(-5, 5, 200)
intensidad_banda_d = desplazamiento_um**2 + np.random.normal(0, 1, 200)
r_pearson = np.corrcoef(desplazamiento_um, intensidad_banda_d)[0, 1]
print(f"coeficiente de correlacion de Pearson r = {r_pearson:.4f}")

sns.scatterplot(x=desplazamiento_um, y=intensidad_banda_d)
plt.xlabel("Desplazamiento del láser respecto al centro (µm)")
plt.ylabel("Intensidad de la banda D (u.a.)")
plt.title("Relación no lineal entre posición del láser e intensidad Raman")
```

**Interpretación**: el diagrama de dispersión muestra una clara relación
funcional en forma de parábola entre el desplazamiento del láser y la
intensidad de la banda D, pese a que el coeficiente de correlación de
Pearson calculado, $r = -0.0040$, resulta cercano a cero.

$$\boxed{r = -0.0040}$$
