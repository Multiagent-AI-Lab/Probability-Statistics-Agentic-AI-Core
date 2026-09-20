"""
Subsistema de contraste texto↔ejecución: compara los `\\boxed{}` de una
lección contra la salida real del código que la acompaña.

Extraído de `engineer_agent.py` (que llegó a 767 líneas) para mantener
cada módulo enfocado en una responsabilidad. Funciones libres, no una
clase — ninguna usa estado de instancia.
"""

import re

# Prefijo literal de la única sintaxis de `\boxed{}` que el sistema
# reconoce (ver `_BOXED` en `engineer_agent.py`, que exige `\boxed{` sin
# espacio -- no `\boxed {`, `\fbox{}` ni otra macro equivalente). Se
# comparte como constante porque `_contradicho_por_prosa_inmediata` corta
# su ventana de búsqueda en la siguiente ocurrencia de este prefijo (Minor
# de revisión, 2026-09-18): si `_BOXED` se relaja en el futuro para
# tolerar una variante, este corte debe actualizarse en el mismo cambio o
# reabre el falso positivo 2 (ventana cruzando al siguiente `\boxed{}`)
# en silencio, sin que ningún test existente lo detecte.
_PREFIJO_BOXED = r"\boxed{"

# `\boxed{...}` con un nivel de anidamiento de llaves -mismo patrón que
# `_BOXED` en `engineer_agent.py`, duplicado aquí (no importado) porque
# `_contraste_boxed.py` no depende de ese módulo. Se usa para volver a
# aislar el CONTENIDO del `\boxed{}` a partir de `expresion_boxed` (que ya
# incluye la línea completa hasta el cierre), cuando hace falta decidir si
# ese contenido es un valor simple o un formato compuesto.
_BOXED_CONTENIDO = re.compile(r"\\boxed\{((?:[^{}]|\{[^{}]*\})*)\}")

# Número final de una expresión: el último numérico que aparece en el
# `\boxed{}`, que es el resultado (`P(X=2) = 190 \times 0.0025 \approx
# 0.18868` -> 0.18868).
_NUMERO = re.compile(r"-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?")

_TOLERANCIA_RELATIVA = 1e-3

# Marcas de fórmula simbólica genérica (con sumatoria/producto/integral),
# no un valor numérico concreto. N-03: relajar el emparejamiento a "un
# solo `\boxed{}` en la sección" sin esta exclusión reporta un falso
# positivo real sobre UNIDAD 7 §6.2
# (`\boxed{\hat{\mu}_{MLE} = \bar{X} = \frac{1}{n}\sum_{i=1}^n X_i}`):
# los dígitos `1`/`n` de la notación de sumatoria no son el valor que el
# código debe producir, y su presencia no debe activar una comparación
# directa contra `producidos`. Verificado ejecutando las 8 unidades
# reales con y sin esta exclusión.
_MARCAS_FORMULA_SIMBOLICA = (r"\\sum", r"\\prod", r"\\int", r"_\{[a-zA-Z]\s*=\s*1\}\^")


def _es_formula_simbolica(expresion: str) -> bool:
    """¿La expresión del `\\boxed{}` es una fórmula simbólica genérica,
    sin valor numérico concreto a contrastar?

    N-08 (auditoría 2026-09-14, cuarta evasión): la versión anterior
    reutilizaba `_operandos_distintivos` para esta pregunta, pero esa
    función descarta enteros <=10 y depende de `_limpiar_latex`, que ya
    había descartado `\\text{}` y exponentes antes de que el filtro de
    enteros viera nada -tres caminos para producir un falso "no hay
    valor concreto" cuando el ÚNICO valor de la expresión caía en uno de
    esos tres casos. El criterio nuevo pregunta directamente "¿hay un
    valor numérico declarado al final de la expresión?" vía
    `_valor_final_declarado`, sin pasar por esos descartes. Verificado
    contra el control negativo real (U7 §6.2, protegido) y los 3 vectores
    de evasión de N-08 (ya no evaden) -- ver
    `test_formula_simbolica_genuina_sin_valor_sigue_excluida` y
    `test_v6*` en tests/council/test_adversarial.py."""
    tiene_marca = any(re.search(m, expresion) for m in _MARCAS_FORMULA_SIMBOLICA)
    return tiene_marca and _valor_final_declarado(expresion) is None


def _limpiar_latex(expresion: str) -> str:
    """Quita los sufijos LaTeX que no son parte del valor (`\\text{nm}`,
    `^2`, `\\%`) para que `15.65\\ \\text{nm}^2` se lea como 15.65.

    `\\frac{a}{b}` se resuelve a su cociente: borrar la macro dejaría
    los dos enteros sueltos y el "último número" de `\\boxed{\\frac{2}{3}}`
    sería 3, no 0.667.
    """
    sin_texto = re.sub(r"\\text\{[^}]*\}", " ", expresion)
    sin_fracciones = re.sub(
        r"\\[dt]?frac\s*\{\s*(-?\d+(?:\.\d+)?)\s*\}\s*\{\s*(-?\d+(?:\.\d+)?)\s*\}",
        lambda m: (
            repr(float(m.group(1)) / float(m.group(2)))
            if float(m.group(2)) != 0
            else " "
        ),
        sin_texto,
    )
    sin_exponente = re.sub(r"\^\s*\{?-?\d+\}?", " ", sin_fracciones)
    return re.sub(r"\\[a-zA-Z]+", " ", sin_exponente)


