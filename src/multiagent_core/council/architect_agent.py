"""
ArchitectAgent (@Architect): Guardian of project structure, syllabus map, and memory.
"""

from typing import Any


class ArchitectAgent:
    """Agent responsible for maintaining project memory, structure, and lesson dependencies."""

    def __init__(self):
        self.units = [
            "UNIDAD_1_ESTADISTICA_DESCRIPTIVA",
            "UNIDAD_2_PROBABILIDAD_COMBINATORIA",
            "UNIDAD_3_VARIABLES_ALEATORIAS_DISCRETAS",
            "UNIDAD_4_DISTRIBUCIONES_CONJUNTAS",
            "UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS",
            "UNIDAD_6_MODELADO_SIMULACION",
            "UNIDAD_7_INFERENCIA_ESTIMACION",
            "UNIDAD_8_PROYECTO_INTEGRADOR",
        ]

    def validate_structure(self, file_tree: list[str]) -> dict[str, Any]:
        missing = [u for u in self.units if not any(u in f for f in file_tree)]
        return {
            "valid": len(missing) == 0,
            "missing_units": missing,
            "total_units": len(self.units),
        }
