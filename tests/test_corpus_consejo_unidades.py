"""
Tests de gate para el corpus de A3-U (medicion contra unidades completas,
docs/superpowers/specs/2026-09-16-a3-unidades-completas-design.md):
confirma que el manifiesto y los archivos del corpus estan sincronizados,
mismo patron que tests/test_corpus_consejo.py para A3.
"""

import json
from pathlib import Path

_CORPUS_DIR = Path(__file__).resolve().parent / "fixtures" / "corpus_consejo_unidades"
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
    campos_requeridos = {
        "archivo",
        "tiene_fallo",
        "tipo_fallo",
        "origen",
        "unidad_origen",
    }
    for caso in manifiesto:
        faltantes = campos_requeridos - caso.keys()
        assert not faltantes, f"caso {caso.get('archivo')} sin campos: {faltantes}"
        assert caso["origen"] in ("real", "sintetico")
        assert isinstance(caso["tiene_fallo"], bool)


def test_hay_exactamente_8_negativos_y_8_positivos():
    manifiesto = _cargar_manifiesto()
    negativos = [c for c in manifiesto if not c["tiene_fallo"]]
    positivos = [c for c in manifiesto if c["tiene_fallo"]]
    assert len(negativos) == 8, f"se esperaban 8 negativos, hay {len(negativos)}"
    assert len(positivos) == 8, f"se esperaban 8 positivos, hay {len(positivos)}"


def test_todos_los_positivos_son_boxed_desincronizado():
    manifiesto = _cargar_manifiesto()
    positivos = [c for c in manifiesto if c["tiene_fallo"]]
    tipos = {c["tipo_fallo"] for c in positivos}
    assert tipos == {"boxed_desincronizado"}, (
        f"A3-U solo debe inyectar boxed_desincronizado (unico tipo con "
        f"detector real confirmado); encontrado: {tipos}"
    )


def test_los_negativos_no_se_desincronizan_de_su_unidad_fuente():
    """Minor de la revision final de A3-U (2026-09-17): los 8 negativos son
    copias byte-a-byte de lecciones/UNIDAD_N.md en el momento en que se
    creo el corpus. Nada detectaba si esa unidad se editaba despues,
    dejando la cifra de A3-U describiendo silenciosamente una version
    fantasma del curso. Este gate compara cada negativo contra su
    unidad_origen actual en disco -- si difieren, hay que regenerar el
    corpus de A3-U (copiar la unidad de nuevo) y volver a correr el runner
    para obtener una cifra valida."""
    raiz_repo = Path(__file__).resolve().parents[1]
    manifiesto = _cargar_manifiesto()
    negativos = [c for c in manifiesto if not c["tiene_fallo"]]

    desincronizados = []
    for caso in negativos:
        fixture = _CORPUS_DIR / caso["archivo"]
        fuente = raiz_repo / "lecciones" / caso["unidad_origen"]
        if fixture.read_text(encoding="utf-8") != fuente.read_text(encoding="utf-8"):
            desincronizados.append(caso["archivo"])

    assert not desincronizados, (
        f"estos negativos de A3-U ya no coinciden con su unidad_origen en "
        f"lecciones/: {desincronizados} -- regenera el corpus de A3-U "
        "(copiar la unidad actualizada) y vuelve a correr "
        "scripts/medir_precision_consejo_unidades.py para obtener una "
        "cifra valida"
    )
