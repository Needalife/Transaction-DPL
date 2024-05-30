import streamlit as st,pandas as pd, numpy as np # type: ignore
import requests,os,sys # type: ignore

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.gcp import read

result = read()
if isinstance(result,int):  
    st.error(f"Error fetching data: {result}")
else:
    st.title("GCS Operations")
    st.write(result)











