"""
Tests para MermaidRenderer.render_to_svg -- wrapper de mmdc (mermaid-cli)
vía subprocess. subprocess.run se mockea: no depende de tener npx/mmdc
instalado para correr en CI.
"""

import subprocess
from unittest.mock import MagicMock, patch

from src.multiagent_core.mermaid_renderer import MermaidRenderer


@patch("src.multiagent_core.mermaid_renderer.subprocess.run")
@patch("src.multiagent_core.mermaid_renderer.os.path.exists")
def test_render_exitoso_retorna_el_output_path(mock_exists, mock_run, tmp_path):
    mock_run.return_value = MagicMock(returncode=0, stderr="")
    mock_exists.return_value = True

    renderer = MermaidRenderer(output_dir=str(tmp_path))
    resultado = renderer.render_to_svg("graph TD\nA --> B", "diagrama.svg")

    assert resultado == str(tmp_path / "diagrama.svg")


@patch("src.multiagent_core.mermaid_renderer.subprocess.run")
def test_returncode_distinto_de_cero_retorna_none(mock_run, tmp_path):
    mock_run.return_value = MagicMock(returncode=1, stderr="mmdc no encontrado")

    renderer = MermaidRenderer(output_dir=str(tmp_path))
    resultado = renderer.render_to_svg("graph TD\nA --> B", "diagrama.svg")

    assert resultado is None


@patch("src.multiagent_core.mermaid_renderer.subprocess.run")
def test_timeout_de_subprocess_no_propaga_excepcion(mock_run, tmp_path):
    mock_run.side_effect = subprocess.TimeoutExpired(cmd="npx", timeout=30)

    renderer = MermaidRenderer(output_dir=str(tmp_path))
    resultado = renderer.render_to_svg("graph TD\nA --> B", "diagrama.svg")

    assert resultado is None


@patch("src.multiagent_core.mermaid_renderer.subprocess.run")
def test_archivo_temporal_se_elimina_incluso_si_falla(mock_run, tmp_path):
    mock_run.return_value = MagicMock(returncode=1, stderr="error")

    renderer = MermaidRenderer(output_dir=str(tmp_path))
    renderer.render_to_svg("graph TD\nA --> B", "diagrama.svg")

    tmp_mmd = tmp_path / "tmp_diagrama.svg.mmd"
    assert not tmp_mmd.exists()


def test_constructor_crea_el_directorio_de_salida_si_no_existe(tmp_path):
    output_dir = tmp_path / "nuevo_subdir"

    MermaidRenderer(output_dir=str(output_dir))

    assert output_dir.exists()
