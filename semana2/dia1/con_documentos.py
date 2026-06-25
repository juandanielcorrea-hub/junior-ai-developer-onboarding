import chromadb
import os

chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="my_collection")

carpeta_documentos = "semana2\\dia1\\documentos"

documentos = []
ids_documentos = []

# Leer cada archivo .txt en la carpeta
for nombre_archivo in os.listdir(carpeta_documentos):
    if nombre_archivo.endswith(".txt"):
        ruta_completa = os.path.join(carpeta_documentos, nombre_archivo)
        
        # Abrir y leer el contenido del archivo
        with open(ruta_completa, "r", encoding="utf-8") as archivo:
            contenido_texto = archivo.read()
            
            # Agregar el contenido y un ID 
            documentos.append(contenido_texto)
            ids_documentos.append(nombre_archivo)

# Hacer el upsert a ChromaDB con los datos reales
if documentos: 
    collection.upsert(
        documents=documentos,
        ids=ids_documentos
    )
    print(f"Éxito: Se indexaron {len(documentos)} documentos en ChromaDB.")

# Hacer una consulta de prueba
resultados = collection.query(
    query_texts=["¿Qué debo hacer para evitar hackeos en mi base de datos?"],
    n_results=2 
)

print(resultados)