def _limpiar_latex_conservando_marcas(expresion: str) -> str:
    """Variante de `_limpiar_latex` para `_valor_final_declarado`: conserva
    como candidatos el contenido de `\\text{}` y el valor de un exponente
    numérico en vez de descartarlos (N-08, auditoría 2026-09-14).

    El orden de las sustituciones importa: primero se resuelve el
    exponente NUMÉRICO (antes de tocar índices), luego se borra cualquier
    índice/límite de sumatoria SIN resolver (`_{i=1}`, `^n` con letra
    dentro -- notación de rango, no un valor), luego se resuelven
    fracciones puramente numéricas, y solo al final se borran las
    fracciones simbólicas restantes y las macros LaTeX sueltas. Hacerlo
    en otro orden deja escapar el índice de una sumatoria (`_{i=1}`) como
    un número suelto -- exactamente el bug que rompía el control negativo
    de U7 §6.2 en la primera versión de esta función.
    """
    sin_texto = re.sub(r"\\text\{([^}]*)\}", r" \1 ", expresion)
    con_exponente_resuelto = re.sub(
        r"(-?\d+(?:\.\d+)?)\s*\^\s*\{?(-?\d+(?:\.\d+)?)\}?",
        lambda m: repr(float(m.group(1)) ** float(m.group(2))),
        sin_texto,
    )
    # Patrón [^{}]*[a-zA-Z][^{}]* es seguro contra ReDoS: la clase [^{}]* no
    # puede solaparse consigo misma de forma ambigua porque excluye explícitamente
    # { y }, y no hay anidamiento de cuantificadores del mismo carácter. Probado
    # con inputs patológicos (200k caracteres sin llave, 5000 grupos sin letra) —
    # mantiene lineariedad, <20ms. Véase _ROTULO_INLINE (línea ~262-290) para
    # el mismo estándar de documentación de seguridad contra ReDoS en este archivo.
    sin_indices_simbolicos = re.sub(
        r"[_^]\{[^{}]*[a-zA-Z][^{}]*\}", " ", con_exponente_resuelto
    )
    sin_fracciones = re.sub(
        r"\\[dt]?frac\s*\{\s*(-?\d+(?:\.\d+)?)\s*\}\s*\{\s*(-?\d+(?:\.\d+)?)\s*\}",
        lambda m: (
            repr(float(m.group(1)) / float(m.group(2)))
            if float(m.group(2)) != 0
            else " "
        ),
        sin_indices_simbolicos,
    )
    sin_fracciones_simbolicas = re.sub(
        r"\\[dt]?frac\s*\{[^{}]*\}\s*\{[^{}]*\}", " ", sin_fracciones
    )
    return re.sub(r"\\[a-zA-Z]+", " ", sin_fracciones_simbolicas)


def _contiene_subindice_anidado(expresion: str) -> bool:
    """¿La expresión tiene un `[_^]{...}` con otro `{` sin cerrar dentro
    de sí mismo (subíndice/superíndice anidado, p.ej. `_{b_{c}}`)?

    `_ultimo_igual_de_asignacion` y `_limpiar_latex_conservando_marcas`
    asumen que un `[_^]{...}` no anida otro `{` dentro -- válido para las
    93 ocurrencias reales de `\\boxed{}` de las 8 unidades (verificado por
    grep, 0 casos de anidamiento), pero una violación silenciosa de esa
    asunción puede devolver un número incorrecto sin ninguna señal de
    alerta (encontrado en la revisión de M1, 2026-09-15: mismo modo de
    falla que M1 mismo, por otra vía). Esta función deja la violación
    explícita para que el llamador pueda degradar a `None` en vez de
    arriesgar un valor mal calculado.
    """
    profundidad = 0
    i = 0
    n = len(expresion)
    while i < n:
        ch = expresion[i]
        if profundidad == 0 and ch in "_^" and i + 1 < n and expresion[i + 1] == "{":
            profundidad = 1
            i += 2
            continue
        if profundidad > 0:
            if ch == "{":
                return True
            if ch == "}":
                profundidad -= 1
            i += 1
            continue
        i += 1
    return False


