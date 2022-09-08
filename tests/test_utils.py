from datetime import datetime, timedelta
from web.utils import format_metric, format_relative_time, jpeg_data_uri, trim_text


def test_format_metric():
    assert format_metric(0) == "0"
    assert format_metric(105) == "105"
    assert format_metric(1024) == "1K"
    assert format_metric(1224) == "1.2K"
    assert format_metric(10040) == "10K"
    assert format_metric(10240) == "10.2K"
    assert format_metric(1002400) == "1M"
    assert format_metric(1224000) == "1.2M"
    assert format_metric(1224000000) == "1.2B"
    assert format_metric(1224000000000) == "1.2T"


def test_format_relative_time():
    assert format_relative_time(datetime.now()) == "just now"
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


def test_jpeg_data_uri():
    assert jpeg_data_uri("https://i.imgur.com/UyI5EK7.jpg") == (
        "data:image/jpeg;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAIAAAACUFjqAAAAy0lEQVQoFXWOS66FIBAF25a+QIwT\n"
        "R7r/7Th2B2ocEH8BgRZ88b7xrWmlck4xDMM8z1VVaa1zztu2tW17HIcQIqWE3vumabTW1lpE/Hw+\n"
        "IQQhBABIKdEYg4hEFEIoy1IpFWO87/s4jud5xHmezNx1HRHlnMuyTClZa5dleeu6rsdxvK6LiPZ9\n"
        "DyFIKZl5Xdd3u2kaZgYAZjbGhBCISEqZc35r59z/bedcjBEA7vtWShVFQUQ4TZP64r2nL957REwp\n"
        "AUDR9z38Bn+r1/wBmTJ7penrddwAAAAASUVORK5CYII=\n"
    )


def test_trim_text():
    assert trim_text("abcdefghijklmnopqrstuvwxyz", 100) == "abcdefghijklmnopqrstuvwxyz"
    assert trim_text("abcdefghijklmnopqrstuvwxyz", 10) == "abcdefghi…"
    assert trim_text("abcdefghij", 10) == "abcdefghij"
