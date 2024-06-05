import functions_framework
import json,random,string, time, os
from datetime import datetime
from google.cloud import storage
from log import loggingData
from producer import generateRandomID, getRandomName, getRandomType, getEmail

def generateData():
    name = getRandomName()
    return {
        "transaction_id": f"{generateRandomID()}",
        "name" : f"{name}",
        "type" : f"{getRandomType()}",
        "status" : f"{random.choice(['error','success','ongoing'])}",
        "email": f"{getEmail(name.lower())}",
        "timestamp": f"{datetime.now()}"
    }

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name, if_generation_match=0)

@functions_framework.http
def run(request):

    file_path = 'transaction.json'
    try:
        with open('transaction.json', 'w') as file:
            file.write('[')

        arr = range(random.randint(1,10))
        for n in arr:
            data = generateData()

            with open(file_path, 'a') as file:
                file.write(json.dumps(data, indent=4))
                if n != arr[-1]:
                    file.write(',\n')
                else:
                    file.write(']')
            
            number = n + 1

        object_name = f'{datetime.now().strftime("%d-%m-%Y_%H:%M")}'
        upload_blob('engineering_experience','transaction.json',object_name)
        
        with open(file_path, 'r') as file:
            file_content = file.read()

        loggingData(file_content)
        
        return file_content

    except Exception as e:
        return f'{e}'


