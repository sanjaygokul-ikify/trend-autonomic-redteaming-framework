from ..core import KnowledgeGraph, ThreatModelDB, MetaAgentController
from ..services import Orchestrator
from ..utils import setup_logging

import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--knowledge-graph', type=str)
    parser.add_argument('--threat-model-db', type=str)
    args = parser.parse_args()

    knowledge_graph = KnowledgeGraph()
    threat_model_db = ThreatModelDB()
    controller = MetaAgentController(knowledge_graph, threat_model_db)
    orchestrator = Orchestrator(knowledge_graph, threat_model_db)

    setup_logging()

    orchestrator.start()

if __name__ == '__main__':
    main()
