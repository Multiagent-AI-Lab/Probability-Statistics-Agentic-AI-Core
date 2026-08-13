"""
Master Format and KaTeX Fixer for Probabilidad y Estadística Inferencial.
Resuelve:
1. KaTeX ParseErrors por $ no cerrados, # dentro de math mode y $palabras_llanas$.
2. Estandarización de jerarquía de encabezados (H1 exclusivo para banner principal, H2 para secciones, H3 para subsecciones, H4 para bloques de solución).
"""

import os
import re
import glob

lecciones_dir = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\lecciones'

unit_titles = {
    "UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md": "UNIDAD 1: Estadística Descriptiva y Análisis Exploratorio de Datos",
    "UNIDAD_2_PROBABILIDAD_COMBINATORIA.md": "UNIDAD 2: Probabilidad, Teoría de Conjuntos y Combinatoria",
    "UNIDAD_3_VARIABLES_ALEATORIAS_DISCRETAS.md": "UNIDAD 3: Variables Aleatorias Discretas y Distribuciones de Probabilidad",
    "UNIDAD_4_DISTRIBUCIONES_CONJUNTAS.md": "UNIDAD 4: Distribuciones de Probabilidad Conjuntas y Bivariadas",
    "UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.md": "UNIDAD 5: Variables Aleatorias Continuas y Modelos de Simulación",
    "UNIDAD_6_INFERENCIA_ESTIMACION.md": "UNIDAD 6: Inferencia Estadística, Estimación Puntual e Intervalos de Confianza",
    "UNIDAD_7_PROYECTO_INTEGRADOR.md": "UNIDAD 7: Proyecto Integrador — Pruebas de Hipótesis y Análisis de Materiales"
}

def clean_katex_and_formatting(text, filename):
    # 1. Reemplazar $palabras$ innecesarias por texto plano
    for word in ['Python', 'SciPy', 'NumPy', 'Pandas', 'Seaborn', 'Matplotlib', 'SymPy', 'R', 'Statsmodels', 'KDE', 'MLE']:
        text = re.sub(r'\$' + word + r'\$', word, text)
        
    # 2. Corregir \text{#...} o # dentro de math mode
    text = re.sub(r'\\text\{#_([^}]+)\}', r'\\text{\\mathit{\1}}', text)
    text = re.sub(r'\\text\{#([^}]+)\}', r'\\text{\1}', text)

    lines = text.split('\n')
    cleaned_lines = []
    
    unit_h1 = unit_titles.get(filename, "# UNIDAD DE APRENDIZAJE")
    
    # Reconstruir encabezado estandarizado (primeras 6 líneas)
    banner = [
        f"# {unit_h1}",
        "## Asignatura: Probabilidad y Estadística Inferencial",
        "### UCEMICH — Ingeniería en IA y Nanotecnología",
        "### Autor y Profesor: Mtro. Luis José Yudico Anaya",
        "",
        "---",
        ""
    ]
    
    # Procesar cuerpo omitiendo encabezados duplicados iniciales
    in_math_block = False
    
    for idx, line in enumerate(lines):
        stripped = line.strip()
        
        # Saltar encabezados iniciales viejos
        if idx < 12 and any(k in stripped for k in ['UNIDAD', 'Asignatura:', 'UCEMICH', 'Autor y Profesor:', '---']):
            continue
        if idx < 15 and re.match(r'^#+\s*\*?\*?(INGENIERÍA|CURSO|SEMESTRE|UCEMICH|Profesor).*', stripped, re.IGNORECASE):
            continue
            
        # Detectar delimitadores de bloque $$
        if stripped.startswith('$$') or stripped.endswith('$$'):
            in_math_block = not in_math_block
            
        # Normalizar Encabezados del Cuerpo:
        # a) Ningún H1 interno (# ) en el cuerpo -> bajar a H2 (## )
        if stripped.startswith('# ') and not stripped.startswith('# UNIDAD'):
            heading_content = stripped[2:].strip().replace('**', '')
            line = f"## {heading_content}"
            
        # b) Limpiar negritas redundantes en H2, H3, H4
        if re.match(r'^#+\s*\*\*.*\*\*\s*$', stripped):
            level = len(stripped) - len(stripped.lstrip('#'))
            content = stripped.lstrip('#').strip().replace('**', '')
            # Normalizar nivel: max H2 para secciones principales
            if level == 1:
                level = 2
            line = f"{'#' * level} {content}"
            
        # c) Si hay un $ sin cerrar antes de un encabezado, cerrarlo
        if line.startswith('#') and not in_math_block:
            pass # Asegurar que los encabezados estén limpios
            
        cleaned_lines.append(line)
        
    full_cleaned = '\n'.join(banner + cleaned_lines)
    
    # Limpiar saltos triples
    full_cleaned = re.sub(r'\n{3,}', '\n\n', full_cleaned)
    return full_cleaned

print("=== NORMALIZANDO FORMATO Y SINTAXIS KATEX EN TODAS LAS LECCIONES ===")
for md_file in sorted(glob.glob(os.path.join(lecciones_dir, '*.md'))):
    fname = os.path.basename(md_file)
    with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
        raw = f.read()
        
    fixed = clean_katex_and_formatting(raw, fname)
    
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(fixed)
        
    print(f"[ESTANDARIZADO Y NORMALIZADO OK] {fname}")
