import math


def main(text):
    # Step 1: Split the text into words and get a list of unique words
    docs = [line.lower().split() for line in text.split('\n')]
    vocabulary = list(set(word for doc in docs for word in doc))

    # Step 2: Calculate term frequency (tf) and document frequency (df)
    tf = {}
    df = {}
    for word in vocabulary:
        df[word] = sum(word in doc for doc in docs)  # Simplified calculation for df
        tf[word] = [doc.count(word) / len(doc) for doc in docs]

    # Step 3: Calculate TF-IDF representation for each line
    tfidf_vectors = []
    for doc in docs:
        tfidf = []
        for word in vocabulary:
            tfidf_val = tf[word][docs.index(doc)] * math.log(len(docs) / df[word], 10)
            tfidf.append(tfidf_val)
        tfidf_vectors.append(tfidf)

    # Step 4: Calculate cosine similarity between each pair of lines (fixed indentation)
    max_similarity = float('-inf')
    most_similar_pair = ()
    for i in range(len(tfidf_vectors)):
        for j in range(i + 1, len(tfidf_vectors)):
            dot_product = sum(a * b for a, b in zip(tfidf_vectors[i], tfidf_vectors[j]))
            magnitude_i = math.sqrt(sum([val**2 for val in tfidf_vectors[i]]))
            magnitude_j = math.sqrt(sum([val**2 for val in tfidf_vectors[j]]))
            if magnitude_i * magnitude_j != 0:  # Check for zero magnitudes
                similarity = dot_product / (magnitude_i * magnitude_j)
                if similarity > max_similarity:
                    max_similarity = similarity
                    most_similar_pair = (i, j)

    # Return the indices of the most similar pair of lines as a tuple
    return most_similar_pair


text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

# Convert the result to string format
result = main(text)
output = f'({result[0]}, {result[1]})'
print(output)
