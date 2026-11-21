from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_ENV: str
    APP_DEBUG: bool
    FIPE_API_URL: str
    FIPE_API_TIMEOUT: float

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


config = Settings()