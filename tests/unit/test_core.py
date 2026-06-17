import unittest
from packages.core import PolicyEngine, Policy, AgentMetadata, Agent

class TestPolicyEngine(unittest.TestCase):
    def test_validate_policy(self):
        policy = Policy('policy1', '{read: true}', 'agent1', ['read'])
        policy_engine = PolicyEngine([policy])
        self.assertTrue(policy_engine.validate_policy(policy))

    def test_execute_policy(self):
        class TestAgent(Agent):
            def execute_policy(self, policy):
                self.policy = policy
        policy = Policy('policy1', '{read: true}', 'agent1', ['read'])
        agent_metadata = AgentMetadata('agent1', '1.0')
        agent = TestAgent(agent_metadata)
        policy_engine = PolicyEngine([policy])
        policy_engine.register_agent(agent)
        policy_engine.execute_policy(policy)
        self.assertEqual(agent.policy, policy)

if __name__ == '__main__':
    unittest.main()