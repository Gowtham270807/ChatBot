from sklearn.feature_extraction.text import TfidfVectorizer

def create_embeddings(chunks):

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(chunks)

    return vectorizer, vectors