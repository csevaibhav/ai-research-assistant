from app.prompts.prompt_manager import PromptManager


def test_prompt_manager_builds_research_prompt():

    prompt = PromptManager.build(
        prompt_name="research",
        question="What is Artificial Intelligence?"
    )

    assert "Artificial Intelligence" in prompt
    assert "research assistant" in prompt