from ..core import MetaAgentController
from ..utils import setup_logging

class Orchestrator:
    def __init__(self, knowledge_graph, threat_model_db):
        self.controller = MetaAgentController(knowledge_graph, threat_model_db)
        setup_logging()

    def start(self) -> None:
        plan = self.controller.plan_attack({"goals": [{"target": "example"}]})
        print(plan)
