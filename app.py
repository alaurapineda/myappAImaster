import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Aplicación de consultas Tec Ops", page_icon="🧭", layout="centered")

# -------------------- ESTILOS --------------------
st.markdown("""
<style>
.stApp, [data-testid="stAppViewContainer"] {background:#191970 !important;}
[data-testid="stHeader"] {background:transparent !important;}
h1,h2,h3,h4,h5,h6,p,label,li,[data-testid="stMarkdownContainer"] {color:#FFFFFF !important;}
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea,
[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea {
    background:#FFFFFF !important; color:#202020 !important;
    -webkit-text-fill-color:#202020 !important; border-radius:8px !important;
}
[data-testid="stTextInput"] label,
[data-testid="stTextArea"] label,
[data-testid="stSelectbox"] label {color:#FFFFFF !important;}
[data-baseweb="select"] > div {background:#FFFFFF !important; color:#202020 !important;}
[data-baseweb="select"] * {color:#202020 !important;}
[role="listbox"],[role="option"] {background:#FFFFFF !important;color:#202020 !important;}
.stButton > button {
    background:#EAF7F7 !important; color:#172B3A !important;
    border:1px solid #D2EEEE !important; border-radius:10px !important;
    font-weight:600 !important;
}
.stButton > button:hover {background:#D9F0FA !important;color:#172B3A !important;}
[data-testid="stAlert"] {background:#D9F0FA !important;border-radius:12px !important;}
[data-testid="stAlert"] p,[data-testid="stAlert"] strong {color:#172B3A !important;}
[data-testid="stExpander"] {
    background:#EAF7F7 !important;border:1px solid #D2EEEE !important;
    border-radius:16px !important;margin-bottom:12px !important;overflow:hidden !important;
}
[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary p {
    color:#172B3A !important;font-size:16px !important;font-weight:600 !important;
}
[data-testid="stExpander"] [data-testid="stMarkdownContainer"],
[data-testid="stExpander"] p,
[data-testid="stExpander"] li,
[data-testid="stExpander"] strong {color:#172B3A !important;}
hr {border-color:rgba(255,255,255,.25) !important;}
</style>
""", unsafe_allow_html=True)

# -------------------- ENCABEZADO --------------------
st.title("Aplicación de consultas Tec Ops")
ahora = datetime.now().time()
if ahora.hour < 12:
    saludo = "¡Bienvenido, buenos días!"
elif ahora.hour < 18 or (ahora.hour == 18 and ahora.minute == 0):
    saludo = "¡Bienvenido, buenas tardes!"
else:
    saludo = "¡Bienvenido, buenas noches!"
st.subheader(saludo)

usuario_bsc = st.text_input("Escribe tu usuario BSC:", placeholder="Usuario BSC").strip()

if not usuario_bsc:
    st.warning("Para continuar, por favor ingresa tu usuario BSC.")
