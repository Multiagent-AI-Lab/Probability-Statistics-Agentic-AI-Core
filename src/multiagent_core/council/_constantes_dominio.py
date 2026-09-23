"""
Tabla curada de constantes físicas/matemáticas del dominio del curso, para
que SemanticAuditorAgent contraste afirmaciones de prosa contra un hecho
determinista -- nunca contra lo que el LLM "recuerde" como valor correcto
(ver docs/superpowers/specs/2026-09-23-semantic-auditor-agent-design.md,
sección "Riesgos y decisiones").

Cada entrada se agrega solo cuando la constante aparece citada POR NOMBRE
en prosa en al menos una de las 8 unidades reales (verificado por grep) --
mismo principio conservador que el resto del Consejo: no auditar contra un
catálogo genérico de física, solo contra lo que el curso de hecho enseña.

Valores verificados contra CODATA 2022 (https://physics.nist.gov/cuu/Constants/).
"""

import re

# nombre_normalizado -> (valor_correcto, unidad, tolerancia_relativa)
CONSTANTES_CONOCIDAS: dict[str, tuple[float, str, float]] = {
    "constante de boltzmann": (1.380649e-23, "J/K", 1e-4),
    "numero de avogadro": (6.02214076e23, "mol^-1", 1e-4),
}


def normalizar_nombre_constante(nombre: str) -> str:
    """Minúsculas, sin acentos, espacios colapsados -- para que "Constante
    de Boltzmann" y "CONSTANTE  DE BOLTZMANN" busquen la misma clave."""
    sin_acentos = (
        nombre.lower()
        .replace("á", "a")
        .replace("é", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ú", "u")
        .replace("ñ", "n")
    )
    return re.sub(r"\s+", " ", sin_acentos).strip()
