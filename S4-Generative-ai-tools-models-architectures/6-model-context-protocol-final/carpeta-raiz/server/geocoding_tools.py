from fastmcp import tool
from server.api_clients import OpenMeteoClient

client = OpenMeteoClient()

@tool
def geocode_city(city: str) -> dict:
    """Obtiene coordenadas de una ciudad."""
    data = client.geocode(city)
    if "results" not in data:
        raise ValueError("Ciudad no encontrada")
    r = data["results"][0]
    return {
        "city": r["name"],
        "country": r["country"],
        "latitude": r["latitude"],
        "longitude": r["longitude"],
        "timezone": r["timezone"]
    }