from sklearn.feature_extraction.text import TfidfVectorizer


def create_embeddings(chunks):
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=5000
    )

    embeddings = vectorizer.fit_transform(chunks).toarray()

    return embeddings, vectorizer