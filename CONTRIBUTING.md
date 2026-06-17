# Contribution Guidelines

## Architecture Review
All changes must pass RFC 001 architecture compliance check

## Policy Implementation

New policies must:
1. Pass 100% coverage tests
2. Comply with the policy interface
3. Include security analysis

## Agent Integration

Submit new agent integrations with:
- 3+ sample sessions
- Fuzz test suite
- Compatibility matrix

## Policy Enforcement

All runtime validation must:
1. Operate in O(1) time complexity
2. Use declarative validation
3. Include monitoring hooks

## Session Management

Session modifications require:
- Vector clock updates
- State consistency guarantees
- Audit trail generation

See [RFC 001](docs/rfcs/001-architecture.md) for detailed design requirements.