from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mongo_connection_string: str

    model_config = SettingsConfigDict(env_file=".env")


"""
Construct settings with model_validate to avoid type error
due to the fact that required fields loaded from .env are do not
cause an error when they are not passed in to the constructor.
https://github.com/pydantic/pydantic/issues/3753
"""
settings = Settings.model_validate({})
