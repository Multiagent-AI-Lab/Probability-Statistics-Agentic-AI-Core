"""Tests for ArchitectAgent."""

from src.multiagent_core.council.architect_agent import ArchitectAgent


def test_units_lists_all_8_current_unit_names():
    agent = ArchitectAgent()
    assert len(agent.units) == 8
    assert "UNIDAD_6_MODELADO_SIMULACION" in agent.units
    assert "UNIDAD_7_INFERENCIA_ESTIMACION" in agent.units
    assert "UNIDAD_8_PROYECTO_INTEGRADOR" in agent.units


def test_validate_structure_passes_with_real_file_tree():
    agent = ArchitectAgent()
    file_tree = [
        "UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md",
        "UNIDAD_2_PROBABILIDAD_COMBINATORIA.md",
        "UNIDAD_3_VARIABLES_ALEATORIAS_DISCRETAS.md",
        "UNIDAD_4_DISTRIBUCIONES_CONJUNTAS.md",
        "UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.md",
        "UNIDAD_6_MODELADO_SIMULACION.md",
        "UNIDAD_7_INFERENCIA_ESTIMACION.md",
        "UNIDAD_8_PROYECTO_INTEGRADOR.md",
    ]
    result = agent.validate_structure(file_tree)
    assert result["valid"] is True
    assert result["missing_units"] == []
    assert result["total_units"] == 8
