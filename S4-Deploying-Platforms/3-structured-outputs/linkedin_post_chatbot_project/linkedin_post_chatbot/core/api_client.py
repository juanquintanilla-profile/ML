import openai
from dotenv import load_dotenv
import os
from models.linkedin_post import LinkedinPost

class OpenAIClient:
    def __init__(self):
        load_dotenv()
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_post(self, idea: str) -> LinkedinPost:
        try:
            response = self.client.responses.parse(
                model="gpt-4.1",
                input=f"Genera un post de LinkedIn basado en esta idea: {idea}",
                text_format=LinkedinPost
            )
            return response.output
        except Exception as e:
            raise RuntimeError(f"Error al generar el post: {e}")
