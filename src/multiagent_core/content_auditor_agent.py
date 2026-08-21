"""
ContentAuditorAgent: Audits lessons and notebooks against the 9 mandatory components of the Protocolo Maestro.
"""

import re
from typing import Any, ClassVar


class ContentAuditorAgent:
    """Auditor for content completeness according to the 9 Protocolo Maestro components."""

    def __init__(self):
        self.mandatory_components = [
            "Teoría Completa (>=800 palabras)",
            "Ejemplo Analítico Paso a Paso",
            "Código de Verificación Simbólica (SymPy)",
            "Contexto Nanotecnológico (>=150 palabras)",
            "Solución Analítica en \\boxed{}",
            "Solución Computacional (SciPy / statsmodels)",
            "Visualización Profesional (>=2 gráficos)",
            "Interpretación Post-Gráfico",
            "Diccionario de Variables",
        ]

    NANO_TERMS: ClassVar[list[str]] = [
        "nanopartíc",
        "nanotub",
        "potencial zeta",
        "diámetro",
        "síntesis",
        "toxicid",
        "nanomater",
    ]
    NANO_MIN_WORDS = 150
    DICCIONARIO_MIN_ENTRADAS = 2
    _DICCIONARIO_ENTRADA_PATTERN = re.compile(r"^\s*\*\s*\$[^$]+\$\s*:", re.MULTILINE)

    def _count_nano_context_words(self, markdown_text: str) -> int:
        """Cuenta las palabras de los parrafos que mencionan terminologia
        nanotecnologica (no el documento completo)."""
        paragraphs = re.split(r"\n\s*\n", markdown_text)
        total = 0
        for paragraph in paragraphs:
            paragraph_lower = paragraph.lower()
            if any(term in paragraph_lower for term in self.NANO_TERMS):
                total += len(paragraph.split())
        return total

    def _has_diccionario_variables(self, markdown_text: str) -> bool:
        """Detecta una lista de al menos DICCIONARIO_MIN_ENTRADAS items con
        formato '* $simbolo$: descripcion' (el patron ya usado en las
        lecciones actuales para el diccionario de variables de cierre)."""
        matches = self._DICCIONARIO_ENTRADA_PATTERN.findall(markdown_text)
        return len(matches) >= self.DICCIONARIO_MIN_ENTRADAS

    def audit_content(self, markdown_text: str) -> dict[str, Any]:
        words = len(markdown_text.split())
        latex_boxed = r"\boxed" in markdown_text or r"\boxed{" in markdown_text
        has_sympy = "sympy" in markdown_text.lower()
        has_scipy = (
            "scipy" in markdown_text.lower() or "statsmodels" in markdown_text.lower()
        )
        nano_context_words = self._count_nano_context_words(markdown_text)

        # Count matplotlib/seaborn figures or plots
        plot_count = (
            markdown_text.lower().count("plt.")
            + markdown_text.lower().count("sns.")
            + markdown_text.lower().count("plotly")
        )

        # Check component checks
        component_checks = {
            "Teoría Completa": words >= 800,
            "Ejemplo Analítico": "ejemplo" in markdown_text.lower()
            or "paso" in markdown_text.lower(),
            "Verificación SymPy": has_sympy,
            "Contexto Nanotecnológico": nano_context_words >= self.NANO_MIN_WORDS,
            "Solución en \\boxed{}": latex_boxed,
            "Solución Computacional SciPy": has_scipy,
            "Visualización Profesional": plot_count >= 2,
            "Interpretación Post-Gráfico": "interpret" in markdown_text.lower(),
            "Diccionario de Variables": self._has_diccionario_variables(markdown_text),
        }

        passed_components = [name for name, ok in component_checks.items() if ok]
        missing_components = [name for name, ok in component_checks.items() if not ok]

        score = (len(passed_components) / len(component_checks)) * 100.0

        return {
            "passed": score >= 75.0,
            "score": score,
            "total_words": words,
            "nano_context_words": nano_context_words,
            "component_checks": component_checks,
            "passed_components": passed_components,
            "missing_components": missing_components,
        }
