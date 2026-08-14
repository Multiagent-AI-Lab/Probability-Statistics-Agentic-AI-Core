"""
Script maestro para estandarizar y corregir la numeración de encabezados (H2/H3)
y comentarios de código Python en las 8 lecciones del curso.
"""

import glob
import os
import re

lecciones = sorted(glob.glob('lecciones/*.md'))

for filepath in lecciones:
    fname = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    new_lines = []
    in_python_code = False

    current_h2_num = 0
    current_h3_idx = 0

    for line in lines:
        sline = line.strip()

        # Rastrear bloques de código
        if sline.startswith('```python'):
            in_python_code = True
            new_lines.append(line)
            continue
        elif sline.startswith('```') and in_python_code:
            in_python_code = False
            new_lines.append(line)
            continue

        # Si estamos DENTRO de un bloque de código Python, los comentarios ## o ### se convierten a #
        if in_python_code:
            if line.lstrip().startswith('## ') or line.lstrip().startswith('### '):
                # Reemplazar encabezados markdown dentro de código Python por comentarios estándar #
                indent = line[:len(line) - len(line.lstrip())]
                comment_text = line.lstrip().lstrip('#').strip()
                new_lines.append(f"{indent}# {comment_text}\n")
            else:
                new_lines.append(line)
            continue

        # FUERA de bloques de código (Markdown puro):

        # 1. Convertir metadatos de Asignatura / UCEMICH / Autor a texto secundario
        if sline.startswith('## Asignatura:') or sline.startswith('### UCEMICH') or sline.startswith('### Autor y Profesor:'):
            clean_txt = sline.lstrip('#').strip()
            new_lines.append(f"> **{clean_txt}**\n")
            continue

        # 2. Procesar Encabezados H2 (##)
        if sline.startswith('## '):
            # Ignorar separadores como ## --------------
            if set(sline.replace('##', '').strip()) <= {'-', '*', '='}:
                continue

            # Buscar si tiene número (arábigo o romano) o guión
            m_arabic = re.match(r'##\s+(\d+)[\.\–\-]\s*(.*)', sline)
            m_roman = re.match(r'##\s+([I|V|X]+)[\.\–\-]\s*(.*)', sline, re.IGNORECASE)
            m_bare_num = re.match(r'##\s+(\d+)\s*$', sline)

            if m_arabic:
                current_h2_num = int(m_arabic.group(1))
                current_h3_idx = 0
                title = m_arabic.group(2).strip()
                new_lines.append(f"## {current_h2_num}. {title}\n")
            elif m_roman:
                current_h2_num += 1
                current_h3_idx = 0
                title = m_roman.group(2).strip()
                new_lines.append(f"## {current_h2_num}. {title}\n")
            elif m_bare_num:
                current_h2_num = int(m_bare_num.group(1))
                current_h3_idx = 0
                new_lines.append(f"## {current_h2_num}. Tema {current_h2_num}\n")
            else:
                # H2 sin número (ej. ## PDF, ## CDF, ## Varianza, ## Módulo de Simulación...)
                title = sline.replace('##', '').strip()
                # Si parece un título de sección principal
                if 'Módulo de Simulación' in title:
                    current_h2_num = 10
                    current_h3_idx = 0
                    new_lines.append(f"## 10. {title.replace('10.', '').strip()}\n")
                elif current_h2_num > 0:
                    # Convertir H2 huérfano en H3 dentro del H2 activo
                    current_h3_idx += 1
                    new_lines.append(f"### {current_h2_num}.{current_h3_idx} {title}\n")
                else:
                    current_h2_num += 1
                    current_h3_idx = 0
                    new_lines.append(f"## {current_h2_num}. {title}\n")
            continue

        # 3. Procesar Encabezados H3 (###)
        if sline.startswith('### '):
            m_h3 = re.match(r'###\s+(\d+)\.(\d+)\s*(.*)', sline)
            if m_h3:
                p_num = int(m_h3.group(1))
                s_num = int(m_h3.group(2))
                title = m_h3.group(3).strip()

                # Ajustar número de padre si no coincide con H2 activo
                if current_h2_num > 0 and p_num != current_h2_num:
                    p_num = current_h2_num

                current_h3_idx = s_num
                new_lines.append(f"### {p_num}.{s_num} {title}\n")
            else:
                title = sline.replace('###', '').strip()
                if current_h2_num > 0:
                    current_h3_idx += 1
                    new_lines.append(f"### {current_h2_num}.{current_h3_idx} {title}\n")
                else:
                    new_lines.append(f"### {title}\n")
            continue

        new_lines.append(line)

    cleaned_content = ''.join(new_lines)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

    print(f"[ESTANDARIZADO OK] {fname}")

print("\n=== NORMALIZACIÓN COMPLETA DE ENCABEZADOS Y CÓDIGO FINALIZADA ===")
