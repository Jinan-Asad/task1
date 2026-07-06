import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from chatbot import ask_question

print("Knowledge Base Assistant")

while True:
    q = input("You: ")

    if q.lower() == "exit":
        break

    print(ask_question(q))