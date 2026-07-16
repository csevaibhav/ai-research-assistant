from app.prompts.prompt_registry import PromptRegistry


class PromptManager:
    """
    Builds prompts using registered prompt templates.
    """

    @staticmethod
    def build(
        prompt_name: str,
        question: str,
    ) -> str:

        prompt_class = PromptRegistry.get_prompt(prompt_name)

        return prompt_class.build(question)