import json
import re
import time
import urllib.parse
import urllib.request
from argparse import ArgumentParser
from typing import Any, Dict, Optional

import feedparser


class VideoParser:
    def __init__(
        self,
        base_url: str,
        channel_id: str,
        lang: str,
        max_videos: int,
        card_width: int,
        border_radius: int,
        background_color: str,
        title_color: str,
        stats_color: str,
        youtube_api_key: Optional[str],
        theme_context_light: Dict[str, str],
        theme_context_dark: Dict[str, str],
        max_title_lines: int,
        show_duration: bool,
        output_type: str,
    ):
        self._base_url = base_url
        self._channel_id = channel_id
        self._lang = lang
        self._max_videos = max_videos
        self._card_width = card_width
        self._border_radius = border_radius
        self._background_color = background_color
        self._title_color = title_color
        self._stats_color = stats_color
        self._theme_context_light = theme_context_light
        self._theme_context_dark = theme_context_dark
        self._max_title_lines = max_title_lines
        self._youtube_api_key = youtube_api_key
        self._show_duration = show_duration
        self._output_type = output_type
        self._youtube_data = {}

    @staticmethod
    def parse_iso8601_duration(duration: str) -> int:
        """Parse ISO 8601 duration and return the number of seconds

        Arguments:
            duration (str): The length of the video. The property value is an ISO 8601 duration.
                For example, for a video that is at least one minute long and less than one hour long,
                the duration is in the format PT#M#S, in which the letters PT indicate that the value
                specifies a period of time, and the letters M and S refer to length in minutes and seconds,
                respectively. The # characters preceding the M and S letters are both integers that
                specify the number of minutes (or seconds) of the video. For example, a value of
                PT15M33S indicates that the video is 15 minutes and 33 seconds long.

                If the video is at least one hour long, the duration is in the format PT#H#M#S, in which the
                # preceding the letter H specifies the length of the video in hours and all of the other
                details are the same as described above. If the video is at least one day long,
                the letters P and T are separated, and the value's format is P#DT#H#M#S.
        """
        pattern = re.compile(
            r"P"
            r"(?:(?P<years>\d+)Y)?"
            r"(?:(?P<months>\d+)M)?"
            r"(?:(?P<days>\d+)D)?"
            r"(?:T"
            r"(?:(?P<hours>\d+)H)?"
            r"(?:(?P<minutes>\d+)M)?"
            r"(?:(?P<seconds>\d+)S)?"
            r")?",
        )
        match = re.match(pattern, duration)
        if not match:
            return 0
        data = match.groupdict()
        return (
            int(data["years"] or 0) * 365 * 24 * 60 * 60
            + int(data["months"] or 0) * 30 * 24 * 60 * 60
            + int(data["days"] or 0) * 24 * 60 * 60
            + int(data["hours"] or 0) * 60 * 60
            + int(data["minutes"] or 0) * 60
            + int(data["seconds"] or 0)
        )

    def get_youtube_data(self, *videos: Dict[str, Any]) -> Dict[str, Any]:
        """Fetch video data from the youtube API"""
        if not self._youtube_api_key:
            return {}
        video_ids = [video["yt_videoid"] for video in videos]
        params = {
            "part": "contentDetails",
            "id": ",".join(video_ids),
            "key": self._youtube_api_key,
            "alt": "json",
        }
        url = f"https://youtube.googleapis.com/youtube/v3/videos?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url)
        req.add_header("Accept", "application/json")
        req.add_header("User-Agent", "GitHub Readme YouTube Cards GitHub Action")
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read())
        return {video["id"]: video for video in data["items"]}

    def parse_video(self, video: Dict[str, Any]) -> str:
        """Parse video entry and return the contents for the readme"""
        video_id = video["yt_videoid"]
        params = {
            "id": video_id,
            "title": video["title"],
            "lang": self._lang,
            "timestamp": int(time.mktime(video["published_parsed"])),
            "background_color": self._background_color,
            "title_color": self._title_color,
            "stats_color": self._stats_color,
            "max_title_lines": self._max_title_lines,
            "width": self._card_width,
            "border_radius": self._border_radius,
        }
        if video_id in self._youtube_data:
            content_details = self._youtube_data[video_id]["contentDetails"]
            if self._show_duration:
                params["duration"] = self.parse_iso8601_duration(content_details["duration"])

        dark_params = params | self._theme_context_dark
        light_params = params | self._theme_context_light

        if self._output_type == "html":
            # translate video to html
            html_escaped_title = params["title"].replace('"', "&quot;")
            if self._theme_context_dark or self._theme_context_light:
                return (
                    f'<a href="{video["link"]}">\n'
                    f"  <picture>\n"
                    f'    <source media="(prefers-color-scheme: dark)" srcset="{self._base_url}?{urllib.parse.urlencode(dark_params)}">\n'
                    f'    <img src="{self._base_url}?{urllib.parse.urlencode(light_params)}" alt="{html_escaped_title}" title="{html_escaped_title}">\n'
                    "  </picture>\n"
                    "</a>"
                )
            return f'<a href="{video["link"]}"><img src="{self._base_url}?{urllib.parse.urlencode(params)}" alt="{html_escaped_title}" title="{html_escaped_title}"></a>'
        else:
            # translate video to standard markdown
            backslash_escaped_title = params["title"].replace('"', '\\"')
            # if theme context is set, create two versions with theme context specified
            if self._theme_context_dark or self._theme_context_light:
                return (
                    f'[![{params["title"]}]({self._base_url}?{urllib.parse.urlencode(dark_params)} "{backslash_escaped_title}")]({video["link"]}#gh-dark-mode-only)'
                    f'[![{params["title"]}]({self._base_url}?{urllib.parse.urlencode(light_params)} "{backslash_escaped_title}")]({video["link"]}#gh-light-mode-only)'
                )
            return f'[![{params["title"]}]({self._base_url}?{urllib.parse.urlencode(params)} "{backslash_escaped_title}")]({video["link"]})'

    def parse_videos(self) -> str:
        """Parse video feed and return the contents for the readme"""
        url = f"https://www.youtube.com/feeds/videos.xml?channel_id={self._channel_id}"
        feed = feedparser.parse(url)
        videos = feed["entries"][: self._max_videos]
        self._youtube_data = self.get_youtube_data(*videos)
        return "\n".join(map(self.parse_video, videos))


