# Auditoría POST-N05/N06/N07 — Probability-Statistics-Agentic-AI-Core

**Fecha:** 2026-09-14 · **HEAD:** `b73931d` · **Modo:** solo lectura sobre el repo; scripts propios en scratchpad externo
**Auditoría de referencia:** `docs/superpowers/audits/2026-09-14-auditoria-post-camino-a-100.md` (94.4/100, HEAD `fa11fed`)
**Trayectoria previa:** 69.3 (`09-04`) → 88.1 (`09-11`) → 89.6 (`09-13`) → 94.4 (`09-14`)
**Pesos:** idénticos a las cuatro anteriores (suman 100), sin renegociar.

**Alcance del trabajo auditado.** `git diff fa11fed..b73931d --stat` → 25 archivos, +316/-28. Cinco commits ejecutando el plan `docs/superpowers/plans/2026-09-14-cierre-n05-n06-n07-plan.md`: cierre de N-05 (`_contraste_boxed.py`), N-06 (`mermaid_renderer.py`), I-5 (`notebook_compiler_agent.py`), B1' (`.github/workflows/ci.yml`) y N-07 (documento de recálculo). Más una revisión final de rama que corrigió el badge (289→291) y añadió validación de path traversal en `MermaidRenderer.render_to_svg`.

**Sincronía con el remoto:** `git rev-list --left-right --count origin/master...master` → `0	0`. Working tree limpio. Todo mergeado y pusheado.

**Nota sobre este archivo.** `docs/superpowers/` sigue en `.gitignore`: esta auditoría, como las cuatro anteriores, vive localmente y no se publica. Comportamiento esperado del repo.

---

## Puntuación por categoría

