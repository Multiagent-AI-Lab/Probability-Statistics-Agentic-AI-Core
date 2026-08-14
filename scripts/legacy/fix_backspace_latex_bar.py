"""
Script para reparar la corrupción de comandos LaTeX \\bar{} causados por secuencias de escape \\b (ASCII 0x08).
Reemplaza \\x08ar{, $ar{ y (ar{ por \\bar{} en todas las lecciones.
"""

import os
import glob
import re

lecciones_dir = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\lecciones'

def fix_bar_latex(text):
    # 1. Reemplazar carácter de retroceso (0x08) seguido de ar{
    text = text.replace('\x08ar{', '\\bar{')
    text = text.replace('\x08', '\\')
    
    # 2. Reemplazar $ar{...}$ por $\bar{...}$
    text = re.sub(r'\$ar\{([^}]+)\}\$', r'$\\bar{\1}$', text)
    text = re.sub(r'\$ar\{([^}]+)\}', r'$\\bar{\1}', text)
    text = re.sub(r'\(ar\{([^}]+)\}', r'(\\bar{\1}', text)
    text = re.sub(r'\s+ar\{([^}]+)\}', r' \\bar{\1}', text)
    
    return text

print("=== REPARANDO COMANDOS LATEX \\bar{} AFECTADOS POR BACKSPACE ESCAPE ===")
for md_file in sorted(glob.glob(os.path.join(lecciones_dir, '*.md'))):
    fname = os.path.basename(md_file)
    with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
        raw_text = f.read()
        
    fixed_text = fix_bar_latex(raw_text)
    
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(fixed_text)
        
    print(f"[REPARADO \\bar{{}} OK] {fname}")
