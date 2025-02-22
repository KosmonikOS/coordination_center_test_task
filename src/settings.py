from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, field_validator
from pathlib import Path
from typing import Optional


class Settings(BaseSettings):
    """
    Settings for the application, loaded from environment variables.
    """

    openai_api_key: str
    openai_base_url: Optional[str] = None
    openai_model: str
    openai_temperature: float = 0.0
    template_path: str
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    @field_validator("template_path")
    def get_absolute_template_path(cls, v):
        """Convert template path to absolute path relative to project root."""
        project_root = Path(__file__).parent.parent
        return str(project_root / v)


settings = Settings()
