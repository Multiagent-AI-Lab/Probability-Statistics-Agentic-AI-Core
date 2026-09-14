"""
EngineerAgent (@Engineer): Code builder using SciPy, Statsmodels, Pandas, SymPy, NumPy.
"""

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

from ..curriculum_map_agent import extract_fenced_blocks
from ._contraste_boxed import (
    _NUMERO,
    _algun_valor_coincide,
    _contrastar_contra_la_unidad,
    _el_codigo_apunta_al_valor,
    _es_formula_simbolica,
    _limpiar_latex,
)

# Una sección arranca en un encabezado Markdown: es la unidad de contraste
# entre un bloque de código y el `\boxed{}` que ese bloque debería producir.
_ENCABEZADO = re.compile(r"^#{1,6}\s+.*$", re.MULTILINE)

# `\boxed{...}` con un nivel de anidamiento de llaves (p. ej.
# `\boxed{15.65\ \text{nm}}` o `\boxed{\frac{2}{3}}`).
_BOXED = re.compile(r"\\boxed\{((?:[^{}]|\{[^{}]*\})*)\}")

# Bloques que la auditoría no ejecuta: dependen del runtime de notebook, de
# la red, del propio repo, o son plantillas para el alumno. Omitirlos no es
# una falla del contenido -- es el límite declarado de esta verificación.
_MARCADORES_NO_EJECUTABLES = (
    "ipytest",
    "get_ipython",
    "input(",
    "requests.",
    "urllib",
    "from src.",
    "import src.",
    "external_skills",
    "StatsTutorAgent",
    "CodeAuditorAgent",
    "%%",
    "TODO",
    "...",
)

# Sintaxis de notebook que no es Python válido y hace fallar la compilación
# del archivo entero (no solo esa línea): escapes a shell (`!git clone`) y
# magics de línea (`%pip install`, `%matplotlib inline`). Un solo bloque con
# esto abortaba la unidad completa con SyntaxError y dejaba la verificación
# en silencio, aprobando todo por falta de salida.
# Se detectan por patrón y no por subcadena para no confundirlos con un
# `!=` o un operador módulo dentro de una expresión.
_ESCAPE_DE_SHELL = re.compile(r"^\s*[!%]\s*\w", re.MULTILINE)

# Prefijo que separa la salida de cada sección dentro del stdout único de
# la unidad. Improbable de aparecer en el texto impreso por una lección.
_MARCADOR_SECCION = "___SECCION_AUDITADA_"

_TIMEOUT_EJECUCION_SEGUNDOS = 300

# Preámbulo que hace ejecutable en batch un bloque escrito para notebook:
# backend sin ventana para matplotlib y `display`/`Math` como no-ops que
# dejan su texto en stdout (ahí viven varios `\boxed{}` generados por f-string).
_PREAMBULO = """\
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot
matplotlib.pyplot.show = lambda *a, **k: None

class Math:
    def __init__(self, s="", *a, **k):
        self.s = s
    def __str__(self):
        return str(self.s)
    __repr__ = __str__

class Latex(Math):
    pass

def display(*args, **kwargs):
    for _a in args:
        print(_a)

# Las lecciones muestran resultados con `display(Math(fr"... \\boxed{{{v}}}"))`.
# IPython está instalado en el entorno, así que esas clases son las reales y
# su repr es "<IPython.core.display.Math object>": el número quedaría fuera
# de stdout y toda la fase de verificación simbólica (GOVERNANCE §2, Fase 2)
# sería invisible para la auditoría.
#
# Se parchean SOLO `display`, `Math` y `Latex` dentro del módulo real, en vez
# de reemplazar el paquete entero: matplotlib importa IPython para instalar
# su displayhook y consulta varios de sus atributos, así que un módulo falso
# rompe la importación de pyplot.
try:
    import IPython.display as _ipd

    _ipd.display = display
    _ipd.Math = Math
    _ipd.Latex = Latex
except ImportError:
    import sys as _sys
    import types as _types

    _mod = _types.ModuleType("IPython.display")
    _mod.display = display
    _mod.Math = Math
    _mod.Latex = Latex
    _sys.modules["IPython.display"] = _mod

import builtins as _b
_b.display = display
_b.Math = Math
"""


