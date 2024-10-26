import sys
import datetime

sys.path.append(".")
from mongodb import MongoDBModel


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
    MongoDBModel().insert(event)
