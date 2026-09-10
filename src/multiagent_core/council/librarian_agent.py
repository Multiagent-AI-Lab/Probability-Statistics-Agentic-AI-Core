"""
LibrarianAgent (@Librarian): Verification agent against statistical textbooks (Walpole, Montgomery) and literature.
"""

import logging
from typing import Any

import requests

from .._doi_utils import extraer_dois

logger = logging.getLogger(__name__)

_REFERENCE_KEYWORDS = ("walpole", "montgomery", "scipy", "mit", "meta-analysis")
CROSSREF_API_BASE = "https://api.crossref.org/works"
CROSSREF_TIMEOUT_SECONDS = 10


class LibrarianAgent:
    """Agent responsible for checking statistical reference literature and citation accuracy."""

    def _extract_dois(self, text: str) -> list[str]:
        """Extrae los DOI citados en el texto (formato `DOI: [10.xxxx/yyyy](url)`),
        deduplicados y en orden de aparición.

        Delega en `_doi_utils.extraer_dois`, la fuente de verdad compartida con
        `StatsTutorAgent` (ver ese módulo para el detalle del patrón)."""
        return extraer_dois(text)

    def _doi_resuelve(self, doi: str) -> bool:
        """Confirma que un DOI existe consultando la API pública de Crossref.

        `allow_redirects=False`: el DOI viene de texto de lección (editable
        por cualquiera con acceso de escritura al repo), no de un endpoint
        controlado -- seguir redirects automáticamente podría llevar la
        petición a un host distinto de Crossref. Un DOI válido que Crossref
        redirija se reportaría como no resuelto; se acepta ese trade-off.
        """
        try:
            response = requests.get(
                f"{CROSSREF_API_BASE}/{doi}",
                timeout=CROSSREF_TIMEOUT_SECONDS,
                allow_redirects=False,
            )
            response.raise_for_status()
            return True
        except requests.RequestException as e:
            logger.warning("DOI %s no resolvió en Crossref: %s", doi, e)
            return False

    def verify_references(self, text: str) -> dict[str, Any]:
        """Verifica que el texto tenga soporte bibliográfico real: al menos
        un DOI citado que resuelva contra Crossref.

        H-01: antes bastaba con que apareciera la subcadena "walpole" (o
        "scipy", o "mit") para aprobar la auditoría bibliográfica, de modo
        que un documento de basura sintética con la palabra "Walpole"
        pegada al final pasaba este control. Un apellido en el texto no es
        una cita verificable; un DOI que resuelve, sí.

        Las palabras clave conocidas se siguen reportando como metadato
        (`has_keyword`) porque son señal útil en el reporte, pero ya no
        deciden el veredicto. Cada unidad del curso cita al menos un DOI,
        así que el criterio no penaliza contenido real.
        """
        text_lower = text.lower()
        has_keyword = any(kw in text_lower for kw in _REFERENCE_KEYWORDS)
        dois = self._extract_dois(text)

        if not dois:
            return {
                "has_references": False,
                "has_keyword": has_keyword,
                "passed": False,
                "dois_verificados": [],
                "dois_no_resueltos": [],
            }

        dois_verificados = [doi for doi in dois if self._doi_resuelve(doi)]
        dois_no_resueltos = [doi for doi in dois if doi not in dois_verificados]

        return {
            "has_references": True,
            "has_keyword": has_keyword,
            "passed": len(dois_no_resueltos) == 0 and bool(dois_verificados),
            "dois_verificados": dois_verificados,
            "dois_no_resueltos": dois_no_resueltos,
        }
