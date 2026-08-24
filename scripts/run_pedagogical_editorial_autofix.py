"""
Script para ejecutar el PedagogicalReviewPipeline con auto-fix editorial
del LayoutEditorialAgent (@Editor) sobre todas las lecciones y recompilar los notebooks.

Invocar desde cualquier directorio: `python scripts/run_pedagogical_editorial_autofix.py`
(las rutas se resuelven relativas a la raíz del repo, no al cwd).
"""

import glob
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.multiagent_core.orchestrator_agent import OrchestratorAgent
from src.multiagent_core.pedagogical_pipeline import PedagogicalReviewPipeline

lecciones_dir = str(REPO_ROOT / "lecciones")
notebooks_dir = str(REPO_ROOT / "notebooks")
backup_dir = os.path.join(lecciones_dir, ".backup")
os.makedirs(backup_dir, exist_ok=True)

pipeline = PedagogicalReviewPipeline()

print("=== EJECUTANDO AUTOCORRECCIÓN EDITORIAL DE @EDITOR EN TODAS LAS UNIDADES ===")

for filepath in sorted(glob.glob(os.path.join(lecciones_dir, "*.md"))):
    unit_name = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    unit_key = (
        f"UNIDAD {unit_name.split('_')[1]}" if "UNIDAD_" in unit_name else unit_name
    )
    res = pipeline.review_and_auto_fix_lesson(text, unit_key, auto_fix=True)
    fixed_text = res["fixed_text"]

    if fixed_text != text:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(backup_dir, f"{unit_name}.{timestamp}.md")
        shutil.copy2(filepath, backup_path)
        print(f"[BACKUP] {unit_name} -> {os.path.basename(backup_path)}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(fixed_text)

    score = res["synthesis"]["coherence_score"]
    critical = res.get("critical_block", False)
    status = "BLOQUEO CRITICO" if critical else "OK"
    print(
        f"[EDITADO Y CORREGIDO {status}] {unit_name} | Coherencia Editorial: {score}/100.0"
    )

print("\n=== RE-COMPILANDO NOTEBOOKS JUPYTER (notebooks/*.ipynb) ===")
orchestrator = OrchestratorAgent(
    lecciones_dir=lecciones_dir, notebooks_dir=notebooks_dir
)
results = orchestrator.run_full_pipeline(enforce_gate=True)

for r in results:
    if r["gate_blocked"]:
        print(f"[GATE BLOQUEADO] {r['md_filename']} | Motivo: {r['gate_reason']}")
        continue
    nb = os.path.basename(r["notebook_path"])
    score = r["evaluation"]["total_score"]
    print(f"[RECOMPILADO OK] {nb} | Score Final: {score}/100.0")
