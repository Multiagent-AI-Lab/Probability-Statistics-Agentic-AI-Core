"""
Tests para AnalystAgent.audit_visualizations -- visualizaciones e
interpretación post-gráfico (>=2 gráficos + interpretación).
"""

from src.multiagent_core.council.analyst_agent import AnalystAgent


def test_pasa_con_dos_o_mas_graficos_e_interpretacion():
    agent = AnalystAgent()
    texto = "plt.plot(x) sns.histplot(y) Interpretación: la media es 10."

    resultado = agent.audit_visualizations(texto)

    assert resultado["plot_count"] >= 2
    assert resultado["has_interpretation"] is True
    assert resultado["passed"] is True


def test_falla_por_menos_de_dos_graficos():
    agent = AnalystAgent()
    texto = "plt.plot(x) Interpretación: la media es 10."

    resultado = agent.audit_visualizations(texto)

    assert resultado["plot_count"] < 2
    assert resultado["passed"] is False


def test_falla_por_falta_de_interpretacion():
    agent = AnalystAgent()
    texto = "plt.plot(x) sns.histplot(y)"

    resultado = agent.audit_visualizations(texto)

    assert resultado["has_interpretation"] is False
    assert resultado["passed"] is False


def test_detecta_interpretacion_en_espanol_con_analisis():
    agent = AnalystAgent()
    texto = "plt.plot(x) sns.histplot(y) Análisis de los resultados obtenidos."

    resultado = agent.audit_visualizations(texto)

    assert resultado["has_interpretation"] is True


def test_detecta_interpretacion_con_conclusion():
    agent = AnalystAgent()
    texto = "plt.plot(x) sns.histplot(y) Conclusion: los datos siguen una normal."

    resultado = agent.audit_visualizations(texto)

    assert resultado["has_interpretation"] is True
