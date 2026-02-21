def format_output(text):
    """
    Clean and normalize AI output.
    """

    if not text:
        return "AI unavailable."

    return text.strip()