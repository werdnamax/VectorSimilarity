import src.vectorize as vectorize


# calculate cosine similarity between two vectors
def cosine_similarity(vec1, vec2):
    dot_product = sum(x * y for x, y in zip(vec1, vec2))
    norm_vec1 = sum(x**2 for x in vec1) ** 0.5
    norm_vec2 = sum(x**2 for x in vec2) ** 0.5

    # avoid division by zero
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0
    else:
        return dot_product / (norm_vec1 * norm_vec2)


def similarity_search(query, connection):
    query_vector = vectorize.vectorize_text(query)
    all_data = list(connection.find({}))
    print(all_data)

    # calls cosine similarity function for each data point in the database keeping the title
    similar_words = []
    for data in all_data:
        similarity = cosine_similarity(query_vector, data["description"])
        if similarity > 0.5:
            similar_words.append((data["title"], similarity))

    return similar_words
