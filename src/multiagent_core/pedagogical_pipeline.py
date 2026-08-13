"""
PedagogicalReviewPipeline: Pipeline de Crítica y Evaluación Colectiva Pedagógica y Editorial.
Integra ContentAuditorAgent, ScientistAgent (@Scientist), SafetyGateAgent (@Safety_Gate),
LayoutEditorialAgent (@Editor), SocraticDebugger y EvaluatorCriticAgent.
"""

from typing import Dict, Any, List
from .content_auditor_agent import ContentAuditorAgent
from .council.scientist_agent import ScientistAgent
from .council.safety_gate_agent import SafetyGateAgent
from .council.layout_editorial_agent import LayoutEditorialAgent
from external_skills.pedagogy.socratic_debugger import SocraticDebugger


class EvaluatorCriticAgent:
    """Agente Evaluador-Crítico que sintetiza los debates, diseño editorial y críticas entre agentes."""

    def synthesize_critique(
        self,
        content_audit: Dict[str, Any],
        sci_critique: Dict[str, Any],
        safety_critique: Dict[str, Any],
        editorial_audit: Dict[str, Any],
        socratic_questions: List[str]
    ) -> Dict[str, Any]:
        
        critiques = []
        recommendations = []
        
        # 1. Crítica de Estructura del ContentAuditorAgent
        missing = content_audit.get("missing_components", [])
        if missing:
            critiques.append(f"📝 [ContentAuditor]: Faltan componentes del Protocolo Maestro: {', '.join(missing)}.")
            recommendations.append(f"Añadir secciones explícitas para: {', '.join(missing)}.")
        else:
            critiques.append("📝 [ContentAuditor]: Estructura del Protocolo Maestro 100% satisfecha.")

        # 2. Crítica de Rigor Teórico del @Scientist
        if sci_critique.get("word_count", 0) < 1000:
            critiques.append("🔬 [@Scientist]: El desarrollo teórico es breve; requiere profundizar en las derivaciones.")
            recommendations.append("Ampliar la explicación axiomática de las propiedades estadísticas.")
        else:
            critiques.append(f"🔬 [@Scientist]: Excelente profundidad teórica ({sci_critique['word_count']:,} palabras).")

        # 3. Crítica Pedagógica del @Safety_Gate
        warnings = safety_critique.get("warnings", [])
        if warnings:
            for w in warnings:
                critiques.append(f"🛡️ [@Safety_Gate]: Alerta instruccional: {w}")
                recommendations.append(f"Incluir verificación previa de supuestos antes del código.")
        else:
            critiques.append("🛡️ [@Safety_Gate]: Coherencia instruccional y supuestos estadísticos validados.")

        # 4. Crítica de Diseño Editorial del @Editor (LayoutEditorialAgent)
        layout_issues = editorial_audit.get("issues", [])
        if layout_issues:
            for issue in layout_issues:
                critiques.append(f"🎨 [@Editor]: Fallo de maquetación: {issue}")
                recommendations.append("Limpiar títulos descontextualizados y reorganizar la introducción teórica.")
        else:
            critiques.append("🎨 [@Editor]: Diseño editorial, maquetación y jerarquía de encabezados impecables.")

        # 5. Integración Socrática
        if socratic_questions:
            critiques.append(f"💡 [SocraticDebugger]: Se sugieren {len(socratic_questions)} preguntas reflexivas para intercalar.")

        # Calificación global de Coherencia Pedagógica y Editorial
        penalties = len(missing) * 10 + len(warnings) * 15 + len(layout_issues) * 10
        coherence_score = max(0.0, 100.0 - penalties)

        return {
            "coherence_score": round(coherence_score, 1),
            "passed": coherence_score >= 80.0,
            "critiques": critiques,
            "recommendations": recommendations,
            "socratic_questions": socratic_questions
        }


class PedagogicalReviewPipeline:
    """Pipeline que ejecuta la crítica pedagógica y editorial cruzada entre agentes."""

    def __init__(self):
        self.content_auditor = ContentAuditorAgent()
        self.scientist = ScientistAgent()
        self.safety_gate = SafetyGateAgent()
        self.editor = LayoutEditorialAgent()
        self.socratic_debugger = SocraticDebugger()
        self.critic_evaluator = EvaluatorCriticAgent()

    def review_and_auto_fix_lesson(self, lesson_text: str, unit_name: str = "Unidad", auto_fix: bool = True) -> Dict[str, Any]:
        # 1. Auditoría inicial de diseño editorial
        editorial_audit = self.editor.audit_layout(lesson_text)
        
        fixed_text = lesson_text
        if auto_fix and not editorial_audit["passed"]:
            fixed_text = self.editor.auto_fix_layout(lesson_text)
            editorial_audit = self.editor.audit_layout(fixed_text)

        # 2. Auditoría de estructura con ContentAuditorAgent
        content_audit = self.content_auditor.audit_content(fixed_text)

        # 3. Crítica de rigor teórico con @Scientist
        sci_critique = self.scientist.check_theory(fixed_text)

        # 4. Crítica de supuestos y flujo con @Safety_Gate
        safety_critique = self.safety_gate.validate_assumptions(fixed_text, unit_name)

        # 5. Generación de preguntas de reflexión pedagógica con SocraticDebugger
        socratic_questions = []
        if "normal" in fixed_text.lower() or "t-test" in fixed_text.lower():
            socratic_questions.append(self.socratic_debugger.generate_socratic_question("normality", unit_name))
        if "p-valor" in fixed_text.lower() or "p_value" in fixed_text.lower():
            socratic_questions.append(self.socratic_debugger.generate_socratic_question("p_value", unit_name))
        if "varianza" in fixed_text.lower() or "dispersión" in fixed_text.lower():
            socratic_questions.append(self.socratic_debugger.generate_socratic_question("variance", unit_name))

        # 6. Síntesis y debate del EvaluatorCriticAgent
        synthesis = self.critic_evaluator.synthesize_critique(
            content_audit, sci_critique, safety_critique, editorial_audit, socratic_questions
        )

        return {
            "unit_name": unit_name,
            "fixed_text": fixed_text,
            "editorial_audit": editorial_audit,
            "content_audit": content_audit,
            "scientist_critique": sci_critique,
            "safety_gate_critique": safety_critique,
            "synthesis": synthesis,
            "critical_block": safety_critique.get("critical", False),
        }
