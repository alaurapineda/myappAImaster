import streamlit as st
from datetime import datetime

st.title("Aplicación de consultas Tec Ops")

# Obtener la hora actual
ahora = datetime.now().time()
hora_actual = ahora.hour
minuto_actual = ahora.minute

# Determinar el saludo según la hora
if 0 <= hora_actual < 12:
    saludo = "¡Bienvenido, buenos días!"
elif 12 <= hora_actual < 18 or (hora_actual == 18 and minuto_actual == 0):
    saludo = "¡Bienvenido, buenas tardes!"
else:
    saludo = "¡Bienvenido, buenas noches!"

# Mostrar el saludo dinámico
st.subheader(saludo)

# 1. Entrada de usuario BSC
usuario_bsc = st.text_input("Escribe tu usuario BSC:", "")

# 2. Dropdown ordenado alfabéticamente
opciones = ["SLA", "proyectos", "Consulta de modeler por area", "Sharepoint Tec Ops", "COP", "otra"]
opciones_ordenadas = sorted(opciones, key=str.lower)

tipo_consulta = st.selectbox("Selecciona el tipo de consulta:", opciones_ordenadas)

# Lógica condicional según la consulta seleccionada
if tipo_consulta == "Consulta de modeler por area":
    area = st.text_input("Escribe el área:", "")
    if area.strip().lower() in ["opti", "fara"]:
        st.info("El nombre del modeler es: **Ana Laura Pineda**")

elif tipo_consulta == "COP":
    opcion_cop = st.selectbox(
        "Selecciona una opción de COP:",
        ["Selecciona una opción...", "horario", "que material debo llevar al COP?"]
    )
    if opcion_cop == "horario":
        st.write("**Horarios disponibles:**")
        st.write("- **Coyol:** Jueves a la 1:00 PM")
        st.write("- **Heredia:** Miércoles a la 1:00 PM")
        st.write("- **Cartago:** Viernes a la 1:00 PM")
    elif opcion_cop == "que material debo llevar al COP?":
        st.write("Por favor, consulta con tu encargado la lista de materiales requerida para la sesión de COP.")

# 3. Caja de texto para procesar (máximo 1000 caracteres)
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
    st.write(f"**Longitud del texto:** {len(texto_entrada)} caracteres")
    st.write(f"**Usuario BSC:** {usuario_bsc}")
    st.write(f"**Tipo de Consulta:** {tipo_consulta}")
    st.write(f"**Longitud del texto:** {len(texto_entrada)} caracteres")
