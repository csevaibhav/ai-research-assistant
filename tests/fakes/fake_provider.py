from app.llm.base_provider import BaseLLMProvider


class FakeProvider(BaseLLMProvider):
    """
    Fake LLM provider used for unit testing.

    No external API calls are made.
    """

    def generate(self, prompt: str) -> str:
        return "This is a fake AI response."