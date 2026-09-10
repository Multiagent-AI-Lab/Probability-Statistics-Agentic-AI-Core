"""Verifica que toda referencia interna a una sección (`§N.M`, `Sección N.M`)
citada en las lecciones apunte a un encabezado que realmente existe.

Motivación: las lecciones se citan entre sí constantemente ("como se vio en
§1.9", "Unidad 4 §7.4"). Cuando una sección se renumera o se mueve, esas citas
quedan colgando y el alumno persigue un puntero roto. Este test las verifica
todas de forma mecánica.

Convención de numeración del curso: `§N.M` es *intra-unidad* — `N` es la
sección de primer nivel (`## N. ...`) DENTRO de la unidad, no el número de
unidad. Una cita solo apunta a otra unidad cuando el texto lo dice
explícitamente ("Unidad 4 §7.4"), y en ese caso `N` sigue siendo la sección de
primer nivel de la unidad destino.
"""

import re
from pathlib import Path

import pytest

LECCIONES_DIR = Path(__file__).resolve().parent.parent / "lecciones"

# `§ 1.2`, `Sección 1.2`, `Seccion 1.2`, `sección 1.2` — y sub-secciones de
# tercer nivel (`§2.12.6`), que el curso también usa.
_REFERENCIA_PATTERN = re.compile(
    r"(?:§\s*|[Ss]ecci[óo]n\s+|[Ss]eccion\s+)(\d+\.\d+(?:\.\d+)?)"
)

# "Unidad 7 (§1.9)", "Unidad 5, §2.4", "Unidad 4 §6.4". El destino explícito se
# busca hacia atrás dentro de la MISMA oración, de modo que "Se aborda en la
# **Unidad 7** (...), con el Método de los Momentos (§1.9)" resuelve a la Unidad
# 7 aunque medien decenas de caracteres, mientras que una unidad mencionada en
# la oración anterior no contamina la resolución de esta cita.
#
# El fin de oración es "un punto NO rodeado de dígitos": los números de sección
# citados en la propia oración (`§1.1-1.8`) llevan punto decimal y no deben
# leerse como fin de oración.
_FIN_DE_ORACION = r"(?<!\d)\.(?!\d)"
_UNIDAD_EXPLICITA_PATTERN = re.compile(
    rf"[Uu]nidad\s+(\d+)(?:(?!{_FIN_DE_ORACION}).)*$"
)
# La ventana acota el retroceso a un párrafo razonable; el corte por oración
# de arriba es el criterio real.
_VENTANA_UNIDAD_CHARS = 400

# `## 1. Fundamentación ...` (sección de primer nivel)
_ENCABEZADO_NIVEL1_PATTERN = re.compile(r"^##\s+(\d+)\.\s", re.MULTILINE)
# `### 1.2 Medidas ...`, `#### 7.8.1 Sobreajuste ...`
_ENCABEZADO_NIVEL2_PATTERN = re.compile(
    r"^#{3,4}\s+(\d+\.\d+(?:\.\d+)?)\s", re.MULTILINE
)

# Los bloques de código llevan comentarios que empiezan con `##`, idénticos a
# un encabezado Markdown (`## 3. Sustitución de valores`), y a veces citan
# secciones en prosa dentro del comentario. Ni unos ni otros son contenido del
# documento: se eliminan antes de extraer nada.
_FENCE_PATTERN = re.compile(r"^(`{3,})[^\n]*\n.*?^\1[ \t]*$", re.MULTILINE | re.DOTALL)


def _sin_bloques_de_codigo(texto: str) -> str:
    """Elimina los bloques de código con fence, preservando el número de líneas."""
    return _FENCE_PATTERN.sub(
        lambda m: "\n" * m.group(0).count("\n"),
        texto,
    )


def _numero_de_unidad(nombre_archivo: str) -> int:
    match = re.match(r"UNIDAD_(\d+)_", nombre_archivo)
    assert match, f"Nombre de lección inesperado: {nombre_archivo}"
    return int(match.group(1))


