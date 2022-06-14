from abc import ABC, abstractmethod


class BasePart(ABC):
    @abstractmethod
    def format(self) -> str:
        raise NotImplementedError


class Sentence:
    def __init__(self) -> None:
        raise NotImplementedError
