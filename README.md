AI Developer Assignment – RAG Chatbot

Project Overview:
This project implements a Retrieval-Augmented Generation (RAG) based chatbot using FastAPI and HuggingFace models.

The chatbot:
- Reads and processes a PDF file
- Creates vector embeddings using FAISS
- Retrieves relevant content based on user queries
- Generates answers using a local LLM
- Exposes functionality through a REST API endpoint
- Validated using Postman

Architecture:
User → FastAPI API → RAG Pipeline  
→ PDF Loader → Text Splitter → Embeddings → FAISS Vector Store  
→ Retriever → Local LLM → Response  

Tech Stack:
- Python
- FastAPI
- LangChain
- FAISS (Vector Database)
- HuggingFace Transformers
- Sentence Transformers (Embeddings)
- Postman (API Testing)

Project Structure:

ai_chatbot_assignment/
│
├── app/
│ ├── main.py
│ ├── rag.py
│
├── data/
│ └── Platforms_Supported.pdf
│
├── requirements.txt
├── README.md
└── screenshots/