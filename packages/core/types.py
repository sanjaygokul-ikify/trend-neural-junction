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

    def __post_init__(self):
        if not self.name:
            raise ValueError('Policy name is required')
        if not self.content:
            raise ValueError('Policy content is required')
        if not self.agent_name:
            raise ValueError('Agent name is required')
        if not self.actions:
            raise ValueError('Policy actions are required')