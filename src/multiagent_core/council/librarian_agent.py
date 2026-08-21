"""
LibrarianAgent (@Librarian): Verification agent against statistical textbooks (Walpole, Montgomery) and literature.
"""

import logging
import re
from typing import Any

import requests

logger = logging.getLogger(__name__)

_DOI_PATTERN = re.compile(r"DOI:\s*\[(10\.\d{4,9}/[^\]\s?#]{1,300})\]", re.IGNORECASE)
_REFERENCE_KEYWORDS = ("walpole", "montgomery", "scipy", "mit", "meta-analysis")
CROSSREF_API_BASE = "https://api.crossref.org/works"
CROSSREF_TIMEOUT_SECONDS = 10


class LibrarianAgent:
    """Agent responsible for checking statistical reference literature and citation accuracy."""

    def _extract_dois(self, text: str) -> list[str]:
        """Extrae los DOI citados en el texto (formato `DOI: [10.xxxx/yyyy](url)`),
        deduplicados y en orden de aparición."""
        return list(dict.fromkeys(_DOI_PATTERN.findall(text)))

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
        una palabra clave de referencia conocida, o DOIs citados que
        resuelvan contra Crossref.

        Si el texto no cita ningún DOI, se aprueba con la sola presencia de
        una palabra clave (no se llama a Crossref sin necesidad). Si cita
        DOIs, cada uno debe resolver para que el reporte pase.
        """
        text_lower = text.lower()
        has_keyword = any(kw in text_lower for kw in _REFERENCE_KEYWORDS)
        dois = self._extract_dois(text)

        if not dois:
            return {
                "has_references": has_keyword,
                "passed": has_keyword,
                "dois_verificados": [],
                "dois_no_resueltos": [],
            }

        dois_verificados = [doi for doi in dois if self._doi_resuelve(doi)]
        dois_no_resueltos = [doi for doi in dois if doi not in dois_verificados]

        return {
            "has_references": True,
            "passed": len(dois_no_resueltos) == 0,
            "dois_verificados": dois_verificados,
            "dois_no_resueltos": dois_no_resueltos,
        }
