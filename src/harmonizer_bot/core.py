class TextGenerator:
    def __init__(self) -> None:
        self.event_handlers = {}

    def register(self, event_name: str):
        def wrapped(func):
            self.event_handlers[event_name] = func
            return func

        return wrapped
