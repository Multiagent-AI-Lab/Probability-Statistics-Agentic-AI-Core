"""
NotebookCompilerAgent: Compiles markdown lesson files (lecciones/*.md) into Jupyter Notebooks (notebooks/*.ipynb).
Dividiendo limpiamente secciones (## H2 y ---) en celdas Markdown modulares.
"""

import json
import os
import re
from typing import Dict, Any, List


class NotebookCompilerAgent:
    """Agent that compiles Markdown lessons into clean, executable Jupyter Notebooks."""

    def __init__(self, lecciones_dir: str = "lecciones", notebooks_dir: str = "notebooks"):
        self.lecciones_dir = lecciones_dir
        self.notebooks_dir = notebooks_dir
        os.makedirs(notebooks_dir, exist_ok=True)

    def _sanitize_text(self, text: str) -> str:
        # Sanitizar secuencias de escape ASCII sin dejar artefactos \f o \r
        text = text.replace('\x0crac', '\\frac').replace('\x0c', '')
        text = text.replace('\x0dight', '\\right').replace('\x0d', '')
        text = text.replace('\x08ar{', '\\bar{').replace('\x08', '')
        text = text.replace('\\f\\frac', '\\frac')
        text = text.replace('\\r\\right', '\\right')
        text = text.replace('\\b\\bar', '\\bar')
        text = text.replace('$ar{X}$', '$\\bar{X}$')

        # 'ar{X}' sin 'b' previo -> '\bar{X}' (typo recurrente en lecciones)
        text = re.sub(r'(?<!b)ar\{([A-Za-z])\}', r'\\bar{\1}', text)

        # '$$\mathbf{...}$$' (bloque display de solo negrita) -> '$\mathbf{...}$' inline
        text = re.sub(r'\$\$\\mathbf\{([^}]*)\}\$\$', r'$\\mathbf{\1}$', text)

        # Typos tipograficos puntuales confirmados en el diagnostico (p. ej. U7)
        text = text.replace('\\ilde{', '\\tilde{')
        text = text.replace('\\lpha', '\\alpha')

        return text

    def _split_markdown_into_modular_cells(self, md_text: str) -> List[Dict[str, Any]]:
        cells = []
        md_text = self._sanitize_text(md_text)
        
        # Dividir por líneas divisorias --- o encabezados ## H2
        raw_sections = re.split(r'\n(?=##\s+|\n---\n)', md_text)
        
        for sec in raw_sections:
            sec_clean = sec.strip()
            # Eliminar la línea --- solitaria al inicio o final de la celda
            sec_clean = re.sub(r'^---\s*\n?', '', sec_clean).strip()
            sec_clean = re.sub(r'\n?---\s*$', '', sec_clean).strip()
            
            if sec_clean:
                cells.append({
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": sec_clean.splitlines(keepends=True)
                })
                
        return cells

    def parse_markdown_to_cells(self, md_content: str) -> List[Dict[str, Any]]:
        cells = []
        pattern = r"```(python|r|mermaid|bash|sh)?\n(.*?)```"
        pos = 0
        
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
                cells.append({
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": code_clean.splitlines(keepends=True)
                })
            else:
                cells.append({
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [f"```{lang}\n", code, "\n```"]
                })
            
            pos = end
        
        # Texto restante después del último bloque de código
        remaining = md_content[pos:].strip()
        if remaining:
            cells.extend(self._split_markdown_into_modular_cells(remaining))
            
        return cells

    def compile_file(self, md_filename: str) -> str:
        md_path = os.path.join(self.lecciones_dir, md_filename)
        if not os.path.exists(md_path):
            raise FileNotFoundError(f"Archivo lección {md_filename} no existe en {self.lecciones_dir}")
            
        with open(md_path, "r", encoding="utf-8", errors="ignore") as f:
            md_content = f.read()
            
        cells = self.parse_markdown_to_cells(md_content)
        
        nb_data = {
            "cells": cells,
            "metadata": {
                "language_info": {"name": "python"},
                "orig_nbformat": 4
            },
            "nbformat": 4,
            "nbformat_minor": 2
        }
        
        nb_filename = md_filename.replace(".md", ".ipynb")
        nb_path = os.path.join(self.notebooks_dir, nb_filename)
        
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb_data, f, indent=2, ensure_ascii=False)
            
        return nb_path
