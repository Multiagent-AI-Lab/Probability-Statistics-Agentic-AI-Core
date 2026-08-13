# Diseño: Hard-Gate de Compilación + Soporte para 8 Unidades

## Contexto

`PLAN_CORRECCION_INTEGRAL.md` (raíz del repo) diagnosticó que el pipeline de agentes
(`src/multiagent_core/`) audita y critica el contenido pedagógico pero nunca bloquea
la compilación: `OrchestratorAgent.run_full_pipeline()` genera el `.ipynb` de cada
lección sin mirar `approved`. Las 4 preguntas abiertas del plan ya se resolvieron
(ver sección "Preguntas Abiertas — Resueltas" en ese mismo archivo) y eso implica
pasar de 7 a 8 unidades:

| Nueva | Contenido |
|---|---|
| U1 | Estadística Descriptiva |
| U2 | Probabilidad, Conjuntos y Combinatoria (reescrita desde cero) |
| U3 | Variables Aleatorias Discretas |
| U4 | Distribuciones Conjuntas |
| U5 | Variables Aleatorias Continuas |
| U6 | Modelado y Simulación (nueva — sección 10 de la U5 actual + material de `raw_student_notebooks/profesor/modelado_simulacion/`) |
| U7 | Inferencia y Estimación |
| U8 | Proyecto Integrador |

Este spec cubre exclusivamente el ajuste del **pipeline de agentes** para que:
(A) soporte 8 unidades sin romperse, y (B) tenga un hard-gate real que pueda
bloquear la compilación cuando el contenido de una unidad tiene anacronismos
curriculares críticos. **No** cubre la reescritura de contenido de U2/U5/U6 en sí
(eso es la Fase 1/4 del plan de corrección, trabajo aparte).

## Objetivo

Que el pipeline pueda ejecutarse ahora mismo (mientras el contenido viejo de U2
y U5 todavía no se ha reescrito) sin romper nada, y que quede listo para exigir
el hard-gate en cuanto la Fase 1 de contenido esté terminada — sin tener que
tocar el pipeline otra vez.

## Componentes a modificar

### 1. `src/multiagent_core/council/safety_gate_agent.py`

- `unit_forbidden_terms`: extender de `"UNIDAD 1"`..`"UNIDAD 5"` a `"UNIDAD 1"`..`"UNIDAD 8"`,
  con los términos prohibidos por unidad según la tabla de renumeración (p. ej. "Prueba UMP",
  "Error Tipo I", "ANOVA" siguen prohibidos hasta U7; en U6 — Modelado y Simulación —
  no aplican las mismas prohibiciones porque el tema es distinto, se define su propia
  lista si hace falta).
- Nuevo diccionario `unit_required_terms: Dict[str, List[str]]`: términos que deben
  aparecer en el texto para que la unidad sea temáticamente coherente con su nombre.
  Ejemplo: `"UNIDAD 2": ["combinatoria", "bayes", "axioma"]` (al menos uno presente,
  no los tres).
- `validate_assumptions(...)` gana una clave nueva en el dict de retorno:
  `"critical": bool` — `True` si hay anacronismos de secuencia curricular
  (`unit_forbidden_terms`) o mismatch temático (`unit_required_terms` ausente por
  completo). Los warnings de supuestos estadísticos (Shapiro, Levene, etc.) NO son
  críticos — siguen siendo solo informativos, no bloquean.

### 2. `src/multiagent_core/council/layout_editorial_agent.py`

- Nuevo método `detect_duplicate_blocks(lessons: Dict[str, str]) -> List[Dict[str, Any]]`:
  - Recibe `{nombre_unidad: texto_markdown}` de todas las lecciones.
  - Fingerprint por bloque (párrafo delimitado por líneas en blanco o sección `##`),
    no solo los primeros N tokens — así cubre tanto el caso cross-unit (intro SciPy
    idéntica en U1/U6 actuales) como el caso intra-archivo ya confirmado en la
    U4 actual (sección "5.3 PMF y PDF Condicionales" duplicada dos veces dentro
    del mismo archivo, líneas ~650 y ~946).
  - Hash normalizado (whitespace colapsado, minúsculas) de cada bloque ≥40 palabras
    para evitar falsos positivos en bloques triviales.
  - Retorna lista de `{"blocks_hash": ..., "locations": [(unidad, línea_inicio), ...]}`
    para cada hash con ≥2 ocurrencias.
- `audit_layout(...)` no cambia su firma (sigue operando sobre un solo texto);
  el chequeo cross-unit se invoca aparte, desde el pipeline, con todas las
  lecciones cargadas.

### 3. `src/multiagent_core/notebook_compiler_agent.py`

- Extender `_sanitize_text()`:
  - Regex `(?<!\\)\bar\{([A-Za-z])\}` → `\\bar{\1}` (corrige `ar{X}` sin backslash
    sin tocar `\bar{X}` ya correcto).
  - Regex `\$\$\\mathbf\{([^}]*)\}\$\$` → `$\\mathbf{\1}$` (bloque display de solo
    negrita → inline).
  - Typos puntuales confirmados en U7: `\ilde{` → `\tilde{`, `\lpha` → `\alpha`
    (con cuidado de no tocar `alpha=` de matplotlib — el regex exige el backslash
    literal `\lpha`, que no aparece en llamadas de Python).

