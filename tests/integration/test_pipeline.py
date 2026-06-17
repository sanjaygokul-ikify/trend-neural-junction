import unittest
from cli.main import main
from services.orchestrator import Orchestrator
from packages.core import PolicyEngine, Policy

class TestPipeline(unittest.TestCase):
    def test_end_to_end(self):
        policies = [Policy('policy1', '{read: true}', 'agent1', ['read'])]
        orchestrator = Orchestrator(policies)
        orchestrator.start()
        # Add assertions for end to end pipeline

if __name__ == '__main__':
    unittest.main()