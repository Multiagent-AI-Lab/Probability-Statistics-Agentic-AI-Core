### 1.4 Demostración Práctica: Implementación Directa del Generador Congruencial Lineal

La recurrencia $X_{n+1} = (a X_n + c) \pmod m$ es la piedra angular de los generadores seudoaleatorios modernos. En esta subsección, implementamos un LCG desde cero para entender su mecanismo interno, verificar su determinismo y su rango, y aplicarlo a la generación de posiciones iniciales de nanopartículas en una simulación de difusión.

#### Implementación Base del LCG

```python
def lcg(seed: int, a: int, c: int, m: int, n: int) -> list[int]:
    """
    Generador Congruencial Lineal: X_{n+1} = (a*X_n + c) mod m.
    
    Parámetros:
    -----------
    seed : int
        Semilla inicial X_0.
    a : int
        Multiplicador (debe garantizar período máximo).
    c : int
        Incremento (generalmente coprimo con m).
    m : int
        Módulo (determina el rango [0, m)).
    n : int
        Número de valores a generar.
    
    Retorna:
    --------
    list[int]
        Secuencia de n enteros seudoaleatorios en [0, m).
    """
    valores = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        valores.append(x)
    return valores

## Demostración numérica con parámetros del RANDU (generador histórico educativo)
secuencia = lcg(seed=7, a=1103515245, c=12345, m=2**31, n=10)
print("Secuencia LCG generada:", secuencia)

## Verificar que todos los valores están en el rango [0, m)
m = 2**31
todos_en_rango = all(0 <= v < m for v in secuencia)
print(f"Todos los valores en [0, {m}):", todos_en_rango)

## Verificar determinismo: misma semilla produce la misma secuencia
secuencia_2 = lcg(seed=7, a=1103515245, c=12345, m=2**31, n=10)
determinístico = secuencia == secuencia_2
print("¿Determinístico (misma semilla)?:", determinístico)

## Normalizar a [0, 1) dividiendo por m
secuencia_normalizada = [x / m for x in secuencia]
print("Primeros 5 valores normalizados a (0, 1):", secuencia_normalizada[:5])
```

**Salida esperada:**
```
Secuencia LCG generada: [1282168116, 642666333, 712265938, 1486001571, 2131988640, 220562521, 2099423262, 2083449087, 523310796, 715197717]
Todos los valores en [0, 2147483648): True
¿Determinístico (misma semilla)?: True
Primeros 5 valores normalizados a (0, 1): [0.5970560554414988, 0.29926483193412423, 0.3316746735945344, 0.6919734044931829, 0.9927845746278763]
```

#### Aplicación a Nanotecnología: Posiciones Iniciales de Nanopartículas

En simulaciones de difusión de nanopartículas en solución acuosa, las posiciones iniciales de las partículas deben ser distribuidas uniformemente en el volumen de la celda de simulación. Usamos el LCG para generar las coordenadas $(x, y, z)$ de $N$ nanopartículas dentro de una caja cúbica $[0, L]^3$:

```python
import numpy as np

def generar_posiciones_iniciales_con_lcg(n_particulas: int, longitud_caja: float, seed: int) -> np.ndarray:
    """
    Genera posiciones iniciales de nanopartículas usando LCG.
    
    Parámetros:
    -----------
    n_particulas : int
        Número de nanopartículas a simular.
    longitud_caja : float
        Lado de la caja cúbica de simulación (en nanómetros).
    seed : int
        Semilla para reproducibilidad.
    
    Retorna:
    --------
    np.ndarray
        Matriz de forma (n_particulas, 3) con coordenadas (x, y, z).
    """
    # Generar 3*n_particulas números seudoaleatorios uniformes en [0, 1)
    numeros_pseudoaleatorios = lcg(seed=seed, a=1103515245, c=12345, m=2**31, n=3 * n_particulas)
    
    # Normalizar a [0, 1)
    uniformes = np.array([x / (2**31) for x in numeros_pseudoaleatorios])
    
    # Escalar a [0, longitud_caja]
    posiciones = uniformes[:3 * n_particulas].reshape(n_particulas, 3) * longitud_caja
    return posiciones

# Ejemplo: 5 nanopartículas en una caja de 100 nm
n_particulas = 5
longitud_caja = 100.0  # nanómetros
posiciones = generar_posiciones_iniciales_con_lcg(n_particulas, longitud_caja, seed=42)

print("Posiciones iniciales de nanopartículas (en nm):")
for i, (x, y, z) in enumerate(posiciones):
    print(f"  Partícula {i+1}: ({x:.2f}, {y:.2f}, {z:.2f})")
```

**Salida esperada:**
```
Posiciones iniciales de nanopartículas (en nm):
  Partícula 1: (58.23, 51.98, 46.60)
  Partícula 2: (77.70, 42.29, 3.34)
  Partícula 3: (41.74, 80.87, 61.23)
  Partícula 4: (71.49, 18.23, 51.62)
  Partícula 5: (56.20, 24.87, 91.96)
```

---

## 2. Ejemplo Analítico Paso a Paso: Simulación de Difusión de Nanopartículas en Medio Viscoso

