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
#
# N-02 (auditoría post-cierre 2026-09-11): la última alternativa
# (`\d+(?:[.,]\d+)?` suelto, sin exigir unidad ni comparación) hacía que
# CUALQUIER número bastara -exactamente lo que este regex existe para
# descartar-, y el intento de quitarla (M-2, Task 1 de esta ronda)
# bloqueaba U2 §8.1 y U4 §10.1 pese a que sus interpretaciones SÍ traen
# magnitudes reales ($45\%$, $\rho=-0.75$): el regex estricto no
# reconocía el `%` escapado en LaTeX (`\%`, con la barra invertida entre
# el número y el símbolo) ni un signo negativo tras `=` (`\rho=-0.75`).
# Se corrigen esos dos huecos y se retira la alternativa laxa: la mejora
# real no era el contenido, era el regex.
#
# M2 (medición de precisión A3, 2026-09-16): la medición de A3 con el
# corpus de negativos corregido (cierre de ciclo completo, ver
# docs/superpowers/audits/2026-09-16-precision-consejo-corpus.md) reveló
# dos huecos más, ambos con `\d{1,15}(?:[.,]\d{1,15})?\s?\\?` seguido de
# un patrón acotado -misma disciplina anti-ReDoS de la nota de abajo,
# nunca un cuantificador sin límite superior nuevo-: (1) el espacio
# forzado de LaTeX antes de `\text{...}` (`$12.9\ \text{nm}$`, no
# `12.9nm` pegado) -- la alternativa de unidad exigía como mucho un `\`
# entre el número y la unidad, y aquí hay `\` + espacio + `\text{`; (2)
# un número con separador de miles (`100,000`) sin unidad física
# reconocida, seguido de una palabra suelta ("réplicas") -- tan
# verificable como `15.65 nm`, pero la alternativa de unidad exige una de
# la lista fija y la de comparación exige `±`/`<>=`.
#
# Seguridad (hallazgo CRITICAL de @security-reviewer, con una segunda
# ronda de medición propia tras el primer intento de fix): la versión
# original con `\d+` sin cota escala cuadrático sobre una racha larga de
# dígitos sin unidad reconocida -medido, 2.9s con solo 3000 dígitos-,
# porque el motor reintenta la alternativa completa en cada una de las N
# posiciones de inicio, y cada intento retrocede sobre un `\d+` que puede
# llegar a consumir el string entero. Acotar cada `\d+` a `\d{1,15}`
# (ningún número real de una lección supera esa longitud) vuelve el
# backtracking por intento O(1) en vez de O(n): medido, 500 000 dígitos
# corren en 5.2s (lineal, no cuadrático). `\s?` (0 o 1 espacio, nunca
# más) cubre tanto `45\%` pegado como `15.65 nm` con un único espacio sin
# reabrir ancho variable. La cota de longitud en `_extraer_interpretacion`
# (`_MAX_CHARS_PARRAFO_AFIRMACION`) es la segunda capa, y aquí es la que
# realmente importa: una segunda ronda de revisión encontró que una racha
# de dígitos con puntos intercalados (p. ej. "123456789012345." repetido)
# es lineal -no cuadrático- pero con una constante ~60x peor que otros
# adversarios (~85 µs/carácter, porque el grupo opcional
# `(?:[.,]\d{1,15})?` reintenta su `\d{1,15}` interno en cada punto), y
# sin la cota de 3000 caracteres ese patrón específico tarda 68s con
# 800 000 caracteres. Con la cota en vigor el peor caso medido es ~26ms.
# El fix de M2 preserva esta propiedad: el nuevo grupo LaTeX usa `\s?`
# (0 o 1 espacio) igual que el resto, nunca `\s*`, y la nueva alternativa
# de miles reutiliza el mismo `\d{1,15}` acotado sin abrir un cuantificador
# nuevo sin límite.
_AFIRMACION_VERIFICABLE = re.compile(
    r"\d{1,15}(?:[.,]\d{1,15})?\s?\\?\s?\\?(?:%|nm|µm|um|mm|s\b|ms\b|°|K\b|eV\b|Ω|ohm|text\{\w{1,20}\})"
    r"|\d{1,15}(?:[.,]\d{1,15}){1,10}\$?\s+\w{1,20}"
    r"|\d{1,15}(?:[.,]\d{1,15})?\s*(?:±|\+/-)"
    r"|[<>=]\s*-?\d",
    re.IGNORECASE,
)

# Cota defensiva adicional (segunda capa): ningún párrafo real de
# interpretación del curso se acerca a esta longitud (el propio Gold
# Standard exige un párrafo, no un ensayo).
_MAX_CHARS_PARRAFO_AFIRMACION = 3000

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
            if not _AFIRMACION_VERIFICABLE.search(
                limpio[:_MAX_CHARS_PARRAFO_AFIRMACION]
            ):
                continue
            return limpio
        return None
