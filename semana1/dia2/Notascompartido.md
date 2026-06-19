Celda 1

Aquí le decimos a Python que se prepare para leer archivos y conectarse a un modelo de lenguaje. Usamos SimpleDirectoryReader para escanear tu archivo ./ArquitecturaLLM.pdf y lo convertimos en un objeto de texto plano gigante que LlamaIndex pueda entender.
Definimos que el cerebro principal será el modelo gpt-3.5-turbo de OpenAI, configurado con una "temperatura" baja de 0.1 para que sus respuestas sean muy precisas y técnicas, sin inventar cosas.

Celda 2

Esta es la primera forma de procesar el PDF. Es como si se cortara el documento oración por oración.
Cuando le haces una pregunta al sistema, este busca la oración exacta que tiene la respuesta. Sin embargo, para que el LLM no reciba una oración suelta y sin sentido, esta estrategia jala las 3 oraciones anteriores y las 3 siguientes. Así, le entregas al modelo un contexto perfecto y fluido.

Celda 3

En lugar de oraciones, aquí se parte el PDF en bloques grandes de 2048 caracteres, luego esos en medianos de 512 y luego en pequeños de 128, creando una estructura de árbol.
El sistema busca coincidencias en los bloques más pequeños. Si detecta que muchos bloquecitos pequeños que pertenecen al mismo bloque padre tienen información útil, se fusionan automáticamente.

Celda 4
Se lanza la misma pregunta "What is the General Architecture of an LLM?" a ambos motores de búsqueda. El objetivo es ver qué estrategia de partición de datos le dio un mejor contexto al LLM para generar una respuesta más completa.



Pero hay un problema: El mensaje AuthenticationError: Error code: 401 del final.

El PDF se leyó, se fragmentó, se vectorizó y los motores de búsqueda funcionaron. Pero, en la ultima celda se mostro el error por falta de llave verdadera.