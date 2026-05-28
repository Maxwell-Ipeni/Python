#import externally defined functions and classes to your code 
from math import sqrt, pi, tan
from datetime import datetime, timedelta 
print(sqrt(16))
print(pi)
print(tan(pi/4))        
print(datetime.now())



#chat bot
from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer
bot = ChatBot('ChatBot')
print(f"Hello, I am {bot.name}. How can I help you?")
conversation = [
    "Hi",
    "Hello",
    "How are you?",
    "I am good, thank you!",
    "What is your name?",
    "My name is ChatBot.",
    "What can you do?",
    "I can chat with you and answer your questions.",
    "Goodbye",
    "Goodbye! Have a nice day!"
]
trainer = ListTrainer(bot)
trainer.train(conversation)
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("ChatBot: Goodbye! Have a nice day!")
        break
    response = bot.get_response(user_input)
    print(f"ChatBot: {response}")