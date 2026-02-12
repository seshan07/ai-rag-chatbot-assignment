from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import RAGPipeline

app = FastAPI(
    title="AI Developer Assignment - RAG Chatbot",
    description="RAG-based chatbot using FastAPI and HuggingFace",
    version="1.0"
)

rag = RAGPipeline("data/Platforms_Supported.pdf")

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_question(request: QueryRequest):
    answer = rag.ask(request.question)
    return {"answer": answer}