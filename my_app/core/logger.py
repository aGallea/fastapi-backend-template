import logging
import sys

from uvicorn.config import LOGGING_CONFIG

from my_app.core.settings import settings


def init_logger() -> None:
    log_handler = logging.StreamHandler(stream=sys.stdout)
    log_handler.setFormatter(Formatter())
    logging.root.addHandler(log_handler)
    logging.root.setLevel(settings.log_severity)
    logging.getLogger("asyncio").setLevel(logging.WARNING)
    logging.getLogger("fastapi").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    LOGGING_CONFIG["loggers"]["uvicorn"]["level"] = "WARN"
    LOGGING_CONFIG["loggers"]["uvicorn.error"]["level"] = "WARN"
    LOGGING_CONFIG["loggers"]["uvicorn.access"]["level"] = "WARN"


class Formatter(logging.Formatter):
    @classmethod
    def _get_level_color(cls, levelno: int) -> str:
        default = "\033[0m"
        return {
            logging.DEBUG: "\033[0;34m",
            logging.INFO: "\033[0;92m",
            logging.WARNING: "\033[0;33m",
            logging.WARN: "\033[0;33m",
            logging.ERROR: "\033[0;31m",
        }.get(levelno, default)

    def format(self, record: logging.LogRecord) -> str:
        record.levelname = (
            f"{self._get_level_color(record.levelno)}{record.levelname}\033[0m"
        )
        log_format = (
            "%(asctime)-15s %(levelname)-18.18s %(message)s [%(filename)s:%(lineno)d]"
        )

        formatter = logging.Formatter(log_format)
        return formatter.format(record)
