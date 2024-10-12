"""Module for interacting with Google Cloud Storage."""

import os
import tempfile
from google.auth.credentials import AnonymousCredentials
from google.cloud import storage, exceptions as google_exceptions
from google.cloud.storage import Client

os.environ.setdefault("STORAGE_EMULATOR_HOST", "http://localhost:4443")


class CloudStorageService:
    """Handles cloud storage operations."""

    client: Client

    def __init__(self) -> None:
        client = storage.Client(
            credentials=AnonymousCredentials(),
            project="test",
        )
        self.client = client

    def upload_file_to_bucket(
        self, bucketname: str, filename: str, destination_file_name: str
    ):
        """Upload a file to the specified Google Cloud Storage bucket."""
        try:
            bucket = self.client.get_bucket(bucketname)
        except google_exceptions.NotFound:
            bucket = self.client.create_bucket(bucketname)

        try:
            blob = bucket.blob(destination_file_name)
            blob.upload_from_filename(filename=filename)
            print(
                f"File {filename} uploaded to {destination_file_name} in bucket {bucketname}."
            )
        except (IOError, OSError) as e:
            print(f"An error occurred while handling the file: {e}")
        except google_exceptions.GoogleCloudError as e:
            print(f"An error occurred during the Google Cloud operation: {e}")

    def get_files_from_bucket(self):
        """List all buckets in the cloud storage."""
        # List the Buckets
        for bucket in self.client.list_buckets():
            print(f"Bucket: {bucket.name}\n")

            # List the Blobs in each Bucket
            for blob in bucket.list_blobs():
                print(f"Blob: {blob.name}")

                # Print the content of the Blob
                b = bucket.get_blob(blob.name)
                with tempfile.NamedTemporaryFile() as temp_file:
                    b.download_to_filename(temp_file.name)
                    temp_file.seek(0, 0)
                    print(temp_file.read(), "\n")
