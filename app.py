import streamlit as st
import tempfile
import os
from lossless_compression import compress_pdf

uploaded_pdf = st.file_uploader("Choose a file", type=['pdf'])
if uploaded_pdf is not None:
    st.write("File uploaded")
    temp_dir = tempfile.TemporaryDirectory()
    temp_file_path = os.path.join(temp_dir.name, uploaded_pdf.name)
    with open(temp_file_path, 'wb') as f:
        f.write(uploaded_pdf.read())
    st.write("File saved", temp_file_path)

    if st.button("Compress"):
        compress_pdf(temp_file_path, "smaller-new-file.pdf")
