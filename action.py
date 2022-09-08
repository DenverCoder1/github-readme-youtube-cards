import time
import urllib.parse
from argparse import ArgumentParser
from typing import Any

import feedparser

BASE_URL = "http://127.0.0.1:8000/web/"


def parse_video(video: dict[str, Any]) -> str:
    """Parse video entry and return the contents for the readme"""
    params = {
        "id": video["yt_videoid"],
        "title": video["title"],
        "timestamp": time.mktime(video["published_parsed"]),
        "views": video["media_statistics"]["views"],
    }
    return f'![{params["title"]}]({BASE_URL}?{urllib.parse.urlencode(params)} "{params["title"]}")'


def parse_videos(channel_id: str, num_videos: int) -> str:
    """Parse video feed and return the contents for the readme"""
    feed = feedparser.parse(f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}")
    videos = feed["entries"][:num_videos]
    return "\n".join(map(parse_video, videos))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-c",
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
    args = parser.parse_args()

    print(parse_videos(args.channel_id, args.max_videos))
