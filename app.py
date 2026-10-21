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
                    st.write("Por favor, consulta con tu encargado la lista de materiales requerida para la sesión de COP.")
                    
                elif cop_limpio == "Representantes por área":
                    areas_representantes = ["Boxing", "FP", "Labs", "Navegator", "Packaging", "ZWG"]
                    rep_area_sel = st.selectbox("Selecciona el área para ver sus representantes:", ["Selecciona área..."] + areas_representantes)
                    
                    if rep_area_sel == "Boxing":
                        st.write("**Boxing:**\n- **Ing. Manufactura:** Luis Sandoval\n- **Ing. Calidad:** Laura Pineda")
                    elif rep_area_sel == "FP":
                        st.write("**FP:**\n- **Ing. Manufactura:** Tania Villanueva\n- **Ing. Calidad:** Karol Hernández")
                    elif rep_area_sel == "Labs":
                        st.write("**Labs:**\n- **Ing. Manufactura:** Carlos Mendéz / Karla Mora\n- **Ing. Calidad:** Pablo González")
                    elif rep_area_sel == "Navegator":
                        st.write("**Navegator:**\n- **Ing. Manufactura:** Jorge Chaves\n- **Ing. Calidad:** María José Sanchez")
                    elif rep_area_sel == "Packaging":
                        st.write("**Packaging:**\n- **Ing. Manufactura:** Josué González\n- **Ing. Calidad:** Carolina Barrantes")
                    elif rep_area_sel == "ZWG":
                        st.write("**ZWG:**\n- **Ing. Calidad:** Luisa Hernández")
                
                elif cop_limpio == "¿Cuándo debo llevar mi cambio o proyecto al COP?":
                    st.write("Por favor consulta los lineamientos de tu planta para verificar los disparadores de presentación de cambios.")
                
                elif cop_limpio == "COP Leads":
                    st.write("Contacta a los líderes de COP de tu respectivo site para más información.")

        # --- MUG ---
        elif tipo_consulta_limpio == "MUG":
            st.write("Para accesar al MUG haz click en el siguiente enlace: https://MUG.guide1234.com")
            st.write("Si tienes feedback para la guía por favor contactar a uno de los modelers o deja tu comentario en la siguiente caja.")
            st.text_area("Déjanos tus comentarios sobre MUG:", "", key="feedback_mug")

        # --- ON-CALL ---
        elif tipo_consulta_limpio == "On-call":
            st.info("El servicio de oncall se da únicamente para líneas detenidas, en turno C, feriados y fines de semana.")
            st.write("**Teléfonos de contacto:**")
            st.write("- **CYL:** 8888-8881")
            st.write("- **HRD:** 8888-8882")
            st.write("- **CTG:** 8888-8883")
            st.write("- **DRD:** 8888-8884")
            st.warning("⚠️ Solo llamadas, no mensajes ni llamadas por WhatsApp.")
            st.write("Al llamar asegúrese de abrir el tiquete primero con toda la evidencia y explicación del issue. Si no recibe respuesta por favor escalar el caso con el manager del departamento **Francisco Castro**.")

        # --- PATH ESCALATIONS ---
        elif tipo_consulta_limpio == "Path escalations":
            st.write("Si necesita ayuda urgente con la aprobación de un incidente, work order, acceso, aprobación de máscara o aprobación de CN por favor contacte primero al site lead que corresponda o con el manager.")
            st.info("Todas las escalafones deben documentarse por correo con la explicación de porqué se le debe de dar prioridad.")

        # --- SHARE POINT TEC OPS ---
        elif tipo_consulta_limpio == "Share Point Tec Ops":
            st.write("Visita nuestro share point a través del siguiente enlace: https://tecopssharepoint1234.com")
            st.write("Si tienes feedback para la guía por favor contactar a uno de los modelers o deja tu comentario en la siguiente caja.")
            st.text_area("Déjanos tu feedback sobre Share Point:", "", key="feedback_sp")

        # --- SLA WORK ORDERS ---
        elif tipo_consulta_limpio == "SLA Work Orders":
            docs_input = st.text_input("¿Cuántos documentos vas a someter en el cambio?", "")
            if docs_input:
                # Validación de número entero estricto
                if not docs_input.isdigit():
                    st.error("Número inválido. Por favor, ingresa únicamente números enteros sin letras, comas ni signos.")
                else:
                    num_docs = int(docs_input)
                    if 1 <= num_docs <= 4:
                        st.success("El SLA es de **3 días**.")
                    elif 5 <= num_docs <= 10:
                        st.success("El SLA es de **5 días**.")
                    elif 11 <= num_docs <= 20:
                        st.success("El SLA es de **9 días**.")
                    elif num_docs >= 21:
                        st.warning("El SLA debe verse directamente con el modeler ya que entraría como proyecto.")
                    else:
                        st.error("Por favor ingresa un número mayor a 0.")

    # 3. Caja de texto para procesar (máximo 1000 caracteres)
    st.markdown("---")
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
