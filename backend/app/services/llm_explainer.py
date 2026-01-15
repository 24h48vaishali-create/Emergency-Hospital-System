import os

def enhance_text_with_llm(text: str) -> str:
    """
    Enhances explanation text using an LLM if API key is available.
    Falls back to original text if not configured.
    """

    api_key = os.getenv("LLM_API_KEY")

    # Fallback: no LLM configured
    if not api_key:
        return text

    # --- Placeholder for LLM call ---
    # This is intentionally minimal and safe.
    # You can later plug OpenAI / Gemini / Groq here.

    enhanced_text = (
        "Explanation (AI-assisted): "
        + text
    )

    return enhanced_text
