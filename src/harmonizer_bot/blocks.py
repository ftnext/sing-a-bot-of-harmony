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
