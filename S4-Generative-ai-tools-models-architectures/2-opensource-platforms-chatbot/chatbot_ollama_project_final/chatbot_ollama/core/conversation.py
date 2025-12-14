
class ConversationHistory:
    def __init__(self):
        self.history = []

    def add(self, role, content):
        self.history.append({"role": role, "content": content})

    def reset(self):
        self.history = []

    def get(self):
        return self.history
