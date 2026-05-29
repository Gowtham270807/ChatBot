from sklearn.metrics.pairwise import cosine_similarity

def retrieve(
    query,
    vectorizer,
    vectors,
    chunks,
    top_k=3
):

    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        vectors
    ).flatten()

    top_indices = similarities.argsort()[-top_k:][::-1]

    return [
        chunks[i]
        for i in top_indices
    ]