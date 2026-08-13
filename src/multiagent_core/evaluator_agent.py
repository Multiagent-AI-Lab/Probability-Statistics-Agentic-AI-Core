"""
EvaluatorAgent: Evaluates statistical notebooks against pedagogical rubrics.
"""

from typing import Dict, Any, List


class EvaluatorAgent:
    """Evaluator agent that assigns scores based on pedagogical and technical criteria."""

    def __init__(self):
        self.rubric = {
            "rigor_teorico": 25.0,        # Fórmulas LaTeX, fundamentación
            "excelencia_codigo": 25.0,     # scipy, pandas, sympy, PEP8
            "visualizacion_datos": 25.0,   # Seaborn, Matplotlib, etiquetado
            "interpretacion_nano": 25.0    # Análisis del contexto nanotecnológico
        }

    def evaluate_notebook(self, audit_results: Dict[str, Any], content_results: Dict[str, Any]) -> Dict[str, Any]:
        scores = {}
        
        # Rigor teórico
        words = content_results.get("total_words", 0)
        rigor = min(25.0, (words / 1000.0) * 25.0)
        scores["rigor_teorico"] = round(rigor, 1)

        # Excelencia código
        code_score = audit_results.get("score", 100.0)
        scores["excelencia_codigo"] = round((code_score / 100.0) * 25.0, 1)

        # Visualización datos (verificar presencia de gráficos o código de graficación)
        has_plots = (
            audit_results.get("metrics", {}).get("has_plots", False) or
            content_results.get("component_checks", {}).get("Visualización Profesional", False)
        )
        scores["visualizacion_datos"] = 25.0 if has_plots else 10.0

        # Interpretación Nano
        has_nano = content_results.get("component_checks", {}).get("Contexto Nanotecnológico", False)
        scores["interpretacion_nano"] = 25.0 if has_nano else 12.5

        total_score = sum(scores.values())

        return {
            "total_score": round(total_score, 1),
            "passed": total_score >= 80.0,
            "category_scores": scores,
            "feedback": self._generate_feedback(scores)
        }

    def _generate_feedback(self, scores: Dict[str, float]) -> List[str]:
        feedback = []
        if scores["rigor_teorico"] < 20.0:
            feedback.append("Aumentar el número de ecuaciones LaTeX y desarrollo formal.")
        if scores["excelencia_codigo"] < 20.0:
            feedback.append("Usar scipy.stats / statsmodels con type hints y display(Math()).")
        if scores["visualizacion_datos"] < 20.0:
            feedback.append("Incluir al menos 2 gráficos estadísticos profesionales (Seaborn).")
        if scores["interpretacion_nano"] < 20.0:
            feedback.append("Enriquecer el análisis e interpretación física en contexto de Nanotecnología.")
        return feedback
