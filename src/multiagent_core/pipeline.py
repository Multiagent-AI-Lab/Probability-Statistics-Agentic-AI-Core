"""
Pipeline: Orquestador principal del Consejo de 8 Expertos con Loops L1, L2 y L3.
"""

from typing import Dict, Any
from .council.architect_agent import ArchitectAgent
from .council.scientist_agent import ScientistAgent
from .council.engineer_agent import EngineerAgent
from .council.safety_gate_agent import SafetyGateAgent
from .council.analyst_agent import AnalystAgent
from .council.librarian_agent import LibrarianAgent
from .council.qa_agent import QAAgent
from .council.layout_editorial_agent import LayoutEditorialAgent


class CouncilPipeline:
    """Pipeline que coordina la refactorización y auditoría mediante el Consejo de 8 Expertos."""

    def __init__(self):
        self.editor = LayoutEditorialAgent()
        self.architect = ArchitectAgent()
        self.scientist = ScientistAgent()
        self.engineer = EngineerAgent()
        self.safety_gate = SafetyGateAgent()
        self.analyst = AnalystAgent()
        self.librarian = LibrarianAgent()
        self.qa = QAAgent()

    def process_content(
        self, text_or_code: str, unit_name: str = "", file_tree: list = None
    ) -> Dict[str, Any]:
        """Ejecuta el Consejo de 8 Expertos sobre una única lección/unidad.

        Nota de diseño sobre `file_tree` (@Architect, opt-in/advisory):
        `ArchitectAgent.validate_structure` audita la *completitud del curso
        completo* (¿existen las 8 UNIDAD_* del programa?), no la validez de
        una lección individual. `process_content()` en cambio se invoca por
        lección (una unidad a la vez, p.ej. desde
        `OrchestratorAgent._check_gate` y desde
        `PedagogicalReviewPipeline.review_and_auto_fix_lesson`). Pasar aquí
        un `file_tree` real del directorio de lecciones bloquearía la
        auditoría de UNIDAD_1 solo porque UNIDAD_5 no está presente en ese
        momento (normal durante desarrollo incremental o en tests que usan
        subconjuntos de unidades) — un falso bloqueo sin relación con la
        calidad de la lección auditada. Por eso ningún caller de producción
        pasa `file_tree` hoy: @Architect queda deliberadamente como
        advisory/opt-in en este flujo (ver GOVERNANCE.md §2), no conectado
        por defecto. Un caller que sí necesite auditar completitud curricular
        puede invocar `ArchitectAgent.validate_structure(file_tree)`
        directamente fuera de este pipeline por-lección.
        """
        # 0. Editor (limpieza estructural, corre primero para que el resto
        #    audite contenido ya limpio de metadatos sueltos/títulos descontextualizados)
        editor_res = self.editor.audit_layout(text_or_code)

        # 1. Architect (estructura del proyecto; solo valida si se provee file_tree)
        architect_res = (
            self._normalize_architect_result(self.architect.validate_structure(file_tree))
            if file_tree is not None
            else {"passed": True, "skipped": True}
        )

        # 2. Scientist (Teoría y LaTeX)
        sci_res = self.scientist.check_theory(text_or_code)

        # 3. Engineer (Código SciPy/Statsmodels + guardrail de convergencia Monte Carlo)
        eng_res = self.engineer.check_code_implementation(text_or_code)
        mc_res = self.engineer.check_monte_carlo_convergence(text_or_code)
        eng_res["passed"] = eng_res["passed"] and not mc_res["critical"]
        eng_res["monte_carlo_warnings"] = mc_res["warnings"]

        # 4. Safety Gate (Loop L1: Verificación de Supuestos Estadísticos + secuencia curricular)
        gate_res = self.safety_gate.validate_assumptions(text_or_code, unit_name)

        # 5. Analyst (Visualizaciones e Interpretación)
        ana_res = self.analyst.audit_visualizations(text_or_code)

        # 6. Librarian (Loop L2: Verificación de Literatura)
        lib_res = self.librarian.verify_references(text_or_code)

        reports = {
            "editor": editor_res,
            "architect": architect_res,
            "scientist": sci_res,
            "engineer": eng_res,
            "safety_gate": gate_res,
            "analyst": ana_res,
            "librarian": lib_res,
        }

        # 7. QA Agent (Loop L3: Verificación Final del Protocolo Maestro)
        final_qa = self.qa.final_audit(reports)

        return {
            "approved": final_qa["approved"],
            "reports": reports,
            "final_qa": final_qa,
        }

    @staticmethod
    def _normalize_architect_result(result: Dict[str, Any]) -> Dict[str, Any]:
        return {**result, "passed": result.get("valid", False)}
