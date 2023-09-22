import streamlit as st
import pandas as pd
import os
import webbrowser
from datetime import datetime

def retira_ano(valor):
    if len(str(valor)) > 4:
        return valor.split(',')[1].replace(' ','')
    else:
        return valor

def extrair_numeros(texto):
    numeros = ''.join(filter(str.isdigit, str(texto)))
    return int(numeros) if numeros else None

def extrair_ano_nome(nome):
    nome = str(nome)
    return '20' + nome[4:6]


if 'data' not in st.session_state:
    diretorio = 'db/fifa/'
    arquivos = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.csv')]
    df_list = list()
    for arquivo in arquivos:
        df = pd.read_csv(os.path.join(diretorio, arquivo))
        df['nome_arq'] = extrair_ano_nome(arquivo)  # Adiciona o nome do arquivo como uma nova coluna
        df_list.append(df)
    df = pd.concat(df_list, ignore_index=True)
    df['nome_arq'] = pd.to_numeric(df['nome_arq'])
    df['Contract Valid Until'] = pd.to_numeric(df['Contract Valid Until'].apply(retira_ano))
    df['Value'] = pd.to_numeric(df['Value'].apply(extrair_numeros))        
    #df = df[df['Contract Valid Until']>= datetime.today().year]
    df =  df[df['Value'] > 0]
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
