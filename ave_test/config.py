
from pydantic import RedisDsn, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    redis_dsn: RedisDsn = Field("redis://localhost:6379/0")

    model_config = SettingsConfigDict(
        env_prefix="SRV_"
    )