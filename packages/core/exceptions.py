class PolicyEngineError(Exception):
    pass

class InvalidPolicyError(PolicyEngineError):
    pass

class AgentError(PolicyEngineError):
    pass