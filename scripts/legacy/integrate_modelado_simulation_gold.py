"""
Script para integrar y fusionar las secciones avanzadas de Simulación
(Monte Carlo, Transformada Inversa, Aceptación-Rechazo, MLE Computacional, Bootstrap y Potencia de Prueba)
procedentes del material de Modelado y Simulación hacia las 7 lecciones en lecciones/*.md.
"""

import os

lecciones_dir = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\lecciones'

# 1. Módulo de Simulación para Unidad 1
u1_sim = """

---

## 10. Módulo de Simulación: Estimación No Paramétrica de Densidad (KDE) y Muestras Multivariadas

En el análisis de datos de caracterización nanotecnológica, cuando no se presupone un modelo paramétrico estricto, se emplea la **Estimación No Paramétrica de Densidad por Kernel (KDE)**.

### 10.1 Definición Matemática de KDE
Dada una muestra independiente de tamaño $n$, el estimador de densidad por kernel $f_h(x)$ viene dado por:
$$f_h(x) = \frac{1}{n h} \sum_{i=1}^n K\left(\frac{x - x_i}{h}\right)$$
donde $K(u)$ es el kernel gaussiano $K(u) = \frac{1}{\sqrt{2\pi}} e^{-u^2/2}$ y $h > 0$ es el ancho de banda (bandwidth).

### 10.2 Implementación Computacional en Python
```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, Math

# Generación de muestra sintética bimodal (nanopartículas coloidales)
np.random.seed(101)
muestras_nano = np.concatenate([
    stats.norm.rvs(loc=15, scale=2, size=300),
    stats.norm.rvs(loc=35, scale=5, size=700)
])

# Estimación KDE
kde = stats.gaussian_kde(muestras_nano, bw_method='silverman')
x_grid = np.linspace(5, 55, 500)
pdf_kde = kde.evaluate(x_grid)

# Visualización
plt.figure(figsize=(10, 5))
sns.histplot(muestras_nano, bins=30, stat="density", color="skyblue", label="Histrograma Muestral")
plt.plot(x_grid, pdf_kde, color="darkblue", linewidth=2.5, label="Estimación KDE (Kernel Gaussiano)")
plt.title("Estimación No Paramétrica de Densidad de Diámetro de Nanopartículas (KDE)", fontsize=12, fontweight="bold")
plt.xlabel("Diámetro (nm)")
plt.ylabel("Densidad de Probabilidad")
plt.legend()
plt.tight_layout()
plt.show()

display(Math(fr"\text{{Estimación KDE completada sobre }} n = {len(muestras_nano)} \text{{ observaciones.}}"))
```
"""

# 2. Módulo de Simulación para Unidad 2
u2_sim = """

---

## 10. Módulo de Simulación: Método de Monte Carlo para Eventos Probabilísticos Complejos

La **Simulación de Monte Carlo** permite estimar probabilidades de eventos aleatorios complejos mediante la generación repetida de números seudoaleatorios según la Ley Fuerte de los Grandes Números.

### 20.1 Teorema Fundamental de Monte Carlo
Sea $E$ un evento de interés con probabilidad $P(E) = p$. Al generar $N$ simulaciones independientes donde $X_i = 1$ si ocurre $E$ y $0$ en otro caso:
$$\lim_{N \to \infty} \frac{1}{N} \sum_{i=1}^N X_i = P(E) \quad \text{con probabilidad 1}$$

### 20.2 Simulación de Filtrado de Nanopartículas por Monte Carlo
```python
import numpy as np
import scipy.stats as stats
from IPython.display import display, Math

# Simulación de Monte Carlo (N = 100,000 experimentos)
N = 100_000
np.random.seed(42)

# Dos filtros coloidales independientes con probabilidades de paso p1=0.85, p2=0.90
paso_filtro1 = stats.bernoulli.rvs(p=0.85, size=N)
paso_filtro2 = stats.bernoulli.rvs(p=0.90, size=N)

# Evento: La partícula atraviesa ambos filtros
exito_ambos = paso_filtro1 & paso_filtro2
prob_simulada = np.mean(exito_ambos)
prob_teorica = 0.85 * 0.90

display(Math(fr"\text{{Probabilidad Teórica }} P(A \cap B): {prob_teorica:.4f}"))
display(Math(fr"\text{{Probabilidad Simulada Monte Carlo (N={N:,}): }} {prob_simulada:.4f}"))
display(Math(fr"\text{{Error Relativo: }} {abs(prob_simulada - prob_teorica)/prob_teorica * 100:.3f}\%"))
```
"""

