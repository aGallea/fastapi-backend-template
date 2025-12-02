from fastapi import APIRouter

from my_app.api.routes import health, utils

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(utils.router)
