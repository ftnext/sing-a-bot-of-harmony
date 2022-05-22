from datetime import date
from textwrap import dedent
from unittest import TestCase
from unittest.mock import MagicMock

from harmonizer_bot.contents import Content, Nagoya109CinemasContent


class Nagoya109CinemasContentTestCase(TestCase):
    def test_init(self):
        date_ = MagicMock(spec=date)

        actual = Nagoya109CinemasContent(date_)

        self.assertIsInstance(actual, Content)
        self.assertEqual(actual._date, date_)

    def test_generate(self):
        expected = dedent(
            """\
            #アイの歌声を聴かせて 愛知の109シネマズ名古屋さんの映画祭でライブ音響上映！！

            - 5/28(土) 16:30〜
            - 5/31(火) 16:35〜

            チケットは、2日後の5/13(金) 0時から発売！

            詳しくは https://109cinemas.net/events/liveonkyo_nagoya/ をどうぞ！
            """
        ).rstrip()

        content = Nagoya109CinemasContent(date(2022, 5, 11))
        actual = content.generate()

        self.assertEqual(actual, expected)
