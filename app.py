# Aplicación para desplegar información de vehículos a la venta

import pandas 
import streamlit 
import plotly_express

car_data = pandas.read_csv(r'C:\Users\Carlo\Documents\TripleTen\Jupyter\Directorio Principal\sprint7_app\sprint7_app\vehicles_us.csv') # Lee los datos del csv
hist_button = streamlit.button('Crear histograma') # Crea un botón 

streamlit.header('Venta de vehículos')

if hist_button:
    streamlit.write('Creación de un histograma para el conjunto de anuncios de venta de vehículos')
    fig = plotly_express.histogram(car_data, x = 'odometer')
    streamlit.plotly_chart(fig, use_container_width=True)

print(car_data)
