import altair as alt,streamlit as st,pandas as pd, numpy as np # type: ignore
import requests,time # type: ignore
from utils.mongo import *
from pymongo import MongoClient # type: ignore

@st.cache_resource
def connectMongo():
    response = requests.get("https://us-central1-project-finance-400806.cloudfunctions.net/get-mongo-uri")
    if response.status_code == 200:
        response.close()
    
    mongoHandler = mongo(response.text,'data')
    
    return mongoHandler

uri = "mongodb+srv://gauakanguyen:AOMhWKFdmlSO6kcU@transactiondata.wecxmij.mongodb.net/?retryWrites=true&w=majority&appName=transactionData"
client = MongoClient(uri)

database = client['data']
collection = database['raw']

rule = database['rule']
rule = rule.find_one({})
#UI start

placeholder = st.empty()

with placeholder.container():

    insert_count = 0
    delete_count = 0
    
    with collection.watch() as stream:
        for changes in stream:
            if changes['operationType'] == 'insert':
                insert_count += 1
            elif changes['operationType'] == 'delete':
                delete_count += 1
        
        st.write(f"Ins ops: {insert_count}")
        st.write(f"Del ops: {delete_count}")