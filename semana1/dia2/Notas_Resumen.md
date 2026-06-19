1. RAG (Retrieval-Augmented Generation)
Imagina que un LLM (como ChatGPT) es un estudiante brillante que se memorizó toda la biblioteca hace dos años, pero no tiene internet. Si le preguntas algo muy nuevo o un documento privado tuyo, va a alucinar (inventar).

¿Qué hace RAG? Le da a ese estudiante un buscador interno. Primero busca (Retrieve) la información exacta en tus PDFs/Bases de datos, y luego se la pasa al modelo para que genere (Generate) una respuesta basada en esos datos reales.

2. Chunking Strategies (Estrategias de fragmentación)
No puedes meter un PDF de 500 páginas de golpe al LLM porque explota su memoria (Context Window). Tienes que picarlo en pedacitos (chunks). El problema es cómo lo picas para no perder el contexto. Hoy implementaste dos formas de hacerlo:

Estrategia A: Sentence Window Retrieval (Ventana de Oraciones)

¿Cómo funciona? Pica el documento oración por oración.

La magia: Cuando el usuario hace una pregunta, el sistema encuentra la oración exacta que tiene el dato. Pero, en lugar de pasarle solo esa oración pelada al LLM (que podría carecer de sentido por sí sola), le pasa una "ventana": las 3 oraciones de antes, la oración clave, y las 3 de después.

¿Para qué sirve? Para preguntas de datos muy específicos (ej. "¿En qué año se fundó la empresa?") donde necesitas precisión quirúrgica pero con un poco de contexto alrededor para que el LLM redacte bien.

Estrategia B: Auto-merging Retrieval (Chunking Jerárquico)

¿Cómo funciona? Crea un "árbol" genealógico de texto. Corta el texto en pedazos de 2048 caracteres (Abuelo), esos los divide en 512 (Padre), y esos en 128 (Hijo).

La magia: El sistema busca respuestas en los nodos pequeños (Hijos). Si detecta que varios "Hijos" del mismo "Padre" tienen información útil para responder la pregunta, automáticamente los fusiona y le manda al LLM el nodo "Padre" completo.

¿Para qué sirve? Para preguntas conceptuales amplias (ej. "Explícame cómo funciona el departamento de finanzas"), donde una sola oración no basta y necesitas darle al LLM párrafos enteros o páginas completas.

3. Similarity Search (Búsqueda de Similitud)
Antes usábamos Ctrl + F para buscar palabras exactas. Hoy usamos "Búsqueda Semántica".

Embeddings: Tu código agarró el texto y lo convirtió en una lista gigante de números (vectores) usando el modelo BAAI/bge-small-en-v1.5. Esos números representan el "significado" del texto.

La búsqueda: Cuando el usuario hace una pregunta, la pregunta también se convierte en números. El sistema busca (usando matemáticas) qué pedazos de texto apuntan en la misma dirección que la pregunta. Así, si buscas "perro", el sistema también te trae resultados que dicen "cachorro" o "canino", aunque no compartan letras.

4. Reranking (Reordenamiento)
La búsqueda de similitud es rapidísima, pero a veces es un poco torpe y te puede traer resultados mediocres junto con los buenos.

El filtro final: El Reranker (en tu código usaste BAAI/bge-reranker-base) es un segundo modelo de IA mucho más minucioso.

¿Cómo funciona? Si la búsqueda rápida trae el Top 10 de posibles respuestas, el Reranker se sienta a leer detenidamente esos 10 fragmentos, los califica contra la pregunta del usuario, y te escupe el Top 2 absoluto y definitivo. Esto asegura que el LLM reciba pura información premium, reduciendo drásticamente las alucinaciones.