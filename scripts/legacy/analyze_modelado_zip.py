"""
Script de análisis detallado del contenido del ZIP 'MODELADO Y SIMULACION'
Genera el reporte de inventario de notebooks (.ipynb) clasificado por profesor vs estudiantes.
"""

import zipfile
import json
import os
import re

zip_path = r'C:\Users\ljyud\Desktop\IA UCEMICH\MODELADO Y SIMULACIÓN\MODELADO Y SIMULACION 2025-2026-I-20260805T163733Z-1-001.zip'

with zipfile.ZipFile(zip_path, 'r') as z:
    file_list = z.namelist()
    ipynb_files = [f for f in file_list if f.endswith('.ipynb')]
    
    profesor_notebooks = []
    student_notebooks = []
    
    for nb_path in ipynb_files:
        info = z.getinfo(nb_path)
        size_mb = info.file_size / (1024 * 1024)
        filename = os.path.basename(nb_path)
        
        # Intentar leer los primeros bytes para determinar autoría
        try:
            with z.open(nb_path) as f:
                data = json.load(f)
                
            text_cells = []
            for cell in data.get('cells', []):
                if cell.get('cell_type') == 'markdown':
                    text_cells.append(''.join(cell.get('source', [])))
                    
            combined_text = ' '.join(text_cells[:5])
            
            is_student = False
            student_match = re.search(r'(Alumno|Estudiante|Integrantes?|Matr[íi]cula):\s*([^\n\r]+)', combined_text, re.IGNORECASE)
            
            if student_match:
                student_name = student_match.group(2).strip()
                is_student = True
            else:
                student_name = "Profesor / Mtro. Luis José Yudico Anaya"
                
            entry = {
                "path": nb_path,
                "filename": filename,
                "size_mb": round(size_mb, 2),
                "author": student_name,
                "is_student": is_student
            }
            
            if is_student:
                student_notebooks.append(entry)
            else:
                profesor_notebooks.append(entry)
                
        except Exception as e:
            profesor_notebooks.append({
                "path": nb_path,
                "filename": filename,
                "size_mb": round(size_mb, 2),
                "author": "Indeterminado",
                "is_student": False
            })

report_lines = []
report_lines.append("# Análisis Detallado del ZIP de Modelado y Simulación")
report_lines.append(f"**Archivo ZIP**: `{os.path.basename(zip_path)}`")
report_lines.append(f"**Ubicación**: `{zip_path}`")
report_lines.append(f"**Total de elementos en ZIP**: {len(file_list)}")
report_lines.append(f"**Total de Notebooks (.ipynb)**: {len(ipynb_files)}\n")

report_lines.append("---")
report_lines.append("## 🟢 NOTEBOOKS BASE DEL PROFESOR (Mtro. Luis José Yudico Anaya)")
report_lines.append(f"**Total identificados**: {len(profesor_notebooks)}\n")

report_lines.append("| Tamaño (MB) | Ruta en ZIP | Nombre del Archivo | Autor Detectado |")
report_lines.append("|---|---|---|---|")
for nb in sorted(profesor_notebooks, key=lambda x: x['size_mb'], reverse=True):
    report_lines.append(f"| {nb['size_mb']} MB | `{nb['path']}` | `{nb['filename']}` | {nb['author']} |")

report_lines.append("\n---")
report_lines.append("## 🎓 NOTEBOOKS DE ALUMNOS E ENTREGAS")
report_lines.append(f"**Total identificados**: {len(student_notebooks)}\n")

report_lines.append("| Tamaño (MB) | Ruta en ZIP | Nombre del Archivo | Alumno Detectado |")
report_lines.append("|---|---|---|---|")
for nb in sorted(student_notebooks, key=lambda x: x['size_mb'], reverse=True)[:30]: # Primeros 30
    report_lines.append(f"| {nb['size_mb']} MB | `{nb['path']}` | `{nb['filename']}` | {nb['author']} |")

out_report = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\docs\ANALISIS_MODELADO_SIMULACION.md'
with open(out_report, 'w', encoding='utf-8') as f:
    f.write('\n'.join(report_lines))

print(f"Análisis completado. Reporte generado en: {out_report}")
print(f"Notebooks del Profesor: {len(profesor_notebooks)} | Notebooks de Alumnos: {len(student_notebooks)}")
