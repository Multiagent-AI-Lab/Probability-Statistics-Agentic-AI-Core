"""Tests for _constantes_dominio: tabla curada de constantes del curso.

Cada valor está verificado contra CODATA -- mismo estándar que la
verificación de la fórmula de Bohr en el repo hermano de Lógica de
Programación (ver GOVERNANCE.md de este repo, sección de precisión de
dominio)."""

from src.multiagent_core.council._constantes_dominio import (
    CONSTANTES_CONOCIDAS,
    normalizar_nombre_constante,
)


def test_constante_de_boltzmann_tiene_el_valor_codata_correcto():
    valor, unidad, _tolerancia = CONSTANTES_CONOCIDAS["constante de boltzmann"]
    assert abs(valor - 1.380649e-23) / 1.380649e-23 < 1e-6
    assert unidad == "J/K"


def test_numero_de_avogadro_tiene_el_valor_codata_correcto():
    valor, _unidad, _tolerancia = CONSTANTES_CONOCIDAS["numero de avogadro"]
    assert abs(valor - 6.02214076e23) / 6.02214076e23 < 1e-6


def test_normalizar_nombre_constante_ignora_mayusculas_y_espacios_extra():
    assert (
        normalizar_nombre_constante("Constante  de Boltzmann")
        == "constante de boltzmann"
    )
    assert normalizar_nombre_constante("NÚMERO DE AVOGADRO") == "numero de avogadro"


def test_normalizar_nombre_constante_desconocida_no_lanza():
    # Una constante fuera de la tabla se normaliza igual -- es el llamador
    # (SemanticAuditorAgent) quien decide abstenerse si no está en la tabla,
    # no esta función.
    resultado = normalizar_nombre_constante("constante inventada de prueba")
    assert resultado not in CONSTANTES_CONOCIDAS
