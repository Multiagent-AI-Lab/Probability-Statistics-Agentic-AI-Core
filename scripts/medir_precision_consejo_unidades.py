"""
Runner de medicion de A3-U: precision del Consejo contra el corpus de
UNIDADES COMPLETAS (docs/superpowers/specs/2026-09-16-a3-unidades-completas-design.md).

Complementario a scripts/medir_precision_consejo.py (A3, que mide contra
fragmentos recortados) -- este runner NO lo reemplaza, reutiliza sus
funciones de calculo de metricas y evaluacion de caso sin duplicarlas.

Herramienta de evaluacion puntual, no parte del pipeline de produccion --
se ejecuta manualmente para producir el reporte. No corre en CI ni en la
suite de pytest.

Uso: python scripts/medir_precision_consejo_unidades.py
"""

import json
from pathlib import Path
from typing import Any

from scripts.medir_precision_consejo import calcular_metricas, evaluar_caso

_RAIZ_REPO = Path(__file__).resolve().parent.parent
_CORPUS_DIR = _RAIZ_REPO / "tests" / "fixtures" / "corpus_consejo_unidades"
_MANIFIESTO = _CORPUS_DIR / "etiquetas.json"


def main() -> None:
    manifiesto = json.loads(_MANIFIESTO.read_text(encoding="utf-8"))

    matriz = {"vp": 0, "fp": 0, "fn": 0, "vn": 0}
    excluidos_por_red = []
    detalle: list[dict[str, Any]] = []

    for caso in manifiesto:
        archivo = _CORPUS_DIR / caso["archivo"]
        evaluacion = evaluar_caso(archivo, unit_name=caso["archivo"])

        if not evaluacion["librarian_paso"] and "DOI" not in archivo.read_text(
            encoding="utf-8"
        ):
            pass
        elif not evaluacion["librarian_paso"]:
            excluidos_por_red.append(caso["archivo"])
            continue

        real = caso["tiene_fallo"]
        predicho = evaluacion["predicho_tiene_fallo"]
        if real and predicho:
            matriz["vp"] += 1
        elif real and not predicho:
            matriz["fn"] += 1
        elif not real and predicho:
            matriz["fp"] += 1
        else:
            matriz["vn"] += 1

        detalle.append(
            {
                "archivo": caso["archivo"],
                "unidad_origen": caso["unidad_origen"],
                "tipo_fallo": caso["tipo_fallo"],
                "tiene_fallo_real": real,
                "predicho_tiene_fallo": predicho,
                "acierto": real == predicho,
            }
        )

    metricas = calcular_metricas(matriz)
    _escribir_reporte(matriz, metricas, detalle, excluidos_por_red)


def _escribir_reporte(
    matriz: dict[str, int],
    metricas: dict[str, float | None],
    detalle: list[dict[str, Any]],
    excluidos_por_red: list[str],
) -> None:
    from datetime import date

    ruta_reporte = (
        _RAIZ_REPO
        / "docs"
        / "superpowers"
        / "audits"
        / f"{date.today().isoformat()}-precision-consejo-unidades.md"
    )

    lineas = [
        "# Precision del Consejo contra unidades completas (A3-U)",
        "",
        f"**Fecha de ejecucion:** {date.today().isoformat()}",
        f"**Casos evaluados:** {len(detalle)} (excluidos por red: {len(excluidos_por_red)})",
        "",
        "Complementario a A3 (`docs/superpowers/audits/2026-09-16-precision-consejo-corpus.md`), "
        "que mide contra fragmentos recortados de las 8 unidades. A3-U mide "
        "especificamente deteccion de `boxed_desincronizado` (el unico tipo de fallo "
        "del catalogo de A3 con mecanismo real confirmado en "
        "`_contraste_boxed.py`) sobre unidades completas sin recortar. No es "
        "comparable 1:1 con la cifra global de A3 -- ver GOVERNANCE.md SS5.1/D6 "
        "para la comparacion completa.",
        "",
        "## Matriz de confusion",
        "",
        "| | Predicho: tiene fallo | Predicho: no tiene fallo |",
        "|---|---|---|",
        f"| **Real: tiene fallo** | VP={matriz['vp']} | FN={matriz['fn']} |",
        f"| **Real: no tiene fallo** | FP={matriz['fp']} | VN={matriz['vn']} |",
        "",
        "## Metricas",
        "",
        f"- Precision: {metricas['precision']}",
        f"- Recall: {metricas['recall']}",
        f"- Kappa de Cohen: {metricas['kappa']}",
        "",
        "## Desglose por unidad de origen",
        "",
        "| Archivo | Unidad origen | Tipo de fallo | Real | Predicho | Acierto |",
        "|---|---|---|---|---|---|",
    ]
    for fila in detalle:
        lineas.append(
            f"| {fila['archivo']} | {fila['unidad_origen']} | {fila['tipo_fallo']} | "
            f"{fila['tiene_fallo_real']} | {fila['predicho_tiene_fallo']} | {fila['acierto']} |"
        )

    if excluidos_por_red:
        lineas += [
            "",
            "## Casos excluidos por Crossref inaccesible",
            "",
            "`@Librarian` consulta la API de Crossref por red; estos casos "
            "citan un DOI real y no se pudieron evaluar honestamente sin "
            "conectividad:",
            "",
        ] + [f"- {a}" for a in excluidos_por_red]

    ruta_reporte.write_text("\n".join(lineas), encoding="utf-8")
    print(f"Reporte escrito en {ruta_reporte}")


if __name__ == "__main__":
    main()