| Categoría | Obtenido/Peso | Evidencia (archivo:línea + qué se ejecutó) |
|---|---|---|
| 1. Profundidad/pertinencia/calidad | **11.0/11** | **Re-verificado, no heredado.** Corrí `ContentAuditorAgent.audit_content` sobre las 8 unidades reales en HEAD `b73931d`: **`score=100.0`, `passed=True`, `missing_components=[]` en las 8**. Volumen re-contado: `wc -l lecciones/UNIDAD_*.md` → **10 069 líneas**, idéntico a la ronda anterior (el rango no toca `lecciones/`). Ya completa. |
| 2. Coherencia y arco narrativo | **7.0/7** | **Heredado; categoría completa desde la ronda de 88.1.** El rango `fa11fed..b73931d` no toca `lecciones/` (verificado en el `--stat`: solo `notebooks/`, `docs/images/`, `src/`, `tests/`, CI y README). `tests/test_referencias_cruzadas.py` pasa dentro de la suite completa que corrí. |
| 3. Calidad técnica/arquitectura/infra | **8.0/8** | **Re-ejecutado por mí en HEAD `b73931d`:** `ruff check src/ tests/` → **`All checks passed!`**; `black --check src/ tests/` → **`52 files would be left unchanged`**; `isort --check-only src/ tests/` → **sin salida, exit 0**. Los tres en verde. Nota que no descuenta pero registro por segunda ronda: el CI (`.github/workflows/ci.yml:30-32`) sigue linteando solo `src/multiagent_core/`, **no `tests/`** — mi verificación es más amplia que la del CI. |
| 4. Infraestructura de agentes | **12.2/14** | Ver **"Categoría 4 en detalle"**. Resumen: **N-05 cerrado de verdad y verificado por mí ejecutando el pipeline** (las 3 variantes de la ronda anterior ahora dan `approved=False`); los adversariales pasan de **12 a 16** (`16 passed in 155.64s`), incluido un **control negativo** de fórmula simbólica genuina; suite completa **291/291 en 8:47**, exit 0. **Pero construí una sexta generación adversarial y encontré la cuarta evasión: 4 variantes con `approved=True, hallazgos=0` y 7/7 agentes en verde → hallazgo N-08 (ALTO)**, con tres vectores independientes y causa raíz aislada a nivel de función. |
| 5. Cobertura de ejercicios | **7.5/8** | **Re-contado.** `^## Ejercicio Propuesto`=1 y `%%writefile`=4 por unidad × 8 → **32 ejercicios evaluables**, idéntico. El rango no toca `lecciones/`, así que las tolerancias `1e-4` de U6 (D3, cerrado la ronda anterior) siguen vigentes. Descuento residual intacto: hardcodear el literal correcto sigue aprobando — límite inherente al diseño del verificador, no deuda nueva. |
| 6. Gobernanza y documentación | **6.0/6** | **B1' cerrado, verificado ejecutando el step de CI a mano. +0.4, categoría completa.** El gate ya no es tautológico: `.github/workflows/ci.yml:41-49` compara `pytest --collect-only` contra el badge en cada push/PR. Reproduje el step literalmente: `REAL=291 BADGE=291 → Badge OK: 291 == 291`. Y los tres números coinciden en mi propia medición: badge `README.md:7` = **291**, `--collect-only -q` = **291 tests collected**, suite completa = **291 passed**. El test local (`tests/test_readme_badge.py:32-42`) **se mantuvo y se documentó explícitamente como complementario**, no se disfrazó de gate real — honestidad de ingeniería que cuenta a favor. Descuento residual retirado. |
| 7. Seguridad del código | **6.0/6** | **Sin regresión, con refuerzo medido.** Re-medí ReDoS sobre la superficie completa (13 adversarios propios, incluidos `_ROTULO_INLINE`, `_NUMERO`, `_limpiar_latex`, `_es_formula_simbolica`, `_operandos_distintivos`): **máximo 0.4802 s con 200 000 caracteres**, todo lo demás por debajo de 0.16 s, comportamiento lineal. Cero patológico. La validación nueva de path traversal (`mermaid_renderer.py:26-27`) es **defensa en profundidad correcta** y tiene 2 tests dedicados que pasan (`test_filename_con_separador_de_ruta_se_rechaza`, `..._separador_windows_...`). `bandit` **sigue sin estar instalado** en `ia_stats` (`No module named bandit`) — lo declaro, no lo heredo como verde. |
| 8. Mantenibilidad y deuda técnica | **5.0/5** | **Re-contado por mí.** `find src -name "*.py" \| xargs wc -l \| sort -rn`: mayor módulo del repo `stats_tutor_agent.py` **549**, luego `engineer_agent.py` **471**, `_contraste_boxed.py` **358** (+14 por el fix de N-05, crecimiento proporcionado). Margen del mayor contra el umbral de 800: **31%**, sin cambio. Total `src/` = 4 691 líneas. Ya completa. |
| 9. Precisión y vigencia de dominio | **15.0/15** | **N-07 cerrado, y por encima de lo pedido. +1.0, categoría completa.** El artefacto que la ronda anterior declaró inexistente **ahora existe**: `docs/superpowers/audits/2026-09-14-recalculo-boxed-completo.md`, **91 filas de inventario** con archivo:línea + valor declarado + valor recalculado + método por entrada. Y no se limitó a cumplir: **auditó la afirmación heredada y la corrigió a la baja** — descubrió que de los 76 "recalculados" que reclamaban las rondas previas, solo **35 tenían evidencia citable**, y en vez de heredar el conteo agregado **recalculó los 93 desde cero** en esta sesión. Corrige además el inventario (93 literales → **92 fórmulas reales**; `U6:316` es un comentario de código, no contenido). **Resultado: 91/92 recalculados, 0 defectos**, con el único no cubierto (`U8:1044`, red TFP no determinista bit-a-bit) documentado con razón técnica explícita, no como omisión. Mi verificación independiente: los conteos por unidad que declara (U1 24, U2 18, U3 5, U4 10, U5 4, U6 5, U7 18, U8 9) coinciden con mi propio grep. |
| 10. Experiencia end-to-end | **5.8/6** | **I-5 cerrado y verificado ejecutando. +0.1.** Los 8 notebooks declaran ahora `metadata.kernelspec` (`{'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}`), verificado leyendo el JSON de los 8. **El efecto es real y lo medí:** mi intento de `nbconvert --execute` sobre U8 **ya no cae al Python 3.13 del sistema** — sin pasar `--ExecutePreprocessor.kernel_name`, arranca directo contra el kernel correcto y llega hasta el bloqueo real, cosa que la ronda anterior solo lograba forzando el flag. **La otra mitad de C4 sigue abierta y la reproduje de primera mano:** `OSError: [WinError 127] … Error loading "…\torch\lib\shm.dll"`. Re-descarté que sea PATH/MKL: `import torch` → **`torch OK 2.13.0+cpu`** en proceso directo y **`sub OK 2.13.0+cpu`** en subproceso limpio; falla **solo** dentro de ipykernel. **Bloqueo ambiental real, no atribuible al trabajo, y declarado como pendiente en vez de oculto.** |
| 11. Vigencia del stack | **5.0/5** | **Re-verificado.** `stats_tutor_agent.py:58` → `MODEL_NAME = os.environ.get("STATS_TUTOR_MODEL", "gemini-3.5-flash")`, con los comentarios `:50-57` documentando la migración y la instrucción de revisar deprecaciones. Sin fecha de caducidad dura pendiente. Ya completa. |
| 12. Diseño y presentación | **4.8/5** | **N-06 cerrado con la causa raíz correcta, y el artefacto existe. +0.3.** La ronda anterior diagnosticó "`mmdc` no resolvible"; la causa real era otra y el fix la identificó bien: `subprocess.run(["npx",…])` lanza `FileNotFoundError [WinError 2]` en Windows porque Python no resuelve `npx`→`npx.cmd` sin `shell=True`; `shutil.which` sí (`mermaid_renderer.py:37`). **Verificado por dos vías, ambas ejecutadas:** (a) `ls docs/images/*.svg` → **8 SVG reales**, uno por unidad, de **14 980 a 32 724 bytes** (no stubs); (b) corrí `pytest tests/test_mermaid_renderer.py -v` → **`9 passed in 15.76s`**, incluido `test_integracion_real_genera_svg_en_disco`, que es **no mockeado, con `skipif` sobre `shutil.which("npx")`** — exactamente el test de integración que la ronda anterior pidió, y que cierra el gap de "la suite en verde no dice nada sobre si el render ocurre". Mermaid sigue 8/8 en `lecciones/`. **C3 sigue abierto:** `ls notebooks/ejecutados/` → **7 notebooks**, falta U8 (bloqueo ambiental de cat. 10). |
| 13. Benchmarking educativo externo | **1.6/2** | **Heredado sin re-verificación, sin cambios en este rango.** Sigue abierta solo la brecha (b), las sesiones "studio" — modalidad de aula, no artefacto del repo. |
| 14. Benchmarking multiagente de producción | **0.65/1** | **Heredado en estructura, y mi sexta generación adversarial vuelve a confirmar los dos huecos, ahora con evidencia por agente.** Inspeccioné `reports` en las variantes evasivas: **los 7 agentes devuelven `passed=True`** sobre un documento que conserva las tres falsedades estadísticas de N-01 más un `\boxed{}` desincronizado. (a) Sin juez de segunda pasada. (b) La precisión del Consejo sigue sin medirse contra corpus etiquetado — **N-08 es la cuarta evasión encontrada en cuatro rondas por construcción manual de adversarios**, exactamente el método que un corpus etiquetado sustituiría. |
| 15. Benchmarking literatura académica | **0.85/1** | **Heredado sin re-verificación.** `GOVERNANCE.md` no cambió en este rango. Comprobé que la fundamentación sigue presente (`:83-84` documenta el *kappa deflation* de 33.8–41.3 puntos) y que el descuento residual sigue vigente: `:139` y `:181` admiten que **el repo aún no mide su propio $\kappa$** ni su acuerdo con juicio humano. |

