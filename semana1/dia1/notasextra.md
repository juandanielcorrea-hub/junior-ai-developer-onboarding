Glosario S1-D1
LLM (Large Language Model)

Modelo de IA entrenado con enormes cantidades de texto para generar lenguaje natural.

Ejemplos:

ChatGPT
Claude
Gemini
Llama

Idea clave: predice el siguiente token.

NLP (Natural Language Processing)

Rama de la IA que permite a las computadoras comprender y generar lenguaje humano.

Ejemplos:

Traducción automática
Chatbots
Análisis de sentimiento
Resumen de texto
Transformer

Arquitectura de red neuronal que revolucionó el NLP en 2017.

Es la base de:

GPT
BERT
Llama
Claude
Gemini

Idea clave: utiliza Attention.

Attention

Mecanismo que permite al modelo identificar qué partes del texto son más importantes para entender el contexto.

Ejemplo:

Pedro habló con Juan porque él estaba preocupado.

Attention ayuda a decidir quién estaba preocupado.

Token

Unidad mínima de texto que procesa el modelo.

Ejemplos:

Hola mundo

Puede convertirse en:

["Hola", " mundo"]

o incluso fragmentos más pequeños.

Tokenización

Proceso de dividir texto en tokens.

Texto
↓
Tokens

Es el primer paso antes de que el modelo pueda procesar información.

Embedding

Representación numérica de un token o texto.

Ejemplo conceptual:

"perro"
↓
[0.12, -0.45, 0.89, ...]

Permite medir similitud semántica.

Vector

Lista de números utilizada para representar información.

Ejemplo:

[0.25, 0.77, -0.14]

Los embeddings son vectores.

Espacio Vectorial

Entorno matemático donde conceptos similares quedan cerca.

Ejemplo:

Perro  ←→ Gato
Perro  ←→ Mascota

Mientras que:

Perro ←→ Avión

están más alejados.

Contexto

Información que el modelo utiliza para generar una respuesta.

Ejemplo:

Usuario:
Mi perro se llama Max.

Usuario:
¿Cuántos años tiene?

El modelo necesita contexto para entender que "tiene" se refiere a Max.

Prompt

Instrucción enviada al modelo.

Ejemplo:

Explícame qué es MongoDB.

Todo comienza con un prompt.

Prompt Engineering

Diseño de prompts para obtener mejores respuestas.

Lo verás nuevamente en Salesforce Agentforce.

Corpus

Conjunto masivo de documentos usados para entrenamiento.

Ejemplos:

Libros
Artículos
Código fuente
Wikipedia
Dataset

Colección organizada de datos utilizada para entrenamiento o evaluación.

Pretraining

Entrenamiento masivo inicial del modelo.

Durante esta etapa aprende:

Gramática
Sintaxis
Conocimiento general
Relaciones semánticas
Foundation Model

Modelo resultante del pretraining.

Todavía no está especializado.

Ejemplo:

GPT Base

antes de convertirse en ChatGPT.

Fine-Tuning

Proceso de especialización de un modelo.

Ejemplos:

Programación
Medicina
Finanzas
Atención al cliente
Instrucción Tuning (Instruction Tuning)

Tipo de Fine-Tuning donde el modelo aprende a seguir instrucciones humanas.

Ejemplo:

Resume este texto.
Traduce al inglés.
RLHF

Reinforcement Learning from Human Feedback.

Proceso donde humanos califican respuestas y el modelo aprende cuáles son preferibles.

Objetivo:

Mayor utilidad
Mayor precisión
Mayor seguridad
Alineación (Alignment)

Proceso para que las respuestas del modelo coincidan con expectativas humanas.

RLHF es una técnica de alineación.

Inferencia

Momento en que el usuario utiliza el modelo.

Prompt
↓
Modelo
↓
Respuesta

No hay entrenamiento aquí.

Solo generación.

Parámetros

Valores internos aprendidos por el modelo durante el entrenamiento.

Cuando escuchas:

7B parámetros
70B parámetros
175B parámetros

se refiere al tamaño del modelo.

Ventana de Contexto (Context Window)

Cantidad máxima de información que el modelo puede considerar simultáneamente.

Ejemplo:

8k tokens
32k tokens
128k tokens
Generación Autoregresiva

Método mediante el cual el modelo genera una respuesta token por token.

Ejemplo:

Hola
↓
Hola, ¿
↓
Hola, ¿cómo
↓
Hola, ¿cómo estás?
RAG (Retrieval-Augmented Generation)

Técnica donde el modelo consulta información externa antes de responder.

Usuario
↓
Búsqueda
↓
Documentos
↓
LLM
↓
Respuesta

Importante: No forma parte del entrenamiento.

Forma parte de la inferencia.