import os
import streamlit as st
import fitz
import google.generativeai as genai

st.set_page_config(page_title="Icubes Resume Scorer")
st.header("Icubes Resume Scorer")

api_key = os.environ.get('GOOGLE_API_KEY')
if not api_key:
    st.error("API key not found. Please set 'GOOGLE_API_KEY' as an environment variable.")
else:
    genai.configure(api_key=api_key)

def extract_pdf_text(uploaded_file):
    try:
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in pdf_document:
            text += page.get_text()
        return text.strip()
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return None

def get_gemini_response(job_description, resume_text, prompt):
    try:
        model = genai.GenerativeModel('gemini-pro-vision')  
        response = model.generate_content([prompt, f"Job Description:\n{job_description}", f"Resume:\n{resume_text}"])
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"

input_prompt = """
You are an expert ATS (Applicant Tracking System) evaluator. Your task is to analyze the resume and compare it with the provided job description.
Return your results in the following structured format:

1. Match Percentage: (numerical value with %)
2. Missing Keywords: (bullet list)
3. Final Thoughts: (brief summary of how well the resume matches the job description)

Be objective, concise, and base your evaluation only on the textual content.
"""

job_description = st.text_area("Paste Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if st.button("Match"):
    if not job_description:
        st.warning("Please enter a job description.")
    elif uploaded_file is None:
        st.warning("Please upload a resume PDF.")
    else:
        with st.spinner("Analyzing resume..."):
            resume_text = extract_pdf_text(uploaded_file)
            if resume_text:
                result = get_gemini_response(job_description, resume_text, input_prompt)
                st.subheader("Result:")
                st.write(result)









# import os
# import base64
# import streamlit as st
# from streamlit.components.v1 import html
# import io
# from PIL import Image 
# import fitz
# import google.generativeai as genai

# st.set_page_config(
#     page_title= "Icubes",
#     # page_icon="Logo.jpg",
# )

# # hide_streamlit_style = """
# #     <style>
# #         #MainMenu {visibility: hidden;}
# #         footer {visibility: hidden;}
# #         header {visibility: hidden;}
# #         </style>
# #     """
# # st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# api_key = os.environ.get('GOOGLE_API_KEY')

# def get_gemini_response(input, pdf_content, prompt):
#     model = genai.GenerativeModel('Gemini 2.5 Flash Preview 05-20')
#     response = model.generate_content([input, pdf_content[0], prompt])
#     return response.text

# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        
#         first_page = pdf_document.load_page(0)
#         pix = first_page.get_pixmap()
#         image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
#         img_byte_arr = io.BytesIO()
#         image.save(img_byte_arr, format='JPEG')
#         img_byte_arr = img_byte_arr.getvalue()

#         pdf_parts = [
#             {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file uploaded")


# st.header("Icubes Resume Scorer")
# input_text = st.text_area("Job Description: ", key="input")
# uploaded_file = st.file_uploader("Upload your resume(PDF)...", type=["pdf"])

# if uploaded_file is not None:
#     st.write("PDF Uploaded Successfully")

# submit1 = st.button("Match")

# input_prompt1 = """
# You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of  ATS functionality and recruitment(Finding Best Match of Resume according to Job Description), 
# your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
# the job description. First the output should come as percentage and then keywords missing and last final thoughts in a structured tabular Format.
# """


# if submit1:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt1, pdf_content, input_text)
#         st.subheader("Result: ")
#         st.write(response)
#     else:
#         st.write("upload the resume")

# # elif submit3:
# #     if uploaded_file is not None:
# #         pdf_content = input_pdf_setup(uploaded_file)
# #         response = get_gemini_response(input_prompt3, pdf_content, input_text)
# #         st.subheader("Result: ")
# #         st.write(response)
# #     else:
# #         st.write("Please upload the resume")
