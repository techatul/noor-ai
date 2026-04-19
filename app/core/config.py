from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class AppConfig(BaseSettings):
    app_name: str = 'Noor AI' 
    app_env: str = 'development'
    GROQ_API_KEY: str
    GROQ_MODEL: str
    APP_API_KEY_NAME: str
    model_config = SettingsConfigDict(env_file='.env')


@lru_cache
def getAppConfig():
    return AppConfig()