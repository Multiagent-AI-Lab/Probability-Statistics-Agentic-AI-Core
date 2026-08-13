"""
Mermaid diagram extraction utilities.
"""

import re
from typing import List, Tuple


def extract_mermaid_blocks(markdown_text: str) -> List[Tuple[int, str]]:
    """Extract mermaid code blocks with their index in the document."""
    pattern = r"```mermaid\s*\n(.*?)\n```"
    matches = re.finditer(pattern, markdown_text, re.DOTALL)
    blocks = []
    for i, match in enumerate(matches):
        blocks.append((i, match.group(1).strip()))
    return blocks
