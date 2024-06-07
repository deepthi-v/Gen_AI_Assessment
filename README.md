# Gen_AI_Assessment
Gen_AI_Assessment
This Python script automates the analysis of financial statements for compliance with regulatory standards. The script uses Streamlit for the user interface, allowing users to upload financial statements in PDF or image formats. The core functionalities include:

Preprocessing: Converts PDF and image files to text using pdfplumber and pytesseract.

Information Extraction: Uses the OpenAI API to extract key financial metrics from the text.

Compliance Analysis: Checks the extracted financial metrics for compliance with regulatory standards using the OpenAI API.

Summarization: Generates a summary of the financial metrics and compliance analysis using the OpenAI API.

Regulatory Retrieval: Retrieves relevant regulatory information using the OpenAI API.
