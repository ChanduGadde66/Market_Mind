from fastapi import APIRouter

# MODELS
from models.chat_model import ChatRequest
from models.business_models import (
    CampaignRequest,
    SalesPitchRequest,
    MarketAnalysisRequest,
    LeadScoreRequest
)

# SERVICES
from services.business_ai import (
    generate_campaign,
    generate_sales_pitch,
    market_analysis,
    lead_score
)

from services.agent_ai import smart_agent
from ai_engine.orchestrator import chat_with_ai

router = APIRouter()


@router.post("/chat")
def chat(req: ChatRequest):

    reply = chat_with_ai(req.message)

    return {"reply": reply}


@router.post("/agent")
def agent(req: ChatRequest):

    reply = smart_agent(req.message)

    return {"reply": reply}

@router.post("/campaign")
def campaign(req: CampaignRequest):

    result = generate_campaign(
        req.product,
        req.audience,
        req.goal
    )

    return {"campaign": result}


@router.post("/sales-pitch")
def sales_pitch(req: SalesPitchRequest):

    result = generate_sales_pitch(
        req.product,
        req.customer_type
    )

    return {"pitch": result}


@router.post("/market-analysis")
def analysis(req: MarketAnalysisRequest):

    result = market_analysis(req.topic)

    return {"analysis": result}

@router.post("/lead-score")
def lead(req: LeadScoreRequest):

    result = lead_score(
        req.engagement,
        req.activity,
        req.fit
    )

    return result