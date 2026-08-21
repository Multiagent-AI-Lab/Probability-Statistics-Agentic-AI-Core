"""
Mermaid diagram extraction utilities.

Incluye también MermaidNodeCounter, la utilidad compartida de generación de
IDs de nodo usada por FlowchartAgent (y potencialmente por PseudocodeAgent),
portada desde Programming-Logic para diagramas de flujo en formato Mermaid
con la convención de identificadores (node_1, node_2, ...).
"""

import re


def extract_mermaid_blocks(markdown_text: str) -> list[tuple[int, str]]:
    """Extract mermaid code blocks with their index in the document."""
    pattern = r"```mermaid\s*\n(.*?)\n```"
    matches = re.finditer(pattern, markdown_text, re.DOTALL)
    blocks = []
    for i, match in enumerate(matches):
        blocks.append((i, match.group(1).strip()))
    return blocks


class MermaidNodeCounter:
    """Genera identificadores secuenciales de nodo para diagramas Mermaid."""

    def __init__(self) -> None:
        self._count = 0

    def next_id(self) -> str:
        """Genera el siguiente identificador de nodo.

        Returns:
            Identificador con el formato "node_N", donde N inicia en 1.
        """
        self._count += 1
        return f"node_{self._count}"

    def reset(self) -> None:
        """Reinicia el contador a cero."""
        self._count = 0
