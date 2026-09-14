"""
Mermaid renderer tool for converting mermaid blocks to images or HTML embeddings.
"""

import logging
import os
import shutil
import subprocess

logger = logging.getLogger(__name__)


class MermaidRenderer:
    """Renderer for Mermaid diagrams using mmdc (mermaid-cli) if available."""

    def __init__(self, output_dir: str = "docs/images"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def render_to_svg(self, mermaid_code: str, filename: str) -> str | None:
        output_path = os.path.join(self.output_dir, filename)
        tmp_mmd = os.path.join(self.output_dir, f"tmp_{filename}.mmd")

        # N-06 (auditoría 2026-09-14): subprocess.run(["npx", ...]) fallaba
        # con FileNotFoundError [WinError 2] en Windows -- Python no resuelve
        # "npx" al shim real "npx.cmd" sin shell=True. shutil.which() sí lo
        # resuelve (devuelve la ruta con extensión) y funciona igual en
        # Linux/Mac, donde "npx" normalmente no necesita extensión.
        npx_path = shutil.which("npx")
        if npx_path is None:
            logger.warning(
                "npx no está disponible en PATH; no se puede renderizar %s",
                filename,
            )
            return None

        try:
            with open(tmp_mmd, "w", encoding="utf-8") as f:
                f.write(mermaid_code)

            cmd = [
                npx_path,
                "-y",
                "@mermaid-js/mermaid-cli",
                "-i",
                tmp_mmd,
                "-o",
                output_path,
            ]
            # Timeout ampliado de 30s a 120s: la primera invocación de
            # "npx -y @mermaid-js/mermaid-cli" puede tardar más de 60s en
            # resolver el paquete (medido en la verificación de N-06).
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=120, check=False
            )

            if result.returncode == 0 and os.path.exists(output_path):
                return output_path
            logger.warning(
                "mmdc no generó %s (returncode=%s): %s",
                output_path,
                result.returncode,
                result.stderr,
            )
        except (OSError, subprocess.SubprocessError) as e:
            logger.warning("Error renderizando %s con mmdc: %s", filename, e)
        finally:
            if os.path.exists(tmp_mmd):
                os.remove(tmp_mmd)

        return None
