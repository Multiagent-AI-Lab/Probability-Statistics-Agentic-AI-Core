"""
Tests para extract_mermaid_blocks y MermaidNodeCounter.
"""

from src.multiagent_core._mermaid_utils import (
    MermaidNodeCounter,
    extract_mermaid_blocks,
)


def test_extract_mermaid_blocks_encuentra_un_bloque():
    texto = "texto previo\n```mermaid\ngraph TD\nA --> B\n```\ntexto posterior"

    bloques = extract_mermaid_blocks(texto)

    assert bloques == [(0, "graph TD\nA --> B")]


def test_extract_mermaid_blocks_indexa_multiples_bloques_en_orden():
    texto = "```mermaid\ngraph TD\n```\n\n```mermaid\ngraph LR\n```"

    bloques = extract_mermaid_blocks(texto)

    assert bloques == [(0, "graph TD"), (1, "graph LR")]


def test_extract_mermaid_blocks_retorna_lista_vacia_sin_bloques():
    bloques = extract_mermaid_blocks("texto sin ningún diagrama")

    assert bloques == []


def test_node_counter_genera_ids_secuenciales():
    counter = MermaidNodeCounter()

    assert counter.next_id() == "node_1"
    assert counter.next_id() == "node_2"
    assert counter.next_id() == "node_3"


def test_node_counter_reset_reinicia_la_secuencia():
    counter = MermaidNodeCounter()
    counter.next_id()
    counter.next_id()

    counter.reset()

    assert counter.next_id() == "node_1"
