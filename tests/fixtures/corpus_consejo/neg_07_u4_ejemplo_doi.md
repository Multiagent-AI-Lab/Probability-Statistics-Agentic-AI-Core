### 4.4 Ejemplos Analíticos Completos

**Ejemplo A — Discreto: Suma de dos dados justos.** Con $P_X(k)=1/6$ para $k=1,\dots,6$, el número de pares $(x,y)$ con $x+y=z$ crece de 1 (en $z=2$) a 6 (en $z=7$) y decrece simétricamente hasta 1 (en $z=12$), produciendo la distribución triangular clásica $P_Z(7) = 6/36 = 1/6$.

```python
import numpy as np
import matplotlib.pyplot as plt

p = np.ones(6) / 6  # pmf de un dado
## convolución discreta (modo 'full')
pz = np.convolve(p, p)
z_vals = np.arange(2, 13)
print("P(Z=z) para z=2..12:", np.round(pz, 4))

plt.stem(z_vals, pz, basefmt=" ")
plt.xlabel("z")
plt.ylabel("P(Z=z)")
plt.title("PMF de la suma de dos dados justos")
plt.grid(True)
plt.show()
```

**Ejemplo B — Suma de Binomiales.** Si $X\sim \mathrm{Binomial}(n_1,p)$ y $Y\sim \mathrm{Binomial}(n_2,p)$ independientes, entonces $Z=X+Y\sim\mathrm{Binomial}(n_1+n_2,p)$. Interpretando $X$ como éxitos en $n_1$ ensayos y $Y$ en $n_2$ ensayos disjuntos con la misma $p$, la unión es $n_1+n_2$ ensayos independientes. Formalmente, por convolución de PMFs y la identidad de Vandermonde $\sum_{i=0}^k \binom{n_1}{i}\binom{n_2}{k-i} = \binom{n_1+n_2}{k}$:
$$P(Z=k) = \binom{n_1+n_2}{k} p^k(1-p)^{n_1+n_2-k}$$

```python
import numpy as np
from scipy.stats import binom

n1, n2, p = 5, 3, 0.4
x = np.arange(0, n1 + 1)
y = np.arange(0, n2 + 1)
pmf_x = binom.pmf(x, n1, p)
pmf_y = binom.pmf(y, n2, p)

pmf_z = np.convolve(pmf_x, pmf_y)
k = np.arange(0, n1 + n2 + 1)
pmf_z_binom = binom.pmf(k, n1 + n2, p)

np.testing.assert_allclose(pmf_z, pmf_z_binom, atol=1e-12)
print("Convolución coincide con Binomial(n1+n2,p).")
```

**Ejemplo C — Suma de Poissons.** Si $X\sim \mathrm{Poisson}(\lambda_1)$ y $Y\sim \mathrm{Poisson}(\lambda_2)$ independientes, entonces $Z=X+Y\sim\mathrm{Poisson}(\lambda_1+\lambda_2)$. Usando la función generadora de probabilidad $G_X(s)=\exp(\lambda_1(s-1))$: $G_Z(s)=G_X(s)G_Y(s)=\exp((\lambda_1+\lambda_2)(s-1))$, que es la PGF de $\mathrm{Poisson}(\lambda_1+\lambda_2)$.

**Ejemplo D — Convolución de dos Uniformes $U[0,1]$.** Con $X,Y\sim U[0,1]$ independientes, el intervalo de integración efectivo es $x\in[\max(0,z-1),\min(1,z)]$, dando la densidad triangular clásica en $[0,2]$:
$$f_Z(z) = \begin{cases} z, & 0 \le z \le 1 \\ 2-z, & 1 < z \le 2 \\ 0, & \text{en otro caso} \end{cases}$$

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve

N = 1000
x = np.linspace(0, 1, N)
dx = x[1] - x[0]
fX = np.ones_like(x)
fY = np.ones_like(x)
fZ_num = fftconvolve(fX, fY) * dx
z = np.linspace(0, 2, len(fZ_num))
fZ_theo = np.where(z <= 1, z, 2 - z)
fZ_theo = np.where((z < 0) | (z > 2), 0, fZ_theo)

