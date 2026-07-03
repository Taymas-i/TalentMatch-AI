import json
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.core.orchestrator import run_pipeline
from app.services.rate_limit import check_and_increment
from app.core.exceptions import RateLimitError
from app.schemas.requests import AnalysisRequest

router = APIRouter()


@router.post("/analyze")
def analyze(request: AnalysisRequest, user_id: int = 1, db: Session = Depends(get_db)):
    try:
        check_and_increment(db, user_id)
    except RateLimitError as e:
        return {"error": str(e)}

    def event_stream():
        for event in run_pipeline(request.cv_text, request.job_description):
            yield f"data: {json.dumps(event.model_dump())}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")