from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from my_app.app import create_app


@pytest.fixture(scope="module")
def client() -> Iterator[TestClient]:
    app = create_app()
    with TestClient(app) as c:
        yield c
