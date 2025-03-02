from transformers import pipeline
import numpy as np

# Load pre-trained model for embeddings
embedder = pipeline("feature-extraction", model="sentence-transformers/all-MiniLM-L6-v2")

def generate_embedding(text):
    """
    Generate embeddings for a given text using a pre-trained model.
    """
    embedding = embedder(text)
    return np.mean(embedding[0], axis=0)  # Average embeddings for all tokens