from abc import ABC, abstractmethod


class Content(ABC):
    @abstractmethod
    def generate(self) -> str:
        raise NotImplementedError
