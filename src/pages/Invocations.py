import pandas as pd, json,requests,streamlit as st,time,numpy as np #type:ignore

def getNewData(rows:int) -> pd.DataFrame:
    input_data = {'rows':rows}
    result = requests.post('https://us-central1-project-finance-400806.cloudfunctions.net/getFunctionLogs',json=input_data)

    if result.status_code == 200:
        data = json.loads(result.text)
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
    
    #chart_data = pd.DataFrame(,columns=[i for i in df.function.unique()])
    with placeholder.container():
        st.write(df['time'].iloc[0] - df['time'].iloc[-1])
        st.dataframe(df)
        st.line_chart(pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"]))

        
    time.sleep(1)