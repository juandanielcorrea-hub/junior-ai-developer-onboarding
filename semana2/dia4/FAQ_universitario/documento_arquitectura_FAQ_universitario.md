Documento de Arquitectura

Componentes

1. requirements.txt

Indica qué librerías necesita Python para que el programa funcione. Incluye ChromaDB para almacenar vectores, Sentence Transformers para generar embeddings, Google Generative AI para comunicarse con Gemini y python-dotenv para cargar variables de entorno.

2. .env

Almacena variables de entorno, como la API Key de Gemini. 

3. faq.txt

Funciona como la base de conocimiento del sistema RAG

4. ingest.py

Este programa prepara toda la información antes de que el chatbot pueda responder preguntas. Lee el archivo de preguntas frecuentes, lo divide en pequeños bloques, los convierte en representaciones numéricas y los guarda en una base de datos especializada para que luego puedan encontrarse rápidamente.

5. app.py

Este es el programa principal, recibe una pregunta, busca la información más relacionada dentro de la base de conocimiento y le pide a Gemini que redacte una respuesta utilizando únicamente esa información.


Flujo completo

`datos/faq.txt` -> `ingest.py` -> chunking -> embeddings con SentenceTransformer -> `ChromaDB` -> persistencia en `chroma_db/`

`Usuario` -> `app.py` -> `buscar_contexto()` -> embedding de la pregunta -> búsqueda en `ChromaDB` -> fragmentos relevantes -> `responder()` -> prompt con contexto -> `Gemini` -> respuesta final

Prompts

Eres un asistente de una universidad.
Responde ÚNICAMENTE usando la información del contexto.
Si la respuesta no existe en el contexto responde:
"No encontré esa información en la base de conocimiento."

Diagrama

`datos/faq.txt` -> `ingest.py` -> `SentenceTransformer` -> `ChromaDB` -> `chroma_db/`

`Usuario` -> `app.py` -> `buscar_contexto()` -> `ChromaDB` -> `responder()` -> `Gemini` -> `Respuesta`