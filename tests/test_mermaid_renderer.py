"""
Tests para MermaidRenderer.render_to_svg -- wrapper de mmdc (mermaid-cli)
vía subprocess. subprocess.run se mockea: no depende de tener npx/mmdc
instalado para correr en CI.
"""

import os
import shutil as _shutil_real  # alias para no chocar con el shutil mockeado abajo
import subprocess
from unittest.mock import MagicMock, patch

import pytest

from src.multiagent_core.mermaid_renderer import MermaidRenderer


@patch("src.multiagent_core.mermaid_renderer.shutil.which")
@patch("src.multiagent_core.mermaid_renderer.subprocess.run")
@patch("src.multiagent_core.mermaid_renderer.os.path.exists")
def test_render_exitoso_retorna_el_output_path(
    mock_exists, mock_run, mock_which, tmp_path
):
    mock_which.return_value = "C:\\fake\\npx.CMD"
    mock_run.return_value = MagicMock(returncode=0, stderr="")
    mock_exists.return_value = True

    renderer = MermaidRenderer(output_dir=str(tmp_path))
    resultado = renderer.render_to_svg("graph TD\nA --> B", "diagrama.svg")

    assert resultado == str(tmp_path / "diagrama.svg")


@patch("src.multiagent_core.mermaid_renderer.shutil.which")
@patch("src.multiagent_core.mermaid_renderer.subprocess.run")
def test_returncode_distinto_de_cero_retorna_none(mock_run, mock_which, tmp_path):
    mock_which.return_value = "C:\\fake\\npx.CMD"
    mock_run.return_value = MagicMock(returncode=1, stderr="mmdc no encontrado")

    renderer = MermaidRenderer(output_dir=str(tmp_path))
    resultado = renderer.render_to_svg("graph TD\nA --> B", "diagrama.svg")

    assert resultado is None


@patch("src.multiagent_core.mermaid_renderer.shutil.which")
@patch("src.multiagent_core.mermaid_renderer.subprocess.run")
def test_timeout_de_subprocess_no_propaga_excepcion(mock_run, mock_which, tmp_path):
    mock_which.return_value = "C:\\fake\\npx.CMD"
    mock_run.side_effect = subprocess.TimeoutExpired(cmd="npx", timeout=30)

    renderer = MermaidRenderer(output_dir=str(tmp_path))
    resultado = renderer.render_to_svg("graph TD\nA --> B", "diagrama.svg")

    assert resultado is None


@patch("src.multiagent_core.mermaid_renderer.shutil.which")
@patch("src.multiagent_core.mermaid_renderer.subprocess.run")
def test_archivo_temporal_se_elimina_incluso_si_falla(mock_run, mock_which, tmp_path):
    mock_which.return_value = "C:\\fake\\npx.CMD"
    mock_run.return_value = MagicMock(returncode=1, stderr="error")

    renderer = MermaidRenderer(output_dir=str(tmp_path))
    renderer.render_to_svg("graph TD\nA --> B", "diagrama.svg")

    tmp_mmd = tmp_path / "tmp_diagrama.svg.mmd"
    assert not tmp_mmd.exists()


def test_constructor_crea_el_directorio_de_salida_si_no_existe(tmp_path):
    output_dir = tmp_path / "nuevo_subdir"

    MermaidRenderer(output_dir=str(output_dir))

    assert output_dir.exists()


@patch("src.multiagent_core.mermaid_renderer.shutil.which")
def test_npx_no_disponible_retorna_none_sin_excepcion(mock_which, tmp_path):
    """N-06 (auditoría 2026-09-14): antes del fix, subprocess.run(["npx", ...])
    fallaba con FileNotFoundError [WinError 2] en Windows porque npx no
    resuelve a un ejecutable directo sin shell=True (el shim real es
    npx.cmd). Si npx ni siquiera está en el PATH, render_to_svg debe
    degradar a None sin lanzar excepción -no debe intentar invocar
    subprocess.run con un comando inválido."""
    mock_which.return_value = None

    renderer = MermaidRenderer(output_dir=str(tmp_path))
    resultado = renderer.render_to_svg("graph TD\nA --> B", "diagrama.svg")

    assert resultado is None


@pytest.mark.skipif(
    _shutil_real.which("npx") is None, reason="requiere npx/Node instalado"
)
def test_integracion_real_genera_svg_en_disco(tmp_path):
    """N-06: confirma que, con npx real disponible, render_to_svg produce
    un archivo .svg de verdad -- los tests de arriba mockean subprocess.run,
    así que un verde ahí no dice nada sobre si el render ocurre en la
    práctica (exactamente el gap que la auditoría señaló). Puede tardar
    hasta 2 minutos en su primera ejecución si npx necesita resolver el
    paquete @mermaid-js/mermaid-cli."""
    renderer = MermaidRenderer(output_dir=str(tmp_path))
    resultado = renderer.render_to_svg(
        "graph TD\n  A[Inicio] --> B[Fin]", "prueba_integracion.svg"
    )

    assert resultado is not None, (
        "render_to_svg devolvió None con npx disponible -- revisar "
        "shutil.which y el timeout de subprocess.run"
    )
    assert os.path.exists(resultado), f"el archivo {resultado} no existe en disco"
