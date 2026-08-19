"""
CodeAuditorAgent: Audits Python code for statistical correctness, PEP8, display(Math()) usage, best practices, and basic security risks.
"""

import ast
import re
from typing import Any, Dict, List


class CodeAuditorAgent:
    """Agent that audits Python statistical code blocks."""

    def __init__(self):
        self.required_imports = ["scipy", "numpy", "pandas", "matplotlib", "seaborn"]
        self._credential_pattern = re.compile(
            r"\b(api_key|token|password|secret|passwd)\s*=\s*['\"][^'\"]{8,}['\"]",
            re.IGNORECASE,
        )

    def extract_python_code_blocks(self, markdown_or_code: str) -> List[str]:
        if "```" not in markdown_or_code:
            return [markdown_or_code]

        pattern = r"```python\s*\n(.*?)\n```"
        return re.findall(pattern, markdown_or_code, re.DOTALL)

    def clean_ipython_magics(self, code_str: str) -> str:
        clean_lines = []
        for line in code_str.split("\n"):
            stripped = line.strip()
            if stripped.startswith("!") or stripped.startswith("%"):
                continue
            clean_lines.append(line)
        return "\n".join(clean_lines)

    def _check_security(self, code_str: str, tree: ast.AST) -> List[str]:
        issues = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in ("eval", "exec"):
                    issues.append(
                        f"Uso de '{node.func.id}()' detectado (Riesgo OWASP LLM-02, línea {node.lineno})."
                    )

        for match in self._credential_pattern.finditer(code_str):
            if "os.environ" not in code_str[max(0, match.start() - 30) : match.end()]:
                issues.append(
                    f"Posible credencial expuesta en texto plano: '{match.group(1)}'."
                )

        return issues

    def audit_code(self, code_str: str) -> Dict[str, Any]:
        blocks = self.extract_python_code_blocks(code_str)

        issues = []
        warnings = []
        security_issues: List[str] = []
        metrics = {
            "uses_scipy": False,
            "uses_statsmodels": False,
            "uses_sympy": False,
            "uses_display_math": False,
            "uses_raw_print_latex": False,
            "has_security_risk": False,
        }

        if not blocks:
            return {
                "passed": True,
                "score": 100.0,
                "issues": [],
                "warnings": ["No Python code blocks found to audit."],
                "security_issues": [],
                "metrics": metrics,
            }

        valid_blocks = 0
        for block in blocks:
            cleaned = self.clean_ipython_magics(block)
            if not cleaned.strip():
                continue

            try:
                tree = ast.parse(cleaned)
                valid_blocks += 1
                security_issues.extend(self._check_security(cleaned, tree))
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            if "scipy" in alias.name:
                                metrics["uses_scipy"] = True
                            if "statsmodels" in alias.name:
                                metrics["uses_statsmodels"] = True
                            if "sympy" in alias.name:
                                metrics["uses_sympy"] = True
                    elif isinstance(node, ast.ImportFrom):
                        if node.module:
                            if "scipy" in node.module:
                                metrics["uses_scipy"] = True
                            if "statsmodels" in node.module:
                                metrics["uses_statsmodels"] = True
                            if "sympy" in node.module:
                                metrics["uses_sympy"] = True

                    if isinstance(node, ast.Call):
                        func_name = ""
                        if isinstance(node.func, ast.Name):
                            func_name = node.func.id
                        elif isinstance(node.func, ast.Attribute):
                            func_name = node.func.attr

                        if func_name == "display":
                            metrics["uses_display_math"] = True
                        elif func_name == "print":
                            for arg in node.args:
                                if isinstance(arg, ast.Constant) and isinstance(
                                    arg.value, str
                                ):
                                    if (
                                        r"\frac" in arg.value
                                        or r"\mu" in arg.value
                                        or r"\sigma" in arg.value
                                    ):
                                        metrics["uses_raw_print_latex"] = True
                                        warnings.append(
                                            "Avoid print() for LaTeX equations; use display(Math()) instead."
                                        )
            except SyntaxError as e:
                issues.append(f"SyntaxError in code block: {e.msg} at line {e.lineno}")

        metrics["has_security_risk"] = len(security_issues) > 0
        passed = (len(issues) == 0 or valid_blocks > 0) and not metrics[
            "has_security_risk"
        ]
        score = 100.0 if len(issues) == 0 else 90.0 if valid_blocks > 0 else 0.0

        return {
            "passed": passed,
            "score": score,
            "issues": issues,
            "warnings": warnings,
            "security_issues": security_issues,
            "metrics": metrics,
        }
