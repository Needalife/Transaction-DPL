import json,random,string, time, os
from datetime import datetime

def generateRandomID():
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(50)])

def getRandomName():
    names = [
    "Jasmine",
    "Xavier",
    "Emily",
    "Alexander",
    "Olivia",
    "Ethan",
    "Isabella",
    "Liam",
    "Sophia",
    "Noah",
    "Mia",
    "Lucas",
    "Ava",
    "Benjamin",
    "Charlotte",
    "Jacob",
    "Amelia",
    "William",
    "Harper",
    "Michael",
    "Evelyn",
    "James",
    "Abigail",
    "Daniel",
    "Grace",
    "Samuel",
    "Lily",
    "Logan",
    "Natalie",
    "Oliver"
]
    random.shuffle(names)
    return names[0]

def getRandomType():
    transaction_types = [
        "Deposits",
        "Withdrawals",
        "Transfers",
        "Payments",
        "Wire Transfers",
        "Direct Debits",
        "Standing Orders",
        "Refunds",
        "Currency Conversions",
        "Investments"
    ]
    random.shuffle(transaction_types)
    return transaction_types[0]
    
def generateData(isLast: bool):
    data = {
        "transaction_id": f"{generateRandomID()}",
        "name" : f"{getRandomName()}",
        "type" : f"{getRandomType()}",
        "status" : f"{random.choice(['error','success','ongoing'])}",
        "timestamp": f"{datetime.now()}"
    }
    
    with open('transaction.json', 'a') as file:
        file.write(json.dumps(data,indent=4))
        if not isLast:
            file.write(',')
        else:
            file.write(']')
        file.write('\n')
    
    return data

def run():
    with open('transaction.json', 'w') as file:
        file.write('[')
        
    iterator = 0    
    try:
        while True:
            print(f'Generate data no.{iterator}...')
            time.sleep(0.5)
            print(generateData(isLast=False))
            time.sleep(10)
            print(f'...continue from session no.{iterator}')
            iterator += 1
            time.sleep(1)
    except KeyboardInterrupt:
        generateData(True)
        
if __name__ == "__main__":
    run()