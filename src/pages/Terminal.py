import streamlit as st #type:ignore
import requests #type:ignore

# Function to execute cloud commands
def invokeTransactionProducer():
    try:
        response = requests.get("https://us-central1-project-finance-400806.cloudfunctions.net/transaction-producer")
        result = response.json()
        return result
    
    except Exception as e:
        st.write(f"{e}")

@st.cache_data
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
        
st.title("Terminal")

# Button 1: Generate Data
if st.button("Generate data"):
    result = invokeTransactionProducer()
    if result is None:
        st.error("Please try again later")
    else:
        st.success(f"Successfully pushed {len(result)} transactions to GCS")
        st.code(result)

with st.form("my_form"):
    st.write("Bucket Lifecycle")
    age = st.number_input("Enter object age lifecycle")
    bucket = st.selectbox("Choose a bucket",("engineering_experience"," "))
    
    submitted = st.form_submit_button("set")
    if submitted:
        invokeSetBucketLifeCycle(int(age),bucket)
    else:
        st.write("Current Rules:")
        invokeGetBucketLifeCycle(bucket)