from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):  # type: ignore[misc]
    log_severity: str = Field(default="INFO", description="Logger severity")
    app_version: str = Field(default="0.0.0", description="Application version")
    http_host: str = Field(default="0.0.0.0", description="Listen address")
    http_port: int = Field(default=8080, description="Listen port")
    timeout_graceful_shutdown: int = Field(
        default=10, description="timeout graceful before shutdown"
    )


settings = Settings()
