import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

load_dotenv()


class RAGPipeline:

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.retriever = None
        self.llm = None
        self.build_pipeline()

    def build_pipeline(self):
        print("Loading PDF...")
        loader = PyPDFLoader(self.pdf_path)
        documents = loader.load()

        print("Splitting text...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150
        )
        texts = text_splitter.split_documents(documents)

        print("Creating embeddings...")
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        vectorstore = FAISS.from_documents(texts, embeddings)

        self.retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

        print("Loading local LLM...")
        pipe = pipeline(
            "text2text-generation",  
            model="google/flan-t5-large",
            max_new_tokens=200,
            temperature=0
        )

        self.llm = HuggingFacePipeline(pipeline=pipe)

        print("RAG pipeline ready!")

    def ask(self, query):
        print(f"User Question: {query}")

        docs = self.retriever.invoke(query)

        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are a helpful assistant.

Use ONLY the information provided in the context below to answer the question.
If the answer is not found in the context, reply with: I don't know.

Context:
{context}

Question:
{query}

Answer:
"""

        response = self.llm.invoke(prompt)

        cleaned_response = response.strip()

        return cleaned_response