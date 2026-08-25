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
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# El tokenizer de HuggingFace (Rust) puede lanzar un TypeError espurio y no
# determinista al tokenizar en paralelo con varios PDFs procesándose a la
# vez (confirmado: la misma llamada exacta a veces falla y a veces no).
# Deshabilitar su paralelismo interno evita la condición de carrera --
# debe fijarse antes de importar transformers/tokenizers.
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

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


MAX_INTENTOS_UPSERT = 3
# Firma exacta del TypeError confirmado como fallo transitorio del tokenizer
# (ver docstring de _upsert_con_reintento). Verificarla evita que un
# TypeError de otro origen (ej. un bug real en documents/metadatas/ids)
# quede enmascarado como "fallo transitorio" y se reintente/omita en vez de
# propagarse de inmediato.
_FIRMA_ERROR_TOKENIZER = "TextEncodeInput must be"


def _upsert_con_reintento(
    collection: chromadb.Collection,
    documents: list[str],
    metadatas: list[dict],
    ids: list[str],
    pdf_name: str,
) -> None:
    """El tokenizer de HuggingFace ocasionalmente lanza un TypeError espurio
    y no determinista al embeber un batch (confirmado: la misma llamada
    exacta sobre los mismos datos a veces falla y a veces no, sin que se
    haya podido aislar un chunk o condición específica -- parece una
    condición de carrera interna de la librería). Un reintento simple casi
    siempre basta porque el fallo no es reproducible de forma consistente."""
    for intento in range(1, MAX_INTENTOS_UPSERT + 1):
        try:
            collection.upsert(documents=documents, metadatas=metadatas, ids=ids)
            return
        except TypeError as e:
            if _FIRMA_ERROR_TOKENIZER not in str(e):
                raise
            if intento == MAX_INTENTOS_UPSERT:
                raise
            logger.warning(
                "%s: fallo transitorio del tokenizer (intento %d/%d), "
                "reintentando...",
                pdf_name,
                intento,
                MAX_INTENTOS_UPSERT,
            )
            time.sleep(1)


def main(
    bibliografia_dir: Path = BIBLIOGRAFIA_DIR, chroma_path: Path = CHROMA_PATH
) -> list[str]:
    """Indexa todos los PDFs de `bibliografia_dir` en una colección ChromaDB
    persistida en `chroma_path`. Los defaults apuntan a la bibliografía y el
    índice del propio repo; se parametrizan para que
    scripts/empaquetar_distribucion_bibliografia.py pueda reusar esta misma
    lógica apuntando a un destino de empaquetado distinto (ej. dist/).

    Returns:
        Lista de nombres de PDFs que no se pudieron indexar (vacía si todos
        se guardaron correctamente). El llamador decide qué hacer con un
        índice parcial -- ej. empaquetar_distribucion_bibliografia.py aborta
        el empaquetado si esta lista no está vacía, para no distribuir un
        zip con bibliografía incompleta sin que sea evidente.
    """
    if not bibliografia_dir.is_dir():
        logger.error("No existe la carpeta %s", bibliografia_dir)
        return []

    pdfs = sorted(bibliografia_dir.glob("*.pdf"))
    if not pdfs:
        logger.error("No hay PDFs en %s", bibliografia_dir)
        return []

    logger.info(
        "Encontrados %d PDFs. Usando hasta %d workers en paralelo.",
        len(pdfs),
        MAX_WORKERS,
    )

    chroma_path.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(chroma_path))
    collection = _get_or_create_bibliografia_collection(client)

    total_chunks_guardados = 0
    pdfs_fallidos: list[str] = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futuros = {executor.submit(_procesar_un_pdf, pdf): pdf for pdf in pdfs}

        for futuro in as_completed(futuros):
            pdf_path = futuros[futuro]
            try:
                _, chunks = futuro.result()
            except Exception:
                logger.exception("Fallo procesando %s, se omite", pdf_path.name)
                pdfs_fallidos.append(pdf_path.name)
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
            try:
                _upsert_con_reintento(
                    collection, documents, metadatas, ids, pdf_path.name
                )
            except TypeError:
                logger.exception(
                    "Fallo guardando %s tras %d intentos, se omite",
                    pdf_path.name,
                    MAX_INTENTOS_UPSERT,
                )
                pdfs_fallidos.append(pdf_path.name)
                continue
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
    if pdfs_fallidos:
        logger.warning(
            "PDFs pendientes de reintentar (%d): %s. Vuelve a correr el "
            "script para completarlos (upsert no duplica los ya guardados).",
            len(pdfs_fallidos),
            ", ".join(pdfs_fallidos),
        )

    return pdfs_fallidos


if __name__ == "__main__":
    main()
