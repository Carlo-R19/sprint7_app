# Aplicación para desplegar información de vehículos a la venta

import pandas as pd
import streamlit as st
import plotly_express as px

st.header('Venta de vehículos', divider = 'blue')


car_data = pd.read_csv(r'C:\Users\Carlo\Documents\TripleTen\Jupyter\Directorio Principal\sprint7_app\sprint7_app\vehicles_us.csv') # Lee los datos del csv
#hist_button = st.button('Crear histograma') # Crea un botón para crear un histograma
#disp_button = st.button('Crear gráfico de dispersión') # Crear un botón para hacer un gráfico de dispersión

build_hist = st.checkbox('Construir histograma')
buld_disp = st.checkbox('Construir gráfico de dispersión')

# opciones = list(df.columns)[0:6]

#v = st.multiselect(
 #   label = 'Seleccione 2 variables',
 #   options = opciones, 
 #   max_selections= 2
#)

if build_hist:
    st.write('Creación de un histograma para el conjunto de anuncios de venta de vehículos')
    fig_hist = px.histogram(car_data, x = 'odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

if buld_disp:
    st.write('Creación de un gráfico de dispersión para el conjunto de anuncuios de venta de vehículos')
    fig_disp = px.scatter(car_data, x = 'odometer', y = 'price')
    st.plotly_chart(fig_disp)
