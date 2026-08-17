"""Tests de caracterización para FlowchartAgent (portado desde Programming-Logic)."""

import pytest

from src.multiagent_core.flowchart_agent import FlowchartAgent


@pytest.fixture
def agent() -> FlowchartAgent:
    return FlowchartAgent()


def test_genera_graph_td_para_funcion_con_if_else(agent: FlowchartAgent):
    codigo = """
def clasificar_convergencia(error):
    if error < 0.01:
        estado = "Convergente"
    else:
        estado = "No convergente"
    return estado
"""
    resultado = agent.build_mermaid_flowchart(codigo)
    assert "graph TD" in resultado
    assert "-- Sí -->" in resultado
    assert "-- No -->" in resultado


def test_genera_nodo_de_iteracion_para_for(agent: FlowchartAgent):
    codigo = """
def simular_monte_carlo(muestras):
    total = 0
    for muestra in muestras:
        total = total + muestra
    return total
"""
    resultado = agent.build_mermaid_flowchart(codigo)
    assert "Para Iterar" in resultado


def test_genera_nodo_de_iteracion_para_while(agent: FlowchartAgent):
    codigo = """
def metropolis_hastings(x0, n_iter):
    x = x0
    while n_iter > 0:
        n_iter = n_iter - 1
    return x
"""
    resultado = agent.build_mermaid_flowchart(codigo)
    assert "Mientras Iterar" in resultado


def test_mensaje_cuando_no_hay_funcion(agent: FlowchartAgent):
    resultado = agent.build_mermaid_flowchart("x = 1 + 1")
    assert "No se encontró una definición de función" in resultado


def test_mensaje_controlado_con_sintaxis_invalida(agent: FlowchartAgent):
    resultado = agent.build_mermaid_flowchart("def foo(:\n    pass")
    assert resultado.startswith("%% Error al parsear código")


def test_node_counter_se_reinicia_en_cada_llamada(agent: FlowchartAgent):
    codigo = """
def simple():
    x = 1
    return x
"""
    primera = agent.build_mermaid_flowchart(codigo)
    segunda = agent.build_mermaid_flowchart(codigo)
    assert primera == segunda