def _ultimo_igual_de_asignacion(expresion: str) -> int:
    """Índice del último `=` de asignación real en `expresion`, ignorando
    cualquier `=` que aparezca dentro de un subíndice/superíndice
    `[_^]{...}` (p.ej. el límite inferior de una sumatoria, `_{i=1}`, o
    un envoltorio de llave sin cerrar como `"$$\\boxed{...}"`).

    M1 (revisión final de rama, 2026-09-15): la versión anterior
    enmascaraba `[_^]{...}` reconstruyendo un relleno de `#` "de la
    misma longitud" antes de buscar el `=` -- pero el cálculo de esa
    longitud no restaba el carácter `_`/`^` inicial (ya reañadido por
    separado), así que cada subíndice/superíndice agregaba una `#` de
    más y desplazaba +1 el índice hallado por cada uno presente en la
    expresión. Aquí se recorre el string UNA sola vez llevando un flag
    de "dentro de un `[_^]{...}`", sin reconstruir ningún string
    intermedio cuya longitud pueda desincronizarse del original. Asume
    que `[_^]{...}` no anida otro `{` dentro -- ver
    `_contiene_subindice_anidado`, que el llamador consulta antes de
    confiar en este resultado.
    """
    ultimo = -1
    dentro_de_subindice = False
    i = 0
    n = len(expresion)
    while i < n:
        ch = expresion[i]
        if (
            not dentro_de_subindice
            and ch in "_^"
            and i + 1 < n
            and expresion[i + 1] == "{"
        ):
            dentro_de_subindice = True
            i += 2
            continue
        if dentro_de_subindice:
            if ch == "}":
                dentro_de_subindice = False
            i += 1
            continue
        if ch == "=":
            ultimo = i
        i += 1
    return ultimo


def _valor_final_declarado(expresion: str) -> float | None:
    """¿La expresión declara explícitamente un valor numérico al final, o
    termina en notación simbólica sin resolver?

    Parte la expresión en el último `=` de asignación real
    (`_ultimo_igual_de_asignacion`) y busca el último número en el
    fragmento resultante, tras limpiarlo con
    `_limpiar_latex_conservando_marcas`.

    Si la expresión viola la asunción de "sin subíndices anidados" que
    ambas funciones auxiliares comparten, degrada a `None` (Important,
    revisión de M1 2026-09-15) en vez de arriesgar un valor numérico mal
    calculado -- no hay ningún `\\boxed{}` real en las 8 unidades con esta
    forma, así que degradar aquí no descarta ningún caso de producción.
    """
    if _contiene_subindice_anidado(expresion):
        return None

    idx_igual = _ultimo_igual_de_asignacion(expresion)

    fragmento = expresion[idx_igual + 1 :] if idx_igual >= 0 else expresion
    limpio = _limpiar_latex_conservando_marcas(fragmento)
    numeros = _NUMERO.findall(limpio)
    if not numeros:
        return None
    return float(numeros[-1])


def _algun_valor_coincide(esperado: float, producidos: list) -> bool:
    """El valor declarado aparece en la salida, con tolerancia y
    admitiendo la forma porcentual (`\\boxed{0.1126\\ (11.26\\%)}` frente
    a un `print` de 0.1126, y viceversa)."""
    candidatos = [esperado, esperado / 100.0, esperado * 100.0]
    return any(
        _valores_coinciden(c, p, _TOLERANCIA_RELATIVA)
        for c in candidatos
        for p in producidos
    )


def _valores_coinciden(a: float, b: float, tol: float) -> bool:
    """Compara con tolerancia relativa: el texto redondea (0.3333) lo que
    el código imprime completo (0.3333333...)."""
    escala = max(abs(a), abs(b), 1.0)
    return abs(a - b) <= tol * escala


def _es_valor_trivial(valor: float) -> bool:
    """Valores que aparecen por casualidad en cualquier salida numérica
    (índices, exponentes, conteos pequeños) y por tanto no sirven ni
    como resultado a contrastar ni como evidencia de corroboración."""
    return abs(valor) <= 2 or (valor == int(valor) and abs(valor) <= 10)


def _operandos_distintivos(expresion: str) -> set:
    """Números que identifican un ejemplo concreto.

    Aquí se descartan solo los enteros pequeños (índices, exponentes,
    conteos), no los decimales: `0.35` es el dato de entrada que
    distingue el ejemplo de UNIDAD 6 §2.3, aunque sea menor que 1.
    """
    return {
        round(float(n), 4)
        for n in _NUMERO.findall(_limpiar_latex(expresion))
        if not (float(n) == int(float(n)) and abs(float(n)) <= 10)
    }


def _comparten_datos(expresion_texto: str, expresion_codigo: str) -> bool:
    """¿Las dos expresiones hablan del mismo cálculo?

    Se consideran el mismo si comparten algún dato de entrada no trivial
    (el mismo λ, la misma μ, el mismo tamaño de muestra) o si el rótulo
    de la cantidad coincide. Es el ancla que evita contrastar el
    resultado de un ejemplo contra el `\\boxed{}` de otro.
    """
    return bool(
        _operandos_distintivos(expresion_texto)
        & _operandos_distintivos(expresion_codigo)
    )


