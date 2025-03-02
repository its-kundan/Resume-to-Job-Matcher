from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(embedding1, embedding2):
    """
    Compute cosine similarity between two embeddings.
    """
    return cosine_similarity([embedding1], [embedding2])[0][0]