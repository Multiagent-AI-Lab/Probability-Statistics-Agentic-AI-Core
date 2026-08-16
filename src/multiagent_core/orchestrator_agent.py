"""
OrchestratorAgent: Coordinates compilation, code auditing, content auditing, and evaluation pipeline.
"""

import os
from typing import Any, Dict, List, Optional

from .code_auditor_agent import CodeAuditorAgent
from .content_auditor_agent import ContentAuditorAgent
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

    @staticmethod
    def _unit_name_from_filename(md_filename: str) -> str:
        if "UNIDAD_" in md_filename:
            return f"UNIDAD {md_filename.split('_')[1]}"
        return md_filename

    def _check_gate(
        self, md_filename: str, md_text: str, duplicate_unit_names: set
    ) -> Dict[str, Any]:
        unit_name = self._unit_name_from_filename(md_filename)

        council_result = self.council.process_content(md_text, unit_name=unit_name)
        safety_result = council_result["reports"]["safety_gate"]
        if safety_result["critical"]:
            reason = "; ".join(w for w in safety_result["warnings"] if "🚨" in w)
            return {"blocked": True, "reason": reason}

        if unit_name in duplicate_unit_names:
            return {
                "blocked": True,
                "reason": f"Bloque de texto duplicado detectado que involucra a {unit_name}.",
            }

        return {"blocked": False, "reason": ""}

    def run_pipeline_on_file(
        self, md_filename: str, gate_decision: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
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

    def run_full_pipeline(self, enforce_gate: bool = True) -> List[Dict[str, Any]]:
        results = []
        if not os.path.exists(self.compiler.lecciones_dir):
            return results

        md_filenames = sorted(
            f for f in os.listdir(self.compiler.lecciones_dir) if f.endswith(".md")
        )

        lessons_text: Dict[str, str] = {}
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
                    fname, lessons_text[unit_name], duplicate_unit_names
                )
            else:
                gate_decision = {"blocked": False, "reason": ""}

            results.append(
                self.run_pipeline_on_file(fname, gate_decision=gate_decision)
            )

        return results
