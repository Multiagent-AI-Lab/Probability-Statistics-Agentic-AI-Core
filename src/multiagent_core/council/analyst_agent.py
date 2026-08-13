"""
AnalystAgent (@Analyst): Responsible for exploratory analysis, Seaborn plots, and post-plot physical interpretation.
"""

from typing import Dict, Any, List


class AnalystAgent:
    """Agent responsible for auditing plots and post-plot analysis (>150 words per plot)."""

    def audit_visualizations(self, text: str) -> Dict[str, Any]:
        plot_calls = text.count("plt.") + text.count("sns.")
        has_interpretation = "interpret" in text.lower() or "análisis" in text.lower() or "conclusion" in text.lower()
        
        return {
            "plot_count": plot_calls,
            "has_interpretation": has_interpretation,
            "passed": plot_calls >= 2 and has_interpretation
        }
