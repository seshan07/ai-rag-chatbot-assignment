import os
import requests
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from app.rag import RAGPipeline
from app.offline_api_bot import OfflineAPIBot

load_dotenv()

app = FastAPI(
    title="AI Developer Assignment - RAG Chatbot",
    description="RAG-based chatbot using FastAPI, FAISS, and Ollama",
    version="1.0"
)

rag = RAGPipeline("data/Platforms_Supported.pdf")

offline_bot = OfflineAPIBot()


class QueryRequest(BaseModel):
    question: str


@app.post("/ask")
def ask_question(request: QueryRequest):
    try:
        answer = rag.ask(request.question)
        return {"answer": answer}
    except Exception as e:
        return {"answer": f"Error processing PDF question: {str(e)}"}



@app.post("/ask-api")
def ask_api(request: QueryRequest):

    try:
        # 🔹 Mock API Response (Based on Assignment Screenshot)
        mock_api_response = {
            "Measure Details for 10.200.2.192 - MS Manager": {
                "CPU utilization": {
                    "unit": "%",
                    "value": "45"
                },
                "Memory usage": {
                    "unit": "MB",
                    "value": "3072"
                },
                "Free space": {
                    "unit": "GB",
                    "value": "120"
                }
            }
        }

        context = str(mock_api_response)

        answer = offline_bot.ask(context, request.question)

        return {"answer": answer}

    except Exception as e:
        return {"answer": f"Error occurred: {str(e)}"}