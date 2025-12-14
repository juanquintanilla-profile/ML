from core.api_client import OpenAIClient

class LinkedInChatbot:
    def __init__(self):
        self.client = OpenAIClient()

    def run(self):
        print("Generador de posts de LinkedIn")
        print("Escribe 'salir' para terminar.\n")

        while True:
            idea = input("Describe la idea de tu post: ").strip()
            if idea.lower() == "salir":
                break
            if not idea:
                print("Por favor escribe una idea válida.\n")
                continue

            try:
                result = self.client.generate_post(idea)
                print("\n--- POST GENERADO ---")
                print("Título:", result.title)
                print("Contenido:", result.content)
                print("Hashtags:", ", ".join(result.hashtags))
                print("Categoría:", result.category)
                print("----------------------\n")
            except Exception as e:
                print(f"Error: {e}\n")
