from gensim.models import KeyedVectors
import json

# Load the pre-trained Word2Vec model
model_path = "model/GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

with open("courses.json", "r") as f:
    course_data = json.load(f)[1:]


def embedding(text):
    try:
        return model[
            text.lower()
            .replace(",", "")
            .replace(".", "")
            .replace("!", "")
            .replace("?", "")
            .replace(";", "")
            .replace(":", "")
            .replace("-", " ")
        ]
    except KeyError as e:
        print(f"Word not in vocabulary: {e}")
        return None


def vectorize_text(text):
    words = text.split()
    if text == "":
        return None
    if len(words) > 1:
        vector = sum(
            embedding(word) for word in words if embedding(word) is not None
        ) / len(words)
    else:
        vector = embedding(text)
    return vector.tolist() if vector is not None else None

    # print(f"Course: {text}")
    # print(f"Vector: {vector}\n")


# Function to get the vector representation of a word
def get_course_vector():
    embedded_course = []

    for course in course_data:

        current_course = {
            "title": course["title"],
            "description": vectorize_text(course["description"]),
        }
        embedded_course.append(current_course)

    # print(embedded_course)
    return embedded_course