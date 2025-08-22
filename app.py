# Aplicación para desplegar información de vehículos a la venta

import pandas as pd
import streamlit as st
import plotly_express as px

st.header('Venta de vehículos', divider = 'blue')

car_data = pd.read_csv(r'vehicles_us.csv') # Lee los datos del csv
#hist_button = st.button('Crear histograma') # Crea un botón para crear un histograma
#disp_button = st.button('Crear gráfico de dispersión') # Crear un botón para hacer un gráfico de dispersión

build_hist = st.button('Construir histograma')
buld_disp = st.button('Construir gráfico de dispersión')

opciones_disp = list(car_data.columns)[0:9]

if build_hist:
    st.write('Creación de un histograma para el conjunto de anuncios de venta de vehículos de acuerdo al odometro') 
    fig_hist = px.histogram(car_data, x = 'odometer') 
    st.plotly_chart(fig_hist, use_container_width=True)

v_d = st.multiselect(
    label = 'Seleccione las variables', 
    options = opciones_disp,
    max_selections = 2
)

if buld_disp:
    try: 
        st.write(f'Creación de un gráfico de dispersión {v_d[1]} vs {v_d[0]}') 
        fig_disp = px.scatter(car_data, x = v_d[0], y = v_d[1], title = f'Dispersión {v_d[1]} vs {v_d[0]}') 
        st.plotly_chart(fig_disp)
    except:
        st.write('Selecciona las variables')