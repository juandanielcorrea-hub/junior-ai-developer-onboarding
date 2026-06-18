Arquitectura General de un LLM

1. Recolección de datos

El entrenamiento de un LLM comienza con la recopilación de grandes volúmenes de información provenientes de libros, artículos, páginas web, documentación técnica y repositorios de código. Estos datos constituyen la base de conocimiento inicial del modelo.

2. Limpieza y preparación

Los datos recopilados son procesados para eliminar duplicados, contenido de baja calidad y formatos incorrectos. El objetivo es garantizar que el modelo aprenda a partir de información útil y consistente.

3. Tokenización

El texto no puede ser procesado directamente por una red neuronal. Por ello, se divide en unidades llamadas tokens, que pueden representar palabras completas, fragmentos de palabras o símbolos.

Ejemplo:

"Hola mundo"

→ ["Hola", " mundo"]

4. Embeddings

Cada token es transformado en un vector numérico que captura información semántica y contextual. Estos vectores permiten que el modelo identifique relaciones entre conceptos similares.

5. Pretraining

Durante esta fase el modelo aprende a predecir el siguiente token en una secuencia de texto. A través de miles de millones de ejemplos desarrolla comprensión estadística del lenguaje, gramática, patrones de razonamiento y conocimiento general.

6. Modelo Base

El resultado del pretraining es un Foundation Model o Modelo Base. Este modelo posee amplios conocimientos generales, pero aún no está optimizado para interactuar con usuarios de manera segura o útil.

7. Fine-Tuning

El modelo base se ajusta utilizando conjuntos de datos especializados para mejorar su desempeño en tareas concretas, como programación, atención al cliente, análisis de documentos o conversación.

8. RLHF

RLHF (Reinforcement Learning from Human Feedback) utiliza evaluaciones humanas para enseñar al modelo qué respuestas son preferibles. Este proceso mejora la utilidad, seguridad y calidad de las respuestas generadas.

9. Modelo Alineado

Después del fine-tuning y RLHF se obtiene un modelo alineado con las expectativas humanas. Ejemplos de esta etapa incluyen sistemas conversacionales como ChatGPT, Claude y Gemini.

10. Inferencia

La inferencia es la fase de uso real. El usuario proporciona un prompt, el texto es tokenizado y procesado por el Transformer, que genera nuevos tokens uno a uno hasta producir la respuesta final.