def _comparte_operando_calculado(expresion: str, numeros_de_la_unidad: list) -> bool:
    """¿El código produce algún operando *calculado* de esta fórmula?

    Solo cuentan los decimales con al menos 2 cifras tras el punto: son
    resultados intermedios de un cálculo (`156.5` no, `76.81` y
    `1.03297` sí), no enteros redondos que dos ejemplos distintos
    pueden compartir por casualidad.
    """
    for texto_numero in _NUMERO.findall(_limpiar_latex(expresion)):
        if "." not in texto_numero:
            continue
        if len(texto_numero.split(".")[1]) < 2:
            continue
        if _algun_valor_coincide(float(texto_numero), numeros_de_la_unidad):
            return True
    return False


# Confirmación/contradicción textual explícita: "Como <valor> < 0.05",
# "Con <valor> se rechaza...". Patrón real de las lecciones (UNIDAD_7 §1.7
# y §2.5): el autor repite en prosa normal el mismo número que acaba de
# encuadrar en `\boxed{}`, sin que el rótulo de la fórmula tenga que
# coincidir con nada. Solo dos ocurrencias en las 8 unidades reales con
# ESTE valor en la oración (verificado por barrido completo, 2026-09-18)
# -- raro pero real, y de bajo riesgo siempre que se exija que el valor
# esperado aparezca en ALGUNO de los números de la oración, no
# específicamente en el primero: "Como 40.5 > 15.725" (UNIDAD_1 §2.4) es
# el mismo patrón sintáctico pero compara el outlier contra el límite, no
# repite el propio `\boxed{}` en primera posición -- exigir el primer
# número ahí generaba un falso positivo real (visto en
# `test_contenido_real_correcto_sigue_aprobando`).
_CONFIRMACION_EN_PROSA = re.compile(
    r"\b(?:[Cc]omo|[Cc]on)\s+\$?(-?\d+(?:\.\d+)?)"
    # Hasta 40 caracteres de ruido tolerado entre el primer número y el
    # operador (unidades LaTeX: `\ \text{nm}`, `\%`, espacios de fórmula) --
    # acotado para no arriesgar backtracking sobre líneas largas, igual
    # disciplina que las demás cotas de este archivo (ver `_ROTULO_INLINE`).
    r"(?:.{0,40}?[<>=]{1,2}\s*\$?(-?\d+(?:\.\d+)?))?\b"
)

# Ventana de búsqueda tras el `\boxed{}`: la confirmación real ocurre en la
# oración inmediatamente siguiente (UNIDAD_7 §2.5 la tiene 2 líneas después
# por el salto de párrafo Markdown); no tiene sentido buscar arbitrariamente
# lejos, donde un "Como <número>" ya hablaría de otro ejemplo.
_VENTANA_CONFIRMACION_CHARS = 300


def _contradicho_por_prosa_inmediata(
    expresion_boxed: str, cuerpo: str, valor_declarado: float
) -> bool:
    """¿La oración inmediatamente posterior al `\\boxed{}` compara valores
    sin incluir en ninguna posición el propio valor declarado -evidencia
    de que el `\\boxed{}` se desincronizó de su propio texto, sin
    necesidad de ningún código-?

    Se exige que NINGUNO de los números capturados de la comparación
    coincida con `valor_declarado`: una oración como "Como 0.0108 < 0.05"
    solo tiene un número relevante (el 0.05 es el umbral fijo de la
    prueba, no el resultado), pero "Como 40.5 > 15.725" tiene el valor del
    `\\boxed{}` en la SEGUNDA posición -- exigir una posición fija
    reportaría un falso positivo sobre contenido correcto.

    Devuelve False también cuando no hay ninguna confirmación textual
    cercana (el patrón es raro): la ausencia de esta señal no es
    evidencia de nada, solo la presencia de una que contradice lo es.
    """
    idx = cuerpo.find(expresion_boxed)
    if idx == -1:
        return False
    inicio = idx + len(expresion_boxed)
    fin = inicio + _VENTANA_CONFIRMACION_CHARS
    # La ventana no debe cruzar el próximo `\boxed{}`: un "Como/Con <num>"
    # después de ese punto confirma o contradice AL SIGUIENTE ejemplo, no
    # a este -- sin este corte, UNIDAD_1 §2.4 (dos `\boxed{}` seguidos,
    # 1.35 y 15.725) generaba un falso positivo real sobre el primero
    # (visto en `test_contenido_real_correcto_sigue_aprobando`): su
    # ventana alcanzaba la confirmación "Como 40.5 > 15.725" del SEGUNDO
    # `\boxed{}`, cuyos números no tienen relación con el primero.
    proximo_boxed = cuerpo.find(_PREFIJO_BOXED, inicio)
    if proximo_boxed != -1:
        fin = min(fin, proximo_boxed)
    ventana = cuerpo[inicio:fin]
    m = _CONFIRMACION_EN_PROSA.search(ventana)
    if not m:
        return False
    valores_en_prosa = [float(g) for g in m.groups() if g is not None]
    return not any(
        _valores_coinciden(valor_declarado, v, _TOLERANCIA_RELATIVA)
        for v in valores_en_prosa
    )


