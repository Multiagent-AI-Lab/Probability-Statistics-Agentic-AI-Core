import glob
import os

lecciones_dir = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\lecciones'
delim = "$$"

def audit_katex_in_text(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        
    errors = []
    for idx, line in enumerate(lines, 1):
        if delim in line:
            parts = line.split(delim)
            for i, p in enumerate(parts):
                if i % 2 == 1:
                    if '$' in p:
                        errors.append((idx, line.strip()[:100]))
                        
    return errors

for filepath in sorted(glob.glob(os.path.join(lecciones_dir, '*.md'))):
    errs = audit_katex_in_text(filepath)
    fname = os.path.basename(filepath)
    if errs:
        print(f"MISMATCH {fname}: {len(errs)} lineas con $ dentro de $$")
        for line_num, l_text in errs[:5]:
            print(f"   Linea {line_num}: {l_text}")
    else:
        print(f"CLEAN {fname}: Sintaxis KaTeX limpia")
