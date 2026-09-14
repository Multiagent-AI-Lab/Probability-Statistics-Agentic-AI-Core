"""
Subsistema de contraste texto↔ejecución: compara los `\\boxed{}` de una
lección contra la salida real del código que la acompaña.

Extraído de `engineer_agent.py` (que llegó a 767 líneas) para mantener
cada módulo enfocado en una responsabilidad. Funciones libres, no una
clase — ninguna usa estado de instancia.
"""

import re

# Número final de una expresión: el último numérico que aparece en el
# `\boxed{}`, que es el resultado (`P(X=2) = 190 \times 0.0025 \approx
# 0.18868` -> 0.18868).
_NUMERO = re.compile(r"-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?")

_TOLERANCIA_RELATIVA = 1e-3


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


def _contrastar_contra_la_unidad(
    titulo: str,
    esperados: list,
    salida_de_la_unidad: str,
    discrepancias: list,
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
    """
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


def _valores_junto_al_rotulo(nombre: str, salida: str) -> list:
    """Números que el código imprime inmediatamente después de un rótulo
    cuyo nombre normalizado coincide con `nombre`, sin importar si
    comparten línea con otras asignaciones."""
    valores = []
    for linea in salida.splitlines():
        if "=" not in linea:
            continue
        linea = linea[:_MAX_CHARS_POR_LINEA_ROTULO]
        for rotulo, numero in _ROTULO_INLINE.findall(linea):
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
