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
            5/30は #アイの歌声を聴かせて 公開🎬から214日目です。
            Blu-ray&DVDリリース📀そしてレンタル配信開始まで、今日を含めてあと58日です(7/27発売。現在予約期間)。

            今日も、元気で、頑張るぞっ、おーっ
            """
        ).rstrip()

        content = MorningGreetingContent(date(2022, 5, 30))
        actual = content.generate()

        self.assertEqual(actual, expected)
