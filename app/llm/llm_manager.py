from app.core.logger import logger
from app.llm.provider_factory import ProviderFactory


class LLMManager:

    def __init__(self, provider):

        self.provider = provider

        logger.info(
            "Loaded provider: %s",
            self.provider.__class__.__name__
        )

    def generate(self, prompt: str) -> str:

        return self.provider.generate(prompt)