from openai import OpenAI
from config.settings import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_llm(messages, tools):
    return client.responses.create(
        model=OPENAI_MODEL,
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )