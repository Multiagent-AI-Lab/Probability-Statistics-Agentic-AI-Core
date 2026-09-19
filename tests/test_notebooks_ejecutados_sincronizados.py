"""
Gate de deriva: `notebooks/ejecutados/*.ipynb` (copias con outputs reales,
publicadas para que el estudiante vea resultados sin clonar el repo, ver
README "Ver los notebooks sin clonar") debe tener el MISMO contenido
fuente -celdas de código y markdown, ignorando outputs- que su
`notebooks/*.ipynb` correspondiente (la salida limpia del build).

Sin este gate, un cambio en `lecciones/*.md` que se propaga a
`notebooks/*.ipynb` (vía `OrchestratorAgent.run_full_pipeline()`) puede
dejar `notebooks/ejecutados/` desactualizado en silencio -exactamente lo
que ocurrió con `UNIDAD_1_ESTADISTICA_DESCRIPTIVA.ipynb` durante la sesión
del 2026-09-18/19: se agregó una sección nueva al `.md`, se regeneró el
notebook limpio, pero `notebooks/ejecutados/` no se volvió a ejecutar y
quedó mostrando una versión anterior del contenido sin que nada lo
detectara- (auditoría comparativa externa, 2026-09-19).

No se compara bit a bit el `.ipynb` completo (los outputs son, por
diseño, diferentes entre ambos: uno los tiene, el otro no) ni metadata de
kernel -solo el campo `source` de cada celda, en el mismo orden.
"""

import json
from pathlib import Path

_RAIZ = Path(__file__).resolve().parents[1]
_NOTEBOOKS_DIR = _RAIZ / "notebooks"
_EJECUTADOS_DIR = _NOTEBOOKS_DIR / "ejecutados"


def _fuentes_de_celdas(path: Path) -> list[str]:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    return ["".join(celda.get("source", [])) for celda in notebook.get("cells", [])]


def _unidades_con_copia_ejecutada() -> list[Path]:
    return sorted(_NOTEBOOKS_DIR.glob("UNIDAD_*.ipynb"))


def test_todas_las_unidades_publicadas_tienen_copia_ejecutada():
    faltantes = [
        nb.name
        for nb in _unidades_con_copia_ejecutada()
        if not (_EJECUTADOS_DIR / nb.name).exists()
    ]
    assert not faltantes, (
        f"estas unidades no tienen copia ejecutada en notebooks/ejecutados/: "
        f"{faltantes} -- un estudiante que las abra en GitHub sin clonar el "
        "repo no vera ningun output. Generar con: jupyter nbconvert --to "
        "notebook --execute --ExecutePreprocessor.timeout=600 "
        "--output-dir=notebooks/ejecutados "
        + " ".join(f"notebooks/{n}" for n in faltantes)
    )


def test_notebooks_ejecutados_no_se_desincronizan_del_build_limpio():
    desincronizados = []
    for nb_limpio in _unidades_con_copia_ejecutada():
        nb_ejecutado = _EJECUTADOS_DIR / nb_limpio.name
        if not nb_ejecutado.exists():
            continue  # cubierto por el test anterior
        if _fuentes_de_celdas(nb_limpio) != _fuentes_de_celdas(nb_ejecutado):
            desincronizados.append(nb_limpio.name)

    assert not desincronizados, (
        f"estos notebooks en notebooks/ejecutados/ ya no coinciden en contenido "
        f"(celdas de codigo/markdown, sin contar outputs) con su version actual "
        f"en notebooks/: {desincronizados} -- regenerar con: jupyter nbconvert "
        "--to notebook --execute --ExecutePreprocessor.timeout=600 "
        "--output-dir=notebooks/ejecutados "
        + " ".join(f"notebooks/{n}" for n in desincronizados)
    )
