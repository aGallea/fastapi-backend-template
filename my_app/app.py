import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

from my_app.api.main import api_router
from my_app.core.settings import settings

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    logger.info(f"Server is running on {settings.http_host}:{settings.http_port}")
    yield
    # Clean up
    logger.warning("Closing server")


def create_app() -> FastAPI:
    app = FastAPI(
        title="Agentic Shopping Website",
        lifespan=lifespan,
    )
    app.add_middleware(GZipMiddleware, minimum_size=1000)
    app.include_router(api_router, prefix="/api/v1")
    return app
