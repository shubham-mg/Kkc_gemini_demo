from dotenv import load_dotenv
load_dotenv()  
import os 
import streamlit as st
import google.generativeai as genai 
from utils.utils import *

api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("API key not found. Please check your .env file.")
    

st.set_page_config(page_title="Gemini Demo")

st.header("Gemini Application")

input_type = st.radio("Choose input type:", ["Image", "Text"])

if input_type == "Image":
            
            st.header("Gemini Application")
            input=st.text_input("Input Prompt: ",key="input")
            uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
            image=""   
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image.", use_column_width=True)


            submit=st.button("Tell me about the image")

            input_prompt = """
                        You are an expert in understanding invoices and other documents.
                        You will receive input images as invoices &
                        you will have to extract the Full Name,Gross Income, Total Tax Paid and Deductions from the given input file
                        You will return the extract data in form of json file 
                        """

            ## If ask button is clicked

            if submit:
                image_data = input_image_setup(uploaded_file)
                response=get_gemini_response_vision(input_prompt,image_data,input)
                st.subheader("The Response is")
                st.write(response)


else:
    # Streamlit app code (unchanged parts omitted for brevity)
    input_prompt = """
                You are an expert in summarizing annual reports.
                Given a text input of an annual report, you will provide a concise summary.
        
                """
    ##initialize our streamlit app
    st.header("Annual Report Summary Application")
    prompt=st.text_input("Input Prompt: ",key="input")
    option = st.radio("Choose input method:", ("Paste Text", "Upload PDF"))

    if option == "Paste Text":
        input_text = st.text_area("Paste the text of the annual report here:")
    else:
        uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
        if uploaded_file is not None:
            input_text = get_pdf_text(uploaded_file)
        else:
            input_text = ""
                        
    submit = st.button("Summarize Report")            
    if submit:
        if input_text:  # Ensure there's input text before making the API call
            summary = get_gemini_response(input_prompt,input_text, prompt)
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.error("Please provide the text of the annual report.")
            
            
            