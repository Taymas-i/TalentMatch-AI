from app.agents.base_agent import BaseAgent
from app.schemas.internal import ExtractedCV
from app.core.prompt_templates.extractor_prompts import EXTRACTOR_SYSTEM_PROMPT

class ExtractorAgent(BaseAgent):
    def extract(self, cv_text: str) -> ExtractedCV:
        messages = [
            {"role": "system", "content": EXTRACTOR_SYSTEM_PROMPT},
            {"role": "user", "content": f"Bu CV'yi analiz et: {cv_text}"},
        ]
        return self._call_llm(messages=messages, response_model=ExtractedCV)
