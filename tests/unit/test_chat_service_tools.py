from app.llm.llm_manager import LLMManager
from tests.fakes.fake_provider import FakeProvider
from app.services.chat_service import ChatService


def create_chat_service():
    provider = FakeProvider()
    llm_manager = LLMManager(provider)
    return ChatService(llm_manager)


def test_calculator_tool():

    chat = create_chat_service()

    result = chat.ask("calculate: 100 + 50")

    assert result == "150"


def test_datetime_tool():

    chat = create_chat_service()

    result = chat.ask("datetime")

    assert isinstance(result, str)
    assert len(result) > 0