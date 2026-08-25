"""
Empaqueta bibliografia/*.pdf + un índice ChromaDB pre-generado en un .zip
listo para distribuir a los alumnos (evita que cada alumno tenga que
reindexar los 9 libros completos desde cero, proceso que puede tardar
horas).

A diferencia de scripts/pregenerar_indice_bibliografia.py (que indexa
sobre lecciones/.chroma, el índice de trabajo de este repo), este script
construye el índice en dist/bibliografia_paquete/.chroma -- una ruta
ASCII-safe dentro del repo, para que quede embebido en el paquete sin
depender de rutas de esta máquina (a diferencia de lecciones/.chroma, que
en este repo se redirige a %TEMP% por contener un acento).

Los PDFs tienen copyright y dist/ está en .gitignore: este script nunca
publica nada en git, solo genera un artefacto local para distribuir por
fuera (Drive, Classroom, USB).

Uso: python scripts/empaquetar_distribucion_bibliografia.py
"""

import logging
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = Path(__file__).resolve().parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from pregenerar_indice_bibliografia import BIBLIOGRAFIA_DIR
from pregenerar_indice_bibliografia import main as indexar_bibliografia

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

DIST_DIR = REPO_ROOT / "dist"
PAQUETE_DIR = DIST_DIR / "bibliografia_paquete"
PAQUETE_CHROMA_PATH = PAQUETE_DIR / ".chroma"
PAQUETE_BIBLIOGRAFIA_DIR = PAQUETE_DIR / "bibliografia"
ZIP_BASENAME = DIST_DIR / "bibliografia_paquete"


def _copiar_pdfs(origen: Path, destino: Path) -> int:
    """Copia los PDFs de `origen` a `destino`, creando el directorio
    destino si no existe. Devuelve cuántos PDFs se copiaron."""
    destino.mkdir(parents=True, exist_ok=True)
    pdfs = sorted(origen.glob("*.pdf"))
    for pdf in pdfs:
        shutil.copy2(pdf, destino / pdf.name)
    return len(pdfs)


def main() -> None:
    if not BIBLIOGRAFIA_DIR.is_dir() or not list(BIBLIOGRAFIA_DIR.glob("*.pdf")):
        logger.error("No hay PDFs en %s -- nada que empaquetar.", BIBLIOGRAFIA_DIR)
        return

    logger.info("Copiando PDFs a %s ...", PAQUETE_BIBLIOGRAFIA_DIR)
    n_copiados = _copiar_pdfs(BIBLIOGRAFIA_DIR, PAQUETE_BIBLIOGRAFIA_DIR)
    logger.info("Copiados %d PDFs.", n_copiados)

    logger.info(
        "Construyendo índice ChromaDB en %s (esto puede tardar varios " "minutos)...",
        PAQUETE_CHROMA_PATH,
    )
    pdfs_fallidos = indexar_bibliografia(
        bibliografia_dir=PAQUETE_BIBLIOGRAFIA_DIR, chroma_path=PAQUETE_CHROMA_PATH
    )
    if pdfs_fallidos:
        logger.error(
            "Abortando empaquetado: %d PDF(s) no se pudieron indexar (%s). "
            "El paquete distribuiría un índice incompleto sin que sea "
            "evidente para el alumno. Vuelve a correr este script para "
            "reintentar (upsert no duplica los PDFs ya indexados).",
            len(pdfs_fallidos),
            ", ".join(pdfs_fallidos),
        )
        return

    logger.info("Comprimiendo paquete en %s.zip ...", ZIP_BASENAME)
    ruta_zip = shutil.make_archive(
        base_name=str(ZIP_BASENAME), format="zip", root_dir=str(PAQUETE_DIR)
    )

    tamano_mb = Path(ruta_zip).stat().st_size / (1024 * 1024)
    logger.info(
        "Paquete listo: %s (%.1f MB). Contiene bibliografia/*.pdf + .chroma "
        "ya indexado -- los alumnos solo necesitan descomprimirlo dentro de "
        "la carpeta del curso.",
        ruta_zip,
        tamano_mb,
    )


if __name__ == "__main__":
    main()
