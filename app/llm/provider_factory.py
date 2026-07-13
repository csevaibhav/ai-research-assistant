from app.core.config import settings
from app.llm.gemini_provider import GeminiProvider


class ProviderFactory:

    @staticmethod
    def get_provider():

        provider = settings.LLM_PROVIDER.lower()

        if provider == "gemini":
            return GeminiProvider()

        raise ValueError(
            f"Unsupported LLM Provider: {provider}"
        )