## Total: 96.4/100

Desglose aritmético verificado (sumado programáticamente, no a ojo):
`11.0 + 7.0 + 8.0 + 12.2 + 7.5 + 6.0 + 6.0 + 5.0 + 15.0 + 5.8 + 5.0 + 4.8 + 1.6 + 0.65 + 0.85` = **96.40**
Suma de pesos: `11 + 7 + 8 + 14 + 8 + 6 + 6 + 5 + 15 + 6 + 5 + 5 + 2 + 1 + 1` = **100**.
Delta contra la ronda anterior: `96.40 − 94.40` = **+2.00**. Puntos faltantes: `100 − 96.40` = **3.60**.

---

## Comparación con la auditoría de 94.4

| Cat | 94.4 (`fa11fed`) | Ahora (`b73931d`) | Δ | Qué cambió |
|---|---|---|---|---|
| 1 | 11.0/11 | **11.0/11** | 0.0 | Re-verificado: 8/8 en `score=100.0`. Ya completa. |
| 2 | 7.0/7 | **7.0/7** | 0.0 | Heredado; el rango no toca `lecciones/`. |
| 3 | 8.0/8 | **8.0/8** | 0.0 | ruff + black + isort re-ejecutados, los tres verdes. |
| 4 | 12.0/14 | **12.2/14** | **+0.2** | N-05 cerrado y reproducido por mí; 12→**16** adversariales con control negativo; 291/291. **Pero N-08 (nuevo, ALTO): cuarta evasión, 3 vectores independientes.** |
| 5 | 7.5/8 | **7.5/8** | 0.0 | Heredado; 32 ejercicios re-contados. |
| 6 | 5.6/6 | **6.0/6** | **+0.4** | **B1' cerrado**: gate de CI real contra `--collect-only`, simulado por mí (`291 == 291`). Test local conservado y documentado como complementario. |
| 7 | 6.0/6 | **6.0/6** | 0.0 | 13 adversarios de ReDoS re-medidos, máx 0.48 s. Path traversal reforzado con 2 tests. `bandit` sigue ausente. |
| 8 | 5.0/5 | **5.0/5** | 0.0 | Re-contado: mayor módulo 549, margen 31%. |
| 9 | 14.0/15 | **15.0/15** | **+1.0** | **N-07 cerrado por encima de lo pedido**: 91 filas de inventario, corrige el conteo heredado a la baja (35 de 76 eran trazables) y recalcula los 93 desde cero. 91/92, 0 defectos. |
| 10 | 5.7/6 | **5.8/6** | **+0.1** | **I-5 cerrado** y con efecto medido: nbconvert ya no cae al Python del sistema. Bloqueo de torch reproducido y re-descartado como PATH/MKL. |
| 11 | 5.0/5 | **5.0/5** | 0.0 | Re-verificado: `gemini-3.5-flash`. |
| 12 | 4.5/5 | **4.8/5** | **+0.3** | **N-06 cerrado con la causa raíz real** (`shutil.which`, no "mmdc irresoluble"): **8 SVG en disco**, y **test de integración no mockeado pasa**. C3 sigue abierto (7/8). |
| 13 | 1.6/2 | **1.6/2** | 0.0 | Heredado. |
| 14 | 0.65/1 | **0.65/1** | 0.0 | Heredado. N-08 vuelve a confirmar ambos huecos, ahora con evidencia por agente (7/7 `passed=True`). |
| 15 | 0.85/1 | **0.85/1** | 0.0 | Heredado. $\kappa$ sigue sin medirse. |

**Salto neto: 94.4 → 96.4 (+2.00).** Trayectoria completa: **69.3 → 88.1 → 89.6 → 94.4 → 96.4**.

**Lectura honesta del +2.00.** Es la **segunda ronda consecutiva sin ninguna categoría en retroceso**, y la segunda mejor cifra de las cinco. Cinco categorías suben, diez se mantienen, ninguna baja. El plan presupuestaba **2.15 puntos por ~12 h de trabajo mecánico** y cobró **2.00 de ellos** — la predicción de la ronda anterior resultó casi exacta, lo que en sí mismo valida la granularidad de la rúbrica.

Lo más relevante no es el tamaño del salto sino **su composición**: las tres ganancias grandes (cat. 9 +1.0, cat. 6 +0.4, cat. 12 +0.3) son exactamente las tres cosas que la ronda anterior señaló como "entregas que quedaron a un paso" — el artefacto que no se escribió, el gate tautológico, el render que no renderizaba. **Las tres se cerraron, y dos de ellas por encima de lo pedido**: N-07 no solo escribió el inventario sino que auditó la cifra heredada y la corrigió a la baja; N-06 no solo arregló el render sino que añadió el test de integración no mockeado que hace la corrección verificable. Eso es respuesta a una auditoría, no cumplimiento de checklist.

El techo del salto está puesto por la misma dinámica de siempre: **N-08 es la cuarta evasión en cuatro rondas**, y por cuarta vez la encontró un auditor construyendo adversarios a mano.

---

## Categoría 4 en detalle

### 4.1 — N-05 cerrado, verificado ejecutando el pipeline

El fix adoptó la **opción 1 "barata"** que la ronda anterior recomendó, implementada con una decisión de diseño mejor que la sugerida: en vez de escribir una condición nueva ad hoc, **reutiliza `_operandos_distintivos`**, la misma heurística que ya separa "dato de un ejemplo" de "ruido sintáctico" en `_comparten_datos`. `_contraste_boxed.py:47-48`:

```python
tiene_marca = any(re.search(m, expresion) for m in _MARCAS_FORMULA_SIMBOLICA)
return tiene_marca and not _operandos_distintivos(expresion)
```

