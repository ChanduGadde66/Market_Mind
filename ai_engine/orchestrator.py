import os
from dotenv import load_dotenv

from ai_engine.memory_manager import add_message, get_history
from ai_engine.model_router import get_model_name
from ai_engine.output_formatter import format_output

load_dotenv()


# Try to use the official Google GenAI client if available and configured.
try:
    from google import genai

    _api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    try:
        if _api_key:
            client = genai.Client(api_key=_api_key)
        else:
            # Allow client to pick up default credentials if available
            client = genai.Client()
    except Exception as e:
        # Print error to process stdout for debugging; fall back to mock
        print("GenAI client initialization error:", e)
        client = None
except Exception as e:
    print("GenAI import error:", e)
    client = None


class _MockResponse:
    def __init__(self, text):
        self.text = text


class _MockClient:
    """Lightweight mock client used when GenAI isn't available.

    This keeps the backend runnable without external credentials by
    returning simple simulated replies based on the latest user message.
    """
    class models:
        @staticmethod
        def generate_content(model, contents):
            # Try to extract last user message from conversation history blob
            last_user = None
            try:
                # Look for the last line that starts with 'user:'
                for line in reversed(contents.splitlines()):
                    if line.lower().startswith("user:"):
                        last_user = line.split(":", 1)[1].strip()
                        break
            except Exception:
                last_user = None

            reply = f"Simulated reply: {last_user or 'Hello from MarketMind (no AI key)'}"
            return _MockResponse(reply)


if client is None:
    client = _MockClient()




def chat_with_ai(user_message):

    try:

        add_message("user", user_message)

        history = get_history()

        prompt = ""

        for msg in history:
            prompt += f"{msg['role']}: {msg['content']}\n"

        model_name = get_model_name()

        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )

        reply = format_output(response.text)

        add_message("assistant", reply)

        return reply

    except Exception:
        return "AI unavailable."



def detect_intent(message):

    msg = message.lower()

    if "campaign" in msg or "marketing" in msg:
        return "campaign"

    if "pitch" in msg or "sales" in msg:
        return "sales"

    if "market" in msg:
        return "analysis"

    if "lead" in msg:
        return "lead"

    return "chat"