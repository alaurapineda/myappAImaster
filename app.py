import streamlit as st
from datetime import datetime

# Configuración de fondo azul medianoche y estilos de tarjetas FAQ
st.markdown(
    """
    <style>
    .stApp {
        background-color: midnightblue; /* Color azul noche */
    }
    /* Asegurar legibilidad general */
    .stApp, p, h1, h2, h3, h4, h5, h6, label {
        color: #FFFFFF;
    }
    /* Estilo para los mensajes de recomendación (info) en celeste claro */
    div[data-testid="stNotification"] {
        background-color: #87CEFA !important;
        color: #000000 !important;
    }
    div[data-testid="stNotification"] p {
        color: #000000 !important;
    }

    /* --- ESTILOS DE ALTA FIDELIDAD PARA FAQ --- */
    .faq-card-wrapper {
        background-color: #E3F2FD !important; /* Fondo celeste para las tarjetas de pregunta */
        border-radius: 50px !important; 
        padding: 12px 25px !important;
        margin-bottom: 16px !important;
        box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.2) !important;
        border: 1px solid #90CAF9 !important;
    }
    
    /* Círculo azul de interrogación izquierdo */
    .faq-circle-q-custom {
        background-color: #1976D2 !important; 
        color: #FFFFFF !important;
        border-radius: 50% !important;
        width: 42px !important;
        height: 42px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-weight: bold !important;
        font-size: 20px !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
        margin-top: 2px !important;
    }

    /* Contenedor de la respuesta en fondo celeste pastel con letras negras */
    .faq-answer-container-clean {
        background-color: #E3F2FD !important; /* Mismo celeste consistente */
        border-radius: 24px !important;
        padding: 15px 25px !important;
        border: 1px solid #90CAF9 !important;
        margin-top: 10px !important;
        margin-bottom: 5px !important;
    }
    
    /* Forzar letras negras en todo el contenido de la tarjeta de preguntas y de las respuestas */
    .faq-card-wrapper, 
    .faq-card-wrapper *, 
    .faq-answer-container-clean, 
    .faq-answer-container-clean *, 
    .faq-answer-text-custom, 
    .faq-answer-text-custom p, 
    .faq-answer-text-custom strong, 
    .faq-answer-text-custom li, 
    .faq-answer-text-custom ul,
    .faq-answer-text-custom ol {
        color: #000000 !important; /* Todo en color negro para legibilidad óptima */
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }

    /* Estilo e interactividad sobre los botones de pregunta (ahora con letra negra) */
    div[data-testid="column"] button {
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
        width: 100% !important;
        text-align: left !important;
        box-shadow: none !important;
        height: 44px !important;
        color: #000000 !important; /* Letra negra de la pregunta */
        font-size: 17px !important;
        font-weight: 600 !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
        transition: color 0.2s ease !important;
    }
    
    /* Botón circular celeste de control (+ / -) */
    div[data-testid="column"] button.faq-trigger-btn {
        background-color: #1976D2 !important; /* Azul para resaltar en el fondo celeste */
        color: #FFFFFF !important; 
        border-radius: 50% !important;
        width: 38px !important;
        height: 38px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 22px !important;
        font-weight: bold !important;
        line-height: 1 !important;
        margin-top: 3px !important;
        text-align: center !important;
    }
    
    div[data-testid="column"] button:hover {
        background: transparent !important;
        border: none !important;
        color: #1976D2 !important;
    }
    div[data-testid="column"] button.faq-trigger-btn:hover {
        background-color: #1565C0 !important;
        color: #FFFFFF !important;
    }
    div[data-testid="column"] p {
        margin: 0 !important;
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
            sites_disponibles = ["Selecciona un site...", "CTG", "CYL", "DRD", "HRD"]
            site_seleccionado = st.selectbox("Selecciona el site:", sites_disponibles)

            if site_seleccionado != "Selecciona un site...":
                sub_opciones_base = ["Navegator", "Packaging", "Boxing", "FP", "ZWG", "Labs"]
                sub_opciones_ordenadas = sorted(sub_opciones_base, key=str.lower)
                sub_opciones_enumeradas = [f"{i+1}. {opcion}" for i, opcion in enumerate(sub_opciones_ordenadas)]
                sub_opciones_con_placeholder = ["Selecciona una opción de área..."] + sub_opciones_enumeradas

                area_seleccionada = st.selectbox("Selecciona el área:", sub_opciones_con_placeholder)

                if area_seleccionada != "Selecciona una opción de área...":
                    area_limpia = area_seleccionada.split(". ", 1)[1] if ". " in area_seleccionada else area_seleccionada

                    # Definición de modeladores específicos para cada site y área
                    modelers_database = {
                        "CTG": {
                            "Packaging": "Ana Pineda",
                            "Boxing": "Carlos Alvarado",
                            "FP": "Victor Campos",
                            "ZWG": "Jose Acuña",
                            "Labs": "Sofía Soto",
                            "Navegator": "Brayan Sanchez"
                        },
                        "CYL": {
                            "Packaging": "Mauricio Solís",
                            "Boxing": "Juan Hernández",
                            "FP": "Mariana Rojas",
                            "ZWG": "Esteban Chaves",
                            "Labs": "Gabriela Quirós",
                            "Navegator": "Andrés Fonseca"
                        },
                        "DRD": {
                            "Packaging": "Valeria Gamboa",
                            "Boxing": "Roberto Delgado",
                            "FP": "Natalia Esquivel",
                            "ZWG": "Kenneth Barboza",
                            "Labs": "Daniela Meléndez",
                            "Navegator": "Alejandro Orozco"
                        },
                        "HRD": {
                            "Packaging": "Lucía Mora",
                            "Boxing": "Felipe Herrera",
                            "FP": "Diego Gutiérrez",
                            "ZWG": "Tatiana Vargas",
                            "Labs": "Melissa Blanco",
                            "Navegator": "Ricardo Brenes"
                        }
                    }

                    # Obtener el nombre correspondiente de la base de datos
                    modeler_nombre = modelers_database.get(site_seleccionado, {}).get(area_limpia, "Modeler no asignado")
                    st.info(f"El modeler de **{area_limpia}** para **{site_seleccionado}** es **{modeler_nombre}**")

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
                    st.write("**Consulta de Representantes por Area y Site**")
                    sites_cop = ["Selecciona site...", "CTG", "CYL", "DRD", "HRD"]
                    site_cop_sel = st.selectbox("Selecciona el site para los representantes:", sites_cop)
                    
                    if site_cop_sel != "Selecciona site...":
                        areas_representantes = ["Boxing", "FP", "Labs", "Navegator", "Packaging", "ZWG"]
                        rep_area_sel = st.selectbox("Selecciona el área para ver sus representantes:", ["Selecciona área..."] + areas_representantes)

                        if rep_area_sel != "Selecciona área...":
                            # Base de datos estructurada con representantes por Site y Área
                            representantes_database = {
                                "CTG": {
                                    "Boxing": {"mfg": "Luis Sandoval", "qa": "Laura Pineda"},
                                    "FP": {"mfg": "Tania Villanueva", "qa": "Karol Hernández"},
                                    "Labs": {"mfg": "Carlos Mendéz", "qa": "Pablo González"},
                                    "Navegator": {"mfg": "Jorge Chaves", "qa": "María José Sanchez"},
                                    "Packaging": {"mfg": "Josué González", "qa": "Carolina Barrantes"},
                                    "ZWG": {"mfg": "Luisa Soto", "qa": "Luisa Hernández"}
                                },
                                "CYL": {
                                    "Boxing": {"mfg": "Andrés Morales", "qa": "Diana Calderón"},
                                    "FP": {"mfg": "Silvia Castro", "qa": "Fabián Ruiz"},
                                    "Labs": {"mfg": "Guillermo Solano", "qa": "Rebeca Campos"},
                                    "Navegator": {"mfg": "Gabriel Arguedas", "qa": "Mónica Villalobos"},
                                    "Packaging": {"mfg": "Esteban Marín", "qa": "Beatriz Rojas"},
                                    "ZWG": {"mfg": "Laura Cubero", "qa": "Federico Gutiérrez"}
                                },
                                "DRD": {
                                    "Boxing": {"mfg": "Rodolfo Vargas", "qa": "Jimena Zamora"},
                                    "FP": {"mfg": "Paula Céspedes", "qa": "Mario Alfaro"},
                                    "Labs": {"mfg": "Karla Mora", "qa": "Santiago Fallas"},
                                    "Navegator": {"mfg": "David Brenes", "qa": "Lucía Madrigal"},
                                    "Packaging": {"mfg": "Francisco Fonseca", "qa": "Elena Carvajal"},
                                    "ZWG": {"mfg": "Daniela Ortiz", "qa": "Gabriel Navarro"}
                                },
                                "HRD": {
                                    "Boxing": {"mfg": "Felipe Peralta", "qa": "Natalia Quesada"},
                                    "FP": {"mfg": "Valeria Araya", "qa": "Alonso Méndez"},
                                    "Labs": {"mfg": "Oscar Bolaños", "qa": "Clara Leitón"},
                                    "Navegator": {"mfg": "Adrián Saborío", "qa": "Daniela Porras"},
                                    "Packaging": {"mfg": "Kevin Matarrita", "qa": "Patricia Núñez"},
                                    "ZWG": {"mfg": "Sofia Barahona", "qa": "Mariano Trejos"}
                                }
                            }

                            rep_info = representantes_database.get(site_cop_sel, {}).get(rep_area_sel, {})
                            st.write(f"**Representantes de {rep_area_sel} en {site_cop_sel}:**")
                            st.write(f"- **Ing. Manufactura:** {rep_info.get('mfg', 'No asignado')}")
                            st.write(f"- **Ing. Calidad:** {rep_info.get('qa', 'No asignado')}")

                elif cop_limpio == "¿Cuándo debo llevar mi cambio o proyecto al COP?":
                    st.write("Debes presentar tu cambio o proyecto en el COP cuando se presente alguna de las siguientes condiciones:")
                    st.write("- **El cambio esté relacionado con un CAPA o un NCEP.**")
                    st.write("- **Se trate de un cambio complejo que requiera evaluación o discusión multidisciplinaria.**")
                    st.write("- **El Modeler recomiende presentar el cambio o proyecto ante el COP.**")
                    st.write("- **Tengas dudas sobre el desarrollo, alcance o implementación del proyecto y necesites orientación, recomendaciones o acompañamiento para su adecuada ejecución.**")

                elif cop_limpio == "COP Leads":
                    st.write("**Líderes de COP por cada Site:**")
                    st.write("- **Lead de COP CTG:** Eduardo Jenkins")
                    st.write("- **Lead de COP CYL:** Sergio Monge")
                    st.write("- **Lead de COP DRD:** Rebeca Alfaro")
                    st.write("- **Lead de COP HRD:** Amanda Solano")

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
            st.info("Todas las escalaciones deben documentarse por correo con la explicación de porqué se le debe de dar prioridad.")

            st.markdown("### Preguntas sugeridas:")

            # Inicializar los estados de expansión de las preguntas en la sesión
            if "faq_1_expanded" not in st.session_state:
                st.session_state.faq_1_expanded = False
            if "faq_2_expanded" not in st.session_state:
                st.session_state.faq_2_expanded = False
            if "faq_3_expanded" not in st.session_state:
                st.session_state.faq_3_expanded = False

            # --- TARJETA 1 ---
            st.markdown('<div class="faq-card-wrapper">', unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 8, 1])
            with col1:
                st.markdown('<div class="faq-circle-q-custom">?</div>', unsafe_allow_html=True)
            with col2:
                # Clic en la pregunta conmuta el estado
                if st.button("¿Quiénes son los Site Leads?", key="q1_btn"):
                    st.session_state.faq_1_expanded = not st.session_state.faq_1_expanded
                    st.rerun()
            with col3:
                signo_1 = "−" if st.session_state.faq_1_expanded else "+"
                # El círculo derecho es un botón nativo estilizado para conmutar también el estado
                if st.button(signo_1, key="q1_trigger", help="Presiona para expandir o contraer"):
                    st.session_state.faq_1_expanded = not st.session_state.faq_1_expanded
                    st.rerun()
                # Inyección del selector CSS especial de forma local sobre este botón
                st.markdown('<script>document.querySelectorAll("button[key=\"q1_trigger\"]").forEach(b => b.classList.add("faq-trigger-btn"));</script>', unsafe_allow_html=True)
            
            if st.session_state.faq_1_expanded:
                st.markdown("""
                <div class="faq-answer-container-clean">
                    <div class="faq-answer-text-custom">
                        <strong>Site Leads designados:</strong><br>
                        Los líderes a cargo de coordinar y dar aprobación preliminar en cada planta son los correspondientes <strong>COP Leads</strong>:<br>
                        <ul>
                            <li><strong>Site Lead CTG:</strong> Eduardo Jenkins</li>
                            <li><strong>Site Lead CYL:</strong> Sergio Monge</li>
                            <li><strong>Site Lead DRD:</strong> Rebeca Alfaro</li>
                            <li><strong>Site Lead HRD:</strong> Amanda Solano</li>
                        </ul>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # --- TARJETA 2 ---
            st.markdown('<div class="faq-card-wrapper">', unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 8, 1])
            with col1:
                st.markdown('<div class="faq-circle-q-custom">?</div>', unsafe_allow_html=True)
            with col2:
                if st.button("¿Quién es el Manager de Tec Ops?", key="q2_btn"):
                    st.session_state.faq_2_expanded = not st.session_state.faq_2_expanded
                    st.rerun()
            with col3:
                signo_2 = "−" if st.session_state.faq_2_expanded else "+"
                if st.button(signo_2, key="q2_trigger"):
                    st.session_state.faq_2_expanded = not st.session_state.faq_2_expanded
                    st.rerun()

            if st.session_state.faq_2_expanded:
                st.markdown("""
                <div class="faq-answer-container-clean">
                    <div class="faq-answer-text-custom">
                        El manager del departamento de Tec Ops es <strong>Francisco Castro</strong>. Puedes escalar tu caso con él directamente si tras abrir el tiquete de soporte técnico y seguir los canales de primera línea no has obtenido respuesta.
                    </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # --- TARJETA 3 ---
            st.markdown('<div class="faq-card-wrapper">', unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 8, 1])
            with col1:
                st.markdown('<div class="faq-circle-q-custom">?</div>', unsafe_allow_html=True)
            with col2:
                if st.button("¿Qué pasa si mi escalación ocurre un feriado o fin de semana?", key="q3_btn"):
                    st.session_state.faq_3_expanded = not st.session_state.faq_3_expanded
                    st.rerun()
            with col3:
                signo_3 = "−" if st.session_state.faq_3_expanded else "+"
                if st.button(signo_3, key="q3_trigger"):
                    st.session_state.faq_3_expanded = not st.session_state.faq_3_expanded
                    st.rerun()

            if st.session_state.faq_3_expanded:
                st.markdown("""
                <div class="faq-answer-container-clean">
                    <div class="faq-answer-text-custom">
                        <strong>Protocolo para Feriados y Fines de Semana:</strong><br>
                        Si el caso ocurre durante el fin de semana, un día festivo nacional, o en el Turno C, el servicio se centraliza mediante los contactos del servicio <strong>On-call</strong> únicamente para situaciones críticas de línea detenida.<br><br>
                        <strong>Pasos obligatorios:</strong>
                        <ol>
                            <li>Asegúrate de abrir el tiquete correspondiente adjuntando toda la evidencia disponible y descripción del problema.</li>
                            <li>Llama directamente por teléfono regular (no mensajes ni WhatsApp) al contacto On-call de tu respectiva planta:
                                <ul>
                                    <li><strong>CYL:</strong> 8888-8881</li>
                                    <li><strong>HRD:</strong> 8888-8882</li>
                                    <li><strong>CTG:</strong> 8888-8883</li>
                                    <li><strong>DRD:</strong> 8888-8884</li>
                                </ul>
                            </li>
                        </ol>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # Script inyectado para asegurar que todos los disparadores laterales hereden el estilo circular celeste
            st.markdown(
                """
                <script>
                const triggers = parent.document.querySelectorAll('button');
                triggers.forEach(btn => {
                    if (btn.innerText === '+' || btn.innerText === '−') {
                        btn.classList.add('faq-trigger-btn');
                    }
                });
                </script>
                """,
                unsafe_allow_html=True
            )

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
                        st.warning("El SLA debe verse directamente con el modeler ya que por la cantidad de markups el mismo sería un proyecto.")
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
