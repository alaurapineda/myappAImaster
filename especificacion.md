# Especificación · [Nombre del producto]

> Una buena especificación es la que otro asistente de IA podría construir sin haceros preguntas. Rellenadla en la semana 2 y usadla como prompt principal con vuestro asistente o agente. De ella sale la ficha del **hito de la semana 2**.

## 1. Problema y usuario

- **Quién tiene el problema:** [persona o colectivo concreto]
- **Cómo lo resuelve hoy:** [a mano, con Excel, preguntando a alguien…]
- **Qué le molesta de cómo lo hace hoy:** [tiempo, errores, no encuentra la información…]
- **Qué parte resuelve la IA:** [y qué parte se queda fuera]

## 2. Qué hace el producto

Máximo tres funcionalidades. Si hay más, van al apartado 8.

1. [Funcionalidad 1]
2. [Funcionalidad 2]
3. [Funcionalidad 3]

## 3. Entradas y salidas

| El usuario da… | La app devuelve… | Ejemplo |
|---|---|---|
| [un texto, una pregunta, un archivo CSV…] | [un resumen, una respuesta, una categoría…] | [ejemplo concreto] |

## 4. La pieza de IA

- **Opción elegida:** [API de un LLM (Gemini) · modelo de Hugging Face · RAG sobre nuestros documentos]
- **Por qué:** [qué gana la app con esa opción]
- **Instrucciones para el modelo (system prompt):** [cómo debe comportarse, tono, qué no debe hacer]

## 5. Flujo del usuario

1. [El usuario entra y ve…]
2. [Escribe o sube…]
3. [Recibe…]

## 6. Restricciones

- Coste cero: capa gratuita de la API y despliegue gratuito (ruta A o B).
- La clave de la API va en secretos, nunca en el código.
- Sin datos personales reales.
- Lenguaje sencillo, para alguien sin conocimientos técnicos.
- [Otras restricciones de vuestro problema]

## 7. Criterios de aceptación

La app está bien si:

| Entrada | Resultado esperado |
|---|---|
| [caso normal] | [qué debe pasar] |
| [caso límite: texto vacío, pregunta fuera de tema…] | [qué debe pasar] |
| [error: se acaba la cuota] | [mensaje claro para el usuario] |

## 8. Fuera de alcance (por ahora)

- [Ideas que dejáis para después]

## 9. Despliegue

- **Ruta:** [A (Streamlit Community Cloud) · B (Hugging Face Spaces)]
- **Si trabajáis en equipo (opcional):** [qué app o funcionalidad construye cada persona]
