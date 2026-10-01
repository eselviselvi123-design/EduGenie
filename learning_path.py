
from ai_client import ask_gemini


def create_learning_path(goal: str, level: str = "Beginner") -> str:
    """Create a step-by-step learning plan using Gemini."""

    if not goal or not goal.strip():
        return "Please enter your learning goal."

    prompt = f"""
    Create a learning roadmap for a student.

    Learning goal: {goal}
    Current level: {level}

    Include:
    1. Learning stages in order
    2. Topics to study in each stage
    3. Small practice tasks
    4. A simple final project

    Use clear, simple English.
    """

    return ask_gemini(prompt)