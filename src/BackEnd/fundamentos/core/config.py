# app/core/config.py
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    mongodb_url: str = Field(..., env='MONGODB_URL')
    mongodb_db: str = Field(..., env='MONGODB_DB')
    secret_key: str = Field(..., env='SECRET_KEY')
    access_token_expire_minutes: int = Field(30, env='ACCESS_TOKEN_EXPIRE_MINUTES')

    class Config:
        env_file = ".env"

settings = Settings()
