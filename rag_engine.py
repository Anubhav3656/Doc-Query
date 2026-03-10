import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(query, retrieved_docs):

    context = "\n\n".join(retrieved_docs)

    prompt = f"""
Answer the question using the provided context.

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content