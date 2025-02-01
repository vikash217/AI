import os
import base64
import streamlit as st
from streamlit.components.v1 import html
import io
from PIL import Image 
import fitz
import google.generativeai as genai

st.set_page_config(
    page_title= "Venturesathi",
    page_icon="Logo.jpg",
)

# hide_streamlit_style = """
#     <style>
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}
#         header {visibility: hidden;}
#         </style>
#     """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)

api_key = os.environ.get('GOOGLE_API_KEY')

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        
        first_page = pdf_document.load_page(0)
        pix = first_page.get_pixmap()
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")


st.header("Venturesthi Resume Stack Ranking")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume(PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Match")

input_prompt1 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of  ATS functionality and recruitment(Finding Best Match of Resume according to Job Description), 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts in a structured tabular Format.
"""


if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("Result: ")
        st.write(response)
    else:
        st.write("upload the resume")

# elif submit3:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt3, pdf_content, input_text)
#         st.subheader("Result: ")
#         st.write(response)
#     else:
#         st.write("Please upload the resume")
