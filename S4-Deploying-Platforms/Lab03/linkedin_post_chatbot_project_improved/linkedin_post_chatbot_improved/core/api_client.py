import openai
from dotenv import load_dotenv
import os
from pydantic import ValidationError
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
            return response.output_parsed

        except openai.APIStatusError as e:
            raise RuntimeError(f"Error de API: {e.message}")

        except openai.APITimeoutError:
            raise RuntimeError("La solicitud tardó demasiado en responder.")

        except openai.RateLimitError:
            raise RuntimeError("Límite de uso alcanzado. Espera antes de intentar nuevamente.")

        except ValidationError as e:
            raise RuntimeError(f"Error validando la estructura del post: {e}")

        except Exception as e:
            if "refusal" in str(e).lower():
                raise RuntimeError("El modelo rechazó generar el contenido solicitado.")
            raise RuntimeError(f"Ocurrió un error inesperado: {e}")
