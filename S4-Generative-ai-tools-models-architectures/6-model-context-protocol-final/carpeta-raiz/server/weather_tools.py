from fastmcp import tool
from server.api_clients import OpenMeteoClient

client = OpenMeteoClient()

@tool
def get_current_weather(latitude: float, longitude: float) -> dict:
    """Clima actual para coordenadas dadas."""
    return client.current_weather(latitude, longitude)["current_weather"]

@tool
def get_weather_forecast(latitude: float, longitude: float) -> dict:
    """Pronóstico del tiempo para varios días."""
    return client.forecast(latitude, longitude)["daily"]