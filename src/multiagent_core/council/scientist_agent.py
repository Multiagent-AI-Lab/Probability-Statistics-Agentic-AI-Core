"""
ScientistAgent (@Scientist): Owner of statistical theory, LaTeX notation, and formal proofs.
"""

from typing import Any


class ScientistAgent:
    """Agent responsible for checking mathematical rigor and LaTeX formatting."""

    def check_theory(self, text: str) -> dict[str, Any]:
        math_count = text.count("$") + text.count(r"\begin")
        has_boxed = r"\boxed" in text
        words = len(text.split())

        return {
            "word_count": words,
            "math_equation_count": math_count,
            "has_boxed_solution": has_boxed,
            "passed": words >= 800 and math_count >= 10,
        }
