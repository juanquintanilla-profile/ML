from providers.openai_provider import AzureOpenAIProvider
from providers.gemini_provider import GeminiProvider
from providers.anthropic_provider import AnthropicProvider

FALLBACK_RESPONSE = "I'm sorry, but i can't answer right now. Please try again later"

class ChatBot:

    def __init__(self,conversation):

        self.conversation = conversation
        self.openai = AzureOpenAIProvider()
        self.anthropic = AnthropicProvider()
        self.gemini = GeminiProvider()

    def ask(self, user_message):

        self.conversation.add("user",user_message)
        history = self.conversation.get()

        for provider in [self.openai, self.anthropic, self.gemini]:
            try:
                print(f"Using provider: {provider.__class__.__name__}")
                answer = provider.generate(history)
                self.conversation.add("assistant",answer)
                return answer
            except Exception as e:
                print(f"{provider.__class__.__name__} failed: {e}")
            
        print("None providers available. Sending fallback response")
        self.conversation.add("assistant",FALLBACK_RESPONSE)
        return FALLBACK_RESPONSE