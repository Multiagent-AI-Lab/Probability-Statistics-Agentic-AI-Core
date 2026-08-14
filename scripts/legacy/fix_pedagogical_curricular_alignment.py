"""
Script de Alineación Curricular y Corrección de Anacronismo Pedagógico:
1. Elimina el bloque de Pruebas de Hipótesis (Líneas 1586-1862) de UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md
   y lo traslada a UNIDAD_6_INFERENCIA_ESTIMACION.md.
2. Corrige los ParseError de KaTeX residuales ($$\mathbf{0.2466}$$.).
"""

import os
import re

u1_path = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\lecciones\UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md'
u6_path = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\lecciones\UNIDAD_6_INFERENCIA_ESTIMACION.md'

with open(u1_path, 'r', encoding='utf-8', errors='ignore') as f:
    u1_lines = f.readlines()

# Buscar donde inicia el anacronismo de Pruebas de Hipótesis en U1
hypothesis_start_idx = -1
for idx, line in enumerate(u1_lines):
    if '## Sección 5.1: Prueba de Hipótesis Estadística' in line or '## Prueba de Hipótesis Estadística' in line:
        hypothesis_start_idx = idx
        break

if hypothesis_start_idx != -1:
    # Buscar hasta donde llega el bloque de hipótesis antes del Módulo de Simulación KDE / Materials Project
    hypothesis_end_idx = len(u1_lines)
    for idx in range(hypothesis_start_idx, len(u1_lines)):
        if '## 10. Módulo de Simulación:' in u1_lines[idx] or '## 11. Módulo de Integración' in u1_lines[idx]:
            hypothesis_end_idx = idx
            break
            
    extracted_hypothesis_block = u1_lines[hypothesis_start_idx:hypothesis_end_idx]
    cleaned_u1_lines = u1_lines[:hypothesis_start_idx] + u1_lines[hypothesis_end_idx:]
    
    # Escribir U1 limpia
    with open(u1_path, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_u1_lines)
    print(f"[ALINEACIÓN U1 OK] Removidos {len(extracted_hypothesis_block)} líneas de Pruebas de Hipótesis anacrónicas de UNIDAD 1.")

    # Integrar bloque en U6 si no está presente
    hypothesis_text = "".join(extracted_hypothesis_block)
    
    # Limpiar KaTeX residual en el bloque extraído: $$\mathbf{0.2466}$$. -> $\mathbf{0.2466}$.
    hypothesis_text = re.sub(r'\$\$\\mathbf\{([^}]+)\}\$\$\.', r'$\\\\mathbf{\\1}$.', hypothesis_text)
    hypothesis_text = re.sub(r'\$\$\\mathbf\{([^}]+)\}\$\$', r'$\\\\mathbf{\\1}$', hypothesis_text)
    
    with open(u6_path, 'r', encoding='utf-8', errors='ignore') as f:
        u6_text = f.read()
        
    if "Prueba UMP" not in u6_text:
        with open(u6_path, 'w', encoding='utf-8') as f:
            f.write(u6_text + "\n\n" + hypothesis_text)
        print("[ALINEACIÓN U6 OK] Trasladado bloque de Pruebas de Hipótesis y UMP a UNIDAD 6.")
    else:
        print("[ALINEACIÓN U6 OK] El bloque de Pruebas de Hipótesis ya existía en UNIDAD 6.")
else:
    print("[ALINEACIÓN U1 OK] UNIDAD 1 ya está limpia de Pruebas de Hipótesis.")
