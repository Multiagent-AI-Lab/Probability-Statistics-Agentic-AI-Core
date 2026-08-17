"""
EngineerAgent (@Engineer): Code builder using SciPy, Statsmodels, Pandas, SymPy, NumPy.
"""

import re
from typing import Any, Dict, List


class EngineerAgent:
    """Agent responsible for checking code quality, type hints, SciPy/Statsmodels usage, and Monte Carlo convergence."""

    _SAMPLE_COUNT_PATTERN = re.compile(
        r"\b(?:N|n)_?(?:sim|muestras|samples|iter|iteraciones)\s*=\s*(\d[\d_]*)",
        re.IGNORECASE,
    )

    def check_code_implementation(self, code_text: str) -> Dict[str, Any]:
        has_scipy = "scipy" in code_text or "statsmodels" in code_text
        has_display_math = "display" in code_text and "Math" in code_text

        return {
            "has_scipy_or_statsmodels": has_scipy,
            "has_display_math": has_display_math,
            "passed": has_scipy,
        }

    def check_monte_carlo_convergence(
        self, code_text: str, min_iterations: int = 1000
    ) -> Dict[str, Any]:
        """Valida que el numero de iteraciones/muestras declarado en codigo de
        simulacion sea suficiente para convergencia razonable, adaptando el
        patron de stability_guardian.analyze_timestep (Antigravity-Nano) al
        dominio estadistico: convergencia Monte Carlo es O(1/sqrt(N)), no
        lineal, asi que un N bajo produce estimaciones con alta varianza."""
        warnings: List[str] = []
        matches = self._SAMPLE_COUNT_PATTERN.findall(code_text)

        for raw_value in matches:
            n = int(raw_value.replace("_", ""))
            if n < min_iterations:
                warnings.append(
                    f"Número de iteraciones/muestras ({n}) por debajo del "
                    f"mínimo recomendado ({min_iterations}) para convergencia "
                    f"Monte Carlo razonable (error ~ O(1/sqrt(N)))."
                )

        return {
            "critical": len(warnings) > 0,
            "warnings": warnings,
        }
