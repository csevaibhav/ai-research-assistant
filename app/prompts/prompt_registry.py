from app.prompts.templates.research_prompt import ResearchPrompt


class PromptRegistry:
    """
    Central registry for all available prompt templates.
    """

    _PROMPTS = {
        "research": ResearchPrompt,
    }

    @classmethod
    def get_prompt(cls, prompt_name: str):
        if prompt_name not in cls._PROMPTS:
            raise ValueError(f"Unknown prompt: {prompt_name}")

        return cls._PROMPTS[prompt_name]