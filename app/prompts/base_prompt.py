from abc import ABC, abstractmethod


class BasePrompt(ABC):
    """
    Base class for every prompt.
    """

    @abstractmethod
    def build(self, question: str) -> str:
        pass