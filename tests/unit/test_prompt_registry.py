from app.prompts.prompt_registry import PromptRegistry


def test_registry_returns_research_prompt():

    prompt = PromptRegistry.get_prompt("research")

    assert prompt.__name__ == "ResearchPrompt"


def test_registry_returns_summary_prompt():

    prompt = PromptRegistry.get_prompt("summary")

    assert prompt.__name__ == "SummaryPrompt"


def test_registry_returns_qa_prompt():

    prompt = PromptRegistry.get_prompt("qa")

    assert prompt.__name__ == "QAPrompt"


def test_registry_returns_code_review_prompt():

    prompt = PromptRegistry.get_prompt("code_review")

    assert prompt.__name__ == "CodeReviewPrompt"