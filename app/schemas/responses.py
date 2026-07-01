from pydantic import BaseModel
from typing import Literal
from app.schemas.internal import ExtractedCV, MatchAnalysis, TailoredExperience

class StreamEvent(BaseModel):
    event_type: Literal["extracting", "analyzing", "tailoring", "done", "error"]
    data: dict

class FinalResult(BaseModel):
    extracted_cv: ExtractedCV
    match_analysis: MatchAnalysis
    tailored_experiences: list[TailoredExperience]