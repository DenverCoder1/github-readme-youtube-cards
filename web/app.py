from datetime import datetime

from flask import Flask, render_template, request
from flask.wrappers import Response

from .utils import format_metric, format_relative_time, jpeg_data_uri, trim_text
from .validate import validate_color, validate_int, validate_string, validate_video_id

app = Flask(__name__)


@app.route("/")
def render():
    try:
        width = validate_int(request, "width", default=250)
        background_color = validate_color(request, "background_color", default="#0d1117")
        title_color = validate_color(request, "title_color", default="#ffffff")
        stats_color = validate_color(request, "stats_color", default="#dedede")
        title = trim_text(validate_string(request, "title"), (width - 32) // 8)
        views = validate_int(request, "views", default=-1)
        views = format_metric(views) if views >= 0 else None
        publish_timestamp = validate_int(request, "timestamp", default=0)
        publish_datetime = (
            datetime.fromtimestamp(int(publish_timestamp)) if publish_timestamp else None
        )
        diff = format_relative_time(publish_datetime) if publish_datetime else None
        video_id = validate_video_id(request, "id", required=True)
        thumbnail = jpeg_data_uri(f"https://i.ytimg.com/vi/{video_id}/mqdefault.jpg")
        stats = f"{views} views • {diff}" if views and diff else ""
        if views and not diff:
            stats = f"{views} views"
        if diff and not views:
            stats = diff
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
            ),
            status=200,
            mimetype="image/svg+xml",
        )
        response.headers["Content-Type"] = "image/svg+xml; charset=utf-8"
        return response
    except Exception as e:
        return f"Error: {e}"
