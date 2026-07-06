from ..core import KnowledgeGraph, ThreatModelDB, MetaAgentController
from ..services import Orchestrator
import unittest

class TestPipeline(unittest.TestCase):
    def test_pipeline(self) -> None:
        knowledge_graph = KnowledgeGraph([{'target': 'example'}])
        threat_model_db = ThreatModelDB({('action', 'example'): {'effectiveness': 0.5}})
        controller = MetaAgentController(knowledge_graph, threat_model_db)
        orchestrator = Orchestrator(knowledge_graph, threat_model_db)
        plan = controller.plan_attack({"goals": [{"target": "example"}]})
        self.assertIsInstance(plan, list)
        orchestrator.start()
