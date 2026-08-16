from backend.pdf_reader import extract_text_from_pdf
from backend.chunker import split_text
from backend.embeddings import create_embeddings




def build_vector_store(pdf_path):

    # 1. Extract text
    text = extract_text_from_pdf(pdf_path)

    print("Text extracted successfully.")
    print("Extracted characters:", len(text))
    print("First 200 characters:", repr(text[:200]))

    # 2. Split text into chunks
    chunks = split_text(text, chunk_size=500, overlap=50)

    print("Number of chunks:", len(chunks))

    # 3. Create embeddings
    embeddings, vectorizer = create_embeddings(chunks)

    print("Embeddings created successfully.")
    print("Embedding dimensions:", len(embeddings[0]))

    return chunks, embeddings, vectorizer