import os
import streamlit as st
from datetime import datetime
from google import genai

# --- CONFIGURACIÓN DE NAVEGACIÓN ---
if "pagina_actual" not in st.session_state:
    st.session_state.pagina_actual = "principal"

# --- CONFIGURACIÓN VISUAL GENERAL Y ESTILOS ---
st.markdown("""
<style>

/* Fondo principal azul medianoche */
.stApp,
[data-testid="stAppViewContainer"] {
    background-color: #191970 !important;
}

/* Encabezado */
[data-testid="stHeader"] {
    background-color: transparent !important;
}

/* Texto general en blanco */
h1, h2, h3, h4, h5, h6,
p, li, label,
[data-testid="stMarkdownContainer"] {
    color: #FFFFFF !important;
}

h1 { font-weight: 700 !important; }
h2, h3 { font-weight: 600 !important; }

/* === GARANTÍA DE LEGIBILIDAD EN INPUTS Y BOTONES === */

input,
textarea,
[data-baseweb="input"] input,
[data-testid="stTextArea"] textarea {
    background-color: #FFFFFF !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    border-radius: 8px !important;
    font-weight: 500 !important;
}

[data-baseweb="select"],
[data-baseweb="select"] * {
    background-color: #FFFFFF !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    border-radius: 8px !important;
}

[role="listbox"],
[role="option"] {
    background-color: #FFFFFF !important;
    color: #000000 !important;
}

.stButton > button {
    background-color: #FFFFFF !important;
    color: #191970 !important;
    border: 2px solid #191970 !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    padding: 8px 18px !important;
    transition: all 0.2s ease-in-out !important;
}

.stButton > button * {
    color: #191970 !important;
}

.stButton > button:hover {
    background-color: #EAF7F7 !important;
    color: #191970 !important;
    border-color: #4A90E2 !important;
}

[data-testid="stAlert"] {
    background-color: #D9F0FA !important;
    border-radius: 12px !important;
}

[data-testid="stAlert"] p,
[data-testid="stAlert"] strong {
    color: #000000 !important;
}

[data-testid="stExpander"] {
    background-color: #EAF7F7 !important;
    border: 1px solid #D2EEEE !important;
    border-radius: 20px !important;
    margin-bottom: 14px !important;
    overflow: hidden;
}

[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary p,
[data-testid="stExpander"] [data-testid="stMarkdownContainer"],
[data-testid="stExpander"] p,
[data-testid="stExpander"] li,
[data-testid="stExpander"] strong {
    color: #000000 !important;
}

[data-testid="stExpander"] [data-testid="stExpanderDetails"] {
    padding: 12px 22px !important;
}

/* === ESTILOS FORZADOS A LETRA NEGRA PARA EL CHATBOT === */

[data-testid="stChatMessage"] {
    background-color: #FFFFFF !important;
    border-radius: 16px !important;
    padding: 14px 18px !important;
    margin-bottom: 14px !important;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2) !important;
}

[data-testid="stChatMessage"] p, 
[data-testid="stChatMessage"] li, 
[data-testid="stChatMessage"] span, 
[data-testid="stChatMessage"] strong,
[data-testid="stChatMessage"] div {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
}

.bot-card-banner {
    background: linear-gradient(135deg, #1E3C72 0%, #2A5298 100%);
    border-radius: 20px;
    padding: 24px;
    border: 1px solid #4A90E2;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.3);
    margin-top: 25px;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# ==============================================================================
# PÁGINA PRINCIPAL
# ==============================================================================
if st.session_state.pagina_actual == "principal":

    st.title("Aplicación de consultas Tec Ops")

    ahora = datetime.now().time()
    hora_actual = ahora.hour
    minuto_actual = ahora.minute

    if 0 <= hora_actual < 12:
        saludo = "¡Bienvenido, buenos días!"
    elif 12 <= hora_actual < 18 or (hora_actual == 18 and minuto_actual == 0):
        saludo = "¡Bienvenido, buenas tardes!"
    else:
        saludo = "¡Bienvenido, buenas noches!"

    st.subheader(saludo)

    usuario_bsc = st.text_input("Escribe tu usuario BSC:", "").strip()

    if not usuario_bsc:
        st.warning("Para continuar por favor ingresa tu usuario BSC")
    else:
        opciones_base = [
            "Consulta de modeler por área",
            "SLA Work Orders",
            "COP",
            "Share Point Tec Ops",
            "MUG",
            "Path escalations",
            "On-call"
        ]

        opciones_ordenadas = sorted(opciones_base, key=str.lower)
        opciones_enumeradas = [f"{i+1}. {opcion}" for i, opcion in enumerate(opciones_ordenadas)]
        opciones_con_placeholder = ["Selecciona una opción..."] + opciones_enumeradas

        tipo_consulta = st.selectbox("Selecciona el tipo de consulta:", opciones_con_placeholder)

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

                        modelers_database = {
                            "CTG": {
                                "Packaging": "Ana Pineda", "Boxing": "Carlos Alvarado", "FP": "Victor Campos",
                                "ZWG": "Jose Acuña", "Labs": "Sofía Soto", "Navegator": "Brayan Sanchez"
                            },
                            "CYL": {
                                "Packaging": "Mauricio Solís", "Boxing": "Juan Hernández", "FP": "Mariana Rojas",
                                "ZWG": "Esteban Chaves", "Labs": "Gabriela Quirós", "Navegator": "Andrés Fonseca"
                            },
                            "DRD": {
                                "Packaging": "Valeria Gamboa", "Boxing": "Roberto Delgado", "FP": "Natalia Esquivel",
                                "ZWG": "Kenneth Barboza", "Labs": "Daniela Meléndez", "Navegator": "Alejandro Orozco"
                            },
                            "HRD": {
                                "Packaging": "Lucía Mora", "Boxing": "Felipe Herrera", "FP": "Diego Gutiérrez",
                                "ZWG": "Tatiana Vargas", "Labs": "Melissa Blanco", "Navegator": "Ricardo Brenes"
                            }
                        }

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
                        st.write("**Consulta de Representantes por Área y Site**")
                        sites_cop = ["Selecciona site...", "CTG", "CYL", "DRD", "HRD"]
                        site_cop_sel = st.selectbox("Selecciona el site para los representantes:", sites_cop)
                        
                        if site_cop_sel != "Selecciona site...":
                            areas_representantes = ["Boxing", "FP", "Labs", "Navegator", "Packaging", "ZWG"]
                            rep_area_sel = st.selectbox("Selecciona el área para ver sus representantes:", ["Selecciona área..."] + areas_representantes)

                            if rep_area_sel != "Selecciona área...":
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
                                        "Boxing": {"mfg": "Felipe Herrera", "qa": "María Mora"},
                                        "FP": {"mfg": "Diego Gutiérrez", "qa": "Andrea Solís"},
                                        "Labs": {"mfg": "Melissa Blanco", "qa": "Kevin Araya"},
                                        "Navegator": {"mfg": "Ricardo Brenes", "qa": "Valeria Montero"},
                                        "Packaging": {"mfg": "Lucía Mora", "qa": "Esteban Cordero"},
                                        "ZWG": {"mfg": "Tatiana Vargas", "qa": "Gabriel Porras"}
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

                st.markdown("### Preguntas sugeridas")

                with st.expander("❔ ¿Quiénes son los Site Leads?"):
                    st.markdown("""
                    **Site Leads designados:**
                    - **CTG:** Eduardo Jenkins
                    - **CYL:** Sergio Monge
                    - **DRD:** Rebeca Alfaro
                    - **HRD:** Amanda Solano
                    """)

                with st.expander("❔ ¿Quién es el Manager de Tec Ops?"):
                    st.markdown("""
                    El manager del departamento de Tec Ops es **Francisco Castro**. 
                    Puedes escalar tu caso con él si, después de abrir el tiquete de soporte y seguir los canales correspondientes, no has obtenido respuesta.
                    """)

                with st.expander("❔ ¿Qué pasa si mi escalación ocurre un feriado o fin de semana?"):
                    st.markdown("""
                    **Protocolo para feriados y fines de semana**
                    El servicio On-call está disponible para situaciones críticas de líneas detenidas, Turno C, feriados y fines de semana.
                    **Contactos On-call:**
                    - **CYL:** 8888-8881
                    - **HRD:** 8888-8882
                    - **CTG:** 8888-8883
                    - **DRD:** 8888-8884
                    """)

            # --- SHARE POINT TEC OPS ---
            elif tipo_consulta_limpio == "Share Point Tec Ops":
                st.write("Visita nuestro share point a través del siguiente enlace: https://tecopssharepoint1234.com")
                st.text_area("Déjanos tu feedback sobre Share Point:", "", key="feedback_sp")

            # --- SLA WORK ORDERS ---
            elif tipo_consulta_limpio == "SLA Work Orders":
                docs_input = st.text_input("¿Cuántos documentos vas a someter en el cambio?", "")
                if docs_input:
                    if not docs_input.isdigit():
                        st.error("Número inválido. Por favor, ingresa únicamente números enteros.")
                    else:
                        num_docs = int(docs_input)
                        if 1 <= num_docs <= 4:
                            st.success("El SLA es de **3 días**.")
                        elif 5 <= num_docs <= 10:
                            st.success("El SLA es de **5 días**.")
                        elif 11 <= num_docs <= 20:
                            st.success("El SLA es de **9 días**.")
                        elif num_docs >= 21:
                            st.warning("El SLA debe verse directamente con el modeler ya que es un proyecto.")

        # --- BANNER Y BOTÓN PARA ABRIR EL CHATBOT ---
        st.markdown("""
        <div class="bot-card-banner">
            <h3 style="margin: 0 0 10px 0; color: #FFFFFF !important;">🤖 ¿Necesitas asistencia personalizada?</h3>
            <p style="margin: 0; color: #E0E6ED !important;">
                Consulta con nuestro asistente virtual inteligente especializado en <strong>Tec Ops</strong> para resolver cualquier duda sobre asignaciones, normas y procesos en tiempo real.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🤖 Abrir Chatbot de Asistencia Tec Ops", key="btn_abrir_chat"):
            st.session_state.pagina_actual = "chatbot"
            st.rerun()


# ==============================================================================
# PÁGINA INDEPENDIENTE DEL CHATBOT
# ==============================================================================
elif st.session_state.pagina_actual == "chatbot":

    col_nav1, col_nav2 = st.columns([7, 3])
    with col_nav1:
        st.title("🤖 Asistente Virtual Tec Ops")
        st.caption("Inteligencia Artificial especializada para soporte de Tec Ops")
    with col_nav2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("⬅️ Regresar al Menú Principal", key="btn_regresar"):
            st.session_state.pagina_actual = "principal"
            st.rerun()

    st.markdown("---")

    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        st.info("ℹ️ Para habilitar el Chatbot, asegura la configuración de la clave en Streamlit Secrets o como variable de entorno `GEMINI_API_KEY`.")
    else:
        if "chat_messages" not in st.session_state:
            st.session_state.chat_messages = []

        for message in st.session_state.chat_messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if user_prompt := st.chat_input("Escribe tu consulta sobre Tec Ops..."):
            st.session_state.chat_messages.append({"role": "user", "content": user_prompt})
            with st.chat_message("user"):
                st.markdown(user_prompt)

            with st.chat_message("assistant"):
                try:
                    client = genai.Client(api_key=api_key)
                    
                    contexto_tec_ops = """
                    Eres el asistente virtual oficial del departamento de Tec Ops. Cuentas con la siguiente información:
                    - Modelers por site y área:
                      * CTG: Packaging (Ana Pineda), Boxing (Carlos Alvarado), FP (Victor Campos), ZWG (Jose Acuña), Labs (Sofía Soto), Navegator (Brayan Sanchez)
                      * CYL: Packaging (Mauricio Solís), Boxing (Juan Hernández), FP (Mariana Rojas), ZWG (Esteban Chaves), Labs (Gabriela Quirós), Navegator (Andrés Fonseca)
                      * DRD: Packaging (Valeria Gamboa), Boxing (Roberto Delgado), FP (Natalia Esquivel), ZWG (Kenneth Barboza), Labs (Daniela Meléndez), Navegator (Alejandro Orozco)
                      * HRD: Packaging (Lucía Mora), Boxing (Felipe Herrera), FP (Diego Gutiérrez), ZWG (Tatiana Vargas), Labs (Melissa Blanco), Navegator (Ricardo Brenes)
                    - Sesiones COP:
                      * COP CYL - Lunes 10am
                      * COP HRD - Martes 10am
                      * COP DRD - Miércoles 10am
                      * COP CTG - Jueves 10am
                    - COP Leads & Site Leads:
                      * CTG: Eduardo Jenkins | CYL: Sergio Monge | DRD: Rebeca Alfaro | HRD: Amanda Solano
                    - Manager de Tec Ops: Francisco Castro.
                    - Teléfonos de Servicio On-call (líneas detenidas, Turno C, feriados/fines de semana, solo llamadas):
                      * CYL: 8888-8881 | HRD: 8888-8882 | CTG: 8888-8883 | DRD: 8888-8884
                    Responde de forma clara, directa, amable y profesional.
                    """

                    response = client.models.generate_content(
                        model="gemini-3.8-flash",
                        contents=f"{contexto_tec_ops}\n\nPregunta del usuario: {user_prompt}",
                    )
                    assistant_response = response.text
                    st.markdown(assistant_response)
                    st.session_state.chat_messages.append({"role": "assistant", "content": assistant_response})
                except Exception as e:
                    st.error(f"Error al conectar con el servicio de IA: {e}")
