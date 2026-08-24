"""
Pre-genera el índice ChromaDB de bibliografia/ para distribuir a los
alumnos junto con los PDFs (evita que cada alumno tenga que reindexar
los 9 libros completos desde cero, proceso que puede tardar horas).

Procesa los PDFs en paralelo (ThreadPoolExecutor) y guarda cada uno en
ChromaDB inmediatamente después de extraerlo -- si el script se
interrumpe, los PDFs ya procesados quedan guardados; solo hace falta
volver a correrlo para completar los que falten (usa upsert por ID de
chunk, así que reprocesar un PDF ya guardado no genera duplicados).

Uso: python scripts/pregenerar_indice_bibliografia.py
"""

import logging
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

from src.multiagent_core.pdf_indexer import index_pdf
from src.multiagent_core.stats_tutor_agent import (
    BIBLIOGRAFIA_COLLECTION_NAME,
    BIBLIOGRAFIA_MAX_CHARS_POR_CHUNK,
    EMBEDDING_MODEL_NAME,
    resolver_chroma_path_seguro,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

BIBLIOGRAFIA_DIR = REPO_ROOT / "bibliografia"
CHROMA_PATH = resolver_chroma_path_seguro(REPO_ROOT / "lecciones" / ".chroma")
MAX_WORKERS = 4


def _get_or_create_bibliografia_collection(
    client: chromadb.ClientAPI,
) -> chromadb.Collection:
    """Réplica del mismo patrón de StatsTutorAgent para no depender de
    instanciar el agente completo (que también indexaría lecciones/DOIs,
    innecesario para este script)."""
    embedding_function = SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL_NAME
    )
    try:
        return client.get_or_create_collection(
            BIBLIOGRAFIA_COLLECTION_NAME, embedding_function=embedding_function
        )
    except ValueError as e:
        if "Embedding function conflict" not in str(e):
            raise
        client.delete_collection(BIBLIOGRAFIA_COLLECTION_NAME)
        return client.get_or_create_collection(
            BIBLIOGRAFIA_COLLECTION_NAME, embedding_function=embedding_function
        )


def _procesar_un_pdf(pdf_path: Path) -> tuple[Path, list[dict]]:
    """Extrae y trocea un PDF (CPU/IO-bound, seguro de correr en threads
    separados -- pypdf no comparte estado mutable entre llamadas)."""
    logger.info("Procesando %s ...", pdf_path.name)
    chunks = index_pdf(pdf_path, max_chars=BIBLIOGRAFIA_MAX_CHARS_POR_CHUNK)
    logger.info("Completado %s: %d chunks", pdf_path.name, len(chunks))
    return pdf_path, chunks


def main() -> None:
    if not BIBLIOGRAFIA_DIR.is_dir():
        logger.error("No existe la carpeta %s", BIBLIOGRAFIA_DIR)
        return

    pdfs = sorted(BIBLIOGRAFIA_DIR.glob("*.pdf"))
    if not pdfs:
        logger.error("No hay PDFs en %s", BIBLIOGRAFIA_DIR)
        return

    logger.info(
        "Encontrados %d PDFs. Usando hasta %d workers en paralelo.",
        len(pdfs),
        MAX_WORKERS,
    )

    CHROMA_PATH.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    collection = _get_or_create_bibliografia_collection(client)

    total_chunks_guardados = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futuros = {executor.submit(_procesar_un_pdf, pdf): pdf for pdf in pdfs}

        for futuro in as_completed(futuros):
            pdf_path = futuros[futuro]
            try:
                _, chunks = futuro.result()
            except Exception:
                logger.exception("Fallo procesando %s, se omite", pdf_path.name)
                continue

            if not chunks:
                logger.warning(
                    "%s no produjo chunks (sin texto extraíble)", pdf_path.name
                )
                continue

            documents = [c["text"] for c in chunks]
            metadatas = [{"source": c["source"], "page": c["page"]} for c in chunks]
            ids = [
                f"{pdf_path.stem}__p{c['page']}__{idx}" for idx, c in enumerate(chunks)
            ]

            # upsert (no add): si el script se re-corre tras una interrupción
            # parcial, los PDFs ya guardados se sobrescriben sin duplicarse.
            collection.upsert(documents=documents, metadatas=metadatas, ids=ids)
            total_chunks_guardados += len(chunks)
            logger.info(
                "Guardado %s en ChromaDB (%d chunks). Total acumulado: %d.",
                pdf_path.name,
                len(chunks),
                total_chunks_guardados,
            )

    logger.info(
        "Terminado. Colección '%s' tiene %d documentos en total.",
        BIBLIOGRAFIA_COLLECTION_NAME,
        collection.count(),
    )


if __name__ == "__main__":
    main()
