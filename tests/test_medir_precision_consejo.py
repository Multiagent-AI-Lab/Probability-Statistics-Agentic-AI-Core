"""
Tests del runner de medicion de A3 (auditoria 2026-09-14). Testea solo el
calculo de metricas contra matrices de confusion sinteticas con resultado
conocido a mano -- no vuelve a correr el Consejo completo en CI (evita
fragilidad si algun fixture depende de renderizado Mermaid/npx o de Crossref).
El runner en si (scripts/medir_precision_consejo.py) se ejecuta manualmente,
igual que convert_to_notebooks_smart.py.
"""

import pytest

from scripts.medir_precision_consejo import calcular_metricas


def test_precision_perfecta_sin_falsos_positivos():
    matriz = {"vp": 10, "fp": 0, "fn": 2, "vn": 8}
    metricas = calcular_metricas(matriz)
    assert metricas["precision"] == pytest.approx(1.0)


def test_recall_perfecto_sin_falsos_negativos():
    matriz = {"vp": 10, "fp": 3, "fn": 0, "vn": 7}
    metricas = calcular_metricas(matriz)
    assert metricas["recall"] == pytest.approx(1.0)


def test_precision_y_recall_con_matriz_mixta():
    # vp=6, fp=2, fn=4, vn=8 -> precision=6/8=0.75, recall=6/10=0.6
    matriz = {"vp": 6, "fp": 2, "fn": 4, "vn": 8}
    metricas = calcular_metricas(matriz)
    assert metricas["precision"] == pytest.approx(0.75)
    assert metricas["recall"] == pytest.approx(0.6)


def test_kappa_de_cohen_con_acuerdo_perfecto_es_uno():
    matriz = {"vp": 10, "fp": 0, "fn": 0, "vn": 10}
    metricas = calcular_metricas(matriz)
    assert metricas["kappa"] == pytest.approx(1.0)


def test_kappa_de_cohen_con_desacuerdo_total_es_negativo():
    # El Consejo predice fallo cuando no hay, y no-fallo cuando sí hay --
    # peor que azar, kappa negativo.
    matriz = {"vp": 0, "fp": 10, "fn": 10, "vn": 0}
    metricas = calcular_metricas(matriz)
    assert metricas["kappa"] < 0


def test_kappa_de_cohen_con_prediccion_aleatoria_cercano_a_cero():
    # Etiquetas 50/50, prediccion independiente de la etiqueta real ->
    # acuerdo observado ~= acuerdo esperado por azar -> kappa ~= 0.
    matriz = {"vp": 5, "fp": 5, "fn": 5, "vn": 5}
    metricas = calcular_metricas(matriz)
    assert metricas["kappa"] == pytest.approx(0.0, abs=1e-9)


def test_precision_es_none_sin_predicciones_positivas():
    matriz = {"vp": 0, "fp": 0, "fn": 5, "vn": 10}
    metricas = calcular_metricas(matriz)
    assert metricas["precision"] is None
