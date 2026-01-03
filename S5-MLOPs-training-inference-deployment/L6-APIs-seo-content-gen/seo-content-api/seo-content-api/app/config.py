"""
Configuración de la aplicación y Azure OpenAI.
Carga variables de entorno y proporciona acceso centralizado a la configuración.
"""
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """
    Clase de configuración que carga variables desde .env
    """
    # Azure OpenAI settings
    azure_openai_api_key: str
    azure_openai_endpoint: str
    openai_api_version: str = "2024-02-15-preview"
    deployment_name: str = "gpt-4o"
    
    # API settings
    app_name: str = "SEO Content API"
    app_version: str = "1.0.0"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """
    Retorna una instancia cacheada de Settings.
    El cache evita recargar el archivo .env en cada llamada.
    """
    return Settings()
