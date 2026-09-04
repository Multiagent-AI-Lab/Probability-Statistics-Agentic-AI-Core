"""
Tests para QAAgent.final_audit -- auditor supremo que agrega los reportes
del Consejo en hallazgos tipados.

Tras H-01 el veredicto ya no es un `all(rep["passed"])` ciego: los reportes
se traducen a hallazgos `{tipo, severidad, agente, mensaje}` y la decisión
se toma sobre ellos, de modo que el reporte diga QUÉ falló y con qué
gravedad, y que un aviso menor no bloquee igual que un error de contenido.
"""

from src.multiagent_core.council.qa_agent import (
    SEVERIDAD_BLOQUEANTE,
    SEVERIDAD_ADVERTENCIA,
    QAAgent,
)


def test_approved_true_cuando_todos_los_reportes_pasan():
    agent = QAAgent()
    reportes = {
        "engineer": {"passed": True},
        "editor": {"passed": True},
        "scientist": {"passed": True},
    }

    resultado = agent.final_audit(reportes)

    assert resultado["approved"] is True
    assert resultado["hallazgos"] == []
    assert resultado["reports"] == reportes


def test_approved_false_si_al_menos_un_reporte_falla():
    agent = QAAgent()
    reportes = {
        "engineer": {"passed": True},
        "editor": {"passed": False},
    }

    resultado = agent.final_audit(reportes)

    assert resultado["approved"] is False


def test_reporte_saltado_no_cuenta_como_fallo():
    """@Architect es advisory-only en el flujo por lección: se auto-reporta
    como `skipped` y eso no debe bloquear la publicación."""
    agent = QAAgent()
    reportes = {
        "engineer": {"passed": True},
        "architect": {"passed": True, "skipped": True},
    }

    resultado = agent.final_audit(reportes)

    assert resultado["approved"] is True


def test_reporte_sin_clave_passed_se_trata_como_no_aprobado():
    agent = QAAgent()
    reportes = {
        "engineer": {"passed": True},
        "architect": {"resultado": "raro"},
    }

    resultado = agent.final_audit(reportes)

    assert resultado["approved"] is False


def test_dict_de_reportes_vacio_aprueba_por_vacuidad():
    agent = QAAgent()

    resultado = agent.final_audit({})

    assert resultado["approved"] is True
    assert resultado["reports"] == {}


# --- Hallazgos tipados (H-01, Step 7) ---


def test_invariante_violado_produce_hallazgo_tipado_bloqueante():
    agent = QAAgent()
    reportes = {
        "scientist": {
            "passed": False,
            "invariantes_violados": ["probabilidad fuera de [0,1]: 1.75"],
        }
    }

    resultado = agent.final_audit(reportes)

    hallazgo = next(h for h in resultado["hallazgos"] if h["tipo"] == "invariante_violado")
    assert hallazgo["severidad"] == SEVERIDAD_BLOQUEANTE
    assert hallazgo["agente"] == "scientist"
    assert "1.75" in hallazgo["mensaje"]
    assert resultado["approved"] is False


def test_discrepancia_ejemplo_salida_produce_hallazgo_tipado():
    agent = QAAgent()
    reportes = {
        "engineer": {
            "passed": False,
            "discrepancias": [
                {
                    "seccion": "### 2.2",
                    "valor_declarado": 19.99,
                    "valores_producidos": [15.65],
                }
            ],
        }
    }

    resultado = agent.final_audit(reportes)

    hallazgo = next(
        h for h in resultado["hallazgos"] if h["tipo"] == "desajuste_ejemplo_salida"
    )
    assert hallazgo["severidad"] == SEVERIDAD_BLOQUEANTE
    assert "19.99" in hallazgo["mensaje"]


def test_referencia_inexistente_produce_hallazgo_tipado():
    agent = QAAgent()
    reportes = {
        "librarian": {"passed": False, "dois_no_resueltos": ["10.9999/roto"]}
    }

    resultado = agent.final_audit(reportes)

    hallazgo = next(
        h for h in resultado["hallazgos"] if h["tipo"] == "referencia_inexistente"
    )
    assert "10.9999/roto" in hallazgo["mensaje"]


def test_supuesto_no_verificado_es_advertencia_y_no_bloquea():
    """Un warning de supuestos estadísticos informa, pero no es un error de
    contenido: no debe bloquear la publicación por sí solo."""
    agent = QAAgent()
    reportes = {
        "safety_gate": {
            "passed": False,
            "critical": False,
            "warnings": ["Se utiliza 't-test' sin antes verificar normalidad."],
        }
    }

    resultado = agent.final_audit(reportes)

    hallazgo = next(
        h for h in resultado["hallazgos"] if h["tipo"] == "supuesto_no_verificado"
    )
    assert hallazgo["severidad"] == SEVERIDAD_ADVERTENCIA
    assert resultado["approved"] is True


def test_anacronismo_curricular_critico_si_bloquea():
    agent = QAAgent()
    reportes = {
        "safety_gate": {
            "passed": False,
            "critical": True,
            "warnings": ["🚨 [Error de Secuencia Curricular]: UNIDAD 2 usa ANOVA."],
        }
    }

    resultado = agent.final_audit(reportes)

    assert resultado["approved"] is False
    assert any(h["severidad"] == SEVERIDAD_BLOQUEANTE for h in resultado["hallazgos"])


def test_interpretacion_ausente_produce_hallazgo_tipado():
    agent = QAAgent()
    reportes = {"analyst": {"passed": False, "has_interpretation": False}}

    resultado = agent.final_audit(reportes)

    assert any(
        h["tipo"] == "interpretacion_ausente" for h in resultado["hallazgos"]
    )


def test_los_hallazgos_se_agrupan_por_severidad_en_el_resumen():
    agent = QAAgent()
    reportes = {
        "scientist": {"passed": False, "invariantes_violados": ["varianza negativa: -4"]},
        "safety_gate": {
            "passed": False,
            "critical": False,
            "warnings": ["Se utiliza 'anova' sin verificar homocedasticidad."],
        },
    }

    resultado = agent.final_audit(reportes)

    assert resultado["resumen"][SEVERIDAD_BLOQUEANTE] == 1
    assert resultado["resumen"][SEVERIDAD_ADVERTENCIA] == 1
