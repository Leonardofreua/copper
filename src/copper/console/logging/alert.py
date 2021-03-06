import logging

from .io_formatter import IOFormatter

logger = logging.getLogger(__name__)


class Alert:
    def __init__(self) -> None:
        handler = logging.StreamHandler()
        handler.setFormatter(IOFormatter())
        logger.addHandler(handler)

    def error(self, message: str) -> None:
        logger.error(f"\n{message}")

    def info(self, message: str) -> None:
        logger.setLevel(logging.INFO)
        logger.info(f"\n{message}")

    def warning(self, message: str) -> None:
        logger.warning(f"\n{message}")

    def help(self) -> None:
        logger.setLevel(logging.INFO)
        logger.info("Type [COMMAND] -h for help.\n")
