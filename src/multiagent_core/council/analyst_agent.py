"""
AnalystAgent (@Analyst): Responsible for exploratory analysis, Seaborn plots, and post-plot physical interpretation.
"""

import re
from typing import Any

# Llamadas de graficación de matplotlib/seaborn.
_LLAMADA_GRAFICO = re.compile(r"\b(?:plt|sns|ax|axes)\s*\.\s*\w+\s*\(")

# Encabezado que anuncia una interpretación o análisis de resultados.
_ROTULO_INTERPRETACION = re.compile(
    r"\b(?:interpretaci[oó]n|interpretation|an[aá]lisis|conclusi[oó]n|conclusion)\b",
    re.IGNORECASE,
)

# Marcas de una afirmación verificable: una magnitud numérica, un símbolo
# con valor, o una comparación explícita entre cantidades.
_AFIRMACION_VERIFICABLE = re.compile(
    r"\d+(?:[.,]\d+)?\s*(?:%|nm|µm|um|mm|s\b|ms\b|°|K\b|eV\b|Ω|ohm)"
    r"|\d+(?:[.,]\d+)?\s*(?:±|\+/-)"
    r"|[<>=]\s*\d"
    r"|\d+(?:[.,]\d+)?",
    re.IGNORECASE,
)

_MIN_GRAFICOS = 2
# Una interpretación real desarrolla; un rótulo suelto ("Interpretación.")
# no. El Gold Standard §3.8 pide un párrafo, no una etiqueta.
_MIN_PALABRAS_INTERPRETACION = 20


class AnalystAgent:
    """Agent responsible for auditing plots and post-plot analysis (>150 words per plot)."""

    def audit_visualizations(self, text: str) -> dict[str, Any]:
        """Audita que la sección grafique y que interprete DESPUÉS de graficar.

        H-01: el criterio anterior era
        `("interpret" in text.lower() or "análisis" in ...)`, que aprueba un
        documento donde la palabra aparece en el índice, en un título previo
        o suelta sin afirmar nada. El Gold Standard §3.8 pide una
        explicación *posterior a cualquier visualización*, así que aquí se
        verifica la posición real en el documento y que el párrafo diga algo
        contrastable (una magnitud, una comparación), no solo su rótulo.
        """
        graficos = list(_LLAMADA_GRAFICO.finditer(text))
        posicion_ultimo = graficos[-1].end() if graficos else -1

        texto_posterior = text[posicion_ultimo:] if graficos else ""
        interpretacion = self._extraer_interpretacion(texto_posterior)

        return {
            "plot_count": len(graficos),
            "posicion_ultimo_grafico": posicion_ultimo,
            "has_interpretation": interpretacion is not None,
            "interpretacion": interpretacion,
            "passed": len(graficos) >= _MIN_GRAFICOS and interpretacion is not None,
        }

    def _extraer_interpretacion(self, texto_posterior: str) -> str | None:
        """Devuelve el párrafo de interpretación posterior al último gráfico,
        o None si no hay uno que cumpla."""
        if not texto_posterior.strip():
            return None

        for parrafo in re.split(r"\n\s*\n", texto_posterior):
            limpio = parrafo.strip()
            if not _ROTULO_INTERPRETACION.search(limpio):
                continue
            if len(limpio.split()) < _MIN_PALABRAS_INTERPRETACION:
                continue
            if not _AFIRMACION_VERIFICABLE.search(limpio):
                continue
            return limpio
        return None
