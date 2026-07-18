from app.prompts.models.prompt_context import PromptContext


class SummaryPrompt:
    """
    Prompt template for summarization tasks.
    """

    @staticmethod
    def build(context: PromptContext) -> str:

        return f"""
You are an expert summarization assistant.

Summarize the following content in a concise,
clear, and well-structured manner.

Content:
{context.question}
""".strip()