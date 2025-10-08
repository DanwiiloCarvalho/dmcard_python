from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.orm import DeclarativeBase


class Settings(BaseSettings):
    API_V1_PREFIX: str
    DB_URL: str
    ALGORITHM: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: str

    class DBBaseModel(DeclarativeBase):
        pass

    model_config = SettingsConfigDict(env_file='.env', case_sensitive=True)


settings = Settings()
