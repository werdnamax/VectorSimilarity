# export the vectorized courses to mongoDB
from pymongo import MongoClient


def export_to_mongodb(embedded_course, connection):
    # Drop the database if it already exists
    connection.drop_database("course_db")
    db = connection["course_db"]

    # Insert the vectorized courses into the MongoDB collection
    collection = db["vectorized_courses"]
    collection.insert_many(embedded_course)
