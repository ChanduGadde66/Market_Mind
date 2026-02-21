from pydantic import BaseModel


class ChatRequest(BaseModel):
    """
    Chat request model
    used by /chat and /agent endpoints
    """
    message: str