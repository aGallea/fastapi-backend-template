from fastapi import APIRouter, status

from my_app.models import TestPostResponse

router = APIRouter(prefix="/utils", tags=["utils"])


@router.post("/test-request", status_code=status.HTTP_201_CREATED)
def test_post_request() -> TestPostResponse:
    return TestPostResponse(message="Test response")
