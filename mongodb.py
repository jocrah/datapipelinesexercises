"""Module for MySQL database operations using PyMySQL."""

import sys
from typing import Any
from pymongo import MongoClient

sys.path.append(".")
from config import (
    MONGO_COLLECTION,
    MONGO_DBNAME,
    MONGO_HOSTNAME,
    MONGO_PASSWORD,
    MONGO_USERNAME,
)


class MongoDBModel:
    """Represents a database model with a connection."""

    collection: Any

    def __init__(self):
        mongo_client = MongoClient(
            "mongodb://" + MONGO_HOSTNAME + ":27017/" + MONGO_DBNAME
        )

        # connect to the db where the collection resides
        mongo_db = mongo_client[MONGO_DBNAME]

        # choose the collection to query documents from
        self.collection = mongo_db[MONGO_COLLECTION]

    def insert(
        self,
        data: object,
    ):
        """Execute the given query and fetch all results."""
        return self.collection.insert_one(data)

    def fetch(
        self,
        query: object,
    ):
        """Execute the given query and fetch all results."""
        return self.collection.find(query, batch_size=3000)
