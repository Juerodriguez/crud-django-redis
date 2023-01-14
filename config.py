from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    redis_host: str = Field(..., env="REDIS_HOST")
    redis_port: int = Field(..., env="REDIS_PORT")
    redis_password: str = Field(..., env="REDIS_PASSWORD")

    class Config:
        env_file = ".env"
