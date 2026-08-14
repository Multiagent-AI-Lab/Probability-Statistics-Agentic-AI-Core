"""
SafetyGateAgent (@Safety_Gate): Agente Guardián de Supuestos Estadísticos,
Secuencia Curricular y Pedagogía Socrática.
"""

from typing import Any, Dict


class SafetyGateAgent:
    """Agente Guardián de la Seguridad Instruccional, Supuestos Estadísticos y Secuencia Curricular."""

    def __init__(self):
        self.assumptions_rules = {
            "t-test": ["shapiro", "normal", "normality"],
            "anova": ["levene", "bartlett", "homoscedasticity", "homocedasticidad"],
            "regression": [
                "linearity",
                "homoscedasticidad",
                "independencia",
                "residuals",
            ],
        }

        # Reglas de secuencia curricular estricta (Anacronismos prohibidos).
        # Terminos de Inferencia Avanzada (Pruebas de Hipotesis formales) estan
        # prohibidos hasta antes de UNIDAD 7 (Inferencia y Estimacion).
        hipotesis_terms = [
            "Prueba UMP",
            "Error Tipo I",
            "Error Tipo II",
            "Rechazar H_0",
            "Región Crítica",
            "Prueba de Hipótesis",
            "Likelihood Ratio",
            "Prueba t de Student",
            "ANOVA",
        ]
        self.unit_forbidden_terms = {
            "UNIDAD 1": hipotesis_terms,
            "UNIDAD 2": hipotesis_terms,
            "UNIDAD 3": hipotesis_terms,
            "UNIDAD 4": hipotesis_terms,
            "UNIDAD 5": hipotesis_terms,
            "UNIDAD 6": hipotesis_terms,
            "UNIDAD 7": [],
            "UNIDAD 8": [],
        }

        # Terminos requeridos por unidad: al menos uno debe aparecer para que
        # la unidad sea tematicamente coherente con su nombre curricular.
        self.unit_required_terms = {
            "UNIDAD 2": [
                "combinatoria",
                "bayes",
                "axioma",
                "permutación",
                "permutacion",
                "combinación",
                "combinacion",
            ],
            "UNIDAD 4": ["conjunta", "marginal", "condicional", "covarianza"],
            "UNIDAD 6": [
                "simulación",
                "simulacion",
                "monte carlo",
                "transformada inversa",
            ],
        }

    def validate_assumptions(
        self, lesson_text: str, unit_name: str = ""
    ) -> Dict[str, Any]:
        warnings = []
        critical_flags = []
        text_lower = lesson_text.lower()

        # 1. Validacion de Supuestos Estadisticos en Codigo/Teoria (NO critico)
        for test, required_assumptions in self.assumptions_rules.items():
            if test in text_lower:
                has_assumption = any(ass in text_lower for ass in required_assumptions)
                if not has_assumption:
                    warnings.append(
                        f"Se utiliza '{test}' sin antes verificar los supuestos de "
                        f"{' / '.join(required_assumptions)}."
                    )

        # 2. Validacion de Secuencia Curricular (CRITICO: anacronismo)
        for unit_key, forbidden_terms in self.unit_forbidden_terms.items():
            if (
                unit_key.lower() in unit_name.lower()
                or unit_key.lower() in lesson_text[:200].lower()
            ):
                for term in forbidden_terms:
                    if term.lower() in text_lower:
                        warnings.append(
                            f"🚨 [Error de Secuencia Curricular]: La '{unit_key}' contiene el tema de Inferencia Avanzada '{term}', el cual pertenece estrictamente a UNIDAD 7 y UNIDAD 8."
                        )
                        critical_flags.append(True)

        # 3. Validacion de Mismatch Tematico (CRITICO: contenido de otra unidad)
        for unit_key, required_terms in self.unit_required_terms.items():
            if (
                unit_key.lower() in unit_name.lower()
                or unit_key.lower() in lesson_text[:200].lower()
            ):
                has_required = any(
                    term.lower() in text_lower for term in required_terms
                )
                if not has_required:
                    warnings.append(
                        f"🚨 [Error de Mismatch Temático]: La '{unit_key}' no contiene ninguno de los términos esperados ({', '.join(required_terms)}); el contenido podría pertenecer a otra unidad."
                    )
                    critical_flags.append(True)

        return {
            "passed": len(warnings) == 0,
            "warnings": warnings,
            "critical": any(critical_flags),
        }
