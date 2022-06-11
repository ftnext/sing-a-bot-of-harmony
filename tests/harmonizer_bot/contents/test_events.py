from datetime import date
from textwrap import dedent
from unittest import TestCase
from unittest.mock import MagicMock

from harmonizer_bot.contents.base import Content
from harmonizer_bot.contents.events import PlayAllTogetherContent


class PlayAllTogetherContentTestCase(TestCase):
    def test_init(self):
        date_ = MagicMock(spec=date)

        actual = PlayAllTogetherContent(date_)

        self.assertIsInstance(actual, Content)
        self.assertEqual(actual._date, date_)

    def test_generate(self):
        expected = dedent(
            """\
            #アイの歌声を聴かせて 期間限定配信🎥は今日を含めてあと13日です(6/10まで)。

            📣たたーん！ 6/10(金)20:30〜 Twitterスペースで #みんなでアイうた
            作品の感想やお気に入りのシーンなど公式先輩が募集中！詳しくは👇
            https://twitter.com/ainouta_movie/status/1533649254425968640
            """
        ).rstrip()

        content = PlayAllTogetherContent(date(2022, 5, 29))
        actual = content.generate()

        self.assertEqual(actual, expected)
