import logging

import uvicorn

from my_app.app import create_app
from my_app.core.logger import init_logger
from my_app.core.settings import settings

logger = logging.getLogger(__name__)


def main() -> None:
    init_logger()
    app = create_app()
    logger.info("Starting server")

    uvicorn.run(
        app,
        host=settings.http_host,
        port=settings.http_port,
        timeout_graceful_shutdown=settings.timeout_graceful_shutdown,
    )


if __name__ == "__main__":
    main()
