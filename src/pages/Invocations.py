import pandas as pd, json,requests,streamlit as st,time #type:ignore

def getNewData(rows):
    input_data = {'rows':rows}
    result = requests.post('https://us-central1-project-finance-400806.cloudfunctions.net/getFunctionLogs',json=input_data)

    if result.status_code == 200:
        data = json.loads(result.text)
        data = pd.DataFrame(data)
        return pd.DataFrame(data)
    else:
        print(result.status_code)
        st.error(f'Error occurred: {result.status_code}', icon="🚨")

#UI start
st.set_page_config(layout="wide")
st.title("Function Status")
placeholder = st.empty()

while True:
    df = getNewData(100)
    u = [i for i in df.function.unique()]
    
    #chart_data = pd.DataFrame(,columns=[])
    with placeholder.container():
        st.write(u)
        st.dataframe(df)

        
    time.sleep(1)