class EngineerAgent:
    """Agent responsible for checking code quality, type hints, SciPy/Statsmodels usage, and Monte Carlo convergence."""

    # No incluye "samples" (inglés): en las lecciones ese nombre se usa para
    # tamaño de dataset (p. ej. n_samples = 45 filas de un ejemplo de RANSAC),
    # no para conteo de iteraciones/muestras de una simulación Monte Carlo.
    # El patrón de simulación real del curso usa "muestras" (español) o
    # "sim"/"iter" explícitos — ver UNIDAD_6_MODELADO_SIMULACION.md.
    _SAMPLE_COUNT_PATTERN = re.compile(
        r"\b(?:N|n)_?(?:sim|muestras|iter|iteraciones)\s*=\s*(\d[\d_]*)",
        re.IGNORECASE,
    )

    def check_code_implementation(self, code_text: str) -> dict[str, Any]:
        """Ejecuta el código de cada sección y contrasta su salida contra los
        `\\boxed{}` de esa misma sección.

        Esta es la verificación que `GOVERNANCE.md §2` promete (el camino
        simbólico y el numérico deben coincidir) y que hasta H-01 ningún
        agente implementaba: el criterio anterior era
        `passed = "scipy" in code_text`, que aprueba cualquier texto que
        mencione la palabra sin ejecutar una sola línea.

        Un `\\boxed{}` sin valor numérico (una fórmula simbólica como
        `X = F^{-1}(U)`) o una sección cuyo código no es ejecutable en batch
        no producen discrepancia: no hay nada que contrastar y esta
        auditoría no inventa hallazgos que no puede sostener.
        """
        discrepancias: list[dict[str, Any]] = []
        errores: list[dict[str, str]] = []

        # Los bloques de una unidad se escriben como celdas de notebook: la
        # sección 6.1 usa el `plt` y los datos que definió la sección 1. Por
        # eso la unidad se ejecuta entera y en orden, una sola vez, como un
        # "Run All" -- y no sección por sección, que daría NameError sobre
        # contenido correcto (y, re-ejecutando el prefijo cada vez, costaría
        # tiempo cuadrático en el número de secciones).
        secciones = self._dividir_en_secciones(code_text)
        plan: list[tuple[str, list[str], list[float]]] = []
        for titulo, cuerpo in secciones:
            ejecutables = [
                codigo
                for _, lang, codigo in extract_fenced_blocks(cuerpo)
                if lang.lower() in ("python", "py") and self._es_ejecutable(codigo)
            ]
            plan.append((titulo, ejecutables, self._extraer_valores_boxed(cuerpo)))

        # Basta con que la unidad tenga algún `\boxed{}` y algún bloque
        # ejecutable, aunque no coincidan en la misma sección: el patrón
        # habitual es justamente derivar a mano en una sección teórica y
        # comprobarlo con el código de otra.
        hay_algo_que_verificar = any(esperados for _, _, esperados in plan) and any(
            ejec for _, ejec, _ in plan
        )
        if hay_algo_que_verificar:
            salida_por_seccion, error, seccion_que_fallo = self._ejecutar_unidad(plan)
            if error is not None and not salida_por_seccion:
                # El proceso murió antes de imprimir nada (p. ej. SyntaxError
                # al compilar: basta una línea de sintaxis de notebook para
                # tumbar el archivo entero). Sin esta rama la unidad quedaría
                # sin salida y aprobaría por vacuidad — el mismo silencio que
                # H-01 denuncia.
                errores.append({"seccion": "(unidad completa)", "error": error})
        else:
            salida_por_seccion, error, seccion_que_fallo = {}, None, None

        # Salida de toda la unidad: un `\boxed{}` derivado a mano en una
        # sección teórica (UNIDAD 1 §2.2 calcula la media a mano) se verifica
        # con el código de la sección computacional (§4). Restringir el
        # contraste a la propia sección dejaría sin verificar justo los
        # ejemplos analíticos, que son los que más fácil se desincronizan.
        salida_de_la_unidad = "\n".join(salida_por_seccion.values())

        for titulo, ejecutables, esperados in plan:
            if not esperados:
                continue
            if not ejecutables:
                _contrastar_contra_la_unidad(
                    titulo, esperados, salida_de_la_unidad, discrepancias
                )
                continue
            # La ejecución aborta en la sección que lanzó la excepción; las
            # posteriores nunca llegaron a correr, así que no se contrastan.
            if error is not None and titulo == seccion_que_fallo:
                errores.append({"seccion": titulo, "error": error})
                continue
            if titulo not in salida_por_seccion:
                if error is not None:
                    continue
                errores.append({"seccion": titulo, "error": "sin salida capturada"})
                continue

            salida = salida_por_seccion.get(titulo, "")
            producidos = self._extraer_numeros(salida)
            if not producidos:
                # El código de la sección es simbólico (SymPy) o solo grafica:
                # no emite un número que contrastar.
                continue

            for valor_esperado, expresion in esperados:
                # N-03: relajado de "un solo boxed Y un solo número
                # producido" a solo "un solo boxed no simbólico en la
                # sección" -- antes, una sección con >=2 números
                # producidos (ruido, pasos intermedios) nunca activaba
                # esta rama, y el boxed fabricado caía en
                # _el_codigo_apunta_al_valor, que lo descartaba sin
                # reportar si su rótulo no aparecía en el stdout.
                # Verificado sin falsos positivos en las 8 unidades
                # reales (UNIDAD 7 §6.2 es el caso que exige excluir
                # fórmulas simbólicas -- ver _es_formula_simbolica).
                emparejamiento_inequivoco = len(
                    esperados
                ) == 1 and not _es_formula_simbolica(expresion)

                # Basta con que el valor aparezca en la salida de la sección:
                # el código lo produjo, aunque el rótulo no sea idéntico.
                if _algun_valor_coincide(valor_esperado, producidos):
                    continue
                if emparejamiento_inequivoco:
                    discrepancias.append(
                        {
                            "seccion": titulo,
                            "valor_declarado": valor_esperado,
                            "valores_producidos": producidos,
                        }
                    )
                    continue
                if not _el_codigo_apunta_al_valor(
                    expresion,
                    salida,
                    valor_esperado,
                    seccion_tiene_un_solo_boxed=len(esperados) == 1,
                ):
                    # El `\boxed{}` proviene de un ejemplo analítico distinto
                    # del que ejecuta el código de la sección (patrón real de
                    # las lecciones: se deriva a mano un caso y se computa
                    # otro). Sin evidencia de que el código pretenda producir
                    # este valor, reportarlo sería un falso positivo.
                    continue
                discrepancias.append(
                    {
                        "seccion": titulo,
                        "valor_declarado": valor_esperado,
                        "valores_producidos": producidos[:10],
                    }
                )

        return {
            "has_scipy_or_statsmodels": "scipy" in code_text
            or "statsmodels" in code_text,
            "has_display_math": "display" in code_text and "Math" in code_text,
            "discrepancias": discrepancias,
            "errores_de_ejecucion": errores,
            "passed": not discrepancias and not errores,
        }

    def _dividir_en_secciones(self, text: str) -> list[tuple[str, str]]:
        """Parte el documento por encabezados Markdown. El contraste es
        por sección para no comparar un `\\boxed{}` contra el código de un
        ejemplo distinto que aparece más abajo en la unidad.

        Solo cuentan los encabezados fuera de bloques de código: las
        lecciones comentan su Python con `## Filtrado del outlier ...`, que
        es un comentario, no una sección. Tomarlo por encabezado partía los
        bloques a la mitad y hacía fallar código correcto por NameError.
        """
        encabezados = [
            m
            for m in _ENCABEZADO.finditer(text)
            if not self._dentro_de_bloque_de_codigo(text, m.start())
        ]
        if not encabezados:
            return [("(documento)", text)]

        secciones: list[tuple[str, str]] = []
        if encabezados[0].start() > 0:
            secciones.append(("(preámbulo)", text[: encabezados[0].start()]))

        for i, match in enumerate(encabezados):
            fin = encabezados[i + 1].start() if i + 1 < len(encabezados) else len(text)
            secciones.append((match.group(0).strip(), text[match.start() : fin]))
        return secciones

    @staticmethod
    def _dentro_de_bloque_de_codigo(text: str, posicion: int) -> bool:
        """Un número impar de fences ``` antes de `posicion` significa que
        esa posición cae dentro de un bloque de código abierto."""
        return text.count("```", 0, posicion) % 2 == 1

    def _extraer_valores_boxed(self, text: str) -> list[tuple[float, str]]:
        """Valor numérico final de cada `\\boxed{}` de la sección, junto con
        la expresión completa que lo encuadra.

        Se toma el último número de la expresión porque el patrón del curso
        es `\\boxed{P(X=2) = 190 \\times 0.0025 \\approx 0.18868}`: el
        resultado es el último, no el primer operando. La expresión se
        conserva porque su lado izquierdo nombra la cantidad, y ese nombre
        es lo que permite saber si el código apunta a este valor.
        """
        valores: list[tuple[float, str]] = []
        for match in _BOXED.finditer(text):
            contenido = match.group(1)
            numeros = _NUMERO.findall(_limpiar_latex(contenido))
            if not numeros:
                continue
            # El nombre de la cantidad suele estar fuera de la caja:
            # `$$\alpha = P(...) \approx \boxed{0.2466}$$` encuadra solo el
            # resultado. Se toma la línea completa para no perderlo.
            inicio_linea = text.rfind("\n", 0, match.start()) + 1
            expresion = text[inicio_linea : match.end()]
            valores.append((float(numeros[-1]), expresion))
        return valores

    def _es_ejecutable(self, codigo: str) -> bool:
        if _ESCAPE_DE_SHELL.search(codigo):
            return False
        return not any(m in codigo for m in _MARCADORES_NO_EJECUTABLES)

    def _ejecutar_unidad(
        self, plan: list[tuple[str, list[str], list[float]]]
    ) -> tuple[dict[str, str], str | None, str | None]:
        """Ejecuta la unidad completa en un solo proceso y reparte su stdout
        por sección.

        Cada sección se precede de un marcador impreso, de modo que la
        salida quede atribuida a quien la produjo: si el número impreso por
        un ejemplo anterior contara como salida de esta sección, podría
        "satisfacer" su `\\boxed{}` y ocultar justo la discrepancia que se
        busca detectar.
        """
        partes: list[str] = []
        for indice, (_, ejecutables, _) in enumerate(plan):
            if not ejecutables:
                continue
            partes.append(f'print("{_MARCADOR_SECCION}{indice}")')
            partes.extend(ejecutables)

        salida, error = self._ejecutar("\n".join(partes))

        por_seccion: dict[str, str] = {}
        ultima_seccion: str | None = None
        for fragmento in salida.split(_MARCADOR_SECCION)[1:]:
            cabecera, _, cuerpo = fragmento.partition("\n")
            try:
                indice = int(cabecera.strip())
            except ValueError:
                continue
            if 0 <= indice < len(plan):
                ultima_seccion = plan[indice][0]
                por_seccion[ultima_seccion] = cuerpo

        # Si la unidad abortó, la excepción ocurrió en la última sección que
        # alcanzó a imprimir su marcador: su salida está truncada y no puede
        # usarse para contrastar valores.
        if error is not None and ultima_seccion is not None:
            por_seccion.pop(ultima_seccion, None)
            return por_seccion, error, ultima_seccion

        return por_seccion, error, None

    def _ejecutar(self, codigo: str) -> tuple[str, str | None]:
        """Corre el bloque en un subproceso aislado.

        Subproceso y no `exec()`: el código de una lección importa
        matplotlib, fija semillas y define nombres globales; ejecutarlo en
        el proceso de la auditoría contaminaría el estado del intérprete
        y un `sys.exit()` o un bucle infinito la tumbarían. El timeout
        acota lo segundo.
        """
        # Las lecciones imprimen notación matemática Unicode (∩, σ, μ). En
        # Windows el stdout de un subproceso usa cp1252 por defecto y esos
        # caracteres lo hacen abortar con UnicodeEncodeError -- un fallo del
        # arnés de auditoría que se reportaría como si fuera un bug del
        # contenido. PYTHONIOENCODING lo evita.
        entorno = {**os.environ, "PYTHONIOENCODING": "utf-8", "MPLBACKEND": "Agg"}

        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "bloque_de_leccion.py"
            script.write_text(_PREAMBULO + "\n" + codigo, encoding="utf-8")
            try:
                proceso = subprocess.run(
                    [sys.executable, str(script)],
                    capture_output=True,
                    text=True,
                    check=False,  # un exit != 0 es un hallazgo, no una excepción
                    timeout=_TIMEOUT_EJECUCION_SEGUNDOS,
                    cwd=tmp,
                    encoding="utf-8",
                    errors="replace",
                    env=entorno,
                )
            except subprocess.TimeoutExpired:
                return "", f"timeout tras {_TIMEOUT_EJECUCION_SEGUNDOS}s"
            except OSError as e:
                return "", f"no se pudo ejecutar el bloque: {e}"

        if proceso.returncode != 0:
            return proceso.stdout or "", (proceso.stderr or "").strip()[-500:]
        return proceso.stdout or "", None

    def _extraer_numeros(self, salida: str) -> list[float]:
        return [float(n) for n in _NUMERO.findall(_limpiar_latex(salida))]

    def check_monte_carlo_convergence(
        self, code_text: str, min_iterations: int = 1000
    ) -> dict[str, Any]:
        """Valida que el numero de iteraciones/muestras declarado en codigo de
        simulacion sea suficiente para convergencia razonable, adaptando el
        patron de stability_guardian.analyze_timestep (Antigravity-Nano) al
        dominio estadistico: convergencia Monte Carlo es O(1/sqrt(N)), no
        lineal, asi que un N bajo produce estimaciones con alta varianza."""
        warnings: list[str] = []
        matches = self._SAMPLE_COUNT_PATTERN.findall(code_text)

        for raw_value in matches:
            n = int(raw_value.replace("_", ""))
            if n < min_iterations:
                warnings.append(
                    f"Número de iteraciones/muestras ({n}) por debajo del "
                    f"mínimo recomendado ({min_iterations}) para convergencia "
                    f"Monte Carlo razonable (error ~ O(1/sqrt(N)))."
                )

        return {
            "critical": len(warnings) > 0,
            "warnings": warnings,
        }
