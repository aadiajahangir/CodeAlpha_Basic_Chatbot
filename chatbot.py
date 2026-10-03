import random
from datetime import datetime


class ChatBot:
    def __init__(self):
        self.name = None
        self.conversation_history = []

        self.responses = {
            "greeting": [
                "Hello! 👋 How can I help you?",
                "Hi there! 😊 Nice to chat with you.",
                "Hey! What's on your mind?"
            ],
            "how_are_you": [
                "I'm doing great! Thanks for asking. 😊",
                "I'm good and ready to chat!",
                "All systems are running perfectly! 🤖"
            ],
            "thanks": [
                "You're welcome! 😊",
                "No problem!",
                "Happy to help! 👍"
            ]
        }

    def get_time(self):
        return datetime.now().strftime("%I:%M %p")

    def get_date(self):
        return datetime.now().strftime("%d %B %Y")

    def tell_joke(self):
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Why did the computer go to the doctor? Because it had a virus! 😂",
            "There are only 10 kinds of people in the world: those who understand binary and those who don't. 😄"
        ]
        return random.choice(jokes)

    def tell_fact(self):
        facts = [
            "Python was created by Guido van Rossum. 🐍",
            "The first computer mouse was made of wood.",
            "The word 'robot' comes from a Czech word meaning forced labor."
        ]
        return random.choice(facts)

    def calculate(self, expression):
        try:
            result = eval(expression, {"__builtins__": None}, {})
            return f"The answer is {result}."
        except:
            return "Sorry, I couldn't calculate that. Please enter a valid expression."

    def respond(self, user_input):
        user_input = user_input.lower().strip()

        self.conversation_history.append(user_input)

        if user_input in ["bye", "exit", "quit"]:
            return f"Goodbye, {self.name or 'friend'}! 👋"

        elif user_input in ["hi", "hello", "hey"]:
            return random.choice(self.responses["greeting"])

        elif "how are you" in user_input:
            return random.choice(self.responses["how_are_you"])

        elif "your name" in user_input or "who are you" in user_input:
            return "I'm a Python-based rule chatbot created for a CodeAlpha internship project. 🤖"

        elif "my name" in user_input:
            if self.name:
                return f"Your name is {self.name}. 😊"
            return "You haven't told me your name yet."

        elif "time" in user_input:
            return f"The current time is {self.get_time()}."

        elif "date" in user_input or "today" in user_input:
            return f"Today's date is {self.get_date()}."

        elif "joke" in user_input:
            return self.tell_joke()

        elif "fact" in user_input:
            return self.tell_fact()

        elif "thank" in user_input:
            return random.choice(self.responses["thanks"])

        elif user_input.startswith("calculate "):
            expression = user_input.replace("calculate ", "", 1)
            return self.calculate(expression)

        elif user_input == "history":
            if self.conversation_history:
                return "You have sent " + str(len(self.conversation_history)) + " messages in this conversation."
            return "No conversation history yet."

        elif "help" in user_input:
            return (
                "Here are some things you can ask me:\n"
                "• Hello / Hi\n"
                "• How are you?\n"
                "• What is your name?\n"
                "• What is my name?\n"
                "• What is the time?\n"
                "• What is today's date?\n"
                "• Tell me a joke\n"
                "• Tell me a fact\n"
                "• Calculate 10 + 5\n"
                "• History\n"
                "• Bye"
            )

        else:
            return "I'm not sure how to respond to that yet. Try typing 'help' to see what I can do."


def main():
    bot = ChatBot()

    print("=" * 50)
    print("🤖  WELCOME TO PYTHON CHATBOT")
    print("=" * 50)

    bot.name = input("🤖 ChatBot: What's your name?\nYou: ").strip()

    if not bot.name:
        bot.name = "Friend"

    print(f"\n🤖 ChatBot: Nice to meet you, {bot.name}! 😊")
    print("🤖 ChatBot: Type 'help' to see what You can ask me.")
    print("🤖 ChatBot: Type 'bye' whenever you want to exit.\n")

    while True:
        user_input = input(f"{bot.name}: ")

        response = bot.respond(user_input)

        print(f"🤖 ChatBot: {response}")

        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            break


if __name__ == "__main__":
    main()