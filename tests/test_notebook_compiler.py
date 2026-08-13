"""
Tests for NotebookCompilerAgent.
"""

import os
from src.multiagent_core.notebook_compiler_agent import NotebookCompilerAgent


def test_parse_markdown_to_cells():
    compiler = NotebookCompilerAgent()
    md_content = """# Title
    
Some text explanation.

```python
import numpy as np
print("Hello World")
```
"""
    cells = compiler.parse_markdown_to_cells(md_content)
    assert len(cells) >= 2
    assert cells[0]["cell_type"] == "markdown"
    assert cells[1]["cell_type"] == "code"


def test_sanitize_fixes_bar_without_backslash():
    compiler = NotebookCompilerAgent()
    result = compiler._sanitize_text("La media es ar{X} y tambien ar{Y}.")
    assert result == "La media es \\bar{X} y tambien \\bar{Y}."


def test_sanitize_preserves_existing_bar():
    compiler = NotebookCompilerAgent()
    result = compiler._sanitize_text("La media es \\bar{X}.")
    assert result == "La media es \\bar{X}."


def test_sanitize_fixes_mathbf_display_block():
    compiler = NotebookCompilerAgent()
    result = compiler._sanitize_text("Resultado: $$\\mathbf{0.45}$$ es el valor.")
    assert result == "Resultado: $\\mathbf{0.45}$ es el valor."


def test_sanitize_fixes_tilde_typo():
    compiler = NotebookCompilerAgent()
    result = compiler._sanitize_text("El estimador es \\ilde{X}.")
    assert result == "El estimador es \\tilde{X}."


def test_sanitize_fixes_alpha_typo():
    compiler = NotebookCompilerAgent()
    result = compiler._sanitize_text("El nivel de significancia es \\lpha = 0.05.")
    assert result == "El nivel de significancia es \\alpha = 0.05."


def test_sanitize_does_not_touch_matplotlib_alpha_kwarg():
    compiler = NotebookCompilerAgent()
    code = "plt.plot(x, y, alpha=0.6)"
    result = compiler._sanitize_text(code)
    assert result == code

