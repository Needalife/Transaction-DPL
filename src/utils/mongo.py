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
    
    def getRule(self):
        collection = self.database['rule']
        return collection.find_one({}, {"_id": 0})
    
    def setRule(self,max_record,amount_delete):
        collection = self.database['rule']
        query_filter = {"action": "Delete"}
        update_operation = {"$set": {"amount": amount_delete, "condition.max_records": max_record}}
        
        collection.update_one(query_filter,update_operation)