Los 16 adversariales pasan, corridos por mí hasta el final:

```
pytest tests/council/test_adversarial.py -v
  16 passed in 155.64s (0:02:35)
```

Pasaron de 12 a 16: las 3 variantes de N-05 (`test_v5_marca_simbolica_decorativa_con_valor_real_se_reporta`, `v5b_indice`, `v5c_integral`) **más un control negativo**, `test_formula_simbolica_genuina_sin_valor_sigue_excluida`. Ese cuarto test es el que importa: versiona la restricción de que el fix **no** puede romper U7 §6.2, en vez de solo probar que detecta lo que antes evadía.

Reproduje las 3 variantes yo mismo con el pipeline completo — **`approved=False`, con la discrepancia correcta**:

```
CONTROL_V5_sum_decorativo   approved=False  hallazgos=1  ['desajuste_ejemplo_salida']  (6.8s)
  engineer.discrepancias: [{'valor_declarado': 0.42, 'valores_producidos': [-1.5216, 0.1281]}]
```

Y verifiqué que **no introduce falso positivo sobre contenido real**: corrí `ContentAuditorAgent` sobre las 8 unidades (**8/8 `score=100.0`**) y extraje todos los `\boxed{}` del curso que contienen marca simbólica. Hay exactamente uno, y sigue protegido:

```
UNIDAD_7_INFERENCIA_ES:1189  simbolica=True  ops=[]
  \boxed{\hat{\mu}_{MLE} = \bar{X} = \frac{1}{n}\sum_{i=1}^n X_i}
```

**N-05 cerrado, con mis propios ojos, sin regresión.**

### 4.2 — Sexta generación adversarial: N-08

Leí el fix y ataqué **la compuerta nueva**, `not _operandos_distintivos(expresion)`. Su docstring (`_contraste_boxed.py:38-42`) dice explícitamente que reutiliza esa función "que ya descarta índices/límites de sumatoria pequeños (`abs<=10`)". Esa es precisamente la superficie: **si el descarte de enteros pequeños es lo que protege a U7 §6.2, entonces un `\boxed{}` cuyo valor *sea* un entero pequeño hereda esa protección**.

Aislamiento a nivel de función, con `salida = "z = -1.5216, p = 0.1281\n"`:

```
caso                                       simbolica  operandos    apunta   veredicto
V3 puro (theta, control)                   False      [0.42]       False    DETECTA
V5 sum decorativo (N-05, ya cerrado)       False      [0.42]       False    DETECTA
V6a sum + entero pequeno (7)               True       []           False    >>> EVADE
V6b sum + entero pequeno (9)               True       []           False    >>> EVADE
V6c int + entero pequeno (5)               True       []           False    >>> EVADE
V6d sum + entero 10 (limite)               True       []           False    >>> EVADE
V6e sum + entero 11 (fuera limite)         False      [11.0]       False    DETECTA
V6f sum + valor dentro de \text{}          True       []           False    >>> EVADE
V6g sum + valor como exponente             True       []           False    >>> EVADE
V6h sum + frac no numerica                 False      [0.42]       False    DETECTA
```

**Tres vectores independientes**, no tres variantes del mismo:

1. **Entero ≤10** (V6a–V6d): `_operandos_distintivos` lo descarta por diseño (`:109`, `abs(float(n)) <= 10`). V6e confirma que el umbral es exactamente ese: con 11 el contraste vuelve a detectar.
2. **Valor dentro de `\text{}`** (V6f): `_limpiar_latex:59` borra `\text{...}` **entero, con su contenido**, antes de que `_NUMERO` busque. El valor desaparece del análisis.
3. **Valor como exponente** (V6g): `_limpiar_latex:69` borra `^{...}`. `10^{-3}` queda sin operandos.

Los vectores 2 y 3 son más interesantes que el 1: no dependen del umbral de 10, sino de que **`_operandos_distintivos` mira la expresión *después* de `_limpiar_latex`**, que está diseñada para descartar decoración — y cualquier cosa que esa función considere decoración se vuelve un escondite.

Confirmado extremo a extremo con `CouncilPipeline.process_content` sobre `_DOCUMENTO_ADAPTATIVO_N01`, cambiando **solo** el `\boxed{}` final:

```
CONTROL_V3_puro            approved=False hallazgos=1 ['desajuste_ejemplo_salida'] (7.4s)
CONTROL_V5_sum_decorativo  approved=False hallazgos=1 ['desajuste_ejemplo_salida'] (6.8s)
V6a_sum_entero_7           approved=True  hallazgos=0 []                           (7.1s)
V6d_sum_entero_10          approved=True  hallazgos=0 []                           (7.0s)
V6f_sum_valor_en_text      approved=True  hallazgos=0 []                           (0.3s)
V6g_sum_valor_exponente    approved=True  hallazgos=0 []                           (9.3s)
```

**Los dos controles bloquean; las cuatro variantes evaden.** Y verifiqué agente por agente que el pipeline corre completo (descartando que V6f evadiera por abortar temprano, dado su tiempo de 0.3 s):

```
--- V6a_entero_7_EVADE: approved=True ---   n_reports=7
    editor  passed=True | architect passed=True | scientist passed=True
    engineer passed=True  discrepancias=[]
    safety_gate passed=True | analyst passed=True | librarian passed=True

--- V6f_text_EVADE: approved=True ---       n_reports=7   (idéntico)
```

**7/7 agentes en verde** sobre un documento que conserva las tres falsedades estadísticas de N-01 más un `\boxed{}` desincronizado.

### 4.3 — Suite completa y calidad

```
pytest tests/ -q --tb=line
  291 passed, 381 warnings in 527.14s (0:08:47)     [exit code 0]
```

