import nltk
import random
import string
from nltk.corpus import stopwords
from nltk.chat.util import Chat, reflections

# Download NLTK data if not already installed
nltk.download('punkt')
nltk.download('stopwords')

# Define pairs of patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello! How can I assist you today?", "Hi there! How can I help?"]),
    (r"what is your name?", ["I am a chatbot created by OpenAI.", "I'm a friendly chatbot!"]),
    (r"how are you?", ["I'm just a program, but I'm doing fine!", "I'm doing well, thanks for asking!"]),
    (r"bye|goodbye", ["Goodbye! Have a great day!", "See you later!"]),
    (r"thank you|thanks", ["You're welcome!", "Glad I could help!"]),
    (r"tell me a joke", ["Why don't programmers like nature? It has too many bugs.", "Why did the developer go broke? Because he used up all his cache!"]),
    (r"(.*)", ["I'm sorry, I don't understand. Can you rephrase that?"])
]

# Create a chatbot with reflection (a set of basic transformations)
chatbot = Chat(pairs, reflections)

# Start conversation
print("Chatbot: Hi! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    
    # Exit if the user says 'bye' or 'goodbye'
    if user_input.lower() in ['bye', 'goodbye']:
        print("Chatbot: Goodbye! Have a nice day!")
        break
    
    # Get the chatbot's response
    response = chatbot.respond(user_input)
    print("Chatbot:", response)

