from unittest import TestCase
from unittest.mock import MagicMock

from harmonizer_bot.blocks import BasePart, Sentence, Sentences


class SentenceTestCase(TestCase):
    def test_init(self):
        sentence = MagicMock(spec=str)

        actual = Sentence(sentence)

        self.assertIsInstance(actual, BasePart)

    def test_format(self):
        sentence = Sentence("これはテストのための文です。")

        actual = sentence.format()

        expected = "これはテストのための文です。\n"
        self.assertEqual(actual, expected)


class SentencesTestCase(TestCase):
    def test_init(self):
        sentence1 = MagicMock(spec=Sentence)
        sentence2 = MagicMock(spec=Sentence)

        actual = Sentences(sentence1, sentence2)

        self.assertIsInstance(actual, BasePart)