**291/291 en verde, corrida por mí hasta el final**, coincidiendo con `pytest --collect-only -q` → `291 tests collected` y con el badge. Las 381 advertencias son el mismo `PydanticDeprecatedSince211` de `chromadb` (dependencia de terceros). La suite pasó de 20:31 a 8:47 — no investigué la causa; no afecta puntaje.

### 4.4 — Puntaje de categoría 4: 12.2/14

**A favor (+0.2 sobre 12.0):** N-05 cerrado con reutilización de heurística existente en vez de condición ad hoc, y reproducido por mí; adversariales de 12 → 16 **incluyendo control negativo** de la restricción que el fix no debe romper; 291/291; cero falsos positivos sobre las 8 unidades reales, verificado extrayendo el único `\boxed{}` del curso con marca simbólica.

**En contra (los 1.8 que faltan):** **N-08** reabre la evasión por **tres vectores independientes**, dos de ellos sin relación con el umbral que el fix eligió; **7 de 7 agentes siguen sin detectar falsedad semántica**; **la precisión del Consejo sigue sin medirse** contra corpus etiquetado.

El +0.2 es deliberadamente modesto: el fix de N-05 es correcto y está bien hecho, pero el **patrón** —cuarta ronda, cuarta evasión, mismo método de descubrimiento— es evidencia acumulada de que el enfoque heurístico-por-parches tiene un techo, y la categoría no puede subir mucho más sin medición.

---

## Hallazgos nuevos

### N-08 — ALTO — Un valor que `_limpiar_latex` u `_operandos_distintivos` descartan desactiva el fix de N-05

**Severidad: ALTO** (misma que N-01, N-03 y N-05: acota lo que el repo puede afirmar sobre su verificador; el modelo de amenaza real sigue siendo desincronización accidental del profesor, no un adversario).

**Causa raíz:** `src/multiagent_core/council/_contraste_boxed.py:47-48` (`_es_formula_simbolica`), en conjunción con `_operandos_distintivos:106-110` y `_limpiar_latex:59,69`.

```python
tiene_marca = any(re.search(m, expresion) for m in _MARCAS_FORMULA_SIMBOLICA)
return tiene_marca and not _operandos_distintivos(expresion)
```

La segunda conjunción pregunta "¿hay algún operando numérico distintivo?". Pero `_operandos_distintivos` **no ve la expresión cruda**: la pasa antes por `_limpiar_latex`, y luego filtra enteros con `abs<=10`. Todo lo que cualquiera de esos dos pasos descarte es invisible para la compuerta, y por tanto es un escondite para un valor real.

**Reproducción exacta** (tres vectores, cualquiera basta):
1. Tomar `_DOCUMENTO_ADAPTATIVO_N01` de `tests/council/test_adversarial.py:163`.
2. Sustituir `$$\boxed{p = 0.42}$$` por **uno** de:
   - `$$\boxed{\hat{\theta} = \sum \; 7}$$` — entero ≤10
   - `$$\boxed{\hat{\theta} = \sum \; \text{0.4200}}$$` — valor dentro de `\text{}`
   - `$$\boxed{\hat{\theta} = \sum \; 10^{-3}}$$` — valor como exponente
3. `CouncilPipeline().process_content(doc, unit_name="ADV-GEN6")`.

**Resultado medido:** `approved=True`, `hallazgos: []`, **7/7 agentes `passed=True`**. Los controles V3 y V5 sobre el mismo documento dan `approved=False`.

**Por qué la exclusión existe y por qué aun así es un hueco.** Igual que en N-05, la exclusión no es gratuita: sin ella, `UNIDAD_7:1189` (`\boxed{\hat{\mu}_{MLE} = \bar{X} = \frac{1}{n}\sum_{i=1}^n X_i}`) da un falso positivo real, y lo verifiqué: ese `\boxed{}` tiene `ops=[]`, exactamente el mismo estado que mis adversarios V6a/V6d. **La protección legítima y el hueco son literalmente el mismo predicado.** Esa es la observación central de este hallazgo, y explica por qué cada fix de esta familia abre el siguiente: se está pidiendo a una prueba léxica que distinga intención.

**Cierre sugerido** (por coste creciente):
1. **Barato, pero ya se probó dos veces:** añadir una tercera condición (p. ej. exigir que la marca esté ligada a índice, `\sum_{...}^{...}`). Cierra V6a–V6d; **no cierra V6f ni V6g**, que no dependen del umbral. **Tres rondas de evidencia sugieren que esta vía no converge.**
2. **Medio — cambiar de léxico a estructural:** decidir si la expresión es simbólica por su **forma** (¿el `\sum` tiene índice y límites, y el cuerpo contiene variables libres?), no por presencia/ausencia de tokens. Cierra los tres vectores de una vez.
3. **Estructural — eliminar la exclusión:** en vez de excluir fórmulas simbólicas, **extraer el valor concreto cuando exista** y contrastarlo; para U7 §6.2 no hay valor concreto que extraer, así que la exclusión se vuelve innecesaria y la clase entera de evasión desaparece. Es el cierre que la ronda anterior ya listaba como opción 3 y sigue sin tomarse.
4. **Medición (la que de verdad cambia el juego):** corpus etiquetado. **Cuatro rondas, cuatro evasiones, cuatro veces el mismo método de descubrimiento manual.**

### I-6 — INFO — `GOVERNANCE.md` no registra N-05, N-06 ni N-07

`grep -n "N-05\|N-06\|N-07\|I-5" GOVERNANCE.md` → **ningún resultado**; solo aparece `I-3` (`:195`). Las rondas anteriores establecieron el patrón de declarar en `GOVERNANCE.md` los límites conocidos del Consejo (B2 se cerró justamente así), y ese patrón no se continuó para los tres hallazgos de este ciclo. N-05 en particular merece entrada propia: **la afirmación defendible sobre el verificador cambió** al cerrarlo, y `GOVERNANCE.md` es el lugar donde el repo documenta esas afirmaciones.

