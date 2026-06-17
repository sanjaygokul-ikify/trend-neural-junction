import time
from prometheus_client import Counter

counter = Counter('requests_total', 'Total number of requests')

def setup_metrics():
    counter.inc(1)
    return counter