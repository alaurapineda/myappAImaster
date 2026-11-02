# Especificación · **Aplicación de consultas Tec Ops**

> Una buena especificación es la que otro asistente de IA podría construir sin haceros preguntas. Rellenadla en la semana 2 y usadla como prompt principal con vuestro asistente o agente. De ella sale la ficha del **hito de la semana 2**.

## 1. Problema y usuario

- **Quién tiene el problema:** Tanto el departamente de TEC OPS al no contar con apoyo de AI para centralizar las consultas de sus clientes, como sus clientes: ingenieros de calidad, producción, manufactura, equipos, etc. 
- **Cómo lo resuelve hoy:** por llamadas, chats de teams, correos, en caso del cliente buscando información antigua. 
- **Qué le molesta de cómo lo hace hoy:** Tiempo consumido respondiendo preguntas repetitivas.
- **Qué parte resuelve la IA:** El Asistente Virtual Inteligente responde dudas genereales en tiempo real y contextualizadas; se queda fuera la automatización directa de la ejecución de cambios en los sistemas de producción, consulta de procedimientos técnicos. 

## 2. Qué hace el producto

Máximo tres funcionalidades. Si hay más, van al apartado 8.

1. Consulta centralizada de datos clave (Modelers por área y site, tiempos de SLA para work orders, normativas COP, guías MUG y contactos on-call).
2. Asistente Virtual conversacional con IA (Gemini 3.8-flash) especializado en soporte y normativas del departamento Tec Ops.
3. Canales interactivos de feedback corporativo (formularios con envío y sistema de calificación por estrellas).

## 3. Entradas y salidas

| El usuario da… | La app devuelve… | Ejemplo |
| Usuario BSC e indicador de área/site | El nombre del modeler o el tiempo de SLA correspondiente | Usuario BSC: otr12, Site: CTG, Área: Packaging $\rightarrow$ Ana Pineda |
| Una pregunta en lenguaje natural al Chatbot de IA | Una respuesta precisa y amable basada en el contexto corporativo | "¿Quiénes son los Site Leads?" $\rightarrow$ CTG: Eduardo Jenkins, CYL: Sergio Monge... |
| Texto de comentarios en MUG o Share Point | Mensaje de éxito de envío del formulario | Comentario escrito $\rightarrow$ "¡Muchas gracias! Tu comentario ha sido enviado exitosamente." |

## 4. La pieza de IA

- **Opción elegida:** API de un LLM (Gemini) utilizando el modelo gemini-3.8-flash mediante el SDK oficial google-genai.
- **Por qué:** Ofrece alta velocidad de respuesta, costo cero en capa gratuita y excelente comprensión de instrucciones de rol basadas en contexto estructurado corporativo.
- **Instrucciones para el modelo (system prompt):** Actuar como asistente virtual oficial del departamento de Tec Ops. Ser siempre extremadamente amable, respetuoso, cálido y educado. Saludar cordialmente y nunca dejar al usuario sin respuesta. Utilizar estrictamente la base de datos interna provista (modelers, sesiones COP, Site Leads, manager Francisco Castro y teléfonos On-call).
- 
## 5. Flujo del usuario

1.El usuario entra a la app, visualiza el saludo dinámico según la hora y escribe su usuario BSC corporativo.
2.Selecciona una opción del menú interactivo (ej. consulta de SLA, modelers, MUG, Escalaciones u On-call) o decide abrir el Chatbot de IA.
3. Recibe la información exacta buscada de forma inmediata, con opción de enviar feedback o interactuar con el asistente virtual.

## 6. Restricciones

- Coste cero: capa gratuita de la API y despliegue gratuito (ruta A o B).
- La clave de la API va en secretos, nunca en el código.
- Sin datos personales reales (uso de usuarios BSC ficticios y datos corporativos simulados).
- Lenguaje sencillo, para alguien sin conocimientos técnicos.
-Sin datos personales reales (uso de usuarios BSC ficticios y datos corporativos simulados).
-Legibilidad garantizada en modo oscuro (estética "MedTech" con contrastes estrictos en inputs y textos).

## 7. Criterios de aceptación

La app está bien si:

| Entrada | Resultado esperado |
|---|---|
| Caso normal: Usuario BSC válido + Selección de 5 documentos en SLA | Muestra el mensaje correcto indicando que el SLA es de 5 días. |
| Caso límite: Pregunta fuera de tema al chatbot ("¿Cómo hacer una receta?") | El asistente responde amablemente ofreciendo ayuda dentro del ámbito de Tec Ops. |
| Error: Se agota la cuota de la API de Gemini (429 / RESOURCE_EXHAUSTED) | La app captura la excepción y muestra un aviso claro para el usuario (st.warning) sin romper la interfaz. |

## 8. Fuera de alcance (por ahora)

Conexión directa y en tiempo real con bases de datos corporativas propietarias o ERPs (SAP/PLM).
Automatización de la aprobación automática de órdenes de trabajo en sistemas externos.

## 9. Despliegue
Ruta: Ruta A (Streamlit Community Cloud) mediante repositorio de GitHub.