No descuenta en cat. 6 porque el descuento de esa categoría era el gate del badge, que sí se cerró, y porque los tres hallazgos están documentados con detalle en el código (docstrings de `_es_formula_simbolica`, `mermaid_renderer.py:32-36`, `notebook_compiler_agent.py:183-190`) y en el documento de recálculo. Es deuda de consolidación, no de transparencia. **Coste: ~30 min.**

**Nota sobre el bloqueo de U8 (no es hallazgo).** Verifiqué la afirmación del encargo por segunda ronda consecutiva y **sigue siendo correcta**: U8 falla con `OSError: [WinError 127] … Error loading "…\torch\lib\shm.dll"`. Re-descarté PATH/MKL (`import torch` → `2.13.0+cpu` OK en proceso directo y en subproceso limpio; falla solo en ipykernel). Ambiental, ajeno al contenido del curso, documentado como pendiente en vez de oculto. **Un matiz nuevo a favor del trabajo de este ciclo:** gracias a I-5, el fallo ahora ocurre **contra el kernel correcto sin flags** — antes, nbconvert caía al Python 3.13 del sistema y moría con `ModuleNotFoundError`, enmascarando el bloqueo real.

---

## Camino a 100/100

Faltan **3.60 puntos** (`100 − 96.40`). Los tamaños individuales suman exactamente 3.60 (verificado programáticamente).

### Bloque A — Infraestructura de agentes y su medición (1.80 pts: cat. 4)

| # | Descuento | Tamaño | Acción que lo cierra |
|---|---|---|---|
| A1'' | **N-08**: valor descartado por `_limpiar_latex`/umbral ≤10 desactiva el fix de N-05 | **0.35 pts** | **No parchear una cuarta vez.** Ir directo a la opción 3: extraer el valor concreto cuando exista en vez de excluir. Añadir los 3 vectores a `test_adversarial.py` + control negativo sobre U7:1189. **Coste: ~5 h.** |
| A2 | **Ningún agente detecta falsedad semántica**: 7/7 aprueban "la binomial tiene varianza $n$" | **0.95 pts** | Techo de diseño. Requiere `@Scientist` con LLM o base de invariantes mucho más amplia. **Coste: ~20-30 h**, decisión de arquitectura. |
| A3 | **Precisión del Consejo sin medir** contra corpus etiquetado | **0.50 pts** | ~50 documentos etiquetados, correr el Consejo, publicar precisión/recall/$\kappa$. Cierra además D5 y vuelve A2 cuantificable. **Coste: ~15 h. Sigue siendo la acción de mayor apalancamiento, ahora con cuatro rondas de evidencia a favor.** |
| | **Subtotal A** | **1.80** = déficit exacto de cat. 4 | |

### Bloque B — Presentación y experiencia (0.40 pts: cat. 12 + 10)

| # | Descuento | Tamaño | Acción que lo cierra |
|---|---|---|---|
| C3 | **U8 sin copia ejecutada** (7/8 en `notebooks/ejecutados/`) | **0.20 pts** en cat. 12 | Bloqueado por torch/ipykernel en Windows. **Vía viable: ejecutar en CI (Linux)**, donde el conflicto de DLL no existe. **Coste: ~2 h.** |
| C4'' | **U8 no re-ejecutado con nbconvert** | **0.20 pts** en cat. 10 | Mismo bloqueo; lo cierra C3. I-5 ya está cerrado, así que el único obstáculo restante es ambiental. |
| | **Subtotal B** | **0.40** | |

### Bloque C — Contenido, ejercicios y benchmarking (1.40 pts)

| # | Descuento | Tamaño | Acción que lo cierra |
|---|---|---|---|
| D3' | **Hardcodear el literal correcto sigue aprobando** ejercicios | **0.50 pts** en cat. 5 | Límite inherente; mitigable exigiendo variables intermedias verificables. **Coste: ~4 h**, parcial. |
| D4 | **Sesiones "studio" ausentes** | **0.40 pts** en cat. 13 | **No recuperable por trabajo en el repositorio** (modalidad de aula presencial). |
| D5 | **Sin juez de segunda pasada** | **0.35 pts** en cat. 14 | Lo cierra **A3**. |
| D6 | **$\kappa$ sin medir**; fundamentación solo en `GOVERNANCE.md` | **0.15 pts** en cat. 15 | Referenciar las 4 fuentes desde README y U1/U8. El $\kappa$ lo cierra A3. **Coste: ~2 h.** |
| — | *(higiene sin puntos: I-6 registrar N-05/06/07 en `GOVERNANCE.md`, `bandit` sin instalar, deuda I-3, CI no lintea `tests/`)* | 0.00 | Recomendado igualmente. |
| | **Subtotal C** | **1.40** | |

**Verificación aritmética** (sumada programáticamente): `A 1.80 + B 0.40 + C 1.40` = **3.60** = `100 − 96.40` ✅. Déficit por categoría, que es la fuente de verdad:

| Cat | Peso | Obtenido | Déficit |
|---|---|---|---|
| 1 | 11 | 11.0 | 0.00 |
| 2 | 7 | 7.0 | 0.00 |
| 3 | 8 | 8.0 | 0.00 |
| 4 | 14 | 12.2 | **1.80** |
| 5 | 8 | 7.5 | **0.50** |
| 6 | 6 | 6.0 | 0.00 |
| 7 | 6 | 6.0 | 0.00 |
| 8 | 5 | 5.0 | 0.00 |
| 9 | 15 | 15.0 | 0.00 |
| 10 | 6 | 5.8 | **0.20** |
| 11 | 5 | 5.0 | 0.00 |
| 12 | 5 | 4.8 | **0.20** |
| 13 | 2 | 1.6 | **0.40** |
| 14 | 1 | 0.65 | **0.35** |
| 15 | 1 | 0.85 | **0.15** |
| | **100** | **96.40** | **3.60** ✅ |

