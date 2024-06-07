import streamlit as st
from pathlib import Path
import pytesseract
import pdfplumber
from PIL import Image
import openai
import os


os.environ["HTTP_PROXY"] = "proxy.its.hpecorp.net:8080"
os.environ["HTTPS_PROXY"] = "proxy.its.hpecorp.net:8080"

# Set your OpenAI API key
openai.api_key = api_key
#OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Preprocessing functions
def preprocess_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def preprocess_image(file_path):
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    return text

# Information extraction function
def extract_information(text):
    prompt = f"Extract key metrics :\n{text}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500
    )
    return response.choices[0].text.strip()

# Compliance analysis function
def compliance_analysis(extracted_info):
    prompt = f"Analyze the following financial metrics for compliance :\n{extracted_info}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500
    )
    return response.choices[0].text.strip()

# Summarization function
def summarize_financial_statement(extracted_info):
    prompt = f"Summarize :\n{extracted_info}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

# RAG function to retrieve relevant regulations
def retrieve_regulations(query):
    prompt = f"Retrieve relevant details:\n{query}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500
    )
    return response.choices[0].text.strip()

# Streamlit app
def main():
    st.title("Automated Financial Statement Analysis")

    uploaded_file = st.file_uploader("Upload Financial Statement", type=["pdf", "png", "jpg", "jpeg"])
    if uploaded_file is not None:
        file_path = Path(uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        if file_path.suffix == ".pdf":
            text = preprocess_pdf(file_path)
        else:
            text = preprocess_image(file_path)

        extracted_info = extract_information(text)
        compliance_report = compliance_analysis(extracted_info)
        summary = summarize_financial_statement(extracted_info)

        st.subheader("Extracted Information")
        st.write(extracted_info)

        st.subheader("Compliance Report")
        st.write(compliance_report)

        st.subheader("Summary")
        st.write(summary)

        query = "current financial regulations"
        regulations = retrieve_regulations(query)
        st.subheader("Relevant Regulations")
        st.write(regulations)

if __name__ == "__main__":
    main()
