class ResearchPrompt:
    """
    Research prompt template.
    """

    @staticmethod
    def build(question: str) -> str:

        return f"""
You are an expert research assistant.

Provide an accurate, detailed, and well-structured answer.

Question:

{question}
"""