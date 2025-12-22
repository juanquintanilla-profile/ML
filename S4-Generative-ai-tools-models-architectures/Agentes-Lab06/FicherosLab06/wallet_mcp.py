from fastmcp import FastMCP
import logging
import sys
from pathlib import Path
import logfire
import logging
from fastmcp.utilities.logging import get_logger
# Aseguramos poder importar la logica desde wallet.py en el mismo directorio
CURRENT_DIR = Path(__file__).parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))

import wallet as wallet_logic


def create_server():
    mcp = FastMCP(
        "Wallet MCP",
        instructions=
        """
        Este servidor expone operaciones de la wallet del usuario conectado:
        - leer_efectivo()
        - leer_posiciones()
        - leer_historico()
        - anadir_posicion(nombre_stock: str, monto_pagado: str, numero_acciones: str = "")
        - vender_posicion(nombre_stock: str, numero_acciones: str, monto_recibido: str = "")
        """,
    )


    @mcp.tool()
    def leer_efectivo() -> str:
        """Obtiene el efectivo disponible en la wallet.

        Returns:
            str: Efectivo actual con dos decimales (por ejemplo, "1000.00").
        """
        logfire.notice("Leyendo efectivo actual", _tags=["leer_efectivo"])
        result = wallet_logic.leer_efectivo()
        logfire.notice("Resultado leer_efectivo: " + str(result), _tags=["leer_efectivo", "resultado"])
        return result

    @mcp.tool()
    def leer_posiciones() -> str:
        """Lista las posiciones actuales del usuario.

        Returns:
            str: JSON con la lista de posiciones. Cada posicion contiene
                `nombre_stock`, `cantidad`, `valor_inicial` y `fecha_compra`.
        """
        logfire.notice("Leyendo posiciones actuales", _tags=["leer_posiciones"])
        result = wallet_logic.leer_posiciones()
        logfire.notice("Resultado leer_posiciones: " + str(result), _tags=["leer_posiciones", "resultado"])
        return result



    @mcp.tool()
    def anadir_posicion(nombre_stock: str, monto_pagado: str, numero_acciones: str = "") -> str:
        """Compra un activo usando el precio de mercado actual.

        Args:
            nombre_stock (str): Simbolo o nombre del activo, por ejemplo "AAPL".
            monto_pagado (str): Importe maximo a invertir. Acepta coma o punto, por ejemplo "500" o "500,00".
            numero_acciones (str, opcional): No usado en esta version; puede dejarse vacio.

        Returns:
            str: JSON con el estado de la operacion, efectivo actualizado, la posicion creada
                y el `precio_utilizado`.
        """
        logfire.notice(
            "Anadiendo posicion de " + nombre_stock + " por monto " + monto_pagado,
            _tags=["anadir_posicion", nombre_stock, monto_pagado, numero_acciones],
        )
        result = wallet_logic.añadir_posicion(nombre_stock, monto_pagado, numero_acciones)
        logfire.notice(
            "Resultado anadir_posicion: " + str(result),
            _tags=["anadir_posicion", "resultado", nombre_stock],
        )
        return result

    @mcp.tool()
    def vender_posicion(nombre_stock: str, numero_acciones: str, monto_recibido: str = "") -> str:
        """Vende una cantidad de un activo al precio de mercado actual.

        Args:
            nombre_stock (str): Simbolo o nombre del activo a vender, por ejemplo "AAPL".
            numero_acciones (str): Cantidad total (entera) a vender.
            monto_recibido (str, opcional): No usado; se calcula con la cotizacion actual.

        Returns:
            str: JSON con el estado de la operacion, efectivo actualizado, detalle de `ventas`,
                `precio_utilizado` y `total_recibido`.
        """
        logfire.notice(
            "Vendiendo " + numero_acciones + " acciones de " + nombre_stock,
            _tags=["vender_posicion", nombre_stock, numero_acciones],
        )
        result = wallet_logic.vender_posicion(nombre_stock, numero_acciones, monto_recibido)
        logfire.notice(
            "Resultado vender_posicion: " + str(result),
            _tags=["vender_posicion", "resultado", nombre_stock, numero_acciones],
        )
        return result
    
    @mcp.tool()
    def leer_historico() -> str:
        """Devuelve el historico de operaciones realizadas.

        Returns:
            str: JSON con la lista de operaciones (compras/ventas) registradas.
        """
        logfire.notice("Leyendo historico de operaciones", _tags=["leer_historico"])
        result = wallet_logic.leer_historico()
        logfire.notice("Resultado leer_historico: " + str(result), _tags=["leer_historico", "resultado"])
        return result

    return mcp


if __name__ == "__main__":
    logfire.configure(token=" ")
    # Send standard logging to Logfire
    logging.basicConfig(handlers=[logfire.LogfireLoggingHandler()], level=logging.WARNING)
    server = create_server()
    server.run(transport="http", port=800, host="0.0.0.0", stateless_http=True)






