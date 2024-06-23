import google.generativeai as genai
import os
import streamlit as st

from dotenv import load_dotenv
# loading Environment Variables
load_dotenv()

# Passing API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Model and get responses
model = genai.GenerativeModel("gemini-pro")
def get_gemini_model(question):
        response = model.generate_content(question)
        return response.text


# Initializing streamlit app
st.set_page_config("Q&A Demo")
st.header("Gemini LLM Model")

input = st.text_input("Input",key="input")
submit = st.button("Ask the Question")

# When Submit button is clicked

if submit:
        response = get_gemini_model(input)
        st.subheader("The Response is: ")
        st.write(response)





