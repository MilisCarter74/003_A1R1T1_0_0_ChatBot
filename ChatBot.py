import random

class ChatBot:
    Hi_keywords = ["hi", "good day", "good morning", "good evening", "wassap", "how are you"]
    Math_task_keywords = ["add", "plus", "substruct", "minus", "calculate", "multiply", "divide"]
    Bye_keywords = ["See you letter", "bye", "chao", "Goodbye"]

    def __init__(self):
        self.Hello_responces = ["Hi, can i help you?", "Hi, do you have any question?",
                                "Good day, what are the tasks today?"]
        self.Task_responceTrue = ["There is the answer:", "Sure, here is the solution:"]
        self.Task_responceFalse = ["Suddenly i cant answer this question",
                                   "Sorry, i couldn't answer that"]
        self.Bye_responce = ["Bye, was happy to help", "Goodbye! if you have any more question, you can ask me",
                             "Well, bye then"]

    def __solve_math(self, math_word, words):
        numbers = []
        for word in words:
            if word.isdigit():
                numbers.append(int(word))
        if len(numbers) < 2:
            return None

        a, b = numbers[0], numbers[1]

        if math_word in ["add", "plus"]:
            return a + b
        elif math_word in ["substruct", "minus"]:
            return a - b
        elif math_word == "multiply":
            return a * b
        elif math_word == "divide":
            if b == 0:
                return "You can't divide by zero!"
            return a / b
        else:
            return None

    def respond(self, message):
        message_lower = message.lower()
        words = message_lower.split()

        for hi_word in ChatBot.Hi_keywords:
            if hi_word in message_lower:
                return random.choice(self.Hello_responces)

        for math_word in ChatBot.Math_task_keywords:
            if math_word in message_lower:
                result = self.__solve_math(math_word, words)
                if result is not None:
                    return random.choice(self.Task_responceTrue) + " " + str(result)
                else:
                    return random.choice(self.Task_responceFalse)

        for bye_word in ChatBot.Bye_keywords:
            if bye_word in message_lower:
                return random.choice(self.Bye_responce)

        return "Sorry, i didnt understand this message."

bot = ChatBot()

while True:
    i = input()
    print(bot.respond(i))
