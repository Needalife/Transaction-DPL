import json

def loggingData(data):
    for i in json.loads(f"[{data.strip('[ ]').strip()}]"):
        print(i)