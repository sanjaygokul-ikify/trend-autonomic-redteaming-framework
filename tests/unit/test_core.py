from ..core import KnowledgeGraph, ThreatModelDB, MetaAgentController
import unittest

class TestCore(unittest.TestCase):
    def test_knowledge_graph(self) -> None:
        graph = KnowledgeGraph([{'target': 'example'}])
        nodes = graph.get_nodes('example')
        self.assertEqual(len(nodes), 1)

    def test_threat_model_db(self) -> None:
        threat_model_db = ThreatModelDB({('action', 'target'): {'effectiveness': 0.5}})
        effectiveness = threat_model_db.get_effectiveness('action', 'target')
        self.assertEqual(effectiveness, 0.5)

    def test_meta_agent_controller(self) -> None:
        knowledge_graph = KnowledgeGraph()
        threat_model_db = ThreatModelDB()
        controller = MetaAgentController(knowledge_graph, threat_model_db)
        plan = controller.plan_attack({"goals": [{"target": "example"}]})
        self.assertIsInstance(plan, list)
