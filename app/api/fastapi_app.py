from fastapi import FastAPI, File, UploadFile
from src.preprocessing.preprocess import preprocess_text
from src.embeddings.generate_embeddings import generate_embedding
from src.matching.cosine_similarity import compute_similarity

app = FastAPI()

@app.post("/match")
async def match_resume_job(resume: UploadFile = File(...), job_desc: UploadFile = File(...)):
    # Read files
    resume_text = (await resume.read()).decode("utf-8")
    job_desc_text = (await job_desc.read()).decode("utf-8")

    # Preprocess text
    resume_processed = preprocess_text(resume_text)
    job_desc_processed = preprocess_text(job_desc_text)

    # Generate embeddings
    resume_embedding = generate_embedding(resume_processed)
    job_desc_embedding = generate_embedding(job_desc_processed)

    # Compute similarity
    similarity_score = compute_similarity(resume_embedding, job_desc_embedding)

    return {"similarity_score": similarity_score}