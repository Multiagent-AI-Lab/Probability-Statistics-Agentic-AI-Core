"""Utilidades compartidas para extraer DOI citados en el texto de una lección.

Fuente de verdad única del patrón DOI. Antes vivía duplicado —con dos regex
sutilmente distintos— en `stats_tutor_agent.py` y en
`council/librarian_agent.py`, de modo que el tutor y el bibliotecario podían
discrepar sobre si un mismo texto citaba o no una fuente.
"""

import re

# Extrae del TEXTO del link Markdown (`DOI: [10.xxxx/yyyy](url)`), no de la
# URL — algunos DOI reales contienen paréntesis en su propio identificador
# (p. ej. `10.1016/0039-6028(69)90148-4`), lo que rompería un regex que
# delimite por ')' en la URL.
#
# El sufijo excluye espacios: un DOI real con espacio en el sufijo (raro, pero
# existen en algunos DOI de libros) no matchearía y el texto se trataría como
# "sin DOI" (degrada a validación por palabra clave, sin lanzar error). No se
# ha visto ese caso en el curso.
#
# La cota `{1,300}` en lugar de `+` acota el trabajo del motor de regex sobre
# texto adversario (el contenido de una lección es editable por cualquiera con
# acceso de escritura al repo) y excede con holgura la longitud de cualquier
# DOI real.
DOI_PATTERN = re.compile(r"DOI:\s*\[(10\.\d{4,9}/[^\]\s?#]{1,300})\]", re.IGNORECASE)


def extraer_dois(texto: str) -> list[str]:
    """Extrae los DOI citados en el texto, deduplicados y en orden de aparición.

    Args:
        texto: Texto Markdown de una lección (o cualquier fragmento).

    Returns:
        Lista de DOI únicos, en el orden en que aparecen en el texto.
    """
    return list(dict.fromkeys(DOI_PATTERN.findall(texto)))
