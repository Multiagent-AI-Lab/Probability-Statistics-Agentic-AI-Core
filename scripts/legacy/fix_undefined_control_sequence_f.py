"""
Script para eliminar los artefactos \\f\\frac, \\r\\right, \\b\\bar que causan el error
'Undefined control sequence: \\f' en KaTeX en todos los notebooks.
"""

import os
import glob
import re

lecciones_dir = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\lecciones'

def clean_undefined_control_sequences(text):
    # 1. Eliminar \f antes de \frac o \ffrac
    text = text.replace('\\f\\frac', '\\frac')
    text = text.replace('\\ffrac', '\\frac')
    text = text.replace('\\f\\', '\\')
    
    # 2. Eliminar \r antes de \right o \left
    text = text.replace('\\r\\right', '\\right')
    text = text.replace('\\r\\left', '\\left')

    # 3. Eliminar \b antes de \bar
    text = text.replace('\\b\\bar', '\\bar')
    text = text.replace('\\t\\text', '\\text')
    
    # 4. Limpiar secuencias de barras triples o dobles antes de comandos LaTeX
    text = re.sub(r'\\{2,}frac', r'\\frac', text)
    text = re.sub(r'\\{2,}right', r'\\right', text)
    text = re.sub(r'\\{2,}left', r'\\left', text)
    text = re.sub(r'\\{2,}bar', r'\\bar', text)
    text = re.sub(r'\\{2,}text', r'\\text', text)

    return text

print("=== REPARANDO SECUENCIAS INDEFINIDAS \\f\\frac EN LAS 7 LECCIONES ===")
for md_file in sorted(glob.glob(os.path.join(lecciones_dir, '*.md'))):
    fname = os.path.basename(md_file)
    with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
        raw_text = f.read()
        
    fixed_text = clean_undefined_control_sequences(raw_text)
    
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(fixed_text)
        
    print(f"[SECUNCIAS \\f\\frac LIMPIAS OK] {fname}")
