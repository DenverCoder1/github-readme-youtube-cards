from action import VideoParser


def test_parse_iso8601_duration():
    assert VideoParser.parse_iso8601_duration("PT30S") == 30
    assert VideoParser.parse_iso8601_duration("PT1M10S") == 70
    assert VideoParser.parse_iso8601_duration("PT1H2M10S") == 3730
    assert VideoParser.parse_iso8601_duration("P1DT2H10M10S") == 94210


def test_parse_video():
    """TODO: Test parsing a video from feedparser video object"""
    pass


def test_parse_videos():
    """TODO: Test parsing a list of videos with feedparser"""
    pass
