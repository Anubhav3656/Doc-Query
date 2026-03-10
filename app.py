import streamlit as st
import os

from pdf_processor import process_pdf
from vectordb import add_documents, delete_document, search, stats
from rag_engine import generate_answer

if "history" not in st.session_state:
    st.session_state.history = []

UPLOAD_FOLDER = "uploads"


os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.set_page_config(page_title="Professional RAG", layout="wide")

st.title("📚 Doc Query")

# Sidebar
st.sidebar.header("Document Manager")

uploaded_files = st.sidebar.file_uploader(
    "Upload PDFs",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:

    for file in uploaded_files:

        path = os.path.join(UPLOAD_FOLDER, file.name)

        with open(path, "wb") as f:
            f.write(file.getbuffer())

        docs = process_pdf(path)

        add_documents(docs, file.name)

        st.sidebar.success(f"{file.name} indexed")

# File Manager
st.sidebar.subheader("Uploaded Files")

files = os.listdir(UPLOAD_FOLDER)

for f in files:

    col1, col2 = st.sidebar.columns([3,1])

    col1.write(f)

    if col2.button("❌", key=f):

        delete_document(f)

        os.remove(os.path.join(UPLOAD_FOLDER, f))

        st.sidebar.warning(f"{f} deleted")

# DB Stats
st.sidebar.subheader("Vector DB Stats")

st.sidebar.write("Total Chunks:", stats())


# Chat Interface
st.header("💬 Ask Questions")

query = st.text_input("Ask anything from documents")

if query:

    results = search(query)

    retrieved_docs = results["documents"][0]

    answer = generate_answer(query, retrieved_docs)

    st.session_state.history.append((query, answer))

    st.write("### Answer")
    st.write(answer)

    st.write("### Retrieved Chunks")

    for i, doc in enumerate(retrieved_docs):

        st.write(f"Chunk {i+1}")
        st.info(doc)

st.subheader("Chat History")

for q, a in st.session_state.history:
    st.write("**Q:**", q)
    st.write("**A:**", a)
    st.markdown("---")