from fastapi import FastAPI, UploadFile, File, Response
from fastapi.middleware.cors import CORSMiddleware
import os

from pydantic import BaseModel

from backend.vector_store import build_vector_store
from backend.retriever import search
from backend.llm import generate_answer


# ==========================================
# Create FastAPI application
# ==========================================

app = FastAPI(
    title="RAG AI Knowledge Assistant",
    description="AI-powered document question answering system",
    version="1.0.0"
)


# ==========================================
# CORS configuration
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "https://rag-ai-knowledge-assistant-frontend.onrender.com",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================
# Request model
# ==========================================

class AskRequest(BaseModel):
    question: str


# ==========================================
# Root endpoint
# ==========================================

@app.get("/")
def root():
    return {
        "message": "RAG AI Knowledge Assistant API is running!"
    }


# ==========================================
# HEAD endpoint
# Prevent Render 405 warning
# ==========================================

@app.head("/")
def head_root():
    return Response(status_code=200)


# ==========================================
# Health check
# ==========================================

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# ==========================================
# Document storage
# ==========================================

DOCUMENTS_DIR = "data/documents"

os.makedirs(
    DOCUMENTS_DIR,
    exist_ok=True
)

CURRENT_PDF_PATH = None


# ==========================================
# PDF Upload
# ==========================================

@app.post("/documents/upload")
async def upload_document(
    file: UploadFile = File(...)
):
    global CURRENT_PDF_PATH

    # Check file type
    if not file.filename.lower().endswith(".pdf"):
        return {
            "filename": file.filename,
            "message": "Please upload a PDF file.",
        }

    # Create file path
    file_path = os.path.join(
        DOCUMENTS_DIR,
        file.filename
    )

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    # Store current PDF path
    CURRENT_PDF_PATH = file_path

    return {
        "filename": file.filename,
        "message": "Document uploaded successfully",
        "path": file_path
    }


# ==========================================
# Ask question
# ==========================================

@app.post("/ask")
async def ask_question(
    request: AskRequest
):

    # Check whether a PDF was uploaded
    if CURRENT_PDF_PATH is None:
        return {
            "question": request.question,
            "answer": "Please upload a PDF document first."
        }

    # ======================================
    # Build vector store
    # ======================================

    chunks, embeddings, vectorizer = build_vector_store(
        CURRENT_PDF_PATH
    )

    # ======================================
    # Handle PDFs with no readable text
    # ======================================

    if not chunks:
        return {
            "question": request.question,
            "answer": (
                "I couldn't extract readable text from this PDF. "
                "Please upload a text-based PDF."
            )
        }

    # ======================================
    # Search relevant chunks
    # ======================================

    results = search(
        request.question,
        chunks,
        embeddings,
        vectorizer
    )

    # ======================================
    # Combine retrieved chunks
    # ======================================

    context = "\n\n".join(
        result["chunk"]
        for result in results
    )

    # ======================================
    # Generate answer with Groq
    # ======================================

    answer = generate_answer(
        request.question,
        context
    )

    # ======================================
    # Return response
    # ======================================

    return {
        "question": request.question,
        "answer": answer
    }