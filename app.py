import pandas as pd
import streamlit as st
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

# exibi titulo
st.header('Relatório da Análise de anuncios de venda de carro')

# titulo tabela de dados
st.header('Tabela dos Dados')

# exibi dataFrame
st.dataframe(car_data, use_container_width=True)

# exibi titulo
st.header('Análise em  Histograma')

hist_button = st.button('Criar Gráfico de Histograma')  # criar um botão

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

st.header('Análise de dispersão')

# criar um gráfico de dispersão

disp_button = st.button('Criar Gráfico de dispersão')   # cria um botão

if disp_button:    # se o botão for cliclado
    # escreva a mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # cria um  gráfico de dispersão
    fig_desp = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig_desp, use_container_width=True)
