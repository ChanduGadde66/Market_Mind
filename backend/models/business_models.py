from pydantic import BaseModel

class CampaignRequest(BaseModel):
    product:str
    audience:str
    goal:str

class SalesPitchRequest(BaseModel):
    product:str
    customer_type:str

class MarketAnalysisRequest(BaseModel):
    topic:str

class LeadScoreRequest(BaseModel):
    engagement:float
    activity:float
    fit:float