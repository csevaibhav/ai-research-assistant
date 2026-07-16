from app.prompts.research_prompt import ResearchPrompt


class PromptManager:

    @staticmethod
    def build_research_prompt(question: str) -> str:

        return ResearchPrompt().build(question)