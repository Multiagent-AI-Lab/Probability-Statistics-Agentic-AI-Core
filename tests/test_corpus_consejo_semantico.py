"""Gate de sincronización del corpus adversarial semántico: el manifiesto
y el disco deben coincidir. No invoca ningún LLM ni al Consejo -- corre en
CI normal, determinista, sin API key (ver Task 6 del plan de
SemanticAuditorAgent)."""

import json
from pathlib import Path

_RAIZ = Path(__file__).resolve().parent
_CORPUS_DIR = _RAIZ / "fixtures" / "corpus_consejo_semantico"
_MANIFIESTO = _CORPUS_DIR / "etiquetas.json"


def _cargar_manifiesto() -> dict:
    return json.loads(_MANIFIESTO.read_text(encoding="utf-8"))


def test_cada_archivo_del_manifiesto_existe_en_disco():
    manifiesto = _cargar_manifiesto()
    faltantes = [nombre for nombre in manifiesto if not (_CORPUS_DIR / nombre).exists()]
    assert faltantes == [], f"en el manifiesto pero no en disco: {faltantes}"


def test_cada_md_en_disco_esta_en_el_manifiesto():
    manifiesto = _cargar_manifiesto()
    archivos_en_disco = {p.name for p in _CORPUS_DIR.glob("*.md")}
    huerfanos = archivos_en_disco - set(manifiesto.keys())
    assert huerfanos == set(), f"en disco pero no en el manifiesto: {huerfanos}"


def test_cada_caso_tiene_los_campos_requeridos():
    manifiesto = _cargar_manifiesto()
    campos_requeridos = {"tiene_fallo", "tipo_fallo", "origen", "unidad_origen"}
    for nombre, caso in manifiesto.items():
        faltantes = campos_requeridos - caso.keys()
        assert faltantes == set(), f"{nombre} le faltan campos: {faltantes}"


def test_tipo_fallo_es_consistente_con_tiene_fallo():
    manifiesto = _cargar_manifiesto()
    for nombre, caso in manifiesto.items():
        if caso["tiene_fallo"]:
            assert caso["tipo_fallo"] in (
                "inversion_semantica",
                "constante_falsa",
            ), f"{nombre} tiene_fallo=True pero tipo_fallo={caso['tipo_fallo']!r}"
        else:
            assert (
                caso["tipo_fallo"] is None
            ), f"{nombre} tiene_fallo=False pero tipo_fallo={caso['tipo_fallo']!r}"
