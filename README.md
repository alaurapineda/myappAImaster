**Aplicación de consultas Tec Ops**

**Enlace a la app:** [https://…streamlit.app o https://…hf.space](https://myappaimaster-7fbuupho2edbt8g9b87dzp.streamlit.app/)
**Autor/a:** Ana Laura Pineda Palma

## Pitch

El departamento de Tec Ops se enfrenta a la dispersión de información sobre sus servicios y canales de contacto, lo que retrasa la resolución de incidentes críticos. Esta aplicación web interactiva en Streamlit centraliza consultas generales que se han identificado como las más repetidas por sus clientes dentro de la empresa. La pieza de IA aporta un Asistente Virtual empático y especializado que resuelve dudas en tiempo real usando un contexto técnico interno optimizado. De las pruebas aprendí la importancia crítica de cuidar los contrastes visuales (CSS) y la robustez de los formularios; como siguientes pasos, planeo integrar bases de datos corporativas en tiempo real y automatizar las métricas del departamento.

## El problema

[Quién tiene el problema, cómo lo resuelve hoy y por qué merece la pena resolverlo. 3 o 4 frases.]

## Qué hace la app

[Qué puede hacer el usuario, paso a paso.]

## La pieza de IA

- **Qué usa:** [API de Gemini con el modelo …, un modelo de Hugging Face …, un RAG sobre …]
- **Por qué esa opción:** [una o dos frases]
- **Qué pasa si falla:** [cómo responde la app si se acaba la cuota o no hay conexión]

## Cómo la he construido

- **Herramientas:** [Gemini en Colab, Copilot, Cursor, Claude Code, Codex, Gemini CLI…]
- **Fichero de contexto del agente:** [enlace a vuestro AGENTS.md, CLAUDE.md o GEMINI.md]
- **Prompts clave:** [los 3 a 5 prompts que más han servido, copiados tal cual]
- **Qué delegué al agente y qué revisé a mano:** [ejemplos concretos]

## Prueba y mejora

| Quién la probó | Qué probó | Qué pasó | Qué cambié |
|---|---|---|---|
| [un compañero, o yo como usuario] | | | |

## Ejecutar en local (opcional)

```bash
pip install -r requirements.txt
# Ruta A: poned la clave en .streamlit/secrets.toml y ejecutad
streamlit run app.py
# Ruta B: exportad la clave y ejecutad
export GEMINI_API_KEY="…" && python app.py
```

## Capturas

[La app funcionando, la app ante un caso límite, un momento de vuestro trabajo con la IA y la prueba. Sin ninguna clave a la vista.]
