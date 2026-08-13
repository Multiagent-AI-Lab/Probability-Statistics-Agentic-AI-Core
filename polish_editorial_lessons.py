"""
Script de pulido editorial para eliminar banners de título internos repetidos
y garantizar una maquetación profesional e impecable en todas las lecciones.
"""

import os
import re
import glob

lecciones_dir = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\lecciones'

redundant_patterns = [
    r'#\s*\*\*INGENIER[ÍI]A\s+EN\s+NANOTECNOLOG[ÍI]A\*\*',
    r'##\s*UCEMICH.*',
    r'##\s*\*\*CURSO:\s*PROBABILIDAD\s+Y\s+ESTAD[ÍI]STICA\*\*',
    r'SEMESTRE\s+2024-2025-I',
    r'SEMESTRE\s+2025-2026-I',
    r'SEMESTRE\s+2025-2026\s*-\s*I',
    r'###\s*Profesor:\s*\*\*Mtro\.\s+Luis\s+Jos[ée]\s+Yudico\s+Anaya\*\*',
    r'<!--\s*Origen:.*-->'
]

def polish_lesson_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    lines = content.split('\n')
    header_lines = lines[:6] # Mantener el encabezado principal intacto
    body_lines = lines[6:]
    
    cleaned_body = []
    for line in body_lines:
        skip = False
        for pat in redundant_patterns:
            if re.match(pat, line.strip(), re.IGNORECASE):
                skip = True
                break
        if not skip:
            cleaned_body.append(line)
            
    # Reconstruir contenido limpio
    polished_text = '\n'.join(header_lines + cleaned_body)
    
    # Remover múltiples saltos de línea consecutivos
    polished_text = re.sub(r'\n{3,}', '\n\n', polished_text)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(polished_text)

print("=== PULIENDO MAQUETACIÓN EDITORIAL DE LECCIONES ===")
for md_file in glob.glob(os.path.join(lecciones_dir, '*.md')):
    polish_lesson_file(md_file)
    print(f"[PULIDO EDITORIAL OK] {os.path.basename(md_file)}")
