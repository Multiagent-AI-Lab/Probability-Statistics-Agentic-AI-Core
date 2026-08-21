"""
OrchestratorAgent: Coordinates compilation, code auditing, content auditing, and evaluation pipeline.
"""

import os
from pathlib import Path
from typing import Any

from .code_auditor_agent import CodeAuditorAgent
from .content_auditor_agent import ContentAuditorAgent
from .curriculum_map_agent import CurriculumMapAgent
from .evaluator_agent import EvaluatorAgent
from .notebook_compiler_agent import NotebookCompilerAgent
from .pipeline import CouncilPipeline


class OrchestratorAgent:
    """Orchestrator for the multiagent auditing and compilation pipeline."""

    def __init__(
        self, lecciones_dir: str = "lecciones", notebooks_dir: str = "notebooks"
    ):
        self.compiler = NotebookCompilerAgent(
            lecciones_dir=lecciones_dir, notebooks_dir=notebooks_dir
        )
        self.code_auditor = CodeAuditorAgent()
        self.content_auditor = ContentAuditorAgent()
        self.evaluator = EvaluatorAgent()
        self.council = CouncilPipeline()
        self.curriculum_map_agent = CurriculumMapAgent()

    @staticmethod
    def _unit_name_from_filename(md_filename: str) -> str:
        if "UNIDAD_" in md_filename:
            return f"UNIDAD {md_filename.split('_')[1]}"
        return md_filename

    # Reportes del Consejo promovidos a bloqueantes ademas de safety_gate:
    # los unicos 3 con logica real de deteccion de un defecto de publicacion
    # (no un stub que siempre pasa, como librarian). Ver GOVERNANCE.md #4.
    _BLOCKING_REPORTS = ("engineer", "editor", "scientist", "analyst")

    @staticmethod
    def _describe_failed_report(name: str, report: dict[str, Any]) -> str:
        """Arma un detalle legible del motivo de fallo de un reporte, usando
        los campos numericos que cada agente expone (si estan presentes) en
        vez de solo su nombre, para que quien depure localmente sepa que
        corregir sin re-ejecutar el pipeline."""
        if name == "scientist" and "word_count" in report:
            return (
                f"{name} (palabras={report['word_count']}, "
                f"formulas={report.get('math_equation_count', 0)})"
            )
        if name == "analyst" and "plot_count" in report:
            return (
                f"{name} (graficos={report['plot_count']}, "
                f"interpretacion={report.get('has_interpretation', False)})"
            )
        if name == "engineer" and "has_scipy_or_statsmodels" in report:
            return f"{name} (scipy/statsmodels={report['has_scipy_or_statsmodels']})"
        if name == "editor" and "issues" in report:
            return f"{name} ({len(report['issues'])} hallazgo(s) de maquetación)"
        if name == "architect" and "missing_units" in report:
            return f"{name} (unidades faltantes={report['missing_units']})"
        return name

    def _check_gate(
        self,
        md_filename: str,
        md_text: str,
        duplicate_unit_names: set,
        file_tree: list[str] | None = None,
    ) -> dict[str, Any]:
        """`file_tree` solo debe pasarse desde un caller que conozca el
        listado completo de lecciones del curso (hoy: `run_full_pipeline`).
        Con `file_tree`, @Architect se vuelve bloqueante (completitud real
        del curso); sin él, `process_content` lo deja como advisory/opt-in
        (`{"passed": True, "skipped": True}`) para no bloquear una lección
        válida solo porque se audita de forma aislada. Ver GOVERNANCE.md §4."""
        unit_name = self._unit_name_from_filename(md_filename)

        council_result = self.council.process_content(
            md_text, unit_name=unit_name, file_tree=file_tree
        )
        reports = council_result["reports"]

        safety_result = reports["safety_gate"]
        if safety_result["critical"]:
            reason = "; ".join(w for w in safety_result["warnings"] if "🚨" in w)
            return {"blocked": True, "reason": reason}

        blocking_reports = self._BLOCKING_REPORTS
        if file_tree is not None:
            blocking_reports = blocking_reports + ("architect",)

        failed_reports = [
            name for name in blocking_reports if not reports[name]["passed"]
        ]
        if failed_reports:
            detalles = [
                self._describe_failed_report(name, reports[name])
                for name in failed_reports
            ]
            return {
                "blocked": True,
                "reason": (
                    f"El Consejo no aprobó la lección en: {', '.join(detalles)}."
                ),
            }

        if unit_name in duplicate_unit_names:
            return {
                "blocked": True,
                "reason": f"Bloque de texto duplicado detectado que involucra a {unit_name}.",
            }

        return {"blocked": False, "reason": ""}

    def run_pipeline_on_file(
        self, md_filename: str, gate_decision: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        if gate_decision is None:
            gate_decision = {"blocked": False, "reason": ""}

        md_path = os.path.join(self.compiler.lecciones_dir, md_filename)
        with open(md_path, "r", encoding="utf-8") as f:
            md_text = f.read()

        # 2. Content Audit
        content_results = self.content_auditor.audit_content(md_text)

        # 3. Code Audit
        code_results = self.code_auditor.audit_code(md_text)

        # 4. Evaluation
        evaluation = self.evaluator.evaluate_notebook(code_results, content_results)

        nb_path = None
        if not gate_decision["blocked"]:
            # 1. Compile Markdown to Notebook (solo si el gate no bloquea)
            nb_path = self.compiler.compile_file(md_filename)

        return {
            "md_filename": md_filename,
            "notebook_path": nb_path,
            "content_audit": content_results,
            "code_audit": code_results,
            "evaluation": evaluation,
            "approved": evaluation["passed"] and content_results["passed"],
            "gate_blocked": gate_decision["blocked"],
            "gate_reason": gate_decision["reason"],
        }

    def generate_curriculum_map(self) -> str:
        """Genera el mapa de dependencias curriculares (Mermaid) a partir de
        las secciones '## Prerequisitos de esta unidad' de las lecciones, y
        lo guarda en notebooks_dir/curriculum_map.mmd."""
        os.makedirs(self.compiler.notebooks_dir, exist_ok=True)
        diagram = self.curriculum_map_agent.render_dag(
            Path(self.compiler.lecciones_dir)
        )
        map_path = os.path.join(self.compiler.notebooks_dir, "curriculum_map.mmd")
        with open(map_path, "w", encoding="utf-8") as f:
            f.write(diagram)
        return map_path

    def run_full_pipeline(self, enforce_gate: bool = True) -> list[dict[str, Any]]:
        results = []
        if not os.path.exists(self.compiler.lecciones_dir):
            return results

        md_filenames = sorted(
            f for f in os.listdir(self.compiler.lecciones_dir) if f.endswith(".md")
        )

        lessons_text: dict[str, str] = {}
        for fname in md_filenames:
            with open(
                os.path.join(self.compiler.lecciones_dir, fname), "r", encoding="utf-8"
            ) as f:
                lessons_text[self._unit_name_from_filename(fname)] = f.read()

        duplicate_unit_names: set = set()
        if enforce_gate:
            duplicates = self.council.editor.detect_duplicate_blocks(lessons_text)
            for dup in duplicates:
                for unit_name, _block_index in dup["locations"]:
                    duplicate_unit_names.add(unit_name)

        for fname in md_filenames:
            if enforce_gate:
                unit_name = self._unit_name_from_filename(fname)
                gate_decision = self._check_gate(
                    fname,
                    lessons_text[unit_name],
                    duplicate_unit_names,
                    file_tree=md_filenames,
                )
            else:
                gate_decision = {"blocked": False, "reason": ""}

            results.append(
                self.run_pipeline_on_file(fname, gate_decision=gate_decision)
            )

        self.generate_curriculum_map()

        return results
