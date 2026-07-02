from app.agents.base_agent import BaseAgent
from app.schemas.internal import Experience, TailoredExperience
from app.core.prompt_templates.tailor_prompts import TAILOR_SYSTEM_PROMPT

class TailorAgent(BaseAgent):
    def tailor(self, experience: Experience, job_description: str) -> TailoredExperience:
        original_text = experience.description

        messages = [
            {"role": "system", "content": TAILOR_SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    f"Original experience description:\n{original_text}\n\n"
                    f"Target job description:\n{job_description}\n\n"
                    f"Rewrite this experience to be more relevant to the target job, "
                    f"following all the rules above."
                ),
            },
        ]
        result = self._call_llm(messages=messages, response_model=TailoredExperience)
        return result