def _unidades() -> dict[int, str]:
    """Mapea número de unidad -> texto de la lección, sin bloques de código."""
    unidades = {}
    for path in sorted(LECCIONES_DIR.glob("UNIDAD_*.md")):
        numero = _numero_de_unidad(path.name)
        unidades[numero] = _sin_bloques_de_codigo(path.read_text(encoding="utf-8"))
    return unidades


def extraer_referencias_por_unidad() -> dict[int, list[dict]]:
    """Extrae toda cita a una sección, resuelta a su unidad destino.

    Returns:
        Mapa de número de unidad origen -> lista de referencias. Cada
        referencia es un dict con `seccion` (p. ej. "1.9"), `unidad_destino`
        (int) y `contexto` (el fragmento de texto donde aparece, para que el
        mensaje de fallo sea accionable).
    """
    referencias: dict[int, list[dict]] = {}

    for unidad_origen, texto in _unidades().items():
        encontradas = []
        for match in _REFERENCIA_PATTERN.finditer(texto):
            inicio_ventana = max(0, match.start() - _VENTANA_UNIDAD_CHARS)
            # Nunca retroceder más allá del inicio de la línea/párrafo actual.
            bruto = texto[inicio_ventana : match.start()]
            ventana = bruto.rsplit("\n", 1)[-1]

            unidad_explicita = _UNIDAD_EXPLICITA_PATTERN.search(ventana)
            unidad_destino = (
                int(unidad_explicita.group(1)) if unidad_explicita else unidad_origen
            )

            encontradas.append(
                {
                    "seccion": match.group(1),
                    "unidad_destino": unidad_destino,
                    "contexto": texto[max(0, match.start() - 90) : match.end() + 40]
                    .replace("\n", " ")
                    .strip(),
                }
            )
        referencias[unidad_origen] = encontradas

    return referencias


def seccion_existe(unidad: int, seccion: str) -> bool:
    """Confirma que la unidad destino tiene un encabezado para esa sección.

    Acepta tanto el encabezado exacto (`### 1.9 ...`) como —para una cita a una
    sub-sección de tercer nivel cuyo encabezado no está desglosado— el
    encabezado padre (`### 2.12 ...` cubre a `§2.12.6`).
    """
    unidades = _unidades()
    if unidad not in unidades:
        return False

    texto = unidades[unidad]
    secciones = set(_ENCABEZADO_NIVEL2_PATTERN.findall(texto))
    secciones.update(_ENCABEZADO_NIVEL1_PATTERN.findall(texto))

    if seccion in secciones:
        return True

    # `§2.12.6` es válida si existe `### 2.12`.
    partes = seccion.split(".")
    return len(partes) == 3 and ".".join(partes[:2]) in secciones


def test_hay_referencias_que_verificar():
    """Guardarraíl: si la extracción deja de encontrar nada, el test de abajo
    pasaría vacío y dejaría de proteger el contenido."""
    total = sum(len(refs) for refs in extraer_referencias_por_unidad().values())
    assert total > 50, f"Se esperaban decenas de referencias, se hallaron {total}"


def test_todas_las_lecciones_fueron_leidas():
    unidades = _unidades()
    assert len(unidades) == 8, f"Se esperaban 8 unidades, se hallaron {len(unidades)}"


@pytest.mark.parametrize("unidad_origen", sorted(_unidades()))
def test_todas_las_referencias_seccion_existen(unidad_origen):
    """Cada `§N.M` citado debe resolver a un encabezado real de su unidad destino."""
    referencias = extraer_referencias_por_unidad()[unidad_origen]

    rotas = [
        ref
        for ref in referencias
        if not seccion_existe(ref["unidad_destino"], ref["seccion"])
    ]

    detalle = "\n".join(
        f"  - §{ref['seccion']} -> UNIDAD_{ref['unidad_destino']} | ...{ref['contexto']}..."
        for ref in rotas
    )
    assert (
        not rotas
    ), f"UNIDAD_{unidad_origen} cita {len(rotas)} sección(es) inexistente(s):\n{detalle}"
