from pydantic import BaseModel, Field


class PromptContext(BaseModel):
    """
    Carries all information required to build a prompt.

    This object is intentionally designed to grow as the
    application evolves (history, RAG documents, tool outputs, etc.).
    """

    question: str = Field(..., description="User's question")

    history: list[str] = Field(
        default_factory=list,
        description="Conversation history",
    )

    documents: list[str] = Field(
        default_factory=list,
        description="Retrieved documents",
    )

    tool_results: list[str] = Field(
        default_factory=list,
        description="Outputs from executed tools",
    )