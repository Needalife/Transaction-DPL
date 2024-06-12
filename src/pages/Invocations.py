import pandas as pd, json,requests,streamlit as st #type:ignore

input_data = {'rows':100}
url = 'https://us-central1-project-finance-400806.cloudfunctions.net/getFunctionLogs'
result = requests.post(url,json=input_data)

if result.status_code == 200:
    data = json.loads(result.text)
    data = pd.DataFrame(data)
    st.dataframe(pd.DataFrame(data))
else:
    print(result.status_code)
    st.error(f'Error occurred: {result.status_code}', icon="🚨")