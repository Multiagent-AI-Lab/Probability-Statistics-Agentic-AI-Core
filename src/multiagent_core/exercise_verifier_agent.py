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
2. **Plantilla completada**: no deben quedar sin resolver los `# TODO:`
   *literales de la plantilla original* (los comentarios `# TODO:` que el
   alumno escriba por su cuenta no cuentan: son suyos, no del ejercicio).
3. **Resultado correcto**: se ejecuta el código del alumno y se evalúan los
   `checks` (expresiones booleanas, típicamente comparaciones de tolerancia
   contra un valor de referencia fijo) sobre las variables que ese código
   define.

Aislamiento de la ejecución
---------------------------
El paso 3 corre en un **subproceso** con timeout, tempdir propio y entorno
controlado — el mismo patrón que `council/engineer_agent.py._ejecutar`, y por
las mismas razones. Una versión anterior de este agente usaba `exec()` sobre
un dict de globals sin `__builtins__`, lo que **no** aísla nada: Python
inyecta el módulo `builtins` completo cuando ese nombre falta, así que
`import os` y `open()` quedaban disponibles, y un `while True: pass` colgaba
el proceso del notebook indefinidamente porque `exec` no admite timeout.

El subproceso no promete ser un sandbox de seguridad frente a un atacante —
el alumno siempre puede correr lo que quiera en su propia máquina, con o sin
este agente. Lo que sí garantiza es lo que el uso pedagógico necesita: que
una entrega con un bucle infinito, una llamada a `sys.exit()`, o un cuelgue
de E/S termine con un mensaje de error acotado en vez de tumbar la sesión del
notebook, y que el estado del intérprete del alumno no quede contaminado por
los nombres que su solución define.
"""

import ast
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

# Segundos que se le conceden a la solución del alumno. Un ejercicio del curso
# resuelve en milisegundos; este margen cubre el arranque del intérprete y la
# importación de numpy/scipy en el subproceso.
TIMEOUT_EJECUCION_SEGUNDOS = 20

# Marcador que separa el informe JSON del agente de cualquier `print` que la
# solución del alumno haya dejado en stdout.
_MARCADOR_INFORME = "___INFORME_VERIFICACION___"

# `# TODO:` de la plantilla, para poder compararlos línea a línea contra el
# código entregado. No se usa sobre el código del alumno: un `# TODO: repasar
# esto antes del examen` suyo en una solución correcta no es un ejercicio sin
# resolver.
TODO_MARKER_PATTERN = re.compile(r"#\s*TODO:")

_ARNES = """\
import builtins as _builtins
import json
import sys

import numpy as np
from scipy import stats

_MARCADOR = {marcador!r}
_CHECKS = {checks!r}
_VARIABLES = {variables!r}

# Módulos que la solución de un ejercicio de estadística puede necesitar. El
# resto (os, sys, subprocess, shutil, socket, pathlib...) no tiene lugar en un
# ejercicio del curso, y permitirlos deja al alumno tocar el disco desde una
# celda que él cree que solo "califica" su respuesta.
_MODULOS_PERMITIDOS = {{
    "numpy", "scipy", "scipy.stats", "scipy.special", "scipy.optimize",
    "scipy.integrate", "scipy.linalg", "math", "statistics", "random",
    "itertools", "functools", "collections", "decimal", "fractions",
    "pandas", "sympy",
}}

_import_real = _builtins.__import__


def _import_restringido(nombre, globals=None, locals=None, fromlist=(), level=0):
    raiz = nombre.split(".")[0]
    if nombre in _MODULOS_PERMITIDOS or raiz in _MODULOS_PERMITIDOS:
        return _import_real(nombre, globals, locals, fromlist, level)
    raise ImportError(
        "importar '{{}}' no está permitido en la autoevaluación: este ejercicio "
        "se resuelve con numpy/scipy/math".format(nombre)
    )


