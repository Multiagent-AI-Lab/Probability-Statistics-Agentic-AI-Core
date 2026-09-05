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

# Una sección arranca en un encabezado Markdown: es la unidad de contraste
# entre un bloque de código y el `\boxed{}` que ese bloque debería producir.
_ENCABEZADO = re.compile(r"^#{1,6}\s+.*$", re.MULTILINE)

# `\boxed{...}` con un nivel de anidamiento de llaves (p. ej.
# `\boxed{15.65\ \text{nm}}` o `\boxed{\frac{2}{3}}`).
_BOXED = re.compile(r"\\boxed\{((?:[^{}]|\{[^{}]*\})*)\}")

# Número final de una expresión: el último numérico que aparece en el
# `\boxed{}`, que es el resultado (`P(X=2) = 190 \times 0.0025 \approx
# 0.18868` -> 0.18868).
_NUMERO = re.compile(r"-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?")

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
_TOLERANCIA_RELATIVA = 1e-3

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
                self._contrastar_contra_la_unidad(
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
                # Basta con que el valor aparezca en la salida de la sección:
                # el código lo produjo, aunque el rótulo no sea idéntico.
                if self._algun_valor_coincide(valor_esperado, producidos):
                    continue
                if not self._el_codigo_apunta_al_valor(
                    expresion, salida, valor_esperado
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

    def _contrastar_contra_la_unidad(
        self,
        titulo: str,
        esperados: list[tuple[float, str]],
        salida_de_la_unidad: str,
        discrepancias: list[dict[str, Any]],
    ) -> None:
        """Contrasta los `\\boxed{}` de una sección sin código propio contra
        la salida de toda la unidad.

        El criterio es la ausencia: un ejemplo analítico correcto termina en
        un número que el código de la unidad también produce (la media
        calculada a mano en §2.2 es la que §4 imprime como `Media: 15.6500`).
        Si ese valor no aparece por ningún lado, el texto afirma un
        resultado que el código nunca respalda.

        No se exige que los rótulos coincidan: el texto la llama `\\bar{x}`
        y el código `Media:`, y ninguna regla sintáctica une esos nombres de
        forma confiable. El valor mismo es la evidencia.
        """
        numeros_de_la_unidad = self._extraer_numeros(salida_de_la_unidad)
        if not numeros_de_la_unidad:
            return

        # Un `\boxed{}` que el propio código imprime (las lecciones lo generan
        # con `display(Math(fr"... \\boxed{{{valor:.4f}}}"))`) es la afirmación
        # más fuerte disponible: el código declara ESE resultado. Si el texto
        # encuadra otro, ambos hablan del mismo cálculo y no coinciden.
        boxed_del_codigo = self._extraer_valores_boxed(salida_de_la_unidad)

        for valor_esperado, expresion in esperados:
            if self._es_valor_trivial(valor_esperado):
                # 0, 1, 2, porcentajes redondos y demás aparecen en cualquier
                # salida por casualidad: su ausencia no prueba nada y su
                # presencia tampoco.
                continue
            if self._algun_valor_coincide(valor_esperado, numeros_de_la_unidad):
                continue
            # Solo se comparan los `\boxed{}` del código que hablan del mismo
            # cálculo: comparten al menos un dato de entrada con la fórmula
            # del texto. Sin ese anclaje, el `\boxed{-2.83}` de un Z-test
            # resuelto a mano (UNIDAD 7 §1.6) se contrastaría contra el
            # `\boxed{}` de cualquier otro ejemplo de la unidad.
            # El dato compartido puede estar en el enunciado de la sección y
            # no en la línea del `\boxed{}` (UNIDAD 6 §2.3 fija U=0.35 en el
            # título y el código lo repite al rotular su resultado), así que
            # el contexto de la sección cuenta como parte de la expresión.
            contexto = f"{titulo}\n{expresion}"
            comparables = [
                valor
                for valor, expresion_codigo in boxed_del_codigo
                if self._comparten_datos(contexto, expresion_codigo)
            ]
            if comparables and not self._algun_valor_coincide(
                valor_esperado, comparables
            ):
                discrepancias.append(
                    {
                        "seccion": titulo,
                        "valor_declarado": valor_esperado,
                        "valores_producidos": comparables[:10],
                        "motivo": (
                            "el código encuadra un resultado distinto del que "
                            "declara el texto para el mismo cálculo"
                        ),
                    }
                )
                continue

            # Última señal: el resultado intermedio del propio ejemplo está
            # en la salida pero el resultado final no. En
            # `T = 12.0 \times 1.03297 \approx 12.3957` el factor 1.03297 es
            # un decimal calculado, no un dato redondo: si el código lo
            # imprime, está ejecutando ESTE ejemplo, y que su resultado no
            # aparezca indica que el texto quedó desincronizado.
            #
            # Se exige un operando decimal y no cualquier número compartido:
            # un entero como `n=50` coincide por casualidad entre ejemplos
            # distintos (UNIDAD 7 §1.6 resuelve a mano un Z-test de notas de
            # examen mientras el código trabaja el caso AgNP) y reportarlo
            # llenaría el informe de ruido sobre contenido correcto.
            if not self._comparte_operando_calculado(expresion, numeros_de_la_unidad):
                continue
            discrepancias.append(
                {
                    "seccion": titulo,
                    "valor_declarado": valor_esperado,
                    "valores_producidos": numeros_de_la_unidad[:10],
                    "motivo": (
                        "el código calcula los pasos intermedios de este "
                        "ejemplo pero no produce el resultado declarado"
                    ),
                }
            )

    @staticmethod
    def _es_valor_trivial(valor: float) -> bool:
        """Valores que aparecen por casualidad en cualquier salida numérica
        (índices, exponentes, conteos pequeños) y por tanto no sirven ni
        como resultado a contrastar ni como evidencia de corroboración."""
        return abs(valor) <= 2 or (valor == int(valor) and abs(valor) <= 10)

    def _comparten_datos(self, expresion_texto: str, expresion_codigo: str) -> bool:
        """¿Las dos expresiones hablan del mismo cálculo?

        Se consideran el mismo si comparten algún dato de entrada no trivial
        (el mismo λ, la misma μ, el mismo tamaño de muestra) o si el rótulo
        de la cantidad coincide. Es el ancla que evita contrastar el
        resultado de un ejemplo contra el `\\boxed{}` de otro.
        """
        # El rótulo NO se usa como ancla: las lecciones reutilizan los
        # símbolos estándar del dominio (`z_0` nombra tanto el estadístico
        # del ejemplo de notas de examen como el del caso AgNP en
        # UNIDAD 7 §1.6), así que un nombre compartido no implica el mismo
        # cálculo. Solo los datos de entrada identifican el ejemplo.
        return bool(
            self._operandos_distintivos(expresion_texto)
            & self._operandos_distintivos(expresion_codigo)
        )

    def _operandos_distintivos(self, expresion: str) -> set[float]:
        """Números que identifican un ejemplo concreto.

        Aquí se descartan solo los enteros pequeños (índices, exponentes,
        conteos), no los decimales: `0.35` es el dato de entrada que
        distingue el ejemplo de UNIDAD 6 §2.3, aunque sea menor que 1.
        """
        return {
            round(float(n), 4)
            for n in _NUMERO.findall(self._limpiar_latex(expresion))
            if not (float(n) == int(float(n)) and abs(float(n)) <= 10)
        }

    def _comparte_operando_calculado(
        self, expresion: str, numeros_de_la_unidad: list[float]
    ) -> bool:
        """¿El código produce algún operando *calculado* de esta fórmula?

        Solo cuentan los decimales con al menos 2 cifras tras el punto: son
        resultados intermedios de un cálculo (`156.5` no, `76.81` y
        `1.03297` sí), no enteros redondos que dos ejemplos distintos
        pueden compartir por casualidad.
        """
        for texto_numero in _NUMERO.findall(self._limpiar_latex(expresion)):
            if "." not in texto_numero:
                continue
            if len(texto_numero.split(".")[1]) < 2:
                continue
            if self._algun_valor_coincide(float(texto_numero), numeros_de_la_unidad):
                return True
        return False

    def _los_datos_del_ejemplo_estan_en_el_codigo(
        self, expresion: str, numeros_de_la_unidad: list[float]
    ) -> bool:
        """¿El código trabaja sobre los mismos datos que este ejemplo?

        La fórmula encuadrada arrastra sus operandos
        (`z_0 = \\frac{7.8-8}{0.5/\\sqrt{50}}`): si ninguno de esos números
        aparece en la salida de la unidad, el ejemplo es autocontenido y su
        resultado no debía salir del código. Si varios sí aparecen, el
        código está reproduciendo el mismo caso y un resultado ausente sí
        indica desincronización.
        """
        operandos = [
            float(n)
            for n in _NUMERO.findall(self._limpiar_latex(expresion))
            if not self._es_valor_trivial(float(n))
        ]
        if not operandos:
            return False
        return any(
            self._algun_valor_coincide(op, numeros_de_la_unidad) for op in operandos
        )

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
            fin = (
                encabezados[i + 1].start() if i + 1 < len(encabezados) else len(text)
            )
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
            numeros = _NUMERO.findall(self._limpiar_latex(contenido))
            if not numeros:
                continue
            # El nombre de la cantidad suele estar fuera de la caja:
            # `$$\alpha = P(...) \approx \boxed{0.2466}$$` encuadra solo el
            # resultado. Se toma la línea completa para no perderlo.
            inicio_linea = text.rfind("\n", 0, match.start()) + 1
            expresion = text[inicio_linea : match.end()]
            valores.append((float(numeros[-1]), expresion))
        return valores

    @staticmethod
    def _limpiar_latex(expresion: str) -> str:
        """Quita los sufijos LaTeX que no son parte del valor (`\\text{nm}`,
        `^2`, `\\%`) para que `15.65\\ \\text{nm}^2` se lea como 15.65.

        `\\frac{a}{b}` se resuelve a su cociente: borrar la macro dejaría
        los dos enteros sueltos y el "último número" de `\\boxed{\\frac{2}{3}}`
        sería 3, no 0.667.
        """
        sin_texto = re.sub(r"\\text\{[^}]*\}", " ", expresion)
        sin_fracciones = re.sub(
            r"\\[dt]?frac\s*\{\s*(-?\d+(?:\.\d+)?)\s*\}\s*\{\s*(-?\d+(?:\.\d+)?)\s*\}",
            lambda m: (
                repr(float(m.group(1)) / float(m.group(2)))
                if float(m.group(2)) != 0
                else " "
            ),
            sin_texto,
        )
        sin_exponente = re.sub(r"\^\s*\{?-?\d+\}?", " ", sin_fracciones)
        return re.sub(r"\\[a-zA-Z]+", " ", sin_exponente)

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
        return [float(n) for n in _NUMERO.findall(self._limpiar_latex(salida))]

    def _algun_valor_coincide(self, esperado: float, producidos: list[float]) -> bool:
        """El valor declarado aparece en la salida, con tolerancia y
        admitiendo la forma porcentual (`\\boxed{0.1126\\ (11.26\\%)}` frente
        a un `print` de 0.1126, y viceversa)."""
        candidatos = [esperado, esperado / 100.0, esperado * 100.0]
        return any(
            self._valores_coinciden(c, p, _TOLERANCIA_RELATIVA)
            for c in candidatos
            for p in producidos
        )

    def _el_codigo_apunta_al_valor(
        self, expresion_boxed: str, salida: str, valor_declarado: float
    ) -> bool:
        """¿El código dice estar calculando la misma cantidad que el `\\boxed{}`?

        Las lecciones alternan ejemplos analíticos resueltos a mano con
        verificaciones computacionales de OTRO caso: UNIDAD 7 §1.3 deriva
        alpha/beta de una exponencial y su bloque ejecuta un escenario AgNP
        distinto; UNIDAD 4 §3.3 encuadra un `E[Y]=7` algebraico cuyo código
        solo calcula `E[Y|X=1]`. Ambos son contenido correcto, y sin esta
        comprobación se reportarían como discrepancias.

        El criterio es la etiqueta: el código del curso imprime sus
        resultados rotulados (`print(f"E[Y|X=1] = {...}")`), así que un
        `\\boxed{}` es contrastable cuando su lado izquierdo —el nombre de
        la cantidad— aparece en la salida. Un valor calculado bajo otro
        nombre pertenece a otro ejemplo; comparar números sueltos entre sí
        no distingue esos dos casos.
        """
        nombre = self._nombre_de_la_cantidad(expresion_boxed)
        if not nombre:
            # Un `\boxed{}` que es solo un número (`\boxed{0.375}`) no trae
            # nombre propio: se contrasta contra la salida sin exigir rótulo.
            return True
        if not self._normalizar_identificador(salida):
            return False

        # No basta que el nombre aparezca en la salida: `alpha` rotula tanto
        # el `\boxed{0.2466}` del ejemplo exponencial de UNIDAD 7 §1.3 como
        # el `alpha=0.05` que imprime el bloque AgNP de la misma sección —
        # dos cantidades distintas que comparten letra griega.
        #
        # Un desajuste real es el mismo cálculo mal transcrito (el código da
        # 7.5, el texto afirma 9.9): los dos valores quedan en el mismo orden
        # de magnitud. Una diferencia de varias veces indica que el rótulo
        # coincidió por homonimia y que se trata de otro ejemplo, así que no
        # se reporta: esta auditoría prefiere callar a inventar un hallazgo.
        valores_rotulados = self._valores_junto_al_rotulo(nombre, salida)
        return any(
            self._mismo_orden_de_magnitud(valor_declarado, v)
            for v in valores_rotulados
        )

    @staticmethod
    def _mismo_orden_de_magnitud(a: float, b: float) -> bool:
        if a == 0 or b == 0:
            return a == b
        return 0.5 <= abs(a / b) <= 2.0

    def _valores_junto_al_rotulo(self, nombre: str, salida: str) -> list[float]:
        """Números que el código imprime inmediatamente después de un rótulo
        cuyo nombre normalizado coincide con `nombre`."""
        valores: list[float] = []
        for linea in salida.splitlines():
            izquierda, sep, derecha = linea.partition("=")
            if not sep:
                continue
            if self._normalizar_identificador(izquierda).endswith(nombre):
                numeros = _NUMERO.findall(self._limpiar_latex(derecha))
                if numeros:
                    valores.append(float(numeros[0]))
        return valores

    def _nombre_de_la_cantidad(self, expresion: str) -> str:
        """Nombre de la cantidad que el `\\boxed{}` reporta: lo que aparece
        antes del primer `=` de la línea, sin delimitadores de fórmula."""
        izquierda, sep, _ = expresion.partition("=")
        if not sep:
            return ""
        return self._normalizar_identificador(izquierda.replace("$", " "))

    @staticmethod
    def _normalizar_identificador(texto: str) -> str:
        """Reduce notación LaTeX y prosa a letras y dígitos en minúscula, de
        modo que `E[Y|X=1]` (texto) y `E[Y|X=1]` (rótulo del print) coincidan
        pese a `\\hat`, `{}`, `\\,` y demás decoración.

        La barra invertida de una macro se descarta pero su palabra se
        conserva: `\\alpha` es el nombre de la cantidad, y el código la
        rotula como `alpha=` (las lecciones escriben sus `print` en ASCII).
        Borrar la macro entera dejaría sin nombre justo a las cantidades
        que se nombran con una letra griega.
        """
        return re.sub(r"[^0-9a-z]+", "", texto.lower())

    @staticmethod
    def _valores_coinciden(a: float, b: float, tol: float) -> bool:
        """Compara con tolerancia relativa: el texto redondea (0.3333) lo que
        el código imprime completo (0.3333333...)."""
        escala = max(abs(a), abs(b), 1.0)
        return abs(a - b) <= tol * escala

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
