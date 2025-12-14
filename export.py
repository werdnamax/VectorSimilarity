# export the vectorized courses to mongoDB
from pymongo import MongoClient

# eventually go in main


def export_to_mongodb(embedded_course, connection):
    connection.drop_database('course_db')
    db = connection['course_db']

    collection = db['vectorized_courses']
    collection.insert_many(embedded_course)
