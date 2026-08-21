"""
Mermaid renderer tool for converting mermaid blocks to images or HTML embeddings.
"""

import logging
import os
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

        try:
            with open(tmp_mmd, "w", encoding="utf-8") as f:
                f.write(mermaid_code)

            # Run mmdc if installed via npx
            cmd = [
                "npx",
                "-y",
                "@mermaid-js/mermaid-cli",
                "-i",
                tmp_mmd,
                "-o",
                output_path,
            ]
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=30, check=False
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
