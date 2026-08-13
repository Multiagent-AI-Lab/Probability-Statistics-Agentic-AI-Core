"""
Elimina definitivamente cualquier celda o bloque de código sintético residual que contenga
x = sp.Symbol('x') o Verificación Simbólica Autor de lecciones/*.md
"""

import os
import glob
import re

lecciones_dir = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\lecciones'

print("=== ELIMINANDO BLOQUES SINTÉTICOS RESIDUALES x = sp.Symbol('x') ===")
for md_file in sorted(glob.glob(os.path.join(lecciones_dir, '*.md'))):
    fname = os.path.basename(md_file)
    with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        
    # Eliminar bloques de código que contengan x = sp.Symbol('x') o Verificación Simbólica Autor
    pattern1 = r'```python\s*import sympy as sp\s*from IPython\.display import display, Math\s*x = sp\.Symbol\(\'x\'\).*?```'
    pattern2 = r'### Resumen del Protocolo Maestro.*?```python.*?sp\.Symbol\(\'x\'\).*?```'
    pattern3 = r'\* \*\*Verificación Simbólica \(SymPy\):\*\*\s*```python\s*import sympy as sp\s*from IPython\.display import display, Math\s*x = sp\.Symbol\(\'x\'\).*?```'
    
    text_clean = re.sub(pattern1, '', text, flags=re.DOTALL)
    text_clean = re.sub(pattern2, '', text_clean, flags=re.DOTALL)
    text_clean = re.sub(pattern3, '', text_clean, flags=re.DOTALL)
    text_clean = text_clean.replace("x = sp.Symbol('x')", "# Variable eliminada")
    
    # También limpiar si la frase 'Verificación Simbólica Autor' está sola
    lines = text_clean.split('\n')
    filtered_lines = [l for l in lines if 'Verificación Simbólica Autor' not in l and "x = sp.Symbol('x')" not in l]
    text_final = '\n'.join(filtered_lines)
    
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(text_final)
        
    print(f"[ELIMINADO BLOQUE SINTÉTICO OK] {fname}")
