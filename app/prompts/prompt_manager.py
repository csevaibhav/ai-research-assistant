from app.prompts.models.prompt_context import PromptContext
from app.prompts.prompt_registry import PromptRegistry


class PromptManager:
    """
    Responsible for constructing prompts using registered templates.
    """

    @staticmethod
    def build(
        prompt_name: str,
        question: str,
    ) -> str:

        context = PromptContext(
            question=question
        )

        prompt_class = PromptRegistry.get_prompt(prompt_name)

        return prompt_class.build(context)