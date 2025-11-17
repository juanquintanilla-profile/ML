import os
from typing import List, Dict, Any
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

load_dotenv()

class Chatbot:
    def __init__(self, model_name: str = None, temperature: float = 0.0):
        model = model_name or os.getenv('DEFAULT_MODEL', 'gpt-4o')
        # instantiate ChatOpenAI from LangChain; model names should match available OpenAI models in your account
        self.llm = ChatOpenAI(model=model, temperature=temperature)
        self.history: List[Dict[str,str]] = []  # list of {'role': 'user'|'assistant', 'content': ...}

    def _build_system_prompt(self, retrieved_texts: List[Dict[str,Any]]) -> str:
        # System instruction: only answer based on retrieved texts. If not found, say you don't know.
        sources = "\n\n".join([f"[source_{i+1}] {r['text'][:800]}" for i, r in enumerate(retrieved_texts)])
        system = (
            "Eres un asistente que responde *solo* usando la información proporcionada en las fuentes recuperadas.\n"
            "Si la pregunta no puede responderse con las fuentes, responde honestamente que no tienes suficiente información.\n"
            "Proporciona respuestas claras y cortas y, si procede, menciona de qué fuente proviene la información.\n\n"
            f"Fuentes:\n{sources}\n\n"
            "RESPONDE AHORA:"
        )
        return system

    def ask(self, question: str, retrieved: List[Dict[str,Any]]) -> str:
        system_prompt = self._build_system_prompt(retrieved)
        messages = [SystemMessage(content=system_prompt)]
        # include short history as previous user/assistant messages
        for turn in self.history[-6:]:  # keep last few turns
            if turn['role'] == 'user':
                messages.append(HumanMessage(content=turn['content']))
            else:
                messages.append(AIMessage(content=turn['content']))
        messages.append(HumanMessage(content=question))
        resp = self.llm(messages)
        answer = resp.content
        # update history
        self.history.append({'role': 'user', 'content': question})
        self.history.append({'role': 'assistant', 'content': answer})
        return answer
