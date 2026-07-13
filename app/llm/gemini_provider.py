from google import genai

from app.core.config import settings
from app.core.logger import logger
from app.llm.base_provider import BaseLLMProvider


class GeminiProvider(BaseLLMProvider):

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate(self, prompt: str) -> str:

        logger.info("Generating response using Gemini")

        response = self.client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt,
        )

        return response.text