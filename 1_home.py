import streamlit as st
import pandas as pd
import os
import webbrowser

if 'data' not in st.session_state:
    df_list = [pd.read_csv('db/fifa/' + x) for x in os.listdir('db/fifa') if '.csv' in x]
    df = pd.concat(df_list)
    df.sort_values(by='ID',inplace=True)
    st.session_state['data'] = df


st.write('# FIFA23 OFFICIAL DATASET')
st.sidebar.markdown('Desenvolvido por Rafael Porto')

btn = st.button('Acessar dataset')
if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database?resource=download')

st.markdown("""

O **"FIFA 23 Complete Player Dataset"** é uma valiosa fonte de informações para entusiastas do futebol e cientistas de dados apaixonados pelo jogo FIFA 21. Este conjunto de dados abrangente reúne detalhes sobre os jogadores presentes no FIFA 21, um dos jogos de futebol mais populares do mundo.

**Conteúdo:**

Habilidades dos jogadores, incluindo classificações de atributos como velocidade, força, dribles e muito mais.
Estatísticas de desempenho em várias temporadas.
Informações sobre as posições dos jogadores.
Clubes e nacionalidades dos jogadores.
Dados de idade e altura.
Usos Potenciais:

Classificação e comparação de jogadores.
Análises de desempenho de equipes e ligas.
Identificação de tendências e estatísticas interessantes.
Projetos de ciência de dados relacionados ao futebol.
            
""")