# Operación aritmética de 2 operandos, justo antes del `=` que abre el
# `\boxed{}`: "13.70 - 12.35 = \boxed{1.35}", "20 \times 0.05 = \boxed{1.0}".
# Patrón real de las lecciones (UNIDAD_1 §2.4, UNIDAD_3 §3.5): un ejemplo
# analítico sin código propio y sin "Como/Con" en prosa, donde la propia
# expresión matemática ya contiene la operación completa.
#
# Deliberadamente estrecho -solo 2 operandos numéricos con un operador
# entre ellos, inmediatamente antes del `=` final-: un barrido de las 8
# unidades reales (2026-09-19) mostró que la mayoría de expresiones con
# `\boxed{}` tienen 3+ operandos, fracciones o formato compuesto
# ("0.86638 (86.64%)") que un evaluador de 2 operandos evalúa mal o no
# reconoce -y evaluar mal es peor que no evaluar, porque generaría un
# falso positivo sobre contenido correcto-. Ampliar el alcance (3+
# operandos, paréntesis) requeriría un evaluador aritmético real
# (sympy.sympify o similar) con su propio ciclo de TDD adversarial; no
# vale el riesgo solo para subir de 2 a 3 unidades cerradas.
#
# Important de revisión (python-reviewer, 2026-09-19): la primera versión
# de este patrón usaba `.search()` sin verificar qué había ANTES del
# match, así que sobre una expresión de 3+ operandos
# ("0.25 + 0.45 + 0.30 = \boxed{1.0}") matcheaba el SUFIJO
# ("0.45 + 0.30 ="), calculaba 0.75, y lo comparaba contra 1.0 como si
# fueran los únicos 2 operandos -falso positivo reproducido en aislamiento
# contra 4 secciones reales de UNIDAD_2 (todas con aritmética CORRECTA de
# 3+ operandos). No se manifestaba en A3-U solo porque esas 4 secciones
# tienen código ejecutable propio en el mismo bloque, y
# `check_code_implementation` nunca invoca este mecanismo en ese caso -una
# coincidencia del contenido actual, no una garantía de la función-.
#
# El fix vive en `_contradicho_por_aritmetica_propia`, no en el regex: tras
# encontrar el match, se verifica que el tramo ANTERIOR al operando
# izquierdo capturado no termine en un dígito, punto decimal, paréntesis
# de cierre NI OPERADOR ARITMÉTICO -evidencia de un tercer operando ahí-.
# El caso real es justo el del operador: en "0.25 + 0.45 + 0.30 =", el
# match de 2 operandos captura "0.45 + 0.30 =", y lo que queda antes es
# "...0.25 + " -termina en el operador "+ ", no en un dígito pegado-, así
# que la verificación debe cubrir ambas formas (dígito pegado O separado
# por un operador con espacios).
_OPERACION_DOS_OPERANDOS = re.compile(
    r"(-?\d+(?:\.\d+)?)\s*(\\times|\\cdot|[+\-*/])\s*(-?\d+(?:\.\d+)?)\s*=\s*$"
)

# Un dígito, punto, `)` o un operador aritmético justo antes del inicio
# del match -ignorando espacios- es evidencia de un operando adicional a
# la izquierda que el match de 2 operandos no cubre. Incluye
# `\times`/`\cdot` como palabras completas (no solo el primer carácter)
# porque terminan en letra, no en un símbolo de la clase de caracteres.
_OPERANDO_ADICIONAL_ANTES = re.compile(r"(?:[\d.)+\-*/]|\\times|\\cdot)\s*$")


