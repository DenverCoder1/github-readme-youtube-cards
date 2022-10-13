import re
from datetime import datetime, timedelta

from api.utils import (
    estimate_duration_width,
    fetch_views,
    format_relative_time,
    data_uri_from_url,
    data_uri_from_file,
    seconds_to_duration,
    trim_text,
)


def test_fetch_views():
    metric_regex = re.compile(r"^\d+(?:\.\d)?[KMBT]? views$")
    assert metric_regex.match(fetch_views("dQw4w9WgXcQ"))


def test_format_relative_time():
    assert format_relative_time(datetime.now() - timedelta(seconds=1)) == "1 second ago"
    assert format_relative_time(datetime.now() - timedelta(seconds=5)) == "5 seconds ago"
    assert format_relative_time(datetime.now() - timedelta(seconds=50)) == "1 minute ago"
    assert format_relative_time(datetime.now() - timedelta(seconds=110)) == "1 minute ago"
    assert format_relative_time(datetime.now() - timedelta(minutes=1)) == "1 minute ago"
    assert format_relative_time(datetime.now() - timedelta(minutes=2)) == "2 minutes ago"
    assert format_relative_time(datetime.now() - timedelta(minutes=60)) == "1 hour ago"
    assert format_relative_time(datetime.now() - timedelta(hours=1)) == "1 hour ago"
    assert format_relative_time(datetime.now() - timedelta(hours=2)) == "2 hours ago"
    assert format_relative_time(datetime.now() - timedelta(hours=24)) == "1 day ago"
    assert format_relative_time(datetime.now() - timedelta(days=1)) == "1 day ago"
    assert format_relative_time(datetime.now() - timedelta(days=2)) == "2 days ago"
    assert format_relative_time(datetime.now() - timedelta(days=30)) == "1 month ago"
    assert format_relative_time(datetime.now() - timedelta(days=31)) == "1 month ago"
    assert format_relative_time(datetime.now() - timedelta(days=60)) == "2 months ago"
    assert format_relative_time(datetime.now() - timedelta(days=335)) == "11 months ago"
    assert format_relative_time(datetime.now() - timedelta(days=365)) == "1 year ago"
    assert format_relative_time(datetime.now() - timedelta(days=366)) == "1 year ago"
    assert format_relative_time(datetime.now() - timedelta(days=730)) == "2 years ago"

def test_format_relative_time_i18n():
    lang = "fr"
    assert format_relative_time(datetime.now() - timedelta(seconds=1), lang=lang) == "il y a 1 seconde"
    assert format_relative_time(datetime.now() - timedelta(seconds=5), lang=lang) == "il y a 5 secondes"
    assert format_relative_time(datetime.now() - timedelta(minutes=1), lang=lang) == "il y a 1 minute"
    assert format_relative_time(datetime.now() - timedelta(minutes=2), lang=lang) == "il y a 2 minutes"
    assert format_relative_time(datetime.now() - timedelta(hours=1), lang=lang) == "il y a 1 heure"
    assert format_relative_time(datetime.now() - timedelta(hours=2), lang=lang) == "il y a 2 heures"
    assert format_relative_time(datetime.now() - timedelta(days=1), lang=lang) == "il y a 1 jour"
    assert format_relative_time(datetime.now() - timedelta(days=2), lang=lang) == "il y a 2 jours"
    assert format_relative_time(datetime.now() - timedelta(days=30), lang=lang) == "il y a 1 mois"
    assert format_relative_time(datetime.now() - timedelta(days=60), lang=lang) == "il y a 2 mois"
    assert format_relative_time(datetime.now() - timedelta(days=365), lang=lang) == "il y a 1 an"
    assert format_relative_time(datetime.now() - timedelta(days=730), lang=lang) == "il y a 2 ans"


def test_data_uri_from_url_and_file():
    expected = (
        "data:image/jpeg;base64,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"
        "ko/3B2oPu5UDUoz3Plf5giIv/B//2Q=="
    )
    assert data_uri_from_url("https://i.imgur.com/Dh1cOVG.jpg") == expected
    assert data_uri_from_file("./api/templates/resources/error.jpg") == expected


def test_trim_text():
    assert trim_text("abcdefghijklmnopqrstuvwxyz", 100) == "abcdefghijklmnopqrstuvwxyz"
    assert trim_text("abcdefghijklmnopqrstuvwxyz", 10) == "abcdefghi…"
    assert trim_text("abcdefghij", 10) == "abcdefghij"


def test_seconds_to_duration():
    assert seconds_to_duration(0) == "0:00"
    assert seconds_to_duration(1) == "0:01"
    assert seconds_to_duration(60) == "1:00"
    assert seconds_to_duration(61) == "1:01"
    assert seconds_to_duration(3600) == "1:00:00"
    assert seconds_to_duration(3601) == "1:00:01"
    assert seconds_to_duration(3661) == "1:01:01"


def test_estimate_duration_width():
    assert estimate_duration_width("1:00") == 34
    assert estimate_duration_width("10:00") == 41
    assert estimate_duration_width("1:00:00") == 53
    assert estimate_duration_width("10:00:00") == 60
