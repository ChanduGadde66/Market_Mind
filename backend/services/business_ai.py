from ai_engine.orchestrator import chat_with_ai
from ai_engine.lead_scoring_engine import calculate_lead_score



def generate_campaign(product, audience, goal):

    prompt = (
        f"Create a marketing campaign for {product}. "
        f"Target audience: {audience}. "
        f"Goal: {goal}."
    )

    return chat_with_ai(prompt)


def generate_sales_pitch(product, customer_type):

    prompt = (
        f"Create a professional sales pitch for {product} "
        f"targeted at {customer_type}."
    )

    return chat_with_ai(prompt)


def market_analysis(topic):

    prompt = f"Provide detailed market analysis for {topic}."

    return chat_with_ai(prompt)


def lead_score(engagement, activity, fit):

    score = calculate_lead_score(
        engagement,
        activity,
        fit
    )

    explanation = chat_with_ai(
        f"Explain lead score value {score} professionally."
    )

    return {
        "score": score,
        "explanation": explanation
    }