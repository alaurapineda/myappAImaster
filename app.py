import streamlit as st
from datetime import datetime

# Configuración de fondo azul medianoche (midnightblue) con CSS personalizado
st.markdown(
    """
    <style>
    .stApp {
        background-color: midnightblue; /* Color azul noche */
    }
    /* Cambiar el color del texto para asegurar que sea legible sobre el fondo azul */
    .stApp, .stMarkdown, p, h1, h2, h3, h4, h5, h6, label {
        color: #FFFFFF !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
usuario_bsc = st.text_input("Escribe tu usuario BSC:", "").strip()

if not usuario_bsc:
    st.warning("Para continuar por favor ingresa tu usuario BSC")
else:
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

    # Enumerar la lista ordenada
    opciones_enumeradas = [f"{i+1}. {opcion}" for i, opcion in enumerate(opciones_ordenadas)]
    opciones_con_placeholder = ["Selecciona una opción..."] + opciones_enumeradas

    tipo_consulta = st.selectbox("Selecciona el tipo de consulta:", opciones_con_placeholder)

    # Lógica condicional según la consulta seleccionada
    if tipo_consulta != "Selecciona una opción...":
        tipo_consulta_limpio = tipo_consulta.split(". ", 1)[1] if ". " in tipo_consulta else tipo_consulta

        # --- CONSULTA MODELER POR ÁREA ---
        if tipo_consulta_limpio == "Consulta de modeler por área":
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
                    st.info("El modeler de Navegator es **Brayan Sanchez**")

        # --- COP ---
        elif tipo_consulta_limpio == "COP":
            opciones_cop = [
                "Horarios",
                "¿Qué material debo llevar al COP?",
                "Representantes por área",
                "¿Cuándo debo llevar mi cambio o proyecto al COP?",
                "COP Leads"
            ]
            # Ordenar alfabéticamente y enumerar
            cop_ordenado = sorted(opciones_cop, key=str.lower)
            cop_enumerado = [f"{i+1}. {opcion}" for i, opcion in enumerate(cop_ordenado)]
            cop_con_placeholder = ["Selecciona una opción de COP..."] + cop_enumerado

            opcion_cop = st.selectbox("Selecciona una opción de COP:", cop_con_placeholder)

            if opcion_cop != "Selecciona una opción de COP...":
                cop_limpio = opcion_cop.split(". ", 1)[1] if ". " in opcion_cop else opcion_cop

                if cop_limpio == "Horarios":
                    st.write("**Horarios de sesiones COP:**")
                    st.write("- **COP CYL** - Lunes 10am")
                    st.write("- **COP HRD** - Martes 10am")
                    st.write("- **COP DRD** - Miércoles 10am")
                    st.write("- **COP CTG** - Jueves 10am")

                elif cop_limpio == "¿Qué material debo llevar al COP?":
                    st.write("Para la sesión del COP, se recomienda preparar una presentación breve que permita explicar claramente el caso, el alcance del cambio y su propósito.")
                    st.write("Es importante incluir la siguiente información:")
                    st.write("- **Descripción del cambio:** explicar qué se desea modificar, por qué es necesario y cuál es el objetivo esperado.")
                    st.write("- **Flujo de trabajo (Workflow):** incluir, preferiblemente, el flujo actual y/o propuesto para facilitar la comprensión del proceso y de los cambios requeridos.")
                    st.write("- **Documentación de soporte:** adjuntar cualquier información, evidencia o referencia que ayude a los Modelers a comprender mejor el alcance y los requerimientos del cambio.")
                    st.write("- **Fechas relevantes:** tener identificadas las fechas previstas de implementación, así como cualquier fecha límite o compromiso asociado al proyecto.")
                    st.write("- **Impacto del cambio:** mencionar las áreas, procesos o sistemas que podrían verse involucrados, cuando corresponda.")
                    st.info("💡 **Recomendación:** entre más clara y completa sea la información presentada, más efectiva será la evaluación del caso y la orientación que los Modelers puedan brindar durante la sesión.")

                elif cop_limpio == "Representantes por área":
                    areas_representantes = [
