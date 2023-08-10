from datetime import datetime
from time import gmtime, strftime

from flask import Flask, render_template, request
from flask.wrappers import Response

from .utils import (
    data_uri_from_file,
    data_uri_from_url,
    estimate_duration_width,
    fetch_views,
    format_relative_time,
    is_rtl,
    seconds_to_duration,
    trim_lines,
)
from .validate import (
    validate_color,
    validate_int,
    validate_lang,
    validate_string,
    validate_video_id,
)

app = Flask(__name__)

# enable jinja2 autoescape for all files including SVG files
app.jinja_options["autoescape"] = True


@app.route("/")
def render():
    try:
        if "id" not in request.args:
            now = datetime.utcnow()
            return Response(response=render_template("index.html", now=now))
        video_id = validate_video_id(request, "id")
        width = validate_int(request, "width", default=250)
        border_radius = validate_int(request, "border_radius", default=5)
        background_color = validate_color(request, "background_color", default="#0d1117")
        title_color = validate_color(request, "title_color", default="#ffffff")
        stats_color = validate_color(request, "stats_color", default="#dedede")
        title = validate_string(request, "title", default="")
        max_title_lines = validate_int(request, "max_title_lines", default=1)
        title_lines = trim_lines(title, (width - 20) // 8, max_title_lines)
        publish_timestamp = validate_int(request, "timestamp", default=0)
        duration_seconds = validate_int(request, "duration", default=0)
        lang = validate_lang(request, "lang", default="en")
        thumbnail = data_uri_from_url(f"https://i.ytimg.com/vi/{video_id}/mqdefault.jpg")
        views = fetch_views(video_id, lang)
        diff = format_relative_time(publish_timestamp, lang) if publish_timestamp else ""
        stats = f"{views}\u2002•\u2002{diff}" if views and diff else (views or diff)
        duration = seconds_to_duration(duration_seconds)
        duration_width = estimate_duration_width(duration)
        thumbnail_height = round(width * 0.56)
        title_line_height = 20
        title_height = len(title_lines) * title_line_height
        height = thumbnail_height + title_height + 60
        response = Response(
            response=render_template(
                "main.svg",
                width=width,
                height=height,
                title_line_height=title_line_height,
                title_height=title_height,
                background_color=background_color,
                title_color=title_color,
                stats_color=stats_color,
                title_lines=title_lines,
                stats=stats,
                thumbnail=thumbnail,
                duration=duration,
                duration_width=duration_width,
                border_radius=border_radius,
                rtl=is_rtl(lang),
            ),
            status=200,
            mimetype="image/svg+xml",
        )
        response.headers["Content-Type"] = "image/svg+xml; charset=utf-8"
        return response
    except Exception as e:
        status = getattr(e, "status", 500)
        thumbnail = data_uri_from_file("./api/templates/resources/error.jpg")
        return Response(
            response=render_template("error.svg", message=str(e), code=status, thumbnail=thumbnail),
            status=status,
            mimetype="image/svg+xml",
        )


@app.after_request
def add_header(r):
    """Add headers to cache the response no longer than an hour."""
    r.headers["Expires"] = strftime(
        "%a, %d %b %Y %H:%M:%S GMT", gmtime(datetime.now().timestamp() + 3600)
    )
    r.headers["Last-Modified"] = strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
    r.headers["Cache-Control"] = "public, max-age=3600"
    return r
