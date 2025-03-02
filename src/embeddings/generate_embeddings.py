# src/embeddings/generate_embeddings.py
from transformers import pipeline
import numpy as np

# Load pre-trained model for embeddings
embedder = pipeline("feature-extraction", model="sentence-transformers/all-MiniLM-L6-v2")

def generate_embedding(text):
    """
    Generate embeddings for a given text using a pre-trained model.
    Handles empty text inputs and returns a zero vector for embeddings.
    """
    if not text:
        return np.zeros(384)  # assuming the embedding size is 384
    try:
        embedding = embedder(text)
        return np.mean(embedding[0], axis=0)  # Average embeddings for all tokens
    except Exception as e:
        print(f"Error during embedding generation: {e}")
        return np.zeros(384)
