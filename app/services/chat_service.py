from app.core.logger import logger
from app.llm.llm_manager import LLMManager


class ChatService:

    def __init__(self):

        self.llm = LLMManager()

    def ask(self, question: str):

        logger.info(
            "Question received: %s",
            question
        )

        answer = self.llm.generate(question)

        logger.info(
            "Response generated successfully"
        )

        return answer


chat_service = ChatService()