from abc import ABC, abstractmethod


class BasePart(ABC):
    @abstractmethod
    def format(self) -> str:
        raise NotImplementedError


class Sentence(BasePart):
    def __init__(self, value: str, /) -> None:
        self.value = value

    def format(self):
        raise NotImplementedError
