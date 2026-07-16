from app.prompts.models.prompt_context import PromptContext


class ResearchPrompt:
    """
    Prompt template for research-oriented questions.
    """

    @staticmethod
    def build(context: PromptContext) -> str:

        return f"""
You are an expert AI research assistant.

Your task is to answer the user's question accurately,
clearly, and with well-structured explanations.

Question:
{context.question}
""".strip()