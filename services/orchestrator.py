from packages.core import PolicyEngine
from packages.utils.logging import setup_logging

logger = setup_logging()

class Orchestrator:
    def __init__(self, policies):
        self.policy_engine = PolicyEngine(policies)
        self.policies = policies

    def start(self):
        for policy in self.policies:
            if not self.policy_engine.validate_policy(policy):
                logger.error(f'Policy {policy.name} is not valid')
                continue
            self.policy_engine.execute_policy(policy)
        logger.info('Orchestrator started')