"""
Tests for NotebookCompilerAgent.
"""

import os
from src.multiagent_core.notebook_compiler_agent import NotebookCompilerAgent


def test_parse_markdown_to_cells():
    compiler = NotebookCompilerAgent()
    md_content = """# Title
    
Some text explanation.

```python
import numpy as np
print("Hello World")
```
"""
    cells = compiler.parse_markdown_to_cells(md_content)
    assert len(cells) >= 2
    assert cells[0]["cell_type"] == "markdown"
    assert cells[1]["cell_type"] == "code"
