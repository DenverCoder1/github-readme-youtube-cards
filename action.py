import time
import urllib.parse
from argparse import ArgumentParser
from typing import Any, Dict

import feedparser


class VideoParser:
    def __init__(
        self,
        base_url: str,
        channel_id: str,
        max_videos: int,
        card_width: int,
        background_color: str,
        title_color: str,
        stats_color: str,
    ):
        self._base_url = base_url
        self._channel_id = channel_id
        self._max_videos = max_videos
        self._card_width = card_width
        self._background_color = background_color
        self._title_color = title_color
        self._stats_color = stats_color

    def parse_video(self, video: Dict[str, Any]) -> str:
        """Parse video entry and return the contents for the readme"""
        params = {
            "id": video["yt_videoid"],
            "title": video["title"],
            "timestamp": int(time.mktime(video["published_parsed"])),
            "views": video["media_statistics"]["views"],
            "width": self._card_width,
            "background_color": self._background_color,
            "title_color": self._title_color,
            "stats_color": self._stats_color,
        }
        md = f'[![{params["title"]}]({self._base_url}?{urllib.parse.urlencode(params)} "{params["title"]}")]({params["link"]})'
        return md.replace("/", "\\/")

    def parse_videos(self) -> str:
        """Parse video feed and return the contents for the readme"""
        url = f"https://www.youtube.com/feeds/videos.xml?channel_id={self._channel_id}"
        feed = feedparser.parse(url)
        videos = feed["entries"][: self._max_videos]
        return "\n".join(map(self.parse_video, videos))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--channel",
        dest="channel_id",
        help="YouTube channel ID",
        required=True,
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
        default="https://youtube-cards.onrender.com/",
    )
    parser.add_argument(
        "--card-width",
        dest="card_width",
        help="Card width for the SVG images",
        default=250,
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
    args = parser.parse_args()

    video_parser = VideoParser(
        base_url=args.base_url,
        channel_id=args.channel_id,
        max_videos=args.max_videos,
        card_width=args.card_width,
        background_color=args.background_color,
        title_color=args.title_color,
        stats_color=args.stats_color,
    )

    print(video_parser.parse_videos())
