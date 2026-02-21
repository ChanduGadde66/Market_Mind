import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.main_routes import router

app = FastAPI(
    title="MarketMind AI Backend",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)


@app.get("/")
def root():
    return {"message": "MarketMind Backend Running"}