import streamlit as st
import pandas as pd
import os

df_list = [pd.read_csv('db/fifa/' + x) for x in os.listdir('db/fifa') if '.csv' in x]

df = pd.concat(df_list)
df.sort_values(by='ID',inplace=True)
st.session_state['data'] = df
df