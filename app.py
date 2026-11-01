import os
import streamlit as str_app
from datetime import datetime
from google import genai

# --- CONFIGURACIÓN DE PÁGINA Y NAVEGACIÓN ---
str_app.set_page_config(
    page_title="Tec Ops Portal - MedTech Support",
    page_icon="💻",
    layout="wide"
)

if "pagina_actual" not in str_app.session_state:
    str_app.session_state.pagina_actual = "principal"

# --- CONFIGURACIÓN VISUAL GENERAL Y ESTILOS "TECH MED" ---
str_app.markdown("""
<style>

/* Fondo degradado Tech Med */
.stApp,
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0B1021 0%, #121B36 50%, #1A264A 100%) !important;
}

/* Encabezado */
[data-testid="stHeader"] {
    background-color: transparent !important;
}

/* Texto general en blanco suave */
h1, h2, h3, h4, h5, h6,
p, li, label,
[data-testid="stMarkdownContainer"] {
    color: #F0F4F8 !important;
}

h1 { font-weight: 700 !important; letter-spacing: 0.5px; }
h2, h3 { font-weight: 600 !important; }

/* Tarjetas con efecto Vidrio / Glassmorphism */
[data-testid="stAlert"], 
[data-testid="stExpander"], 
.bot-card-banner,
.rating-card {
    background: rgba(255, 255, 255, 0.04) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(0, 229, 255, 0.25) !important;
    border-radius: 16px !important;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3) !important;
}

/* === GARANTÍA DE LEGIBILIDAD EN INPUTS Y BOTONES === */

input,
textarea,
[data-baseweb="input"] input,
[data-testid="stTextArea"] textarea {
    background-color: #FFFFFF !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    border-radius: 10px !important;
    font-weight: 500 !important;
}

[data-baseweb="select"],
[data-baseweb="select"] * {
    background-color: #FFFFFF !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    border-radius: 10px !important;
}

[role="listbox"],
[role="option"] {
    background-color: #FFFFFF !important;
    color: #000000 !important;
}

/* Botones con brillo futurista MedTech (Acción principal) */
.stButton > button {
    background: linear-gradient(135deg, #00E5FF 0%, #0052CC 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    padding: 8px 20px !important;
    box-shadow: 0px 4px 15px rgba(0, 229, 255, 0.3) !important;
    transition: all 0.25s ease-in-out !important;
}

.stButton > button * {
    color: #FFFFFF !important;
}

.stButton > button:hover {
    box-shadow: 0px 6px 20px rgba(0, 229, 255, 0.6) !important;
    transform: translateY(-2px) !important;
}

/* Botones de envío dentro de formularios (MUG y Share Point) con texto legible oscuro */
[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #00E5FF 0%, #0052CC 100%) !important;
    color: #FFFFFF !important;
}

[data-testid="stFormSubmitButton"] > button * {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

[data-testid="stAlert"] p,
[data-testid="stAlert"] strong {
    color: #F0F4F8 !important;
}

/* Legibilidad perfecta en los Expanders (Preguntas sugeridas) */
[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary p,
[data-testid="stExpander"] summary span {
    color: #F0F4F8 !important;
    font-weight: 600 !important;
}

[data-testid="stExpander"] [data-testid="stMarkdownContainer"] p,
[data-testid="stExpander"] [data-testid="stMarkdownContainer"] li,
[data-testid="stExpander"] [data-testid="stMarkdownContainer"] strong {
    color: #000000 !important;
}

[data-testid="stExpander"] [data-testid="stExpanderDetails"] {
    background-color: #FFFFFF !important;
    border-radius: 0 0 12px 12px !important;
    padding: 15px !important;
}

/* === ESTILOS PARA EL CHATBOT === */

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

[data-testid="stBottomBlockContainer"] {
    background-color: transparent !important;
    padding-bottom: 25px !important;
    padding-top: 10px !important;
}

[data-testid="stChatInput"] {
    background-color: #FFFFFF !important;
    border-radius: 14px !important;
    border: 2px solid #00E5FF !important;
    box-shadow: 0px 4px 20px rgba(0, 229, 255, 0.25) !important;
    padding: 4px !important;
}

[data-testid="stChatInput"] textarea {
    font-size: 16px !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
}

.bot-card-banner {
    background: linear-gradient(135deg, rgba(0, 229, 255, 0.1) 0%, rgba(0, 114, 255, 0.2) 100%);
    border-radius: 20px;
    padding: 24px;
    border: 1px solid #00E5FF;
    box-shadow: 0px 8px 25px rgba(0, 229, 255, 0.15);
    margin-top: 25px;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# ==============================================================================
# PÁGINA PRINCIPAL
# ==============================================================================
if str_app.session_state.pagina_actual == "principal":

    str_app.title("💻 Sistema de consultas generales del departamento Tec Ops")
    str_app.markdown("---")

    ahora = datetime.now().time()
    hora_actual = ahora.hour
    minuto_actual = ahora.minute

    if 0 <= hora_actual < 12:
        saludo = "¡Bienvenido, buenos días!"
    elif 12 <= hora_actual < 18 or (hora_actual == 18 and minuto_actual == 0):
        saludo = "¡Bienvenido, buenas tardes!"
    else:
        saludo = "¡Bienvenido, buenas noches!"

    str_app.subheader(saludo)

    usuario_bsc = str_app.text_input("Escribe tu usuario BSC:", "").strip()

    # Validación de usuario BSC
    if not usuario_bsc:
        str_app.info("Recuerda que el usuario BSC debe contener al menos 5 caracteres alfanuméricos.")
    elif len(usuario_bsc) < 5 or not usuario_bsc.isalnum():
        str_app.warning("⚠️ Usuario no reconocido. Por favor, verifica tus datos. Recuerda que el usuario BSC debe contener al menos 5 caracteres alfanuméricos.")
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

        tipo_consulta = str_app.selectbox("Selecciona el tipo de consulta:", opciones_con_placeholder)

        if tipo_consulta != "Selecciona una opción...":
            tipo_consulta_limpio = tipo_consulta.split(". ", 1)[1] if ". " in tipo_consulta else tipo_consulta

            # --- CONSULTA MODELER POR ÁREA ---
            if tipo_consulta_limpio == "Consulta de modeler por área":
                sites_disponibles = ["Selecciona un site...", "CTG", "CYL", "DRD", "HRD"]
                site_seleccionado = str_app.selectbox("Selecciona el site:", sites_disponibles)

                if site_seleccionado != "Selecciona un site...":
                    sub_opciones_base = ["Navegator", "Packaging", "Boxing", "FP", "ZWG", "Labs"]
                    sub_opciones_ordenadas = sorted(sub_opciones_base, key=str.lower)
                    sub_opciones_enumeradas = [f"{i+1}. {opcion}" for i, opcion in enumerate(sub_opciones_ordenadas)]
                    sub_opciones_con_placeholder = ["Selecciona una opción de área..."] + sub_opciones_enumeradas

                    area_seleccionada = str_app.selectbox("Selecciona el área:", sub_opciones_con_placeholder)

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
                        str_app.info(f"El modeler de **{area_limpia}** para **{site_seleccionado}** es **{modeler_nombre}**")

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

                opcion_cop = str_app.selectbox("Selecciona una opción de COP:", cop_con_placeholder)

                if opcion_cop != "Selecciona una opción de COP...":
                    cop_limpio = opcion_cop.split(". ", 1)[1] if ". " in opcion_cop else opcion_cop

                    if cop_limpio == "Horarios":
                        str_app.write("**Horarios de sesiones COP:**")
                        str_app.write("- **COP CYL** - Lunes 10am")
                        str_app.write("- **COP HRD** - Martes 10am")
                        str_app.write("- **COP DRD** - Miércoles 10am")
                        str_app.write("- **COP CTG** - Jueves 10am")

                    elif cop_limpio == "¿Qué material debo llevar al COP?":
                        str_app.write("Para la sesión del COP, se recomienda preparar una presentación breve que permita explicar claramente el caso, el alcance del cambio y su propósito.")
                        str_app.write("Es importante incluir la siguiente información:")
                        str_app.write("- **Descripción del cambio:** explicar qué se desea modificar, por qué es necesario y cuál es el objetivo esperado.")
                        str_app.write("- **Flujo de trabajo (Workflow):** incluir, preferiblemente, el flujo actual y/o propuesto para facilitar la comprensión del proceso y de los cambios requeridos.")
                        str_app.write("- **Documentación de soporte:** adjuntar cualquier información, evidencia o referencia que ayude a los Modelers a comprender mejor el alcance y los requerimientos del cambio.")
                        str_app.write("- **Fechas relevantes:** tener identificadas las fechas previstas de implementación, así como cualquier fecha límite o compromiso asociado al proyecto.")
                        str_app.write("- **Impacto del cambio:** mencionar las áreas, procesos o sistemas que podrían verse involucrados, cuando corresponda.")
                        str_app.info("💡 **Recomendación:** entre más clara y completa sea la información presentada, más efectiva será la evaluación del caso y la orientación que los Modelers puedan brindar durante la sesión.")

                    elif cop_limpio == "Representantes por área":
                        str_app.write("**Consulta de Representantes por Área y Site**")
                        sites_cop = ["Selecciona site...", "CTG", "CYL", "DRD", "HRD"]
                        site_cop_sel = str_app.selectbox("Selecciona el site para los representantes:", sites_cop)
                        
                        if site_cop_sel != "Selecciona site...":
                            areas_representantes = ["Boxing", "FP", "Labs", "Navegator", "Packaging", "ZWG"]
                            rep_area_sel = str_app.selectbox("Selecciona el área para ver sus representantes:", ["Selecciona área..."] + areas_representantes)

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
                                str_app.write(f"**Representantes de {rep_area_sel} en {site_cop_sel}:**")
                                str_app.write(f"- **Ing. Manufactura:** {rep_info.get('mfg', 'No asignado')}")
                                str_app.write(f"- **Ing. Calidad:** {rep_info.get('qa', 'No asignado')}")

                    elif cop_limpio == "¿Cuándo debo llevar mi cambio o proyecto al COP?":
                        str_app.write("Debes presentar tu cambio o proyecto en el COP cuando se presente alguna de las siguientes condiciones:")
                        str_app.write("- **El cambio esté relacionado con un CAPA o un NCEP.**")
                        str_app.write("- **Se trate de un cambio complejo que requiera evaluación o discusión multidisciplinaria.**")
                        str_app.write("- **El Modeler recomiende presentar el cambio o proyecto ante el COP.**")
                        str_app.write("- **Tengas dudas sobre el desarrollo, alcance o implementación del proyecto y necesites orientación, recomendaciones o acompañamiento para su adecuada ejecución.**")

                    elif cop_limpio == "COP Leads":
                        str_app.write("**Líderes de COP por cada Site:**")
                        str_app.write("- **Lead de COP CTG:** Eduardo Jenkins")
                        str_app.write("- **Lead de COP CYL:** Sergio Monge")
                        str_app.write("- **Lead de COP DRD:** Rebeca Alfaro")
                        str_app.write("- **Lead de COP HRD:** Amanda Solano")

            # --- MUG ---
            elif tipo_consulta_limpio == "MUG":
                str_app.write("Para accesar al MUG haz click en el siguiente enlace: https://MUG.guide1234.com")
                str_app.write("Si tienes feedback para la guía por favor contactar a uno de los modelers o deja tu comentario en la siguiente caja.")
                
                with str_app.form(key="form_feedback_mug"):
                    comentario_mug = str_app.text_area("Déjanos tus comentarios sobre MUG:", "", key="feedback_mug")
                    submit_mug = str_app.form_submit_button("Enviar comentario MUG")
                    if submit_mug:
                        if comentario_mug.strip():
                            str_app.success("¡Muchas gracias! Tu comentario sobre MUG ha sido enviado exitosamente.")
                        else:
                            str_app.warning("Por favor escribe un comentario antes de enviar.")

            # --- ON-CALL ---
            elif tipo_consulta_limpio == "On-call":
                str_app.info("El servicio de oncall se da únicamente para líneas detenidas, en turno C, feriados y fines de semana.")
                str_app.write("**Teléfonos de contacto:**")
                str_app.write("- **CYL:** 8888-8881")
                str_app.write("- **HRD:** 8888-8882")
                str_app.write("- **CTG:** 8888-8883")
                str_app.write("- **DRD:** 8888-8884")
                str_app.warning("⚠️ Solo llamadas, no mensajes ni llamadas por WhatsApp.")
                str_app.write("Al llamar asegúrese de abrir el tiquete primero con toda la evidencia y explicación del issue. Si no recibe respuesta por favor escalar el caso con el manager del departamento **Francisco Castro**.")

            # --- PATH ESCALATIONS ---
            elif tipo_consulta_limpio == "Path escalations":
                str_app.write("Si necesita ayuda urgente con la aprobación de un incidente, work order, acceso, aprobación de máscara o aprobación de CN por favor contacte primero al site lead que corresponda o con el manager.")
                str_app.info("Todas las escalaciones deben documentarse por correo con la explicación de porqué se le debe de dar prioridad.")

                str_app.markdown("### Preguntas sugeridas")

                with str_app.expander("¿Quiénes son los Site Leads designados?"):
                    str_app.markdown("""
                    - **CTG:** Eduardo Jenkins
                    - **CYL:** Sergio Monge
                    - **DRD:** Rebeca Alfaro
                    - **HRD:** Amanda Solano
                    """)

                with str_app.expander("¿Qué pasa si debo escalar alguna ayuda un feriado o fin de semana?"):
                    str_app.markdown("""
                    Para líneas detenidas en **turno C, feriados y fines de semana**, se cuenta con el servicio **On-call** (solo llamadas):
                    - **CYL:** 8888-8881
                    - **HRD:** 8888-8882
                    - **CTG:** 8888-8883
                    - **DRD:** 8888-8884
                    
                    *Nota: Asegúrese de abrir el tiquete primero con toda la evidencia y explicación del issue antes de llamar.*
                    """)

                with str_app.expander("¿Quién es el manager del departamento?"):
                    str_app.markdown("""
                    El manager del departamento de Tec Ops es **Francisco Castro**. Si no recibe respuesta o requiere una escalación mayor de prioridad, puede contactarle directamente.
                    """)

            # --- SHARE POINT TEC OPS ---
            elif tipo_consulta_limpio == "Share Point Tec Ops":
                str_app.write("Visita nuestro share point a través del siguiente enlace: https://tecopssharepoint1234.com")
                
                with str_app.form(key="form_feedback_sp"):
                    comentario_sp = str_app.text_area("Déjanos tu feedback sobre Share Point:", "", key="feedback_sp")
                    submit_sp = str_app.form_submit_button("Enviar comentario Share Point")
                    if submit_sp:
                        if comentario_sp.strip():
                            str_app.success("¡Muchas gracias! Tu comentario sobre Share Point ha sido enviado exitosamente.")
                        else:
                            str_app.warning("Por favor escribe un comentario antes de enviar.")

            # --- SLA WORK ORDERS ---
            elif tipo_consulta_limpio == "SLA Work Orders":
                docs_input = str_app.text_input("¿Cuántos documentos vas a someter en el cambio?", "")
                if docs_input:
                    if not docs_input.isdigit():
                        str_app.error("Número inválido. Por favor, ingresa únicamente números enteros.")
                    else:
                        num_docs = int(docs_input)
                        if 1 <= num_docs <= 4:
                            str_app.success("El SLA es de **3 días**.")
                        elif 5 <= num_docs <= 10:
                            str_app.success("El SLA es de **5 días**.")
                        elif 11 <= num_docs <= 20:
                            str_app.success("El SLA es de **9 días**.")
                        elif num_docs >= 21:
                            str_app.warning("El SLA debe verse directamente con el modeler ya que es un proyecto.")

        # --- BANNER ACCESO A IA ---
        str_app.markdown("""
        <div class="bot-card-banner">
            <h3 style="margin: 0 0 10px 0; color: #FFFFFF !important;">🤖 Asistente Virtual Inteligente Tec Ops</h3>
            <p style="margin: 0; color: #E0E6ED !important;">
                ¿Dudas sobre nuestros servicios? Consulta en tiempo real con nuestra Inteligencia Artificial oficial.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if str_app.button("🤖 Abrir Chatbot de Asistencia Tec Ops", key="btn_abrir_chat"):
            str_app.session_state.pagina_actual = "chatbot"
            str_app.rerun()

        # --- SECCIÓN DE CALIFICACIÓN POR ESTRELLAS INTERACTIVA ---
        str_app.markdown("<br>", unsafe_allow_html=True)
        str_app.markdown("### ⭐ Califica tu experiencia con la aplicación")
        
        # Componente interactivo de estrellas integrado en Streamlit
        feedback_estrella = str_app.feedback("stars", key="rating_stars")

        if feedback_estrella is not None:
            puntos = feedback_estrella + 1  # st.feedback devuelve índices de 0 a 4
            if str_app.button("Enviar Calificación", key="btn_enviar_calif"):
                if puntos <= 3:
                    str_app.info("💡 ¡Muchas gracias por tu comentario! Ten por seguro que seguiremos mejorando, ya que la aplicación está en constante cambio para brindarte una mejor experiencia.")
                else:
                    str_app.success(f"¡Muchas gracias por calificar con {puntos} estrellas! Nos alegra que disfrutes de la aplicación.")


# ==============================================================================
# PÁGINA INDEPENDIENTE DEL CHATBOT
# ==============================================================================
elif str_app.session_state.pagina_actual == "chatbot":

    col_nav1, col_nav2 = str_app.columns([7, 3])
    with col_nav1:
        str_app.title("🤖 Asistente Virtual Tec Ops")
        str_app.caption("Inteligencia Artificial especializada para soporte de Tec Ops")
    with col_nav2:
        # Botones de navegación arriba a la derecha en formato vertical
        if str_app.button("🗑️ Limpiar Chat", key="btn_limpiar", use_container_width=True):
            str_app.session_state.chat_messages = []
            str_app.rerun()
        if str_app.button("⬅️ Menú Principal", key="btn_regresar", use_container_width=True):
            str_app.session_state.pagina_actual = "principal"
            str_app.rerun()

    str_app.markdown("---")

    # --- CONSULTAS RÁPIDAS (EN FORMATO VERTICAL) ---
    str_app.write("**Consultas rápidas:**")
    prompt_sugerido = None
    
    if str_app.button("📞 Ver teléfonos On-Call", key="pill1"):
        prompt_sugerido = "¿Cuáles son los números de teléfono del servicio On-call?"
    if str_app.button("📅 Horarios del COP", key="pill2"):
        prompt_sugerido = "¿Cuáles son los horarios de las sesiones del COP por site?"
    if str_app.button("👤 Ver Site Leads", key="pill3"):
        prompt_sugerido = "¿Quiénes son los Site Leads de Tec Ops?"

    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        str_app.info("ℹ️ Para habilitar el Chatbot, asegura la configuración de la clave en Streamlit Secrets o como variable de entorno `GEMINI_API_KEY`.")
    else:
        if "chat_messages" not in str_app.session_state:
            str_app.session_state.chat_messages = []

        # Historial de mensajes
        for message in str_app.session_state.chat_messages:
            with str_app.chat_message(message["role"]):
                str_app.markdown(message["content"])

        # Captura de entrada del usuario o botón sugerido
        user_prompt = str_app.chat_input("Escribe tu consulta sobre Tec Ops...") or prompt_sugerido

        if user_prompt:
            str_app.session_state.chat_messages.append({"role": "user", "content": user_prompt})
            with str_app.chat_message("user"):
                str_app.markdown(user_prompt)

            with str_app.chat_message("assistant"):
                try:
                    client = genai.Client(api_key=api_key)
                    
                    contexto_tec_ops = """
                    Eres el asistente virtual oficial del departamento de Tec Ops. 
                    
                    INSTRUCCIONES DE COMPORTAMIENTO Y TONO:
                    1. Sé siempre extremadamente amable, respetuoso, cálido y educado. Usa un lenguaje profesional pero cercano.
                    2. Siempre saluda amablemente cuando el usuario diga "hola", "buenos días", "buenas tardes", etc. (por ejemplo: "¡Hola! Es un gusto saludarte. ¿En qué puedo colaborarte el día de hoy?").
                    3. Da las gracias de manera cordial y muestra siempre disposición para ayudar.
                    4. NUNCA dejes al usuario sin respuesta. Si te pregunta algo de lo que no tienes datos específicos o no logras comprender del todo la consulta, responde con amabilidad (por ejemplo: "Muchas gracias por tu consulta. Lamentablemente no cuento con la información exacta sobre ese tema en este momento, pero con mucho gusto te puedo ayudar a contactar con tu Site Lead o el Manager Francisco Castro para orientarte mejor. ¿Deseas que te comparta sus contactos?").

                    BASE DE DATOS DE TEC OPS:
                    - Modelers por site y área:
                      * CTG: Packaging (Ana Pineda), Boxing (Carlos Alvarado), FP (Victor Campos), ZWG (Jose Acuña), Labs (Sofía Soto), Navegator (Brayan Sanchez)
                      * CYL: Packaging (Mauricio Solís), Boxing (Juan Hernández), FP (Mariana Rojas), ZWG (Esteban Chaves), Labs (Gabriela Quirós), Navegator (Andrés Fonseca)
                      * DRD: Packaging (Valeria Gamboa), Boxing (Roberto Delgado), FP (Natalia Esquivel), ZWG (Kenneth Barboza), Labs (Daniela Meléndez), Navegator (Alejandro Orozco)
                      * HRD: Packaging (Lucía Mora), Boxing (Felipe Herrera), FP (Diego Gutiérrez), ZWG (Tatiana Vargas), Labs (Melissa Blanco), Navegator (Ricardo Brenes)
                    - Sesiones COP:
                      * COP CYL - Lunes 10am | COP HRD - Martes 10am | COP DRD - Miércoles 10am | COP CTG - Jueves 10am
                    - COP Leads & Site Leads:
                      * CTG: Eduardo Jenkins | CYL: Sergio Monge | DRD: Rebeca Alfaro | HRD: Amanda Solano
                    - Manager de Tec Ops: Francisco Castro.
                    - Teléfonos de Servicio On-call (líneas detenidas, Turno C, feriados/fines de semana, solo llamadas):
                      * CYL: 8888-8881 | HRD: 8888-8882 | CTG: 8888-8883 | DRD: 8888-8884
                    """

                    response = client.models.generate_content(
                        model="gemini-3.8-flash",
                        contents=f"{contexto_tec_ops}\n\nPregunta del usuario: {user_prompt}",
                    )
                    assistant_response = response.text
                    str_app.markdown(assistant_response)
                    str_app.session_state.chat_messages.append({"role": "assistant", "content": assistant_response})
                except Exception as e:
                    if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                        str_app.warning("⚠️ En este momento el asistente ha alcanzado el límite diario de consultas de la API. Por favor, intenta de nuevo más tarde.")
                    else:
                        str_app.error(f"Error al conectar con el servicio de IA: {e}")
