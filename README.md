**Aplicación de consultas Tec Ops**

**Enlace a la app:** [https://…streamlit.app o https://…hf.space](https://myappaimaster-7fbuupho2edbt8g9b87dzp.streamlit.app/)
**Autor/a:** Ana Laura Pineda Palma

## Pitch

El departamento de Tec Ops se enfrenta a la dispersión de información sobre sus servicios y canales de contacto, lo que retrasa la resolución de incidentes críticos. Esta aplicación web interactiva en Streamlit centraliza consultas generales que se han identificado como las más repetidas por sus clientes dentro de la empresa. La pieza de IA aporta un Asistente Virtual empático y especializado que resuelve dudas en tiempo real usando un contexto técnico interno optimizado. De las pruebas aprendí la importancia crítica de cuidar los contrastes visuales (CSS) y la robustez de los formularios; como siguientes pasos, planeo integrar bases de datos corporativas en tiempo real y automatizar las métricas del departamento.

## El problema

Los ingenieros de manufactura, calidad, producción o cualquier cliente operativo en la empresa necesitan consultar constantemente normativas, modelers según el área, políticas de cambios y tiempos de SLA del departamento de Tec Ops. Hoy en día, esto se resuelve buscando manualmente en correos antiguos, chats vía teams, llamadas o manuales extensos y poco dinámicos, lo que genera errores humanos, llamadas innecesarias y retrasos en la aprobación de cambios críticos que pueden detener líneas de producción.

## Qué hace la app

**Identificación y acceso:** El usuario ingresa su usuario BSC válido (con validación de al menos 5 caracteres alfanuméricos) para acceder al menú principal según el horario del día (saludo dinámico).
**Navegación de Consultas:** Permite seleccionar entre múltiples opciones ordenadas alfabéticamente (Consulta de modeler por área, SLA Work Orders, COP, Share Point Tec Ops, MUG, Escalaciones y On-call).
**Interacción y Feedback:** Cada sección ofrece datos precisos, calculadoras de SLA, enlaces directos y formularios de comentarios protegidos con botón de envío.
**Asistente de IA y Calificación:** Incluye un chat inteligente potenciado con Gemini para resolver preguntas frecuentes de manera cálida y un sistema interactivo de calificación por estrellas.

## La pieza de IA

**Qué usa:** API de Gemini con el modelo gemini-3.8-flash.
**Por qué esa opción:** Ofrece una velocidad excepcional de respuesta, bajo costo operativo, alta capacidad multitarea y excelente comprensión de instrucciones de rol basadas en contexto estructurado (Prompt Engineering).
**Qué pasa si falla:** Si se agota la cuota diaria (429 / RESOURCE_EXHAUSTED) o no hay conexión a internet, la aplicación captura la excepción y muestra un mensaje de advertencia amigable (st.warning / st.error) sin interrumpir la navegación general del usuario.

## Cómo la he construido

- **Herramientas:** Cursor, Google AI studios, Google Collab, Copilot y Streamlit.
- **Fichero de contexto del agente:** [enlace a vuestro AGENTS.md, CLAUDE.md o GEMINI.md]
- **Prompts clave:** 
1. Prompt para definir el diseño visual, tema oscuro y legibilidad perfecta
"Hola, estoy creando una aplicación en Streamlit para el departamento de Tec Ops con un estilo visual futurista Medtech. Necesito que por favor configures todo el CSS global para garantizar una legibilidad absoluta: los textos generales deben ser claros, pero los campos de texto, los menús desplegables, las opciones y los elementos dentro de los contenedores desplegables deben tener un contraste perfecto para que nunca se pierda la visibilidad. Asegúrate también de que los botones de envío dentro de los formularios tengan texto blanco visible y resalten bien."
2. Prompt para el comportamiento, tono y la base de datos interna del Chatbot
"Para la sección del Chatboot quiero que adoptes un rol extremadamente amable, cálido, respetuoso y profesional. Nunca debes dejar al usuario sin respuesta, si no sabes algo ofrecele amablemente contactar al manager Francisco Castro o a su respectivo Site Lead. Ademas asegurate de integrar todo la información que tiene el codigo dentro del contexto del asistente para que haga match perfecto y responda con precision.
3. Prompt para corregir formularios de feedback (MUG y Share Point) y el botón de regreso
"En la app tengo las opciones de feedback para MUG y Share Point donde los usuarios pueden escribir pero falta el botón de enviar. Por favor envuelve cada área de texto de esas secciones dentro de un formulario con su respectivo botón de envío para que funcione correctamente y muestre un mensaje de éxito al enviarlo. Asegurese de que en todas las subopciones siempre haya un botón para devolverse al menu principal."

- **Qué delegué al agente y qué revisé a mano:** Delegué la generación masiva del código CSS para el diseño Glassmorphism y la estructura condicional de Streamlit, revisé y ajusté manualmente los selectores CSS de los componentes nativos para asegurar la legibilidad del texto y corregí los textos específicos de los SLAs para proyectos complejos. Además, Gemini el codigo siempre me lo tiraba con Gemini-1.5, así que lo cambié a 3.8 flash.

## Prueba y mejora
**Quién la probó:** Yo como desarrolladora, mi esposo como usuario para revisar funcionalidad y wording.

**Qué probó:** La legibilidad de los textos en modo oscuro, el comportamiento de los formularios en las secciones de MUG y Share Point, y la visualización de los expanders de "Preguntas sugeridas". Y sobretodo el chatboot, fue lo que más probamos. 
**Qué pasó:** Inicialmente, el color de los textos dentro de los expanders colisionaba con el fondo oscuro y los botones de envío carecían de contraste adecuado. El chatboot no funcionaba porque estaba llamadando a Gemini-1.5. 
**Qué cambié:** Forcé mediante inyección CSS estilos explícitos para los elementos internos de los contenedores (stExpander y stFormSubmitButton), garantizando fondos blancos/claros con texto negro en entradas y textos blancos nítidos en títulos. Cambié Gemini-1.5, por Gemini-3.8-flash.

## Capturas
<img width="1440" height="900" alt="Captura de Pantalla 2026-11-01 a la(s) 17 34 15" src="https://github.com/user-attachments/assets/1e4cb767-668e-487e-b362-c2d9cde73843" /> <img width="1440" height="900" alt="Captura de Pantalla 2026-11-01 a la(s) 17 35 14" src="https://github.com/user-attachments/assets/a1eec67b-2253-4612-b99f-664eed097a85" /> <img width="1440" height="900" alt="Captura de Pantalla 2026-11-01 a la(s) 17 35 55" src="https://github.com/user-attachments/assets/3404ef7a-39c5-462b-883f-f013d030c699" />
<img width="1440" height="900" alt="Captura de Pantalla 2026-11-01 a la(s) 17 38 15" src="https://github.com/user-attachments/assets/cc8950fc-aea6-4120-b1f2-3a1380b92b71" />
