from client.openai_client import ask_llm

def run_cli(tools):
    messages = [{"role": "system", "content": "Asistente experto en clima y finanzas"}]
    print("CLI MCP IA (/ayuda, /salir)")

    while True:
        user = input("> ")
        if user == "/salir":
            break
        if user == "/ayuda":
            print("Ejemplos: Convierte 100 USD a EUR | ¿Qué tiempo hace en Madrid?")
            continue

        messages.append({"role": "user", "content": user})
        response = ask_llm(messages, tools)

        for msg in response.output:
            if msg["type"] == "message":
                print(msg["content"][0]["text"])