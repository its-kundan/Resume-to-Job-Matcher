import streamlit as st
from src.preprocessing.preprocess import preprocess_text
from src.embeddings.generate_embeddings import generate_embedding
from src.matching.cosine_similarity import compute_similarity

import sys
from pathlib import Path

# Add the project root directory to sys.path
project_root = Path(__file__).resolve().parents[2]  # Adjust the number of parents based on your folder depth
sys.path.append(str(project_root))

# Now import from src
from src.preprocessing.preprocess import preprocess_text
from src.embeddings.generate_embeddings import generate_embedding
from src.matching.cosine_similarity import compute_similarity
# Streamlit App
st.title("Resume-to-Job Matcher")

# File uploaders
resume_file = st.file_uploader("Upload Resume", type=["txt", "pdf"])
job_desc_file = st.file_uploader("Upload Job Description", type=["txt", "pdf"])

if resume_file and job_desc_file:
    # Read files
    resume_text = resume_file.read().decode("utf-8")
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