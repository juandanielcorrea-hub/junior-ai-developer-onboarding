# LangChain Functional Chain — S2-D2
Este repositorio contiene una cadena funcional construida con LangChain y Google Gemini.

## Arquitectura
El flujo de datos sigue el estándar estricto:
`Input` ➔ `PromptTemplate` ➔ `LLM (Gemini)` ➔ `JsonOutputParser (Estructurado)`

## Instalación
1. Instala las dependencias: `pip install -r requirements.txt`
2. Configura tu API Key en tu entorno o edita el script con tu token de Google AI Studio.
3. Ejecuta el archivo: `python chain_funcional.py`