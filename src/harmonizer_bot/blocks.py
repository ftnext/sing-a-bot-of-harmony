from abc import ABC, abstractmethod
from dataclasses import dataclass


class BasePart(ABC):
    @abstractmethod
    def format(self) -> str:
        raise NotImplementedError


@dataclass(frozen=True)
class Sentence(BasePart):
    def __init__(self, value: str, /) -> None:
        object.__setattr__(self, "value", value)

    def format(self) -> str:
        return f"{self.value}\n"


@dataclass(frozen=True)
class Sentences(BasePart):
    def __init__(self, *args) -> None:
        object.__setattr__(self, "values", args)

    def format(self) -> str:
        return "".join(sentence.format() for sentence in self.values).rstrip()
