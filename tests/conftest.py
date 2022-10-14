import pytest

from api import app


@pytest.fixture()
def client():
    return app.test_client()
