chat_history = []

def add_message(role, content):
    """
    Store conversation history.
    """
    chat_history.append({
        "role": role,
        "content": content
    })


def get_history(limit=10):
    """
    Return last N messages.
    """
    return chat_history[-limit:]