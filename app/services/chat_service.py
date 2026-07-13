from app.core.logger import logger
from app.llm.provider_factory import ProviderFactory


class ChatService:

    def __init__(self):

        self.provider = ProviderFactory.get_provider()

    def ask(self, question: str):

        logger.info(
            "Question received: %s",
            question
        )

        answer = self.provider.generate(question)

        logger.info(
            "Response generated successfully"
        )

        return answer


chat_service = ChatService()