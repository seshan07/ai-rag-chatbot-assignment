import requests


class OfflineAPIBot:

    def __init__(self):
        self.ollama_url = "http://localhost:11434/api/generate"

    def ask(self, context, question):

        prompt = f"""
You are an AI assistant.

Use ONLY the API data below to answer the question.
If the answer is not present, reply with: I don't know.

API Data:
{context}

Question:
{question}

Answer:
"""

        response = requests.post(
            self.ollama_url,
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]