def _contradicho_por_aritmetica_propia(
    expresion_boxed: str, valor_declarado: float
) -> bool:
    """¿La propia expresión que precede al `\\boxed{}` ya contiene una
    operación de 2 operandos cuyo resultado no coincide con el valor
    declarado -evidencia interna a la línea, sin necesidad de código ni
    de otra oración-?

    Solo actúa cuando el patrón es inequívoco: exactamente 2 operandos
    numéricos (sin variables, sin fracciones, sin paréntesis) inmediatamente
    antes del `=` que abre el `\\boxed{}`, Y el contenido del `\\boxed{}`
    tiene un único número (no un formato compuesto). Cualquier otra forma
    (3+ operandos, `\\frac{}`, subíndices, o `\\boxed{0.86638 (86.64\\%)}`
    con dos números) no se evalúa -devuelve `False`-, para no arriesgar un
    falso positivo sobre una expresión que este evaluador simple
    interpretaría mal.

    Falso positivo real encontrado por el gate adversarial (2026-09-19,
    `neg_u5_variables_continuas.md`, sin alterar): `\\boxed{0.86638 \\quad
    (86.64\\%)}` tiene DOS números -el valor y su versión en porcentaje-;
    `valor_declarado` (extraído por el llamador como "el último número")
    era 86.64, pero la operación real (0.93319 - 0.06681) da 0.86638 -el
    PRIMER número, no el último-. El evaluador comparaba correctamente su
    propio cálculo contra el número equivocado. Exigir un único número
    dentro del `\\boxed{}` excluye este caso por completo, en vez de
    intentar adivinar cuál de los dos números es "el correcto".

    Segundo falso positivo real (revisión de `python-reviewer`, 2026-09-19):
    sobre una expresión de 3+ operandos ("0.25 + 0.45 + 0.30 = \\boxed{1.0}",
    UNIDAD_2 §1.3), el patrón de 2 operandos matcheaba el SUFIJO
    ("0.45 + 0.30 =") ignorando que había un tercer operando más a la
    izquierda -reportando 0.75 != 1.0 sobre aritmética correcta-. Se
    verifica ahora que nada preceda al operando izquierdo del match salvo
    espacio (ver `_OPERANDO_ADICIONAL_ANTES`): un dígito, punto o `)`
    justo antes es evidencia de ese tercer operando.
    """
    contenido_boxed_match = _BOXED_CONTENIDO.search(expresion_boxed)
    if contenido_boxed_match is None:
        return False
    numeros_en_boxed = _NUMERO.findall(contenido_boxed_match.group(1))
    if len(numeros_en_boxed) != 1:
        return False

    izquierda = expresion_boxed.rpartition(_PREFIJO_BOXED)[0]
    m = _OPERACION_DOS_OPERANDOS.search(izquierda)
    if not m:
        return False
    if _OPERANDO_ADICIONAL_ANTES.search(izquierda[: m.start()]):
        return False
    a, operador, b = float(m.group(1)), m.group(2), float(m.group(3))
    if operador in ("+",):
        calculado = a + b
    elif operador in ("-",):
        calculado = a - b
    elif operador in ("*", r"\times", r"\cdot"):
        calculado = a * b
    elif operador == "/":
        if b == 0:
            return False
        calculado = a / b
    else:
        return False
    return not _valores_coinciden(calculado, valor_declarado, _TOLERANCIA_RELATIVA)


def _contrastar_contra_la_unidad(
    titulo: str,
    esperados: list,
    salida_de_la_unidad: str,
    discrepancias: list,
    cuerpo: str = "",
) -> None:
    """Contrasta los `\\boxed{}` de una sección sin código propio contra
    la salida de toda la unidad.

    El criterio es la ausencia: un ejemplo analítico correcto termina en
    un número que el código de la unidad también produce (la media
    calculada a mano en §2.2 es la que §4 imprime como `Media: 15.6500`).
    Si ese valor no aparece por ningún lado, el texto afirma un
    resultado que el código nunca respalda.

    No se exige que los rótulos coincidan: el texto la llama `\\bar{x}`
    y el código `Media:`, y ninguna regla sintáctica une esos nombres de
    forma confiable. El valor mismo es la evidencia.

    La confirmación/contradicción por prosa (ver `_contradicho_por_prosa_inmediata`)
    y la aritmética de la propia expresión (ver `_contradicho_por_aritmetica_propia`)
    corren ANTES del filtro de `_es_valor_trivial`: ese filtro descarta valores
    pequeños porque suelen ser índices/exponentes sin significado propio como
    resultado, pero un p-valor real (p. ej. 0.02) o un IQR de 1.35 son
    exactamente ese rango y sí son resultados con significado -la evidencia
    aquí no es "aparece en algún lado", es interna al propio texto.
    """
    for valor_esperado, expresion in esperados:
        ya_reportado = False
        if cuerpo and _contradicho_por_prosa_inmediata(
            expresion, cuerpo, valor_esperado
        ):
            discrepancias.append(
                {
                    "seccion": titulo,
                    "valor_declarado": valor_esperado,
                    "valores_producidos": [],
                    "motivo": (
                        "el propio texto, en la oración inmediatamente "
                        "posterior, cita un valor distinto para el mismo "
                        "resultado"
                    ),
                }
            )
            ya_reportado = True
        if not ya_reportado and _contradicho_por_aritmetica_propia(
            expresion, valor_esperado
        ):
            discrepancias.append(
                {
                    "seccion": titulo,
                    "valor_declarado": valor_esperado,
                    "valores_producidos": [],
                    "motivo": (
                        "la propia operación de la expresión (2 operandos) "
                        "no produce el valor declarado en el boxed"
                    ),
                }
            )

    numeros_de_la_unidad = [
        float(n) for n in _NUMERO.findall(_limpiar_latex(salida_de_la_unidad))
    ]
    if not numeros_de_la_unidad:
        return

    boxed_del_codigo = _extraer_valores_boxed_local(salida_de_la_unidad)

    for valor_esperado, expresion in esperados:
        if _es_valor_trivial(valor_esperado):
            continue
        if _algun_valor_coincide(valor_esperado, numeros_de_la_unidad):
            continue
        contexto = f"{titulo}\n{expresion}"
        comparables = [
            valor
            for valor, expresion_codigo in boxed_del_codigo
            if _comparten_datos(contexto, expresion_codigo)
        ]
        if comparables and not _algun_valor_coincide(valor_esperado, comparables):
            discrepancias.append(
                {
                    "seccion": titulo,
                    "valor_declarado": valor_esperado,
                    "valores_producidos": comparables[:10],
                    "motivo": (
                        "el código encuadra un resultado distinto del que "
                        "declara el texto para el mismo cálculo"
                    ),
                }
            )
            continue

        if not _comparte_operando_calculado(expresion, numeros_de_la_unidad):
            continue
        discrepancias.append(
            {
                "seccion": titulo,
                "valor_declarado": valor_esperado,
                "valores_producidos": numeros_de_la_unidad[:10],
                "motivo": (
                    "el código calcula los pasos intermedios de este "
                    "ejemplo pero no produce el resultado declarado"
                ),
            }
        )


