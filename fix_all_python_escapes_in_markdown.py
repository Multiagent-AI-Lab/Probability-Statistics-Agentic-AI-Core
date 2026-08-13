"""
Fix all ASCII escape corruption (0x08 backspace -> \\bar, 0x09 tab -> \\text)
across all Markdown lessons and re-compile Jupyter Notebooks.
"""

import os
import glob
import re

lecciones_dir = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\lecciones'

def sanitize_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        
    # 1. Reparar \bar{} corrompido por \b (ASCII 0x08)
    text = text.replace('\x08ar{', '\\bar{')
    text = text.replace('\x08', '\\')
    text = re.sub(r'\$ar\{([^}]+)\}\$', r'$\\bar{\1}$', text)
    text = re.sub(r'\$ar\{([^}]+)\}', r'$\\bar{\1}', text)
    text = re.sub(r'\(ar\{([^}]+)\}', r'(\\bar{\1}', text)
    text = re.sub(r'\s+ar\{([^}]+)\}', r' \\bar{\1}', text)
    text = text.replace('($ar{X}$)', '($\\bar{X}$)')
    text = text.replace('$ar{X}$', '$\\bar{X}$')

    # 2. Reparar \text{} corrompido por \t (ASCII 0x09)
    text = text.replace('\text{', '\\text{')
    text = text.replace('\t\text{', '\\text{')
    text = re.sub(r'\t\s*ext\{', r'\\text{', text)
    text = re.sub(r'\t+ext\{', r'\\text{', text)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

print("=== DEPURANDO Y SANITIZANDO SECUENCIAS DE ESCAPE EN LECCIONES ===")
for md_file in sorted(glob.glob(os.path.join(lecciones_dir, '*.md'))):
    fname = os.path.basename(md_file)
    sanitize_markdown_file(md_file)
    print(f"[SANITIZADO OK] {fname}")
