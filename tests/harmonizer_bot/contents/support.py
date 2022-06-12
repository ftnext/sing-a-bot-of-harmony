from datetime import date
from textwrap import dedent
from unittest import TestCase
from unittest.mock import MagicMock

from harmonizer_bot.contents.base import Content


class ContentTesterMetaclass(type):
    """ref: https://github.com/python/cpython/blob/v3.10.5/Lib/test/test_argparse.py#L155-L266"""

    def __init__(cls, name, bases, bodydict):
        if name == "ContentTestCase":
            return

        class AddTests:
            def __init__(self, tester_cls):
                for test_func in [self.test_init, self.test_generate]:
                    test_name = test_func.__name__

                    def wrapper(self, test_func=test_func):
                        test_func(self)

                    setattr(tester_cls, test_name, wrapper)

            def test_init(self, tester):
                date_ = MagicMock(spec=date)

                actual = tester.target_class(date_)

                tester.assertIsInstance(actual, Content)
                tester.assertEqual(actual._date, date_)

            def test_generate(self, tester):
                expected = dedent(tester.generated_content).strip()

                content = tester.target_class(tester.generation_date)
                actual = content.generate()

                tester.assertEqual(actual, expected)

        AddTests(cls)


ContentTestCase = ContentTesterMetaclass("ContentTestCase", (TestCase,), {})
