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
            #アイの歌声を聴かせて 期間限定配信🎥は終了。
            で・す・が、6/10(金)のTwitterスペース #みんなでアイうた が楽しめます（1週間程度とのことなので、今日を含めてあと2日くらい）。

            公式先輩、ありがとうございます❤️
            もう一度ラジオを聴かせて！
            https://twitter.com/ainouta_movie/status/1535260028474896384
            """
        ).rstrip()

        content = PlayAllTogetherContent(date(2022, 6, 16))
        actual = content.generate()

        self.assertEqual(actual, expected)
