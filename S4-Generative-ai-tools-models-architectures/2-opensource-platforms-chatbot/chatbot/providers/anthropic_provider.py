# providers/anthropic_provider.py

from anthropic import Anthropic
import os

class AnthropicProvider:
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    def generate(self, messages):
        """
        Convert OpenAI-style history to Anthropic format.
        """
        try:
            formatted_messages = []
            for m in messages:
                formatted_messages.append({"role": m["role"], "content": m["content"]})

            with self.client.messages.stream(
                model="claude-3-7-sonnet-latest",
                messages=formatted_messages,
                max_tokens=500
            ) as stream:
                full_response = ""
                for text in stream.text_stream:
                    print(text, end="", flush=True)
                    full_response += text

            print()
            return full_response

        except Exception as e:
            raise RuntimeError(f"Anthropic provider failed: {e}")
