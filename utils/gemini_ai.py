    try:
    import google.generativeai as genai  # type: ignore
except ImportError:
    genai = None

from config import GEMINI_API_KEY

# Configure Gemini
if genai is not None:
    genai.configure(api_key=GEMINI_API_KEY)

# Load Model
model = genai.GenerativeModel("gemini-1.5-flash") if genai is not None else None


def ask_gemini(question):
    """
    Generate an AI response using Gemini.
    """

    try:
        prompt = f"""
You are StudyMate AI, an intelligent academic assistant.

Rules:
- Answer clearly and accurately.
- Help students with programming, engineering, mathematics, science, and study planning.
- Use bullet points whenever useful.
- Keep answers concise unless detailed explanation is requested.
- If the question is unrelated to studies, answer politely.

Student Question:
{question}
"""

        if model is None:
            return "⚠️ Gemini is not available. Please install the Google Generative AI package."

        response = model.generate_content(prompt)

        if response and hasattr(response, "text"):
            return response.text

        return "⚠️ Sorry, I couldn't generate a response."

    except Exception as e:
        return f"❌ Gemini Error: {str(e)}"