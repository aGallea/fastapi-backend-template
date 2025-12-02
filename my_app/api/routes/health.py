from fastapi import APIRouter, status

from my_app.models import ReturnHealthcheckStruct

router = APIRouter(prefix="/healthcheck", tags=["healthcheck"])


@router.get(
    "/liveness",
    tags=["healthcheck"],
    summary="Perform a Liveness Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=ReturnHealthcheckStruct,
)
async def liveness() -> ReturnHealthcheckStruct:
    return {"status": "success"}


@router.get(
    "/readiness",
    tags=["healthcheck"],
    summary="Perform a Readiness Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=ReturnHealthcheckStruct,
)
async def readiness() -> ReturnHealthcheckStruct:
    return {"status": "success"}
