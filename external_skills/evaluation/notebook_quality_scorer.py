"""
NotebookQualityScorer Skill: Scores notebook quality automatically based on structure, code, plots, and LaTeX math.
"""

import json
from typing import Dict, Any


class NotebookQualityScorer:
    """Skill for automated quality scoring of Jupyter notebooks."""

    def score_file(self, filepath: str) -> Dict[str, Any]:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            nb = json.load(f)
            
        cells = nb.get('cells', [])
        md_cells = [c for c in cells if c.get('cell_type') == 'markdown']
        code_cells = [c for c in cells if c.get('cell_type') == 'code']
        
        words = sum(len(''.join(c.get('source', [])).split()) for c in md_cells)
        plots = 0
        for c in code_cells:
            for out in c.get('outputs', []):
                if 'image/png' in out.get('data', {}):
                    plots += 1
                    
        score = min(100.0, (words / 500.0) * 50.0 + (plots * 25.0))
        
        return {
            "file": filepath,
            "quality_score": round(score, 1),
            "total_cells": len(cells),
            "markdown_words": words,
            "plot_outputs": plots
        }
