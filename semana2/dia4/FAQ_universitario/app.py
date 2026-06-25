import os

import chromadb
import google.generativeai as genai

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

llm = genai.GenerativeModel("gemini-2.5-flash")

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection("faq_universidad")


def buscar_contexto(pregunta):

    embedding = embedding_model.encode(
        pregunta
    ).tolist()

    resultados = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    documentos = resultados["documents"][0]

    return "\n\n".join(documentos)


def responder(pregunta):

    contexto = buscar_contexto(pregunta)

    prompt = f"""
Eres un asistente de una universidad.

Responde ÚNICAMENTE usando la información del contexto.

Si la respuesta no existe en el contexto responde:

"No encontré esa información en la base de conocimiento."

Contexto:

{contexto}

Pregunta:

{pregunta}
"""

    respuesta = llm.generate_content(prompt)

    return respuesta.text


def main():

    print("=" * 60)
    print("ASISTENTE FAQ UNIVERSIDAD")
    print("=" * 60)

    while True:

        pregunta = input("\nPregunta ('salir' para terminar): ")

        if pregunta.lower() == "salir":
            break

        respuesta = responder(pregunta)

        print("\nRespuesta:\n")
        print(respuesta)


if __name__ == "__main__":
    main()