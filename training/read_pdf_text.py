import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import requests
import tempfile
import os
import re


def clean_text(input_text):
    """
        Clean the text by removing unwanted characters and excessive spaces.
    """
    cleaned_text = re.sub(r'[\n\x0c]+', ' ', input_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    cleaned_text = re.sub(r'[^\x00-\x7F]+', '', cleaned_text)
    cleaned_text = cleaned_text.strip()

    return cleaned_text

def read_pdf_text_from_url(pdf_url):
    """
        Read the text from a PDF file.
    """
    temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
    response = requests.get(pdf_url)
    temp_pdf.write(response.content)
    temp_pdf.close()
    pdf_path = temp_pdf.name
    images = convert_from_path(pdf_path)
    text_content = ""

    for image in images:
        text = pytesseract.image_to_string(image)
        text_content += text + "\n"

    if pdf_path.endswith('.pdf') and os.path.exists(pdf_path):
        os.unlink(pdf_path)
    
    return clean_text(text_content)



