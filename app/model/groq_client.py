# app/model/groq_client.py

import os
from groq import Groq
from dotenv import load_dotenv

# 🔥 LOAD ENV FIRST
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found. Check your .env file")

client = Groq(api_key=api_key)


def ask_groq(context, question):
    prompt = f"""
    You are a smart driving assistant.

    Context:
    {context}

    Question:
    {question}

    Answer briefly and clearly.
    """

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192"
    )

    return response.choices[0].message.content