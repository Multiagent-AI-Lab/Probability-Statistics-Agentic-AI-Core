import glob
import os

lecciones_dir = r'C:\Users\ljyud\Desktop\IA UCEMICH\PROBABILIDAD Y ESTADÍSTICA\lecciones'

for filepath in sorted(glob.glob(os.path.join(lecciones_dir, '*.md'))):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    for idx, line in enumerate(lines, 1):
        if "rf'\\text{" in line or 'rf"\\text{' in line:
            clean = line.strip().encode('ascii', 'ignore').decode('ascii')
            print(f"{os.path.basename(filepath)} L{idx}: {clean[:100]}")
