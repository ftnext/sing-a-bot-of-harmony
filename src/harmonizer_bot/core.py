import inspect
from datetime import date

from .contents.base import Content


class TextGenerator:
    def __init__(self) -> None:
        self.event_handlers = {}

    def register(self, event_name: str):
        def wrapped(func):
            self.event_handlers[event_name] = func
            return func

        return wrapped

    def generate(self, event_name: str, *, date_: date, **kwargs) -> str:
        handler = self.event_handlers[event_name]

        if inspect.isfunction(handler):
            return handler(date_, **kwargs)

        if inspect.isclass(handler) and issubclass(handler, Content):
            instance = handler(date_)
            return instance.generate()
