from app.prompts.models.prompt_context import PromptContext


class QAPrompt:
    """
    Prompt template for question-answer tasks.
    """

    @staticmethod
    def build(context: PromptContext) -> str:

        return f"""
You are a knowledgeable AI assistant.

Answer the user's question accurately and briefly.

Question:
{context.question}
""".strip()