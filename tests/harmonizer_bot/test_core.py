from datetime import date
from unittest import TestCase

from harmonizer_bot.core import TextGenerator


class TextGeneratorTestCase(TestCase):
    def test_register(self):
        sut = TextGenerator()

        @sut.register("func1")
        def f1():
            return 42

        @sut.register("function2")
        def f2(name):
            return f"Hello {name}"

        self.assertEqual(sut.event_handlers, {"func1": f1, "function2": f2})
        self.assertEqual(f1(), 42)
        self.assertEqual(f2("spam"), "Hello spam")

    def test_generate(self):
        sut = TextGenerator()

        @sut.register("morning")
        def f(date_: date, **kwargs) -> str:
            return f"おはよう {date_:%-m/%-d}"

        @sut.register("evening")
        def g(date_: date, *, name: str, **kwargs) -> str:
            return f"こんばんは、{name}さん {date_:%m/%d}"

        self.assertEqual(
            sut.generate("morning", date_=date(2022, 5, 31)), "おはよう 5/31"
        )
        self.assertEqual(
            sut.generate("evening", date_=date(2022, 6, 6), name="Shion"),
            "こんばんは、Shionさん 06/06",
        )
