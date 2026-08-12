import numpy as np

from backend.vector_store import build_vector_store
from backend.embeddings import model
from backend.llm import generate_answer


def search(query, chunks, embeddings, top_k=4):
    # Create embedding for the user's question
    query_embedding = model.encode([query])[0]

    # Calculate cosine similarity
    similarities = np.dot(embeddings, query_embedding) / (
        np.linalg.norm(embeddings, axis=1)
        * np.linalg.norm(query_embedding)
    )

    # Get the most relevant chunks
    top_indices = np.argsort(similarities)[::-1][:top_k]

    results = []

    for index in top_indices:
        results.append({
            "chunk": chunks[index],
            "score": float(similarities[index])
        })

    return results


if __name__ == "__main__":

    # Build vector store
    chunks, embeddings = build_vector_store()

    # User question
    query = "What is RAG?"

    # Search for relevant chunks
    results = search(query, chunks, embeddings)

    print("\n===== SEARCH RESULTS =====")

    for i, result in enumerate(results, start=1):
        print(f"\nResult {i}")
        print("Score:", result["score"])
        print("Text:", result["chunk"])

    # Combine retrieved chunks into context
    context = "\n\n".join(
        result["chunk"] for result in results
    )

    # Generate answer using Llama 3.2
    answer = generate_answer(query, context)

    print("\n===== FINAL RAG ANSWER =====")
    print(answer)