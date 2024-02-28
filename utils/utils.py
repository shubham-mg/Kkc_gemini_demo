import PyPDF2
import google.generativeai as genai
from PIL import Image

def get_pdf_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text

def get_gemini_response(input_prompt, content, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input_prompt, content, prompt])
    return response.text


def get_gemini_response_vision(input,image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    return response.text


def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")