import logging
from typing import List, Dict
from .types import Policy, Agent, AgentMetadata
from .exceptions import PolicyEngineError, InvalidPolicyError, AgentError

logger = logging.getLogger(__name__)

class PolicyEngine:
    def __init__(self, policies: List[Policy]):
        self.policies = policies
        self.agents: Dict[str, Agent] = {}

    def validate_policy(self, policy: Policy) -> bool:
        try:
            # Validate policy syntax and semantics
            if not self._validate_policy_syntax(policy):
                return False
            if not self._validate_policy_semantics(policy):
                return False
            return True
        except InvalidPolicyError as e:
            logger.error(f"Invalid policy: {e}")
            return False

    def _validate_policy_syntax(self, policy: Policy) -> bool:
        # Check policy syntax (e.g., YAML structure)
        try:
            # Use a YAML parser to check syntax
            import yaml
            yaml.safe_load(policy.content)
            return True
        except yaml.YAMLError as e:
            logger.error(f"Invalid policy syntax: {e}")
            return False

    def _validate_policy_semantics(self, policy: Policy) -> bool:
        # Check policy semantics (e.g., action permissions)
        try:
            # Check if policy actions are valid
            for action in policy.actions:
                if action not in self._get_valid_actions():
                    logger.error(f"Invalid policy action: {action}")
                    return False
            return True
        except Exception as e:
            logger.error(f"Error validating policy semantics: {e}")
            return False

    def _get_valid_actions(self) -> List[str]:
        # Return a list of valid policy actions
        return ["read", "write", "execute"]

    def register_agent(self, agent: Agent):
        try:
            # Register an agent with the policy engine
            self.agents[agent.metadata.name] = agent
            logger.info(f"Registered agent: {agent.metadata.name}")
        except AgentError as e:
            logger.error(f"Error registering agent: {e}")

    def execute_policy(self, policy: Policy):
        try:
            # Execute a policy on registered agents
            for agent_name, agent in self.agents.items():
                if policy.agent_name == agent_name:
                    # Execute policy on matching agent
                    agent.execute_policy(policy)
                    logger.info(f"Executed policy on agent: {agent_name}")
        except PolicyEngineError as e:
            logger.error(f"Error executing policy: {e}")