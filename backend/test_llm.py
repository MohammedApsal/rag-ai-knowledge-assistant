from llm import generate_answer


context = """
Retrieval-Augmented Generation (RAG) combines document retrieval
with a language model. A RAG system first searches a knowledge base
for relevant information and then provides that information to a
language model so it can generate a grounded answer.
"""

question = "What is RAG?"

answer = generate_answer(question, context)

print("\n===== AI ANSWER =====")
print(answer)