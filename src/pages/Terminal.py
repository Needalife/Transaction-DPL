import streamlit as st #type:ignore
import subprocess,requests #type:ignore

def sessionStateButtons(number_of_buttons:int):
    i = 0
    while i < number_of_buttons:
        i += 1
        if f"button{i}" not in st.session_state:
            st.session_state[f"button{i}"] = False
    
# Function to execute cloud commands
def invokeTransactionProducer():
    try:
        response = requests.get("https://us-central1-project-finance-400806.cloudfunctions.net/transaction-producer")
        result = response.json()
        return result
    
    except Exception as e:
        st.write(f"{e}")
        
st.title("Terminal")

sessionStateButtons(2)

#Button 1
if st.button("Generate data"):
    result = invokeTransactionProducer()
    if result is None:
        st.error("Please try again later")
    else:
        st.success(f"Successfully push {len(result)} transactions to GCS")
        st.code(result)
    st.session_state['button1'] = not st.session_state['button1']
else:
    st.code(" ")

#Button 2
if st.button('test'):
    if st.session_state["button1"]:
        st.write('do something..')
        st.session_state['button1'] = st.session_state['button1']
        st.session_state["button2"] = not st.session_state["button2"]
else:
    st.code(" ")

st.write(
    f"""
    ## Session state:
    {st.session_state["button1"]=}

    {st.session_state["button2"]=}
    """
)
