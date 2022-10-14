import pytest
from flask.wrappers import Request

from api.index import app


@pytest.fixture()
def client():
    """A test client for the app"""
    return app.test_client()


class MockRequest(Request):
    """Mock request object for testing"""

    def __init__(self, **kwargs):
        self.args = kwargs  # type: ignore

    def set_args(self, **kwargs):
        self.args = kwargs  # type: ignore

    def update_args(self, **kwargs):
        self.args.update(kwargs)


@pytest.fixture()
def req():
    """Mock request object for testing with no arguments"""
    return MockRequest()
