
import ollama
from experts.expert_prompts import PROGRAMMING_PROMPT, MARKETING_PROMPT, LEGAL_PROMPT
from core.conversation import ConversationHistory

class ChatBot:
    def __init__(self):
        self.model = "gemma3:1b"
        self.experts = {
            "1": ("Programación", PROGRAMMING_PROMPT),
            "2": ("Marketing", MARKETING_PROMPT),
            "3": ("Legal", LEGAL_PROMPT)
        }
        self.active_expert = None
        self.history = ConversationHistory()

        try:
            ollama.show(model=self.model)
        except Exception:
            print("Error: modelo gemma3:1b no disponible.")
            exit()

    def select_expert(self):
        print("Selecciona un experto:")
        for key, val in self.experts.items():
            print(f"{key}. {val[0]}")
        choice = input("Opción: ").strip()
        if choice in self.experts:
            self.active_expert = choice
            self.history.reset()
            print(f"Experto activo: {self.experts[choice][0]}")
        else:
            print("Opción inválida.")

    def generate(self, user_msg):
        try:
            messages = [
                {"role": "system", "content": self.experts[self.active_expert][1]}
            ] + self.history.get() + [
                {"role": "user", "content": user_msg}
            ]
            response = ollama.chat(model=self.model, messages=messages)
            return response["message"]["content"]
        except Exception:
            return "Error al conectarse con Ollama o generar respuesta."

    def run(self):
        self.select_expert()
        while True:
            print("\nOpciones: cambiar | reiniciar | salir")
            user_input = input("Tú: ").strip()

            if user_input == "salir":
                break
            if user_input == "cambiar":
                self.select_expert()
                continue
            if user_input == "reiniciar":
                self.history.reset()
                print("Historial reiniciado.")
                continue

            self.history.add("user", user_input)
            reply = self.generate(user_input)
            self.history.add("assistant", reply)
            print("Bot:", reply)
