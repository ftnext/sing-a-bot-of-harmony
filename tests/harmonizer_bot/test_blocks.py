from textwrap import dedent
from unittest import TestCase
from unittest.mock import MagicMock

from harmonizer_bot.blocks import Balloon, BasePart, Sentence, Sentences


class SentenceTestCase(TestCase):
    def test_init(self):
        sentence = MagicMock(spec=str)

        actual = Sentence(sentence)

        self.assertIsInstance(actual, BasePart)

    def test_format(self):
        sentence = Sentence("これはテストのための文です。")

        actual = sentence.format()

        expected = "これはテストのための文です。"
        self.assertEqual(actual, expected)


class SentencesTestCase(TestCase):
    def test_init(self):
        sentence1 = MagicMock(spec=Sentence)
        sentence2 = MagicMock(spec=Sentence)

        actual = Sentences(sentence1, sentence2)

        self.assertIsInstance(actual, BasePart)

    def test_format(self):
        sentence1 = MagicMock(spec=Sentence)
        sentence2 = MagicMock(spec=Sentence)
        sentence1.format.return_value = "やっはろー、1文目"
        sentence2.format.return_value = "これは2文目。ごきげんよう"

        sentences = Sentences(sentence1, sentence2)
        actual = sentences.format()

        expected = "やっはろー、1文目\nこれは2文目。ごきげんよう"
        self.assertEqual(actual, expected)
        sentence1.format.assert_called_once_with()
        sentence2.format.assert_called_once_with()


class BalloonTestCase(TestCase):
    def test_init(self):
        sentence = MagicMock(spec=str)

        actual = Balloon(sentence)

        self.assertIsInstance(actual, BasePart)

    def test_format(self):
        balloon = Balloon("吹き出しの中の一文です！")

        actual = balloon.format()

        expected = dedent(
            """
            ／
             吹き出しの中の一文です！
            ＼
            """
        ).strip()
        self.assertEqual(actual, expected)
