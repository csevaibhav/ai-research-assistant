from app.llm.llm_manager import LLMManager
from app.llm.provider_factory import ProviderFactory
from app.services.chat_service import ChatService


def get_provider():
    """
    Returns the configured LLM provider.
    """
    return ProviderFactory.get_provider()


def get_llm_manager():
    """
    Creates an LLMManager using the configured provider.
    """
    provider = get_provider()
    return LLMManager(provider)


def get_chat_service():
    """
    Creates the ChatService with all required dependencies.
    """
    llm = get_llm_manager()
    return ChatService(llm)