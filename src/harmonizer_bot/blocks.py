from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import ClassVar


class BasePart(ABC):
    @abstractmethod
    def format(self) -> str:
        raise NotImplementedError


@dataclass(frozen=True)
class Sentence(BasePart):
    def __init__(self, value: str, /) -> None:
        object.__setattr__(self, "value", value)

    def format(self) -> str:
        return f"{self.value}"


NEW_LINE = Sentence("")


@dataclass(frozen=True)
class Sentences(BasePart):
    def __init__(self, *args) -> None:
        object.__setattr__(self, "values", args)

    def format(self) -> str:
        return "\n".join(sentence.format() for sentence in self.values)


@dataclass(frozen=True)
class Balloon(BasePart):
    value: str
    _sentences: Sentences = field(init=False)
    START_BALLOON: ClassVar[str] = "／"
    END_BALLOON: ClassVar[str] = "＼"

    def __post_init__(self):
        sentences = Sentences(
            Sentence(self.START_BALLOON),
            Sentence(f" {self.value}"),
            Sentence(self.END_BALLOON),
        )
        object.__setattr__(self, "_sentences", sentences)

    def format(self) -> str:
        return self._sentences.format()
