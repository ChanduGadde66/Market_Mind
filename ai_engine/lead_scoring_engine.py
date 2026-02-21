def calculate_lead_score(engagement, activity, fit):
    """
    Simple weighted lead score.
    """

    score = (
        engagement * 0.4 +
        activity * 0.3 +
        fit * 0.3
    )

    return round(score, 2)