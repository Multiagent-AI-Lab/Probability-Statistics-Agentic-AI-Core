"""
ExerciseVerifierAgent: verifica el RESULTADO real de la solución de un alumno a
un ejercicio de la Autoevaluación, no solo su estilo/seguridad.

`CodeAuditorAgent.audit_code` (ver `code_auditor_agent.py`) solo mide PEP8,
buenas prácticas de visualización y riesgos OWASP: un archivo vacío, un
`pass`, o una respuesta numéricamente imposible (p. ej. una probabilidad > 1)
pasan esa auditoría sin problema porque nunca ejecuta el código ni compara sus
valores contra una referencia.

Este agente cierra esa brecha (hallazgo H-06) con tres verificaciones, en
orden, cortando en la primera que falla:

1. **No trivial**: el código no puede estar vacío, ser solo comentarios, o
   reducirse a un cuerpo `pass`.
2. **Plantilla completada**: no deben quedar marcadores `# TODO:` de la
   plantilla original sin resolver.
3. **Resultado correcto**: se ejecuta el código del alumno en un namespace
   aislado y se evalúan `checks` (expresiones booleanas, típicamente
   `assert`s de tolerancia contra un valor de referencia de SciPy) sobre las
   variables que dicho namespace define.

El código ejecutado es siempre la solución que el propio alumno escribió para
un ejercicio del curso (nunca input de un tercero no confiable ni datos de
producción): el `exec` corre en un namespace nuevo y aislado por invocación,
sin acceso a builtins peligrosos más allá de los que scipy/numpy ya requieren
para este uso pedagógico local.
"""

import ast
import re
from dataclasses import dataclass, field

import numpy as np
from scipy import stats

TODO_MARKER_PATTERN = re.compile(r"#\s*TODO:")


@dataclass(frozen=True)
class ResultadoVerificacion:
    """Resultado de `ExerciseVerifierAgent.verificar`."""

    aprueba: bool
    issues: list[str] = field(default_factory=list)


class ExerciseVerifierAgent:
    """Verifica que la solución de un ejercicio produce el resultado esperado."""

    def __init__(
        self,
        variables_requeridas: list[str],
        checks: list[str],
        plantilla: str | None = None,
    ) -> None:
        self.variables_requeridas = variables_requeridas
        self.checks = checks
        self.plantilla = plantilla

    def _es_trivial(self, codigo: str) -> bool:
        """Detecta archivo vacío, solo comentarios, o cuerpo reducido a `pass`."""
        codigo_sin_comentarios = "\n".join(
            line
            for line in codigo.splitlines()
            if line.strip() and not line.strip().startswith("#")
        ).strip()

        if not codigo_sin_comentarios:
            return True

        try:
            tree = ast.parse(codigo_sin_comentarios)
        except SyntaxError:
            return False

        cuerpo_no_trivial = [
            node for node in tree.body if not isinstance(node, (ast.Pass, ast.Expr))
        ]
        return len(cuerpo_no_trivial) == 0

    def _tiene_todos_sin_resolver(self, codigo: str) -> bool:
        return bool(TODO_MARKER_PATTERN.search(codigo))

    def _es_plantilla_sin_tocar(self, codigo: str) -> bool:
        if self.plantilla is None:
            return False
        return codigo.strip() == self.plantilla.strip()

    def verificar(self, codigo: str) -> ResultadoVerificacion:
        issues: list[str] = []

        if self._es_trivial(codigo):
            return ResultadoVerificacion(
                aprueba=False,
                issues=["El archivo está vacío, es solo comentarios, o es un `pass`."],
            )

        if self._es_plantilla_sin_tocar(codigo):
            return ResultadoVerificacion(
                aprueba=False,
                issues=["La plantilla no fue modificada: sigue siendo la entregada."],
            )

        if self._tiene_todos_sin_resolver(codigo):
            return ResultadoVerificacion(
                aprueba=False,
                issues=["Quedan marcadores '# TODO:' de la plantilla sin resolver."],
            )

        namespace: dict[str, object] = {"stats": stats, "np": np}
        try:
            exec(compile(codigo, "<solucion_alumno>", "exec"), namespace)  # noqa: S102
        except Exception as exc:  # noqa: BLE001 - se reporta como issue, no se relanza
            return ResultadoVerificacion(
                aprueba=False,
                issues=[f"El código no ejecuta: {type(exc).__name__}: {exc}"],
            )

        faltantes = [v for v in self.variables_requeridas if v not in namespace]
        if faltantes:
            issues.append(
                "No se definieron las variables requeridas: " + ", ".join(faltantes)
            )
            return ResultadoVerificacion(aprueba=False, issues=issues)

        for check in self.checks:
            try:
                ok = bool(eval(check, {"stats": stats, "np": np}, namespace))
            except Exception as exc:  # noqa: BLE001 - se reporta como issue
                issues.append(f"No se pudo evaluar '{check}': {exc}")
                continue
            if not ok:
                issues.append(f"No se cumple: {check}")

        return ResultadoVerificacion(aprueba=len(issues) == 0, issues=issues)
