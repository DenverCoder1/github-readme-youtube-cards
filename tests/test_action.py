from action import VideoParser

video_parser = VideoParser(
    base_url="https://ytcards.demolab.com/",
    channel_id="UCipSxT7a3rn81vGLw9lqRkg",
    max_videos=6,
    card_width=250,
    background_color="#0d1117",
    title_color="#ffffff",
    stats_color="#dedede",
    youtube_api_key="",
    show_duration=False,
)


def test_parse_iso8601_duration():
    assert video_parser.parse_iso8601_duration("PT30S") == 30
    assert video_parser.parse_iso8601_duration("PT1M10S") == 70
    assert video_parser.parse_iso8601_duration("PT1H2M10S") == 3730
    assert video_parser.parse_iso8601_duration("P1DT2H10M10S") == 94210


def test_parse_video():
    """TODO: Test parsing a video from feedparser video object"""
    pass


def test_parse_videos():
    """TODO: Test parsing a list of videos with feedparser"""
    pass
