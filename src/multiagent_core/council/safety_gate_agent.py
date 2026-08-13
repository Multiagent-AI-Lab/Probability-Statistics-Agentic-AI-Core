"""
SafetyGateAgent (@Safety_Gate): Agente Guardián de Supuestos Estadísticos,
Secuencia Curricular y Pedagogía Socrática.
"""

import re
from typing import Dict, Any, List


class SafetyGateAgent:
    """Agente Guardián de la Seguridad Instruccional, Supuestos Estadísticos y Secuencia Curricular."""

    def __init__(self):
        self.assumptions_rules = {
            "t-test": ["shapiro", "normal", "normality"],
            "anova": ["levene", "bartlett", "homoscedasticity", "homocedasticidad"],
            "regression": ["linearity", "homoscedasticidad", "independencia", "residuals"],
        }
        
        # Reglas de secuencia curricular estricta (Anacronismos prohibidos)
        self.unit_forbidden_terms = {
            "UNIDAD 1": ["Prueba UMP", "Error Tipo I", "Error Tipo II", "Rechazar H_0", "Región Crítica", "Prueba de Hipótesis", "Likelihood Ratio"],
            "UNIDAD 2": ["Prueba UMP", "Error Tipo I", "Rechazar H_0", "Prueba t de Student", "ANOVA"],
            "UNIDAD 3": ["Prueba UMP", "Error Tipo I", "Rechazar H_0", "Prueba t de Student"],
            "UNIDAD 4": ["Prueba UMP", "Error Tipo I", "Rechazar H_0"],
            "UNIDAD 5": ["Prueba UMP", "Error Tipo I", "Rechazar H_0"],
        }

    def validate_assumptions(self, lesson_text: str, unit_name: str = "") -> Dict[str, Any]:
        warnings = []
        text_lower = lesson_text.lower()

        # 1. Validación de Supuestos Estadísticos en Código/Teoría
        for test, required_assumptions in self.assumptions_rules.items():
            if test in text_lower:
                has_assumption = any(ass in text_lower for ass in required_assumptions)
                if not has_assumption:
                    warnings.append(
                        f"Se utiliza '{test}' sin antes verificar los supuestos de "
                        f"{' / '.join(required_assumptions)}."
                    )

        # 2. Validación de Secuencia Curricular (Detección de Anacronismos Pedagógicos)
        for unit_key, forbidden_terms in self.unit_forbidden_terms.items():
            if unit_key.lower() in unit_name.lower() or unit_key.lower() in lesson_text[:200].lower():
                for term in forbidden_terms:
                    if term.lower() in text_lower:
                        warnings.append(
                            f"🚨 [Error de Secuencia Curricular]: La '{unit_key}' contiene el tema de Inferencia Avanzada '{term}', el cual pertenece estrictamente a las Unidades 6 y 7."
                        )

        return {
            "passed": len(warnings) == 0,
            "warnings": warnings,
        }
