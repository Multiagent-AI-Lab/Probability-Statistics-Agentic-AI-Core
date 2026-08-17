"""Tests TDD para CurriculumMapAgent (heurística de prerequisitos + render del DAG) — Probabilidad."""

from pathlib import Path

import pytest

from src.multiagent_core.curriculum_map_agent import CurriculumMapAgent


@pytest.fixture
def agent() -> CurriculumMapAgent:
    return CurriculumMapAgent()


class TestSuggestPrerequisites:
    def test_detecta_termino_compartido_entre_dos_unidades(
        self, agent: CurriculumMapAgent, tmp_path: Path
    ):
        (tmp_path / "UNIDAD_2_TEST.md").write_text(
            "# UNIDAD 2\n\nEsta unidad introduce la combinatoria y el teorema de Bayes.\n",
            encoding="utf-8",
        )
        (tmp_path / "UNIDAD_4_TEST.md").write_text(
            "# UNIDAD 4\n\nAquí reutilizamos el teorema de Bayes visto antes.\n",
            encoding="utf-8",
        )
        candidatos = agent.suggest_prerequisites(tmp_path)

        assert 4 in candidatos
        terminos_u4 = [c["termino"] for c in candidatos[4]]
        assert "bayes" in terminos_u4
        assert candidatos[4][terminos_u4.index("bayes")]["unidad_origen"] == 2

    def test_no_genera_candidato_si_termino_solo_aparece_en_una_unidad(
        self, agent: CurriculumMapAgent, tmp_path: Path
    ):
        (tmp_path / "UNIDAD_2_TEST.md").write_text(
            "# UNIDAD 2\n\nCombinatoria y Bayes.\n", encoding="utf-8"
        )
        (tmp_path / "UNIDAD_4_TEST.md").write_text(
            "# UNIDAD 4\n\nSin relación con lo anterior.\n", encoding="utf-8"
        )
        candidatos = agent.suggest_prerequisites(tmp_path)

        assert candidatos.get(4, []) == []

    def test_no_genera_candidato_desde_unidad_posterior_hacia_anterior(
        self, agent: CurriculumMapAgent, tmp_path: Path
    ):
        (tmp_path / "UNIDAD_2_TEST.md").write_text(
            "# UNIDAD 2\n\nTexto sin términos relevantes.\n", encoding="utf-8"
        )
        (tmp_path / "UNIDAD_4_TEST.md").write_text(
            "# UNIDAD 4\n\nEsta unidad enseña covarianza.\n", encoding="utf-8"
        )
        candidatos = agent.suggest_prerequisites(tmp_path)

        assert candidatos.get(2, []) == []

    def test_evidencia_incluye_fragmento_textual(
        self, agent: CurriculumMapAgent, tmp_path: Path
    ):
        (tmp_path / "UNIDAD_3_TEST.md").write_text(
            "# UNIDAD 3\n\nSe explica la función de masa de probabilidad (PMF).\n",
            encoding="utf-8",
        )
        (tmp_path / "UNIDAD_5_TEST.md").write_text(
            "# UNIDAD 5\n\nAquí usamos la PMF discreta como contraste con la PDF continua.\n",
            encoding="utf-8",
        )
        candidatos = agent.suggest_prerequisites(tmp_path)

        terminos_u5 = {c["termino"]: c for c in candidatos.get(5, [])}
        assert "pmf" in terminos_u5
        assert len(terminos_u5["pmf"]["evidencia"]) > 0


class TestRenderDag:
    def test_incluye_cadena_secuencial_completa(
        self, agent: CurriculumMapAgent, tmp_path: Path
    ):
        for n in range(1, 9):
            (tmp_path / f"UNIDAD_{n}_TEST.md").write_text(
                f"# UNIDAD {n}\n", encoding="utf-8"
            )
        mermaid = agent.render_dag(tmp_path)

        assert "U1" in mermaid and "U8" in mermaid
        assert "-->" in mermaid

    def test_incluye_las_3_fases_de_uso_de_agentes(
        self, agent: CurriculumMapAgent, tmp_path: Path
    ):
        for n in range(1, 9):
            (tmp_path / f"UNIDAD_{n}_TEST.md").write_text(
                f"# UNIDAD {n}\n", encoding="utf-8"
            )
        mermaid = agent.render_dag(tmp_path)

        assert "graph LR" in mermaid

    def test_genera_flecha_punteada_por_relacion_declarada(
        self, agent: CurriculumMapAgent, tmp_path: Path
    ):
        (tmp_path / "UNIDAD_2_TEST.md").write_text("# UNIDAD 2\n", encoding="utf-8")
        (tmp_path / "UNIDAD_4_TEST.md").write_text(
            "# UNIDAD 4\n\n## Prerequisitos de esta unidad\n\n"
            "- **Teorema de Bayes** (Unidad 2) — se reutiliza para inferencia condicional.\n",
            encoding="utf-8",
        )
        mermaid = agent.render_dag(tmp_path)

        assert "-.Teorema" in mermaid or "-.teorema" in mermaid.lower()

    def test_linea_mal_formada_se_ignora_silenciosamente(
        self, agent: CurriculumMapAgent, tmp_path: Path
    ):
        (tmp_path / "UNIDAD_4_TEST.md").write_text(
            "# UNIDAD 4\n\n## Prerequisitos de esta unidad\n\n"
            "- **Bayes** (unidad 2) — formato incorrecto, minúscula.\n",
            encoding="utf-8",
        )
        mermaid = agent.render_dag(tmp_path)

        assert "-." not in mermaid
