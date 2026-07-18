from app.prompts.templates.research_prompt import ResearchPrompt
from app.prompts.templates.summary_prompt import SummaryPrompt
from app.prompts.templates.qa_prompt import QAPrompt
from app.prompts.templates.code_review_prompt import CodeReviewPrompt


class PromptRegistry:
    """
    Central registry for all available prompt templates.
    """

    _PROMPTS = {
        "research": ResearchPrompt,
        "summary": SummaryPrompt,
        "qa": QAPrompt,
        "code_review": CodeReviewPrompt,
    }

    @classmethod
    def get_prompt(cls, prompt_name: str):

        if prompt_name not in cls._PROMPTS:
            raise ValueError(
                f"Unknown prompt: {prompt_name}"
            )

        return cls._PROMPTS[prompt_name]