import requests #type:ignore

class gcp:
    def __init__(self,type) -> None:
        self.type = type
    
    @staticmethod
    def readMongoURI():
        response = requests.get("https://us-central1-project-finance-400806.cloudfunctions.net/get-mongo-uri")
        
        if response.status_code == 200:
            response.close()
            return response.text
        else:
            return response.status_code

        