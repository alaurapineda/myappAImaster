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
    /* Estilo para los mensajes de recomendación (info) en celeste claro con texto oscuro para legibilidad */
    div[data-testid="stNotification"] {
        background-color: #87CEFA !important; /* Celeste claro (LightSkyBlue) */
        color: #000000 !important;
    }
    div[data-testid="stNotification"] p {
        color: #000000 !important;
    }
    
    /* Estilos personalizados para el acordeón de preguntas FAQ */
    .faq-card {
        background-color: #FFFFFF !important;
        border-radius: 16px !important;
        padding: 18px 24px;
        margin-bottom: 16px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
        color: #1E293B !important;
    }
    .faq-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
    }
    .faq-left {
        display: flex;
        align-items: center;
        gap: 14px;
    }
    .faq-icon-circle {
        background-color: #1E40AF;
        color: #FFFFFF !important;
        border-radius: 50%;
        width: 32px;
        height: 32px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 16px;
        flex-shrink: 0;
    }
    .faq-title {
        color: #1E293B !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        margin: 0 !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .faq-trigger-btn button {
        background: none !important;
        border: none !important;
        color: #1E40AF !important;
        font-size: 22px !important;
        font-weight: bold !important;
        cursor: pointer;
        padding: 0 !important;
    }
    .faq-content {
        margin-top: 14px;
        padding-top: 14px;
        border-top: 1px solid #E2E8F0;
        color: #334155 !important;
        font-size: 14px !important;
        line-height: 1.6;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .faq-content p, .faq-content ul, .faq-content li {
        color: #334155 !important;
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
    opciones_con_placeholder = [