plt.plot(z, fZ_num, label='numérica (fft conv)')
plt.plot(z, fZ_theo, '--', label='teórica')
plt.legend()
plt.xlabel('z'); plt.ylabel('f_Z(z)')
plt.title('Convolución de dos Uniformes[0,1]')
plt.show()
```

**Ejemplo E — Suma de Normales.** Si $X\sim N(\mu_1,\sigma_1^2)$ y $Y\sim N(\mu_2,\sigma_2^2)$ independientes, usando la función característica $\phi_X(t)=\exp(i\mu_1 t - \tfrac12\sigma_1^2t^2)$ se obtiene $\phi_Z(t)=\phi_X(t)\phi_Y(t)=\exp(i(\mu_1+\mu_2)t - \tfrac12(\sigma_1^2+\sigma_2^2)t^2)$, que corresponde a $Z\sim N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$.

### 4.5 Tabla Resumen: Suma de Distribuciones Comunes

| Distribución de $X$ | Distribución de $Y$ | Distribución de $Z=X+Y$ | Nota |
|:---:|:---:|:---:|:---|
| $\mathrm{Binomial}(n_1,p)$ | $\mathrm{Binomial}(n_2,p)$ | $\mathrm{Binomial}(n_1+n_2,p)$ | Identidad de Vandermonde |
| $\mathrm{Poisson}(\lambda_1)$ | $\mathrm{Poisson}(\lambda_2)$ | $\mathrm{Poisson}(\lambda_1+\lambda_2)$ | Producto de PGFs |
| $\mathrm{Normal}(\mu_1,\sigma_1^2)$ | $\mathrm{Normal}(\mu_2,\sigma_2^2)$ | $\mathrm{Normal}(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$ | Función característica |
| $\mathrm{Gamma}(\alpha_1,\theta)$ | $\mathrm{Gamma}(\alpha_2,\theta)$ | $\mathrm{Gamma}(\alpha_1+\alpha_2,\theta)$ | Mismo parámetro de escala |

---

## 5. Ejemplo Analítico Paso a Paso: Diámetro y Potencial Zeta de Nanopartículas Coloidales

### 5.1 Contexto Aplicado en Nanotecnología
En el análisis bivariado de propiedades fisicoquímicas de nanopartículas coloidales, la distribución de probabilidad conjunta permite evaluar el impacto simultáneo de dos variables críticas para la estabilidad de una suspensión: el **diámetro de partícula** $X$ (en nm) y el **potencial zeta** $Y$ (en mV, una medida de la carga superficial efectiva que gobierna la repulsión electrostática entre partículas). Estas dos variables no son independientes en un proceso real de síntesis: partículas más grandes tienden a exhibir un potencial zeta más negativo debido a la mayor área superficial disponible para la adsorción de iones estabilizantes (p. ej. citrato).

Se modela el par $(X,Y)$ como un vector aleatorio bivariado con:
$$\mu = \begin{pmatrix} 25.0 \\ -40.0 \end{pmatrix} \text{nm, mV}, \qquad \Sigma = \begin{pmatrix} 16.0 & -18.0 \\ -18.0 & 36.0 \end{pmatrix}$$

### 5.2 Paso 1: Interpretación de la Matriz de Covarianza
La varianza de $X$ es $\mathrm{Var}(X)=16\ \text{nm}^2$ ($\sigma_X=4\ \text{nm}$) y la de $Y$ es $\mathrm{Var}(Y)=36\ \text{mV}^2$ ($\sigma_Y=6\ \text{mV}$). La covarianza $\mathrm{Cov}(X,Y)=-18$ es negativa, confirmando la relación inversa esperada entre tamaño de partícula y potencial zeta.

### 5.3 Paso 2: Coeficiente de Correlación
$$\rho_{X,Y} = \frac{\mathrm{Cov}(X,Y)}{\sigma_X \sigma_Y} = \frac{-18}{4 \times 6} = \boxed{-0.75}$$

Una correlación de $-0.75$ indica una relación lineal inversa fuerte: lotes con nanopartículas de mayor diámetro promedio tienden sistemáticamente a un potencial zeta más negativo, lo cual es relevante para el control de calidad, ya que un $|\zeta| < 30\ \text{mV}$ suele considerarse zona de riesgo de agregación coloidal.

### 5.4 Paso 3: Simulación por Descomposición de Cholesky
Para generar muestras correlacionadas de este vector bivariado, se factoriza $\Sigma = LL^T$ (descomposición de Cholesky) y se transforma ruido gaussiano independiente $Z\sim N(0,I_2)$:
$$X = \mu + LZ \implies X \sim N(\mu, \Sigma)$$

### 5.5 Paso 4: Probabilidad de Zona de Riesgo de Agregación
Usando la marginal de $Y\sim N(-40, 36)$, la probabilidad de que un lote tenga $|\zeta|<30\ \text{mV}$ (es decir $-30 < Y$) es:
$$P(Y > -30) = P\left(Z > \frac{-30-(-40)}{6}\right) = P(Z > 1.667) \approx \boxed{0.0478}$$

Aproximadamente el $4.78\%$ de las nanopartículas individuales caen en zona de riesgo de agregación por baja repulsión electrostática, información crítica para decidir si el lote requiere reformulación del agente estabilizante.

### 5.6 Prueba Unitaria con pytest

Antes de simular por Cholesky, se verifica que $\Sigma$ sea una matriz de covarianza válida (semidefinida positiva — de lo contrario `np.linalg.cholesky` fallaría al intentar factorizarla), además de contrastar la correlación y la probabilidad de zona de riesgo:

```python
import ipytest
import numpy as np
import pytest
from scipy.stats import norm

ipytest.autoconfig()

Sigma = np.array([[16.0, -18.0], [-18.0, 36.0]])
sigma_x, sigma_y = 4.0, 6.0


def test_matriz_de_covarianza_es_semidefinida_positiva():
    ## Requisito para que exista la descomposicion de Cholesky (Sigma = L L^T)
    eigenvalores = np.linalg.eigvalsh(Sigma)
    assert (eigenvalores >= 0).all()


def test_coeficiente_de_correlacion_diametro_potencial_zeta():
    rho = Sigma[0, 1] / (sigma_x * sigma_y)
    assert rho == pytest.approx(-0.75)


def test_probabilidad_de_zona_de_riesgo_de_agregacion():
    prob_riesgo = 1 - norm.cdf(-30, loc=-40, scale=sigma_y)
    assert prob_riesgo == pytest.approx(0.0478, rel=1e-2)


ipytest.run("-vv")
```

---

## 6. Vectores Aleatorios, Matriz de Covarianza y Normal Multivariada

---

* Pochapski, D. J. et al. (2021). Zeta Potential and Colloidal Stability Predictions for Inorganic Nanoparticle Dispersions: Effects of Experimental Conditions and Electrokinetic Models on the Interpretation of Results. *Langmuir*, 37(43), 13379-13389. DOI: [10.1021/acs.langmuir.1c02056](https://doi.org/10.1021/acs.langmuir.1c02056) — relación entre diámetro de partícula y potencial zeta en dispersiones coloidales, la distribución conjunta bivariada modelada en el ejemplo aplicado de esta unidad.
