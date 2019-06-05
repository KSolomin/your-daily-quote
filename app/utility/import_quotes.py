# This is a script to populate database with some quotes
import pymongo

# TODO: Add exception handling, if DB is not running
db_client = pymongo.MongoClient('localhost', 27017)
database = db_client["quotes"]
collection = database["collection"]

# Making mock quotes
quotes = [{"author": 1, "quote": "text1", "category": ""},
          {"author": 2, "quote": "text2", "category": ""},
          {"author": 3, "quote": "text3", "category": ""}]

# Inserting them
for i in quotes:
    collection.insert_one(i)
