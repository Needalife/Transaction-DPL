import altair as alt,streamlit as st,pandas as pd, numpy as np # type: ignore
import requests,time # type: ignore
from utils.mongo import *

@st.cache_resource
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

        df['timestamp'] = pd.to_datetime(df['timestamp']).dt.floor('min')

        # Transform data to count each status per timestamp
        status_count = df.groupby(['timestamp', 'status']).size().reset_index(name='count')
        status_count['timestamp'] = status_count['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
        # Plotting the stacked bar chart
        st.subheader('Transaction Status')
        chart = alt.Chart(status_count).mark_bar().encode(
            x='timestamp:T',
            y='count:Q',
            color=alt.Color('status:N', scale=alt.Scale(domain=['error', 'ongoing', 'success'],
                                                        range=['#FF4B4B', '#FFD700', '#32CD32'])),
        ).properties(
            width='container',
            height=400
        ).interactive()

        st.altair_chart(chart,use_container_width=True)
    except Exception as e:
        st.error(f'Error occurred during: {e}', icon="🚨")

#UI start
st.set_page_config(layout="wide")
st.title("Overview")
placeholder = st.empty()

old_errors = 0
old_successes = 0
old_ongoing = 0

while True:
    sum_records = connectMongo().getTotalRecords('raw') 
    
    df = getLatestRecords(500)
    
    errors = df[df['status'] == 'error'].shape[0]
    successes = df[df['status'] == 'success'].shape[0]
    ongoing = df[df['status'] == 'ongoing'].shape[0]
    
    err_diff = errors - old_errors
    suc_diff = successes - old_successes
    ong_diff = ongoing - old_ongoing
    
    with placeholder.container():
        st.write(sum_records)
        kp1,kp2,kp3 = st.columns(3)
        
        kp1.metric(label="Success ✅",value=int(successes),delta=suc_diff)
        kp2.metric(label="Ongoing ⏳",value=int(ongoing),delta=ong_diff)
        kp3.metric(label="Errors ❌",value=int(errors),delta=err_diff)
            
        plotTransactionStatus(df)

    old_errors = errors
    old_successes = successes
    old_ongoing = ongoing
    
    time.sleep(60)













