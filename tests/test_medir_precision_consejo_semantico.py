"""
Tests del runner de medición A3-Semántico (deuda de seguimiento, plan
2026-09-23-semantic-auditor-agent). Solo testea que el runner reutilice
`calcular_metricas` de scripts/medir_precision_consejo.py -- ya probada
con matrices sintéticas en tests/test_medir_precision_consejo.py -- en
vez de reimplementarla, y que el reporte incluya kappa. No hace ninguna
llamada de red real: `SemanticAuditorAgent.check_semantics` se mockea.
"""

from unittest.mock import patch

from scripts.medir_precision_consejo_semantico import (
    _calcular_matriz,
    _escribir_reporte,
)


def test_calcular_matriz_usa_calcular_metricas_del_modulo_compartido():
    """Confirma la reutilización real (no una reimplementación con el
    mismo resultado): si `calcular_metricas` cambiara mañana, este test
    seguiría verde solo si el runner de verdad la importa y llama."""
    detalle = [
        {"real": True, "predicho": True},
        {"real": True, "predicho": False},
        {"real": False, "predicho": True},
        {"real": False, "predicho": False},
    ]

    with patch(
        "scripts.medir_precision_consejo_semantico.calcular_metricas",
        return_value={"precision": 0.5, "recall": 0.5, "kappa": 0.0},
    ) as mock_calcular:
        matriz, metricas = _calcular_matriz(detalle)

    mock_calcular.assert_called_once_with({"vp": 1, "fp": 1, "fn": 1, "vn": 1})
    assert metricas == {"precision": 0.5, "recall": 0.5, "kappa": 0.0}
    assert matriz == {"vp": 1, "fp": 1, "fn": 1, "vn": 1}


def test_reporte_incluye_kappa():
    detalle = [
        {
            "archivo": "neg_u1.md",
            "unidad_origen": "UNIDAD_1",
            "tipo_fallo": None,
            "real": False,
            "predicho": False,
            "acierto": True,
            "auditoria_incompleta": False,
            "explicacion_fp": None,
        }
    ]
    matriz = {"vp": 0, "fp": 0, "fn": 0, "vn": 1}
    metricas = {"precision": None, "recall": None, "kappa": 1.0}

    contenido = _escribir_reporte(detalle, matriz, metricas, escribir_archivo=False)

    assert "Kappa de Cohen: 1.0" in contenido
