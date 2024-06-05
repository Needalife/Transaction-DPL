import streamlit as st #type:ignore
import requests #type:ignore

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
        
st.title("Bucket")

#Set data lifecycle
with st.form("my_form"):
    st.write("Bucket Lifecycle")
    age = st.number_input("Enter object age lifecycle")
    bucket = st.selectbox("Choose a bucket",("engineering_experience"," "))
    
    submitted = st.form_submit_button("set")
    if submitted:
        invokeSetBucketLifeCycle(int(age),bucket)

    st.write("Current Rules:")
    invokeGetBucketLifeCycle(bucket)