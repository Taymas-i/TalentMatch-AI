from pydantic import BaseModel

class AnalysisRequest(BaseModel):
    cv_text: str
    job_description: str
