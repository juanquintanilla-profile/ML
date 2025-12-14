# 🧠 Proyecto IA – Servidor MCP con Conversión de Monedas y Clima

## 📌 Descripción general

Este proyecto implementa un **servidor MCP (Model Context Protocol)** que expone herramientas de conversión de monedas y consulta meteorológica usando **FastMCP**, integrando APIs públicas reales. Además, incluye un **cliente en Python** que utiliza la **API de OpenAI (Responses)** para interactuar con dichas herramientas mediante lenguaje natural, junto con una **interfaz CLI** interactiva.

El sistema funciona de extremo a extremo:  
**usuario → cliente OpenAI → servidor MCP → APIs externas → respuesta al usuario**.

---

## 🎯 Objetivos del proyecto

- Proporcionar herramientas externas a una IA generativa mediante MCP.
- Integrar APIs reales de conversión de monedas y clima.
- Demostrar llamadas secuenciales a herramientas (geocodificación → clima).
- Construir una CLI usable y documentada.
- Cumplir criterios de evaluación automática con IA.

---

## 🧪 Funcionalidades principales

### Conversión de monedas (ExchangeRate-API)
- Conversión entre divisas en tiempo real.
- Consulta de tasas de cambio actuales desde una moneda base.

### Clima y geocodificación (Open-Meteo)
- Geocodificación: ciudad → latitud/longitud.
- Clima actual: temperatura, humedad y descripción.
- Pronóstico meteorológico a varios días.

### Cliente OpenAI
- Uso del modelo `gpt-4o` o `gpt-4o-mini`.
- Llamadas automáticas y secuenciales a herramientas MCP.
- Manejo de errores, reintentos y respuestas síncronas.

### Interfaz CLI
- Consultas en lenguaje natural.
- Comandos especiales (`/ayuda`, `/salir`, `/monedas`).
- Validación de entradas y errores de usuario.

---

## 🗂️ Estructura del proyecto

```text
├── server/
│   ├── __init__.py
│   ├── mcp_server.py           # Servidor MCP con FastMCP
│   ├── currency_tools.py       # Herramientas de conversión de monedas
│   ├── weather_tools.py        # Herramientas de clima
│   ├── geocoding_tools.py      # Herramientas de geocodificación
│   └── api_clients.py          # Clientes HTTP para APIs externas
├── client/
│   ├── __init__.py
│   ├── openai_client.py        # Cliente OpenAI con MCP
│   └── cli_interface.py        # Interfaz de línea de comandos
├── config/
│   ├── __init__.py
│   └── settings.py             # Configuración y variables de entorno
├── main_server.py              # Punto de entrada del servidor
├── main_client.py              # Punto de entrada del cliente
├── requirements.txt
├── .env.example                # Ejemplo de variables de entorno
├── .env                        # Variables reales (no subir a git)
└── README.md
