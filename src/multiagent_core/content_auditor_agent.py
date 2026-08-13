"""
ContentAuditorAgent: Audits lessons and notebooks against the 8 mandatory components of the Protocolo Maestro.
"""

import re
from typing import Dict, Any, List


class ContentAuditorAgent:
    """Auditor for content completeness according to the 8 Protocolo Maestro components."""

    def __init__(self):
        self.mandatory_components = [
            "Teoría Completa (>=800 palabras)",
            "Ejemplo Analítico Paso a Paso",
            "Código de Verificación Simbólica (SymPy)",
            "Contexto Nanotecnológico (>=150 palabras)",
            "Solución Analítica en \\boxed{}",
            "Solución Computacional (SciPy / statsmodels)",
            "Visualización Profesional (>=2 gráficos)",
            "Interpretación Post-Gráfico & Diccionario de Variables"
        ]

    def audit_content(self, markdown_text: str) -> Dict[str, Any]:
        words = len(markdown_text.split())
        latex_boxed = r"\boxed" in markdown_text or r"\boxed{" in markdown_text
        has_sympy = "sympy" in markdown_text.lower()
        has_scipy = "scipy" in markdown_text.lower() or "statsmodels" in markdown_text.lower()
        has_nano_context = any(term in markdown_text.lower() for term in ["nanopartíc", "nanotub", "potencial zeta", "diámetro", "síntesis", "toxicid", "nanomater"])
        
        # Count matplotlib/seaborn figures or plots
        plot_count = markdown_text.lower().count("plt.") + markdown_text.lower().count("sns.") + markdown_text.lower().count("plotly")
        
        # Check component checks
        component_checks = {
            "Teoría Completa": words >= 800,
            "Ejemplo Analítico": "ejemplo" in markdown_text.lower() or "paso" in markdown_text.lower(),
            "Verificación SymPy": has_sympy,
            "Contexto Nanotecnológico": has_nano_context,
            "Solución en \\boxed{}": latex_boxed,
            "Solución Computacional SciPy": has_scipy,
            "Visualización Profesional": plot_count >= 2,
            "Interpretación & Diccionario": "interpret" in markdown_text.lower() or "diccionario" in markdown_text.lower() or "variables" in markdown_text.lower()
        }

        passed_components = [name for name, ok in component_checks.items() if ok]
        missing_components = [name for name, ok in component_checks.items() if not ok]
        
        score = (len(passed_components) / len(component_checks)) * 100.0

        return {
            "passed": score >= 75.0,
            "score": score,
            "total_words": words,
            "component_checks": component_checks,
            "passed_components": passed_components,
            "missing_components": missing_components
        }
