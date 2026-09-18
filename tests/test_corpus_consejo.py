"""
Tests de gate para el corpus etiquetado de A3 (auditoría 2026-09-14):
confirma que el manifiesto y los archivos del corpus están sincronizados,
para no repetir el patrón de desincronización silenciosa que ya afectó al
badge de tests tres veces en esta sesión extendida.
"""

import json
from pathlib import Path

_CORPUS_DIR = Path(__file__).resolve().parent / "fixtures" / "corpus_consejo"
_MANIFIESTO = _CORPUS_DIR / "etiquetas.json"


def _cargar_manifiesto() -> list[dict]:
    return json.loads(_MANIFIESTO.read_text(encoding="utf-8"))


def test_todos_los_archivos_del_manifiesto_existen():
    manifiesto = _cargar_manifiesto()
    faltantes = [
        caso["archivo"]
        for caso in manifiesto
        if not (_CORPUS_DIR / caso["archivo"]).exists()
    ]
    assert (
        not faltantes
    ), f"archivos listados en el manifiesto pero ausentes: {faltantes}"


def test_todos_los_archivos_md_estan_en_el_manifiesto():
    manifiesto = _cargar_manifiesto()
    archivos_listados = {caso["archivo"] for caso in manifiesto}
    archivos_en_disco = {p.name for p in _CORPUS_DIR.glob("*.md")}
    huerfanos = archivos_en_disco - archivos_listados
    assert (
        not huerfanos
    ), f".md en el directorio pero ausentes del manifiesto: {huerfanos}"


def test_cada_caso_tiene_los_campos_requeridos():
    manifiesto = _cargar_manifiesto()
    campos_requeridos = {"archivo", "tiene_fallo", "tipo_fallo", "origen"}
    for caso in manifiesto:
        faltantes = campos_requeridos - caso.keys()
        assert not faltantes, f"caso {caso.get('archivo')} sin campos: {faltantes}"
        assert caso["origen"] in ("real", "adversarial_previo", "sintetico")
        assert isinstance(caso["tiene_fallo"], bool)
