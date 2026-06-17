import argparse
from services.orchestrator import Orchestrator
from packages.core import Policy

parser = argparse.ArgumentParser(description='Neural Junction CLI')
def main():
    parser.add_argument('--policies', help='Path to policies file', required=True)
    args = parser.parse_args()
    policies = []
    with open(args.policies, 'r') as f:
        for line in f:
            policy = Policy(line.strip(), '', 'agent1', ['read', 'write'])
            policies.append(policy)
    orchestrator = Orchestrator(policies)
    orchestrator.start()

if __name__ == '__main__':
    main()