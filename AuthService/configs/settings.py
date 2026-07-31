from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

from configs.auth import AuthConfig
from configs.cache import CacheConfig
from configs.db import DataBaseConfig


class Settings(BaseSettings):
    db: DataBaseConfig
    cache: CacheConfig
    auth: AuthConfig

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / ".env",
        env_nested_delimiter="__",
    )

@lru_cache(maxsize=128)
def get_settings() -> Settings:
    return Settings()