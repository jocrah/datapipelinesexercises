import csv
import datetime
from datetime import timedelta
import sys

sys.path.append(".")
from cloud_storage import CloudStorageService
from mongodb import MongoDBModel


start_date = datetime.datetime.today() + timedelta(days=-1)
end_date = start_date + timedelta(days=1)

mongo_query = {
    "$and": [
        {"event_timestamp": {"$gte": start_date}},
        {"event_timestamp": {"$lt": end_date}},
    ]
}

event_docs = MongoDBModel().fetch(query=mongo_query)

# create a blank list to store the results
all_events = []

# iterate through the cursor
for doc in event_docs:
    # Include default values
    event_id = str(doc.get("event_id", -1))
    event_timestamp = doc.get("event_timestamp", None)
    event_name = doc.get("event_name", None)

    # add all the event properties into a list
    current_event = []
    current_event.append(event_id)
    current_event.append(event_timestamp)
    current_event.append(event_name)

    # add the event to the final list of events
    all_events.append(current_event)

export_file = "export_file.csv"

with open(export_file, "w", encoding="utf-8") as fp:
    csvw = csv.writer(fp, delimiter="|")
    csvw.writerows(all_events)

fp.close()

CloudStorageService().upload_file_to_bucket(
    bucketname="test-bucket",
    filename=export_file,
    destination_file_name=f"events/{export_file}",
)

CloudStorageService().get_files_from_bucket()
