"""
Script para ejecutar el PedagogicalReviewPipeline con auto-fix editorial
del LayoutEditorialAgent (@Editor) sobre todas las lecciones y recompilar los notebooks.
"""

import os
import glob
from src.multiagent_core.pedagogical_pipeline import PedagogicalReviewPipeline
from src.multiagent_core.orchestrator_agent import OrchestratorAgent

lecciones_dir = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\lecciones'
pipeline = PedagogicalReviewPipeline()

print("=== EJECUTANDO AUTOCORRECCIÓN EDITORIAL DE @EDITOR EN TODAS LAS UNIDADES ===")

for filepath in sorted(glob.glob(os.path.join(lecciones_dir, '*.md'))):
    unit_name = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        
    unit_key = f"UNIDAD {unit_name.split('_')[1]}" if "UNIDAD_" in unit_name else unit_name
    res = pipeline.review_and_auto_fix_lesson(text, unit_key, auto_fix=True)
    fixed_text = res['fixed_text']
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_text)
        
    score = res['synthesis']['coherence_score']
    print(f"[EDITADO Y CORREGIDO OK] {unit_name} | Coherencia Editorial: {score}/100.0")

print("\n=== RE-COMPILANDO NOTEBOOKS JUPYTER (notebooks/*.ipynb) ===")
orchestrator = OrchestratorAgent(lecciones_dir='lecciones', notebooks_dir='notebooks')
results = orchestrator.run_full_pipeline()

for r in results:
    nb = os.path.basename(r['notebook_path'])
    score = r['evaluation']['total_score']
    print(f"[RECOMPILADO OK] {nb} | Score Final: {score}/100.0")
