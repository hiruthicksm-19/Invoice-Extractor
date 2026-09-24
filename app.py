import os
import google.genai as genai
from dotenv import load_dotenv
from PIL import Image
import streamlit as st

load_dotenv()  # Load environment variables from .env file

# Ensure your .env file uses GOOGLE_API_KEY
client = genai.Client(api_key=os.getenv("GOOGLE-API-KEY"))


def get_gemini_response(system_prompt, image, user_input):
    # Pass prompt, PIL image, and user query as a list
    response = client.models.generate_content(
        model="gemini-3.6-flash",  # Use gemini-2.5-flash for understanding/analyzing images
        contents=[system_prompt, image, user_input],
    )
    return response.text


# Initialize Streamlit app
st.set_page_config(page_title="MultiLanguage Invoice Extractor")
st.header("MultiLanguage Invoice Extractor")

input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader(
    "Choose an image...", type=["jpg", "jpeg", "png"]
)

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", width=True)

submit = st.button("Tell me about the invoice")

system_prompt = """
You are a financial expert in understanding invoices.
I will upload an image of an invoice and you will have to 
answer my questions based on the input invoice image.
"""

if submit:
    if uploaded_file is not None:
        response = get_gemini_response(system_prompt, image, input_text)
        st.subheader("Response from Gemini API")
        st.write(response)
    else:
        st.error("Please upload an invoice image first.")