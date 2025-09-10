import pandas as pd
import streamlit as st
import plotly_express as px

st.header = ('Tabela dos Dados')

car_data = pd.read_csv('vehicles_us.csv')

st.header = ('Gráfico Histograma')

hist_button = st.button('Criar histograma')  # criar um botão

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

st.header = ('Gráfico de dispersão')

# criar um gráfico de dispersão
fig = px.scatter(car_data, x="odometer", y="price")
fig.show()
