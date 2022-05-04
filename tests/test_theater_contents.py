from datetime import date
from textwrap import dedent
from unittest import TestCase
from unittest.mock import MagicMock

from lambda_function import CinemaNekoContent, Content, WasedaShochikuContent


class WasedaShochikuContentTestCase(TestCase):
    def test_init(self):
        date_ = MagicMock(spec=date)

        actual = WasedaShochikuContent(date_)

        self.assertIsInstance(actual, Content)
        self.assertEqual(actual._date, date_)

    def test_generate(self):
        expected = dedent(
            """\
            #アイの歌声を聴かせて 早稲田松竹さんで5/7から上映開始！（今日を含めてあと4日）

            たたーん🎵 開映時間は
            - 5/7(土)・10(火)・13(金)が 13:00 / 17:45
            - 5/9(月)・12(木)が 12:25 / 16:35 / 20:45
            - 5/8(日)・11(水)は上映なし

            詳しくは http://wasedashochiku.co.jp/archives/schedule/19087#film2 をどうぞ！
            """
        ).rstrip()

        content = WasedaShochikuContent(date(2022, 5, 3))
        actual = content.generate()

        self.assertEqual(actual, expected)


class CinemaNekoContentTestCase(TestCase):
    def test_init(self):
        date_ = MagicMock(spec=date)

        actual = CinemaNekoContent(date_)

        self.assertIsInstance(actual, Content)
        self.assertEqual(actual._date, date_)

    def test_generate(self):
        expected = dedent(
            """\
            #アイの歌声を聴かせて 青梅のシネマネコさんで4/22(金)から5/15(日)まで上映中！（今日を含めて残り12日）

            たたーん🎵 上映時間は、毎日 15:40〜 （5/10(火)は定休日）
            詳しくは https://cinema-neko.com/movie_detail.php?id=94c58c03-e4b1-484d-8a0f-bc9bb885493c をどうぞ！

            シネマネコさんのラッキープレイスはー、カフェ！☕️
            """
        ).rstrip()

        content = CinemaNekoContent(date(2022, 5, 4))
        actual = content.generate()

        self.assertEqual(actual, expected)
