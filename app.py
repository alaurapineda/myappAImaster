import streamlit as st

st.title("Aplicación de Consultas BSC")

# 1. Entrada de usuario BSC
usuario_bsc = st.text_input("Escribe tu usuario BSC:", "")

# 2. Entrada para el tipo de consulta
tipo_consulta = st.text_input("Escribe el tipo de consulta:", "")

# 3. Dropdown ordenado alfabéticamente
opciones = ["SLA", "proyectos", "Consulta de modeler por area", "Sharepoint Tec Ops", "COP", "otra"]
opciones_ordenadas = sorted(opciones, key=str.lower)

opcion_seleccionada = st.selectbox("Selecciona una opción:", opciones_ordenadas)

# 4. Caja de texto para procesar (máximo 1000 caracteres)
texto_entrada = st.text_area("Escribe el texto a procesar (máx. 1000 caracteres):", "", max_chars=1000)

# Procesamiento del texto (en mayúsculas)
texto_mayusculas = texto_entrada.upper()

# Desplegar resultado procesado
st.subheader("Resultado del procesamiento")
st.text_area("Texto procesado (en mayúsculas):", value=texto_mayusculas, height=150)

# Mostrar resumen de datos del formulario
if st.button("Mostrar Resumen"):
    st.write(f"**Usuario BSC:** {usuario_bsc}")
    st.write(f"**Tipo de Consulta:** {tipo_consulta}")
    st.write(f"**Opción Seleccionada:** {opcion_seleccionada}")
    st.write(f"**Longitud del texto:** {len(texto_entrada)} caracteres")
