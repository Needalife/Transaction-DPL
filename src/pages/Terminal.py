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

# Button 1: Generate Data
if st.button("Generate data"):
    result = invokeTransactionProducer()
    if result is None:
        st.error("Please try again later")
    else:
        st.success(f"Successfully pushed {len(result)} transactions to GCS")
        st.code(result)
        st.session_state['button1'] = True
        st.session_state['button1_result'] = result

# Display result if button 1 was pressed
if st.session_state['button1']:
    st.code(st.session_state['button1_result'])

# Button 2: Perform some action without reloading the page
if st.button('Test'):
    if st.session_state['button1']:
        st.write('Do something..')
        st.session_state['button2'] = not st.session_state['button2']

# Optionally, you can add some logic based on the state of button 2
if st.session_state['button2']:
    st.write('Button 2 was pressed and toggled its state.')

st.write(
    f"""
    ## Session state:
    {st.session_state["button1"]=}

    {st.session_state["button2"]=}
    """
)
