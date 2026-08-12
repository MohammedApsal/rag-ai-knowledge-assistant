from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    embeddings = model.encode(chunks)

    return embeddings


if __name__ == "__main__":

    chunks = [
        "Artificial Intelligence is the field of computer science.",
        "RAG combines document retrieval with a language model.",
        "A RAG system retrieves relevant information from a knowledge base."
    ]

    embeddings = create_embeddings(chunks)

    print("===== EMBEDDINGS =====")
    print("Number of chunks:", len(embeddings))
    print("Embedding size:", len(embeddings[0]))

    print("\nFirst embedding:")
    print(embeddings[0])