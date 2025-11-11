# providers/gemini_provider.py

from google import genai
import os

class GeminiProvider:
    def __init__(self):
        """
        Initialize Google Gemini provider.
        """
        self.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model_name = "gemini-2.5-pro"  # or gemini-2.5-flash

    def generate(self, messages):
        """
        Generate streamed output from Gemini API.
        We convert conversation history into a single text prompt.
        """
        try:
            # Combine conversation into simple transcript format
            text_input = ""
            for msg in messages:
                role = "User" if msg["role"] == "user" else "Assistant"
                text_input += f"{role}: {msg['content']}\n"

            # Stream response
            stream = self.client.generate_stream(
                model=self.model_name,
                contents=text_input,
            )

            full_response = ""

            for chunk in stream:
                if chunk.text:  # some chunks contain only metadata
                    print(chunk.text, end="", flush=True)
                    full_response += chunk.text

            print()  # newline after output completes
            return full_response

        except Exception as e:
            raise RuntimeError(f"Google Gemini provider failed: {e}")
