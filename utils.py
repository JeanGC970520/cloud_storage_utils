import os
from dotenv import load_dotenv
from google.cloud import storage

# Loading enviroment variables
load_dotenv(".env")

BUCKET_NAME = os.getenv("BUCKET_NAME")

def upload_file(bucket_name: str, file_path: str):
    # Create Cloud Storage client
    client = storage.Client() # TODO: Verify if its necessary use a Service Account

    # Get the Bucket
    bucket = client.get_bucket(bucket_name)

    # Create a BLOB (Binary Large Object) object from the file
    file_name = file_path.replace("\\", "/").split("/")[-1]
    blob = bucket.blob(file_name)

    # Upload the file
    blob.upload_from_filename(file_path)
    print(f"File {file_name} uploaded to {blob.public_url}")

def rename_file(bucket_name: str, old_name: str, new_name:str):
    # Create Cloud Storage client
    client = storage.Client()

    # Get a Bucket object
    bucket = client.get_bucket(bucket_name)

    # Create a BLOB (Binary Large Object) object from the file
    blob = bucket.blob(old_name)

    # Renaming the file
    bucket.rename_blob(blob, new_name)
    print(f"File {old_name} renamed to {new_name}")

def check_file_existence(bucket_name: str, file_name: str):
    # Create Cloud Storage client
    client = storage.Client()

    # Get a Bucket object
    bucket = client.get_bucket(bucket_name)

    # Create BLOB (Binary Large Object) object from the file
    blob = bucket.blob(file_name)

    return blob.exists()

def delete_file(bucket_name:str, file_name:str):
    # Create Cloud Storage client
    client = storage.Client()

    # Get a Bucket object 
    bucket = client.get_bucket(bucket_name)

    # Get BLOB object from the file
    blob = bucket.get_blob(file_name)

    # Delete the file from the Bucket
    blob.delete()

def push_to_cloud_storage(bucket_name:str, file_path:str):
    # Verify if the file exists}
    file_name = file_path.replace("\\", "/").split("/")[-1]
    exists = check_file_existence(bucket_name, file_name)
    if not exists:
        upload_file(bucket_name, file_path)
        return 
    # If exists rename it and upload the last version
    name, extension = file_name.split(".")
    deprecated_file = name + "-deprecated." + extension
    if check_file_existence(bucket_name, deprecated_file):
        delete_file(bucket_name, deprecated_file)
    rename_file(bucket_name, file_name, deprecated_file)
    upload_file(bucket_name, file_path)
    