from backend.pdf_reader import extract_text_from_pdf
from backend.chunker import split_text
from backend.embeddings import create_embeddings




def build_vector_store(pdf_path):

    # 1. Extract text
    text = extract_text_from_pdf(pdf_path)

    print("Text extracted successfully.")

    # 2. Split text into chunks
    chunks = split_text(text, chunk_size=500, overlap=50)

    print("Number of chunks:", len(chunks))

    # 3. Create embeddings
    embeddings, vectorizer = create_embeddings(chunks)

    print("Embeddings created successfully.")
    print("Embedding dimensions:", len(embeddings[0]))

    return chunks, embeddings, vectorizer


if __name__ == "__main__":
    pdf_path = "data/documents/rag_test_knowledge.pdf"

    chunks, embeddings, vectorizer = build_vector_store(pdf_path)

    print("\n===== VECTOR STORE TEST =====")

    for i, chunk in enumerate(chunks):
        print(f"\nChunk {i + 1}:")
        print(chunk[:200])

    print("\nTotal chunks:", len(chunks))
    print("Embedding size:", len(embeddings[0]))