import pandas as pd
import streamlit as st 
import plotly_express as px 

car_data = pd.read_csv('vehicles_us.csv')

st.header('Escoje tu vehículo') # Titulo de la app

st.write('Con nuestra app puedes revisar los detalles de tu nuevo vehículo') # Descripción de la app

casilla_transmision = st.checkbox('Transmisión') # crear casiila Transmisión
casilla_color = st.checkbox('Color') # crear casilla Color
casilla_estado = st.checkbox('Estado') #crear casilla Estado

if casilla_transmision: # si la casilla de verificación está seleccionada
    st.write('Acá puedes ver la cantidad de vehículos que cuentan con transmisión automática o manual')
    fig = px.histogram(car_data, x="transmission",labels={"transmission": "Tipo de Transmisión"},title="Transmisión") # crear el gráfico
    st.plotly_chart(fig, use_container_width=True)


if casilla_color:
    st.write('Revisa los colores disponibles')
    fig = px.histogram(car_data,x= 'paint_color',labels={"paint_color": "Colores Disponibles"},title="Colores") # crear el gráfico
    st.plotly_chart(fig,use_container_width=True)

if casilla_estado:
    st.write('Revisa el estado de nuestros vehículos')
    fig = px.histogram(car_data,x= 'condition',labels={"condition": "Condiciones de los vehículos"},title="Estado de Nuestros Vehículos") #crear el gráfico
    st.plotly_chart(fig, use_container_width=True)