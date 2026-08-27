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


# PROJECT_PLAN Integration
# Added by Claude Config Manager Extension

When working on this project, always refer to and maintain the project plan located at `PROJECT_PLAN.md` in the workspace root.

**Instructions for Claude Code:**
1. **Read the project plan first** - Always check `PROJECT_PLAN.md` when starting work to understand the project context, architecture, and current priorities.
2. **Update the project plan regularly** - When making significant changes, discoveries, or completing major features, update the relevant sections in PROJECT_PLAN.md to keep it current.
3. **Use it for context** - Reference the project plan when making architectural decisions, understanding dependencies, or explaining code to ensure consistency with project goals.

**Plan Mode Integration:**
- **When entering plan mode**: Read the current PROJECT_PLAN.md to understand existing context and priorities
- **During plan mode**: Build upon and refine the existing project plan structure
- **When exiting plan mode**: ALWAYS update PROJECT_PLAN.md with your new plan details, replacing or enhancing the relevant sections (Architecture, TODO, Development Workflow, etc.)
- **Plan persistence**: The PROJECT_PLAN.md serves as the permanent repository for all planning work - plan mode should treat it as the single source of truth

This ensures better code quality and maintains project knowledge continuity across different Claude Code sessions and plan mode iterations.