# 3. Módulo de Simulación para Unidad 3
u3_sim = """

---

## 10. Módulo de Simulación: Algoritmo de Generación Estocástica de Variables Discretas

La generación de variables aleatorias discretas a partir de una variable uniforme $U \sim \text{Uniforme}(0, 1)$ se fundamenta en la **Inversión por Suma Acumulada de la PMF**.

### 30.1 Algoritmo General de Inversión Discreta
Dada una variable discreta $X$ con PMF $P(X = x_k) = p_k$:
1. Generar $U \sim \text{Uniforme}(0, 1)$.
2. Retornar el menor valor $x_k$ tal que $\sum_{j=1}^k p_j \ge U$.

### 30.2 Simulación Estocástica de Fallas de Micro-sensores (Poisson)
```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from IPython.display import display, Math

np.random.seed(123)
N_sim = 50_000
lam = 4.5 # Promedio de defectos por obleas de silicio

# Generación directa por inversión
u_vals = stats.uniform.rvs(size=N_sim)
sim_poisson = stats.poisson.ppf(u_vals, mu=lam)

media_sim = np.mean(sim_poisson)
var_sim = np.var(sim_poisson)

display(Math(fr"\text{{Media Simulada (Poisson }} \lambda={lam}\text{{): }} {media_sim:.4f}"))
display(Math(fr"\text{{Varianza Simulada: }} {var_sim:.4f}"))
```
"""

# 4. Módulo de Simulación para Unidad 4
u4_sim = """

---

## 10. Módulo de Simulación: Generación Bivariada y Descomposición de Cholesky

Para simular vectores aleatorios continuos bivariados $(X, Y)$ con matriz de covarianza especificada $\Sigma$, se utiliza la **Descomposición de Cholesky** $\Sigma = L L^T$.

### 40.1 Algoritmo de Generación Bivariada Correlacionada
Dado $Z = (Z_1, Z_2)^T \sim \mathcal{N}(0, I_2)$ independientes:
$$X = \mu + L Z \implies X \sim \mathcal{N}(\mu, \Sigma)$$

### 40.2 Simulación en Python de Potencial Zeta y Diámetro Nanométrico
```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, Math

# Parámetros: [Diámetro (nm), Potencial Zeta (mV)]
mu = np.array([25.0, -40.0])
cov = np.array([
    [16.0, -18.0],   # Varianza X=16, Cov(X,Y)=-18
    [-18.0, 36.0]    # Varianza Y=36
])

# Descomposición de Cholesky
L = np.linalg.cholesky(cov)

# Muestreo
np.random.seed(99)
Z = stats.norm.rvs(size=(2, 10_000))
muestras_bivariadas = (mu.reshape(2, 1) + L @ Z).T

# Visualización
df_bivariado = pd.DataFrame(muestras_bivariadas, columns=["Diametro_nm", "PotencialZeta_mV"])
g = sns.jointplot(data=df_bivariado, x="Diametro_nm", y="PotencialZeta_mV", kind="kde", cmap="Blues", fill=True)
g.fig.suptitle("Simulación Bivariada por Cholesky: Diámetro vs Potencial Zeta", y=1.02, fontweight="bold")
plt.show()

cov_sim = np.cov(muestras_bivariadas.T)
display(Math(fr"\text{{Covarianza Simulada: }} \text{{Cov}}(X, Y) = {cov_sim[0, 1]:.2f}"))
```
"""

# 5. Módulo de Simulación para Unidad 5
u5_sim = """

---

## 10. Módulo de Simulación: Método de la Transformada Inversa y Aceptación-Rechazo

El muestreo numérico de distribuciones continuas complejas (como Weibull o Gamma) se basa en el **Método de la Transformada Inversa** y el **Método de Aceptación-Rechazo de von Neumann**.

### 50.1 Teorema de la Transformada Inversa
Si $U \sim \text{Uniforme}(0, 1)$ y $F(x)$ es una CDF estrictamente creciente:
$$X = F^{-1}(U) \implies X \sim F(x)$$

### 50.2 Simulación de la Distribución de Weibull para Resistencia de Fibras de Carbono
```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from IPython.display import display, Math

# Parámetros de Weibull (forma k=2.5, escala lambda=50.0)
k_shape = 2.5
lambda_scale = 50.0
N_sim = 50_000

np.random.seed(77)
U = stats.uniform.rvs(size=N_sim)

# Inversión explícita de CDF: X = lambda * (-ln(1 - U))^(1/k)
X_weibull_sim = lambda_scale * (-np.log(1.0 - U))**(1.0 / k_shape)

# Comparación con SciPy
media_teorica = stats.weibull_min.mean(c=k_shape, scale=lambda_scale)
media_simulada = np.mean(X_weibull_sim)

display(Math(fr"\text{{Media Teórica Weibull: }} \mu = {media_teorica:.4f} \text{{ MPa}}"))
display(Math(fr"\text{{Media Simulada Transformada Inversa: }} \bar{{X}} = {media_simulada:.4f} \text{{ MPa}}"))
```
"""

