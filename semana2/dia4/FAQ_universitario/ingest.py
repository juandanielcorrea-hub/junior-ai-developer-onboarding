import chromadb
from sentence_transformers import SentenceTransformer

# Modelo para embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="faq_universidad"
)

# Leer documento
with open("datos/faq.txt", "r", encoding="utf-8") as f:
    contenido = f.read()

# Chunking sencillo
chunks = [
    chunk.strip()
    for chunk in contenido.split("\n\n")
    if chunk.strip()
]

# Insertar documentos
for i, chunk in enumerate(chunks):

    embedding = model.encode(chunk).tolist()

    collection.add(
        ids=[str(i)],
        documents=[chunk],
        embeddings=[embedding]
    )

print(f"Se almacenaron {len(chunks)} documentos.")