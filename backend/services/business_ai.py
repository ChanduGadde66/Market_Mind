from ai_engine.orchestrator import chat_with_ai
from ai_engine.lead_scoring_engine import calculate_lead_score

def generate_campaign(p,a,g):
    return chat_with_ai(f"Create campaign for {p}, audience {a}, goal {g}")

def generate_sales_pitch(p,c):
    return chat_with_ai(f"Create sales pitch for {p} for {c}")

def market_analysis(t):
    return chat_with_ai(f"Market analysis about {t}")

def lead_score(e,a,f):
    score = calculate_lead_score(e,a,f)
    return {"score":score}