"""
Pipeline: Orquestador principal del Consejo de 7 Expertos con Loops L1, L2 y L3.
"""

from typing import Dict, Any, List
from .council.architect_agent import ArchitectAgent
from .council.scientist_agent import ScientistAgent
from .council.engineer_agent import EngineerAgent
from .council.safety_gate_agent import SafetyGateAgent
from .council.analyst_agent import AnalystAgent
from .council.librarian_agent import LibrarianAgent
from .council.qa_agent import QAAgent


class CouncilPipeline:
    """Pipeline que coordina la refactorización y auditoría mediante el Consejo de Expertos."""

    def __init__(self):
        self.architect = ArchitectAgent()
        self.scientist = ScientistAgent()
        self.engineer = EngineerAgent()
        self.safety_gate = SafetyGateAgent()
        self.analyst = AnalystAgent()
        self.librarian = LibrarianAgent()
        self.qa = QAAgent()

    def process_content(self, text_or_code: str) -> Dict[str, Any]:
        # 1. Scientist (Teoría y LaTeX)
        sci_res = self.scientist.check_theory(text_or_code)
        
        # 2. Engineer (Código SciPy/Statsmodels)
        eng_res = self.engineer.check_code_implementation(text_or_code)
        
        # 3. Safety Gate (Loop L1: Verificación de Supuestos Estadísticos)
        gate_res = self.safety_gate.validate_assumptions(text_or_code)
        
        # 4. Analyst (Visualizaciones e Interpretación)
        ana_res = self.analyst.audit_visualizations(text_or_code)
        
        # 5. Librarian (Loop L2: Verificación de Literatura)
        lib_res = self.librarian.verify_references(text_or_code)
        
        reports = {
            "scientist": sci_res,
            "engineer": eng_res,
            "safety_gate": gate_res,
            "analyst": ana_res,
            "librarian": lib_res
        }
        
        # 6. QA Agent (Loop L3: Verificación Final del Protocolo Maestro)
        final_qa = self.qa.final_audit(reports)
        
        return {
            "approved": final_qa["approved"],
            "reports": reports,
            "final_qa": final_qa
        }
