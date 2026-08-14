"""
Script maestro para sanitizar globalmente los 8 archivos de lecciones en lecciones/*.md:
- Sanear ar{X} -> \bar{X}
- Sanear $$\mathbf{...}$$ -> $\mathbf{...}$
- Sanear \ilde -> \tilde, \lpha -> \alpha
- Verificar 1 solo H1 por unidad
"""

import glob
import os
import re

lecciones = sorted(glob.glob('lecciones/*.md'))

for filepath in lecciones:
    fname = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    # 1. Sanear ar{X} -> \bar{X}
    text = re.sub(r'(?<!b)ar\{([A-Za-z])\}', r'\\bar{\1}', text)

    # 2. Sanear $$\mathbf{...}$$ -> $\mathbf{...}$
    text = re.sub(r'\$\$\\mathbf\{([^}]*)\}\$\$', r'$\\mathbf{\1}$', text)

    # 3. Typos KaTeX
    text = text.replace('\\ilde{', '\\tilde{').replace('\\lpha', '\\alpha')

    # 4. Asegurar 1 solo H1 por lección (líneas secundarias con # -> ##)
    lines = text.split('\n')
    new_lines = []
    h1_found = False
    for line in lines:
        if line.startswith('# '):
            if not h1_found:
                h1_found = True
                new_lines.append(line)
            else:
                new_lines.append('#' + line)  # Convertir a ##
        else:
            new_lines.append(line)

    cleaned_text = '\n'.join(new_lines)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(cleaned_text)

    print(f"[SANIDAD OK] {fname}")

print("\n=== SANITIZACIÓN KATEX Y HIERARCHY COMPLETADA EN LAS 8 UNIDADES ===")
