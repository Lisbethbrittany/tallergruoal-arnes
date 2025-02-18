# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 20:50:57 2025

@author: BRITT
"""

import streamlit as st
import joblib
import numpy as np 

model_filename = 'arnes.pkl'
# Cargamos el modelo desde el archivo
loaded_model = joblib.load(model_filename)
 
st.title('Compra de Arneses y Botas para perros')
st.header("Tienda RED")
st.subheader("Ingrese los datos de su perro")

with st.form(key='perritos-pred-form'):
    col1, col2 = st.columns(2)
    
    arnes = col1.slider(label='Tamaño del arnés:', min_value=0, max_value=100)
    botas = col2.text_input(label='Tamaño de la Bota:')
    submit = st.form_submit_button(label='Check')
    
    if submit:
        # Convertir el valor de la bota a entero
        try:
            botas = int(botas)
        except ValueError:
            st.error("Por favor, ingrese un valor válido para el tamaño de la bota.")
            st.stop()
        
        inputs = np.array(arnes).reshape(-1, 1)
        # Usamos el modelo para hacer predicciones
        predicted_boot_size = int(loaded_model.predict(inputs)[0])
        st.write("El tamaño de bota recomendado es", predicted_boot_size)
        
        # Comparar el valor predicho con el valor ingresado
        if predicted_boot_size > botas:
            st.write("El tamaño de la bota es muy pequeño.")
        elif predicted_boot_size < botas:
            st.write("El tamaño de la bota es muy grande.")
        else:
            st.write("El tamaño de la bota es correcto.")