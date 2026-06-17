from dataclasses import dataclass
from typing import List

@dataclass
class AgentMetadata:
    name: str
    version: str

@dataclass
class Agent:
    metadata: AgentMetadata
    def execute_policy(self, policy: 'Policy'):
        # Execute a policy on this agent
        pass

@dataclass
class Policy:
    name: str
    content: str
    agent_name: str
    actions: List[str]