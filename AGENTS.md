# AGENTS.md · Aplicación de consultas Tec Ops

> Este fichero lo leen los agentes de programación (Copilot, Cursor, Codex, Gemini CLI y otros) antes de tocar vuestro código. Para Claude Code, cread un `CLAUDE.md` con una sola línea: `Sigue las instrucciones de AGENTS.md`. Para Gemini CLI, haced lo mismo con `GEMINI.md`.

## Qué es este proyecto

Portal web interactivo en Streamlit que centraliza consultas que tienen los ingenieros y clientes del departamento de Tec Ops, como por ejemplo modelers por área, tiempos de SLA para work orders, normativas COP, guías MUG, escalaciones, contactos on-call y un asistente virtual inteligente basado en IA.

## Cómo está hecho

- Python 3.12.
- Interfaz: Streamlit.
- IA: API de Gemini con el SDK `google-genai`. El modelo está en la constante `MODELO` de `app.py`.
- Archivos: `app.py` (toda la app), `requirements.txt` (dependencias) y `README.md`.
- La especificación completa está en https://github.com/alaurapineda/myappAImaster/blob/main/especificacion.md.

## Reglas

- La clave de la API va SIEMPRE en secretos (`st.secrets` en la ruta A, variable de entorno `GEMINI_API_KEY` en la ruta B). Nunca en el código, en el README ni en el chat.
- Cada llamada a la API va dentro de `try/except` y muestra un mensaje claro para el usuario.
- Textos de la interfaz en español, sencillos, pensados para alguien sin conocimientos técnicos.
- Cambios pequeños: uno por petición. Al terminar, explica qué has cambiado y por qué.
- Si añades una librería, añádela también a `requirements.txt` y dilo.
- No uses datos personales reales. Para probar, inventa ejemplos.

## Cómo comprobar que funciona

- Ruta A: `streamlit run app.py` en local (con `.streamlit/secrets.toml`), o haz push y revisa la app en Streamlit Cloud.
- Ruta B: `python app.py` con `GEMINI_API_KEY` exportada, o sube los archivos al Space.
- Casos de prueba (entrada → lo que esperamos):
1. Usuario BSC válido + consulta de modeler para Packaging en CTG → Muestra el nombre correcto del modeler (Ana Pineda).
2. SLA Work Orders con 25 documentos ingresados → Muestra la advertencia indicando que el cambio se clasifica como proyecto y debe coordinarse directamente con el modeler del área.
3. Pregunta fuera de tema al Chatbot de IA ("¿Cómo preparar una receta de cocina?") → El asistente responde con amabilidad corporativa ofreciendo ayuda dentro del ámbito del departamento Tec Ops.
## Qué no hacer
- No borres ni reescribas el README sin preguntar.
- No cambies el modelo ni la arquitectura sin preguntar.
- No hagas push ni despliegues sin que yo lo haya revisado.
