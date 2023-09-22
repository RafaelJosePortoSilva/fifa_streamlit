import streamlit as st
import pandas as pd
import os

st.write('# PLAYERS')

df = st.session_state['data']

clubes = df.Club.drop_duplicates().dropna().sort_values(ascending = True)

filtro = st.sidebar.text_input('Pesquisar Clubes')
if filtro != '':
    clubes_filtrado = [x for x in clubes if filtro.lower() in x.lower()]
else:
    clubes_filtrado = clubes

clube = st.sidebar.selectbox('Clube',clubes_filtrado)

df_players = df[df.Club == clube]
players = df_players.Name.drop_duplicates().sort_values()
player = st.sidebar.selectbox('Jogadores',players)
