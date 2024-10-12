from pymongo import MongoClient
import datetime
import configparser

# load the mongo_config values
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
hostname = parser.get("mongo_config", "hostname")
username = parser.get("mongo_config", "username")
password = parser.get("mongo_config", "password")
database_name = parser.get("mongo_config", "database")
collection_name = parser.get("mongo_config", "collection")

# Establish a connection to the MongoDB server
mongo_client = MongoClient(
    "mongodb+srv://"
    + username
    + ":"
    + password
    + "@"
    + hostname
    + "/"
    + database_name
    + "?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
)

# Select the database and collection
mongo_db = mongo_client[database_name]
mongo_collection = mongo_db[collection_name]

# Define the events to be inserted
events = [
    {
        "event_id": 1,
        "event_timestamp": datetime.datetime.today(),
        "event_name": "signup",
    },
    {
        "event_id": 2,
        "event_timestamp": datetime.datetime.today(),
        "event_name": "pageview",
    },
    {
        "event_id": 3,
        "event_timestamp": datetime.datetime.today(),
        "event_name": "login",
    },
]

# Insert the events into the collection
for event in events:
    mongo_collection.insert_one(event)
