"""
Script para corregir el bug de des-escape de corchetes en f-strings de Python:
reemplaza display(Math(rf'\\text{...}')) por display(Math(r'\\text{...}'))
en todas las lecciones y notebooks.
"""

import os
import glob
import re

lecciones_dir = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\lecciones'

def fix_rf_text_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        
    # Reemplazar display(Math(rf'\text{ por display(Math(r'\text{
    text = text.replace("display(Math(rf'\\text{", "display(Math(r'\\text{")
    text = text.replace('display(Math(rf"\\text{', 'display(Math(r"\\text{')
    text = text.replace("display(Math(f'\\text{", "display(Math(r'\\text{")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

print("=== REPARANDO F-STRINGS LATEX EN CÓDIGO PYTHON EN TODAS LAS LECCIONES ===")
for md_file in sorted(glob.glob(os.path.join(lecciones_dir, '*.md'))):
    fname = os.path.basename(md_file)
    fix_rf_text_in_file(md_file)
    print(f"[F-STRINGS \\text{{}} REPARADOS OK] {fname}")
