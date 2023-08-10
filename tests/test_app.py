import re
from urllib.parse import urlencode


def test_request_no_id(client):
    response = client.get("/")
    data = response.data.decode("utf-8")

    assert response.status_code == 200
    assert "</html>" in data


def test_request_invalid_id(client):
    response = client.get("/?id=**********")
    data = response.data.decode("utf-8")

    assert response.status_code == 400
    assert "&#39;id&#39; expects a video ID but got &#39;**********&#39;" in data


def test_request_unknown_id(client):
    response = client.get("/?id=abc_123-456")
    data = response.data.decode("utf-8")

    assert response.status_code == 404
    assert "Not Found" in data


def test_request_valid_params(client):
    params = {
        "id": "dQw4w9WgXcQ",
        "title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
        "timestamp": "1256450400",
        "background_color": "#000000",
        "title_color": "#111111",
        "stats_color": "#222222",
        "width": "500",
        "border_radius": "10",
        "duration": "211",
        "max_title_lines": "1",
    }
    response = client.get(f"/?{urlencode(params)}")
    data = response.data.decode("utf-8")

    assert response.status_code == 200

    # test views
    views_regex = re.compile(r"\d+(?:\.\d)?[KMBT]? views")
    assert views_regex.search(data) is not None

    # test width
    assert 'width="500"' in data

    # test border radius
    assert 'rx="10"' in data

    # test background color
    assert 'fill="#000000"' in data

    # test title color
    assert 'fill="#111111"' in data

    # test stats color
    assert 'fill="#222222"' in data

    # test title
    assert "Rick Astley - Never Gonna Give You Up (Official Music Video)" in data

    # test duration
    assert "3:31" in data

    # test thumbnail
    thumbnail_regex = re.compile(r'href="data:image/jpeg;base64,[a-zA-Z0-9+/]+={0,2}"')
    assert thumbnail_regex.search(data) is not None

    # test timestamp
    timestamp_regex = re.compile(r"\d+ years ago")
    assert timestamp_regex.search(data) is not None

    # test direction
    assert 'direction="ltr"' in data


def test_request_right_to_left(client):
    params = {
        "id": "dQw4w9WgXcQ",
        "title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
        "timestamp": "1256450400",
        "lang": "he",
    }
    response = client.get(f"/?{urlencode(params)}")
    data = response.data.decode("utf-8")

    # stats group should be 10 pixels from the right
    assert "translate(240, 195)" in data

    # test direction
    assert 'direction="rtl"' in data

    # test views
    views_regex = re.compile(r"\d+(?:\.\d)?[KMBT]?\u200f צפיות")
    assert views_regex.search(data) is not None


def test_max_title_lines(client):
    params = {
        "id": "dQw4w9WgXcQ",
        "title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
        "timestamp": "1256450400",
        "max_title_lines": "2",
    }
    response = client.get(f"/?{urlencode(params)}")
    data = response.data.decode("utf-8")

    assert response.status_code == 200

    assert data.count('<tspan x="0" dy="20px">') == 2
