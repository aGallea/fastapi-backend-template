import logging

from my_app.core.logger import Formatter


def test_formatter_get_level_color() -> None:
    assert Formatter._get_level_color(logging.DEBUG) == "\033[0;34m"
    assert Formatter._get_level_color(logging.INFO) == "\033[0;92m"
    assert Formatter._get_level_color(logging.WARNING) == "\033[0;33m"
    assert Formatter._get_level_color(logging.ERROR) == "\033[0;31m"
    assert Formatter._get_level_color(999) == "\033[0m"


def test_formatter_format() -> None:
    formatter = Formatter()
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname="test.py",
        lineno=10,
        msg="test message",
        args=(),
        exc_info=None,
    )
    formatted_message = formatter.format(record)
    # Check if the message contains the level color and reset
    assert "\033[0;92mINFO\033[0m" in formatted_message
    assert "test message" in formatted_message
    assert "[test.py:10]" in formatted_message
