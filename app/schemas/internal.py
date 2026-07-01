from pydantic import BaseModel, Field

class Experience(BaseModel):
    company: str
    role: str
    description: str

class ExtractedCV(BaseModel):
    full_name: str
    skills: list[str]
    experiences: list[Experience]
    education: list[str]

class MatchAnalysis(BaseModel):
    score: int = Field(ge=0, le=100)
    matched_skills: list[str]
    missing_skills: list[str]
    reason: str

class TailoredExperience(BaseModel):
    original_text: str
    tailored_text: str

