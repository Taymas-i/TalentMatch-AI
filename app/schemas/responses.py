"""
[ADIM 1.3]

API dışarıya ne dönecek? SSE stream'de hangi event'ler gönderilecek?

Örnek:
- StreamEvent(BaseModel): event_type: str (örn. "extracting", "analyzing", "tailoring", "done")
                           data: dict
- FinalResult(BaseModel): match_analysis: MatchAnalysis, tailored_cv: list[TailoredExperience]
"""
