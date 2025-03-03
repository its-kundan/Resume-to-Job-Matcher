import sys
from pathlib import Path

# Add the project root directory to sys.path
project_root = Path(__file__).resolve().parents[2]  # Adjust the number of parents based on your folder depth
sys.path.append(str(project_root))

# Now import from src
from src.preprocessing.preprocess import preprocess_text
from src.embeddings.generate_embeddings import generate_embedding
from src.matching.cosine_similarity import compute_similarity
from src.Courses import ds_course, web_course, android_course, ios_course, uiux_course, resume_videos, interview_videos
from src.components.navigation_bar import navigation_bar  # Import navigation bar
from src.components.footer import footer  # Import footer

import streamlit as st
import pandas as pd
import base64
import time
import datetime
import pdfplumber  # For extracting text from PDF files
import random


def fetch_yt_video(link):
    """
    Fetch YouTube video title (placeholder function).
    """
    return f"Video Title for {link}"


def course_recommender(course_list):
    """
    Recommend courses based on the skills gap.
    """
    st.subheader("**Courses & Certificates🎓 Recommendations**")
    c = 0
    rec_course = []
    no_of_reco = st.slider('Choose Number of Course Recommendations:', 1, 10, 4)
    random.shuffle(course_list)
    for c_name, c_link in course_list:
        c += 1
        st.markdown(f"({c}) [{c_name}]({c_link})")
        rec_course.append(c_name)
        if c == no_of_reco:
            break
    return rec_course


def extract_text_from_pdf(file):
    """
    Extract text from a PDF file using pdfplumber.
    """
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text


def calculate_resume_score(resume_text):
    """
    Calculate resume score based on the presence of key sections.
    """
    resume_score = 0
    if 'Objective' in resume_text:
        resume_score += 20
        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>[+] Awesome! You have added Objective</h4>''',
                    unsafe_allow_html=True)
    else:
        st.markdown(
            '''<h4 style='text-align: left; color: #fabc10;'>[-] Add a Career Objective to improve your resume.</h4>''',
            unsafe_allow_html=True)

    if 'Skills' in resume_text:
        resume_score += 20
        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>[+] Great! You have added Skills</h4>''',
                    unsafe_allow_html=True)
    else:
        st.markdown(
            '''<h4 style='text-align: left; color: #fabc10;'>[-] Add a Skills section to improve your resume.</h4>''',
            unsafe_allow_html=True)

    if 'Projects' in resume_text:
        resume_score += 20
        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>[+] Awesome! You have added Projects</h4>''',
                    unsafe_allow_html=True)
    else:
        st.markdown(
            '''<h4 style='text-align: left; color: #fabc10;'>[-] Add a Projects section to improve your resume.</h4>''',
            unsafe_allow_html=True)

    if 'Experience' in resume_text:
        resume_score += 20
        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>[+] Great! You have added Experience</h4>''',
                    unsafe_allow_html=True)
    else:
        st.markdown(
            '''<h4 style='text-align: left; color: #fabc10;'>[-] Add an Experience section to improve your resume.</h4>''',
            unsafe_allow_html=True)

    if 'Education' in resume_text:
        resume_score += 20
        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>[+] Great! You have added Education</h4>''',
                    unsafe_allow_html=True)
    else:
        st.markdown(
            '''<h4 style='text-align: left; color: #fabc10;'>[-] Add an Education section to improve your resume.</h4>''',
            unsafe_allow_html=True)

    return resume_score


# from src.components.navigation_bar import navigation_bar  # Import navigation bar

def main():
    st.set_page_config(page_title="Resume-to-Job Matcher", page_icon="📄")

    # Add navigation bar
    # navigation_bar()

    st.title("Resume-to-Job Matcher")
    st.markdown(
        '''<h4 style='text-align: left; color: #d73b5c;'>* Upload your resume and job description to get started.</h4>''',
        unsafe_allow_html=True)

    # File uploaders
    resume_file = st.file_uploader("Upload Your Resume", type=["pdf", "txt"])
    job_desc_file = st.file_uploader("Upload Job Description", type=["pdf", "txt"])

    if resume_file and job_desc_file:
        # Read files
        if resume_file.name.endswith(".pdf"):
            resume_text = extract_text_from_pdf(resume_file)
        else:
            resume_text = resume_file.read().decode("utf-8")

        if job_desc_file.name.endswith(".pdf"):
            job_desc_text = extract_text_from_pdf(job_desc_file)
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
        st.header("**Resume Analysis**")



        # Resume Score Calculation
        st.subheader("**Resume Score**")
        resume_score = calculate_resume_score(resume_text)

        st.markdown(f"<h1 style='text-align: center; color: #1ed760;'>{resume_score}/100</h1>", unsafe_allow_html=True)
        st.subheader("**Similarity Score**")
        st.markdown(f"<h1 style='text-align: center; color: #1ed760;'>{similarity_score:.2f}</h1>",
                    unsafe_allow_html=True)
        # Skill Recommendations
        st.subheader("**Skill Recommendations💡**")
        recommended_skills = ["Data Visualization", "Machine Learning", "Python", "SQL"]
        st.markdown(
            '''<h4 style='text-align: left; color: #1ed760;'>Adding these skills will boost your resume:</h4>''',
            unsafe_allow_html=True)
        for skill in recommended_skills:
            st.markdown(f"- {skill}")

        # Course Recommendations
        st.subheader("**Course Recommendations🎓**")
        course_recommender(ds_course)  # Use ds_course from Courses.py

        # YouTube Videos
        st.header("**Bonus Videos for Resume Writing & Interview Tips💡**")
        resume_vid = random.choice(resume_videos)  # Use resume_videos from Courses.py
        interview_vid = random.choice(interview_videos)  # Use interview_videos from Courses.py
        st.subheader("✅ **Resume Writing Tips**")
        st.video(resume_vid)
        st.subheader("✅ **Interview Preparation Tips**")
        st.video(interview_vid)

    # Add footer
    footer()


if __name__ == "__main__":
    main()