# CLAUDE.md — Guía de Desarrollo para AI Assistants

## Comandos de Desarrollo Rápido
- **Ejecutar Pruebas**: `pytest`
- **Compilar Lecciones a Notebooks**: `python -c "from src.multiagent_core.orchestrator_agent import OrchestratorAgent; OrchestratorAgent().run_full_pipeline()"`
- **Formatear Código** (en ese orden): `isort src/ tests/` → `black src/ tests/` (el `setup.cfg` fija `profile = black` para que ambos coincidan sin reformatear entre sí)
- **Linter**: `ruff check src/ tests/`

## Convenciones de Código y Arquitectura
1. **Fuente de Verdad**: Los archivos en `lecciones/*.md` son la fuente primaria. NUNCA edites directamente los notebooks compilados `notebooks/*.ipynb`.
2. **Formato Matemático**: Usa notación LaTeX limpia en Markdown (`$$...$$` o `$..$`) y `display(Math(...))` en Python.
3. **Librerías Permitidas**: `scipy.stats`, `statsmodels`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `sympy`.
4. **Respeto a las 8 Reglas del Protocolo Maestro**: Toda lección debe contener teoría, ejemplo paso a paso, contexto nano, SymPy, solución `\boxed{}`, SciPy, 2 gráficos y diccionario de variables.

## Trabajo no trivial (nuevo agente, cambio de arquitectura)

Para cualquier feature nueva o cambio que no sea un fix puntual, sigue el flujo `superpowers:brainstorming` → spec en `docs/superpowers/specs/` → `superpowers:writing-plans` → plan en `docs/superpowers/plans/` (ambos gitignored, solo locales). Revisar specs/planes existentes antes de proponer algo que pueda solaparse.
