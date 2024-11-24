import streamlit as st
import sys
import os
from pathlib import Path
sys.path.append(os.path.join(Path(__file__).parent.parent))
print(sys.path)
from training.read_pdf_text import read_pdf_text_from_url
import pandas as pd
st.title("PDF Classification")

st.write("Add pdf url to classify it.")

pdf_url = st.text_input("Enter PDF URL")

if pdf_url:
    text = read_pdf_text_from_url(pdf_url)
    st.write(text)

    if st.button("Classify PDF"):
        prediction= [('lighting',0.9), ('fuses',0.05), ('cable',0.03), ('others',0.02)]
        st.write("Classification in progress...")
        # Display the prediction results
        st.subheader("Classification Results:")
        st.write(f"Predicted disease: {prediction[0][0]}")
        prediction = pd.DataFrame(prediction, columns=['disease', 'confidence (in %)'])
        # Visualize the results with a bar chart
        st.bar_chart(prediction, x='disease', y='confidence (in %)')
    else:
        st.warning("Please upload an image or select a sample image before classifying.")
