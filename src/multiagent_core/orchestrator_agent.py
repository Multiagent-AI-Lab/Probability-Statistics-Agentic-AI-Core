"""
OrchestratorAgent: Coordinates compilation, code auditing, content auditing, and evaluation pipeline.
"""

from typing import Dict, Any, List
from .code_auditor_agent import CodeAuditorAgent
from .content_auditor_agent import ContentAuditorAgent
from .evaluator_agent import EvaluatorAgent
from .notebook_compiler_agent import NotebookCompilerAgent


class OrchestratorAgent:
    """Orchestrator for the multiagent auditing and compilation pipeline."""

    def __init__(self, lecciones_dir: str = "lecciones", notebooks_dir: str = "notebooks"):
        self.compiler = NotebookCompilerAgent(lecciones_dir=lecciones_dir, notebooks_dir=notebooks_dir)
        self.code_auditor = CodeAuditorAgent()
        self.content_auditor = ContentAuditorAgent()
        self.evaluator = EvaluatorAgent()

    def run_pipeline_on_file(self, md_filename: str) -> Dict[str, Any]:
        # 1. Compile Markdown to Notebook
        nb_path = self.compiler.compile_file(md_filename)
        
        # Read compiled markdown text
        with open(self.compiler.lecciones_dir + "/" + md_filename, "r", encoding="utf-8") as f:
            md_text = f.read()

        # 2. Content Audit
        content_results = self.content_auditor.audit_content(md_text)

        # 3. Code Audit
        code_results = self.code_auditor.audit_code(md_text)

        # 4. Evaluation
        evaluation = self.evaluator.evaluate_notebook(code_results, content_results)

        return {
            "notebook_path": nb_path,
            "content_audit": content_results,
            "code_audit": code_results,
            "evaluation": evaluation,
            "approved": evaluation["passed"] and content_results["passed"]
        }

    def run_full_pipeline(self) -> List[Dict[str, Any]]:
        results = []
        import os
        if not os.path.exists(self.compiler.lecciones_dir):
            return results

        for fname in os.listdir(self.compiler.lecciones_dir):
            if fname.endswith(".md"):
                results.append(self.run_pipeline_on_file(fname))

        return results
