# CLAUDE.md — Guía de Desarrollo para AI Assistants

## Comandos de Desarrollo Rápido
- **Ejecutar Pruebas**: `pytest`
- **Compilar Lecciones a Notebooks**: `python -c "from src.multiagent_core.orchestrator_agent import OrchestratorAgent; OrchestratorAgent().run_full_pipeline()"`
- **Formatear Código**: `black src/ tests/`
- **Linter**: `ruff check src/ tests/`

## Convenciones de Código y Arquitectura
1. **Fuente de Verdad**: Los archivos en `lecciones/*.md` son la fuente primaria. NUNCA edites directamente los notebooks compilados `notebooks/*.ipynb`.
2. **Formato Matemático**: Usa notación LaTeX limpia en Markdown (`$$...$$` o `$..$`) y `display(Math(...))` en Python.
3. **Librerías Permitidas**: `scipy.stats`, `statsmodels`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `sympy`.
4. **Respeto a las 8 Reglas del Protocolo Maestro**: Toda lección debe contener teoría, ejemplo paso a paso, contexto nano, SymPy, solución `\boxed{}`, SciPy, 2 gráficos y diccionario de variables.
