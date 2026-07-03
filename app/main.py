from fastapi import FastAPI
from app.api.endpoints import analysis

app = FastAPI(title="TalentMatch AI V2")

app.include_router(analysis.router, prefix="/api", tags=["analysis"])


@app.get("/")
def root():
    return {"status": "TalentMatch AI V2 is running"}