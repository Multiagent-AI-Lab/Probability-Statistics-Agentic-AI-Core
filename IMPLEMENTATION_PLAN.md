# Plan de Enriquecimiento: Extracción de Modelado y Simulación a Probabilidad y Estadística

Este plan detalla el proceso para extraer los componentes clave de simulación estocástica, métodos numéricos y modelos avanzados desde el ZIP `MODELADO Y SIMULACION 2025-2026-I-20260805T163733Z-1-001.zip` (227 notebooks base del profesor) para enriquecer las 7 lecciones de **Probabilidad y Estadística Inferencial**.

---

## 🎯 Objetivo General
Elevar el rigor computacional y práctico del curso de **Probabilidad y Estadística Inferencial**, integrando métodos de **Simulación Monte Carlo, Generación por Transformada Inversa, Método de Aceptación-Rechazo, Estimación MLE Computacional, Bootstrap e Inferencia Simulada** extraídos del material maestro de **Modelado y Simulación**.

---

## 🛠️ Plan de Trabajo por Fases

### Fase 1: Extracción de Notebooks Clave de Simulación
Extraer los notebooks maestros de simulación del ZIP a la carpeta local `raw_student_notebooks/profesor/modelado_simulacion/`:
- `Investigación_VADC.ipynb` (6.95 MB) — Modelos de simulación continua.
- `Investigación_de_variables_.ipynb` (6.19 MB) — Simulación de variables aleatorias.
- `Proyecto_final_MyS.ipynb` (5.88 MB) — Aplicación integradora de simulación.
- `MODELOS_PARA_VARIABLES_ALEATORIAS_DARS1python.ipynb` (5.15 MB) — Algoritmos de generación probabilística.
- `Ejercicios_Distribuciones_Conjuntas_II .ipynb` (5.17 MB) — Simulación bivariada.

---

### Fase 2: Enriquecimiento Específico de las 7 Lecciones (`lecciones/*.md`)

| Unidad | Contenido de Simulación a Agregar |
|---|---|
| **U1: Estadística Descriptiva** | Estimación No Paramétrica de Densidad (KDE), Kernel smoothing y simulación de muestras sintéticas multivariadas. |
| **U2: Probabilidad y Combinatoria** | Algoritmos de **Simulación de Monte Carlo** para estimar probabilidades de eventos complejos y reglas condicionales. |
| **U3: Variables Discretas** | Algoritmo de Generación Estocástica por Suma Acumulada para Binomial, Poisson y Geométrica aplicada a fallas en nano-dispositivos. |
| **U4: Distribuciones Conjuntas** | Generación de muestras bivariadas continuas/discretas, matriz de covarianza simulada y descomposición de Cholesky. |
| **U5: Variables Continuas** | **Método de la Transformada Inversa** (Inversión de CDF) y **Método de Aceptación-Rechazo** para distribuciones Weibull, Gamma y Lognormal. |
| **U6: Inferencia y Estimación** | Estimación por **Máxima Verosimilitud (MLE) Computacional** con `scipy.optimize` e **Intervalos de Confianza por Bootstrap**. |
| **U7: Proyecto Integrador** | Simulación computacional de la **Potencia de la Prueba ($1 - \beta$)** y curva de características operativas (OC curve). |

---

### Fase 3: Ejecución de la Pipeline Agéntica y Compilación de Notebooks

#### 3.1 Reparación y Pulido Editorial con `@Editor` (`LayoutEditorialAgent`)
- Depurar automáticamente etiquetas o encabezados descontextualizados procedentes del ZIP de Modelado.
- Garantizar maquetación limpia y formato KaTeX perfecto en todas las 7 lecciones.

#### 3.2 Compilación de Notebooks Jupyter (`notebooks/*.ipynb`)
- Recompilar las 7 unidades con `NotebookCompilerAgent` y `OrchestratorAgent`.

#### 3.3 Auditoría de Coherencia Pedagógica (`PedagogicalReviewPipeline`)
- Ejecutar el debate colectivo entre `ContentAuditorAgent`, `@Scientist`, `@Safety_Gate`, `@Editor`, `SocraticDebugger` y `EvaluatorCriticAgent`.

---

## 🧪 Plan de Verificación

1. **Compilación Exitos:** Las 7 unidades en `notebooks/*.ipynb` deben obtener un estatus de **APPROVED** con calificación $\ge 95.0 / 100$.
2. **Coherencia Pedagógica & Editorial:** Cada unidad debe obtener **100.0/100** en el reporte `docs/REPORT_PEDAGOGICAL_CRITIQUE.md`.
3. **Suite de Pruebas Automáticas:** Ejecutar `pytest` garantizando que **6/6 tests pasen en 0.20s**.