### 2.1 Contexto Aplicado en Nanotecnología
En el desarrollo de nanosistemas de liberación controlada de fármacos antitumorales (doxorrubicina encapsulada en liposomas nanométricos), se requiere evaluar el tiempo de tránsito $T$ (en segundos) que tarda una nanopartícula en atravesar la membrana endotelial microvascular. Debido a la heterogeneidad estructural del tejido tumoral, la tasa de permeación sigue una distribución de Weibull con parámetro de forma $k = 1.5$ y parámetro de escala $\lambda = 12.0\text{ segundos}$.

Para optimizar la dosis mediante simulaciones estocásticas de millones de trayectorias celulares:
1. Derivar la fórmula analítica explicita del método de la transformada inversa para la distribución de Weibull.
2. Calcular analíticamente el tiempo de tránsito $T$ correspondiente a un número aleatorio uniforme generado $U = 0.35$.
3. Estimar la media del tiempo de tránsito $\mathbb{E}[T]$ utilizando la función Gamma.

### 2.2 Paso 1: Derivación del Método de la Transformada Inversa para Weibull
La función de distribución acumulada (CDF) de la distribución de Weibull es:
$$F(t) = 1 - \exp\left(-\left(\frac{t}{\lambda}\right)^k\right), \quad t \ge 0$$

Igualando $F(t) = U$ con $U \sim \text{Uniforme}(0, 1)$:
$$1 - \exp\left(-\left(\frac{t}{\lambda}\right)^k\right) = U \implies 1 - U = \exp\left(-\left(\frac{t}{\lambda}\right)^k\right)$$

Tomando logaritmo natural en ambos lados:
$$\ln(1 - U) = -\left(\frac{t}{\lambda}\right)^k \implies -\ln(1 - U) = \left(\frac{t}{\lambda}\right)^k$$

Despejando el tiempo de tránsito $T$:
$$t = \lambda \left(-\ln(1 - U)\right)^{1/k}$$

Puesto que si $U \sim \text{Uniforme}(0, 1)$, entonces $(1 - U) \sim \text{Uniforme}(0, 1)$, la fórmula generadora simplificada es:
$$\boxed{T = \lambda \cdot (-\ln U)^{1/k}}$$

### 2.3 Paso 2: Evaluación Numérica Paso a Paso para $U = 0.35$
Sustituyendo los parámetros $\lambda = 12.0$, $k = 1.5$ y $U = 0.35$:
1. Logaritmo natural: $-\ln(0.35) \approx -(-1.049822) = 1.049822$
2. Exponente $1/k = 1/1.5 = \frac{2}{3} \approx 0.666667$
3. Potencia: $(1.049822)^{0.666667} \approx 1.032945$
4. Tiempo final $T$:
$$\boxed{T = 12.0 \times 1.032945 \approx 12.3953 \text{ segundos}}$$

### 2.4 Paso 3: Cálculo del Valor Esperado Teórico $\mathbb{E}[T]$
$$\mathbb{E}[T] = \lambda \cdot \Gamma\left(1 + \frac{1}{k}\right) = 12.0 \cdot \Gamma(1 + 0.6667) = 12.0 \cdot \Gamma(1.6667) \approx 12.0 \times 0.902746 \approx 10.833 \text{ s}$$

### 2.5 Prueba Unitaria con pytest

Antes de lanzar millones de trayectorias simuladas, se verifica la fórmula generadora de la transformada inversa contra un valor de $U$ conocido y contra la función de supervivencia de `scipy.stats.weibull_min` (deben ser funciones inversas entre sí):

```python
import ipytest
import pytest
import numpy as np
from scipy.stats import weibull_min
from scipy.special import gamma

ipytest.autoconfig()

lam, k = 12.0, 1.5


def test_transformada_inversa_para_u_conocida():
    U = 0.35
    T = lam * (-np.log(U)) ** (1 / k)
    assert T == pytest.approx(12.3953, rel=1e-4)


def test_transformada_inversa_es_consistente_con_la_funcion_de_supervivencia():
    ## La formula usa T = lambda*(-ln U)^(1/k), que invierte 1-F(t)=U (la
    ## funcion de supervivencia), no F(t)=U directamente -- por eso se
    ## contrasta contra .sf() y no contra .cdf().
    U = 0.35
    T = lam * (-np.log(U)) ** (1 / k)
    assert weibull_min.sf(T, c=k, scale=lam) == pytest.approx(U, rel=1e-6)


def test_esperanza_teorica_del_tiempo_de_transito():
    esperanza = lam * gamma(1 + 1 / k)
    assert esperanza == pytest.approx(10.833, rel=1e-3)


ipytest.run("-vv")
```

---

## 3. Código de Verificación Simbólica (SymPy)

---

* Shabbir, F., Mujeeb, A. A., Jawed, S. F. et al. (2024). Simulation of transvascular transport of nanoparticles in tumor microenvironments for drug delivery applications. *Scientific Reports*, 14, 1764. DOI: [10.1038/s41598-024-52292-0](https://doi.org/10.1038/s41598-024-52292-0) — simulación computacional del transporte de nanopartículas a través de la microvasculatura tumoral, el mismo escenario de difusión estocástica modelado en el ejemplo aplicado de esta unidad.