def _extraer_valores_boxed_local(text: str) -> list:
    """Copia mínima de `_extraer_valores_boxed` para uso interno de
    `_contrastar_contra_la_unidad`, que necesita re-detectar los
    `\\boxed{}` que el propio código imprime en su stdout (no los del
    Markdown de la lección — esos los extrae `engineer_agent.py` con su
    propia `_extraer_valores_boxed`, que usa `_BOXED`, no movida aquí)."""
    boxed_pattern = re.compile(r"\\boxed\{((?:[^{}]|\{[^{}]*\})*)\}")
    valores = []
    for match in boxed_pattern.finditer(text):
        contenido = match.group(1)
        numeros = _NUMERO.findall(_limpiar_latex(contenido))
        if not numeros:
            continue
        inicio_linea = text.rfind("\n", 0, match.start()) + 1
        expresion = text[inicio_linea : match.end()]
        valores.append((float(numeros[-1]), expresion))
    return valores


def _nombre_de_la_cantidad(expresion: str) -> str:
    """Nombre de la cantidad que el `\\boxed{}` reporta: lo que aparece
    antes del primer `=` de la línea, sin delimitadores de fórmula.

    `\\boxed` se descarta explícitamente: es el envoltorio, no el nombre
    de la cantidad. Dejarlo convertiría `\\boxed{\\bar{x} = 99.0}` en la
    etiqueta "boxedbarx", que nunca coincide con lo que imprime el
    código y silenciaría la comparación.
    """
    izquierda, sep, _ = expresion.partition("=")
    if not sep:
        return ""
    sin_envoltorio = izquierda.replace("$", " ").replace(r"\boxed", " ")
    return _normalizar_identificador(sin_envoltorio)


def _normalizar_identificador(texto: str) -> str:
    """Reduce notación LaTeX y prosa a letras y dígitos en minúscula, de
    modo que `E[Y|X=1]` (texto) y `E[Y|X=1]` (rótulo del print) coincidan
    pese a `\\hat`, `{}`, `\\,` y demás decoración.

    La barra invertida de una macro se descarta pero su palabra se
    conserva: `\\alpha` es el nombre de la cantidad, y el código la
    rotula como `alpha=` (las lecciones escriben sus `print` en ASCII).
    Borrar la macro entera dejaría sin nombre justo a las cantidades
    que se nombran con una letra griega.
    """
    return re.sub(r"[^0-9a-z]+", "", texto.lower())


# Un rótulo dentro de una línea con varias asignaciones (patrón real del
# curso: `print(f"alpha={alpha}, beta={beta:.4f}, potencia={potencia:.4f}")`
# imprime "alpha=0.05, beta=0.1492, potencia=0.8508" en una sola línea).
# Cada segmento es un identificador corto (letras/dígitos/paréntesis,
# sin espacios) seguido de `=` y un número; el separador es el propio
# `=` que abre el segmento siguiente, una coma, o el fin de línea.
#
# Seguridad (hallazgo CRITICAL de @security-reviewer, con dos rondas
# de medición propia): la primera versión (`[\w().]+\s*=\s*...`)
# permitía que `[\w().]+` y `\s*` se solaparan sobre la misma racha
# de espacios. Quitar el `\s*` (`[\w().]+?=...`) rompió el caso real
# `z = -1.5216, p = 0.1281` (espacios alrededor del `=`, patrón
# habitual de un `print(f"... {a} = {b}, ...")`) y seguía escalando
# cuadrático -medido, 0.13s con solo 2000 caracteres sin `=`- porque
# el identificador no tenía cota superior. La versión final acota el
# identificador a `{1,40}` (ningún nombre de variable real del curso
# se acerca a esa longitud) y permite hasta 2 espacios -acotados, no
# `\s*`- a cada lado del `=`, sin que ese espacio pueda solaparse con
# el identificador (ambos tienen cota fija, no hay ambigüedad de
# partición): medido, 200 000 caracteres sin `=` corren en 0.76s y
# 100 000 repeticiones de "a " sin `=` en 0.04s (ambos lineales).
_ROTULO_INLINE = re.compile(
    r"([\w().]{1,40}?)\s{0,2}=\s{0,2}(-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)"
)

# Cota defensiva adicional (segunda capa): aunque el regex ya es
# lineal, una línea de decenas de miles de caracteres sigue siendo
# trabajo desperdiciado sobre una salida que ningún `print` real del
# curso produce tan larga.
_MAX_CHARS_POR_LINEA_ROTULO = 2000

