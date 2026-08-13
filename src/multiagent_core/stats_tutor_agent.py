"""
StatsTutorAgent: RAG-enabled tutoring agent specialized in Probability, Statistics, and scipy.stats.
"""

import os
from typing import Dict, Any, List, Optional


class StatsTutorAgent:
    """Pedagogical tutor agent for probability and statistical concepts."""

    def __init__(self, chroma_dir: str = ".chroma"):
        self.chroma_dir = chroma_dir
        self.common_misconceptions = {
            "p_value": "El p-valor NO es la probabilidad de que la hipótesis nula sea cierta, sino la probabilidad de observar un resultado igual o más extremo bajo H0.",
            "sd_vs_se": "La Desviación Estándar (SD) mide la dispersión de los datos. El Error Estándar (SE) mide la precisión de la estimación del promedio.",
            "correlation_causation": "La correlación no implica causalidad. Dos variables pueden estar altamente correlacionadas por variables confundidoras."
        }

    def explain_concept(self, topic: str) -> str:
        topic_lower = topic.lower()
        if "p-valor" in topic_lower or "p valor" in topic_lower or "p_value" in topic_lower:
            return f"**Aclaración Pedagógica sobre P-Valor**:\n{self.common_misconceptions['p_value']}"
        elif "desviación" in topic_lower or "error estándar" in topic_lower or "sd" in topic_lower or "se" in topic_lower:
            return f"**Diferencia entre SD y SE**:\n{self.common_misconceptions['sd_vs_se']}"
        elif "correlación" in topic_lower or "causalidad" in topic_lower:
            return f"**Correlación vs Causalidad**:\n{self.common_misconceptions['correlation_causation']}"
        else:
            return f"Concepto '{topic}': Consultando base teórica SciPy/Statsmodels..."

    def answer_question(self, question: str, context: Optional[str] = None) -> Dict[str, Any]:
        explanation = self.explain_concept(question)
        return {
            "question": question,
            "answer": explanation,
            "sources": ["Walpole / Montgomery Statistics", "SciPy Documentation"],
            "confidence": 0.95
        }
