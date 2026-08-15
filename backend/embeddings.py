from sklearn.feature_extraction.text import TfidfVectorizer


def create_embeddings(chunks):
    # Remove empty chunks
    chunks = [chunk.strip() for chunk in chunks if chunk and chunk.strip()]

    if not chunks:
        raise ValueError("No usable text found in the document.")

    # Lightweight TF-IDF vectorization
    # Do not remove English stop words because some PDFs may contain
    # short or limited vocabulary text.
    vectorizer = TfidfVectorizer(
        max_features=5000,
        lowercase=True,
        token_pattern=r"(?u)\b\w+\b"
    )

    embeddings = vectorizer.fit_transform(chunks).toarray()

    return embeddings, vectorizer