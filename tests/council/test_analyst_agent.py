"""
Tests para AnalystAgent.audit_visualizations -- visualizaciones e
interpretación post-gráfico.

Tras H-01 ya no basta con que la palabra "interpretación" aparezca en
cualquier parte del documento: debe estar DESPUÉS del gráfico (Gold
Standard §3.8 dice "posterior a cualquier visualización") y afirmar algo
verificable, no ser un rótulo vacío.
"""

import time

from src.multiagent_core.council.analyst_agent import (
    _AFIRMACION_VERIFICABLE,
    AnalystAgent,
)

_INTERPRETACION_REAL = (
    "Interpretación: el histograma muestra que el diámetro medio de las "
    "nanopartículas es de 15.65 nm, con una desviación estándar de 8.76 nm "
    "dominada por el agregado de 40.5 nm; al excluirlo la muestra se "
    "concentra entre 11.8 y 14.2 nm, confirmando una síntesis homogénea."
)


def _con_graficos(texto_posterior: str, texto_previo: str = "") -> str:
    return (
        f"{texto_previo}\n"
        "```python\n"
        "plt.hist(diametros)\n"
        "sns.boxplot(x=diametros)\n"
        "```\n"
        f"{texto_posterior}\n"
    )


def test_pasa_con_dos_graficos_e_interpretacion_posterior():
    agent = AnalystAgent()

    resultado = agent.audit_visualizations(_con_graficos(_INTERPRETACION_REAL))

    assert resultado["plot_count"] >= 2
    assert resultado["has_interpretation"] is True
    assert resultado["passed"] is True


def test_falla_por_menos_de_dos_graficos():
    agent = AnalystAgent()
    texto = "```python\nplt.hist(x)\n```\n" + _INTERPRETACION_REAL

    resultado = agent.audit_visualizations(texto)

    assert resultado["plot_count"] < 2
    assert resultado["passed"] is False


def test_falla_por_falta_de_interpretacion():
    agent = AnalystAgent()

    resultado = agent.audit_visualizations(_con_graficos(""))

    assert resultado["has_interpretation"] is False
    assert resultado["passed"] is False


def test_interpretacion_previa_al_grafico_no_cuenta():
    """H-01: `"interpret" in text.lower()` aceptaba la palabra en cualquier
    posición. El Gold Standard §3.8 exige interpretación POSTERIOR."""
    agent = AnalystAgent()

    resultado = agent.audit_visualizations(
        _con_graficos("", texto_previo=_INTERPRETACION_REAL)
    )

    assert resultado["has_interpretation"] is False
    assert resultado["passed"] is False


def test_la_sola_palabra_interpretacion_no_basta():
    """Un rótulo sin afirmación no interpreta nada."""
    agent = AnalystAgent()

    resultado = agent.audit_visualizations(_con_graficos("Interpretación."))

    assert resultado["has_interpretation"] is False
    assert resultado["passed"] is False


def test_interpretacion_debe_afirmar_algo_verificable():
    """Una interpretación real cita magnitudes o una relación concreta; la
    prosa genérica ('los resultados son interesantes') no."""
    agent = AnalystAgent()
    generico = (
        "Interpretación: los resultados obtenidos son muy interesantes y "
        "muestran un comportamiento adecuado para el contexto estudiado, "
        "tal como se esperaba de acuerdo con la teoría revisada arriba."
    )

    resultado = agent.audit_visualizations(_con_graficos(generico))

    assert resultado["has_interpretation"] is False


def test_reporta_la_posicion_del_ultimo_grafico():
    agent = AnalystAgent()

    resultado = agent.audit_visualizations(_con_graficos(_INTERPRETACION_REAL))

    assert resultado["posicion_ultimo_grafico"] > 0


# --------------------------------------------------------------------------
# Regresión de ReDoS en `_AFIRMACION_VERIFICABLE` (hallazgo CRITICAL de
# @security-reviewer sobre el fix de N-02, cerrado con `\d{1,15}` acotado
# en vez de `\d+`). El párrafo real ya está acotado por
# `_MAX_CHARS_PARRAFO_AFIRMACION`, pero estos tests ejercitan el regex
# directamente -sin esa cota externa- para que una futura edición que
# reintroduzca un cuantificador sin límite se detecte aunque la cota de
# longitud también se toque en el mismo cambio.
# --------------------------------------------------------------------------

_TECHO_SEGUNDOS_REDOS = 2.0


def test_afirmacion_verificable_no_escala_cuadratico_con_digitos_sueltos():
    """Una racha larga de dígitos sin unidad reconocida no debe colgar ni
    degradar cuadráticamente."""
    texto = "9" * 50_000

    t0 = time.perf_counter()
    resultado = _AFIRMACION_VERIFICABLE.search(texto)
    duracion = time.perf_counter() - t0

    assert resultado is None
    assert duracion < _TECHO_SEGUNDOS_REDOS, (
        f"_AFIRMACION_VERIFICABLE tardo {duracion:.2f}s sobre 50_000 "
        "digitos sueltos -- posible regresion de ReDoS"
    )


def test_afirmacion_verificable_no_escala_cuadratico_con_digitos_y_puntos():
    """Dígitos con puntos intercalados (p. ej. una cita bibliográfica o un
    número mal formateado) es el adversario con la constante de tiempo más
    alta encontrada para este regex -- ver el comentario junto a
    `_AFIRMACION_VERIFICABLE` en `analyst_agent.py`."""
    texto = "123456789012345." * 5_000

    t0 = time.perf_counter()
    resultado = _AFIRMACION_VERIFICABLE.search(texto)
    duracion = time.perf_counter() - t0

    assert resultado is None
    assert duracion < _TECHO_SEGUNDOS_REDOS, (
        f"_AFIRMACION_VERIFICABLE tardo {duracion:.2f}s sobre digitos y "
        "puntos intercalados -- posible regresion de ReDoS"
    )
