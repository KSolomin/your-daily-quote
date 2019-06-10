import os
from pymongo import MongoClient
import random
import yaml
import logging

from flask import Flask

# Setting global variables and defaults:
logfile = "./logs/app.log"

# For local execution:
# dbconfigfile = "./source/dbconfig.yaml"
dbconfigfile = "/var/dbconfig/dbconfig.yaml"

app = Flask(__name__)
logging.basicConfig(filename = logfile, level = logging.INFO)

def readCollectionFromMongo(host, port, dbname):
    db_client = MongoClient(host, port)   
    database = db_client[dbname]
    collection = database["collection"]
    return collection

def readDataBaseConfig(dbconfigfile):
    with open (dbconfigfile, "r") as configfile:
        try:
            config = yaml.safe_load(configfile)
            global db_host
            db_host = config["db"]["host"]
            global db_port
            db_port = config["db"]["port"]
            global db_name
            db_name = config["db"]["name"]
            global db_collection
            db_collection = config["db"]["collection"]
            app.logger.info("Successfully read config.")

        except yaml.YAMLError as exc:
            app.logger.error("Error reading database config.")

@app.route('/health')
def health():
    return '200'

@app.route('/random')
def randomquote():
    collection = readCollectionFromMongo(db_host, db_port, db_name)
    rand = random.randrange(collection.count())
    document = collection.find()[rand]
    return "<p1>" + document["quote"] + " </p1><i>" + document["author"] + "</i>"

# Starting application
if __name__ == '__main__':
    readDataBaseConfig(dbconfigfile)
    app.logger.info("Working with following database config:\nHost: " + str(db_host) + "\nPort: " + str(db_port) + "\nDatabase name: " + str(db_name))
    app.run(host='0.0.0.0', port=5000)