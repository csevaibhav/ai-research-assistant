from app.llm.llm_manager import LLMManager
from app.services.chat_service import ChatService
from tests.fakes.fake_provider import FakeProvider


def test_chat_service_returns_fake_response():

    provider = FakeProvider()

    llm = LLMManager(provider)

    service = ChatService(llm)

    response = service.ask("What is AI?")

    assert response == "This is a fake AI response."