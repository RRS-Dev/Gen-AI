import os
import google.generativeai as genai
import streamlit as st
from PIL import Image

from dotenv import load_dotenv

# Loading Environment Variables
load_dotenv()

# Getting API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Model Generation
model = genai.GenerativeModel("gemini-pro")

# Chat History
chat = model.start_chat(history=[])

# Function to get response
def get_gemini_model(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize our Streamlit app
st.set_page_config("Chatbot")
st.header("Conversational Q&A Application")

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input", key="input")
submit = st.button("Ask a question")

if submit and input:
    response = get_gemini_model(input)
    # Get User query and response to session chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is:")
    
    # Placeholder for the dynamic response
    response_placeholder = st.empty()
    response_text = ""
    
    # st.subheader("The Response is:")
    for chunk in response:
        response_text += chunk.text
        response_placeholder.markdown(response_text)
    
    st.session_state['chat_history'].append(("Bot", response_text))

st.subheader("Chat History is")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
