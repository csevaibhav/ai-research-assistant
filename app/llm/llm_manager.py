from app.core.logger import logger
from app.llm.provider_factory import ProviderFactory


class LLMManager:

    def __init__(self):

        self.provider = ProviderFactory.get_provider()

        logger.info(
            "Loaded provider: %s",
            self.provider.__class__.__name__
        )

    def generate(self, prompt: str) -> str:

        return self.provider.generate(prompt)