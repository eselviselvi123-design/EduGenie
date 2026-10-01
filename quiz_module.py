
import json
from ai_client import ask_gemini


def generate_quiz(topic: str, number_of_questions: int = 5) -> dict:
    """Generate a multiple-choice quiz using Gemini."""

    if not topic or not topic.strip():
        return {"error": "Please enter a topic."}

    number_of_questions = max(1, min(number_of_questions, 10))

    prompt = f"""
    Create {number_of_questions} multiple-choice questions about:
    {topic}

    Return ONLY valid JSON in this format:
    {{
      "questions": [
        {{
          "question": "Question text",
          "options": ["Option A", "Option B", "Option C", "Option D"],
          "answer": "Option A",
          "explanation": "Explain why this answer is correct"
        }}
      ]
    }}
    """

    result = ask_gemini(prompt)

    try:
        cleaned = result.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.split("\n", 1)[1]
            cleaned = cleaned.rsplit("```", 1)[0].strip()

        data = json.loads(cleaned)

        if not isinstance(data.get("questions"), list):
            return {"error": "The AI returned an invalid quiz format."}

        return data

    except (json.JSONDecodeError, AttributeError):
        return {"error": "Could not generate a valid quiz. Please try again."}