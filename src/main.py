from pymongo import MongoClient
import export
import src.similarity as similarity
import src.vectorize as vectorize


def main():
    # Example usage of the export module
    connection = MongoClient(
        "localhost", 27017, username="root", password="rootpassword"
    )
    export.export_to_mongodb(vectorize.get_course_vector(), connection)

    # simple REPL for similarity search
    print("Welcome to the Similarity Search REPL!")
    print("Type 'exit' to quit the program.")
    while True:
        user_input = input("Enter a similar course term (or 'exit' to quit): ")
        if (
            user_input.lower() == "exit"
            or user_input.lower() == "quit"
            or user_input.lower() == "q"
            or user_input.lower() == "e"
        ):
            break
        similar_courses = similarity.similarity_search(
            user_input, connection["course_db"]["vectorized_courses"]
        )
        print(f"Similar courses to '{user_input}': {similar_courses}")


if __name__ == "__main__":
    main()
