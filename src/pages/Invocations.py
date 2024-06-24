import pandas as pd,json,requests,time #type:ignore
import altair as alt,streamlit as st #type:ignore

def getNewData(rows: int) -> pd.DataFrame:
    input_data = {'rows': rows}
    result = requests.post('https://us-central1-project-finance-400806.cloudfunctions.net/getFunctionLogs', json=input_data)

    if result.status_code == 200:
        data = json.loads(result.text)
        return pd.DataFrame(data)
    else:
        st.error(f'Error occurred: {result.status_code}', icon="🚨")
        return pd.DataFrame()  # return an empty DataFrame in case of error

def showTimeDiff(df:pd.DataFrame) -> None:
    time_diff = df['time'].iloc[0] - df['time'].iloc[-1]
    minutes, seconds = divmod(time_diff.total_seconds(), 60)
    st.write(f"Last: {int(minutes)} minutes and {int(seconds)} seconds")

# UI start
st.set_page_config(layout="wide")
st.title("Function Status")
placeholder = st.empty()

while True:
    df = getNewData(100)
    if df.empty:
        continue  # skip if no data is returned

    df['time'] = pd.to_datetime(df['time'], format='%c')

    # Group by time and function, then count the occurrences
    df_counts = df.groupby(['time', 'function']).size().reset_index(name='count')

    # Pivot the DataFrame to have functions as columns and times as index
    df_pivot = df_counts.pivot(index='time', columns='function', values='count').fillna(0)

    with placeholder.container():
        if not df.empty:
            showTimeDiff(df=df)
            
            # Plotting area chart
            st.write('**Invocations/Minutes**')
            st.area_chart(df_pivot)

            #Plot altair chart
            st.write('**Latency**')
            # Create the Altair chart
            chart = alt.Chart(df).mark_line().encode(
                x='time:T',
                y='latency:Q',
                color='function:N'
            ).properties(
                width=800,
                height=400
            ).interactive()
            
            st.altair_chart(chart, use_container_width=True)
            
            st.dataframe(df)
                
            
        
    time.sleep(0.1)
                     