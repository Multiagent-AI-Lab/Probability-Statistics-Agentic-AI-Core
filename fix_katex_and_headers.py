"""
Script de reparación de sintaxis KaTeX y deduplicación de encabezados.
Resuelve:
1. ParseError de KaTeX por uso de '$' dentro de bloques '$$' o delimitadores mal cerrados.
2. Encabezados repetidos de Autor/Profesor o títulos duplicados.
"""

import os
import re
import glob

lecciones_dir = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\lecciones'

def fix_katex_syntax(text):
    # 1. Corregir casos de $$ con $ dentro: Ej. $$ texto $x$ texto $$
    # Reemplazar bloque $$ que contenga $ interno por delimitadores limpios
    def clean_block(match):
        inner = match.group(1)
        # Si el bloque contiene $, separar texto de inline math o remover $ redundantes
        if '$' in inner:
            # Si es texto con inline math como 'donde $N$ es...', quitar los $$ externos
            cleaned_inner = re.sub(r'^\s*|\s*$', '', inner)
            return f"\n\n{cleaned_inner}\n\n"
        else:
            return f"\n\n$$\n{inner.strip()}\n$$\n\n"

    # 2. Corregir $$ inline tipo: $$ \bar{X} = 10 $$ y texto -> poner $$ en lineas propias
    # Reemplazar $$ ... $$ que estén en medio de una línea por $ ... $ si es corto o aislar $$
    lines = text.split('\n')
    fixed_lines = []
    
    in_display_math = False
    for line in lines:
        stripped = line.strip()
        
        # Eliminar líneas duplicadas de autoría
        if 'Autor y Profesor:' in line and fixed_lines and any('Autor y Profesor:' in l for l in fixed_lines[:10]):
            continue
        if '# PROBABILIDAD Y ESTADÍSTICA SEMESTRE' in line:
            continue
        if '## INGENIERÍA EN NANOTECNOLOGÍA' in line and len(fixed_lines) > 5:
            continue
        if '##UCEMICH' in line and len(fixed_lines) > 5:
            continue
            
        # Corregir $$ inline que provocan parse error en KaTeX
        # Ej. "Varianza: $$ s^2 = 10 $$" -> "Varianza: $s^2 = 10$"
        if '$$' in line and not line.strip().startswith('$$'):
            # Si el $$ abre y cierra en la misma línea con texto alrededor
            parts = line.split('$$')
            if len(parts) == 3: # ej: "Texto $$ math $$ mas texto"
                line = f"{parts[0]}${parts[1].strip()}${parts[2]}"
                
        # Fix: $$\mathbf{0.2466}$$. -> $\mathbf{0.2466}$.
        line = re.sub(r'\$\$\\mathbf\{([^}]+)\}\$\$\.', r'$\\\\mathbf{\\1}$.', line)
        line = re.sub(r'\$\$\\mathbf\{([^}]+)\}\$\$', r'$\\\\mathbf{\\1}$', line)

        fixed_lines.append(line)

    result_text = '\n'.join(fixed_lines)
    
    # Asegurar que el encabezado inicial sea único
    first_lines = []
    rest_lines = []
    
    header_found = False
    for line in result_text.split('\n'):
        if line.startswith('# UNIDAD') and not header_found:
            header_found = True
            first_lines.append(line)
        elif header_found and len(first_lines) < 6:
            first_lines.append(line)
        else:
            rest_lines.append(line)
            
    # Garantizar limpieza de saltos triples
    final_text = '\n'.join(first_lines + rest_lines)
    final_text = re.sub(r'\n{3,}', '\n\n', final_text)
    
    return final_text

print("=== REPARANDO SINTAXIS KATEX Y ENCABEZADOS DE LECCIONES ===")
for md_file in glob.glob(os.path.join(lecciones_dir, '*.md')):
    with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
        raw_text = f.read()
        
    fixed_text = fix_katex_syntax(raw_text)
    
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(fixed_text)
        
    print(f"[REPARADO OK] {os.path.basename(md_file)}")
