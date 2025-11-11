from dotenv import load_dotenv
from core.conversation import ConversationHistory
from core.chatbot import ChatBot

def main():

    load_dotenv()

    conversation = ConversationHistory()
    bot = ChatBot(conversation=conversation)

    print("\n Chatbot read! type '/exit' to quit. \n")

    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in ("/exit", "/salir", "quit"):
            print("Goodbye!. I hope i Helped")
            break

        bot.ask(user_input)

if __name__ == "__main__":
    main()