import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Flask Secret Key
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "studymate_secret_key"
)

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")