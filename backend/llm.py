import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"


def generate_answer(question, context):

    prompt = f"""
You are a document question-answering assistant.

Your job is to answer the user's question using ONLY the document context provided below.

IMPORTANT RULES:
1. Use the Context as the source of truth.
2. Do not use your own general knowledge.
3. Do not invent or assume information.
4. If the answer is clearly present in the Context, answer it directly.
5. If the answer is NOT present in the Context, respond exactly:
"I couldn't find the answer in the uploaded document."
6. Keep the answer clear and concise.
7. You may combine information from multiple context sections if necessary.

DOCUMENT CONTEXT:
-----------------
{context}
-----------------

USER QUESTION:
{question}

ANSWER:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0
            }
        }
    )

    response.raise_for_status()

    return response.json()["response"].strip()