from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class AppConfig(BaseSettings):
    # Application
    APP_NAME: str = "BaseKit API"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "local"


    # API
    API_V1_PREFIX: str = "/api/v1"
    
    #Pagination
    PAGE_SIZE: int = 10
    PAGE_SIZE_MAX: int = 100


    # Security
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # CORS
    CORS_ORIGINS: str = "*"


    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


@lru_cache
def get_config() -> AppConfig:
    return AppConfig()


config = get_config()