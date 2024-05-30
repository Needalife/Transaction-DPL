import requests #type:ignore

def read():
    response = requests.get("https://us-central1-project-finance-400806.cloudfunctions.net/query-data")
    if response.status_code == 200:
        return response
    else:
        return response.status_code