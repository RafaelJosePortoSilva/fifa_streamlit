import streamlit as st
import pandas as pd
import os

df = st.session_state['data']


ano = st.sidebar.select_slider('Ano',df.nome_arq.drop_duplicates().sort_values())
df = df[df.nome_arq == ano]
# selecionar o clube
clubes = df.Club.drop_duplicates().dropna().sort_values(ascending = True)
filtro = st.sidebar.text_input('Pesquisar Clubes')
if filtro != '':
    clubes_filtrado = [x for x in clubes if filtro.lower() in x.lower()]
else:
    clubes_filtrado = clubes

clube = st.sidebar.selectbox('Clube',clubes_filtrado)

# selecionar o jogador
df_players = df[df.Club == clube]
players = df_players.Name.drop_duplicates().sort_values()
filtro2 = st.sidebar.text_input('Pesquisar Jogador')
if filtro2 != '':
    players_filtrado = [x for x in players if filtro2.lower() in x.lower()]
else:
    players_filtrado = players

player = st.sidebar.selectbox('Jogadores',players_filtrado)
player_stats = df_players[df_players.Name == player].iloc[0]

st.image(player_stats.Photo,
         width= 120)
st.title(player_stats.Name)

st.markdown(f'**Clube:** {player_stats.Club}')
st.markdown(f'**Posição:** {player_stats.Position}')
