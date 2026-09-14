"""
NotebookCompilerAgent: Compiles markdown lesson files (lecciones/*.md) into Jupyter Notebooks (notebooks/*.ipynb).
Dividiendo limpiamente secciones (## H2 y ---) en celdas Markdown modulares.
"""

import json
import os
import re
from typing import Any, ClassVar

from .flowchart_agent import FlowchartAgent
from .mermaid_renderer import MermaidRenderer


class NotebookCompilerAgent:
    """Agent that compiles Markdown lessons into clean, executable Jupyter Notebooks."""

    FLOWCHART_ENABLED_UNITS: ClassVar[set[str]] = {"UNIDAD_6_MODELADO_SIMULACION.md"}

    def __init__(
        self, lecciones_dir: str = "lecciones", notebooks_dir: str = "notebooks"
    ):
        self.lecciones_dir = lecciones_dir
        self.notebooks_dir = notebooks_dir
        os.makedirs(notebooks_dir, exist_ok=True)
        self.flowchart_agent = FlowchartAgent()

    def _sanitize_text(self, text: str) -> str:
        # Sanitizar secuencias de escape ASCII sin dejar artefactos \f o \r
        text = text.replace("\x0crac", "\\frac").replace("\x0c", "")
        text = text.replace("\x0dight", "\\right").replace("\x0d", "")
        text = text.replace("\x08ar{", "\\bar{").replace("\x08", "")
        text = text.replace("\\f\\frac", "\\frac")
        text = text.replace("\\r\\right", "\\right")
        text = text.replace("\\b\\bar", "\\bar")
        text = text.replace("$ar{X}$", "$\\bar{X}$")

        # 'ar{X}' sin backslash previo -> '\bar{X}' (typo recurrente en lecciones).
        # El caracter antes de 'ar{' debe ser inicio de linea/espacio/$ para no
        # corromper palabras como 'covar{...}' o 'similar{...}'.
        text = re.sub(r"(?<![\\a-zA-Z])ar\{([A-Za-z])\}", r"\\bar{\1}", text)

        # '$$\mathbf{...}$$' (bloque display de solo negrita) -> '$\mathbf{...}$' inline
        text = re.sub(r"\$\$\\mathbf\{([^}]*)\}\$\$", r"$\\mathbf{\1}$", text)

        # Typos tipograficos puntuales confirmados en el diagnostico (p. ej. U7)
        text = text.replace("\\ilde{", "\\tilde{")
        text = text.replace("\\lpha", "\\alpha")

        return text

    def _split_markdown_into_modular_cells(self, md_text: str) -> list[dict[str, Any]]:
        cells = []
        md_text = self._sanitize_text(md_text)

        # Dividir por líneas divisorias --- o encabezados ## H2
        raw_sections = re.split(r"\n(?=##\s+|\n---\n)", md_text)

        for sec in raw_sections:
            sec_clean = sec.strip()
            # Eliminar la línea --- solitaria al inicio o final de la celda
            sec_clean = re.sub(r"^---\s*\n?", "", sec_clean).strip()
            sec_clean = re.sub(r"\n?---\s*$", "", sec_clean).strip()

            if sec_clean:
                cells.append(
                    {
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": sec_clean.splitlines(keepends=True),
                    }
                )

        return cells

    def parse_markdown_to_cells(
        self, md_content: str, md_filename: str = ""
    ) -> list[dict[str, Any]]:
        cells = []
        pattern = r"```(python|r|mermaid|bash|sh)?\n(.*?)```"
        pos = 0
        contador_mermaid = 0

        for match in re.finditer(pattern, md_content, re.DOTALL):
            start, end = match.span()
            lang = match.group(1) or ""
            code = match.group(2)

            # Texto Markdown antes del código
            md_text = md_content[pos:start].strip()
            if md_text:
                cells.extend(self._split_markdown_into_modular_cells(md_text))

            if lang.lower() in ["python", "r"]:
                code_clean = self._sanitize_text(code)
                cells.append(
                    {
                        "cell_type": "code",
                        "execution_count": None,
                        "metadata": {},
                        "outputs": [],
                        "source": code_clean.splitlines(keepends=True),
                    }
                )
                if (
                    md_filename in self.FLOWCHART_ENABLED_UNITS
                    and lang.lower() == "python"
                    and "def " in code_clean
                    and len(code_clean.strip().splitlines()) > 5
                ):
                    mermaid_diagram = self.flowchart_agent.build_mermaid_flowchart(
                        code_clean
                    )
                    if not mermaid_diagram.startswith("%%"):
                        cells.append(
                            {
                                "cell_type": "markdown",
                                "metadata": {},
                                "source": [
                                    "<details><summary>📊 Diagrama de flujo (auto-generado)</summary>\n\n",
                                    f"```mermaid\n{mermaid_diagram}\n```\n\n",
                                    "</details>\n",
                                ],
                            }
                        )
            else:
                source = [f"```{lang}\n", code, "\n```"]
                if lang.lower() == "mermaid":
                    contador_mermaid += 1
                    nombre_base = md_filename.removesuffix(".md")
                    nombre_svg = (
                        f"{nombre_base}_{contador_mermaid}.svg"
                        if nombre_base
                        else f"diagrama_{contador_mermaid}.svg"
                    )
                    svg_path = MermaidRenderer().render_to_svg(code, nombre_svg)
                    if svg_path:
                        # render_to_svg devuelve una ruta relativa a la raíz
                        # del repo (donde corre el proceso de compilación),
                        # pero el .ipynb se guarda en self.notebooks_dir --
                        # sin recalcular, el markdown del notebook resolvería
                        # la imagen desde notebooks_dir/docs/images/..., que
                        # no existe. os.path.relpath la recalcula relativa a
                        # notebooks_dir, cualquiera sea su profundidad real.
                        ruta_desde_notebook = os.path.relpath(
                            svg_path, start=self.notebooks_dir
                        ).replace(os.sep, "/")
                        source.append(f"\n\n![Diagrama]({ruta_desde_notebook})\n")
                cells.append(
                    {
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": source,
                    }
                )

            pos = end

        # Texto restante después del último bloque de código
        remaining = md_content[pos:].strip()
        if remaining:
            cells.extend(self._split_markdown_into_modular_cells(remaining))

        return cells

    def compile_file(self, md_filename: str) -> str:
        md_path = os.path.join(self.lecciones_dir, md_filename)
        if not os.path.exists(md_path):
            raise FileNotFoundError(
                f"Archivo lección {md_filename} no existe en {self.lecciones_dir}"
            )

        with open(md_path, "r", encoding="utf-8", errors="ignore") as f:
            md_content = f.read()

        cells = self.parse_markdown_to_cells(md_content, md_filename=md_filename)

        nb_data = {
            "cells": cells,
            "metadata": {
                "language_info": {"name": "python"},
                "orig_nbformat": 4,
                # I-5 (auditoría 2026-09-14): sin kernelspec, nbconvert
                # --execute cae al kernel "python3" del sistema en vez del
                # entorno del proyecto -- ModuleNotFoundError engañoso que
                # enmascara errores reales. Se usa el nombre genérico
                # "python3" (no un entorno conda específico como "ia_stats")
                # para no atar el repo al nombre local del entorno del
                # profesor; cualquier kernel registrado como "python3"
                # (el nombre por defecto de `ipykernel install`) sirve.
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3",
                },
            },
            "nbformat": 4,
            "nbformat_minor": 2,
        }

        nb_filename = md_filename.replace(".md", ".ipynb")
        nb_path = os.path.join(self.notebooks_dir, nb_filename)

        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb_data, f, indent=2, ensure_ascii=False)

        return nb_path
