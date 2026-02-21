from ai_engine.orchestrator import (
    detect_intent,
    chat_with_ai
)

from services.business_ai import (
    generate_campaign,
    generate_sales_pitch,
    market_analysis,
    lead_score
)


def smart_agent(message):

    intent = detect_intent(message)

   
    if intent == "campaign":
        return generate_campaign(
            "AI Product",
            "general audience",
            "growth"
        )

    if intent == "sales":
        return generate_sales_pitch(
            "AI Product",
            "business clients"
        )

    if intent == "analysis":
        return market_analysis(message)

    if intent == "lead":
        result = lead_score(80, 70, 90)
        return result["explanation"]

    # Default chat
    return chat_with_ai(message)