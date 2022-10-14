import codecs
from datetime import datetime
from typing import Optional
from urllib.request import Request, urlopen

import i18n
import orjson

i18n.set("filename_format", "{locale}.{format}")
i18n.set("enable_memoization", True)
i18n.load_path.append("./api/locale")


def format_relative_time(date: datetime, lang: str = "en") -> str:
    """Get relative time from datetime (ex. "3 hours ago")"""
    # find time difference in seconds
    seconds_diff = int((datetime.now() - date).total_seconds())
    # number of days in difference
    days_diff = seconds_diff // 86400
    # less than 50 seconds ago
    if seconds_diff < 50:
        return i18n.t("seconds-ago", count=seconds_diff, locale=lang)
    # less than 2 minutes ago
    if seconds_diff < 120:
        return i18n.t("minutes-ago", count=1, locale=lang)
    # less than an hour ago
    if seconds_diff < 3600:
        return i18n.t("minutes-ago", count=seconds_diff // 60, locale=lang)
    # less than 2 hours ago
    if seconds_diff < 7200:
        return i18n.t("hours-ago", count=1, locale=lang)
    # less than 24 hours ago
    if seconds_diff < 86400:
        return i18n.t("hours-ago", count=seconds_diff // 3600, locale=lang)
    # 1 day ago
    if days_diff == 1:
        return i18n.t("days-ago", count=1, locale=lang)
    # less than a month ago
    if days_diff < 30:
        return i18n.t("days-ago", count=days_diff, locale=lang)
    # less than 12 months ago
    if days_diff < 336:
        if round(days_diff / 30.5) == 1:
            return i18n.t("months-ago", count=1, locale=lang)
        return i18n.t("months-ago", count=round(days_diff / 30.5), locale=lang)
    # more than a year ago
    if round(days_diff / 365) == 1:
        return i18n.t("years-ago", count=1, locale=lang)
    return i18n.t("years-ago", count=round(days_diff / 365), locale=lang)


def data_uri_from_bytes(*, data: bytes, mime_type: str) -> str:
    """Return a base-64 data URI for bytes"""
    base64 = codecs.encode(data, "base64").decode("utf-8").replace("\n", "")
    return f"data:{mime_type};base64,{base64}"


def data_uri_from_url(url: str, *, mime_type: Optional[str] = None) -> str:
    """Return base-64 data URI for an image at a given URL.
    If not passed, the content type is determined from the response header
    if present, otherwise, jpeg is assumed.
    """
    with urlopen(url) as response:
        data = response.read()
    mime_type = mime_type or response.headers["Content-Type"] or "image/jpeg"
    assert mime_type is not None
    return data_uri_from_bytes(data=data, mime_type=mime_type)


def data_uri_from_file(path: str, *, mime_type: Optional[str] = None) -> str:
    """Return base-64 data URI for an image at a given file path.
    If not passed, the content type is determined from the file extension
    if present, otherwise, jpeg is assumed.
    """
    with open(path, "rb") as file:
        data = file.read()
    if mime_type is None:
        mime_types = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".gif": "image/gif",
        }
        mime_type = mime_types.get(path[path.rfind(".") :].lower(), "image/jpeg")
    assert mime_type is not None
    return data_uri_from_bytes(data=data, mime_type=mime_type)


def trim_text(text: str, max_length: int) -> str:
    """Trim text to max_length characters, adding ellipsis if necessary"""
    if len(text) <= max_length:
        return text
    return text[: max_length - 1].strip() + "…"


def fetch_views(video_id: str, lang: str = "en") -> str:
    """Get number of views for a YouTube video as a formatted metric"""
    try:
        req = Request(f"https://img.shields.io/youtube/views/{video_id}.json")
        req.add_header("User-Agent", "GitHub Readme YouTube Cards")
        with urlopen(req) as response:
            value = orjson.loads(response.read()).get("value", "")
            # replace G with B for billion and convert to uppercase
            return (
                i18n.t("views", number=value.replace("G", "B").upper(), locale=lang)
                if value
                else ""
            )
    except Exception:
        return ""


def seconds_to_duration(seconds: int) -> str:
    """Convert seconds to a formatted duration (ex. "1:23")"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    if hours:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    return f"{minutes}:{seconds:02d}"


def estimate_duration_width(duration: str) -> int:
    """Estimate width of duration string"""
    num_digits = len([c for c in duration if c.isdigit()])
    num_colons = len([c for c in duration if c == ":"])
    return num_digits * 7 + num_colons * 5 + 8


def is_rtl(lang: str) -> bool:
    """Check if language is to be displayed right-to-left"""
    return i18n.t("direction", locale=lang, default="ltr") == "rtl"
