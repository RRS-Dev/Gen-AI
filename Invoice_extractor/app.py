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

def get_gemini_model(input,image,prompt):
    response = model.generate_content([input,image,prompt])
    return response.text

def input_image_data(uploaded_file):
    if uploaded_file is not None:
        #Read file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts =[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    
    else:
        raise FileNotFoundError("No File Uploaded")



# Initialize our streamlit app
st.set_page_config("Multilanguage Invoice Extractor")
st.header("Invoice Extractor")
input = st.text_input("Input",key="input")

uploaded_file = st.file_uploader("Choose an image: ", type=["jpg","jpeg","png"])
image=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

submit=st.button("Tell me about the image")

input_prompt = """
You are an expert in understanding invoices. 
We will upload a image as invoice and you will have to answer any question based on the uploaded invoice image.
"""

if submit:
    image_data = input_image_data(uploaded_file)
    response = get_gemini_model(input_prompt,image,input)
    st.subheader("The Response is: ")
    st.write(response)

