from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os

from pydantic import BaseModel

from backend.vector_store import build_vector_store
from backend.retriever import search
from backend.llm import generate_answer


# Create FastAPI application
app = FastAPI(
    title="RAG AI Knowledge Assistant",
    description="AI-powered document question answering system",
    version="0.1.0"
)


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AskRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "RAG AI Knowledge Assistant API is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


DOCUMENTS_DIR = "data/documents"

os.makedirs(DOCUMENTS_DIR, exist_ok=True)

CURRENT_PDF_PATH = None


@app.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    global CURRENT_PDF_PATH

    file_path = os.path.join(DOCUMENTS_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    CURRENT_PDF_PATH = file_path

    return {
        "filename": file.filename,
        "message": "Document uploaded successfully",
        "path": file_path
    }


@app.post("/ask")
async def ask_question(request: AskRequest):

    if CURRENT_PDF_PATH is None:
        return {
            "question": request.question,
            "answer": "Please upload a PDF document first."
        }

    chunks, embeddings = build_vector_store(CURRENT_PDF_PATH)

    results = search(
        request.question,
        chunks,
        embeddings
    )

    context = "\n\n".join(
        result["chunk"] for result in results
    )

    answer = generate_answer(
        request.question,
        context
    )

    return {
        "question": request.question,
        "answer": answer
    }