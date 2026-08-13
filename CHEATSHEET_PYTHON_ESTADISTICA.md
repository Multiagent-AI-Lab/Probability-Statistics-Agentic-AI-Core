# CHEATSHEET DE PYTHON PARA PROBABILIDAD Y ESTADÍSTICA

## 1. Importaciones Estándar
```python
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
import sympy as sp
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, Math
```

## 2. Estadística Descriptiva (SciPy & Pandas)
```python
# Media, Mediana, Varianza y Desviación Estándar
media = np.mean(data)
mediana = np.median(data)
var_s = np.var(data, ddof=1)
std_s = np.std(data, ddof=1)
cv = (std_s / media) * 100
kurt = stats.kurtosis(data)
```

## 3. Distribuciones de Probabilidad (scipy.stats)
```python
# Normal N(mu, sigma)
rv_norm = stats.norm(loc=120, scale=8)
pdf_val = rv_norm.pdf(125)      # f(x)
cdf_val = rv_norm.cdf(128)      # P(X <= 128)
ic_95 = rv_norm.interval(0.95)  # Intervalo 95%

# Poisson(lambda)
rv_poi = stats.poisson(mu=3.5)
pmf_val = rv_poi.pmf(4)         # P(X = 4)

# Hipergeométrica(M, n, N)
rv_hyp = stats.hypergeom(M=10, n=4, N=3)
pmf_hyp = rv_hyp.pmf(2)
```

## 4. Inferencia e Intervalos de Confianza
```python
# IC t-Student para la media
ic_t = stats.t.interval(confidence=0.95, df=len(data)-1, loc=np.mean(data), scale=stats.sem(data))

# Test de Bondad de Ajuste Kolmogorov-Smirnov
ks_stat, p_val = stats.kstest(data, 'norm', args=(np.mean(data), np.std(data, ddof=1)))
```

## 5. Salida Matemática Elegante
```python
display(Math(fr"\bar{{x}} = {media:.2f} \text{{ nm}}, \quad s = {std_s:.2f} \text{{ nm}}"))
```
