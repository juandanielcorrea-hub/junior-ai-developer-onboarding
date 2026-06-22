import chromadb
import os

chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="my_collection")

# 1. Definir la ruta donde están tus archivos .txt
carpeta_documentos = "semana2\\dia1\\documentos"

documentos = []
ids_documentos = []

# 2. Leer cada archivo .txt en la carpeta
for nombre_archivo in os.listdir(carpeta_documentos):
    if nombre_archivo.endswith(".txt"):
        ruta_completa = os.path.join(carpeta_documentos, nombre_archivo)
        
        # Abrir y leer el contenido del archivo
        with open(ruta_completa, "r", encoding="utf-8") as archivo:
            contenido_texto = archivo.read()
            
            # Agregar el contenido y un ID 
            documentos.append(contenido_texto)
            ids_documentos.append(nombre_archivo)

# 3. Hacer el upsert a ChromaDB con los datos reales
if documentos: # Verificamos que la lista no esté vacía
    collection.upsert(
        documents=documentos,
        ids=ids_documentos
    )
    print(f"Éxito: Se indexaron {len(documentos)} documentos en ChromaDB.")

# 4. Hacer una consulta de prueba
resultados = collection.query(
    query_texts=["¿Qué debo hacer para evitar hackeos en mi base de datos?"],
    n_results=2 
)

print(resultados)