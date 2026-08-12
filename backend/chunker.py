def split_text(text, chunk_size=500, overlap=50):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


if __name__ == "__main__":
    sample_text = """
    Artificial Intelligence (AI) is the field of computer science focused on
    building systems that can perform tasks that normally require human
    intelligence.

    Retrieval-Augmented Generation (RAG) combines document retrieval with
    a language model. A RAG system searches a knowledge base for relevant
    information and uses that information to generate a grounded answer.
    """

    chunks = split_text(sample_text, chunk_size=100, overlap=20)

    print("===== CHUNKS =====")

    for i, chunk in enumerate(chunks, start=1):
        print(f"\n--- Chunk {i} ---")
        print(chunk)

    print(f"\nTotal chunks: {len(chunks)}")