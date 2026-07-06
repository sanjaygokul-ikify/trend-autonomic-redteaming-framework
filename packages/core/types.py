from typing import Dict, List

class KnowledgeGraph:
    def __init__(self, nodes: List[Dict] = None):
        self.nodes = nodes if nodes is not None else []

    def get_nodes(self, target: str) -> List[Dict]:
        # Get nodes from the knowledge graph that match the target
        nodes = [node for node in self.nodes if node['target'] == target]
        return nodes

class ThreatModelDB:
    def __init__(self, threat_models: Dict = None):
        self.threat_models = threat_models if threat_models is not None else {}

    def get_effectiveness(self, action: str, target: str) -> float:
        # Get the effectiveness of the action on the target from the threat model database
        if (action, target) in self.threat_models:
            return self.threat_models[(action, target)]['effectiveness']
        else:
            return 0.0