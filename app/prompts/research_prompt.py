from app.prompts.base_prompt import BasePrompt
from app.prompts.system_prompt import SystemPrompt


class ResearchPrompt(BasePrompt):

    def build(self, question: str) -> str:

        return f"""
{SystemPrompt.TEXT}

User Question:

{question}

Provide a detailed answer.
"""