else:
    opciones = [
        "Consulta de modeler por área", "SLA Work Orders", "COP",
        "Share Point Tec Ops", "MUG", "Path escalations", "On-call"
    ]
    opciones = sorted(opciones, key=str.lower)
    seleccion = st.selectbox(
        "Selecciona el tipo de consulta:",
        ["Selecciona una opción..."] + [f"{i+1}. {x}" for i, x in enumerate(opciones)]
    )

    if seleccion != "Selecciona una opción...":
        tipo = seleccion.split(". ", 1)[1]

        # -------------------- MODELER --------------------
        if tipo == "Consulta de modeler por área":
            modelers = {
                "Packaging": "Ana Pineda",
                "Boxing": "Juan Hernández",
                "FP": "Victor Campos",
                "ZWG": "Jose Acuña",
                "Labs": "Sofía Soto",
                "Navegator": "Brayan Sanchez"
            }
            area = st.selectbox("Selecciona el área:", ["Selecciona una opción de área..."] + sorted(modelers))
            if area != "Selecciona una opción de área...":
                st.info(f"El modeler de {area} es **{modelers[area]}**.")

        # -------------------- COP --------------------
        elif tipo == "COP":
            opciones_cop = [
                "Horarios", "¿Qué material debo llevar al COP?",
                "Representantes por área",
                "¿Cuándo debo llevar mi cambio o proyecto al COP?", "COP Leads"
            ]
            opcion = st.selectbox(
                "Selecciona una opción de COP:",
                ["Selecciona una opción de COP..."] +
                [f"{i+1}. {x}" for i, x in enumerate(sorted(opciones_cop, key=str.lower))]
            )
            if opcion != "Selecciona una opción de COP...":
                cop = opcion.split(". ", 1)[1]
                if cop == "Horarios":
                    st.markdown("""**Horarios de sesiones COP:**
- **COP CYL:** Lunes, 10:00 a. m.
- **COP HRD:** Martes, 10:00 a. m.
- **COP DRD:** Miércoles, 10:00 a. m.
- **COP CTG:** Jueves, 10:00 a. m.""")
                elif cop == "¿Qué material debo llevar al COP?":
                    st.markdown("""Prepara una presentación breve que explique el caso, su alcance y el propósito de llevarlo al COP.

Incluye, según corresponda:
- Descripción del cambio o proyecto.
- Flujo de trabajo actual y flujo propuesto.
- Documentación de soporte y evidencia.
- Fechas de implementación y fechas límite.
- Impacto en áreas, procesos y sistemas involucrados.

Mientras más clara esté la información, más productiva será la discusión. Confirma con tu encargado si tu caso requiere documentación adicional.""")
                elif cop == "Representantes por área":
                    reps = {
                        "Boxing": {"Ing. Manufactura": "Luis Sandoval", "Ing. Calidad": "Laura Pineda"},
                        "FP": {"Ing. Manufactura": "Tania Villanueva", "Ing. Calidad": "Karol Hernández"},
                        "Labs": {"Ing. Manufactura": "Carlos Mendéz / Karla Mora", "Ing. Calidad": "Pablo González"},
                        "Navegator": {"Ing. Manufactura": "Jorge Chaves", "Ing. Calidad": "María José Sanchez"},
                        "Packaging": {"Ing. Manufactura": "Josué González", "Ing. Calidad": "Carolina Barrantes"},
                        "ZWG": {"Ing. Calidad": "Luisa Hernández"}
                    }
                    area_rep = st.selectbox("Selecciona el área para ver sus representantes:", ["Selecciona área..."] + sorted(reps))
                    if area_rep != "Selecciona área...":
                        st.markdown(f"**{area_rep}:**")
                        for rol, persona in reps[area_rep].items():
                            st.markdown(f"- **{rol}:** {persona}")
                elif cop == "¿Cuándo debo llevar mi cambio o proyecto al COP?":
                    st.markdown("""Considera presentar tu cambio o proyecto en el COP cuando:
- Está relacionado con una CAPA o un NCEP.
- Es un cambio complejo que requiere discusión multidisciplinaria.
- El modeler recomienda llevarlo al COP.
- Tienes dudas sobre el alcance, impacto o implementación y necesitas orientación de las áreas involucradas.

Si no estás seguro de si tu caso debe presentarse, consulta con tu modeler o encargado.""")
                elif cop == "COP Leads":
                    leads = {"CTG": "Eduardo Jenkins", "CYL": "Sergio Monge", "DRD": "Rebeca Alfaro", "HRD": "Amanda Solano"}
                    st.markdown("**COP Leads por site:**")
                    for site, lead in leads.items():
                        st.markdown(f"- **{site}:** {lead}")

        # -------------------- MUG --------------------
        elif tipo == "MUG":
            st.write("Para acceder al MUG, utiliza el siguiente enlace:")
            st.markdown("[Abrir MUG](https://MUG.guide1234.com)")
            st.write("Si tienes feedback para la guía, puedes contactar a uno de los modelers o dejar tu comentario.")
            st.text_area("Déjanos tus comentarios sobre MUG:", key="feedback_mug")

        # -------------------- ON-CALL --------------------
        elif tipo == "On-call":
            st.info("El servicio de On-call aplica únicamente para situaciones críticas de línea detenida durante Turno C, feriados y fines de semana.")
            st.markdown("""**Teléfonos de contacto:**
- **CYL:** 8888-8881
- **HRD:** 8888-8882
- **CTG:** 8888-8883
- **DRD:** 8888-8884""")
            st.warning("Únicamente llamadas telefónicas. No se atienden mensajes de texto ni llamadas por WhatsApp.")
            st.markdown("""Antes de llamar:
1. Abre el tiquete correspondiente.
2. Incluye toda la evidencia disponible.
3. Explica claramente el problema y el impacto en la línea.

Si no recibes respuesta, escala el caso con el manager del departamento, **Francisco Castro**.""")

        # -------------------- PATH ESCALATIONS --------------------
        elif tipo == "Path escalations":
            st.markdown("Si necesitas ayuda urgente con la aprobación de un incidente, Work Order, acceso, aprobación de máscara o aprobación de CN, contacta primero al Site Lead correspondiente o al manager.")
            st.info("Todas las escalaciones deben documentarse por correo, incluyendo la explicación de por qué se requiere prioridad.")
            st.markdown("### Preguntas frecuentes")
            with st.expander("❔ ¿Quiénes son los Site Leads?"):
                st.markdown("""- **CTG:** Eduardo Jenkins
- **CYL:** Sergio Monge
- **DRD:** Rebeca Alfaro
- **HRD:** Amanda Solano""")
            with st.expander("❔ ¿Quién es el Manager de Tec Ops?"):
                st.markdown("El Manager de Tec Ops es **Francisco Castro**.")
            with st.expander("❔ ¿Qué pasa si mi escalación ocurre un feriado o fin de semana?"):
                st.markdown("""Para situaciones críticas que provoquen una línea detenida, puedes utilizar el servicio de On-call.

**Contactos:**
- **CYL:** 8888-8881
- **HRD:** 8888-8882
- **CTG:** 8888-8883
- **DRD:** 8888-8884

Debes abrir primero un tiquete con la evidencia y explicación del problema. El contacto de On-call es únicamente por llamada telefónica, no por mensajes ni WhatsApp.""")

        # -------------------- SHAREPOINT --------------------
        elif tipo == "Share Point Tec Ops":
            st.write("Visita nuestro SharePoint a través del siguiente enlace:")
            st.markdown("[Abrir SharePoint Tec Ops](https://tecopssharepoint1234.com)")
            st.write("Si tienes feedback para la guía, puedes contactar a uno de los modelers o dejar tu comentario.")
            st.text_area("Déjanos tu feedback sobre SharePoint:", key="feedback_sp")

        # -------------------- SLA WORK ORDERS --------------------
        elif tipo == "SLA Work Orders":
            docs = st.text_input("¿Cuántos documentos vas a someter en el cambio?", key="cantidad_documentos").strip()
            if docs:
                if not docs.isdigit():
                    st.error("Número inválido. Ingresa únicamente números enteros sin letras, comas ni signos.")
                else:
                    n = int(docs)
                    if 1 <= n <= 4:
                        st.success("El SLA es de **3 días**.")
                    elif 5 <= n <= 10:
                        st.success("El SLA es de **5 días**.")
                    elif 11 <= n <= 20:
                        st.success("El SLA es de **9 días**.")
                    elif n >= 21:
                        st.warning("El SLA debe revisarse directamente con el modeler, ya que por la cantidad de markups podría tratarse como un proyecto.")
                    else:
                        st.error("Por favor ingresa un número mayor a 0.")

    # -------------------- PROCESAMIENTO DE TEXTO --------------------
    st.markdown("---")
    st.subheader("Procesamiento de texto")
    texto = st.text_area("Escribe el texto a procesar (máx. 1000 caracteres):", max_chars=1000, key="texto_original")
    st.text_area("Texto procesado (en mayúsculas):", value=texto.upper(), height=150, disabled=True, key="texto_procesado")

    # -------------------- RESUMEN --------------------
    if st.button("Mostrar resumen"):
        st.markdown("### Resumen de la consulta")
        st.write(f"**Usuario BSC:** {usuario_bsc}")
        st.write(f"**Tipo de consulta:** {seleccion}")
        st.write(f"**Longitud del texto:** {len(texto)} caracteres")
