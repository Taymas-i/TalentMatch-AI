from app.agents.base_agent import BaseAgent 
from app.schemas.internal import ExtractedCV, MatchAnalysis
from app.core.prompt_templates.analyzer_prompts import ANALYZER_SYSTEM_PROMPT

class AnalyzerAgent(BaseAgent):
    def analyze(self, extracted_cv: ExtractedCV, job_description: str) -> MatchAnalysis:
        cv_summary = extracted_cv.model_dump_json(indent=2)

        messages = [
            {"role": "system", "content": ANALYZER_SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    f"Candidate CV data:\n{cv_summary}\n\n"
                    f"Job Description:\n{job_description}"
                ),
            },
        ]
        return self._call_llm(messages=messages, response_model=MatchAnalysis)
