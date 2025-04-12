import streamlit as st
from datetime import datetime
import random

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! 👋"],
    "how are you": ["I'm good, thanks!", "Doing great, and you?", "All good!"],
    "bye": ["Goodbye!", "See you later!", "Bye! 👋"],
    "default": ["I'm not sure I understand. Could you rephrase? 🤔"]
}

def simple_chatbot(user_input):
    """Returns a random response based on user input."""
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Streamlit UI setup
st.title("Simple Chatbot")
st.header("Chat with me!")

# Initialize chat history in session state if not already present
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Display previous chat messages
for message in st.session_state['chat_history']:
    st.write(message)

# User input
user_input = st.text_input("You: ", "")

# Handle user input and generate response
if user_input:
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Append the user input to the chat history with timestamp
    st.session_state['chat_history'].append(f"[{timestamp}] You: {user_input}")
    
    # Get the chatbot's response
    response = simple_chatbot(user_input)
    
    # Append the bot's response to the chat history with timestamp
    st.session_state['chat_history'].append(f"[{timestamp}] Bot: {response}")
    
    # Display updated chat history with the new message
    for message in st.session_state['chat_history']:
        st.write(message)
