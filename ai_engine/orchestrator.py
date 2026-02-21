import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def chat_with_ai(prompt):

    try:
        res = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return res.text
    except:
        return backup_ai(prompt)

# BACKUP MODEL (LOCAL FALLBACK)
def backup_ai(prompt):
    return "Backup AI response: " + prompt