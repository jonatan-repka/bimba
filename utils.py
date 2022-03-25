import logging
import sys

from google.cloud.logging import Client as GcpLoggingClient


def setup_logger(name):
    try:
        gcp_logging_client = GcpLoggingClient()
        gcp_logging_client.setup_logging()
        gcp_exception = None
    except Exception as exception:
        gcp_exception = exception
    logging.basicConfig(format='[%(asctime)s - %(levelname)s] %(message)s',
                        datefmt="%H:%M:%S",
                        level="INFO")
    logger = logging.getLogger(name)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    if gcp_exception:
        logger.exception("Google Cloud Logging failed to initialize", exc_info=gcp_exception)
    return logger
