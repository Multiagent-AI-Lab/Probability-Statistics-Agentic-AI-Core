# AUDITORÍA DETALLADA DE NOTEBOOKS Y CONTENIDO (FASE 1)
## Course: Probabilidad y Estadística Inferencial — UCEMICH
### Ingeniería en IA y Nanotecnología | Semestre 2026-2027-I

---

## 1. RESUMEN DE LA AUDITORÍA

Se auditaron un total de **22 notebooks** pertenecientes a los archivos clave extraídos:
- **20 Notebooks del Profesor** (`raw_student_notebooks/profesor/`)
- **2 Notebooks Seleccionados de Alumnos** (`raw_student_notebooks/alumnos_seleccionados/`)

---

## 2. REPORTE DE NOTEBOOKS DEL PROFESOR (`raw_student_notebooks/profesor/`)

| Archivo | Tamaño | Celdas (MD/Code) | Palabras MD | Ecuaciones LaTeX | Librerías clave | Gráficos |
|---|---|---|---|---|---|---|
| `Estadística_SciPy_MEJORADA.ipynb` | 5.1 MB | 142 (69/73) | 9,897 | 914 | scipy, statsmodels, seaborn, pandas | ✅ Sí |
| `Copy_of_Estadística_SciPy_MEJORADA (1).ipynb` | 5.2 MB | 159 (80/79) | 11,944 | 1,270 | scipy, statsmodels, seaborn, pandas | ✅ Sí |
| `Ejercicios2EvaluacióndeRespuestas.ipynb` | 3.0 MB | 139 (106/33) | 8,286 | 1,375 | scipy, pandas, matplotlib, numpy | ✅ Sí |
| `Distribuciones_de_probabilidad_continuas.ipynb` | 1.0 MB | 107 (79/28) | 23,623 | 1,957 | scipy, seaborn, pandas, numpy | ✅ Sí |
| `Variables Aleatorias Continuas.ipynb` | 982 KB | 47 (32/15) | 4,403 | 395 | scipy, matplotlib, numpy | ✅ Sí |
| `Capítulo 5 secciones 5.3 a 5.8.ipynb` | 859 KB | 56 (34/22) | 9,105 | 1,379 | scipy, sympy, matplotlib, numpy | ✅ Sí |
| `Ejercicios 2 Conclusiones y Ejercicios de Tarea.ipynb` | 723 KB | 162 (135/27) | 10,995 | 1,873 | scipy, sympy, matplotlib, numpy | ✅ Sí |
| `Ejercicios_de_variables_Aleatorias_Continuas(1).ipynb` | 717 KB | 60 (45/15) | 5,024 | 847 | scipy, matplotlib, numpy | ✅ Sí |
| `Copia de MODELOS_PARA_VARIABLES_ALEATORIAS_python.ipynb` | 498 KB | 113 (65/48) | 5,893 | 547 | scipy, seaborn, pandas, numpy | ✅ Sí |
| `Variables discretas.ipynb` | 349 KB | 32 (21/11) | 1,406 | 184 | matplotlib, numpy | ✅ Sí |
| `Investigación(5).ipynb` | 254 KB | 34 (24/10) | 2,731 | 438 | sympy, scipy, matplotlib | ✅ Sí |
| `Ejercicios_2_Conclusiones_y_Ejercicios_de_Tarea.ipynb` | 105 KB | 12 (10/2) | 3,478 | 508 | sympy, scipy, matplotlib | ✅ Sí |

---

## 3. REPORTE DE NOTEBOOKS SELECCIONADOS DE ALUMNOS (`raw_student_notebooks/alumnos_seleccionados/`)

| Archivo | Alumno | Tamaño | Celdas (MD/Code) | Palabras MD | Ecuaciones LaTeX | Librerías clave |
|---|---|---|---|---|---|---|
| `Resumen_del_capitulo_3_y_ejercicios.ipynb` | Oswaldo Odel López Gil (200160) | 2.9 MB | 109 (57/52) | 7,875 | 645 | scipy, seaborn, pandas, numpy |
| `Resumen_del_capitulo_4_y_ejercicios.ipynb` | Oswaldo Odel López Gil (200160) | 3.4 MB | 152 (83/69) | 16,625 | 1,652 | scipy, seaborn, pandas, numpy |

---

## 4. SELECCIÓN DE NOTEBOOKS "GOLD STANDARD" POR UNIDAD

De la auditoría se determinan los notebooks base que servirán como **"Gold Standard"** para alimentar el pipeline de refactorización y generación de lecciones Markdown:

| Unidad | Título | Notebook Base Principal (Gold Standard) | Aporte secundario / Complemento |
|---|---|---|---|
| **U1** | Estadística Descriptiva y EDA | `Estadística_SciPy_MEJORADA.ipynb` | `Practica Estadistica Descriptiva.tex` (LaTeX) |
| **U2** | Probabilidad y Combinatoria | `ejercicios1.tex` + `examen1_prob_basica_nano.tex` | `Ejercicios_2_Conclusiones_y_Ejercicios_de_Tarea.ipynb` |
| **U3** | Variables Aleatorias Discretas | `MODELOS_PARA_VARIABLES_ALEATORIAS_python.ipynb` | `Resumen_del_capitulo_3_y_ejercicios.ipynb` (Oswaldo) |
| **U4** | Distribuciones Conjuntas | `Capítulo 5 secciones 5.3 a 5.8.ipynb` | `Ejercicios 2 Conclusiones y Ejercicios de Tarea.ipynb` |
| **U5** | Variables Aleatorias Continuas | `Distribuciones_de_probabilidad_continuas.ipynb` | `Resumen_del_capitulo_4_y_ejercicios.ipynb` (Oswaldo) |
| **U6** | Inferencia y Pruebas de Hipótesis | `Estadística_SciPy_MEJORADA.ipynb` (sección 6) | `Investigación_Capítulo_5_secciones_5.3_a_5.8.ipynb` |
| **U7** | Proyecto Integrador & Evaluación AI | `Ejercicios2EvaluacióndeRespuestas.ipynb` | Dataset `nn8b07562_si_0012.csv` (Meta-Analysis Nanopartículas) |

---

## 5. DIAGNÓSTICO DE BRECHAS (GAPS) Y ACCIONES DE REFACTORIZACIÓN

1. **Estandarización de Fórmulas Matemática en Python**:
   - Muchos notebooks usan la notación matemática en bloques de markdown, pero carecen del estándar `display(Math())` de SymPy/IPython exigido por el Protocolo Maestro.
2. **Homogeneización del Contexto de Nanotecnología**:
   - `Distribuciones_de_probabilidad_continuas.ipynb` y `Estadística_SciPy_MEJORADA.ipynb` tienen un altísimo rigor matemático (>20,000 palabras en conjunto), pero requieren conectar explícitamente sus ejemplos con las propiedades de nanopartículas (potencial zeta, diámetro, toxicidad).
3. **Consolidación de Probabilidad y Combinatoria (U2)**:
   - La teoría de combinatoria está contenida en archivos LaTeX (`.tex`). Debe migrarse a la lección `UNIDAD_2_PROBABILIDAD_COMBINATORIA.md`.
4. **Validación Numérica con scipy.stats & statsmodels**:
   - Todo el código computacional debe auditarse para asegurar docstrings completos, type hints y comentarios "Master Class".
