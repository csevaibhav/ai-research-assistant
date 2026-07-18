from app.prompts.models.prompt_context import PromptContext


class CodeReviewPrompt:
    """
    Prompt template for code review tasks.
    """

    @staticmethod
    def build(context: PromptContext) -> str:

        return f"""
You are a senior software engineer.

Review the following code.

Provide:

- Strengths
- Weaknesses
- Improvements
- Best Practices

Code:

{context.question}
""".strip()