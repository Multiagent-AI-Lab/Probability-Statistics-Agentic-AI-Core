"""
Tests para QAAgent.final_audit -- auditor supremo que agrega los reportes
del Consejo (no decide el gate de publicación, ver GOVERNANCE.md §4).
"""

from src.multiagent_core.council.qa_agent import QAAgent


def test_approved_true_cuando_todos_los_reportes_pasan():
    agent = QAAgent()
    reportes = {
        "engineer": {"passed": True},
        "editor": {"passed": True},
        "scientist": {"passed": True},
    }

    resultado = agent.final_audit(reportes)

    assert resultado["approved"] is True
    assert resultado["reports"] == reportes


def test_approved_false_si_al_menos_un_reporte_falla():
    agent = QAAgent()
    reportes = {
        "engineer": {"passed": True},
        "editor": {"passed": False},
    }

    resultado = agent.final_audit(reportes)

    assert resultado["approved"] is False


def test_reporte_sin_clave_passed_se_trata_como_no_aprobado():
    agent = QAAgent()
    reportes = {
        "engineer": {"passed": True},
        "architect": {"skipped": True},
    }

    resultado = agent.final_audit(reportes)

    assert resultado["approved"] is False


def test_dict_de_reportes_vacio_aprueba_por_vacuidad():
    agent = QAAgent()

    resultado = agent.final_audit({})

    assert resultado["approved"] is True
    assert resultado["reports"] == {}
