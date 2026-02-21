def get_model_name(task="general"):
    """
    Central model router.
    Easy future upgrade for multi-model support.
    """

    if task == "fast":
        return "gemini-2.5-flash"

    return "gemini-2.5-flash"