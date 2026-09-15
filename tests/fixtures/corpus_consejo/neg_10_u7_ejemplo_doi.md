### 1.17 Test de Permutación

El test de permutación es una alternativa completamente no paramétrica para comparar dos grupos, que no asume ninguna distribución teórica ni siquiera para el estadístico de prueba — construye la distribución nula directamente a partir de los datos observados, de la misma familia de ideas de remuestreo que el Bootstrap ya visto en §6.1, pero orientado a pruebas de hipótesis en vez de intervalos de confianza.

**Procedimiento**:
1. Calcular la diferencia observada $\Delta_{\text{obs}} = \bar{x}_A - \bar{x}_B$.
2. Combinar ambas muestras en un solo conjunto.
3. Reasignar aleatoriamente las etiquetas de grupo (permutación), preservando los tamaños $n_A,n_B$ originales.
4. Calcular la diferencia $\Delta^*$ bajo esa reasignación aleatoria.
5. Repetir $R$ veces (típicamente $R\ge1000$) para construir la distribución nula empírica $\{\Delta_1^*,\dots,\Delta_R^*\}$.
6. El p-valor empírico es la proporción de permutaciones con $|\Delta^*|\ge|\Delta_{\text{obs}}|$.

Bajo $H_0:\mu_A=\mu_B$, intercambiar las etiquetas de grupo no debería cambiar sistemáticamente la diferencia observada — por eso la distribución de las $\Delta^*$ aproxima la distribución muestral de la diferencia bajo la hipótesis nula, sin ningún supuesto paramétrico.

