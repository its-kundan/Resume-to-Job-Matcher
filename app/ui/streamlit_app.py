# app/ui/streamlit_app.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st
import pdfplumber
from src.preprocessing.preprocess import preprocess_text
from src.embeddings.generate_embeddings import generate_embedding
from src.matching.cosine_similarity import compute_similarity

def read_pdf(file):
    with pdfplumber.open(file) as pdf:
        first_page = pdf.pages[0]
        return first_page.extract_text()

st.title("Resume-to-Job Matcher")

# File uploader
resume_file = st.file_uploader("Upload Resume", type=["txt", "pdf"])
job_desc_file = st.file_uploader("Upload Job Description", type=["txt", "pdf"])

if resume_file and job_desc_file:
    # Read files based on file type
    if resume_file.type == "application/pdf":
        resume_text = read_pdf(resume_file)
    else:
        resume_text = resume_file.read().decode("utf-8")

    if job_desc_file.type == "application/pdf":
        job_desc_text = read_pdf(job_desc_file)
    else:
        job_desc_text = job_desc_file.read().decode("utf-8")

    # Preprocess text
    resume_processed = preprocess_text(resume_text)
    job_desc_processed = preprocess_text(job_desc_text)

    # Generate embeddings
    resume_embedding = generate_embedding(resume_processed)
    job_desc_embedding = generate_embedding(job_desc_processed)

    # Compute similarity
    similarity_score = compute_similarity(resume_embedding, job_desc_embedding)

    # Display results
    st.write(f"Similarity Score: {similarity_score:.2f}")
    if similarity_score > 0.7:
        st.success("Strong Match!")
    elif similarity_score > 0.5:
        st.warning("Moderate Match.")
    else:
        st.error("Weak Match.")
