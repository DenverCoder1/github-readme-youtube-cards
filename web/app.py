from datetime import datetime
from time import gmtime, strftime

from flask import Flask, render_template, request
from flask.wrappers import Response

from .utils import (
    estimate_duration_width,
    fetch_views,
    format_relative_time,
    jpeg_data_uri,
    seconds_to_duration,
    trim_text,
)
from .validate import validate_color, validate_int, validate_string, validate_video_id

app = Flask(__name__)


@app.route("/")
def render():
    try:
        width = validate_int(request, "width", default=250)
        background_color = validate_color(request, "background_color", default="#0d1117")
        title_color = validate_color(request, "title_color", default="#ffffff")
        stats_color = validate_color(request, "stats_color", default="#dedede")
        title = trim_text(validate_string(request, "title"), (width - 20) // 8)
        publish_timestamp = validate_int(request, "timestamp", default=0)
        duration_seconds = validate_int(request, "duration", default=0)
        video_id = validate_video_id(request, "id", required=True)
        thumbnail = jpeg_data_uri(f"https://i.ytimg.com/vi/{video_id}/mqdefault.jpg")
        views = fetch_views(video_id)
        diff = (
            format_relative_time(datetime.fromtimestamp(int(publish_timestamp)))
            if publish_timestamp
            else ""
        )
        stats = f"{views} • {diff}" if views and diff else (views or diff)
        duration = seconds_to_duration(duration_seconds)
        duration_width = estimate_duration_width(duration)
        response = Response(
            response=render_template(
                "main.svg",
                width=width,
                background_color=background_color,
                title_color=title_color,
                stats_color=stats_color,
                title=title,
                stats=stats,
                thumbnail=thumbnail,
                duration=duration,
                duration_width=duration_width,
            ),
            status=200,
            mimetype="image/svg+xml",
        )
        response.headers["Content-Type"] = "image/svg+xml; charset=utf-8"
        return response
    except Exception as e:
        status = getattr(e, "status", getattr(e, "code", None)) or 400
        return Response(
            response=render_template("error.svg", message=str(e), code=status),
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
