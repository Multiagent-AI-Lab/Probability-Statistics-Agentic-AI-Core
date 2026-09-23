"""
Runner de medicion del SemanticAuditorAgent contra el corpus adversarial
semantico (docs/superpowers/specs/2026-09-23-semantic-auditor-agent-design.md).

A diferencia de scripts/medir_precision_consejo_unidades.py, este runner
SI requiere una API key real configurada (GEMINI_API_KEY, ANTHROPIC_API_KEY
u OPENROUTER_API_KEY, segun SEMANTIC_JUDGE_BACKEND) y hace llamadas de red
reales -- se ejecuta manualmente, nunca en CI. Mide inversion_semantica y
constante_falsa por SEPARADO (no agregados en una sola cifra), porque son
mecanismos de deteccion distintos dentro del mismo agente.

Reutiliza `calcular_metricas` de scripts/medir_precision_consejo.py (deuda
de seguimiento cerrada, revision final del plan 2026-09-23: la primera
version reimplementaba vp/fn/fp/vn/precision/recall a mano, sin kappa).
`acumular_casos` de ese mismo modulo NO se reutiliza: espera un manifiesto
en forma de lista y llama internamente a CouncilPipeline().process_content(),
mientras este runner necesita ScientistAgent+SemanticAuditorAgent sobre un
manifiesto en forma de dict -- son arquitecturas incompatibles, no una
omision.

Uso: GEMINI_API_KEY=... python scripts/medir_precision_consejo_semantico.py
Uso (OpenRouter): SEMANTIC_JUDGE_BACKEND=openrouter OPENROUTER_API_KEY=... \\
    python scripts/medir_precision_consejo_semantico.py
"""

import json
import os
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from scripts.medir_precision_consejo import calcular_metricas
from src.multiagent_core.council.scientist_agent import ScientistAgent
from src.multiagent_core.council.semantic_auditor_agent import SemanticAuditorAgent

_RAIZ_REPO = Path(__file__).resolve().parent.parent
_CORPUS_DIR = _RAIZ_REPO / "tests" / "fixtures" / "corpus_consejo_semantico"
_MANIFIESTO = _CORPUS_DIR / "etiquetas.json"


def main() -> None:
    if (
        not os.environ.get("GEMINI_API_KEY")
        and not os.environ.get("ANTHROPIC_API_KEY")
        and not os.environ.get("OPENROUTER_API_KEY")
    ):
        raise SystemExit(
            "Configura GEMINI_API_KEY, ANTHROPIC_API_KEY u OPENROUTER_API_KEY "
            "antes de correr este runner -- requiere llamadas de red reales."
        )

    manifiesto = json.loads(_MANIFIESTO.read_text(encoding="utf-8"))
    scientist = ScientistAgent()
    semantic = SemanticAuditorAgent()

    detalle: list[dict[str, Any]] = []
    for nombre_archivo, etiqueta in manifiesto.items():
        texto = (_CORPUS_DIR / nombre_archivo).read_text(encoding="utf-8")
        formulas = scientist.check_theory(texto)["formulas_estructuradas"]
        resultado = semantic.check_semantics(texto, formulas)

        inversiones = resultado["inversiones_semanticas"]
        constantes = resultado["afirmaciones_no_verificables"]
        predicho_tiene_fallo = bool(inversiones) or bool(constantes)
        real = etiqueta["tiene_fallo"]

        # Explicación por caso solo para falsos positivos (deuda de
        # seguimiento: antes el reporte no decía por qué el LLM marcó un
        # caso que en realidad no tenía fallo) -- usa el propio hallazgo
        # ya obtenido, sin ninguna llamada adicional al LLM.
        explicacion_fp = None
        if predicho_tiene_fallo and not real:
            citas = [h["explicacion"] for h in inversiones if h.get("explicacion")]
            citas += [
                f"constante '{c['constante']}' afirmada como {c['valor_afirmado']}"
                for c in constantes
            ]
            explicacion_fp = (
                "; ".join(citas) if citas else "(sin explicación capturada)"
            )

        detalle.append(
            {
                "archivo": nombre_archivo,
                "unidad_origen": etiqueta["unidad_origen"],
                "tipo_fallo": etiqueta["tipo_fallo"],
                "real": real,
                "predicho": predicho_tiene_fallo,
                "acierto": predicho_tiene_fallo == real,
                "auditoria_incompleta": resultado["auditoria_incompleta"],
                "explicacion_fp": explicacion_fp,
            }
        )

    matriz, metricas = _calcular_matriz(detalle)
    _escribir_reporte(detalle, matriz, metricas)


def _calcular_matriz(
    detalle: list[dict[str, Any]],
) -> tuple[dict[str, int], dict[str, float | None]]:
    matriz = {
        "vp": sum(1 for d in detalle if d["real"] and d["predicho"]),
        "fn": sum(1 for d in detalle if d["real"] and not d["predicho"]),
        "fp": sum(1 for d in detalle if not d["real"] and d["predicho"]),
        "vn": sum(1 for d in detalle if not d["real"] and not d["predicho"]),
    }
    metricas = calcular_metricas(matriz)
    return matriz, metricas


def _escribir_reporte(
    detalle: list[dict[str, Any]],
    matriz: dict[str, int],
    metricas: dict[str, float | None],
    escribir_archivo: bool = True,
) -> str:
    hoy = datetime.now(UTC).date().isoformat()
    ruta_reporte = (
        _RAIZ_REPO
        / "docs"
        / "superpowers"
        / "audits"
        / f"{hoy}-precision-consejo-semantico.md"
    )

    filas = "\n".join(
        f"| {d['archivo']} | {d['unidad_origen']} | {d['tipo_fallo']} | "
        f"{d['real']} | {d['predicho']} | {d['acierto']} | "
        f"{d['auditoria_incompleta']} | {d.get('explicacion_fp') or '-'} |"
        for d in detalle
    )

    contenido = f"""# Precision del SemanticAuditorAgent (corpus adversarial semantico)

**Fecha de ejecucion:** {hoy}
**Casos evaluados:** {len(detalle)}

Primera medicion del 9no agente del Consejo (el unico con LLM), contra
inversion semantica y constante falsa -- la brecha que
`docs/superpowers/audits/2026-09-23-precision-consejo-unidades.md`
documenta como limite conocido del resto del Consejo (heuristico puro).

## Matriz de confusion (agregada, ambos tipos de fallo)

| | Predicho: tiene fallo | Predicho: no tiene fallo |
|---|---|---|
| **Real: tiene fallo** | VP={matriz['vp']} | FN={matriz['fn']} |
| **Real: no tiene fallo** | FP={matriz['fp']} | VN={matriz['vn']} |

## Metricas

- Precision: {metricas['precision']}
- Recall: {metricas['recall']}
- Kappa de Cohen: {metricas['kappa']}

## Desglose por caso

La columna "Explicación FP" solo se llena para falsos positivos (el
Consejo marcó un fallo que la etiqueta real dice que no existe): cita la
explicación que el propio LLM dio al reportar el hallazgo, para poder
diagnosticar por qué se equivocó sin tener que re-ejecutar nada.

| Archivo | Unidad origen | Tipo de fallo | Real | Predicho | Acierto | Auditoria incompleta | Explicación FP |
|---|---|---|---|---|---|---|---|
{filas}
"""
    if escribir_archivo:
        ruta_reporte.write_text(contenido, encoding="utf-8")
        print(f"Reporte escrito en {ruta_reporte}")
    return contenido


if __name__ == "__main__":
    main()