# Builtins expuestos a la solución del alumno: los de cálculo y estructuras de
# datos, sin los que tocan el sistema de archivos, el proceso o el intérprete
# (`open`, `eval`, `exec`, `compile`, `input`, `exit`, `__loader__`...).
_BUILTINS_PERMITIDOS = {{
    nombre: getattr(_builtins, nombre)
    for nombre in (
        "abs", "all", "any", "bool", "callable", "chr", "complex", "dict",
        "divmod", "enumerate", "filter", "float", "format", "frozenset",
        "getattr", "hasattr", "hash", "int", "isinstance", "issubclass",
        "iter", "len", "list", "map", "max", "min", "next", "object", "ord",
        "pow", "print", "range", "repr", "reversed", "round", "set", "setattr",
        "slice", "sorted", "str", "sum", "tuple", "type", "zip",
        "True", "False", "None", "Exception", "ValueError", "TypeError",
        "KeyError", "IndexError", "ZeroDivisionError", "ArithmeticError",
        "AttributeError", "NameError", "RuntimeError", "StopIteration",
        "ImportError", "AssertionError", "NotImplementedError",
    )
    if hasattr(_builtins, nombre)
}}
_BUILTINS_PERMITIDOS["__import__"] = _import_restringido
_BUILTINS_PERMITIDOS["__build_class__"] = _builtins.__build_class__

_namespace = {{
    "stats": stats,
    "np": np,
    "__name__": "__main__",
    "__builtins__": _BUILTINS_PERMITIDOS,
}}

_informe = {{"error": None, "faltantes": [], "fallidos": [], "no_evaluables": []}}

with open({ruta_solucion!r}, encoding="utf-8") as _f:
    _fuente = _f.read()

try:
    exec(compile(_fuente, "<solucion_alumno>", "exec"), _namespace)
except BaseException as _exc:
    _informe["error"] = "{{}}: {{}}".format(type(_exc).__name__, _exc)
else:
    _informe["faltantes"] = [v for v in _VARIABLES if v not in _namespace]
    if not _informe["faltantes"]:
        for _check in _CHECKS:
            try:
                _ok = bool(eval(_check, {{"stats": stats, "np": np}}, _namespace))
            except BaseException as _exc:
                _informe["no_evaluables"].append([_check, str(_exc)])
                continue
            if not _ok:
                _informe["fallidos"].append(_check)

