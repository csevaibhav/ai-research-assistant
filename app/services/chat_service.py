from app.core.config import settings
from app.core.logger import logger
from app.llm.gemini_client import client


class ChatService:

    def ask(self, question: str) -> str:

        logger.info("Question received: %s", question)

        logger.info("Using Gemini model: %s", settings.GEMINI_MODEL)

        response = client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=question,
        )

        logger.info("Response generated successfully")

        return response.text


chat_service = ChatService()