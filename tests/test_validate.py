import pytest
from api.validate import validate_color, validate_int, validate_string, validate_video_id
from flask.wrappers import Request


class MockRequest(Request):
    def __init__(self, **kwargs):
        self.args = kwargs  # type: ignore


def test_validate_int():
    # missing field
    req = MockRequest()
    assert validate_int(req, "width", default=250) == 250
    # invalid field
    req = MockRequest(width="abc")
    assert validate_int(req, "width", default=250) == 250
    # valid field
    req = MockRequest(width="100")
    assert validate_int(req, "width", default=250) == 100


def test_validate_color():
    # missing field
    req = MockRequest()
    assert validate_color(req, "background_color", default="#0d1117") == "#0d1117"
    # invalid field characters
    req = MockRequest(background_color="#fghijk")
    assert validate_color(req, "background_color", default="#0d1117") == "#0d1117"
    # invalid field length
    req = MockRequest(background_color="#012345678")
    assert validate_color(req, "background_color", default="#0d1117") == "#0d1117"
    # valid field - 6 characters
    req = MockRequest(background_color="#ffffff")
    assert validate_color(req, "background_color", default="#0d1117") == "#ffffff"
    # valid field - 8 characters
    req = MockRequest(background_color="#01234567")
    assert validate_color(req, "background_color", default="#0d1117") == "#01234567"
    # valid field - 4 characters
    req = MockRequest(background_color="#89ab")
    assert validate_color(req, "background_color", default="#0d1117") == "#89ab"
    # valid field - 3 characters
    req = MockRequest(background_color="#cde")
    assert validate_color(req, "background_color", default="#0d1117") == "#cde"


def test_validate_video_id():
    # missing field
    req = MockRequest()
    with pytest.raises(ValueError):
        validate_video_id(req, "id")
    # invalid field
    req = MockRequest(id="<script>alert('xss')</script>")
    with pytest.raises(ValueError):
        validate_video_id(req, "id")
    # valid field
    req = MockRequest(id="abc_123-456")
    assert validate_video_id(req, "id") == "abc_123-456"


def test_validate_string():
    # missing field
    req = MockRequest()
    assert validate_string(req, "text", default="Hello, world!") == "Hello, world!"
    # valid field
    req = MockRequest(text="Hello, world!")
    assert validate_string(req, "text", default="Hello, world!") == "Hello, world!"
