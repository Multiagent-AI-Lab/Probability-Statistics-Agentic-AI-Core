"""
ScientistAgent (@Scientist): Owner of statistical theory, LaTeX notation, and formal proofs.
"""

import ast
import operator
import re
from typing import Any

# Un bloque LaTeX cuenta como "fórmula estructurada" solo si contiene una
# relación (=, <=, >=, <, >, \sim, \approx, \propto) o un operador/macro
# matemática real (\sum, \int, \frac, \sqrt, ^, _). H-01: el criterio
# anterior era `text.count("$") >= 10`, que aprobaba prosa con `$x$`
# repetido -- un símbolo aislado no afirma nada verificable.
_LATEX_INLINE = re.compile(r"\$([^$\n]+)\$")
_LATEX_DISPLAY = re.compile(
    r"\$\$(.+?)\$\$|\\begin\{(?:align|equation|gather)\*?\}(.+?)\\end\{(?:align|equation|gather)\*?\}",
    re.DOTALL,
)
_ESTRUCTURA_FORMULA = re.compile(
    r"=|\\leq|\\geq|\\le\b|\\ge\b|<|>|\\sim|\\approx|\\propto"
    r"|\\sum|\\int|\\prod|\\frac|\\sqrt|\^|_"
)

# Un valor solo cuenta como "declarado" si la expresión TERMINA ahí: el
# número debe ser el resultado, no el primer operando de un cálculo mayor.
# Sin este anclaje se producen falsos positivos sobre contenido correcto:
#   $P(C|G_B) = 2/3$              -> leería "2" (es una fracción)
#   $P(X=2) = 190 \times 0.0025$  -> leería "190" (es un factor)
#   p-valor = 2 \cdot P(Z < -2.55) -> leería "2" (es un coeficiente)
# `_FIN_DE_VALOR` exige que tras el número no siga un operador ni un dígito
# que lo continúe (/, \times, \cdot, ^, e-notación, etc.).
_FIN_DE_VALOR = r"(?!\s*(?:[/*+^]|-\s*\d|\d|\\times|\\cdot|\\frac|\\sqrt|[eE][-+]?\d))"
_NUMERO = r"(-?\d+(?:\.\d+)?)"

# Un número declarado como probabilidad: P(...) = v, P_algo = v.
_PROBABILIDAD_DECLARADA = re.compile(
    r"\bP\s*(?:\([^)]*\))?\s*=\s*" + _NUMERO + _FIN_DE_VALOR
)
# Correlación de Pearson: \rho = v.
_CORRELACION_DECLARADA = re.compile(r"\\rho\s*=\s*" + _NUMERO + _FIN_DE_VALOR)
# Varianza: \sigma^2 = v o Var(...) = v.
_VARIANZA_DECLARADA = re.compile(
    r"(?:\\sigma\s*\^\s*(?:2|\{2\})|\bVar\s*\([^)]*\))\s*=\s*" + _NUMERO + _FIN_DE_VALOR
)
# Suma de una función de masa: \sum... P(...) = v.
_SUMA_PMF_DECLARADA = re.compile(
    r"\\sum[^=]{0,80}?P\s*\([^)]*\)\s*=\s*" + _NUMERO + _FIN_DE_VALOR
)

_MIN_PALABRAS_TEORIA = 800
_TOLERANCIA_PMF = 1e-6

# Aritmética declarada dentro de un `\boxed{}`: una fracción de dos
# expresiones numéricas seguida del resultado afirmado.
#   \frac{145.19-125.37}{22.32} \approx 0.75
_FRACCION_CON_RESULTADO = re.compile(
    r"\\[dt]?frac\s*\{([^{}]+)\}\s*\{([^{}]+)\}\s*"
    r"(?:=|\\approx|\\simeq)\s*(-?\d+(?:\.\d+)?)"
)
# Expresión aritmética simple: solo números, operadores y \times / \cdot.
# El filtro léxico es la primera barrera; la segunda (y la que de verdad
# acota el costo) es `_evaluar_aritmetica`, que recorre el AST y rechaza
# `ast.Pow` -- este regex por sí solo acepta `**`. Ver I-1.
_ARITMETICA_SIMPLE = re.compile(r"^[\d\s.+\-*/()]+$")
# El resultado se compara con la precisión que el propio texto declara: si
# afirma 0.75, basta con que el cálculo redondee a 0.75.
_TOLERANCIA_ARITMETICA = 0.51

# Operaciones admitidas al evaluar aritmética simple. La potencia (ast.Pow)
# queda deliberadamente fuera: es la única cuyo resultado puede crecer sin
# relación con el tamaño de la entrada (`9**9**9**9`).
_OPERACIONES_PERMITIDAS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


