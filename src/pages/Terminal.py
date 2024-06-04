import streamlit as st #type:ignore
import subprocess,requests #type:ignore

# Function to execute cloud commands
def invokeTransactionProducer():
    try:
        response = requests.get("https://us-central1-project-finance-400806.cloudfunctions.net/transaction-producer")
        result = response.json()
        return result
    
    except Exception as e:
        st.write(f"{e}")
        
st.title("Terminal")

# Button 1: Generate Data
if st.button("Generate data"):
    result = invokeTransactionProducer()
    if result is None:
        st.error("Please try again later")
    else:
        st.success(f"Successfully pushed {len(result)} transactions to GCS")
        st.code(result)

# Button 2: Perform some action without reloading the page
if st.button('Set bucket lifecycle'):
    st.session_state['button2'] = not st.session_state['button2']
st.write('After')