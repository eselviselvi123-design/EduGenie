
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key missing. Check your .env file.")
else:
    client = genai.Client(api_key=api_key)

    try:
        for model in client.models.list():
            name = model.name or ""
            actions = getattr(model, "supported_actions", None) or []

            if "generateContent" in actions:
                print(name)

    except Exception as error:
        print("Model check failed:", error)