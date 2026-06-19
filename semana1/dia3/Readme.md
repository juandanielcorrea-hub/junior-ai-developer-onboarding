# MongoDB CRUD - Gamer Lobby

Este script es una prueba de concepto para establecer la conexión entre Python y un clúster de MongoDB Atlas utilizando la librería `pymongo`.

## ¿Qué hace este código?
El script ejecuta las 4 operaciones fundamentales (CRUD) directamente en la nube:
* **Create (Crear):** Registra un nuevo jugador en la base de datos, asignándole automáticamente un `_id`.
* **Read (Leer):** Busca y recupera la información de un jugador específico usando su nickname.
* **Update (Actualizar):** Modifica un registro existente (ej. agregando nuevos títulos a su lista de juegos activos usando `$push`).
* **Delete (Eliminar):** Borra un jugador de la colección.

## Requisitos para ejecutarlo
1. Python 3.x instalado.
2. Instalar el driver de MongoDB: `pip install "pymongo[srv]"`
3. Una cadena de conexión válida de MongoDB Atlas con permisos de lectura y escritura.