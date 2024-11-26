import pandas as pd
import streamlit as st 
import plotly_express as px 

car_data = pd.read_csv('vehicles_us.csv')

st.header('app proyecto 6')

st.write('app en construccion')

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)



# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
