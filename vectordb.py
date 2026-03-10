import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection("rag_docs")

embed_model = SentenceTransformer("all-MiniLM-L6-v2")


def add_documents(docs, filename):

    texts = [d["text"] for d in docs]

    embeddings = embed_model.encode(texts).tolist()

    ids = [f"{filename}_{i}" for i in range(len(texts))]

    metadatas = []

    for d in docs:
        m = d["metadata"]
        m["filename"] = filename
        metadatas.append(m)

    collection.add(
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )


def delete_document(filename):

    collection.delete(
        where={"filename": filename}
    )


def search(query):

    q_embed = embed_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[q_embed],
        n_results=5
    )

    return results


def stats():

    data = collection.get()

    return len(data["documents"])