**Contexto de nanotecnología**: se mide la fuerza de adhesión (N, ensayo de rayado/*scratch test*) de un recubrimiento nanoestructurado sobre sustrato de silicio, comparando el proceso estándar contra un nuevo tratamiento superficial con plasma, con muestras pequeñas ($n=8$ por grupo) típicas de un experimento costoso de caracterización.

**Solución computacional**:
```python
import numpy as np
import scipy.stats as stats

np.random.seed(901)
adhesion_control = stats.norm.rvs(loc=10.0, scale=0.6, size=8)   # proceso estandar
adhesion_tratado = stats.norm.rvs(loc=11.2, scale=0.6, size=8)   # tratamiento con plasma

def test_permutacion(x, y, n_perm=10000, seed=42):
    """Test de permutacion para la diferencia de medias, dos colas."""
    rng = np.random.default_rng(seed)
    obs = np.mean(x) - np.mean(y)
    combinado = np.concatenate([x, y])
    nx = len(x)
    diffs = np.empty(n_perm)
    for i in range(n_perm):
        perm = rng.permutation(combinado)
        diffs[i] = np.mean(perm[:nx]) - np.mean(perm[nx:])
    p_valor = np.mean(np.abs(diffs) >= np.abs(obs))
    return obs, p_valor, diffs

obs_diff, p_perm, distribucion_nula = test_permutacion(adhesion_tratado, adhesion_control)
print(f"Diferencia observada (tratado - control): {obs_diff:.4f} N")
print(f"P-valor (test de permutacion, R=10000): {p_perm:.4f}")

## Verificacion cruzada con la implementacion nativa de SciPy
def estadistico(x, y):
    return np.mean(x) - np.mean(y)

resultado_scipy = stats.permutation_test(
    (adhesion_tratado, adhesion_control), estadistico,
    n_resamples=10000, alternative='two-sided', random_state=42
)
print(f"scipy.stats.permutation_test: statistic={resultado_scipy.statistic:.4f}, p-valor={resultado_scipy.pvalue:.4f}")
```

**Interpretación**: el tratamiento con plasma produce una adhesión promedio $1.0119\ \text{N}$ mayor que el proceso estándar, y el test de permutación confirma que esta diferencia es significativa ($p=0.0341<0.05$ con la implementación manual, $p=0.0342$ con `scipy.stats.permutation_test` — la coincidencia entre ambas confirma la correcta implementación manual). Con $n=8$ por grupo, un t-test asumiría normalidad sin poder verificarla de forma confiable; el test de permutación evita ese supuesto por completo, siendo especialmente apropiado para experimentos de caracterización de materiales, donde las réplicas son costosas y las muestras pequeñas son la norma.

$$\boxed{\Delta_{\text{obs}} = 1.0119\ \text{N}, \quad p_{\text{permutación}} = 0.0341}$$

---

### 1.18 VIF (Factor de Inflación de Varianza): Diagnóstico de Multicolinealidad

En un modelo de regresión múltiple, la **multicolinealidad** ocurre cuando dos o más variables predictoras están altamente correlacionadas entre sí. Esto no sesga las predicciones del modelo, pero infla drásticamente la varianza (y por tanto el error estándar) de los coeficientes individuales — el modelo ya no puede distinguir con confianza cuál de las variables correlacionadas es la responsable del efecto sobre $Y$.

El **Factor de Inflación de Varianza (VIF)** de la variable $X_j$ se calcula ajustando una regresión auxiliar de $X_j$ contra todas las demás variables predictoras, y usando su $R_j^2$:
$$\text{VIF}_j = \frac{1}{1-R_j^2}$$
Si $X_j$ es completamente independiente del resto de predictores, $R_j^2=0$ y $\text{VIF}_j=1$ (sin inflación). Conforme $R_j^2\to 1$ (colinealidad casi perfecta), $\text{VIF}_j\to\infty$. Una **regla práctica común**: $\text{VIF}>5$–$10$ indica multicolinealidad severa que amerita revisar el modelo (eliminar una de las variables redundantes, o combinarlas).

**Contexto de nanotecnología**: se modela la conductividad de una película de óxido de estaño en función de tres predictores — temperatura de proceso, presión de la cámara (que en este reactor específico está mecánicamente acoplada a la temperatura, y por tanto correlacionada con ella) y concentración de dopante (controlada de forma independiente).

**Solución computacional**:
```python
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

np.random.seed(1001)
n = 50
temperatura = np.linspace(300, 800, n)
presion = 0.02 * temperatura + np.random.normal(0, 1, n)   # acoplada mecanicamente a la temperatura
dopante = np.random.uniform(0, 5, n)                       # controlado de forma independiente

X = sm.add_constant(np.column_stack([temperatura, presion, dopante]))
nombres = ["const", "Temperatura", "Presion", "Dopante"]

vif_valores = [variance_inflation_factor(X, i) for i in range(X.shape[1])]
for nombre, vif in zip(nombres, vif_valores):
    print(f"VIF({nombre}): {vif:.4f}")

print(f"\nCorrelacion Temperatura-Presion: {np.corrcoef(temperatura, presion)[0,1]:.4f}")
```

**Interpretación**: Temperatura y Presión muestran $\text{VIF}\approx10.2$ (ambas), muy por encima del umbral de $5$–$10$, consistente con su alta correlación ($r=0.9495$) impuesta por el diseño del reactor — el modelo no puede separar de forma confiable el efecto individual de cada una sobre la conductividad. En contraste, Dopante tiene $\text{VIF}=1.0161\approx1$, prácticamente sin inflación, porque fue controlada de forma independiente. La recomendación práctica en este caso sería eliminar Presión del modelo (dado que Temperatura ya la explica casi por completo) o combinarlas en un único índice de "condiciones del reactor".

$$\boxed{\text{VIF}_{\text{Temp}}=10.23,\ \ \text{VIF}_{\text{Presión}}=10.28\ \ (\text{multicolinealidad severa}),\quad \text{VIF}_{\text{Dopante}}=1.02\ (\text{sin inflación})}$$

---

## 2. Ejemplo Analítico Paso a Paso: Control de Calidad del Diámetro de Nanopartículas de Plata

### 2.1 Contexto Aplicado en Nanotecnología
Un fabricante de nanopartículas de plata (AgNPs) para recubrimientos antimicrobianos afirma que su proceso de síntesis produce partículas con un diámetro medio de $\mu_0 = 50\ \text{nm}$ y desviación estándar histórica conocida $\sigma = 4\ \text{nm}$ (parámetro bien caracterizado tras años de producción). Un laboratorio de control de calidad toma una muestra de $n=36$ nanopartículas de un nuevo lote y mide, vía dispersión dinámica de luz (DLS), un diámetro promedio muestral de $\bar{x} = 48.3\ \text{nm}$. Con $\alpha = 0.05$, se desea determinar si el nuevo lote es consistente con el proceso caracterizado o si el diámetro medio se ha desviado significativamente.

### 2.2 Paso 1: Planteamiento de Hipótesis
$$H_0: \mu = 50\ \text{nm} \qquad H_1: \mu \neq 50\ \text{nm}$$
Como $\sigma$ es conocida a partir del historial extenso del proceso, corresponde un **Z-test** bilateral para la media.

### 2.3 Paso 2: Cálculo del Estadístico de Prueba
$$z_0 = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}} = \frac{48.3 - 50}{4/\sqrt{36}} = \frac{-1.7}{0.6\overline{6}} \approx \boxed{-2.55}$$

### 2.4 Paso 3: Región Crítica y Decisión
Para $\alpha=0.05$ bilateral, $z_{\alpha/2} = z_{0.025} = 1.96$. La regla de rechazo es $z_0 \notin (-1.96,\ 1.96)$.

Como $z_0 = -2.55 < -1.96$, **se rechaza $H_0$**: existe evidencia estadística significativa de que el diámetro medio de las nanopartículas de plata del nuevo lote difiere de los $50\ \text{nm}$ especificados.

### 2.5 Paso 4: Cálculo del p-valor
$$\text{p-valor} = 2 \cdot P(Z < -2.55) = 2 \cdot 0.00539 \approx \boxed{0.0108}$$

Como $0.0108 < 0.05$, el p-valor confirma la decisión de rechazo tomada con el valor crítico, reforzando que el lote debe someterse a revisión del proceso de síntesis antes de su liberación para recubrimientos antimicrobianos.

### 2.6 Prueba Unitaria con pytest

Se verifica que el estadístico $z_0$, el valor crítico $z_{0.025}$ y el p-valor coincidan con los calculados a mano, y que la regla de decisión (rechazar $H_0$ porque $z_0$ cae fuera de la región de no rechazo) sea la correcta:

```python
import ipytest
import pytest
from scipy.stats import norm

ipytest.autoconfig()

x_bar, mu_0, sigma, n = 48.3, 50, 4, 36
alpha = 0.05


def test_estadistico_z_de_prueba():
    z0 = (x_bar - mu_0) / (sigma / n ** 0.5)
    assert z0 == pytest.approx(-2.55, rel=1e-3)


def test_valor_critico_bilateral_para_alpha_005():
    z_critico = norm.ppf(1 - alpha / 2)
    assert z_critico == pytest.approx(1.96, rel=1e-3)


def test_se_rechaza_h0_porque_z0_cae_fuera_de_la_region_de_no_rechazo():
    z0 = (x_bar - mu_0) / (sigma / n ** 0.5)
    z_critico = norm.ppf(1 - alpha / 2)
    assert abs(z0) > z_critico


def test_p_valor_coincide_con_la_decision_de_rechazo():
    z0 = (x_bar - mu_0) / (sigma / n ** 0.5)
    p_valor = 2 * norm.cdf(z0)
    assert p_valor == pytest.approx(0.0108, rel=1e-2)
    assert p_valor < alpha


ipytest.run("-vv")
```

---

## 3. Código de Verificación Simbólica (SymPy)

---

* *Optimization of Silver Nanoparticle-Coating Methods on Acrylic, Silicone, and Zirconia Facial Prosthetic Materials: Surface Characterization and Antimicrobial Activity Against Pseudomonas aeruginosa* (2026). *Prosthesis*, 8(7), 66. DOI: [10.3390/prosthesis8070066](https://doi.org/10.3390/prosthesis8070066) — usa pruebas $t$ pareadas para evaluar reproducibilidad y confiabilidad del recubrimiento de nanopartículas de plata (AgNPs), la misma prueba de hipótesis sobre diámetro de AgNPs desarrollada en el ejemplo aplicado de esta unidad.
