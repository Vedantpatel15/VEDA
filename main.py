import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

st.set_page_config(
    page_title="Chat with VEDA",
    page_icon="🤖",
    layout="centered",
)

# Get API key correctly
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")

def map_role(role):
    return "assistant" if role == "model" else role

def get_message_text(message):
    """Safely extract text from Gemini message"""
    if hasattr(message, "parts"):
        return "".join(
            part.text for part in message.parts if hasattr(part, "text")
        )
    return ""

# Initialize chat session
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("🤖 Chat with VEDA")

# Display chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(map_role(message.role)):
        st.markdown(get_message_text(message))

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    response = st.session_state.chat_session.send_message(user_input)

    with st.chat_message("assistant"):
        st.markdown(response.text)
