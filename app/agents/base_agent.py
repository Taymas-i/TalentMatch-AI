from groq import Groq
import instructor
from tenacity import retry, stop_after_attempt, wait_exponential
from app.core.config import settings

class BaseAgent:
    def __init__(self):
        self.client = instructor.from_groq(
            Groq(api_key=settings.groq_api_key),
            mode=instructor.Mode.JSON,
        )

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    def _call_llm(self, messages, response_model, model="openai/gpt-oss-120b"):
        return self.client.chat.completions.create(
            model=model,
            messages=messages,
            response_model=response_model,
        )