class FileUpdater:
    """Update the readme file"""

    @staticmethod
    def update(readme_path: str, comment_tag: str, replace_content: str):
        """Replace the text between the begin and end tags with the replace content"""
        begin_tag = f"<!-- BEGIN {comment_tag} -->"
        end_tag = f"<!-- END {comment_tag} -->"
        with open(readme_path, "r") as readme_file:
            readme = readme_file.read()
        begin_index = readme.find(begin_tag)
        end_index = readme.find(end_tag)
        if begin_index == -1 or end_index == -1:
            raise RuntimeError(f"Could not find tags {begin_tag} and {end_tag} in {readme_path}")
        readme = f"{readme[:begin_index + len(begin_tag)]}\n{replace_content}\n{readme[end_index:]}"
        with open(readme_path, "w") as readme_file:
            readme_file.write(readme)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--channel",
        dest="channel_id",
        help="YouTube channel ID",
        required=True,
    )
    parser.add_argument(
        "--lang",
        dest="lang",
        help="Language to be used for card description",
        default="en",
    )
    parser.add_argument(
        "--comment-tag-name",
        dest="comment_tag_name",
        help="Comment tag name",
        default="YOUTUBE-CARDS",
    )
    parser.add_argument(
        "--max-videos",
        dest="max_videos",
        help="Maximum number of videos to include",
        default=6,
        type=int,
    )
    parser.add_argument(
        "--base-url",
        dest="base_url",
        help="Base URL for the readme",
        default="https://ytcards.demolab.com/",
    )
    parser.add_argument(
        "--card-width",
        dest="card_width",
        help="Card width for the SVG images",
        default=250,
        type=int,
    )
    parser.add_argument(
        "--border-radius",
        dest="border_radius",
        help="Card border radius for the SVG images",
        default=5,
        type=int,
    )
    parser.add_argument(
        "--background-color",
        dest="background_color",
        help="Background color for the SVG images",
        default="#0d1117",
    )
    parser.add_argument(
        "--title-color",
        dest="title_color",
        help="Title color for the SVG images",
        default="#ffffff",
    )
    parser.add_argument(
        "--stats-color",
        dest="stats_color",
        help="Stats color for the SVG images",
        default="#dedede",
    )
    parser.add_argument(
        "--theme-context-light",
        dest="theme_context_light",
        help="JSON theme for light mode (keys: background_color, title_color, stats_color)",
        default="{}",
    )
    parser.add_argument(
        "--theme-context-dark",
        dest="theme_context_dark",
        help="JSON theme for dark mode (keys: background_color, title_color, stats_color)",
        default="{}",
    )
    parser.add_argument(
        "--max-title-lines",
        dest="max_title_lines",
        help="Maximum number of lines for the title",
        default=1,
        type=int,
    )
    parser.add_argument(
        "--youtube-api-key",
        dest="youtube_api_key",
        help="YouTube API key",
        default=None,
    )
    parser.add_argument(
        "--show-duration",
        dest="show_duration",
        help="Whether to show the duration of the videos",
        default="false",
        choices=("true", "false"),
    )
    parser.add_argument(
        "--readme-path",
        dest="readme_path",
        help="Path to the readme file",
        default="README.md",
    )
    parser.add_argument(
        "--output-only",
        dest="output_only",
        help="Only output the cards, do not update the readme",
        default="false",
        choices=("true", "false"),
    )
    parser.add_argument(
        "--output-type",
        dest="output_type",
        help="The type of output to be rendered by the action",
        default="markdown",
        choices=("html", "markdown"),
    )
    args = parser.parse_args()

    if args.show_duration == "true" and not args.youtube_api_key:
        parser.error("--youtube-api-key is required when --show-duration is true")

    video_parser = VideoParser(
        base_url=args.base_url,
        channel_id=args.channel_id,
        lang=args.lang,
        max_videos=args.max_videos,
        card_width=args.card_width,
        border_radius=args.border_radius,
        background_color=args.background_color,
        title_color=args.title_color,
        stats_color=args.stats_color,
        theme_context_light=json.loads(args.theme_context_light),
        theme_context_dark=json.loads(args.theme_context_dark),
        max_title_lines=args.max_title_lines,
        youtube_api_key=args.youtube_api_key,
        show_duration=args.show_duration == "true",
        output_type=args.output_type,
    )

    video_content = video_parser.parse_videos()

    # output to stdout
    print(video_content)

    # update the readme file
    if args.output_only == "false":
        FileUpdater.update(args.readme_path, args.comment_tag_name, video_content)
