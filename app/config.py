from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Ai researcher"
    model_name: str = "openrouter/google/gemini-2.0-flash-lite-preview-02-05:free"
    openai_api_key: str | None = None
    anthropic_api_key: str | None = None
    openrouter_api_key: str | None = None
    serper_api_key: str | None = None
    tavily_api_key: str | None = None
    use_real_crew: bool = False
    request_timeout_seconds: int = 120
    gemini_api_key: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", frozen=True, extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    """Returns a cached instance of the Settings object."""
    return Settings()
