"""
Tests for NotebookCompilerAgent.
"""

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


def test_sanitize_does_not_corrupt_spanish_words_ending_in_ar_before_brace():
    compiler = NotebookCompilerAgent()
    text = "La covar{Y} es una palabra valida, igual que similar{Z}."
    result = compiler._sanitize_text(text)
    assert result == text


def test_flowchart_agent_se_activa_solo_en_unidad_6(tmp_path):
    from src.multiagent_core.notebook_compiler_agent import NotebookCompilerAgent

    lecciones_dir = tmp_path / "lecciones"
    lecciones_dir.mkdir()
    notebooks_dir = tmp_path / "notebooks"

    contenido_con_funcion = """# UNIDAD 6 MODELADO Y SIMULACION

## 1. Simulación Monte Carlo

```python
def estimar_pi_monte_carlo(n_muestras):
    dentro = 0
    for i in range(n_muestras):
        if i % 2 == 0:
            dentro = dentro + 1
    return dentro / n_muestras
```
"""
    (lecciones_dir / "UNIDAD_6_MODELADO_SIMULACION.md").write_text(
        contenido_con_funcion, encoding="utf-8"
    )
    (lecciones_dir / "UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md").write_text(
        contenido_con_funcion.replace("UNIDAD 6 MODELADO Y SIMULACION", "UNIDAD 1"),
        encoding="utf-8",
    )

    compiler = NotebookCompilerAgent(
        lecciones_dir=str(lecciones_dir), notebooks_dir=str(notebooks_dir)
    )
    nb_path_u6 = compiler.compile_file("UNIDAD_6_MODELADO_SIMULACION.md")
    nb_path_u1 = compiler.compile_file("UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md")

    import json

    with open(nb_path_u6, encoding="utf-8") as f:
        nb_u6 = json.load(f)
    with open(nb_path_u1, encoding="utf-8") as f:
        nb_u1 = json.load(f)

    u6_has_mermaid = any(
        "graph TD" in "".join(cell.get("source", []))
        for cell in nb_u6["cells"]
        if cell["cell_type"] == "markdown"
    )
    u1_has_mermaid = any(
        "graph TD" in "".join(cell.get("source", []))
        for cell in nb_u1["cells"]
        if cell["cell_type"] == "markdown"
    )

    assert u6_has_mermaid is True
    assert u1_has_mermaid is False