Reparto por causa concreta:

- **Cat. 4 (agentes):** 1.80 — N-08 0.35, A2 0.95, A3 0.50
- **Cat. 5 (ejercicios):** 0.50 — hardcodeo, límite inherente
- **Cat. 13 (benchmark educativo):** 0.40 — **no recuperable en el repo**
- **Cat. 14 (juez 2ª pasada):** 0.35 — lo cierra A3
- **Cat. 10 (end-to-end):** 0.20 — U8 con nbconvert (ambiental)
- **Cat. 12 (presentación):** 0.20 — U8 ejecutado (ambiental)
- **Cat. 15 (literatura):** 0.15 — referencias + $\kappa$ (A3)
- **Total: 3.60** ✅

### Resumen del camino

| Prioridad | Puntos | Coste | Carácter |
|---|---|---|---|
| **U8 vía CI (Linux)** — cierra C3 + C4'' de una vez | **0.40** | ~2 h | **Mejor relación punto/hora del ciclo.** Único ítem puramente mecánico que queda. |
| A3 (corpus etiquetado) | **0.50** directos | ~15 h | **Mayor apalancamiento: además desbloquea D5 (0.35) y D6 (0.15)** |
| D5 (juez de 2ª pasada) | **0.35** | incluido en A3 | Depende de A3 |
| N-08 por la vía estructural | **0.35** | ~5 h | Accionable, **pero no por parcheo** |
| D6 (referencias + $\kappa$) | **0.15** | ~2 h | Parcialmente vía A3 |
| D3' (hardcodeo) | **0.50** | ~4 h | Parcial, límite inherente |
| A2 (falsedad semántica) | **0.95** | ~20-30 h | Decisión de arquitectura |
| D4 (sesiones studio) | **0.40** | — | **No recuperable por trabajo en el repo** |
| **Total** | **3.60** | **~48 h** | **Techo real alcanzable ≈ 99.6/100** |

**Tres conclusiones:**

1. **El techo honesto sigue siendo 99.6/100** — D4 (0.40, modalidad de aula presencial) no es un artefacto versionable. Invariante por tercera ronda.
2. **El trabajo mecánico se acabó.** La ronda anterior tenía 2.15 puntos disponibles por ~12 h de trabajo sin arquitectura; se cobraron 2.00 de ellos. **Lo que queda son 0.40 puntos mecánicos (U8 vía CI) y 3.20 que requieren decisiones de diseño o no son recuperables.** Este es el cambio cualitativo más importante de esta ronda: el repo agotó su deuda barata.
3. **A3 deja de ser "la acción de mayor apalancamiento" para ser la única vía restante en cat. 4.** Cuatro rondas, cuatro evasiones (N-01, N-03, N-05, N-08), las cuatro encontradas por un auditor construyendo adversarios a mano, cada fix correcto y verificado, cada uno abriendo el siguiente. **N-08 añade la evidencia que faltaba para cerrar el argumento:** sus vectores V6f y V6g no dependen del umbral que el último fix eligió, así que un quinto parche sobre ese umbral no los cerraría. La pregunta ya no es si el corpus etiquetado vale 15 h, sino cuántas rondas más de parcheo se quieren pagar antes.

---

## Lectura honesta de la cifra

**96.4/100 es la mejor cifra de las cinco rondas, y la segunda consecutiva sin ninguna categoría en retroceso.** El plan `cierre-n05-n06-n07` hizo lo que dijo, y en dos de sus cinco entregas hizo **más** de lo que dijo.

Tres cosas merecen crédito explícito, y las tres son de la misma naturaleza: **respuesta a una auditoría, no cumplimiento de un checklist**.

**La primera es N-07.** La tarea pedía escribir el inventario de los 93 `\boxed{}`. El documento entregado hace eso y además **audita la cifra que iba a heredar**: descubre que de los 76 "recalculados" de rondas previas, solo 35 tenían evidencia citable con archivo:línea, y en vez de aceptar el conteo agregado **recalcula los 93 desde cero**. De paso corrige el inventario mismo (93 literales → 92 de contenido; `U6:316` era un comentario de código). Un documento que se encarga de que su propia afirmación sea más débil de lo que podría haber reclamado es exactamente lo que hace creíbles a los demás números de este repo.

**La segunda es N-06.** La ronda anterior diagnosticó la causa como "`mmdc` no resolvible como ejecutable". Eso era incorrecto, y el fix lo dice: la causa era que Python no resuelve `npx`→`npx.cmd` sin `shell=True`. **El trabajo corrigió a su auditor**, con el diagnóstico correcto y la evidencia (8 SVG reales en disco, de 15 a 33 KB). Y añadió el test de integración no mockeado con `skipif` —lo único que convierte "el código es correcto" en "el render ocurre"—, que corrí y pasa.

**La tercera es el manejo de B1'.** Habría sido fácil reemplazar el test local tautológico por el gate de CI y declarar el problema resuelto. En vez de eso, **conservó ambos y documentó en el propio test por qué el local sigue siendo tautológico y qué cubre cada uno**. Esa es la misma disciplina que ya se vio en `test_v3_variante_rotulo_ausente_con_dos_boxed_sigue_sin_detectarse`: versionar el límite en vez de silenciarlo.

Lo que impide más es, por primera vez en cinco rondas, **casi todo de la misma clase**. No hay ya entregas a medio camino ni artefactos prometidos y no escritos: los tres que la ronda anterior señaló están cerrados y verificados ejecutando. Quedan **N-08**, que es la cuarta iteración de un patrón conocido; **A2/A3**, que son decisiones de arquitectura; **0.40 de bloqueo ambiental** con una vía de salida clara (CI en Linux); y **0.40 que no son recuperables** por trabajo en el repositorio.

