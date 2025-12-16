from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    """
    Splits documents into overlapping chunks.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=80
    )

    chunks = splitter.create_documents(documents)
    return chunks


if __name__ == "__main__":
    from preprocessing.text_builder import build_documents

    docs = build_documents()
    chunks = chunk_documents(docs)

    print(f"✅ Created {len(chunks)} chunks")
    print("\nSample chunk:\n")
    print(chunks[0].page_content)
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    """
    Splits documents into overlapping chunks.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=80
    )

    chunks = splitter.create_documents(documents)
    return chunks


if __name__ == "__main__":
    from preprocessing.text_builder import build_documents

    docs = build_documents()
    chunks = chunk_documents(docs)

    print(f"✅ Created {len(chunks)} chunks")
    print("\nSample chunk:\n")
    print(chunks[0].page_content)
