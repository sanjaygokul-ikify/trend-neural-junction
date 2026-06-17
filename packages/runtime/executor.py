import logging
from typing import List
from ..core.engine import PolicyEngine
from ..core.types import Policy

logger = logging.getLogger(__name__)

class Executor:
    def __init__(self, policies: List[Policy]):
        self.policy_engine = PolicyEngine(policies)
        self.running_policies: List[Policy] = []

    def start_execution(self):
        try:
            # Start executing policies
            for policy in self.policy_engine.policies:
                self.running_policies.append(policy)
                self.policy_engine.execute_policy(policy)
                logger.info(f"Started executing policy: {policy.name}")
        except Exception as e:
            logger.error(f"Error starting execution: {e}")

    def stop_execution(self, policy_name: str):
        try:
            # Stop executing a policy
            for policy in self.running_policies:
                if policy.name == policy_name:
                    # Remove policy from running policies
                    self.running_policies.remove(policy)
                    logger.info(f"Stopped executing policy: {policy_name}")
                    return
            logger.error(f"Policy not found: {policy_name}")
        except Exception as e:
            logger.error(f"Error stopping execution: {e}")