Sobre N-08 conviene ser preciso, porque su lectura correcta no es "otro bug". El fix de N-05 es **bueno**: eligió reutilizar `_operandos_distintivos` en vez de inventar una condición ad hoc, lo que es la decisión de diseño correcta. El problema es que esa función **ya servía para proteger a U7 §6.2**, y usarla también como compuerta hace que **la protección legítima y el hueco sean el mismo predicado**: verifiqué que `UNIDAD_7:1189` produce `ops=[]`, idéntico estado que mis adversarios V6a y V6d. No hay forma de cerrar uno sin tocar el otro mientras la decisión se tome léxicamente. Por eso el cierre sugerido no es un cuarto parche sino la opción estructural que lleva dos rondas en la mesa.

La afirmación defendible sobre el Consejo se afina una cuarta vez. Tras N-05 se podía decir: "detecta desincronización numérica de un `\boxed{}` único, salvo que sea una fórmula simbólica genuina". N-08 añade la cláusula: **…donde "genuina" significa, operativamente, que ningún número sobreviva a `_limpiar_latex` y al umbral de 10 — de modo que un valor real escondido en `\text{}`, en un exponente, o simplemente menor que 11, cuenta como genuina.** Es más estrecho de lo que el repo cree tener, por cuarta vez consecutiva, y por cuarta vez lo reveló un adversario construido a mano. **Ese patrón, y no las evasiones individuales, es el hallazgo real de esta ronda.**

### Declaración de alcance: qué ejecuté y qué heredé

**Ejecutado por mí en HEAD `b73931d`** (nada acreditado por lectura del diff):

| Verificación | Resultado |
|---|---|
| Suite completa `pytest tests/ -q --tb=line` | **291 passed, exit 0** (8:47) |
| `pytest --collect-only -q` vs badge `README.md:7` | **291 = 291** ✅ |
| **Simulación literal del step B1' de CI** | `REAL=291 BADGE=291` → **`Badge OK`** ✅ |
| `pytest tests/council/test_adversarial.py -v` | **16 passed** (2:35), eran 12 |
| **3 controles de N-05 por el pipeline completo** | **`approved=False`** con `desajuste_ejemplo_salida` — **N-05 cerrado** ✅ |
| **10 adversarios de sexta generación, construidos por mí (aislamiento)** | **6/10 evaden**, 3 vectores independientes → **N-08** |
| **4 adversarios de sexta generación e2e por el pipeline** | **4/4 `approved=True, hallazgos=0`** |
| Inspección de `reports` en las variantes evasivas | **7/7 agentes `passed=True`** — descarta aborto temprano |
| Control de falso positivo: `\boxed{}` reales con marca simbólica | **1 en todo el curso** (`U7:1189`), sigue protegido (`ops=[]`) |
| `ContentAuditorAgent.audit_content` × 8 unidades | **8/8 `score=100.0`, `passed=True`** |
| `pytest tests/test_mermaid_renderer.py -v` | **9 passed** — incluye `test_integracion_real_genera_svg_en_disco` (**no mockeado**) ✅ |
| `ls -la docs/images/*.svg` + tamaños | **8 SVG**, 14 980–32 724 bytes — **N-06 cerrado** ✅ |
| `metadata.kernelspec` × 8 notebooks | **8/8 declaran `python3`** — **I-5 cerrado** ✅ |
| `jupyter nbconvert --execute` sobre U8 (sin flag de kernel) | llega al kernel correcto; **`OSError WinError 127 shm.dll`** |
| `import torch` directo / subproceso limpio | **`2.13.0+cpu` OK en ambos** — el fallo es exclusivo de ipykernel |
| **13 adversarios de ReDoS sobre la superficie de regex** | **máx 0.4802 s @ 200k chars**, todo lineal — sin patológico |
| `ruff` · `black --check` · `isort --check-only` sobre `src/ tests/` | los tres en verde (52 archivos) |
| `wc -l` de todos los módulos de `src/` | mayor: `stats_tutor_agent.py` **549**; `_contraste_boxed.py` 358; total 4 691 |
| Documento de recálculo N-07: existencia + estructura | **existe**, **91 filas de inventario**, 8 secciones por unidad ✅ |
| `grep -c '^```mermaid'` × 8 unidades · ejercicios · `%%writefile` | **8/8** · **1/unidad** · **4/unidad** (32 evaluables) |
| `wc -l lecciones/UNIDAD_*.md` | **10 069 líneas** |
| `ls notebooks/ejecutados/` | **7 notebooks** — falta U8 (C3 abierto) |
| `MODEL_NAME` en `stats_tutor_agent.py:58` | **`gemini-3.5-flash`** ✅ |
| `git rev-list --left-right --count origin/master...master` · `git status` | **`0	0`** · working tree limpio ✅ |
| `grep -n "N-05\|N-06\|N-07\|I-5" GOVERNANCE.md` | **ningún resultado** → **I-6** |

**Heredado explícitamente de la auditoría de 94.4, sin re-verificación** (el rango de commits no toca sus artefactos): categorías **2, 13, 15**, y la estructura de la **14** (aunque mi sexta generación sí re-confirmó sus dos huecos con evidencia nueva por agente).

**No verificado, declarado como tal:** `bandit` sigue sin estar instalado en `ia_stats` (`No module named bandit`). No investigué por qué la suite bajó de 20:31 a 8:47.

**96.4/100 es una cifra ganada y defendible.** Los 3.6 que faltan se reparten entre **0.40 mecánicos** (U8 vía CI en Linux), **1.00 que dependen de medir el Consejo** en vez de estimarlo (A3 0.50 + D5 0.35 + D6 0.15), **0.35 de N-08** por la vía estructural, **0.95 que son una decisión de arquitectura** (A2), **0.50 de un límite inherente** al verificador de ejercicios, y **0.40 que no son recuperables** por trabajo en el repositorio. Por primera vez en cinco rondas, **el repo no tiene deuda barata pendiente**.
