import functions_framework, pymongo
from utils import log, write_read
from google.cloud import storage
from datetime import datetime

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def run(cloud_event):
    current_time = datetime.now().strftime("%d-%m-%Y_%H:%M")
    log(cloud_event)
    
    try:
        uri = "mongodb+srv://gauakanguyen:AOMhWKFdmlSO6kcU@transactiondata.wecxmij.mongodb.net/?retryWrites=true&w=majority&appName=transactionData"
        client = pymongo.MongoClient(uri)
        
        database = client['data']
        collection = database['raw']
        
        data = write_read('engineering_experience',f"{current_time}")
        count = 0
        for i in data:
            print(i)
            count += 1
            collection.insert_one(i)
            
        print(f"Successfully export {count} records to MongoDB")
    except Exception as e:
        print(f"Operation fail: {e}")
