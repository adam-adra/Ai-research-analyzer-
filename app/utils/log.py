import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api_logger")


def log_request(idea: str, duration_ms: float, engine: str):
    """
    logs the details of the request safely
    """
    logger.info(
        f"Engine: {engine} | Idea Length: {len(idea)} chars | Duration: {duration_ms:.2f}ms"
    )


def log_debug(text: str):
    """
    this is a logger for debug
    """
    logger.info(f"[Debug]: {text}")
