from typing import TypedDict


class ReturnHealthcheckStruct(TypedDict):
    status: str


class TestPostResponse(TypedDict):
    message: str
