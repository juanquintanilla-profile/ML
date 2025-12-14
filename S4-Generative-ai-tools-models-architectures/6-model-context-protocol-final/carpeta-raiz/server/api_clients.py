import requests

class ExchangeRateClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_rates(self, base: str) -> dict:
        url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/{base}"
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.json()

class OpenMeteoClient:
    def geocode(self, city: str) -> dict:
        url = "https://geocoding-api.open-meteo.com/v1/search"
        r = requests.get(url, params={"name": city, "count": 1}, timeout=10)
        r.raise_for_status()
        return r.json()

    def current_weather(self, lat: float, lon: float) -> dict:
        url = "https://api.open-meteo.com/v1/forecast"
        r = requests.get(url, params={
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        }, timeout=10)
        r.raise_for_status()
        return r.json()

    def forecast(self, lat: float, lon: float) -> dict:
        url = "https://api.open-meteo.com/v1/forecast"
        r = requests.get(url, params={
            "latitude": lat,
            "longitude": lon,
            "daily": "temperature_2m_max,temperature_2m_min",
            "timezone": "auto"
        }, timeout=10)
        r.raise_for_status()
        return r.json()