### 4. `src/multiagent_core/content_auditor_agent.py`

- Endurecer el check `"Contexto Nanotecnológico"`: hoy es un booleano de substring
  (`any(term in text.lower() ...)`). El propio `mandatory_components` promete
  "Contexto Nanotecnológico (>=150 palabras)" pero nunca se mide longitud. Cambiar
  a: contar palabras del/los párrafo(s) que contienen los términos nano y exigir
  ≥150 palabras totales, igual que ya hace `"Teoría Completa"` con las 800 palabras
  globales.
- El resto de checks de `ContentAuditorAgent` queda fuera de este spec (no forman
  parte del hard-gate; son informativos y su rediseño es un trabajo aparte si se
  decide abordarlo).

### 5. `src/multiagent_core/pedagogical_pipeline.py`

- `review_and_auto_fix_lesson(...)` propaga `critical_block: bool` en el resultado,
  derivado de `safety_critique["critical"]` y de si `detect_duplicate_blocks`
  encontró al menos una coincidencia que involucre esta unidad (ese chequeo cruzado
  se hace a nivel de pipeline completo, no por lección aislada — ver punto 6).

### 6. `src/multiagent_core/orchestrator_agent.py`

- `run_full_pipeline(enforce_gate: bool = True)`:
  - Carga todas las lecciones primero (para poder correr `detect_duplicate_blocks`
    cross-unit antes de procesar unidad por unidad).
  - Por cada unidad: si `enforce_gate=True` y el resultado combinado (`SafetyGateAgent`
    crítico, o duplicado detectado que la involucra) es bloqueante, **no** se llama a
    `compiler.compile_file(...)` para esa unidad; el resultado se marca
    `"gate_blocked": True` con el motivo, y el `.ipynb` existente (si lo hay) queda
    intacto sin tocar.
  - Si `enforce_gate=False`, comportamiento actual (compila siempre), para permitir
    seguir generando notebooks mientras la Fase 1 de contenido está en curso.

### 7. `run_pedagogical_editorial_autofix.py`

- Antes de sobrescribir cada `lecciones/*.md`: copiar el archivo original a
  `lecciones/.backup/<archivo>.<timestamp>.md` (usando `shutil.copy2`, timestamp
  formato `YYYYMMDD_HHMMSS`). `.backup/` se agrega a `.gitignore`.
- Llama a `OrchestratorAgent(...).run_full_pipeline(enforce_gate=False)` explícitamente,
  con un comentario indicando que se cambia a `True` (o se quita el argumento, ya
  que `True` es el default) cuando la Fase 1 de reescritura de contenido (U2, U5→U5+U6)
  esté terminada.

## Fuera de alcance

- Reescritura de contenido de U2, división de U5/U6, purga de términos de hipótesis
  en U1/U3/U5, corrección masiva de LaTeX en el cuerpo de las lecciones (eso corre
  el `_sanitize_text()` mejorado solo en el momento de compilar, no reescribe los
  `.md` fuente retroactivamente salvo que se ejecute el autofix sobre ellos).
- Rediseño completo de `ContentAuditorAgent` más allá del check de contexto nano.
- Integración del material de `raw_student_notebooks/profesor/modelado_simulacion/`
  dentro de la nueva U6 (contenido, no pipeline).

## Riesgo identificado en tests existentes

`tests/test_pedagogical_pipeline.py::test_pedagogical_review_pipeline` usa una
lección de prueba etiquetada `"Unidad 1 Test"` que contiene "Prueba t de Student"
y "Shapiro-Wilk" — términos que hoy están en `unit_forbidden_terms["UNIDAD 1"]`.
El test pasa hoy porque `unit_name="Unidad 1 Test"` no hace match exacto con
`"unidad 1"` dentro de `unit_name.lower()`... en realidad sí lo contiene como
substring, así que **ya debería estar fallando o el string no dispara el match
por estar en `lesson_text[:200]` en vez de en `unit_name`**. Verificar al
implementar; si con `critical=True` este test empieza a fallar, renombrar la
unidad de prueba a algo neutro (`"Unidad Genérica Test"`) en vez de relajar el
gate.

## Testing

- `tests/council/test_council_pipeline.py` — sin cambios de fondo, verificar que
  sigue pasando con las nuevas reglas de `SafetyGateAgent`.
- `tests/test_pedagogical_pipeline.py` — ajustar el caso de riesgo señalado arriba;
  añadir caso donde `critical_block=True` se propaga correctamente.
- Nuevo: `tests/council/test_safety_gate_8_unidades.py` (o extender el archivo
  existente de SafetyGate si existe) — parametrizado sobre las 8 unidades,
  verificando `unit_forbidden_terms` y `unit_required_terms`.
- Nuevo: test de `detect_duplicate_blocks` con dos casos reales conocidos
  (duplicado cross-unit sintético tipo intro U1/U6; duplicado intra-archivo
  tipo U4 5.3-5.4).
- Nuevo: test de `OrchestratorAgent.run_full_pipeline(enforce_gate=True)` que
  confirma que una unidad con anacronismo crítico no genera/actualiza su `.ipynb`,
  y que con `enforce_gate=False` sí lo hace (comportamiento actual preservado).
- Nuevo: test de backup en `run_pedagogical_editorial_autofix.py` (verificar que
  se crea el archivo en `.backup/` antes de sobrescribir).
