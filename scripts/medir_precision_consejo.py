"""
Runner de medicion de precision del Consejo contra el corpus etiquetado de
A3 (auditoria 2026-09-14, docs/superpowers/audits/2026-09-14-auditoria-post-n05-n06-n07.md).

Herramienta de evaluacion puntual, no parte del pipeline de produccion --
se ejecuta manualmente para producir el reporte, igual que
convert_to_notebooks_smart.py. No corre en CI ni en la suite de pytest
(salvo calcular_metricas, que si tiene test unitario en
tests/test_medir_precision_consejo.py).

Uso: python scripts/medir_precision_consejo.py
"""

import json
from pathlib import Path
from typing import Any

from src.multiagent_core.pipeline import CouncilPipeline

_RAIZ_REPO = Path(__file__).resolve().parent.parent
_CORPUS_DIR = _RAIZ_REPO / "tests" / "fixtures" / "corpus_consejo"
_MANIFIESTO = _CORPUS_DIR / "etiquetas.json"


def calcular_metricas(matriz_confusion: dict[str, int]) -> dict[str, float | None]:
    """Precision, recall y kappa de Cohen sobre una matriz de confusion
    binaria {vp, fp, fn, vn} (verdadero/falso positivo/negativo).

    Kappa de Cohen: acuerdo observado corregido por el acuerdo esperable
    solo por azar, dadas las frecuencias marginales de cada evaluador
    (aqui, la etiqueta humana y el veredicto del Consejo). Formula
    estandar: kappa = (po - pe) / (1 - pe).
    """
    vp, fp, fn, vn = (
        matriz_confusion["vp"],
        matriz_confusion["fp"],
        matriz_confusion["fn"],
        matriz_confusion["vn"],
    )
    total = vp + fp + fn + vn

    precision = vp / (vp + fp) if (vp + fp) > 0 else None
    recall = vp / (vp + fn) if (vp + fn) > 0 else None

    po = (vp + vn) / total
    # Marginal humano: cuantos casos etiqueto "tiene fallo" (vp+fn) y
    # "no tiene fallo" (fp+vn). Marginal Consejo: cuantos predijo
    # "tiene fallo" (vp+fp) y "no tiene fallo" (fn+vn).
    p_humano_si = (vp + fn) / total
    p_consejo_si = (vp + fp) / total
    p_humano_no = (fp + vn) / total
    p_consejo_no = (fn + vn) / total
    pe = (p_humano_si * p_consejo_si) + (p_humano_no * p_consejo_no)
    kappa = (po - pe) / (1 - pe) if pe != 1 else 0.0

    return {"precision": precision, "recall": recall, "kappa": kappa}


def evaluar_caso(archivo: Path, unit_name: str) -> dict[str, Any]:
    """Corre el Consejo completo sobre un caso del corpus.

    Devuelve el veredicto (`predicho_tiene_fallo`) y si `@Librarian` paso
    (para que el llamador pueda excluir casos que fallaron solo por
    Crossref inaccesible, no por defecto de contenido -- ver Global
    Constraints del plan)."""
    texto = archivo.read_text(encoding="utf-8")
    resultado = CouncilPipeline().process_content(texto, unit_name=unit_name)
    return {
        "predicho_tiene_fallo": not resultado["approved"],
        "librarian_paso": resultado["reports"]["librarian"]["passed"],
        "hallazgos": resultado["final_qa"]["hallazgos"],
    }


def acumular_casos(
    manifiesto: list[dict[str, Any]],
    corpus_dir: Path,
    campos_extra: list[str] | None = None,
) -> tuple[dict[str, int], list[dict[str, Any]], list[str]]:
    """Corre `evaluar_caso` sobre cada entrada del manifiesto y acumula la
    matriz de confusion + el detalle por caso.

    Compartida entre A3 (`main` de este modulo) y A3-U
    (`scripts/medir_precision_consejo_unidades.py`) -- antes cada runner
    tenia su propia copia de este bucle (Important de la revision final de
    A3-U, 2026-09-17): un fix futuro en la logica de exclusion por Crossref
    o en el conteo de la matriz solo se aplicaba al runner editado, no al
    otro. `campos_extra` deja que cada runner agregue columnas propias a
    `detalle` (A3 usa "origen", A3-U usa "unidad_origen") sin bifurcar el
    bucle en si.
    """
    matriz = {"vp": 0, "fp": 0, "fn": 0, "vn": 0}
    excluidos_por_red: list[str] = []
    detalle: list[dict[str, Any]] = []

    for caso in manifiesto:
        archivo = corpus_dir / caso["archivo"]
        evaluacion = evaluar_caso(archivo, unit_name=caso["archivo"])

        if not evaluacion["librarian_paso"] and "DOI" not in archivo.read_text(
            encoding="utf-8"
        ):
            # Librarian fallo sin que el caso cite DOI -> no es el problema
            # de red conocido, se cuenta igual.
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

        fila = {
            "archivo": caso["archivo"],
            "tipo_fallo": caso["tipo_fallo"],
            "tiene_fallo_real": real,
            "predicho_tiene_fallo": predicho,
            "acierto": real == predicho,
        }
        for campo in campos_extra or []:
            fila[campo] = caso[campo]
        detalle.append(fila)

    return matriz, detalle, excluidos_por_red


def main() -> None:
    manifiesto = json.loads(_MANIFIESTO.read_text(encoding="utf-8"))
    matriz, detalle, excluidos_por_red = acumular_casos(
        manifiesto, _CORPUS_DIR, campos_extra=["origen"]
    )
    metricas = calcular_metricas(matriz)
    _escribir_reporte(matriz, metricas, detalle, excluidos_por_red)


def _escribir_reporte(
    matriz: dict[str, int],
    metricas: dict[str, float | None],
    detalle: list[dict[str, Any]],
    excluidos_por_red: list[str],
) -> None:
    from datetime import UTC, datetime

    hoy = datetime.now(UTC).date().isoformat()
    ruta_reporte = (
        _RAIZ_REPO
        / "docs"
        / "superpowers"
        / "audits"
        / f"{hoy}-precision-consejo-corpus.md"
    )

    lineas = [
        "# Precision del Consejo contra corpus etiquetado (A3)",
        "",
        f"**Fecha de ejecucion:** {hoy}",
        f"**Casos evaluados:** {len(detalle)} (excluidos por red: {len(excluidos_por_red)})",
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
        "## Desglose por tipo de fallo y origen",
        "",
        "| Archivo | Origen | Tipo de fallo | Real | Predicho | Acierto |",
        "|---|---|---|---|---|---|",
    ]
    for fila in detalle:
        lineas.append(
            f"| {fila['archivo']} | {fila['origen']} | {fila['tipo_fallo']} | "
            f"{fila['tiene_fallo_real']} | {fila['predicho_tiene_fallo']} | {fila['acierto']} |"
        )

    if excluidos_por_red:
        lineas += [
            "",
            "## Casos excluidos por Crossref inaccesible",
            "",
            (
                "`@Librarian` consulta la API de Crossref por red; estos casos "
                "citan un DOI real y no se pudieron evaluar honestamente sin "
                "conectividad:"
            ),
            "",
        ] + [f"- {a}" for a in excluidos_por_red]

    ruta_reporte.write_text("\n".join(lineas), encoding="utf-8")
    print(f"Reporte escrito en {ruta_reporte}")


if __name__ == "__main__":
    main()
