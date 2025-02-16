from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_key: SecretStr
    db_path: SecretStr
    temp_folder: SecretStr
    templates_folder: SecretStr
    model_config: SettingsConfigDict = SettingsConfigDict (
        env_file="config/.env",
        env_file_encoding="utf-8"
    )


config = Settings()
