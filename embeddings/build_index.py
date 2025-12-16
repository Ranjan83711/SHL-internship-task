import numpy as np
from preprocessing.text_builder import build_documents
from preprocessing.chunker import chunk_documents
from embeddings.embedder import load_embedding_model
from embeddings.vector_store import build_faiss_index

def build_index():
    documents = build_documents()
    chunks = chunk_documents(documents)

    model = load_embedding_model()
    embeddings = model.encode(
        [c.page_content for c in chunks],
        show_progress_bar=True
    )

    index = build_faiss_index(np.array(embeddings))
    print(f"✅ FAISS index built with {index.ntotal} vectors")

    return chunks


if __name__ == "__main__":
    build_index()
