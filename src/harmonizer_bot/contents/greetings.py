from datetime import date

from .base import Content


class MorningGreetingContent(Content):
    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        raise NotImplementedError
