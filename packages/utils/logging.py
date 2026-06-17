import logging

def setup_logging(log_level='INFO'):
    logging.basicConfig(level=getattr(logging, log_level))
    return logging.getLogger(__name__)