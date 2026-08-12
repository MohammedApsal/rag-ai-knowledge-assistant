# RAG AI Knowledge Assistant

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their content.

The system retrieves relevant information from uploaded documents and uses a local Large Language Model to generate answers based only on the retrieved context.

## 🚀 Features

- 📄 Upload PDF documents
- 🔍 Semantic document search
- 🧠 Retrieval-Augmented Generation (RAG)
- 💬 Ask questions about uploaded documents
- 🤖 Local LLM-powered responses using Ollama
- 🗃️ Vector database for document embeddings
- ⚡ FastAPI backend
- 🌐 Simple web-based frontend
- 🔒 Answers are generated from document context

## 🏗️ Architecture

```text
User
 │
 ▼
Web Interface
 │
 ▼
FastAPI Backend
 │
 ├── PDF Processing
 │
 ├── Text Chunking
 │
 ├── Embeddings
 │
 ▼
Vector Database
 │
 ▼
Relevant Context
 │
 ▼
Ollama LLM
 │
 ▼
Generated Answer