import pytest

from api.validate import (
    ValidationError,
    validate_color,
    validate_int,
    validate_string,
    validate_video_id,
)


def test_validate_int(req):
    # missing field
    assert validate_int(req, "width", default=250) == 250
    # invalid field
    req.set_args(width="abc")
    assert validate_int(req, "width", default=250) == 250
    # valid field
    req.set_args(width="100")
    assert validate_int(req, "width", default=250) == 100


def test_validate_color(req):
    # missing field
    assert validate_color(req, "background_color", default="#0d1117") == "#0d1117"
    # invalid field characters
    req.set_args(background_color="#fghijk")
    assert validate_color(req, "background_color", default="#0d1117") == "#0d1117"
    # invalid field length
    req.set_args(background_color="#012345678")
    assert validate_color(req, "background_color", default="#0d1117") == "#0d1117"
    # valid field - 6 characters
    req.set_args(background_color="#ffffff")
    assert validate_color(req, "background_color", default="#0d1117") == "#ffffff"
    # valid field - 8 characters
    req.set_args(background_color="#01234567")
    assert validate_color(req, "background_color", default="#0d1117") == "#01234567"
    # valid field - 4 characters
    req.set_args(background_color="#89ab")
    assert validate_color(req, "background_color", default="#0d1117") == "#89ab"
    # valid field - 3 characters
    req.set_args(background_color="#cde")
    assert validate_color(req, "background_color", default="#0d1117") == "#cde"


def test_validate_video_id(req):
    # missing field
    with pytest.raises(ValidationError):
        validate_video_id(req, "id")
    # invalid field
    req.set_args(id="*********")
    with pytest.raises(ValidationError):
        validate_video_id(req, "id")
    # valid field
    req.set_args(id="abc_123-456")
    assert validate_video_id(req, "id") == "abc_123-456"


def test_validate_string(req):
    # missing field
    assert validate_string(req, "text", default="Hello, world!") == "Hello, world!"
    # valid field
    req.set_args(text="Hello, world!")
    assert validate_string(req, "text", default="Hello, world!") == "Hello, world!"
