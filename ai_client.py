
import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY) if API_KEY else None


def ask_gemini(prompt: str) -> str:
    """Send a prompt to Gemini with retries for temporary errors."""

    if client is None:
        return "Gemini API key is missing. Check your .env file."

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )
            return response.text or "No response was generated."

        except Exception as error:
            error_text = str(error)
            temporary_error = any(
                marker in error_text
                for marker in [
                    "503", "UNAVAILABLE", "10054",
                    "429", "RESOURCE_EXHAUSTED"
                ]
            )

            if temporary_error and attempt < 2:
                wait_seconds = 2 * (attempt + 1)
                print(
                    f"Temporary Gemini error. "
                    f"Retrying in {wait_seconds} seconds..."
                )
                time.sleep(wait_seconds)
                continue

            print(f"Gemini API error: {error}")
            return (
                "Gemini is temporarily unavailable or the request failed. "
                "Please try again later. Check the VS Code terminal."
            )

    return "Gemini is temporarily unavailable. Please try again later."