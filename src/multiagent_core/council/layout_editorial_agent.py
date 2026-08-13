"""
LayoutEditorialAgent (@Editor): Agente especializado en la edición de diseño, maquetación,
limpieza de títulos descontextualizados y jerarquía de encabezados (H1, H2, H3).
"""

import re
from typing import Dict, Any, List


class LayoutEditorialAgent:
    """Agente Editor responsable del diseño editorial y maquetación visual limpia."""

    def __init__(self):
        self.displaced_title_patterns = [
            r'#+\s*\*?\*?Ejercicios\s+\d+.*',
            r'#+\s*\*?\*?Problemas\s+de\s+Nanotecnología.*',
            r'^\s*\*\*(Materia|Profesor|Semestre|Fecha):\*\*.*',
            r'^\s*(Materia|Profesor|Semestre|Fecha):\s*.*',
            r'#\s*\*\*PROBABILIDAD Y ESTADÍSTICA SEMESTRE.*'
        ]

    def audit_layout(self, markdown_text: str) -> Dict[str, Any]:
        issues = []
        lines = markdown_text.split('\n')
        
        # 1. Verificar si el primer encabezado secundario después de la cabecera es un título de ejercicio descontextualizado
        first_h2 = ""
        for line in lines[6:25]:
            if line.strip().startswith("#"):
                first_h2 = line.strip()
                break
                
        if "Ejercicios" in first_h2 or "Tarea" in first_h2:
            issues.append(f"⚠️ El inicio de la unidad arranca con un título de tarea o ejercicio ('{first_h2}') en lugar de la Fundamentación Teórica.")

        # 2. Verificar metadatos sueltos (Fecha, Semestre, Materia)
        for line in lines:
            if any(re.search(pat, line, re.IGNORECASE) for pat in [r'Semestre:', r'Fecha:\s*\d{2}/\d{2}']):
                issues.append(f"⚠️ Metadatos de tarea sueltos detectados: '{line.strip()}'")

        return {
            "passed": len(issues) == 0,
            "issues": issues,
            "first_heading": first_h2
        }

    def auto_fix_layout(self, markdown_text: str, default_intro_title: str = "## 1. Fundamentación Teórica y Conceptos Clave") -> str:
        lines = markdown_text.split('\n')
        header_block = lines[:6] # Mantener encabezado principal
        body_lines = lines[6:]
        
        cleaned_body = []
        has_intro_header = False
        
        for line in body_lines:
            stripped = line.strip()
            
            # Filtrar metadatos sueltos como "Semestre: 5.º semestre", "Fecha: 10/11/2025", "Materia: ..."
            if any(re.match(pat, stripped, re.IGNORECASE) for pat in [
                r'^\s*\*?\*?(Materia|Profesor|Semestre|Fecha):\*?\*?\s*.*',
                r'^#+\s*\*?\*?Ejercicios\s+\d+\s+Conclusiones.*',
            ]):
                continue
                
            if re.search(r'^##+\s*1\.\s+.*', stripped) or "Fundamentación Teórica" in stripped:
                has_intro_header = True
                
            cleaned_body.append(line)
            
        # Si la unidad no arranca con introducción teórica, agregarla arriba
        if not has_intro_header:
            cleaned_body = [default_intro_title, ""] + cleaned_body
            
        # Reconstruir texto
        fixed_text = '\n'.join(header_block + cleaned_body)
        fixed_text = re.sub(r'\n{3,}', '\n\n', fixed_text)
        return fixed_text

    def detect_duplicate_blocks(self, lessons: Dict[str, str]) -> List[Dict[str, Any]]:
        """Detecta bloques de texto (>=40 palabras) repetidos entre unidades o dentro
        de la misma unidad, via hash normalizado (whitespace colapsado, minusculas)."""
        import hashlib

        block_locations: Dict[str, List[Any]] = {}

        for unit_name, text in lessons.items():
            raw_blocks = re.split(r'\n\s*\n', text)
            for block_index, raw_block in enumerate(raw_blocks):
                words = raw_block.split()
                if len(words) < 40:
                    continue
                normalized = ' '.join(words).lower()
                block_hash = hashlib.sha256(normalized.encode('utf-8')).hexdigest()
                block_locations.setdefault(block_hash, []).append((unit_name, block_index))

        duplicates = [
            {"hash": block_hash, "locations": locations}
            for block_hash, locations in block_locations.items()
            if len(locations) >= 2
        ]
        return duplicates

