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
    
    def run(self, user_input: str) -> str:
        response = client.chat.completion.create(
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

    def run    
    
    

