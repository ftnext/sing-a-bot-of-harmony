from unittest import TestCase
from unittest.mock import MagicMock

from harmonizer_bot.blocks import BasePart, Sentence


class SentenceTestCase(TestCase):
    def test_init(self):
        sentence = MagicMock(spec=str)

        actual = Sentence(sentence)

        self.assertIsInstance(actual, BasePart)
