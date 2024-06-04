import streamlit as st #type:ignore
import requests #type:ignore
try:
    from pydantic import BaseModel #type:ignore
    import streamlit_pydantic as sp #type:ignore
except Exception as e:
    print(e)

@st.cache_data
class form(BaseModel):
    age: int
    bucket: str
    
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
    
st.title("Terminal")

# Button 1: Generate Data
if st.button("Generate data"):
    result = invokeTransactionProducer()
    if result is None:
        st.error("Please try again later")
    else:
        st.success(f"Successfully pushed {len(result)} transactions to GCS")
        st.code(result)

#Button 2: Set bucket life cycle
if st.button('Set bucket life cycle'):
    data = sp.pydantic_form(key="my_form", model=form)
    if data:
        st.json(data.json())