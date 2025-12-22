import logfire
import logging
import finnhub
from fastmcp import FastMCP
from fastmcp.utilities.logging import get_logger

from typing import Union, Literal
logger = get_logger(__name__)

MetricType = Literal[
    "10DayAverageTradingVolume",
    "13WeekPriceReturnDaily",
    "26WeekPriceReturnDaily",
    "3MonthADReturnStd",
    "3MonthAverageTradingVolume",
    "52WeekHigh",
    "52WeekHighDate",
    "52WeekLow",
    "52WeekLowDate",
    "52WeekPriceReturnDaily",
    "5DayPriceReturnDaily",
    "assetTurnoverAnnual",
    "assetTurnoverTTM",
    "beta",
    "bookValuePerShareAnnual",
    "bookValuePerShareQuarterly",
    "bookValueShareGrowth5Y",
    "capexCagr5Y",
    "cashFlowPerShareAnnual",
    "cashFlowPerShareQuarterly",
    "cashFlowPerShareTTM",
    "cashPerSharePerShareAnnual",
    "cashPerSharePerShareQuarterly",
    "currentDividendYieldTTM",
    "currentEv/freeCashFlowAnnual",
    "currentEv/freeCashFlowTTM",
    "currentRatioAnnual",
    "currentRatioQuarterly",
    "dividendGrowthRate5Y",
    "dividendPerShareAnnual",
    "dividendPerShareTTM",
    "dividendYieldIndicatedAnnual",
    "ebitdPerShareAnnual",
    "ebitdPerShareTTM",
    "ebitdaCagr5Y",
    "ebitdaInterimCagr5Y",
    "enterpriseValue",
    "epsAnnual",
    "epsBasicExclExtraItemsAnnual",
    "epsBasicExclExtraItemsTTM",
    "epsExclExtraItemsAnnual",
    "epsExclExtraItemsTTM",
    "epsGrowth3Y",
    "epsGrowth5Y",
    "epsGrowthQuarterlyYoy",
    "epsGrowthTTMYoy",
    "epsInclExtraItemsAnnual",
    "epsInclExtraItemsTTM",
    "epsNormalizedAnnual",
    "epsTTM",
    "focfCagr5Y",
    "forwardPE",
    "grossMargin5Y",
    "grossMarginAnnual",
    "grossMarginTTM",
    "inventoryTurnoverAnnual",
    "inventoryTurnoverTTM",
    "longTermDebt/equityAnnual",
    "longTermDebt/equityQuarterly",
    "marketCapitalization",
    "monthToDatePriceReturnDaily",
    "netIncomeEmployeeAnnual",
    "netIncomeEmployeeTTM",
    "netInterestCoverageAnnual",
    "netInterestCoverageTTM",
    "netMarginGrowth5Y",
    "netProfitMargin5Y",
    "netProfitMarginAnnual",
    "netProfitMarginTTM",
    "operatingMargin5Y",
    "operatingMarginAnnual",
    "operatingMarginTTM",
    "payoutRatioAnnual",
    "payoutRatioTTM",
    "pb",
    "pbAnnual",
    "pbQuarterly",
    "pcfShareAnnual",
    "pcfShareTTM",
    "peAnnual",
    "peBasicExclExtraTTM",
    "peExclExtraAnnual",
    "peExclExtraTTM",
    "peInclExtraTTM",
    "peNormalizedAnnual",
    "peTTM",
    "pegTTM",
    "pfcfShareAnnual",
    "pfcfShareTTM",
    "pretaxMargin5Y",
    "pretaxMarginAnnual",
    "pretaxMarginTTM",
    "priceRelativeToS&P50013Week",
    "priceRelativeToS&P50026Week",
    "priceRelativeToS&P5004Week",
    "priceRelativeToS&P50052Week",
    "priceRelativeToS&P500Ytd",
    "psAnnual",
    "psTTM",
    "ptbvAnnual",
    "ptbvQuarterly",
    "quickRatioAnnual",
    "quickRatioQuarterly",
    "receivablesTurnoverAnnual",
    "receivablesTurnoverTTM",
    "revenueEmployeeAnnual",
    "revenueEmployeeTTM",
    "revenueGrowth3Y",
    "revenueGrowth5Y",
    "revenueGrowthQuarterlyYoy",
    "revenueGrowthTTMYoy",
    "revenuePerShareAnnual",
    "revenuePerShareTTM",
    "revenueShareGrowth5Y",
    "roa5Y",
    "roaRfy",
    "roaTTM",
    "roe5Y",
    "roeRfy",
    "roeTTM",
    "roi5Y",
    "roiAnnual",
    "roiTTM",
    "tangibleBookValuePerShareAnnual",
    "tangibleBookValuePerShareQuarterly",
    "tbvCagr5Y",
    "totalDebt/totalEquityAnnual",
    "totalDebt/totalEquityQuarterly",
    "yearToDatePriceReturnDaily"
]

def create_server():
    mcp = FastMCP("Servidor de datos financieros", instructions="""
    Este servidor permite obtener datos financieros de una accion en tiempo real.
    Tiene dos herramientas:
    - parse_financials: Obtiene los datos basicos de una accion
    - get_stock_symbol: Obtiene el nombre tecnico de una accion
    """)

    @mcp.tool()
    def parse_financials(symbol: str, metric: MetricType) -> object:

        """
        Obtiene los datos basicos de una accion
        """
        logfire.notice("Obteniendo datos financieros de la accion " + symbol + " para la métrica " + metric, _tags=["parse_financials", symbol, metric])

        all_data = finnhub_client.company_basic_financials(symbol, 'all')
        if "metric" in all_data and metric in all_data["metric"]:
            logfire.notice(f"Se encontraron datos financieros para la accion {symbol} y la métrica {metric}, datos: {all_data['metric'][metric]}")
            return all_data["metric"][metric]
        else:
            logfire.warning("No se encontraron datos financieros para la accion " + symbol + " y la métrica " + metric)
            return "No se encontraron datos financieros para la accion %s y la métrica %s"
        
    @mcp.tool()
    def get_stock_symbol(query: str) -> str:
        """
        Obtiene el nombre tecnico de una accion
        """
        logfire.notice("Obteniendo el nombre tecnico de la accion " + query, _tags=["get_stock_symbol", query])
        symbol = finnhub_client.symbol_lookup(query)
        # si no hay symbol, devolvemos un mensaje de error
        if not symbol:
            logfire.warning("No se encontró el nombre tecnico de la accion " + query)
            symbol = "No se encontró el nombre tecnico de la accion " + query + " quiza deberias probar con un sinonimo"
        return symbol
    
    return mcp



if __name__ == "__main__":
    logfire.configure(token=" ")
    # Send standard logging to Logfire
    logging.basicConfig(handlers=[logfire.LogfireLoggingHandler()], level=logging.WARNING)
    finnhub_api_key = " "
    finnhub_client = finnhub.Client(api_key=finnhub_api_key)
    logger.info("Servidor MCP iniciado en puerto %s", 8002)

    server = create_server()
    server.run(transport="http", port=8002, host="0.0.0.0", stateless_http=True)






