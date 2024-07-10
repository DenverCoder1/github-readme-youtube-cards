import os
import re

from action import FileUpdater, VideoParser


def create_video_parser(**kwargs):
    return VideoParser(
        base_url=kwargs.get("base_url", "https://ytcards.demolab.com/"),
        channel_id=kwargs.get("channel_id", "UCipSxT7a3rn81vGLw9lqRkg"),
        playlist_id=kwargs.get("playlist_id", None),
        lang=kwargs.get("lang", "en"),
        max_videos=kwargs.get("max_videos", 6),
        card_width=kwargs.get("card_width", 250),
        border_radius=kwargs.get("border_radius", 5),
        background_color=kwargs.get("background_color", "#0d1117"),
        title_color=kwargs.get("title_color", "#ffffff"),
        stats_color=kwargs.get("stats_color", "#dedede"),
        youtube_api_key=kwargs.get("youtube_api_key", ""),
        theme_context_light=kwargs.get("theme_context_light", {}),
        theme_context_dark=kwargs.get("theme_context_dark", {}),
        max_title_lines=kwargs.get("max_title_lines", 1),
        show_duration=kwargs.get("show_duration", False),
        output_type=kwargs.get("output_type", "markdown"),
    )


def test_parse_iso8601_duration():
    assert VideoParser.parse_iso8601_duration("PT30S") == 30
    assert VideoParser.parse_iso8601_duration("PT1M10S") == 70
    assert VideoParser.parse_iso8601_duration("PT1H2M10S") == 3730
    assert VideoParser.parse_iso8601_duration("P1DT2H10M10S") == 94210


def test_parse_videos():
    video_parser = create_video_parser()
    videos = video_parser.parse_videos()

    assert len(videos.splitlines()) == 6

    line_regex = r"^\[!\[.*\]\(.* \"(.*)\"\)\]\(.*\)$"
    assert all(re.match(line_regex, line) for line in videos.splitlines())

    assert "https://ytcards.demolab.com/?id=" in videos
    assert "title=" in videos
    assert "timestamp=" in videos
    assert "background_color=" in videos
    assert "title_color=" in videos
    assert "stats_color=" in videos
    assert "width=" in videos
    assert "border_radius=" in videos


def test_parse_videos_with_theme_context():
    video_parser = create_video_parser(
        theme_context_light={
            "background_color": "#ffffff",
            "title_color": "#000000",
            "stats_color": "#000000",
        },
        theme_context_dark={
            "background_color": "#000000",
            "title_color": "#ffffff",
            "stats_color": "#ffffff",
        },
    )
    videos = video_parser.parse_videos()

    assert len(videos.splitlines()) == 6

    line_regex = (
        r"^\[!\[.*\]\(.* \"(.*)\"\)\]\(.*\#gh-dark-mode-only\)"
        r"\[!\[.*\]\(.* \"(.*)\"\)\]\(.*\#gh-light-mode-only\)$"
    )
    assert all(re.match(line_regex, line) for line in videos.splitlines())


def test_parse_videos_html():
    video_parser = create_video_parser(output_type="html")
    videos = video_parser.parse_videos()

    assert len(videos.splitlines()) == 6

    line_regex = r"<a href=\".*\"><img src=\".*\" [^>]*></a>"
    assert all(re.match(line_regex, line) for line in videos.splitlines())


def test_parse_videos_html_theme_context():
    video_parser = create_video_parser(
        theme_context_light={
            "background_color": "#ffffff",
            "title_color": "#000000",
            "stats_color": "#000000",
        },
        theme_context_dark={
            "background_color": "#000000",
            "title_color": "#ffffff",
            "stats_color": "#ffffff",
        },
        output_type="html",
    )
    videos = video_parser.parse_videos()

    assert len(videos.splitlines()) == 36

    anchor_tag_regex = r"<a href=\".*\">"
    picture_tag_regex = r"</?picture>"
    img_tag_regex = f'<img src="{video_parser._base_url}.*" alt=".*">'
    assert all(re.match(anchor_tag_regex, line) for line in videos.splitlines()[::6])
    assert all(re.match(picture_tag_regex, line.strip()) for line in videos.splitlines()[1::3])
    assert all(re.match(img_tag_regex, line.strip()) for line in videos.splitlines()[3::6])

    assert "https://ytcards.demolab.com/?id=" in videos
    assert "title=" in videos
    assert "timestamp=" in videos
    assert "background_color=" in videos
    assert "title_color=" in videos
    assert "stats_color=" in videos
    assert "width=" in videos
    assert "border_radius=" in videos
    assert "max_title_lines=" in videos


def test_playlist_id():
    video_parser = create_video_parser(
        channel_id=None, playlist_id="PL9YUC9AZJGFFAErr_ZdK2FV7sklMm2K0J"
    )
    videos = video_parser.parse_videos()

    assert len(videos.splitlines()) == 6

    line_regex = r"^\[!\[.*\]\(.* \"(.*)\"\)\]\(.*\)$"
    assert all(re.match(line_regex, line) for line in videos.splitlines())


def test_update_file():
    path = "./tests/README.md"
    # create a file to test with
    with open(path, "w+") as f:
        f.write(
            "Test Before\n"
            "\n"
            "<!-- BEGIN YOUTUBE-CARDS -->\n"
            "<!-- END YOUTUBE-CARDS -->\n"
            "\n"
            "Test After\n"
        )
    try:
        # update the file
        FileUpdater.update(path, "YOUTUBE-CARDS", "A\nB\nC")
        # read the file and assert the contents
        with open(path, "r") as f:
            assert f.read() == (
                "Test Before\n"
                "\n"
                "<!-- BEGIN YOUTUBE-CARDS -->\n"
                "A\n"
                "B\n"
                "C\n"
                "<!-- END YOUTUBE-CARDS -->\n"
                "\n"
                "Test After\n"
            )
    finally:
        # remove the file
        os.remove(path)
