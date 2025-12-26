from pydantic import BaseModel
from typing import List
from openai import OpenAI 


client = OpenAI() 

class LinkedInPost(BaseModel):

    title: str
    content: str
    hashtags: List[str]
    category: str


class MarkingAgent:
    
    name = "Marketing agent",
    
    def run(self, user_input: str) -> LinkedInPost:
        response = client.chat.completions.create(
            model = "gpt-4.1-mini",
            messages = [
                {
                    "role": "system",
                    "create":(
                        "Eres un experto en marketing digital. "
                        "Genera una publicacion de LinkedIn con "
                        "titulo, contenido, hashtag y categoría Marketing"
                    )
                },
                {"role":"user","content": user_input}
            ]
        )
        return response.choices[0].message.content
    
class ProgrammingAgent:
    name = "Programming Agent"

    def run(self, user_input: str) -> LinkedInPost:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Eres un desarrollador senior. "
                        "Genera una publicación de LinkedIn técnica. "
                        "category = Programación. Devuelve SOLO JSON."
                    )
                },
                {"role": "user", "content": user_input}
            ]
        )
        return LinkedInPost.model_validate_json(
            response.choices[0].message.content
        )


class LegalAgent:

    name = "Legal Agent"

    def run(self,user_input: str) -> LinkedInPost:
        response = client.chat.completions.create(
            model = "gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Eres un experto jurídico. "
                        "Genera una publicación de LinkedIn legal. "
                        "category = Legal. Devuelve SOLO JSON."
                    )
                },
                {"role": "user", "content": user_input}
            ]
        )
        return LinkedInPost.model_validate_json(
            response.choices[0].message.content
        )
        
    
    
    

