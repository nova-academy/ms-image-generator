"""Module providing base class and utilities for config"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Class representing my app config"""
    app_name: str
    app_version: str
    openai_api_key: str
    ai_model: str

    model_config = SettingsConfigDict(env_file=".env")
