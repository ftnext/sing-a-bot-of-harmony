from abc import ABC, abstractmethod


class BasePart(ABC):
    @abstractmethod
    def format(self) -> str:
        raise NotImplementedError
