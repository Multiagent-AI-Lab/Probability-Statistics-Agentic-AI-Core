"""
CodeAuditorAgent: Audits Python code for statistical correctness, PEP8, display(Math()) usage, best practices, and basic security risks.
"""

import ast
import re
from typing import Any

# Librería (subcadena buscada en el nombre del módulo importado) -> clave de
# `metrics` que se marca cuando aparece.
_LIBRERIAS_RASTREADAS = {
    "scipy": "uses_scipy",
    "statsmodels": "uses_statsmodels",
    "sympy": "uses_sympy",
}

# Marcas que delatan LaTeX crudo dentro de un `print()`.
_MARCAS_LATEX = (r"\frac", r"\mu", r"\sigma")


class CodeAuditorAgent:
    """Agent that audits Python statistical code blocks."""

    def __init__(self):
        self.required_imports = ["scipy", "numpy", "pandas", "matplotlib", "seaborn"]
        self._credential_pattern = re.compile(
            r"\b(api_key|token|password|secret|passwd)\s*=\s*['\"][^'\"]{8,}['\"]",
            re.IGNORECASE,
        )

    def extract_python_code_blocks(self, markdown_or_code: str) -> list[str]:
        if "```" not in markdown_or_code:
            return [markdown_or_code]

        pattern = r"```python\s*\n(.*?)\n```"
        return re.findall(pattern, markdown_or_code, re.DOTALL)

    def clean_ipython_magics(self, code_str: str) -> str:
        clean_lines = []
        for line in code_str.split("\n"):
            stripped = line.strip()
            if stripped.startswith(("!", "%")):
                continue
            clean_lines.append(line)
        return "\n".join(clean_lines)

    def _check_security(self, code_str: str, tree: ast.AST) -> list[str]:
        issues = []
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id in ("eval", "exec")
            ):
                issues.append(
                    f"Uso de '{node.func.id}()' detectado (Riesgo OWASP LLM-02, línea {node.lineno})."
                )

        for match in self._credential_pattern.finditer(code_str):
            if "os.environ" not in code_str[max(0, match.start() - 30) : match.end()]:
                issues.append(
                    f"Posible credencial expuesta en texto plano: '{match.group(1)}'."
                )

        return issues

    @staticmethod
    def _empty_metrics() -> dict[str, bool]:
        return {
            "uses_scipy": False,
            "uses_statsmodels": False,
            "uses_sympy": False,
            "uses_display_math": False,
            "uses_raw_print_latex": False,
            "has_security_risk": False,
        }

    @staticmethod
    def _record_library_usage(module_name: str, metrics: dict[str, bool]) -> None:
        """Marca en `metrics` las librerías estadísticas presentes en un import."""
        for libreria, clave in _LIBRERIAS_RASTREADAS.items():
            if libreria in module_name:
                metrics[clave] = True

    @staticmethod
    def _called_func_name(node: ast.Call) -> str:
        """Nombre de la función invocada: `f()` -> "f", `obj.f()` -> "f"."""
        if isinstance(node.func, ast.Name):
            return node.func.id
        if isinstance(node.func, ast.Attribute):
            return node.func.attr
        return ""

    @staticmethod
    def _args_con_latex_crudo(node: ast.Call) -> int:
        """Cuenta los literales de un `print()` que contienen LaTeX crudo."""
        return sum(
            1
            for arg in node.args
            if isinstance(arg, ast.Constant)
            and isinstance(arg.value, str)
            and any(marca in arg.value for marca in _MARCAS_LATEX)
        )

    def _check_imports(self, node: ast.AST, metrics: dict[str, bool]) -> None:
        """Registra el uso de scipy/statsmodels/sympy en un nodo de import."""
        if isinstance(node, ast.Import):
            for alias in node.names:
                self._record_library_usage(alias.name, metrics)
            return

        if isinstance(node, ast.ImportFrom) and node.module:
            self._record_library_usage(node.module, metrics)

    def _check_display_usage(
        self, node: ast.AST, metrics: dict[str, bool], warnings: list[str]
    ) -> None:
        """Distingue `display(Math(...))` de un `print()` con LaTeX crudo."""
        if not isinstance(node, ast.Call):
            return

        func_name = self._called_func_name(node)
        if func_name == "display":
            metrics["uses_display_math"] = True
            return

        if func_name != "print":
            return

        # Una advertencia por argumento con LaTeX crudo (no una por llamada):
        # se conserva el conteo del comportamiento original.
        for _ in range(self._args_con_latex_crudo(node)):
            metrics["uses_raw_print_latex"] = True
            warnings.append(
                "Avoid print() for LaTeX equations; use display(Math()) instead."
            )

    def _audit_block(
        self,
        cleaned: str,
        metrics: dict[str, bool],
        warnings: list[str],
        security_issues: list[str],
    ) -> bool:
        """Audita un bloque ya limpio de magics. Devuelve True si parseó bien.

        Acumula sus hallazgos en `metrics`, `warnings` y `security_issues`.
        """
        tree = ast.parse(cleaned)
        security_issues.extend(self._check_security(cleaned, tree))

        for node in ast.walk(tree):
            self._check_imports(node, metrics)
            self._check_display_usage(node, metrics, warnings)

        return True

    def audit_code(self, code_str: str) -> dict[str, Any]:
        blocks = self.extract_python_code_blocks(code_str)
        metrics = self._empty_metrics()

        if not blocks:
            return {
                "passed": True,
                "score": 100.0,
                "issues": [],
                "warnings": ["No Python code blocks found to audit."],
                "security_issues": [],
                "metrics": metrics,
            }

        issues: list[str] = []
        warnings: list[str] = []
        security_issues: list[str] = []
        valid_blocks = 0

        for block in blocks:
            cleaned = self.clean_ipython_magics(block)
            if not cleaned.strip():
                continue

            try:
                valid_blocks += self._audit_block(
                    cleaned, metrics, warnings, security_issues
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