# Rótulo = expresión intermedia [= expresión intermedia...] = valor final,
# en una sola línea (patrón real, `pos_u2_probabilidad_combinatoria.md` de
# A3-U, 2026-09-18: `print(f"P(A) = |A|/|Omega| = 0.1846")`). `_ROTULO_INLINE`
# exige identificador-igual-número en el MISMO segmento, así que nunca
# encontraba nada aquí: el primer '=' deja `|A|/|Omega|` de un lado (no es
# un número) y `0.1846` del otro (separado por un segundo '='). Este
# patrón toma el PRIMER segmento como rótulo y el ÚLTIMO como valor,
# ignorando cuántos '=' intermedios haya.
#
# Important (revisión de python-reviewer, 2026-09-18): con 3+ '=' en la
# línea, el ÚLTIMO segmento por sí solo (`intermedio2 = valor`) SÍ cumple
# el patrón de `_ROTULO_INLINE` -- activar este fallback solo "si `pares`
# está vacío" nunca disparaba en ese caso, y el rótulo real (el del primer
# segmento) quedaba sin comparar. La condición correcta no es "la lista
# está vacía" sino "ningún par ya encontrado tiene el nombre que se busca"
# -- se decide en `_valores_junto_al_rotulo`, que es quien conoce `nombre`.
#
# Misma disciplina de acotamiento que `_ROTULO_INLINE` (ver su
# comentario): identificador limitado a `{1,40}`, sin `\s*` sin cota,
# y ya opera sobre `linea` recortada a `_MAX_CHARS_POR_LINEA_ROTULO`.
_ROTULO_CADENA = re.compile(
    r"^([\w().]{1,40}?)\s{0,2}=.*=\s{0,2}(-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)\s*$"
)


def _valores_junto_al_rotulo(nombre: str, salida: str) -> list:
    """Números que el código imprime inmediatamente después de un rótulo
    cuyo nombre normalizado coincide con `nombre`, sin importar si
    comparten línea con otras asignaciones."""
    valores = []
    for linea in salida.splitlines():
        if "=" not in linea:
            continue
        linea = linea[:_MAX_CHARS_POR_LINEA_ROTULO]
        pares = _ROTULO_INLINE.findall(linea)
        if not any(_normalizar_identificador(r).endswith(nombre) for r, _ in pares):
            cadena = _ROTULO_CADENA.match(linea)
            if cadena:
                pares = [*pares, cadena.groups()]
        for rotulo, numero in pares:
            if _normalizar_identificador(rotulo).endswith(nombre):
                valores.append(float(numero))
    return valores


def _mismo_orden_de_magnitud(a: float, b: float) -> bool:
    if a == 0 or b == 0:
        return a == b
    return 0.5 <= abs(a / b) <= 2.0


def _el_codigo_apunta_al_valor(
    expresion_boxed: str,
    salida: str,
    valor_declarado: float,
    seccion_tiene_un_solo_boxed: bool,
) -> bool:
    """¿El código dice estar calculando la misma cantidad que el `\\boxed{}`?

    Las lecciones alternan ejemplos analíticos resueltos a mano con
    verificaciones computacionales de OTRO caso: UNIDAD 7 §1.3 deriva
    alpha/beta de una exponencial y su bloque ejecuta un escenario AgNP
    distinto; UNIDAD 4 §3.3 encuadra un `E[Y]=7` algebraico cuyo código
    solo calcula `E[Y|X=1]`. Ambos son contenido correcto, y sin esta
    comprobación se reportarían como discrepancias.

    El criterio es la etiqueta: el código del curso imprime sus
    resultados rotulados (`print(f"E[Y|X=1] = {...}")`), así que un
    `\\boxed{}` es contrastable cuando su lado izquierdo —el nombre de
    la cantidad— aparece en la salida. Un valor calculado bajo otro
    nombre pertenece a otro ejemplo; comparar números sueltos entre sí
    no distingue esos dos casos.

    Límite de diseño (N-04, auditoría 2026-09-13): este mecanismo
    detecta desincronización NUMÉRICA, no un nombre incorrecto sobre
    un valor correcto. `\\boxed{0.1281}` sin rótulo, etiquetado en
    prosa como "significancia crítica" cuando el código lo produce
    como p-valor, no genera discrepancia -el número es real- y no
    hay verificación heurística que distinga eso de un nombre
    correcto. Requiere comprensión semántica que este diseño
    (heurístico, sin LLM) no puede sostener.
    """
    nombre = _nombre_de_la_cantidad(expresion_boxed)
    if not nombre:
        return True
    if not _normalizar_identificador(salida):
        return False

    valores_rotulados = _valores_junto_al_rotulo(nombre, salida)
    if not valores_rotulados:
        return False

    if seccion_tiene_un_solo_boxed:
        return True

    return any(_mismo_orden_de_magnitud(valor_declarado, v) for v in valores_rotulados)