sys.stdout.write("\\n" + _MARCADOR + json.dumps(_informe))
sys.stdout.flush()
"""


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
        timeout: int = TIMEOUT_EJECUCION_SEGUNDOS,
    ) -> None:
        self.variables_requeridas = variables_requeridas
        self.checks = checks
        self.plantilla = plantilla
        self.timeout = timeout

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

    def _todos_de_la_plantilla(self) -> list[str]:
        """Líneas `# TODO:` literales de la plantilla original.

        Son las únicas que cuentan como ejercicio sin resolver. Un patrón
        genérico sobre el código entregado reprobaba a quien dejara su propio
        `# TODO: repasar` en una solución correcta, y encima le decía que el
        TODO era "de la plantilla".
        """
        if self.plantilla is None:
            return []
        return [
            linea.strip()
            for linea in self.plantilla.splitlines()
            if TODO_MARKER_PATTERN.search(linea)
        ]

    def _tiene_todos_sin_resolver(self, codigo: str) -> bool:
        pendientes = self._todos_de_la_plantilla()
        if not pendientes:
            return False
        entregado = {linea.strip() for linea in codigo.splitlines()}
        return any(todo in entregado for todo in pendientes)

    def _es_plantilla_sin_tocar(self, codigo: str) -> bool:
        if self.plantilla is None:
            return False
        return codigo.strip() == self.plantilla.strip()

    def _ejecutar_y_evaluar(self, codigo: str) -> dict[str, object] | str:
        """Corre la solución y sus `checks` en un subproceso con timeout.

        Devuelve el informe del arnés, o un string con el motivo por el que no
        hubo informe (timeout, proceso caído, salida ilegible).
        """
        entorno = {**os.environ, "PYTHONIOENCODING": "utf-8", "MPLBACKEND": "Agg"}

        with tempfile.TemporaryDirectory() as tmp:
            ruta_solucion = Path(tmp) / "solucion_alumno.py"
            ruta_solucion.write_text(codigo, encoding="utf-8")

            arnes = _ARNES.format(
                marcador=_MARCADOR_INFORME,
                checks=self.checks,
                variables=self.variables_requeridas,
                ruta_solucion=str(ruta_solucion),
            )
            ruta_arnes = Path(tmp) / "arnes_verificacion.py"
            ruta_arnes.write_text(arnes, encoding="utf-8")

            try:
                proceso = subprocess.run(
                    [sys.executable, str(ruta_arnes)],
                    capture_output=True,
                    text=True,
                    check=False,  # un exit != 0 es un hallazgo, no una excepción
                    timeout=self.timeout,
                    cwd=tmp,
                    encoding="utf-8",
                    errors="replace",
                    env=entorno,
                )
            except subprocess.TimeoutExpired:
                return (
                    f"El código no terminó en {self.timeout}s (timeout). "
                    "¿Hay un bucle que nunca corta o una espera bloqueante?"
                )
            except OSError as exc:
                return f"No se pudo ejecutar el código: {exc}"

        salida = proceso.stdout or ""
        _, marcador, informe_json = salida.partition(_MARCADOR_INFORME)
        if not marcador:
            detalle = (proceso.stderr or "").strip()[-300:] or "sin salida"
            return f"El código terminó de forma anómala: {detalle}"

        try:
            informe = json.loads(informe_json.strip())
        except json.JSONDecodeError:
            return "No se pudo leer el informe de verificación."
        return informe

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

        informe = self._ejecutar_y_evaluar(codigo)
        if isinstance(informe, str):
            return ResultadoVerificacion(aprueba=False, issues=[informe])

        if informe["error"]:
            return ResultadoVerificacion(
                aprueba=False,
                issues=[f"El código no ejecuta: {informe['error']}"],
            )

        faltantes = informe["faltantes"]
        if faltantes:
            return ResultadoVerificacion(
                aprueba=False,
                issues=[
                    "No se definieron las variables requeridas: " + ", ".join(faltantes)
                ],
            )

        for check, motivo in informe["no_evaluables"]:
            issues.append(f"No se pudo evaluar '{check}': {motivo}")
        for check in informe["fallidos"]:
            issues.append(f"No se cumple: {check}")

        return ResultadoVerificacion(aprueba=len(issues) == 0, issues=issues)


def reportar_resultado_ejercicio(
    resultado: dict[str, object],
    resultado_ejercicio: ResultadoVerificacion,
    nombre_ejercicio: str,
    unidad: str,
    debugger: object,
) -> None:
    """Imprime el veredicto de una celda de Autoevaluación.

    Único punto de mantenimiento del bloque que antes se repetía, idéntico
    salvo `nombre_ejercicio`/`unidad`, en las 32 celdas de Autoevaluación de
    las 8 unidades (`CodeAuditorAgent` + `ExerciseVerifierAgent` +
    `SocraticDebugger`). No importa `SocraticDebugger` directamente porque
    vive en `external_skills/pedagogy/` -- un paquete de dominio pedagógico
    separado de `src/multiagent_core/` -- así que la celda se lo pasa ya
    instanciado; `debugger` solo necesita exponer
    `generate_socratic_question(error_type, context)`.

    Reproduce EXACTAMENTE el output del bloque original: mismo texto, mismo
    orden, mismos emojis, para que el refactor sea puro (sin cambio de
    comportamiento observable por el alumno).
    """
    hay_hallazgos = (
        resultado["issues"]
        or resultado["metrics"]["has_security_risk"]
        or not resultado_ejercicio.aprueba
    )
    if not hay_hallazgos:
        print(
            "✅ Tu código pasa las verificaciones automáticas de estilo, seguridad y resultado."
        )
        print(resultado)
        print(resultado_ejercicio)
        return

    for issue in resultado["issues"]:
        tipo_error = "syntax_error" if "SyntaxError" in issue else "generic"
        print("💡", debugger.generate_socratic_question(tipo_error, unidad))
    for issue in resultado["security_issues"]:
        print("🔒", debugger.generate_socratic_question("security_risk", unidad))
        print("   ", issue)
    for issue in resultado_ejercicio.issues:
        print("❌", debugger.generate_socratic_question("generic", unidad))
        print("   ", issue)
    print(f"\n--- Detalle técnico ({nombre_ejercicio}) ---")
    print(resultado)
    print(resultado_ejercicio)
