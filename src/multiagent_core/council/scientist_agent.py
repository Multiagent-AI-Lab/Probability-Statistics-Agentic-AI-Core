"""
ScientistAgent (@Scientist): Owner of statistical theory, LaTeX notation, and formal proofs.
"""

import re
from typing import Any

# Un bloque LaTeX cuenta como "fórmula estructurada" solo si contiene una
# relación (=, <=, >=, <, >, \sim, \approx, \propto) o un operador/macro
# matemática real (\sum, \int, \frac, \sqrt, ^, _). H-01: el criterio
# anterior era `text.count("$") >= 10`, que aprobaba prosa con `$x$`
# repetido -- un símbolo aislado no afirma nada verificable.
_LATEX_INLINE = re.compile(r"\$([^$\n]+)\$")
_LATEX_DISPLAY = re.compile(r"\$\$(.+?)\$\$|\\begin\{(?:align|equation|gather)\*?\}(.+?)\\end\{(?:align|equation|gather)\*?\}", re.DOTALL)
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

        return {
            "word_count": words,
            "math_equation_count": len(formulas),
            "tiene_formulas_estructuradas": tiene_formulas,
            "has_boxed_solution": has_boxed,
            "invariantes_violados": invariantes_violados,
            "passed": (
                words >= _MIN_PALABRAS_TEORIA
                and tiene_formulas
                and has_boxed
                and not invariantes_violados
            ),
        }

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
