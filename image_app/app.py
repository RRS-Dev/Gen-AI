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
model = genai.GenerativeModel("gemini-pro-vision")

# Function to get response

def get_gemini_model(input,image):
    if input !="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text


# Initialize our streamlit app
st.set_page_config("Gemini Image")
st.header("Image Application")
input = st.text_input("Input",key="input")

uploaded_file = st.file_uploader("Choose an image: ", type=["jpg","jpeg","png"])
image=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

submit=st.button("Tell about the image")

if submit:
    response = get_gemini_model(input,image)
    st.subheader("The Response is: ")
    st.write(response)

