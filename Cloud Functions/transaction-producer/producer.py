import functions_framework
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
    "Oliver"]
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

def getEmail(name):
    email_format = '@gmail.com'
    return name + email_format 