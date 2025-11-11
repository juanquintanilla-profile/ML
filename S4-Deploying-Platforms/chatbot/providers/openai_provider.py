# providers/azure_openai_provider.py

from openai import AzureOpenAI
import os

class AzureOpenAIProvider:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_version="2024-02-01"
        )
        self.deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

    def generate(self, messages):
        try:
            stream = self.client.chat.completions.create(
                model=self.deployment,
                messages=messages,
                stream=True
            )

            full_response = ""
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    text = chunk.choices[0].delta.content
                    print(text, end="", flush=True)
                    full_response += text

            print()
            return full_response

        except Exception as e:
            raise RuntimeError(f"Azure OpenAI provider failed: {e}")
