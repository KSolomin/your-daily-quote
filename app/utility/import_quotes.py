# This is a script to populate database with some quotes
import pymongo

# TODO: Add exception handling, if DB is not running
db_client = pymongo.MongoClient('localhost', 27017)
database = db_client["quotes"]
collection = database["collection"]

# Making mock quotes
quotes = [{"author": "Winston Churchill", "quote": "If you're going through hell, keep going.", "category": ""},
          {"author": "Abraham Lincoln", "quote": "Better to remain silent and be thought a fool than to speak out and remove all doubt.", "category": ""},
          {"author": "Albert Einstein", "quote": "The difference between stupidity and genius is that genius has its limits.", "category": ""},
          {"author": "Charles de Gaulle", "quote": "He who laughs last didn’t get the joke.", "category": ""},
          {"author": "George Carlin", "quote": "Have you ever noticed that anybody driving slower than you is an idiot, and anyone going faster than you is a maniac?", "category": ""}]

# Inserting them
for i in quotes:
    collection.insert_one(i)
