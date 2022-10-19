import codecs
from datetime import datetime
from typing import Optional
from urllib.request import Request, urlopen

import i18n
import orjson
from babel import Locale, dates, numbers

i18n.set("filename_format", "{locale}.{format}")
i18n.set("enable_memoization", True)
i18n.load_path.append("./api/locale")


def format_relative_time(date: datetime, lang: str = "en") -> str:
    """Get relative time from datetime (ex. "3 hours ago")"""
    return dates.format_timedelta(delta=date - datetime.now(), add_direction=True, locale=lang)


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


def format_decimal_compact(number: float, lang: str = "en") -> str:
    """Format number with compact notation (ex. "1.2K")

    TODO: This can be refactored once it is supported by Babel
    Sees https://github.com/python-babel/babel/pull/909
    """
    compact = "short"
    compact_format = Locale.parse(lang)._data["compact_decimal_formats"][compact]
    number_format = None
    for magnitude in sorted([int(m) for m in compact_format["other"]], reverse=True):
        if abs(number) >= magnitude:
            compact_other_format = compact_format["other"][str(magnitude)]
            pattern = numbers.parse_pattern(compact_other_format).pattern
            if pattern != "0" and abs(number) >= 1000:
                number_format = compact_other_format
                number = number / (magnitude / (10 ** (pattern.count("0") - 1)))
                if float(number) == 1.0 and "one" in compact_format:
                    number_format = compact_format["one"][str(magnitude)]
            break
    decimal_quantization = True
    if number_format:
        decimal_quantization = False
        number = round(number, 1)
    return numbers.format_decimal(
        number=number,
        format=number_format,
        locale=lang,
        decimal_quantization=decimal_quantization,
    )


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
    formatted_value = format_decimal_compact(int_value, lang=lang)
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
