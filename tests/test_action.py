import os
import re

from action import FileUpdater, VideoParser

video_parser = VideoParser(
    base_url="https://ytcards.demolab.com/",
    channel_id="UCipSxT7a3rn81vGLw9lqRkg",
    lang="en",
    max_videos=6,
    card_width=250,
    border_radius=5,
    background_color="#0d1117",
    title_color="#ffffff",
    stats_color="#dedede",
    youtube_api_key="",
    theme_context_light={},
    theme_context_dark={},
    max_title_lines=1,
    show_duration=False,
    output_type="markdown",
)


def test_parse_iso8601_duration():
    assert VideoParser.parse_iso8601_duration("PT30S") == 30
    assert VideoParser.parse_iso8601_duration("PT1M10S") == 70
    assert VideoParser.parse_iso8601_duration("PT1H2M10S") == 3730
    assert VideoParser.parse_iso8601_duration("P1DT2H10M10S") == 94210


def test_parse_videos():
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
    video_parser._theme_context_light = {
        "background_color": "#ffffff",
        "title_color": "#000000",
        "stats_color": "#000000",
    }
    video_parser._theme_context_dark = {
        "background_color": "#000000",
        "title_color": "#ffffff",
        "stats_color": "#ffffff",
    }
    videos = video_parser.parse_videos()

    assert len(videos.splitlines()) == 6

    line_regex = (
        r"^\[!\[.*\]\(.* \"(.*)\"\)\]\(.*\#gh-dark-mode-only\)"
        r"\[!\[.*\]\(.* \"(.*)\"\)\]\(.*\#gh-light-mode-only\)$"
    )
    assert all(re.match(line_regex, line) for line in videos.splitlines())


def test_parse_videos_html():
    video_parser._output_type = "html"
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
