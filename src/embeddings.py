import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# قراءة ملف .env
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

# إنشاء عميل Gemini
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def embed_text(text):
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values