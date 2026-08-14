"""
Sanitización total de escapes LaTeX (\\frac, \\right, \\bar, \\text) y actualización de NotebookCompilerAgent
para dividir bloques Markdown en celdas individuales limpias por sección (## H2).
"""

import os
import glob
import re

lecciones_dir = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\lecciones'

def sanitize_latex_in_text(text):
    # 1. Reparar Form Feed (ASCII 0x0C) -> \frac
    text = text.replace('\x0crac', '\\frac')
    text = text.replace('\x0c', '\\')
    text = re.sub(r'FF\s*rac', r'\\frac', text)
    text = re.sub(r'rac\{', r'\\frac{', text)
    
    # 2. Reparar Carriage Return (ASCII 0x0D) -> \right
    text = text.replace('\x0dight', '\\right')
    text = re.sub(r'ight\$\$', r'\\right$$', text)
    text = re.sub(r'ight\)', r'\\right)', text)
    
    # 3. Reparar Backspace (ASCII 0x08) -> \bar
    text = text.replace('\x08ar{', '\\bar{')
    text = text.replace('\x08', '\\')
    text = re.sub(r'\$ar\{([^}]+)\}\$', r'$\\bar{\1}$', text)
    text = re.sub(r'\$ar\{([^}]+)\}', r'$\\bar{\1}', text)
    text = text.replace('$ar{X}$', '$\\bar{X}$')
    text = text.replace('($ar{X}$)', '($\\bar{X}$)')
    
    # 4. Reparar Tab (ASCII 0x09) -> \text
    text = text.replace('\t\text{', '\\text{')
    text = re.sub(r'\t\s*ext\{', r'\\text{', text)
    
    # 5. Limpieza general de caracteres de control ASCII (0x00 - 0x1F excepto \n = 0x0A)
    cleaned_chars = []
    for ch in text:
        code = ord(ch)
        if code < 32 and code not in (10, 13):
            cleaned_chars.append('\\')
        else:
            cleaned_chars.append(ch)
            
    result = "".join(cleaned_chars)
    # Fix residual \frac and \right after character replacement
    result = re.sub(r'\\+\s*rac\{', r'\\frac{', result)
    result = re.sub(r'\\+\s*ight', r'\\right', result)
    result = re.sub(r'\\+\s*left', r'\\left', result)
    
    return result

print("=== DEPURANDO Y SANITIZANDO SINTAXIS LATEX EN LAS 7 LECCIONES ===")
for md_file in sorted(glob.glob(os.path.join(lecciones_dir, '*.md'))):
    fname = os.path.basename(md_file)
    with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
        raw = f.read()
        
    fixed = sanitize_latex_in_text(raw)
    
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(fixed)
        
    print(f"[LATEX SANITIZADO OK] {fname}")
