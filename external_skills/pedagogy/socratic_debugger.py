"""
Socratic Debugger Skill: Generates guided questions when student code or analysis has errors.
"""

from typing import Dict, Any, List


class SocraticDebugger:
    """Skill for generating Socratic pedagogical feedback."""

    def generate_socratic_question(self, error_type: str, context: str) -> str:
        if "normality" in error_type.lower():
            return "¿Por qué es fundamental verificar la simetría y normalidad de los datos antes de aplicar una prueba t de Student?"
        elif "p_value" in error_type.lower():
            return "Si obtienes un p-valor de 0.03 con alpha = 0.05, ¿qué decisión tomas respecto a H0 y qué representa físicamente ese 0.03?"
        elif "variance" in error_type.lower():
            return "¿Qué diferencia existe entre evaluar la dispersión con la varianza frente al coeficiente de variación al comparar unidades distintas?"
        else:
            return f"Revisa el desarrollo del paso actual: ¿concuerdan las unidades y supuestos en {context}?"
