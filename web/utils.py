import codecs
from datetime import datetime
from urllib.request import urlopen


def format_relative_time(date: datetime) -> str:
    """Get relative time from datetime (ex. "3 hours ago")"""
    # find time difference in seconds
    seconds_diff = int((datetime.now() - date).total_seconds())
    # number of days in difference
    days_diff = seconds_diff // 86400
    # less than 5 seconds ago
    if seconds_diff < 5:
        return "just now"
    # less than 50 seconds ago
    if seconds_diff < 50:
        return f"{seconds_diff} seconds ago"
    # less than 2 minutes ago
    if seconds_diff < 120:
        return "1 minute ago"
    # less than an hour ago
    if seconds_diff < 3600:
        return f"{seconds_diff // 60} minutes ago"
    # less than 2 hours ago
    if seconds_diff < 7200:
        return "1 hour ago"
    # less than 24 hours ago
    if seconds_diff < 86400:
        return f"{seconds_diff // 3600} hours ago"
    # 1 day ago
    if days_diff == 1:
        return "1 day ago"
    # less than a month ago
    if days_diff < 30:
        return f"{days_diff} days ago"
    # less than 12 months ago
    if days_diff < 336:
        if round(days_diff / 30.5) == 1:
            return "1 month ago"
        return f"{round(days_diff / 30.5)} months ago"
    # more than a year ago
    if round(days_diff / 365) == 1:
        return "1 year ago"
    return f"{round(days_diff / 365)} years ago"


def format_metric(num: float) -> str:
    """Format number with metric suffix (ex. 1.2K, 1.2M)"""
    units = ["", "K", "M", "B", "T"]
    for unit in units:
        if abs(num) < 1000:
            return f"{num:.1f}{unit}".replace(".0", "")
        num /= 1000
    return f"{round(num)}"


def jpeg_data_uri(url: str) -> str:
    """Return base-64 data URI for jpeg image at a given URL"""
    with urlopen(url) as response:
        return f"data:image/jpeg;base64,{codecs.encode(response.read(), 'base64').decode('utf-8')}"


def trim_text(text: str, max_length: int) -> str:
    """Trim text to max_length characters, adding ellipsis if necessary"""
    if len(text) <= max_length:
        return text
    return text[: max_length - 1].strip() + "…"
