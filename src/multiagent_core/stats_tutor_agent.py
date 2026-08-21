"""
StatsTutorAgent - Probabilidad y Estadística Inferencial 🎲
=============================================================

Agente Tutor que responde dudas del curso usando un sistema RAG local
(Retrieval-Augmented Generation) con embeddings de ChromaDB sobre las
lecciones de lecciones/*.md, más Gemini para la respuesta final. Incluye
debugger socrático para errores estadísticos comunes (misconceptions),
no solo excepciones de Python.
"""

import json
import logging
import os
import re
from pathlib import Path

import chromadb
import requests
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from dotenv import load_dotenv
from google import genai

load_dotenv()

logger = logging.getLogger(__name__)

SKILL_METADATA = {
    "name": "stats_tutor_agent",
    "description": "Responde dudas del curso vía RAG semántico (ChromaDB) + Gemini, con debugger socrático de misconceptions estadísticos y memoria episódica.",
    "version": "1.0.0",
    "input": "question: str (ask) | course_dir: Path, chroma_path: Optional[Path], memory_path: Optional[Path] (constructor)",
    "output": "str (respuesta en Markdown, o pregunta socrática si detecta un misconception)",
    "requires_api_key": True,
}

DEFAULT_CHROMA_DIRNAME = ".chroma"
TOP_K_RESULTS = 3
DEFAULT_MEMORY_FILENAME = ".tutor_memory.json"
MAX_EPISODIOS = 50
PREFIJO_LONGITUD = 5
EMBEDDING_MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"
_DOI_PATTERN = re.compile(r"DOI:\s*\[(10\.\d{4,9}/[^\]\s?#]+)\]", re.IGNORECASE)
CROSSREF_API_BASE = "https://api.crossref.org/works"
CROSSREF_TIMEOUT_SECONDS = 10

_SOCRATIC_RULES: dict[str, str] = {
    "p-valor": (
        "Antes de darte la respuesta: un p-valor NO es la probabilidad de que "
        "H0 sea verdadera (o falsa). Es la probabilidad de observar un "
        "resultado igual o más extremo que el tuyo, ASUMIENDO que H0 es "
        "verdadera. ¿Qué significa entonces tu p-valor de 0.03 en esos términos?"
    ),
    "probabilidad de que h0": (
        "Antes de darte la respuesta: un p-valor NO es la probabilidad de que "
        "H0 sea verdadera. Es P(observar esto o algo más extremo | H0 verdadera). "
        "¿Ves la diferencia entre esas dos afirmaciones?"
    ),
    "varianza muestral": (
        "Antes de darte la respuesta: ¿estás usando el denominador n o n-1 "
        "para tu varianza? Revisa si necesitas un estimador insesgado de la "
        "varianza poblacional (corrección de Bessel) o la varianza descriptiva "
        "de la muestra tal cual."
    ),
    "correlación": (
        "Antes de darte la respuesta: correlación no implica causalidad. "
        "¿Podrías pensar en una tercera variable que explique la relación "
        "que observaste, sin que una cause a la otra?"
    ),
}

_SOCRATIC_FALLBACK = (
    "Antes de darte la respuesta directa: revisa tus supuestos. ¿Verificaste "
    "normalidad, homocedasticidad, o independencia antes de aplicar esta "
    "prueba estadística?"
)


