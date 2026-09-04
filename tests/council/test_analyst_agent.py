"""
Tests para AnalystAgent.audit_visualizations -- visualizaciones e
interpretación post-gráfico.

Tras H-01 ya no basta con que la palabra "interpretación" aparezca en
cualquier parte del documento: debe estar DESPUÉS del gráfico (Gold
Standard §3.8 dice "posterior a cualquier visualización") y afirmar algo
verificable, no ser un rótulo vacío.
"""

from src.multiagent_core.council.analyst_agent import AnalystAgent

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
