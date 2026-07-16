from app.core.logger import logger
from app.llm.llm_manager import LLMManager
from app.prompts.prompt_manager import PromptManager


class ChatService:
    """
    Handles chat-related business logic.

    This service is independent of any specific LLM provider.
    It only depends on an LLMManager.
    """

    def __init__(self, llm: LLMManager):
        self.llm = llm

    def ask(self, question: str) -> str:

        logger.info("Question received: %s", question)

        prompt = PromptManager.build_research_prompt(question)

        logger.info("Prompt created successfully.")

        response = self.llm.generate(prompt)

        logger.info("Response generated successfully.")

        return response