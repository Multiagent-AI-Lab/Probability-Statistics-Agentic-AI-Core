"""
Tests del runner de medicion de A3 (auditoria 2026-09-14). Testea solo el
calculo de metricas contra matrices de confusion sinteticas con resultado
conocido a mano -- no vuelve a correr el Consejo completo en CI (evita
fragilidad si algun fixture depende de renderizado Mermaid/npx o de Crossref).
El runner en si (scripts/medir_precision_consejo.py) se ejecuta manualmente,
igual que convert_to_notebooks_smart.py.
"""

from unittest.mock import patch

import pytest

from scripts.medir_precision_consejo import acumular_casos, calcular_metricas


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


@patch("scripts.medir_precision_consejo.evaluar_caso")
def test_acumular_casos_clasifica_vp_fp_fn_vn_correctamente(mock_evaluar, tmp_path):
    """Helper compartido entre A3 y A3-U (Important de la revision final de
    A3-U, 2026-09-17): antes cada runner tenia su propia copia de este bucle
    de acumulacion -- un fix futuro en uno no se propagaba al otro."""
    (tmp_path / "a.md").write_text("sin DOI", encoding="utf-8")
    (tmp_path / "b.md").write_text("sin DOI", encoding="utf-8")
    (tmp_path / "c.md").write_text("sin DOI", encoding="utf-8")
    (tmp_path / "d.md").write_text("sin DOI", encoding="utf-8")
    manifiesto = [
        {"archivo": "a.md", "tiene_fallo": True, "tipo_fallo": "x", "origen": "real"},
        {"archivo": "b.md", "tiene_fallo": True, "tipo_fallo": "x", "origen": "real"},
        {"archivo": "c.md", "tiene_fallo": False, "tipo_fallo": None, "origen": "real"},
        {"archivo": "d.md", "tiene_fallo": False, "tipo_fallo": None, "origen": "real"},
    ]
    mock_evaluar.side_effect = [
        {"predicho_tiene_fallo": True, "librarian_paso": True, "hallazgos": []},  # vp
        {"predicho_tiene_fallo": False, "librarian_paso": True, "hallazgos": []},  # fn
        {"predicho_tiene_fallo": True, "librarian_paso": True, "hallazgos": []},  # fp
        {"predicho_tiene_fallo": False, "librarian_paso": True, "hallazgos": []},  # vn
    ]

    matriz, detalle, excluidos = acumular_casos(
        manifiesto, tmp_path, campos_extra=["origen"]
    )

    assert matriz == {"vp": 1, "fp": 1, "fn": 1, "vn": 1}
    assert excluidos == []
    assert len(detalle) == 4
    assert detalle[0]["archivo"] == "a.md"
    assert detalle[0]["origen"] == "real"
    assert detalle[0]["tiene_fallo_real"] is True
    assert detalle[0]["predicho_tiene_fallo"] is True
    assert detalle[0]["acierto"] is True


@patch("scripts.medir_precision_consejo.evaluar_caso")
def test_acumular_casos_excluye_fallo_de_librarian_por_red(mock_evaluar, tmp_path):
    """Un caso que cita DOI y falla @Librarian se excluye de la matriz (no
    es un fallo de contenido, es Crossref inaccesible) -- mismo criterio ya
    usado por evaluar_caso, ahora centralizado en acumular_casos."""
    (tmp_path / "con_doi.md").write_text("cita DOI: 10.1000/xyz", encoding="utf-8")
    manifiesto = [
        {
            "archivo": "con_doi.md",
            "tiene_fallo": False,
            "tipo_fallo": None,
            "origen": "real",
        },
    ]
    mock_evaluar.return_value = {
        "predicho_tiene_fallo": True,
        "librarian_paso": False,
        "hallazgos": [],
    }

    matriz, detalle, excluidos = acumular_casos(manifiesto, tmp_path)

    assert matriz == {"vp": 0, "fp": 0, "fn": 0, "vn": 0}
    assert excluidos == ["con_doi.md"]
    assert detalle == []


@patch("scripts.medir_precision_consejo.evaluar_caso")
def test_acumular_casos_acepta_campos_de_detalle_extra(mock_evaluar, tmp_path):
    """A3-U agrega el campo unidad_origen a cada fila de detalle (A3 no lo
    tiene) -- acumular_casos debe propagar cualquier campo extra del
    manifiesto sin necesitar un parametro especial por cada runner."""
    (tmp_path / "u1.md").write_text("sin DOI", encoding="utf-8")
    manifiesto = [
        {
            "archivo": "u1.md",
            "tiene_fallo": False,
            "tipo_fallo": None,
            "unidad_origen": "UNIDAD_1.md",
        },
    ]
    mock_evaluar.return_value = {
        "predicho_tiene_fallo": False,
        "librarian_paso": True,
        "hallazgos": [],
    }

    _, detalle, _ = acumular_casos(manifiesto, tmp_path, campos_extra=["unidad_origen"])

    assert detalle[0]["unidad_origen"] == "UNIDAD_1.md"
