# app/api/fastapi_app.py
from fastapi import FastAPI, File, UploadFile, HTTPException
from src.preprocessing.preprocess import preprocess_text
from src.embeddings.generate_embeddings import generate_embedding
from src.matching.cosine_similarity import compute_similarity

app = FastAPI()

@app.post("/match")
async def match_resume_job(resume: UploadFile = File(...), job_desc: UploadFile = File(...)):
    # Read and preprocess files with error handling
    try:
        if resume.content_type == "application/pdf":
            resume_text = read_pdf(await resume.read())
        else:
            resume_text = (await resume.read()).decode("utf-8")

        if job_desc.content_type == "application/pdf":
            job_desc_text = read_pdf(await job_desc.read())
        else:
            job_desc_text = (await job_desc.read()).decode("utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read files: {e}")

    try:
        # Preprocess text
        resume_processed = preprocess_text(resume_text)
        job_desc_processed = preprocess_text(job_desc_text)

        # Generate embeddings
        resume_embedding = generate_embedding(resume_processed)
        job_desc_embedding = generate_embedding(job_desc_processed)

        # Compute similarity
        similarity_score = compute_similarity(resume_embedding, job_desc_embedding)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing error: {e}")

    return {"similarity_score": similarity_score}
