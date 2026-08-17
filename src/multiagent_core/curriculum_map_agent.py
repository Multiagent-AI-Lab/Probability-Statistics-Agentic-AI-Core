"""
Agente Mapa Curricular (CurriculumMapAgent) - Probabilidad y Estadística UCEMICH 🗺️
======================================================================================

Genera el mapa de dependencias entre las 8 unidades del curso: sugiere
candidatos de relación de concepto entre unidades (para aprobación humana)
y renderiza el diagrama Mermaid final a partir de relaciones ya aprobadas.
Heurístico puro, sin LLM. Portado desde el repo hermano Programming-Logic,
adaptado al dominio de probabilidad y estadística.
"""

import re
from pathlib import Path
from typing import Dict, List

SKILL_METADATA = {
    "name": "curriculum_map_agent",
    "description": "Sugiere y renderiza el mapa de dependencias entre las 8 unidades del curso de Probabilidad y Estadística.",
    "version": "1.0.0",
    "input": "course_dir: Path",
    "output": "Dict[int, List[dict]] (suggest_prerequisites) | str Mermaid (render_dag)",
    "requires_api_key": False,
}

# Términos curados del dominio de Probabilidad y Estadística (equivalente
# a la lista de 19 conceptos de programación del repo hermano, adaptada).
TERMINOS_TECNICOS_CURADOS = [
    "combinatoria",
    "bayes",
    "axioma",
    "pmf",
    "pdf",
    "cdf",
    "esperanza",
    "varianza",
    "covarianza",
    "distribución conjunta",
    "distribución marginal",
    "distribución condicional",
    "normal",
    "binomial",
    "poisson",
    "monte carlo",
    "transformada inversa",
    "estimador",
    "máxima verosimilitud",
    "hipótesis",
    "p-valor",
    "chi-cuadrada",
    "t-student",
    "regresión",
    "correlación",
]

_UNIT_NUMBER_FROM_FILENAME = re.compile(r"UNIDAD_(\d+)_")
_PREREQUISITO_LINEA = re.compile(r"^- \*\*(.+?)\*\*\s*\(Unidad (\d+)\)")


def extract_fenced_blocks(markdown_text: str) -> List[tuple]:
    """Extrae bloques de código fenced (```lang\\ncode\\n```) de un texto Markdown.

    Returns:
        Lista de tuplas (match_completo, lenguaje, codigo).
    """
    pattern = r"```(\w*)\n(.*?)```"
    return [
        (m.group(0), m.group(1), m.group(2))
        for m in re.finditer(pattern, markdown_text, re.DOTALL)
    ]


class CurriculumMapAgent:
    """Agente que sugiere y renderiza el mapa de dependencias entre unidades."""

    _NOMBRES_UNIDAD = {
        1: "Estadística Descriptiva",
        2: "Probabilidad y Combinatoria",
        3: "Variables Aleatorias Discretas",
        4: "Distribuciones Conjuntas",
        5: "Variables Aleatorias Continuas",
        6: "Modelado y Simulación",
        7: "Inferencia y Estimación",
        8: "Proyecto Integrador",
    }

    def _numero_de_unidad(self, md_path: Path) -> int:
        match = _UNIT_NUMBER_FROM_FILENAME.match(md_path.name)
        return int(match.group(1)) if match else -1

    def _leer_unidades_ordenadas(self, course_dir: Path) -> List[tuple]:
        resultado = []
        for md_path in course_dir.glob("UNIDAD_*.md"):
            numero = self._numero_de_unidad(md_path)
            if numero == -1:
                continue
            content = md_path.read_text(encoding="utf-8")
            resultado.append((numero, content))
        return sorted(resultado, key=lambda t: t[0])

    def _buscar_evidencia_prosa(self, termino: str, content: str) -> str:
        for linea in content.split("\n"):
            if termino.lower() in linea.lower():
                return linea.strip()
        return ""

    def suggest_prerequisites(self, course_dir: Path) -> Dict[int, List[dict]]:
        unidades = self._leer_unidades_ordenadas(course_dir)
        resultado: Dict[int, List[dict]] = {}

        for i, (numero_actual, content_actual) in enumerate(unidades):
            candidatos: List[dict] = []
            unidades_anteriores = unidades[:i]

            for termino in TERMINOS_TECNICOS_CURADOS:
                if termino.lower() not in content_actual.lower():
                    continue
                for numero_origen, content_origen in unidades_anteriores:
                    if termino.lower() in content_origen.lower():
                        candidatos.append(
                            {
                                "unidad_origen": numero_origen,
                                "termino": termino,
                                "evidencia": self._buscar_evidencia_prosa(
                                    termino, content_actual
                                ),
                            }
                        )
                        break

            resultado[numero_actual] = candidatos

        return resultado

    def _extrae_relaciones_de_seccion(self, content: str) -> List[dict]:
        relaciones = []
        for linea in content.split("\n"):
            match = _PREREQUISITO_LINEA.match(linea.strip())
            if match:
                relaciones.append(
                    {"termino": match.group(1), "unidad_origen": int(match.group(2))}
                )
        return relaciones

    def render_dag(self, course_dir: Path) -> str:
        unidades = self._leer_unidades_ordenadas(course_dir)
        numeros_presentes = {n for n, _ in unidades}

        lineas = ["graph LR"]

        cadena = " --> ".join(f"U{n}" for n in sorted(numeros_presentes))
        if cadena:
            lineas.append(f"  {cadena}")

        for n in sorted(numeros_presentes):
            nombre = self._NOMBRES_UNIDAD.get(n, f"Unidad {n}")
            lineas.append(f"  U{n}[U{n}: {nombre}]")

        for numero_actual, content in unidades:
            for relacion in self._extrae_relaciones_de_seccion(content):
                lineas.append(
                    f"  U{relacion['unidad_origen']} -.{relacion['termino']}.-> U{numero_actual}"
                )

        return "\n".join(lineas)


if __name__ == "__main__":
    agent = CurriculumMapAgent()
    course_dir = Path(__file__).parent.parent.parent / "lecciones"
    candidatos = agent.suggest_prerequisites(course_dir)
    for unidad, lista in sorted(candidatos.items()):
        print(f"\n=== Unidad {unidad} ===")
        for c in lista:
            print(
                f"  - {c['termino']} (de Unidad {c['unidad_origen']}): {c['evidencia']}"
            )
    print("\n\n=== DAG actual (basado en secciones ya aprobadas) ===")
    print(agent.render_dag(course_dir))
