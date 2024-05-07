import os, sys,datetime
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'data'))
import transactionProducer #add module to path then import 
from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name, if_generation_match=0)

    print(
        f"File {source_file_name} uploaded to {bucket_name} as {destination_blob_name}."
    )

def run():
    current_time = datetime.datetime.now().strftime("%d/%m_%H:%M:%S")
    object_name = f'transaction_data_{current_time}'
    
    transactionProducer.run()
    upload_blob('engineering_experience','transaction.json',object_name)

if __name__ == '__main__':
    run()