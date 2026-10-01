
from ai_client import ask_gemini


def summarize_content(content: str) -> str:
    """Summarize educational content using Gemini."""

    if not content or not content.strip():
        return "Please enter content to summarize."

    prompt = f"""
    Summarize the following educational content.

    Use:
    - A clear title
    - Important key points
    - Simple English
    - A short conclusion

    Content:
    {content}
    """

    return ask_gemini(prompt)