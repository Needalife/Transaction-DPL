import pymongo #type:ignore
    
class mongo:
    def __init__(self,uri,database):
        self.uri = uri
        self.client = pymongo.MongoClient(self.uri)   
        self.database = self.client[f'{database}']
    
    def getNewestRecords(self,collection_name,number_of_records):
        collection = self.database[f'{collection_name}']
        return collection.find().sort('_id', -1).limit(number_of_records)

    def getTotalRecords(self,collection_name):
        collection = self.database[f'{collection_name}']
        return collection.count_documents({})
