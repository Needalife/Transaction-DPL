import altair as alt,streamlit as st,pandas as pd, numpy as np # type: ignore
import requests,os,sys,pymongo # type: ignore

from src.utils import mongo
from src.utils import gcp

def connectMongo():
    response = requests.get("https://us-central1-project-finance-400806.cloudfunctions.net/get-mongo-uri")
        
    if response.status_code == 200:
        response.close()
    
    mongoHandler = mongo(response.text,'data')
    return mongoHandler

def getLatestRecords(records): #Don't cache data this, it will retrieve old data
    job = connectMongo()   
    df = pd.json_normalize(list(job.getNewestRecords('raw',records)))
    return df.drop('_id', axis=1)

def plotTransactionStatus(df):
    try:
        # Mapping status to numerical values for count purposes
        status_mapping = {'error': -1, 'ongoing': 0, 'success': 1}
        df['status_num'] = df['status'].map(status_mapping)

        df['timestamp'] = pd.to_datetime(df['timestamp']).dt.floor('T')

        # Transform data to count each status per timestamp
        status_count = df.groupby(['timestamp', 'status']).size().reset_index(name='count')

        # Plotting the stacked bar chart
        st.subheader('Transaction Status')
        chart = alt.Chart(status_count).mark_bar().encode(
            x='timestamp:T',
            y='count:Q',
            color=alt.Color('status:N', scale=alt.Scale(domain=['error', 'ongoing', 'success'],
                                                        range=['#FF4B4B', '#FFD700', '#32CD32'])),
        ).properties(
            width=800,
            height=400
        ).interactive()

        st.altair_chart(chart)
        st.success('Successfuly retrieve new data', icon="✅")
    except Exception as e:
        st.error(f'Error occurred during: {e}', icon="🚨")

#UI start
st.button("Reload")
st.title("Overview")
number = st.slider("Number of records", 0, 700)

df = getLatestRecords(number)
    
if st.checkbox('Show raw data'):
    st.dataframe(df)
    
plotTransactionStatus(df)

st.subheader('Type')














