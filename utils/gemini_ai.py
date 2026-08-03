import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini only if API key exists
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    model = None


def ask_gemini(question):
    """
    Generate an AI response using Gemini.
    """

    if model is None:
        return "⚠️ Gemini API Key is not configured."

    prompt = f"""
You are StudyMate AI, an intelligent academic assistant.

Rules:
- Answer clearly and accurately.
- Help students with programming, engineering, mathematics, science and study planning.
- Use bullet points where useful.
- Keep answers concise unless detailed explanation is requested.

Student Question:
{question}
"""

    try:
        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            return response.text

        return "⚠️ No response generated."

    except Exception as e:
        return f"❌ Gemini Error: {str(e)}"