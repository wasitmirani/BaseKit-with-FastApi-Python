from functools import lru_cache

from pydantic import Field, PostgresDsn, RedisDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


def parse_cors_origins(value: str) -> list[str]:
    return [origin.strip() for origin in value.split(",") if origin.strip()]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    PROJECT_NAME: str = "BaseKit API"
    VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = False
    API_V1_PREFIX: str = "/api/v1"

    SECRET_KEY: str = Field(..., min_length=32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    ALGORITHM: str = "HS256"

    DATABASE_URL: PostgresDsn
    DATABASE_POOL_SIZE: int = 10
    DATABASE_MAX_OVERFLOW: int = 20

    REDIS_URL: RedisDsn | None = None

    CORS_ORIGINS: str = "http://localhost:3000,http://localhost:8000"

    @computed_field
    @property
    def cors_origins_list(self) -> list[str]:
        return parse_cors_origins(self.CORS_ORIGINS)

    SMTP_HOST: str | None = None
    SMTP_PORT: int = 587
    SMTP_USER: str | None = None
    SMTP_PASSWORD: str | None = None
    EMAILS_FROM: str | None = None

    CELERY_BROKER_URL: str | None = None
    CELERY_RESULT_BACKEND: str | None = None

    STORAGE_BUCKET: str | None = None
    STORAGE_REGION: str | None = None

@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
