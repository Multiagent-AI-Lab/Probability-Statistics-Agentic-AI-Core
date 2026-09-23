"""
Runner de medicion del SemanticAuditorAgent contra el corpus adversarial
semantico (docs/superpowers/specs/2026-09-23-semantic-auditor-agent-design.md).

A diferencia de scripts/medir_precision_consejo_unidades.py, este runner
SI requiere una API key real configurada (GEMINI_API_KEY, ANTHROPIC_API_KEY
u OPENROUTER_API_KEY, segun SEMANTIC_JUDGE_BACKEND) y hace llamadas de red
reales -- se ejecuta manualmente, nunca en CI. Mide inversion_semantica y
constante_falsa por SEPARADO (no agregados en una sola cifra), porque son
mecanismos de deteccion distintos dentro del mismo agente.

Uso: GEMINI_API_KEY=... python scripts/medir_precision_consejo_semantico.py
Uso (OpenRouter): SEMANTIC_JUDGE_BACKEND=openrouter OPENROUTER_API_KEY=... \\
    python scripts/medir_precision_consejo_semantico.py
"""

import json
import os
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

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

        detectado_inversion = len(resultado["inversiones_semanticas"]) > 0
        detectado_constante = len(resultado["afirmaciones_no_verificables"]) > 0
        predicho_tiene_fallo = detectado_inversion or detectado_constante

        detalle.append(
            {
                "archivo": nombre_archivo,
                "unidad_origen": etiqueta["unidad_origen"],
                "tipo_fallo": etiqueta["tipo_fallo"],
                "real": etiqueta["tiene_fallo"],
                "predicho": predicho_tiene_fallo,
                "acierto": predicho_tiene_fallo == etiqueta["tiene_fallo"],
                "auditoria_incompleta": resultado["auditoria_incompleta"],
            }
        )

    _escribir_reporte(detalle)


def _escribir_reporte(detalle: list[dict[str, Any]]) -> None:
    vp = sum(1 for d in detalle if d["real"] and d["predicho"])
    fn = sum(1 for d in detalle if d["real"] and not d["predicho"])
    fp = sum(1 for d in detalle if not d["real"] and d["predicho"])
    vn = sum(1 for d in detalle if not d["real"] and not d["predicho"])

    precision = vp / (vp + fp) if (vp + fp) > 0 else None
    recall = vp / (vp + fn) if (vp + fn) > 0 else None

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
        f"{d['auditoria_incompleta']} |"
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
| **Real: tiene fallo** | VP={vp} | FN={fn} |
| **Real: no tiene fallo** | FP={fp} | VN={vn} |

## Metricas

- Precision: {precision}
- Recall: {recall}

## Desglose por caso

| Archivo | Unidad origen | Tipo de fallo | Real | Predicho | Acierto | Auditoria incompleta |
|---|---|---|---|---|---|---|
{filas}
"""
    ruta_reporte.write_text(contenido, encoding="utf-8")
    print(f"Reporte escrito en {ruta_reporte}")


if __name__ == "__main__":
    main()
