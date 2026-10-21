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

# 2. Dropdown ordenado alfabéticamente y enumerado
opciones_base = [
    "Consulta de modeler por área",
    "SLA Work Orders",
    "COP",
    "Share Point Tec Ops",
    "MUG",
    "Path escalations",
    "On-call"
]

# Ordenar alfabéticamente de manera insensible a mayúsculas/minúsculas
opciones_ordenadas = sorted(opciones_base, key=str.lower)

# Enumerar la lista ordenada (ej: "1. COP", "2. Consulta de modeler por área", etc.)
opciones_enumeradas = [f"{i+1}. {opcion}" for i, opcion in enumerate(opciones_ordenadas)]

# Añadir un valor placeholder al inicio para que no esté pre-seleccionada ninguna opción
opciones_con_placeholder = ["Selecciona una opción..."] + opciones_enumeradas

tipo_consulta = st.selectbox("Selecciona el tipo de consulta:", opciones_con_placeholder)

# Lógica condicional según la consulta seleccionada (limpiando el número del inicio)
if tipo_consulta != "Selecciona una opción...":
    tipo_consulta_limpio = tipo_consulta.split(". ", 1)[1] if ". " in tipo_consulta else tipo_consulta

    if tipo_consulta_limpio == "Consulta de modeler por área":
        # Opciones para el segundo dropdown
        sub_opciones_base = ["Navegator", "Packaging", "Boxing", "FP", "ZWG", "Labs"]
        sub_opciones_ordenadas = sorted(sub_opciones_base, key=str.lower)
        sub_opciones_enumeradas = [f"{i+1}. {opcion}" for i, opcion in enumerate(sub_opciones_ordenadas)]
        sub_opciones_con_placeholder = ["Selecciona una opción de área..."] + sub_opciones_enumeradas

        area_seleccionada = st.selectbox("Selecciona el área:", sub_opciones_con_placeholder)

        if area_seleccionada != "Selecciona una opción de área...":
            area_limpia = area_seleccionada.split(". ", 1)[1] if ". " in area_seleccionada else area_seleccionada
            
            if area_limpia == "Packaging":
                st.info("El modeler de Packaging es **Ana Pineda**")
            elif area_limpia == "Boxing":
                st.info("El modeler de Boxing es **Juan Hernández**")
            elif area_limpia == "FP":
                st.info("El modeler de FP es **Victor Campos**")
            elif area_limpia == "ZWG":
                st.info("El modeler de ZWG es **Jose Acuña**")
            elif area_limpia == "Labs":
                st.info("El modeler de Labs es **Sofía Soto**")
            elif area_limpia == "Navegator":
                st.warning("No hay un modeler asignado para Navegator.")

    elif tipo_consulta_limpio == "COP":
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
