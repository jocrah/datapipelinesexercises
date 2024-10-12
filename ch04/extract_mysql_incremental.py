"""Module for extracting data from MySQL database incrementally"""

import csv
import sys

sys.path.append(".")

from cloud_storage import CloudStorageService
from mysql import MySQLModel


M_QUERY = "SELECT * FROM Orders WHERE LastUpdated > %s;"
LOCAL_FILENAME = "order_extract.csv"

LAST_UPDATED = "1900-01-01"

results = MySQLModel().fetch(query=M_QUERY, args=(LAST_UPDATED,))

with open(LOCAL_FILENAME, "w", encoding="utf-8") as fp:
    csv_w = csv.writer(fp, delimiter="|")
    csv_w.writerows(results)

fp.close()

CloudStorageService().upload_file_to_bucket(
    bucketname="test-bucket",
    filename=LOCAL_FILENAME,
    destination_file_name=f"orders/{LOCAL_FILENAME}",
)

CloudStorageService().get_files_from_bucket()