class StatsTutorAgent:
    """Agente Tutor RAG que responde dudas del curso de Probabilidad y
    Estadística usando embeddings de ChromaDB sobre la documentación local."""

    def __init__(
        self,
        course_dir: Path,
        chroma_path: Path | None = None,
        memory_path: Path | None = None,
    ) -> None:
        self.course_dir = Path(course_dir)
        self.model_name = "gemini-2.5-flash"
        self.chroma_path = (
            Path(chroma_path)
            if chroma_path
            else self.course_dir / DEFAULT_CHROMA_DIRNAME
        )
        self.memory_path = (
            Path(memory_path)
            if memory_path
            else self.course_dir / DEFAULT_MEMORY_FILENAME
        )
        self.chroma_path.mkdir(parents=True, exist_ok=True)
        self.chroma_client = chromadb.PersistentClient(path=str(self.chroma_path))
        self.collection = self._get_or_create_collection()
        self._build_index()

    def _get_or_create_collection(self) -> chromadb.Collection:
        embedding_function = SentenceTransformerEmbeddingFunction(
            model_name=EMBEDDING_MODEL_NAME
        )
        try:
            return self.chroma_client.get_or_create_collection(
                "lecciones_probabilidad", embedding_function=embedding_function
            )
        except ValueError as e:
            if "Embedding function conflict" not in str(e):
                raise
            logger.warning(
                "Colección 'lecciones_probabilidad' indexada con un embedding "
                "distinto; reconstruyendo con %s.",
                EMBEDDING_MODEL_NAME,
            )
            self.chroma_client.delete_collection("lecciones_probabilidad")
            return self.chroma_client.get_or_create_collection(
                "lecciones_probabilidad", embedding_function=embedding_function
            )

    def _get_markdown_files(self) -> list[Path]:
        return list(self.course_dir.glob("UNIDAD_*.md"))

    def _split_into_sections(self, content: str) -> list[str]:
        return [s.strip() for s in re.split(r"\n(?=##?\s)", content) if s.strip()]

    def _extract_dois(self, content: str) -> list[str]:
        """Extrae los identificadores DOI citados en el texto de una lección.

        Extrae del texto del link Markdown (`[10.xxxx/yyyy]`), no de la URL —
        algunos DOI reales contienen paréntesis en su propio identificador,
        lo que rompería un regex que delimite por ')' en la URL.

        Args:
            content: Texto completo de un archivo Markdown de lección.

        Returns:
            Lista de DOI únicos, en el orden en que aparecen en el texto.
        """
        return list(dict.fromkeys(_DOI_PATTERN.findall(content)))

    def _fetch_abstract(self, doi: str) -> str | None:
        """Consulta el abstract público de un DOI vía la API de Crossref.

        La API de Crossref es gratuita, no requiere API key, y expone el
        abstract de un registro incluso cuando el texto completo del paper
        está detrás de un paywall.

        Args:
            doi: Identificador DOI a consultar.

        Returns:
            Texto plano del abstract (markup JATS removido), o None si la
            consulta falla o el registro no tiene abstract.
        """
        try:
            response = requests.get(
                f"{CROSSREF_API_BASE}/{doi}",
                timeout=CROSSREF_TIMEOUT_SECONDS,
                allow_redirects=False,
            )
            response.raise_for_status()
            abstract_jats = response.json()["message"].get("abstract")
            if not abstract_jats:
                logger.info("DOI %s no tiene abstract disponible en Crossref.", doi)
                return None
            return re.sub(r"<[^>]+>", "", abstract_jats).strip()
        except (requests.RequestException, KeyError, ValueError, AttributeError) as e:
            logger.warning("No se pudo obtener el abstract de DOI %s: %s", doi, e)
            return None

    def _build_index(self) -> None:
        """Indexa los MDs del curso y los abstracts de sus DOI citados en
        ChromaDB, si aún no lo están.

        Cada DOI citado (en cualquier archivo) se consulta una sola vez vía
        Crossref y se indexa como un documento adicional — si el mismo DOI
        aparece en varios archivos, se indexa un solo documento con todas
        las fuentes listadas en su metadata.
        """
        if self.collection.count() > 0:
            return

        documents: list[str] = []
        metadatas: list[dict] = []
        ids: list[str] = []
        doi_a_archivos: dict[str, list[str]] = {}

        for filepath in self._get_markdown_files():
            try:
                content = filepath.read_text(encoding="utf-8")
            except OSError as e:
                logger.error("Error leyendo %s: %s", filepath.name, e)
                continue

            for idx, section in enumerate(self._split_into_sections(content)):
                title_match = re.match(r"##?\s+(.+)", section)
                title = title_match.group(1).strip() if title_match else filepath.stem
                documents.append(section)
                metadatas.append({"source": filepath.name, "section": title})
                ids.append(f"{filepath.stem}__{idx}")

            for doi in self._extract_dois(content):
                doi_a_archivos.setdefault(doi, []).append(filepath.name)

        for doi, archivos in doi_a_archivos.items():
            abstract = self._fetch_abstract(doi)
            if abstract is None:
                continue
            documents.append(abstract)
            metadatas.append(
                {
                    "source": ", ".join(archivos),
                    "section": f"Referencia DOI: {doi}",
                }
            )
            ids.append(f"doi_{doi.replace('/', '_')}")

        if documents:
            self.collection.add(documents=documents, metadatas=metadatas, ids=ids)

    def _search_local_docs(self, query: str) -> str:
        if self.collection.count() == 0:
            return "No se encontraron documentos locales relevantes."

        resultados = self.collection.query(query_texts=[query], n_results=TOP_K_RESULTS)
        documentos = resultados.get("documents", [[]])[0]
        metadatas = resultados.get("metadatas", [[]])[0]

        if not documentos:
            return "No se encontraron documentos locales relevantes."

        context_parts = []
        for doc, meta in zip(documentos, metadatas):
            fuente = meta.get("source", "desconocido")
            seccion = meta.get("section", "")
            context_parts.append(
                f"--- Fuente: {fuente} | Sección: {seccion} ---\n{doc}\n"
            )

        return "\n".join(context_parts)

    def _load_episodes(self) -> list[dict]:
        if not self.memory_path.exists():
            return []
        try:
            return json.loads(self.memory_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return []

    def _add_episode(self, question: str, answer_summary: str) -> None:
        episodios = self._load_episodes()
        episodios.append({"question": question, "answer_summary": answer_summary})
        episodios = episodios[-MAX_EPISODIOS:]
        self.memory_path.write_text(
            json.dumps(episodios, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    def _prefijos(self, texto: str) -> set[str]:
        palabras = re.findall(r"\w+", texto.lower())
        return {p[:PREFIJO_LONGITUD] for p in palabras}

    def _retrieve_relevant_episodes(
        self, query: str, top_k: int = TOP_K_RESULTS
    ) -> list[dict]:
        episodios = self._load_episodes()
        query_words = self._prefijos(query)

        puntuados = []
        for ep in episodios:
            ep_words = self._prefijos(ep["question"])
            overlap = len(query_words & ep_words)
            score = overlap / max(len(query_words), 1)
            if score > 0:
                puntuados.append({**ep, "score": round(score, 3)})

        puntuados.sort(key=lambda e: e["score"], reverse=True)
        return puntuados[:top_k]

    def _diagnose_error(self, message: str) -> str | None:
        """Genera una pista socrática si el mensaje contiene un misconception
        estadístico conocido (p-valor mal interpretado, varianza muestral vs
        poblacional, correlación/causalidad) — a diferencia del TutorAgent de
        Lógica de Programación, aquí no se detectan excepciones de Python
        sino errores CONCEPTUALES de estadística en la pregunta del alumno."""
        if not message:
            return None

        message_lower = message.lower()
        for clave, pregunta in _SOCRATIC_RULES.items():
            if clave in message_lower:
                return pregunta

        # Solo dispara el fallback si el mensaje sugiere aplicar una prueba
        # sin mencionar verificación de supuestos — evita falsos positivos
        # en preguntas puramente conceptuales sin código de por medio.
        aplica_prueba_sin_supuestos = (
            (
                "t-test" in message_lower
                or "ttest" in message_lower
                or "prueba t" in message_lower
            )
            and "normal" not in message_lower
            and "supuesto" not in message_lower
        )
        if aplica_prueba_sin_supuestos:
            return _SOCRATIC_FALLBACK

        return None

    def ask(self, question: str) -> str:
        pista_socratica = self._diagnose_error(question)
        if pista_socratica:
            return pista_socratica

        context = self._search_local_docs(question)
        episodios_previos = self._retrieve_relevant_episodes(question)

        contexto_memoria = ""
        if episodios_previos:
            lineas = [
                f"  - Pregunta anterior: \"{ep['question']}\" (respuesta resumida: {ep['answer_summary'][:150]})"
                for ep in episodios_previos
            ]
            contexto_memoria = (
                "\n\nContexto de sesiones anteriores (memoria episódica):\n"
                + "\n".join(lineas)
            )

        prompt = f"""
Eres un Agente Tutor experto en Probabilidad y Estadística Inferencial para el curso de Ingeniería en Nanotecnología de la UCEMICH.
Tu misión es guiar al estudiante de forma clara, didáctica y técnica.

Usa el siguiente contexto recuperado de las lecciones del curso para responder la pregunta del alumno.
Si la información no está en el contexto, indícalo amablemente y responde con base en tus conocimientos generales del curso.

---
CONTEXTO DE LECCIONES:
{context}
{contexto_memoria}
---

PREGUNTA DEL ALUMNO:
{question}

Responde en español de forma estructurada, usando Markdown. Explica el razonamiento estadístico paso a paso.
"""
        try:
            client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
            response = client.models.generate_content(
                model=self.model_name, contents=prompt
            )
            respuesta_texto = response.text
        except Exception as e:
            logger.exception("Fallo al invocar al modelo Gemini")
            respuesta_texto = (
                f"Error al invocar al modelo Gemini: {e}\n\n"
                f"[Contexto Local Recuperado]:\n{context}"
            )

        self._add_episode(question, respuesta_texto[:300])
        return respuesta_texto
