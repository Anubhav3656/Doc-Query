#  RAG System using Groq

## Overview

This project implements a **Multimodal Retrieval-Augmented Generation (RAG)** system capable of retrieving information from documents containing **text and generating accurate responses using a Large Language Model.

The system processes PDF documents, converts them into embeddings, stores them in a vector database, and retrieves the most relevant information to answer user queries.

## Features

* PDF document processing
* Vector embeddings for semantic search
* ChromaDB vector storage
* Groq-powered LLM response generation
* Streamlit-based user interface

## Tech Stack

* Python
* ChromaDB (Vector Database)
* Sentence Transformers (Embeddings)
* Groq API (LLM)
* Streamlit (Frontend)
* LangChain

## Architecture

1. Document ingestion
2. Text chunking
3. Embedding generation
4. Storage in vector database
5. Semantic retrieval
6. LLM-based answer generation

## Installation

Clone the repository:

git clone https://github.com/yourusername/multimodal-rag-groq.git

Install dependencies:

pip install -r requirements.txt

Add your Groq API key:

export GROQ_API_KEY=your_key_here

Run the application:

streamlit run app/streamlit_app.py

## Example Query

"What is the formula for Scaled Dot Product Attention?"

## Future Improvements

* Hybrid search
* Reranking
* Better multimodal reasoning
* Deployment on cloud platforms

## Author

Anubhav Chaudhary
