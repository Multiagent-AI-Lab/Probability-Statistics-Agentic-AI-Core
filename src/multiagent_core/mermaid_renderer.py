"""
Mermaid renderer tool for converting mermaid blocks to images or HTML embeddings.
"""

import json
import logging
import os
import re
import shutil
import subprocess
import tempfile

logger = logging.getLogger(__name__)

# Nombre de archivo seguro para render_to_svg: solo letras, dígitos, "_", "."
# y "-", terminado en ".svg". Una allowlist cierra por construcción cualquier
# separador de ruta (en cualquier plataforma), null bytes, prefijos de unidad
# de Windows ("C:algo.svg") y caracteres unicode look-alike de separadores --
# sin necesitar enumerar cada vector conocido como haría una denylist.
_FILENAME_SVG_SEGURO = re.compile(r"^[A-Za-z0-9_.-]+\.svg$")


class MermaidRenderer:
    """Renderer for Mermaid diagrams using mmdc (mermaid-cli) if available."""

    def __init__(self, output_dir: str = "docs/images"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def render_to_svg(self, mermaid_code: str, filename: str) -> str | None:
        # Defensa en profundidad (revisión de seguridad, 2026-09-14, endurecida
        # 2026-09-17 tras un fallo real de CI en ubuntu-latest): filename hoy
        # solo llega desde notebook_compiler_agent.py, construido a partir del
        # nombre de unidad + un contador (sin separadores de ruta), pero esta
        # función es reutilizable y no debe depender de que su único llamador
        # actual siga siendo "seguro por construcción".
        #
        # Allowlist en vez de denylist de separadores: la versión anterior
        # (`os.path.basename(filename) != filename`) interpreta separadores
        # según la plataforma en la que corre -- en Linux/Mac "\" es un
        # carácter de nombre válido, así que "..\fuera\escape.svg" pasaba sin
        # cambios (confirmado por un fallo real de CI: el test
        # test_filename_con_separador_windows_se_rechaza fallaba con "DID NOT
        # RAISE ValueError" en ubuntu-latest). La allowlist cierra ese caso y,
        # de paso, cualquier otro vector no enumerado explícitamente (un
        # prefijo de unidad de Windows como "C:algo.svg", null bytes,
        # unicode look-alike de separadores) sin depender de la plataforma.
        if not _FILENAME_SVG_SEGURO.fullmatch(filename):
            raise ValueError(f"filename inválido (no puede contener rutas): {filename}")

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

        tmp_puppeteer_config = None
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

            # Runners de GitHub Actions (ubuntu-latest 24.04+) restringen
            # namespaces de usuario sin privilegios vía AppArmor, y el
            # sandbox de Chromium que Puppeteer lanza internamente falla con
            # "No usable sandbox!" (ver
            # https://github.com/mermaid-js/mermaid-cli/blob/master/docs/linux-sandbox-issue.md).
            # --no-sandbox reduce el aislamiento del proceso Chromium, así
            # que solo se activa cuando la variable de entorno CI está
            # presente (GitHub Actions la define automáticamente) -- en
            # cualquier máquina de desarrollo o del curso, el comando queda
            # exactamente igual que antes de este fix.
            if os.environ.get("CI"):
                fd, tmp_puppeteer_config = tempfile.mkstemp(suffix=".json")
                with os.fdopen(fd, "w", encoding="utf-8") as f:
                    json.dump({"args": ["--no-sandbox", "--disable-setuid-sandbox"]}, f)
                cmd.extend(["-p", tmp_puppeteer_config])

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
            if tmp_puppeteer_config and os.path.exists(tmp_puppeteer_config):
                os.remove(tmp_puppeteer_config)

        return None
