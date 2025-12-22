# -*- coding: utf-8 -*-
from __future__ import annotations

import json
from datetime import datetime
import argparse
import sys
import finnhub
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any, Dict, List
from urllib.parse import urlencode
from urllib.request import urlopen


WALLET_FILE = Path(__file__).with_name("wallet.json")
FINNHUB_API_KEY = " "
FINNHUB_QUOTE_URL = "https://finnhub.io/api/v1/quote"
finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)

def _now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def _quantize_money(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def _parse_decimal(amount_str: str) -> Decimal:
    if not isinstance(amount_str, str):
        raise ValueError("El importe debe ser string")
    text = amount_str.strip().replace(",", ".")
    try:
        value = Decimal(text)
    except InvalidOperation as exc:
        raise ValueError("Importe inválido") from exc
    return _quantize_money(value)


def _parse_int(int_str: str) -> int:
    if not isinstance(int_str, str):
        raise ValueError("La cantidad debe ser string")
    try:
        value = int(int_str.strip())
    except Exception as exc:
        raise ValueError("Cantidad inválida") from exc
    if value <= 0:
        raise ValueError("La cantidad debe ser mayor que 0")
    return value


def _load_wallet() -> Dict[str, Any]:
    if not WALLET_FILE.exists():
        data = {"Efectivo": 0.0, "posiciones": [], "historico": []}
        WALLET_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return data
    text = WALLET_FILE.read_text(encoding="utf-8")
    try:
        return json.loads(text) if text.strip() else {"Efectivo": 0.0, "posiciones": [], "historico": []}
    except json.JSONDecodeError:
        # Si el JSON está corrupto, no sobrescribimos; lanzamos un error claro
        raise RuntimeError("El archivo wallet.json está corrupto o no es JSON válido")


def _save_wallet(data: Dict[str, Any]) -> None:
    WALLET_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def _decimal_from_wallet(value: Any) -> Decimal:
    return _quantize_money(Decimal(str(value)))


def _fetch_quote_price(symbol: str) -> Decimal:
    """
    Obtiene el precio actual (campo 'c') para el símbolo indicado desde Finnhub.
    Devuelve Decimal con dos decimales. Lanza ValueError en caso de error.
    """
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Símbolo inválido")
    
    try:
        data = finnhub_client.quote(symbol.strip())
    except Exception as exc:
        raise ValueError("No se pudo obtener la cotización", exc) from exc

    price = data.get("c")
    try:
        price_dec = Decimal(str(price))
    except Exception as exc:
        raise ValueError("Cotización inválida") from exc
    if price_dec <= 0:
        raise ValueError("Cotización no disponible", symbol, data)
    return _quantize_money(price_dec)


def init_wallet(efectivo_inicial: str) -> str:
    """
    Inicializa (o recrea) el archivo wallet.json con el efectivo indicado.

    Parámetros:
    - efectivo_inicial: string numérico (permite coma o punto) no negativo.

    Retorna string JSON con el estado y el efectivo resultante.
    """
    try:
        efectivo = _parse_decimal(efectivo_inicial)
    except ValueError as e:
        return json.dumps({"status": "error", "mensaje": str(e)}, ensure_ascii=False)

    if efectivo < Decimal("0"):
        return json.dumps({"status": "error", "mensaje": "El efectivo inicial no puede ser negativo"}, ensure_ascii=False)

    data = {"Efectivo": float(efectivo), "posiciones": [], "historico": []}
    _save_wallet(data)
    return json.dumps({"status": "ok", "efectivo": f"{efectivo:.2f}"}, ensure_ascii=False)


def leer_efectivo() -> str:
    """
    Devuelve el efectivo actual como string con dos decimales.
    """
    wallet = _load_wallet()
    efectivo = _decimal_from_wallet(wallet.get("Efectivo", 0))
    return f"{efectivo:.2f}"


def leer_posiciones() -> str:
    """
    Devuelve las posiciones actuales como string JSON.
    """
    wallet = _load_wallet()
    return json.dumps(wallet.get("posiciones", []), ensure_ascii=False)


def leer_historico() -> str:
    """
    Devuelve el histórico de operaciones como string JSON.
    """
    wallet = _load_wallet()
    return json.dumps(wallet.get("historico", []), ensure_ascii=False)


def añadir_posicion(nombre_stock: str, monto_pagado: str, numero_acciones: str = "") -> str:
    """
    Compra una nueva posición (lote) y la agrega a `posiciones` usando el precio de mercado actual.

    Parámetros (todos strings):
    - nombre_stock: símbolo o nombre del activo
    - monto_pagado: importe total máximo a invertir en euros (permite coma o punto). Se ignora `numero_acciones`.

    Reglas:
    - Obtiene la cotización actual desde Finnhub.
    - Calcula cuántas acciones enteras se pueden comprar con el menor de (monto_pagado, efectivo disponible).
    - Resta del `Efectivo` el importe efectivo invertido (precio_actual * cantidad_comprada).
    - Guarda `valor_inicial` como precio por acción con dos decimales (precio de mercado).

    Retorna string JSON con estado, efectivo y la posición creada.
    """
    wallet = _load_wallet()
    nombre = (nombre_stock or "").strip()
    if not nombre:
        return json.dumps({"status": "error", "mensaje": "El nombre del stock es obligatorio"}, ensure_ascii=False)

    try:
        total_pagado = _parse_decimal(monto_pagado)
    except ValueError as e:
        return json.dumps({"status": "error", "mensaje": str(e)}, ensure_ascii=False)

    efectivo = _decimal_from_wallet(wallet.get("Efectivo", 0))
    try:
        precio_unitario = _fetch_quote_price(nombre)
    except ValueError as e:
        return json.dumps({"status": "error", "mensaje": str(e)}, ensure_ascii=False)

    presupuesto = min(efectivo, total_pagado)
    if precio_unitario <= 0:
        return json.dumps({"status": "error", "mensaje": "Precio de mercado no disponible"}, ensure_ascii=False)

    # Cantidad entera máxima a comprar
    cantidad = int((presupuesto // precio_unitario))
    if cantidad <= 0:
        return json.dumps({"status": "error", "mensaje": "Monto insuficiente para comprar al precio actual"}, ensure_ascii=False)

    inversion_real = _quantize_money(precio_unitario * Decimal(cantidad))
    if inversion_real > efectivo:
        return json.dumps({"status": "error", "mensaje": "Efectivo insuficiente"}, ensure_ascii=False)

    nueva_posicion = {
        "nombre_stock": nombre,
        "cantidad": cantidad,
        "valor_inicial": float(precio_unitario),
        "fecha_compra": _now_iso(),
    }

    wallet.setdefault("posiciones", []).append(nueva_posicion)
    wallet["Efectivo"] = float(_quantize_money(efectivo - inversion_real))
    _save_wallet(wallet)

    return json.dumps(
        {
            "status": "ok",
            "efectivo": f"{_decimal_from_wallet(wallet['Efectivo']):.2f}",
            "posicion": nueva_posicion,
            "precio_utilizado": f"{precio_unitario:.2f}",
        },
        ensure_ascii=False,
    )


def vender_posicion(nombre_stock: str, numero_acciones: str, monto_recibido: str = "") -> str:
    """
    Vende acciones de un `nombre_stock` y mueve los lotes correspondientes a `historico`,
    calculando el precio de venta con la cotización actual.

    Parámetros (todos strings):
    - nombre_stock: símbolo o nombre del activo a vender
    - numero_acciones: cantidad total a vender (entera). Se ignora `monto_recibido`.

    Reglas:
    - Verifica que existan suficientes acciones sumando todos los lotes del activo.
    - Aplica FIFO por fecha de compra para descargar lotes.
    - Obtiene la cotización actual desde Finnhub y la usa como `valor_venta` (precio por acción) con dos decimales.
    - Suma al `Efectivo` el total recibido (precio_actual * numero_acciones).

    Retorna string JSON con estado, efectivo y detalle de ventas registradas en histórico.
    """
    wallet = _load_wallet()
    nombre = (nombre_stock or "").strip()
    if not nombre:
        return json.dumps({"status": "error", "mensaje": "El nombre del stock es obligatorio"}, ensure_ascii=False)

    try:
        cantidad_a_vender = _parse_int(numero_acciones)
    except ValueError as e:
        return json.dumps({"status": "error", "mensaje": str(e)}, ensure_ascii=False)

    posiciones: List[Dict[str, Any]] = wallet.get("posiciones", [])
    lotes_objetivo = [p for p in posiciones if (p.get("nombre_stock") or "").strip() == nombre]
    if not lotes_objetivo:
        return json.dumps({"status": "error", "mensaje": "No existen posiciones de ese activo"}, ensure_ascii=False)

    total_disponible = sum(int(p.get("cantidad", 0)) for p in lotes_objetivo)
    if cantidad_a_vender > total_disponible:
        return json.dumps({"status": "error", "mensaje": "Cantidad a vender superior a la disponible"}, ensure_ascii=False)

    try:
        precio_unitario_venta = _fetch_quote_price(nombre)
    except ValueError as e:
        return json.dumps({"status": "error", "mensaje": str(e)}, ensure_ascii=False)
    total_recibido = _quantize_money(precio_unitario_venta * Decimal(cantidad_a_vender))
    restante = cantidad_a_vender
    ahora = _now_iso()

    # Orden FIFO por fecha_compra
    def parse_fecha(p: Dict[str, Any]) -> str:
        return str(p.get("fecha_compra", ""))

    lotes_objetivo.sort(key=parse_fecha)
    ventas_registradas: List[Dict[str, Any]] = []

    for lote in lotes_objetivo:
        if restante <= 0:
            break
        disponible_lote = int(lote.get("cantidad", 0))
        if disponible_lote <= 0:
            continue
        a_descargar = min(restante, disponible_lote)

        registro_historico = {
            "nombre_stock": nombre,
            "cantidad": a_descargar,
            "valor_inicial": float(_quantize_money(Decimal(str(lote.get("valor_inicial", 0))))),
            "fecha_compra": lote.get("fecha_compra"),
            "fecha_venta": ahora,
            "valor_venta": float(precio_unitario_venta),
        }
        wallet.setdefault("historico", []).append(registro_historico)
        ventas_registradas.append(registro_historico)

        # Actualizar o eliminar el lote
        lote["cantidad"] = disponible_lote - a_descargar
        restante -= a_descargar

    # Eliminar lotes con cantidad 0
    wallet["posiciones"] = [p for p in wallet.get("posiciones", []) if int(p.get("cantidad", 0)) > 0]

    # Actualizar efectivo
    efectivo_actual = _decimal_from_wallet(wallet.get("Efectivo", 0))
    wallet["Efectivo"] = float(_quantize_money(efectivo_actual + total_recibido))

    _save_wallet(wallet)

    return json.dumps(
        {
            "status": "ok",
            "efectivo": f"{_decimal_from_wallet(wallet['Efectivo']):.2f}",
            "ventas": ventas_registradas,
            "precio_utilizado": f"{precio_unitario_venta:.2f}",
            "total_recibido": f"{total_recibido:.2f}",
        },
        ensure_ascii=False,
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wallet",
        description="Gestor de wallet: inicializar, consultar efectivo/posiciones/histórico, comprar y vender.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # init
    p_init = subparsers.add_parser(
        "init", help="Inicializa la wallet con el efectivo indicado (recrea wallet.json)"
    )
    p_init.add_argument("efectivo", help="Efectivo inicial. Acepta coma o punto. Ej: 1000,50")

    # efectivo
    subparsers.add_parser("efectivo", help="Muestra el efectivo actual")

    # posiciones
    subparsers.add_parser("posiciones", help="Muestra las posiciones actuales (JSON)")

    # historico
    subparsers.add_parser("historico", help="Muestra el historico de operaciones (JSON)")

    # comprar (añadir_posicion)
    p_comprar = subparsers.add_parser(
        "comprar", help="Compra un activo usando el precio de mercado actual"
    )
    p_comprar.add_argument("nombre", help="Símbolo o nombre del activo. Ej: AAPL")
    p_comprar.add_argument(
        "monto", help="Importe máximo a invertir. Acepta coma o punto. Ej: 500"
    )

    # vender (vender_posicion)
    p_vender = subparsers.add_parser(
        "vender", help="Vende una cantidad de un activo al precio de mercado actual"
    )
    p_vender.add_argument("nombre", help="Símbolo o nombre del activo. Ej: AAPL")
    p_vender.add_argument("cantidad", type=int, help="Cantidad total a vender (entera)")

    return parser


def main(argv: List[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "init":
        output = init_wallet(args.efectivo)
    elif args.command == "efectivo":
        output = leer_efectivo()
    elif args.command == "posiciones":
        output = leer_posiciones()
    elif args.command == "historico":
        output = leer_historico()
    elif args.command == "comprar":
        output = añadir_posicion(args.nombre, args.monto)
    elif args.command == "vender":
        # La API espera strings
        output = vender_posicion(args.nombre, str(args.cantidad))
    else:
        parser.error("Comando no reconocido")
        return 2

    print(output)
    return 0


__all__ = [
    "init_wallet",
    "leer_efectivo",
    "añadir_posicion",
    "vender_posicion",
    "leer_posiciones",
    "leer_historico",
]


if __name__ == "__main__":
    raise SystemExit(main())