class _AritmeticaNoPermitida(Exception):
    """La expresión contiene un nodo u operador fuera de la aritmética simple."""


class ScientistAgent:
    """Agent responsible for checking mathematical rigor and LaTeX formatting."""

    def check_theory(self, text: str) -> dict[str, Any]:
        """Audita rigor matemático real, no densidad de símbolos.

        Tres criterios, todos necesarios (H-01: antes bastaban palabras +
        conteo de `$`, y `has_boxed_solution` se calculaba pero se
        descartaba del veredicto):

        1. Volumen teórico (>= 800 palabras, Gold Standard §3.1).
        2. Fórmulas LaTeX con estructura real, no símbolos sueltos.
        3. Solución final en `\\boxed{}` (Gold Standard §3.5).

        Además reporta invariantes de dominio violados -- afirmaciones
        objetivamente falsas que se pueden refutar sin LLM ni contexto.
        """
        words = len(text.split())
        formulas = self._extraer_formulas_estructuradas(text)
        tiene_formulas = len(formulas) >= 2
        has_boxed = r"\boxed" in text
        invariantes_violados = self._validar_invariantes_dominio(text)
        aritmetica_inconsistente = self._validar_aritmetica_declarada(text)

        return {
            "word_count": words,
            "math_equation_count": len(formulas),
            "formulas_estructuradas": formulas,
            "tiene_formulas_estructuradas": tiene_formulas,
            "has_boxed_solution": has_boxed,
            "invariantes_violados": invariantes_violados,
            "aritmetica_inconsistente": aritmetica_inconsistente,
            "passed": (
                words >= _MIN_PALABRAS_TEORIA
                and tiene_formulas
                and has_boxed
                and not invariantes_violados
                and not aritmetica_inconsistente
            ),
        }

    def _validar_aritmetica_declarada(self, text: str) -> list[str]:
        """Comprueba que una fórmula encuadrada cierre consigo misma.

        `\\boxed{d = \\frac{145.19-125.37}{22.32} \\approx 0.75}` afirma a la
        vez los operandos y el resultado: esa división da 0.888, así que uno
        de los dos está mal (UNIDAD 7 usaba la media nominal 145 en vez de
        la muestral 142.19). Es un error verificable sin ejecutar código ni
        interpretar el enunciado — solo hay que hacer la cuenta.
        """
        violaciones: list[str] = []
        for numerador, denominador, resultado in _FRACCION_CON_RESULTADO.findall(text):
            calculado = self._evaluar_expresion(numerador, denominador)
            if calculado is None:
                continue
            declarado = float(resultado)
            # Se compara al número de decimales que el texto declara: 0.888
            # frente a 0.75 no coincide ni redondeando.
            decimales = len(resultado.split(".")[1]) if "." in resultado else 0
            if round(calculado, decimales) != declarado:
                violaciones.append(
                    f"la fórmula encuadrada no cierra: "
                    f"({numerador.strip()})/({denominador.strip()}) = "
                    f"{calculado:.4f}, pero el texto declara {declarado}"
                )
        return violaciones

    @classmethod
    def _evaluar_expresion(cls, numerador: str, denominador: str) -> float | None:
        """Evalúa una fracción cuyos dos lados son aritmética simple.

        Solo se aceptan cadenas de números y operadores tras normalizar
        `\\times`/`\\cdot`: nunca se evalúa contenido arbitrario del texto.
        """

        def _normalizar(expresion: str) -> str:
            limpio = re.sub(r"\\(?:times|cdot)", "*", expresion)
            limpio = re.sub(r"\\[a-zA-Z]+|[{}]", " ", limpio)
            return limpio.strip()

        num, den = _normalizar(numerador), _normalizar(denominador)
        if not (_ARITMETICA_SIMPLE.match(num) and _ARITMETICA_SIMPLE.match(den)):
            return None
        if not (any(c.isdigit() for c in num) and any(c.isdigit() for c in den)):
            return None

        divisor = cls._evaluar_aritmetica(den)
        dividendo = cls._evaluar_aritmetica(num)
        if divisor is None or dividendo is None or divisor == 0:
            return None
        return dividendo / divisor

    @classmethod
    def _evaluar_aritmetica(cls, expresion: str) -> float | None:
        """Evalúa una expresión aritmética simple recorriendo su AST.

        I-1: antes esto era `eval(expresion, {"__builtins__": {}}, {})`.
        Vaciar `__builtins__` impide alcanzar nombres y llamadas, pero no
        acota el COSTO de la expresión: `_ARITMETICA_SIMPLE` acepta `*`, y
        por tanto `**`, así que un `\\boxed{}` con `9**9**9**9` colgaba el
        proceso construyendo un entero de miles de millones de dígitos —
        un DoS trivial desde texto de lección, y esta ruta no corre en un
        subproceso con timeout como la de @Engineer.

        Se recorre el AST en vez de evaluar: solo constantes numéricas y las
        cuatro operaciones (más el signo unario) están permitidas, y
        `ast.Pow` se rechaza explícitamente. Ninguna operación admitida
        puede crecer más allá del tamaño de sus operandos, así que el costo
        queda acotado por la longitud del texto de entrada.
        """
        try:
            arbol = ast.parse(expresion, mode="eval")
        except SyntaxError:
            return None
        try:
            return cls._evaluar_nodo(arbol.body)
        except (_AritmeticaNoPermitida, ArithmeticError, TypeError, ValueError):
            return None

    @classmethod
    def _evaluar_nodo(cls, nodo: ast.AST) -> float:
        if isinstance(nodo, ast.Constant):
            if isinstance(nodo.value, bool) or not isinstance(nodo.value, (int, float)):
                raise _AritmeticaNoPermitida("solo se admiten constantes numéricas")
            return float(nodo.value)

        if isinstance(nodo, ast.UnaryOp) and isinstance(nodo.op, (ast.UAdd, ast.USub)):
            valor = cls._evaluar_nodo(nodo.operand)
            return -valor if isinstance(nodo.op, ast.USub) else valor

        if isinstance(nodo, ast.BinOp):
            operacion = _OPERACIONES_PERMITIDAS.get(type(nodo.op))
            if operacion is None:
                # Incluye ast.Pow: la potencia no se necesita para las
                # fracciones que audita este agente, y es la única de estas
                # operaciones cuyo resultado puede explotar en tamaño.
                raise _AritmeticaNoPermitida(
                    f"operador no permitido: {type(nodo.op).__name__}"
                )
            return operacion(
                cls._evaluar_nodo(nodo.left), cls._evaluar_nodo(nodo.right)
            )

        raise _AritmeticaNoPermitida(f"nodo no permitido: {type(nodo).__name__}")

    def _extraer_formulas_estructuradas(self, text: str) -> list[str]:
        """Devuelve los bloques LaTeX que realmente afirman una relación
        matemática, descartando símbolos aislados como `$x$`."""
        candidatos: list[str] = []

        for match in _LATEX_DISPLAY.finditer(text):
            cuerpo = match.group(1) or match.group(2) or ""
            candidatos.append(cuerpo)

        # Los inline se buscan sobre el texto sin los display ya consumidos,
        # para no partir un `$$...$$` en dos delimitadores inline sueltos.
        texto_sin_display = _LATEX_DISPLAY.sub(" ", text)
        candidatos.extend(_LATEX_INLINE.findall(texto_sin_display))

        return [c for c in candidatos if _ESTRUCTURA_FORMULA.search(c)]

    def _validar_invariantes_dominio(self, text: str) -> list[str]:
        """Verifica invariantes estadísticos que no dependen del contexto:
        una probabilidad fuera de [0,1] o una varianza negativa son falsas
        en cualquier lección, sin necesidad de interpretar el enunciado."""
        violaciones: list[str] = []

        for valor in self._extraer_probabilidades_declaradas(text):
            if not 0 <= valor <= 1:
                violaciones.append(f"probabilidad fuera de [0,1]: {valor}")

        for valor in self._extraer_correlaciones_declaradas(text):
            if abs(valor) > 1:
                violaciones.append(f"|rho| > 1: {valor}")

        for valor in self._extraer_varianzas_declaradas(text):
            if valor < 0:
                violaciones.append(f"varianza negativa: {valor}")

        for valor in self._extraer_sumas_pmf_declaradas(text):
            if abs(valor - 1.0) > _TOLERANCIA_PMF:
                violaciones.append(
                    f"la suma de una función de masa (pmf) debe ser 1, no {valor}"
                )

        return violaciones

    def _extraer_probabilidades_declaradas(self, text: str) -> list[float]:
        # La suma de una pmf se valida aparte (su invariante es "= 1", no
        # "en [0,1]"), así que se excluye de la extracción de probabilidades
        # para no reportar dos veces el mismo error.
        texto = _SUMA_PMF_DECLARADA.sub(" ", text)
        return [float(v) for v in _PROBABILIDAD_DECLARADA.findall(texto)]

    def _extraer_correlaciones_declaradas(self, text: str) -> list[float]:
        return [float(v) for v in _CORRELACION_DECLARADA.findall(text)]

    def _extraer_varianzas_declaradas(self, text: str) -> list[float]:
        return [float(v) for v in _VARIANZA_DECLARADA.findall(text)]

    def _extraer_sumas_pmf_declaradas(self, text: str) -> list[float]:
        return [float(v) for v in _SUMA_PMF_DECLARADA.findall(text)]
