from unittest.mock import MagicMock, patch

from my_app.__main__ import main


@patch("my_app.__main__.uvicorn.run")
@patch("my_app.__main__.create_app")
@patch("my_app.__main__.init_logger")
def test_main(
    mock_init_logger: MagicMock,
    mock_create_app: MagicMock,
    mock_uvicorn_run: MagicMock,
) -> None:
    main()
    mock_init_logger.assert_called_once()
    mock_create_app.assert_called_once()
    mock_uvicorn_run.assert_called_once()
