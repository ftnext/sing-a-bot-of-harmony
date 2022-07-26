from datetime import date
from textwrap import dedent
from unittest import TestCase
from unittest.mock import MagicMock

from harmonizer_bot.contents.base import Content
from harmonizer_bot.contents.greetings import MorningGreetingContent


class MorningGreetingContentTestCase(TestCase):
    def test_init(self):
        date_ = MagicMock(spec=date)

        actual = MorningGreetingContent(date_)

        self.assertIsInstance(actual, Content)
        self.assertEqual(actual._date, date_)

    def test_generate(self):
        expected = dedent(
            """\
            7/28は #アイの歌声を聴かせて 公開🎬から273日目、
            Blu-ray&DVDリリース📀&レンタル配信開始から2日目です。

            今日も、元気で、頑張るぞっ、おーっ
            """
        ).rstrip()

        content = MorningGreetingContent(date(2022, 7, 28))
        actual = content.generate()

        self.assertEqual(actual, expected)
