import streamlit as st
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file):
    pdf_reader=PdfReader(pdf_file)
    text=""

    #Iterate through each page and extract text
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text() + "\n"

    return text

def save_text_to_file(text, filename):
    with open(filename, 'w') as f:
        f.write(str(text))
    
#Streamlit app layout
st.title("PDF Uploader and Viewer")

uploaded_file = st.file_uploader("Upload a Pdf file")

if uploaded_file is not None:
    #Extract text from uploaded pdf
    pdf_text = extract_text_from_pdf(uploaded_file)
    #Display the extracted text
    st.subheader("Extracted Text")
    st.text_area("PDF Contents", pdf_text, height=300)

    #Provided option to save the text file
    if st.button("Save as Text File"):
        save_text_to_file(pdf_text, "extracted_text.txt")
        st.success("Text file saves successfully!")