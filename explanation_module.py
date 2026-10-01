
from ai_client import ask_gemini


def explain_topic(topic: str, level: str = "Beginner") -> str:
    """Explain a learning topic in a student-friendly way."""

    if not topic or not topic.strip():
        return "Please enter a topic to learn."

    prompt = f"""
    You are EduGenie, a friendly AI learning assistant.

    Explain this topic: {topic}
    Student level: {level}

    Instructions:
    1. Use simple English.
    2. Explain step by step.
    3. Include an example.
    4. Include a short summary at the end.
    """

    return ask_gemini(prompt)