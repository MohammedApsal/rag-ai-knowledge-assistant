import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL_NAME = "openai/gpt-oss-20b"


def generate_answer(question, context):

    prompt = f"""
You are a document question-answering assistant.

Answer the user's question using ONLY the document context below.

Rules:
1. Use the context as the source of truth.
2. Do not use outside knowledge.
3. Do not invent information.
4. If the answer is not present in the context, say:
"I couldn't find the answer in the uploaded document."
5. Keep the answer clear and concise.

DOCUMENT CONTEXT:
-----------------
{context}
-----------------

USER QUESTION:
{question}

ANSWER:
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content