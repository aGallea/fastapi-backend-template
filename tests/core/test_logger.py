import logging
from unittest.mock import MagicMock, patch

from my_app.core.logger import Formatter, init_logger


@patch("my_app.core.logger.logging")
def test_init_logger(mock_logging: MagicMock) -> None:
    # Setup mocks
    mock_root = MagicMock()
    mock_logging.root = mock_root
    mock_handler = MagicMock()
    mock_logging.StreamHandler.return_value = mock_handler

    # Call the function
    init_logger()

    # Assertions
    mock_logging.StreamHandler.assert_called_once()
    mock_handler.setFormatter.assert_called_once()
    mock_root.addHandler.assert_called_with(mock_handler)
    mock_root.setLevel.assert_called()

    # Check if other loggers levels were set
    mock_logging.getLogger.assert_any_call("asyncio")
    mock_logging.getLogger.assert_any_call("fastapi")
    mock_logging.getLogger.assert_any_call("httpx")
    mock_logging.getLogger.assert_any_call("httpcore")


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
