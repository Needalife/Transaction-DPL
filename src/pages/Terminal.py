import streamlit as st #type:ignore
import subprocess,requests #type:ignore

st.title("Terminal")

# Function to execute cloud commands
def invokeTransactionProducer():
    try:
        response = requests.get("https://us-central1-project-finance-400806.cloudfunctions.net/transaction-producer")
        result = response.json()
        return result
    
    except Exception as e:
        st.write(f"{e}")

if st.button("Generate data"):
    result = invokeTransactionProducer()
    if result is None:
        st.error("Please try again later")
    else:
        st.success(f"Successfully push {len(result)} transactions to GCS")
        st.json(result)
else:
    st.code(" ")
