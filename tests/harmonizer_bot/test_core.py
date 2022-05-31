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
