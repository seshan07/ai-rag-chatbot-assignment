AI Developer Assignment

Task 1 – RAG Chatbot

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
- FAISS
- HuggingFace Transformers
- Sentence Transformers
- Postman

Project Structure:

ai_chatbot_assignment/
│
├── app/
│   ├── main.py
│   ├── rag.py
│   └── offline_api_bot.py
│
├── data/
│   └── Platforms_Supported.pdf
│
├── requirements.txt
├── README.md
└── Screen-Shots/


Task 2 – API Integration with Offline LLM

Overview:

Task 2 implements a chatbot that answers questions based on monitoring data received from an API.

As mentioned in the assignment email, the external API was not reachable. Therefore, a hardcoded mock API response was used to simulate the expected API output.

The chatbot processes this data using an offline LLM and exposes the functionality through a FastAPI endpoint.

Architecture:

User → FastAPI → Mock API Response → Offline LLM (Ollama Mistral) → Answer

- A mock monitoring API response is defined inside the /ask-api endpoint.
- The JSON response is converted into context.
- The offline LLM generates answers strictly based on this context.

Offline Model:

- Ollama
- Mistral model
- Fully local inference (no external API calls)

Endpoint:

POST /ask-api

Request:

{
  "question": "What is the free space for the server 10.200.2.192?"
}


Response:

{
  "answer": "The free space for the server 10.200.2.192 is 120 GB."
}