
from ai_client import ask_gemini


def answer_question(question: str) -> str:
    """Answer a student's question using Gemini."""

    if not question or not question.strip():
        return "Please enter a question."

    prompt = f"""
    You are EduGenie, a helpful educational assistant.

    Answer this student's question:
    {question}

    Explain clearly in simple English.
    Give an example when useful.
    """

    return ask_gemini(prompt)