"""
Tests for CouncilPipeline.
"""

from src.multiagent_core.pipeline import CouncilPipeline


def test_council_pipeline():
    pipeline = CouncilPipeline()
    sample_text = """# Título de Prueba
""" + "teoría " * 850 + """
$$\\boxed{E = mc^2}$$

```python
import scipy.stats as stats
from IPython.display import display, Math
import matplotlib.pyplot as plt
import seaborn as sns

data = [1, 2, 3, 4, 5]
stats.shapiro(data)
plt.plot(data)
sns.histplot(data)
display(Math(r'\\bar{x} = 3.0'))
```
Interpretación y análisis nanotecnológico con referencia a Walpole.
"""
    res = pipeline.process_content(sample_text)
    assert "reports" in res
    assert "final_qa" in res
