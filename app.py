import streamlit as st

st.title("Convertidor a Mayúsculas")

# Caja de texto de entrada
texto_entrada = st.text_input("Escribe tu texto aquí:", "")

# Procesamiento del texto
texto_mayusculas = texto_entrada.upper()

# Caja de texto para mostrar el resultado
st.text_area("Texto procesado (en mayúsculas):", value=texto_mayusculas, height=100)
