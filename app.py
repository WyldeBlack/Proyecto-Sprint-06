import pandas as pd
import streamlit as st 
import plotly_express as px 

car_data = pd.read_csv('vehicles_us.csv')

st.header('Escoje tu vehículo')

st.write('Con nuestra app puedes escojer tu mejor opción de compra de tu nuevo vehículo')

hist_button = st.button('Transmisión') # crear un botón
        
if hist_button: # al hacer clic en el botón
            
    st.write('Total de vehículos con transmición manual y automática')
            
            # crear un histograma
    fig = px.bar(car_data, x="transmission")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)



