from app.llm.llm_manager import LLMManager
from app.prompts.prompt_manager import PromptManager
from app.tools.tool_executor import ToolExecutor


class ChatService:
    """
    Handles chat requests and routes them to either the LLM
    or the appropriate tool.
    """

    def __init__(self, llm_manager: LLMManager):
        self.llm_manager = llm_manager
        self.prompt_manager = PromptManager()

    def ask(self, question: str) -> str:
        """
        Process a user question.
        """

        question = question.strip()

        # Calculator Tool
        if question.lower().startswith("calculate:"):
            expression = question.split(":", 1)[1].strip()

            return ToolExecutor.execute(
                "calculator",
                expression=expression,
            )

        # DateTime Tool
        if question.lower() == "datetime":
            return ToolExecutor.execute("datetime")

        # Default: Use LLM
        prompt = self.prompt_manager.build(
            prompt_name="research",
            question=question,
        )

        return self.llm_manager.generate(prompt)