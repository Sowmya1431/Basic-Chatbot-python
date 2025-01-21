
from flask import Flask, render_template, request, jsonify
import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK resources
nltk.download("punkt")

# Define more advanced conversation pairs for pattern matching
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I assist you today?"]],
    [r"how are you?", ["I'm doing great, thank you!", "I'm good. How about you?"]],
    [r"what is your name?", ["I'm a chatbot created for this demo. You can call me ChatBot!"]],
    [r"what is your hobby?", ["I love chatting with humans like you! It's always fun to learn new things."]],
    [r"tell me a joke", ["Why don't skeletons fight each other? They don't have the guts!", "What do you call fake spaghetti? An impasta!"]],
    [r"can you help me with (.*)", ["Sure! I'd be happy to help with %1. How can I assist you?"]],
    [r"(.*) weather in (.*)", ["Sorry, I can't check the weather right now, but you can easily find it on your weather app!"]],
    [r"(bye|exit|quit)", ["Goodbye! Have a nice day!", "See you soon!"]],
    [r"(.*)", ["I'm not sure I understand. Could you rephrase that?", "That's an interesting question, but I don't have an answer for it."]], [r"what is your name?", ["I'm a chatbot created for this demo. You can call me ChatBot!"]],
    [r"what is your hobby?", ["I love chatting with humans like you! It's always fun to learn new things."]],
    [r"tell me a joke", ["Why don't skeletons fight each other? They don't have the guts!", "What do you call fake spaghetti? An impasta!"]],
    [r"can you help me with (.*)", ["Sure! I'd be happy to help with %1. How can I assist you?"]],
    [r"(.*) weather in (.*)", ["Sorry, I can't check the weather right now, but you can easily find it on your weather app!"]],
    [r"(good morning|morning)", ["Good morning! How can I help you today?", "Morning! What can I do for you?"]],
    [r"(good afternoon|afternoon)", ["Good afternoon! How's your day going?", "Good afternoon! What can I assist you with today?"]],
    [r"(good evening|evening)", ["Good evening! How was your day?", "Good evening! How may I help you?"]],
    [r"how do you do?", ["I'm doing well, thank you for asking! How do you do?", "I'm doing great! How are you today?"]],
    [r"bye|exit|quit", ["Goodbye! Have a nice day!", "See you soon!"]],
    [r"(.*)", ["I'm not sure I understand. Could you rephrase that?", "That's an interesting question, but I don't have an answer for it."]],
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    """
    Render the home page.
    """
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    """
    Get response from the chatbot.
    """
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"response": "Please provide a message."})

    # Get the chatbot response
    response = chatbot.respond(user_message)
    
    if response is None:
        response = "I'm not sure I understand. Could you try again?"
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
