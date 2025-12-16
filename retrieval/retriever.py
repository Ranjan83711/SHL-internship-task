import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from utils.config import FAISS_DIR

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_chunks(query, chunks, top_k=5):
    """
    Perform semantic search over FAISS index and return top-k chunks.
    """
    index_path = FAISS_DIR / "shl.index"
    index = faiss.read_index(str(index_path))

    query_embedding = model.encode([query])
    scores, indices = index.search(
        np.array(query_embedding), top_k
    )

    results = []
    for idx in indices[0]:
        results.append(chunks[idx].page_content)

    return results
