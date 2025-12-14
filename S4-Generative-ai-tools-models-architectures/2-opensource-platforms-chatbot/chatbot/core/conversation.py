
"""
This class acts as an in-memory storage  for the conversation, no database needed.
"""
class ConversationHistory:

    def __init__(self):
        self.messages = []
    
    def add(self, role: str, content : str):

        """
        Add a message to the conversation history.
        role = ""user"" or ""assistant""
        """

        self.messages.append({"role": role, "content":content})
    
    def get(self):

        """Return the entire conversation history"""
        return self.messages
    