## 🚀 Live Demo

**Frontend:**  
https://rag-ai-knowledge-assistant-frontend.onrender.com

**Backend API:**  
https://rag-ai-knowledge-assistant-98t0.onrender.com

# 🤖 RAG AI Knowledge Assistant

![RAG AI Knowledge Assistant](docs/rag-ai-assistant.png)

A Generative AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their content.

The system extracts text from uploaded documents, splits it into overlapping chunks, retrieves relevant information using TF-IDF and cosine similarity, and generates context-aware answers using a Groq-hosted Large Language Model (LLM).

## 🚀 Features

- 📄 Upload PDF documents
- 🔍 Document retrieval using TF-IDF
- 📊 Cosine similarity-based search
- 🧩 Overlapping text chunking
- 🤖 Retrieval-Augmented Generation (RAG)
- 💬 Ask questions about uploaded documents
- 🎯 Context-grounded LLM responses
- ⚡ FastAPI backend
- 🌐 Web-based frontend
- ☁️ Deployed on Render
- 🔐 Groq API integration using environment variables
- 🛡️ Graceful handling of PDFs without readable text

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn

### AI / RAG

- Retrieval-Augmented Generation (RAG)
- Text chunking
- TF-IDF vectorization
- Cosine similarity
- In-memory vector retrieval
- Groq API
- GPT-OSS-20B

### Frontend
- HTML
- CSS
- JavaScript

## 🏗️ Architecture

```text
User
  |
  v
Web Interface
  |
  v
FastAPI Backend
  |
  +----------------------+
  |                      |
  v                      v
PDF Processing       User Question
  |                      |
  v                      v
Text Chunking       TF-IDF Vectorization
  |                      |
  v                      |
TF-IDF Vectors <---------+
  |
  v
Cosine Similarity
  |
  v
Relevant Context
  |
  v
Groq GPT-OSS-20B
  |
  v
Generated Answer

    ## 🔄 How It Works

## 🔄 How It Works

PDF Document
↓
Text Extraction
↓
Text Chunking
↓
TF-IDF Vectorization
↓
User Question
↓
Question Vectorization
↓
Cosine Similarity
↓
Relevant Chunks
↓
Context Construction
↓
Groq GPT-OSS-20B
↓
Generated Answer

## ☁️ Deployment

The application is deployed as two separate services on Render.

### Frontend
Render Static Site

### Backend
FastAPI Web Service

The frontend communicates with the backend through HTTPS API requests.

## 🔗 Project Links

**Live Demo:**  
https://rag-ai-knowledge-assistant-frontend.onrender.com

**GitHub:**  
https://github.com/MohammedApsal/rag-ai-knowledge-assistant