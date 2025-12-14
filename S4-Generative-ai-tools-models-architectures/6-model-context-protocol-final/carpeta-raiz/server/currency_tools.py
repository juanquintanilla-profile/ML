from fastmcp import tool
from server.api_clients import ExchangeRateClient
from config.settings import EXCHANGE_API_KEY

client = ExchangeRateClient(EXCHANGE_API_KEY)

@tool
def convert_currency(amount: float, base: str, target: str) -> float:
    """Convierte una cantidad entre dos monedas."""
    data = client.get_rates(base.upper())
    if target.upper() not in data["conversion_rates"]:
        raise ValueError("Moneda no soportada")
    return amount * data["conversion_rates"][target.upper()]

@tool
def get_exchange_rates(base: str) -> dict:
    """Devuelve tasas de cambio para una moneda base."""
    return client.get_rates(base.upper())["conversion_rates"]