from sentence_transformers import SentenceTransformer

def load_embedding_model():
    """
    Loads and returns the sentence-transformer embedding model.
    """
    return SentenceTransformer("all-MiniLM-L6-v2")
