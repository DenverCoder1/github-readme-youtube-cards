import codecs
import textwrap
from datetime import datetime, timedelta
from typing import Optional
from urllib.request import Request, urlopen

import i18n
import orjson
from babel.dates import format_timedelta
from babel.numbers import format_compact_decimal

i18n.set("filename_format", "{locale}.{format}")
i18n.set("enable_memoization", True)
i18n.load_path.append("./api/locale")


def format_relative_time(timestamp: float, lang: str = "en") -> str:
    """Get relative time from unix timestamp (ex. "3 hours ago")"""
    delta = timedelta(seconds=timestamp - datetime.now().timestamp())
    return format_timedelta(delta=delta, add_direction=True, locale=lang)


def data_uri_from_bytes(*, data: bytes, mime_type: str) -> str:
    """Return a base-64 data URI for bytes"""
    base64 = codecs.encode(data, "base64").decode("utf-8").replace("\n", "")
    return f"data:{mime_type};base64,{base64}"


def data_uri_from_url(url: str, *, mime_type: Optional[str] = None) -> str:
    """Return base-64 data URI for an image at a given URL.
    If not passed, the content type is determined from the response header
    if present, otherwise, jpeg is assumed.

    Raises:
        HTTPError: If the request fails
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


def trim_lines(text: str, max_length: int, max_lines: int) -> list[str]:
    """Trim text to max_length characters per line, adding ellipsis if necessary"""
    # use textwrap to split into lines
    lines = textwrap.wrap(text, width=max_length)
    # if there are more lines than max_lines, trim the last line and add ellipsis
    if len(lines) > max_lines:
        lines[max_lines - 1] = lines[max_lines - 1][: max_length - 1].strip() + "…"
    return lines[:max_lines]


def parse_metric_value(value: str) -> int:
    """Parse a metric value (ex. "1.2K" => 1200)

    See https://github.com/badges/shields/blob/master/services/text-formatters.js#L56
    for the reverse of this function.
    """
    suffixes = ["k", "M", "G", "T", "P", "E", "Z", "Y"]
    if value[-1] in suffixes:
        return int(float(value[:-1]) * 1000 ** (suffixes.index(value[-1]) + 1))
    return int(value)


def format_views_value(value: str, lang: str = "en") -> str:
    """Format view count, for example "1.2M" => "1.2M views", translations included"""
    int_value = parse_metric_value(value)
    if int_value == 1:
        return i18n.t("view", locale=lang)
    formatted_value = format_compact_decimal(int_value, locale=lang, fraction_digits=1)
    return i18n.t("views", number=formatted_value, locale=lang)


def fetch_views(video_id: str, lang: str = "en") -> str:
    """Get number of views for a YouTube video as a formatted metric"""
    try:
        req = Request(f"https://img.shields.io/youtube/views/{video_id}.json")
        req.add_header("User-Agent", "GitHub Readme YouTube Cards")
        with urlopen(req) as response:
            value = orjson.loads(response.read()).get("value", "")
            return format_views_value(value, lang)
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
