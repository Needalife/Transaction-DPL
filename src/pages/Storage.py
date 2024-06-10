import streamlit as st #type:ignore
import requests #type:ignore
from utils.mongo import *

def invokeSetBucketLifeCycle(age,bucket):
    try:
        url = "https://us-central1-project-finance-400806.cloudfunctions.net/setBucketLifeCycle"

        input_data = {"age": age,"bucket":bucket}

        response = requests.post(url,json = input_data)

        if response.status_code == 200:
            st.success(f"{response.text}")
        else:
            st.error(f"Status code: {response.status_code}")
    except Exception as e:
        st.error(f"{e}")

def invokeGetBucketLifeCycle(bucket):
    try:
        url = "https://us-central1-project-finance-400806.cloudfunctions.net/getBucketLifeCycleRule"

        input_data = {"bucket":bucket}

        response = requests.post(url,json = input_data)

        if response.status_code == 200:
            st.json(response.text.strip())
        else:
            st.error(f"Status code: {response.status_code}")

    except Exception as e:
        st.error(f"{e}")

@st.cache_resource
def connectMongo():
    response = requests.get("https://us-central1-project-finance-400806.cloudfunctions.net/get-mongo-uri")
    if response.status_code == 200:
        response.close()
    
    mongoHandler = mongo(response.text,'data')
    
    return mongoHandler

def getClusterRule():
    job = connectMongo()
    return job.getRule()
    
st.title("Bucket")

#Set bucket object lifecycle
with st.form("bucket"):
    st.write("Bucket lifecycle")
    age = st.number_input("Enter object age lifecycle")
    bucket = st.selectbox("Choose a bucket",("engineering_experience"," "))
    
    submitted = st.form_submit_button("set")
    if submitted:
        invokeSetBucketLifeCycle(int(age),bucket)

    st.write("Current Rules:")
    invokeGetBucketLifeCycle(bucket)

st.title("Cluster")

#Set cluster records lifecycle
with st.form("cluster"):
    st.write("Cluster lifecycle")
    maxRecord = st.slider("Set max number of record:",1000,20000,10000)
    
    submitted = st.form_submit_button("set")
    if submitted:
        pass
    
    st.write("Current Rules:")
    st.json(getClusterRule())
    