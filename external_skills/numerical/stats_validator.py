"""
StatsValidator Skill: Validates numerical results of statistical calculations (scipy.stats).
"""

from typing import Dict, Any
import numpy as np


class StatsValidator:
    """Skill for validating statistical numerical calculations."""

    def validate_mean_std(self, data: list, expected_mean: float, expected_std: float, tol: float = 1e-3) -> Dict[str, Any]:
        arr = np.array(data)
        calc_mean = float(np.mean(arr))
        calc_std = float(np.std(arr, ddof=1))
        
        mean_ok = abs(calc_mean - expected_mean) <= tol
        std_ok = abs(calc_std - expected_std) <= tol
        
        return {
            "valid": mean_ok and std_ok,
            "calculated_mean": calc_mean,
            "calculated_std": calc_std,
            "expected_mean": expected_mean,
            "expected_std": expected_std
        }
