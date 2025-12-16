import faiss
import numpy as np
from utils.config import FAISS_DIR, create_directories

def build_faiss_index(embeddings):
    create_directories()

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    faiss.write_index(index, str(FAISS_DIR / "shl.index"))
    return index