# 6. Módulo de Simulación para Unidad 6
u6_sim = """

---

## 10. Módulo de Simulación: Estimación MLE Computacional y Bootstrap No Paramétrico

La inferencia moderna combina la **Estimación por Máxima Verosimilitud (MLE) Computacional** con el **Remuestreo Bootstrap** para obtener intervalos de confianza empíricos sin asunciones de normalidad.

### 60.1 Algoritmo de Bootstrap No Paramétrico
Dada una muestra $x_1, \dots, x_n$:
1. Generar $B$ muestras con reemplazo de tamaño $n$: $x_b^*$.
2. Calcular el estimador $\hat{\theta}_b^*$ para cada réplica.
3. Construir el intervalo de confianza del $(1-\alpha)\times 100\%$ mediante los percentiles $[\alpha/2, 1 - \alpha/2]$.

### 60.2 Inferencia Bootstrap en Python
```python
import numpy as np
import scipy.stats as stats
from IPython.display import display, Math

np.random.seed(42)
muestra_exp = stats.expon.rvs(scale=12.5, size=40) # Muestra original

# Bootstrap (B = 10,000 réplicas)
B = 10_000
medias_boot = [np.mean(np.random.choice(muestra_exp, size=len(muestra_exp), replace=True)) for _ in range(B)]

ic_inf = np.percentile(medias_boot, 2.5)
ic_sup = np.percentile(medias_boot, 97.5)

display(Math(fr"\text{{Media Muestral Original: }} \bar{{X}} = {np.mean(muestra_exp):.3f}"))
display(Math(fr"\text{{Intervalo de Confianza Bootstrap 95\%: }} [{ic_inf:.3f}, {ic_sup:.3f}]"))
```
"""

# 7. Módulo de Simulación para Unidad 7
u7_sim = """

---

## 10. Módulo de Simulación: Simulación Computacional de la Potencia de la Prueba (1 - beta)

La **Potencia de una Prueba de Hipótesis ($1 - \beta$)** representa la probabilidad de detectar un efecto real cuando la hipótesis nula $H_0$ es falsa. La simulación de Monte Carlo permite calcular la potencia empírica ante desviaciones arbitrarias de los supuestos.

### 70.1 Algoritmo de Simulación de Potencia
Para un tamaño de muestra $n$, nivel $\alpha$ y diferencia de medias $\Delta = \mu_1 - \mu_0$:
1. Simular $N_{\text{exp}} = 10,000$ muestras bajo $H_1$.
2. Ejecutar la prueba $t$ y contabilizar el número de rechazos ($p \le \alpha$).
3. $\text{Potencia} = \frac{\text{Rechazos}}{N_{\text{exp}}}$.

### 70.2 Curva de Potencia Simulada en Python
```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from IPython.display import display, Math

N_exp = 5_000
alpha = 0.05
delta_efectos = np.linspace(0.0, 1.5, 15)
tamanos_n = [10, 25, 50]

plt.figure(figsize=(10, 5))
for n in tamanos_n:
    potencias = []
    for d in delta_efectos:
        # Generar muestras con diferencia d
        rechazos = 0
        for _ in range(N_exp):
            sample = stats.norm.rvs(loc=d, scale=1.0, size=n)
            res = stats.ttest_1samp(sample, popmean=0.0)
            if res.pvalue <= alpha:
                rechazos += 1
        potencias.append(rechazos / N_exp)
    plt.plot(delta_efectos, potencias, marker='o', label=f'Muestra n = {n}')

plt.axhline(0.80, color='red', linestyle='--', label='Potencia Deseada (80%)')
plt.title("Curva de Potencia Simulada por Monte Carlo (Prueba t de 1 Muestra)", fontsize=12, fontweight="bold")
plt.xlabel("Tamaño del Efecto (d de Cohen)")
plt.ylabel("Potencia de la Prueba (1 - beta)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

display(Math(r"\text{Simulación de Potencia Empírica completada con 5,000 experimentos por punto.}"))
```
"""

sim_modules = {
    "UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md": u1_sim,
    "UNIDAD_2_PROBABILIDAD_COMBINATORIA.md": u2_sim,
    "UNIDAD_3_VARIABLES_ALEATORIAS_DISCRETAS.md": u3_sim,
    "UNIDAD_4_DISTRIBUCIONES_CONJUNTAS.md": u4_sim,
    "UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.md": u5_sim,
    "UNIDAD_6_INFERENCIA_ESTIMACION.md": u6_sim,
    "UNIDAD_7_PROYECTO_INTEGRADOR.md": u7_sim,
}

print("=== FUSIONANDO MÓDULOS AVANZADOS DE SIMULACIÓN EN LECCIONES ===")
for fname, module_text in sim_modules.items():
    filepath = os.path.join(lecciones_dir, fname)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # Evitar duplicaciones
        if "Módulo de Simulación:" not in content:
            updated_content = content + "\n" + module_text
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"[FUSIÓN OK] {fname}")
        else:
            print(f"[YA EXISTE] {fname}")
