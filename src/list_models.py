import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

for model in client.models.list():
    print(model.name)