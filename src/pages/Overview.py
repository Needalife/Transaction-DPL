import plotly.express as px,streamlit as st,pandas as pd, numpy as np # type: ignore
import requests,os,sys,pymongo # type: ignore

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.mongo import mongo
from utils.gcp import readMongoURI

@st.cache_resource
def connectMongo():
    mongoHandler = mongo(readMongoURI(),'data')
    return mongoHandler

@st.cache_data
def getLatestRecords(records):
    job = connectMongo()   
    df = pd.json_normalize(list(job.getNewestRecords('raw',records)))
    return df.drop('_id', axis=1)

st.title("Overview")
number = st.slider("Latest records", 0, 100)

if st.checkbox('Show raw data'):
    st.dataframe(getLatestRecords(number))
    
st.subheader('Transaction Status')
status_timestamp = getLatestRecords(number)[["status","timestamp"]]
st.line_chart(status_timestamp,x='timestamp',y='status')


















